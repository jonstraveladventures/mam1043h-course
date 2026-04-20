"""
parse_nb.py — Parse a Wolfram .nb file and emit a Hugo-flavoured Markdown page.

Usage:
    python parse_nb.py <input.nb> <output.md> [--images-dir images/partXX]

The script:
  - Extracts text cells → Markdown
  - Converts BoxData math → KaTeX-compatible LaTeX  ($…$ or $$…$$)
  - Hides Input cells entirely
  - Inserts image placeholders for Output / graphics cells
  - Skips blank Text cells
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Allow running from any directory
sys.path.insert(0, str(Path(__file__).parent))
from boxes_to_latex import box_to_latex, replace_wolfram_chars

# ── Tokeniser ────────────────────────────────────────────────────────────────

# Tokens: STRING, IDENT, LBRACKET, RBRACKET, LBRACE, RBRACE, COMMA, OTHER

_TOKEN_RE = re.compile(
    r'"(?:[^"\\]|\\[\s\S])*"'  # quoted string (\\[\s\S] matches \+any char incl. newline)
    r'|[A-Za-z$][A-Za-z0-9$`]*'  # identifier / symbol
    r'|[0-9]+(?:\.[0-9]*)?(?:`[0-9.]*)?(?:\*\^-?[0-9]+)?'  # number
    r'|[,\[\]{}]'           # punctuation
    r'|->|:>'               # rule arrows
    r'|[^\s,\[\]{}]'        # any other single char
)


def tokenise(src: str) -> list[str]:
    return _TOKEN_RE.findall(src)


# ── Parser ───────────────────────────────────────────────────────────────────

class Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self) -> str:
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def expect(self, tok: str):
        t = self.consume()
        if t != tok:
            raise ValueError(f"Expected {tok!r}, got {t!r} at pos {self.pos}")

    def parse_expr(self):
        """Parse one Mathematica expression."""
        tok = self.peek()
        if tok is None:
            return None

        # String literal
        if tok.startswith('"'):
            self.consume()
            return unescape_mma_string(tok[1:-1])

        # Number
        if tok and (tok[0].isdigit() or (tok[0] == '-' and len(tok) > 1)):
            self.consume()
            return tok

        # Identifier — could be a function call Head[...]
        if tok and (tok[0].isalpha() or tok[0] == '$'):
            self.consume()
            head = tok
            if self.peek() == '[':
                self.expect('[')
                args = []
                while self.peek() not in (']', None):
                    args.append(self.parse_expr())
                    if self.peek() == ',':
                        self.consume()
                self.expect(']')
                return [head] + args
            return head

        # List {a, b, c}
        if tok == '{':
            self.consume()
            items = []
            while self.peek() not in ('}', None):
                items.append(self.parse_expr())
                if self.peek() == ',':
                    self.consume()
            if self.peek() == '}':
                self.consume()
            return items

        # Rule  a -> b  or  a :> b
        # (already consumed lhs at this point — handled inline)

        # Skip unknown tokens
        self.consume()
        return tok

    def parse_top(self):
        """Parse all top-level expressions from the token stream."""
        results = []
        while self.pos < len(self.tokens):
            e = self.parse_expr()
            if e is not None:
                results.append(e)
        return results


def unescape_mma_string(s: str) -> str:
    """Unescape Mathematica string internals and clean up line continuations."""
    # Wolfram continuation: backslash-newline inside strings → single space
    s = re.sub(r'\\\n\s*', ' ', s)
    # \< … \> is Mathematica's raw string indicator — strip them
    s = re.sub(r'\\[<>]', '', s)
    # Standard Mathematica string escapes
    s = s.replace('\\"', '"')
    s = s.replace('\\n', '\n')   # newline
    s = s.replace('\\t', '    ') # tab → 4 spaces for prose
    s = s.replace('\\\\', '\\')
    return s


_INLINE_MATH_RE = re.compile(r'\$([^$\n]*)\$')
_ALLOWED_CHARS_RE = re.compile(r"^[A-Za-z0-9\s\-,.:;!?()/']*$")


def _unwrap_text_only_math(match: "re.Match[str]") -> str:
    inner = match.group(1)
    # Only unwrap if at least one \text{} is present AND the non-\text residue
    # is plain prose (letters, digits, spaces, simple punctuation).
    if r'\text{' not in inner:
        return match.group(0)
    residue = re.sub(r'\\text\{[^{}]*\}', '', inner)
    if not _ALLOWED_CHARS_RE.match(residue):
        return match.group(0)
    unwrapped = re.sub(r'\\text\{\s*([^{}]*?)\s*\}', r'\1', inner)
    return re.sub(r'\s+', ' ', unwrapped).strip()


_LIST_MARKER_RE = re.compile(r'^(\s*)([-*+]|\d+[.)])\s')


def _unindent_orphan_lists(s: str) -> str:
    """Strip leading whitespace from list-item lines that don't sit under
    a parent list item. This prevents Markdown from treating
    Mathematica-pretty-printed lists (indented by \\t) as code blocks.

    An "orphan" block is a contiguous run of indented list-item lines
    where the preceding non-blank line is not itself a list item. For
    each such block we subtract the minimum indent from every line in
    the block so relative nesting within the block is preserved.
    """
    lines = s.split('\n')
    out: list[str] = []
    i = 0
    n = len(lines)

    def list_match(ln: str):
        return _LIST_MARKER_RE.match(ln)

    while i < n:
        ln = lines[i]
        m = list_match(ln)
        if m and m.group(1):  # list item with leading whitespace
            # Check prior non-blank line context.
            prev_nonblank = None
            for j in range(len(out) - 1, -1, -1):
                if out[j].strip():
                    prev_nonblank = out[j]
                    break
            prev_is_list = prev_nonblank is not None and list_match(prev_nonblank) is not None
            if not prev_is_list:
                # Collect the orphan block — consecutive list lines &
                # blank lines between them.
                block_start = i
                block_indents: list[int] = []
                j = i
                while j < n:
                    mj = list_match(lines[j])
                    if mj:
                        block_indents.append(len(mj.group(1)))
                        j += 1
                        continue
                    if not lines[j].strip():
                        # Peek: is the next non-blank line also an indented list?
                        k = j + 1
                        while k < n and not lines[k].strip():
                            k += 1
                        if k < n and list_match(lines[k]):
                            j = k
                            continue
                    break
                if block_indents:
                    min_indent = min(block_indents)
                    for k in range(block_start, j):
                        line = lines[k]
                        if list_match(line) and line[:min_indent].strip() == '':
                            out.append(line[min_indent:])
                        else:
                            out.append(line)
                    i = j
                    continue
        out.append(ln)
        i += 1
    return '\n'.join(out)


def _unindent_orphan_prose(s: str) -> str:
    """Strip 4+ leading spaces on prose lines that aren't continuations
    of a Markdown list. Otherwise they render as an indented code block."""
    lines = s.split('\n')
    out: list[str] = []
    for ln in lines:
        if _LIST_MARKER_RE.match(ln):
            out.append(ln)
            continue
        # Prose line with 4+ leading spaces?
        m = re.match(r'^( {4,})(\S.*)$', ln)
        if not m:
            out.append(ln)
            continue
        # Look back for context.
        prev_nonblank = None
        for j in range(len(out) - 1, -1, -1):
            if out[j].strip():
                prev_nonblank = out[j]
                break
        prev_is_list = prev_nonblank is not None and _LIST_MARKER_RE.match(prev_nonblank)
        if prev_is_list:
            # Keep indent — genuine list continuation.
            out.append(ln)
        else:
            out.append(m.group(2))
    return '\n'.join(out)


def clean_text_whitespace(s: str) -> str:
    """Collapse runs of whitespace in plain prose (not math)."""
    # Preserve leading whitespace on each line (for list-item continuation
    # and sub-item indent). Collapse runs of spaces/tabs only in the interior
    # of lines.
    def _collapse_interior_ws(line: str) -> str:
        m = re.match(r'^([ \t]*)(.*)$', line)
        lead, rest = m.group(1), m.group(2)
        return lead + re.sub(r'[ \t]+', ' ', rest)
    s = '\n'.join(_collapse_interior_ws(ln) for ln in s.split('\n'))
    s = re.sub(r'\n{3,}', '\n\n', s)
    # Unwrap $...$ blocks that only contain \text{} fragments (plus prose)
    s = _INLINE_MATH_RE.sub(_unwrap_text_only_math, s)
    # Strip leaked Mathematica metadata
    s = re.sub(r'\\?InputExpressionUUID->[\w-]+', '', s)
    s = re.sub(r'\\?ExpressionUUID->[\w-]+', '', s)
    # Remove orphaned brace lines
    s = re.sub(r'(?m)^\s*[{}]\s*$', '', s)
    # Convert N) enumeration at line start to Markdown "1." so Markdown
    # auto-numbers (handles author typos like "1), 2), 2)" in the source).
    s = re.sub(r'(?m)^\d+\)\s+', '1. ', s)
    # Convert a), b), c) sub-enumeration to indented sub-items (preserve letter)
    s = re.sub(r'(?m)^([a-z])\)\s+', r'    - \1) ', s)
    # Also handle indented sub-items: "   a) text" → "    - a) text"
    s = re.sub(r'(?m)^ {2,}([a-z])\)\s+', r'    - \1) ', s)
    # Convert top-level bullet chars: "• item" or "∘ item" → "- item"
    s = re.sub(r'(?m)^[•∘]\s*', '- ', s)
    # Convert indented sub-bullet chars (1+ leading spaces + ∘/◦) to sub-item
    s = re.sub(r'(?m)^ +[∘◦]\s*', '    - ', s)
    s = re.sub(r'(?m)^ +•\s*', '    - ', s)

    # Un-indent "orphan" list-item blocks that aren't nested under a real
    # parent list. Mathematica authors often use \t to pretty-print lists
    # inside plain Text cells; after \t → 4-space conversion these would
    # render as Markdown code blocks. We look at each indented list-item
    # line and strip its leading whitespace unless the previous non-blank
    # line is itself a list item (genuine nesting).
    s = _unindent_orphan_lists(s)
    # Same for orphan indented prose (e.g. tab-pretty-printed ToC lines):
    # a 4+ space indent on a prose line whose previous non-blank line is
    # not a list item would render as a Markdown code block. Strip it.
    s = _unindent_orphan_prose(s)
    # Drop trailing-whitespace-only lines (e.g. "    \n") left after
    # un-indenting — they'd otherwise linger as visible blank indented lines.
    s = re.sub(r'(?m)^[ \t]+$', '', s)
    return s.strip()


# ── Notebook cell extraction ─────────────────────────────────────────────────

def is_graphics_output(cell_content) -> bool:
    """True if the cell content is a graphics object (not displayable as text)."""
    if isinstance(cell_content, list):
        head = cell_content[0] if cell_content else ""
        if head in ("GraphicsBox", "Graphics3DBox", "RasterBox",
                    "DynamicBox", "DynamicModuleBox",
                    "TagBox",    # often wraps graphics
                    "LocatorPaneBox", "PanelBox"):
            return True
        # TagBox wrapping graphics
        if head == "TagBox" and len(cell_content) > 1:
            return is_graphics_output(cell_content[1])
    return False


def boxdata_to_latex(bd) -> str:
    """Convert a BoxData node to LaTeX string."""
    if isinstance(bd, list) and bd and bd[0] == "BoxData":
        inner = bd[1] if len(bd) > 1 else bd
    else:
        inner = bd
    return box_to_latex(inner)


# ── Text content extraction ──────────────────────────────────────────────────

def textdata_to_md(items) -> str:
    """Convert a TextData list to Markdown text (with inline math)."""
    parts = []
    if not isinstance(items, list):
        return replace_wolfram_chars(str(items))

    for item in items:
        if isinstance(item, str):
            parts.append(replace_wolfram_chars(item))
        elif isinstance(item, list):
            head = item[0] if item else ""
            if head == "Cell":
                # Inline Cell — usually BoxData math
                parts.append(inline_cell_to_md(item))
            elif head == "StyleBox":
                inner_text = textdata_to_md(item[1:2])
                # Check for font options
                opts = item[2:] if len(item) > 2 else []
                bold = any(
                    (isinstance(o, list) and o == ["Rule", "FontWeight", "Bold"])
                    or o == "Bold"
                    for o in opts
                )
                italic = any(
                    (isinstance(o, list) and o == ["Rule", "FontSlant", "Italic"])
                    or o == "Italic"
                    for o in opts
                )
                if bold:
                    inner_text = f"**{inner_text.strip()}**"
                elif italic:
                    inner_text = f"*{inner_text.strip()}*"
                parts.append(inner_text)
            elif head == "ButtonBox":
                parts.append(textdata_to_md(item[1:2]))
            else:
                # Unknown — try to extract string content recursively
                parts.append(textdata_to_md(item[1:]))
        else:
            parts.append(str(item))

    return "".join(parts)


def inline_cell_to_md(cell_node: list) -> str:
    """Convert an inline Cell[BoxData[...], ...] to $...$."""
    # cell_node = ["Cell", content, cell_type, ...]
    if len(cell_node) < 2:
        return ""
    content = cell_node[1]
    if isinstance(content, list) and content and content[0] == "BoxData":
        latex = boxdata_to_latex(content)
        if not latex.strip():
            return ""
        return f"${latex}$"
    return ""


def plain_string_to_md(s: str) -> str:
    """Convert a plain Mathematica string cell content to Markdown."""
    return replace_wolfram_chars(s)


# ── Main cell dispatcher ─────────────────────────────────────────────────────

def cell_to_md(cell: list, image_counter: list[int], images_dir: str,
               show_input: bool = False) -> str | None:
    """
    Convert a parsed Cell[...] node to a Markdown string.
    Returns None if the cell should be skipped.

    cell = ["Cell", content, cell_type, ...options...]
    """
    if not isinstance(cell, list) or cell[0] != "Cell" or len(cell) < 2:
        return None

    content   = cell[1]
    cell_type = cell[2] if len(cell) > 2 else ""

    # ── Input cells ─────────────────────────────────────────────────────────
    if cell_type in ("Input", "Code"):
        if not show_input:
            return None
        # Extract code as readable Mathematica syntax
        from boxes_to_latex import box_to_code
        if isinstance(content, list) and content and content[0] == "BoxData":
            code = box_to_code(content[1] if len(content) > 1 else content)
        else:
            code = extract_text(content)
        code = code.strip()
        if not code:
            return None
        return f"```mathematica\n{code}\n```"

    if cell_type in ("Print", "Message"):
        return None
    # Skip button/hyperlink cells (navigation widgets at notebook bottom)
    if isinstance(content, list) and content and content[0] in ("ButtonBox", "TemplateBox"):
        return None

    # ── CellGroupData — handled by walk_cells, skip here ───────────────────
    if isinstance(content, list) and content and content[0] == "CellGroupData":
        return None

    # ── Output cells with graphics ──────────────────────────────────────────
    if cell_type == "Output":
        inner = content
        if isinstance(inner, list) and inner and inner[0] == "BoxData":
            inner = inner[1] if len(inner) > 1 else inner
        if is_graphics_output(inner):
            image_counter[0] += 1
            n = image_counter[0]
            img_path = f"{images_dir}/output_{n:03d}.png"
            return f'![Figure {n}]({img_path})'
        # Non-graphics output (e.g. a computed number)
        if show_input:
            from boxes_to_latex import box_to_code
            code = box_to_code(content[1] if isinstance(content, list) and content and content[0] == "BoxData" and len(content) > 1 else content)
            code = code.strip()
            if code:
                return f"```\n(* Out: *) {code}\n```"
        return None

    # ── Headings ────────────────────────────────────────────────────────────
    if cell_type == "Title":
        # Skip — the Hugo page header already shows the title.
        # The Title cell is the generic "MAM2046W - Second year nonlinear dynamics"
        # which is redundant on every page.
        return None

    if cell_type == "Section":
        text = clean_text_whitespace(extract_text(content))
        # Skip author/contact info sections
        # Filter author/contact sections (text may have \text{} artifacts)
        if text and ("@" in text and "Cape Town" in text):
            return None
        return f"## {text}" if text else None

    if cell_type == "Subsection":
        text = clean_text_whitespace(extract_text(content))
        return f"### {text}" if text else None

    if cell_type == "Subsubsection":
        text = clean_text_whitespace(extract_text(content))
        return f"#### {text}" if text else None

    # ── Display math ────────────────────────────────────────────────────────
    if cell_type in ("DisplayFormula", "DisplayFormulaNumbered",
                     "Equation", "EquationNumbered"):
        latex = extract_display_math(content)
        if latex and latex.strip():
            return f"$$\n{latex.strip()}\n$$"
        return None

    # ── List items ──────────────────────────────────────────────────────────
    if cell_type in ("Item", "ItemParagraph", "Item1", "Item1Exercise"):
        text = clean_text_whitespace(extract_text(content)).strip()
        return f"- {text}" if text else None

    if cell_type in ("Subitem", "Subitem1", "Item2", "Item2Exercise"):
        text = clean_text_whitespace(extract_text(content)).strip()
        return f"    - {text}" if text else None

    if cell_type in ("Subsubitem", "Subsubitem1", "Item3"):
        text = clean_text_whitespace(extract_text(content)).strip()
        return f"        - {text}" if text else None

    if cell_type in ("ItemNumbered",):
        text = clean_text_whitespace(extract_text(content)).strip()
        return f"1. {text}" if text else None

    # ── Text cells ──────────────────────────────────────────────────────────
    if cell_type in ("Text", "Subsubsubsection", ""):
        # Skip navigation-button-only cells (TextData[ButtonBox[...]])
        if (isinstance(content, list) and content and content[0] == "TextData"
                and len(content) > 1
                and isinstance(content[1], list) and content[1]
                and content[1][0] == "ButtonBox"):
            return None
        text = clean_text_whitespace(extract_text(content))
        if not text:
            return None  # skip blank text cells
        return text

    # ── Inline math inside Text as BoxData ──────────────────────────────────
    if cell_type in ("InlineFormula",):
        latex = extract_display_math(content)
        return f"${latex}$" if latex and latex.strip() else None

    # ── Anything else — skip ────────────────────────────────────────────────
    return None


def extract_text(content) -> str:
    """Extract human-readable text from a cell's content node."""
    if isinstance(content, str):
        return plain_string_to_md(content)

    if isinstance(content, list):
        head = content[0] if content else ""

        if head == "TextData":
            inner = content[1] if len(content) > 1 else []
            if isinstance(inner, list) and inner:
                first = inner[0]
                # If the first element is a Wolfram head (uppercase, no spaces),
                # then `inner` is a single expression like StyleBox[...], not a list of items.
                if isinstance(first, str) and first[:1].isupper() and " " not in first:
                    return extract_text(inner)
                return textdata_to_md(inner)
            return replace_wolfram_chars(str(inner))

        if head == "StyleBox":
            return extract_text(content[1]) if len(content) > 1 else ""

        if head == "BoxData":
            return boxdata_to_latex(content)

        if head == "FormBox":
            return box_to_latex(content)

        if head == "Cell":
            # Inline Cell[content, options...] — only process the content,
            # skip options like CellChangeTimes, FontSize, ExpressionUUID.
            # Wrap as inline math if content is BoxData.
            if len(content) < 2:
                return ""
            inner = content[1]
            if isinstance(inner, list) and inner and inner[0] == "BoxData":
                latex = boxdata_to_latex(inner)
                return f"${latex}$" if latex.strip() else ""
            return extract_text(inner)

        if head == "ButtonBox":
            # ButtonBox[label, options...] — only use label
            return extract_text(content[1]) if len(content) > 1 else ""

        # Fallback — join string children, but stop at option-looking tokens
        # (Mathematica "Rule" args, or bare "Symbol->value" sequences that
        # leak cell metadata like CellChangeTimes, FontSize, ExpressionUUID).
        _OPT_NAMES = {
            "CellChangeTimes", "ExpressionUUID", "FontSize", "FontColor",
            "FontWeight", "FontSlant", "FontVariations", "BaseStyle",
            "ButtonData", "ButtonNote", "ImageSize", "PlotRange",
            "CellTags", "CellLabel", "CellDingbat",
        }
        parts = []
        i = 1
        while i < len(content):
            c = content[i]
            if isinstance(c, list) and c and c[0] in ("Rule", "RuleDelayed"):
                i += 1
                continue
            if isinstance(c, str) and c in _OPT_NAMES:
                # Skip "Name -> value" triple (or until next non-option token)
                break
            parts.append(extract_text(c))
            i += 1
        return "".join(parts)

    return ""


def extract_display_math(content) -> str:
    """Extract LaTeX from a display-math cell."""
    if isinstance(content, list):
        head = content[0] if content else ""
        if head == "BoxData":
            return boxdata_to_latex(content)
        if head == "FormBox":
            return box_to_latex(content)
        if head == "RowBox":
            return box_to_latex(content)
        # Try first child
        if len(content) > 1:
            return extract_display_math(content[1])
    return ""


# ── Top-level notebook walker ────────────────────────────────────────────────

def walk_cells(cell_list: list, blocks: list, image_counter: list,
               images_dir: str, show_input: bool = False):
    """Recursively walk a list of Cell nodes, appending Markdown blocks."""
    for node in cell_list:
        if not isinstance(node, list) or not node:
            continue
        if node[0] != "Cell":
            continue

        content  = node[1] if len(node) > 1 else None
        cell_type = node[2] if len(node) > 2 else ""

        # CellGroupData — recurse into children
        if isinstance(content, list) and content and content[0] == "CellGroupData":
            inner = content[1]
            if isinstance(inner, list):
                walk_cells(inner, blocks, image_counter, images_dir, show_input)
            continue

        # Leaf cell — convert to Markdown
        md = cell_to_md(node, image_counter, images_dir, show_input=show_input)
        if md and md.strip():
            blocks.append(md)


def walk_notebook(nb: list, images_dir: str, show_input: bool = False) -> list[str]:
    """Walk a parsed Notebook[{...}] expression and return Markdown blocks."""
    if not isinstance(nb, list) or nb[0] != "Notebook":
        raise ValueError("Not a Notebook expression")

    cells_list = nb[1]  # The list of cells ({...} first arg)
    if not isinstance(cells_list, list):
        return []

    blocks: list[str] = []
    image_counter = [0]
    walk_cells(cells_list, blocks, image_counter, images_dir, show_input)
    return blocks


# ── File reading with line-continuation handling ─────────────────────────────

def read_nb_source(path: Path) -> str:
    """Read a .nb file, stripping the header comment block."""
    src = path.read_text(encoding="utf-8", errors="replace")
    # Strip the (* ... *) header
    src = re.sub(r'^\(\*.*?\*\)\n', '', src, flags=re.DOTALL)
    # Remove (* Content-type ... *) lines
    src = re.sub(r'\(\*[^*]*\*\)', '', src)
    # Normalise Wolfram's \r\n
    src = src.replace('\r\n', '\n').replace('\r', '\n')
    return src


# ── Frontmatter generation ────────────────────────────────────────────────────

def make_frontmatter(title: str, weight: int) -> str:
    safe_title = title.replace('"', '\\"')
    return f"""---
title: "{safe_title}"
weight: {weight}
math: true
---
"""


# ── CLI entry point ───────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Convert a .nb file to Hugo Markdown.")
    ap.add_argument("input",  type=Path, help="Input .nb file")
    ap.add_argument("output", type=Path, help="Output .md file")
    ap.add_argument("--images-dir", default="", help="Relative image path prefix for this page")
    ap.add_argument("--weight", type=int, default=10, help="Hugo page weight (ordering)")
    ap.add_argument("--title", default=None, help="Override extracted title")
    ap.add_argument("--show-input", action="store_true",
                    help="Include Input cells as Mathematica code blocks")
    args = ap.parse_args()

    print(f"Parsing {args.input} …", file=sys.stderr)
    src = read_nb_source(args.input)
    tokens = tokenise(src)
    print(f"  {len(tokens)} tokens", file=sys.stderr)

    parser = Parser(tokens)
    exprs = parser.parse_top()

    # Find the Notebook[...] expression
    nb = next((e for e in exprs if isinstance(e, list) and e and e[0] == "Notebook"), None)
    if nb is None:
        print("ERROR: No Notebook expression found", file=sys.stderr)
        sys.exit(1)

    images_dir = args.images_dir or f"images/{args.input.stem}"
    blocks = walk_notebook(nb, images_dir, show_input=args.show_input)

    # Extract title: prefer the first ## Section heading (specific to this page)
    # over the generic # MAM2046W course title that appears in every notebook
    title = "Untitled"
    h1_title = None
    for b in blocks:
        if b.startswith("## ") and title == "Untitled":
            title = b[3:].split("\n")[0].strip()
        elif b.startswith("# ") and h1_title is None:
            h1_title = b[2:].split("\n")[0].strip()
    # Fall back to # heading if no ## found (e.g. part0 intro)
    if title == "Untitled" and h1_title:
        title = h1_title
    if args.title:
        title = args.title

    md = make_frontmatter(title, args.weight)
    md += "\n\n".join(blocks)

    # Final scrub: drop orphan `$$` lines (not part of a proper open/close pair).
    # A proper pair is: `$$` on its own line, some non-`$$` content, `$$` on its own line.
    lines = md.split("\n")
    # indices of lines whose trimmed content is exactly `$$`
    dd_idx = [i for i, l in enumerate(lines) if l.strip() == "$$"]
    kept = set()
    i = 0
    while i < len(dd_idx) - 1:
        a, b = dd_idx[i], dd_idx[i + 1]
        # Body between them must not be empty — empty means orphan pair
        body_lines = lines[a + 1:b]
        if any(ln.strip() for ln in body_lines):
            kept.add(a)
            kept.add(b)
            i += 2
        else:
            # empty block — drop both
            i += 2
    # Any remaining unpaired (odd-count tail) is dropped
    remove = set(dd_idx) - kept
    md = "\n".join(l for idx, l in enumerate(lines) if idx not in remove)
    md = re.sub(r'\n{3,}', '\n\n', md)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(md, encoding="utf-8")
    print(f"  Written {args.output}  ({len(blocks)} blocks)", file=sys.stderr)


if __name__ == "__main__":
    main()
