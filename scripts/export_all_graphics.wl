(* export_all_graphics.wl — Export Output cell graphics from a .nb file as PNGs.
   Uses UsingFrontEnd + Rasterize for reliable rendering.

   Usage: wolframscript -file export_all_graphics.wl <input.nb> <output-dir>
*)

args = $ScriptCommandLine;

If[Length[args] < 3,
  Print["Usage: wolframscript -file export_all_graphics.wl <input.nb> <output-dir>"];
  Exit[1]
];

nbFile = args[[2]];
outDir = args[[3]];

Print["Exporting: ", nbFile];
Print["Output:    ", outDir];

UsingFrontEnd[
  (* Open notebook invisibly *)
  nb = NotebookOpen[nbFile, Visible -> False];
  If[nb === $Failed,
    Print["ERROR: Could not open notebook"];
    Exit[1]
  ];

  (* Ensure output directory exists *)
  If[!DirectoryQ[outDir], CreateDirectory[outDir]];

  (* Find all Output cells *)
  cells = Cells[nb, CellStyle -> "Output"];
  Print["Found ", Length[cells], " Output cell(s)"];

  (* Export only Output cells that contain graphics *)
  count = 0;
  skipped = 0;
  Do[
    Module[{cellExpr, img, fname, hasGraphics},
      cellExpr = NotebookRead[cells[[i]]];

      (* Skip empty or non-Cell outputs *)
      If[cellExpr === {} || cellExpr === "" || Head[cellExpr] =!= Cell,
        skipped++;
        Continue[]
      ];

      (* Stricter filter: a real graphics output has a Graphics{,3D}Box at
         the *top* of its BoxData (possibly wrapped in TagBox/StyleBox/FormBox
         or a Manipulate's DynamicModuleBox).  An expression like
         {InterpolatingFunction[...][t], …} also contains GraphicsBox deep
         inside (the IF icon), but its top is a RowBox — we want to skip
         those, which the previous !FreeQ-based filter rasterised as garbage. *)
      hasGraphics = Module[{inner = cellExpr},
        While[
          MatchQ[inner, _Cell] && Length[inner] >= 1, inner = inner[[1]]];
        While[
          MatchQ[inner, _BoxData | _TagBox | _StyleBox | _FormBox] &&
            Length[inner] >= 1, inner = inner[[1]]];
        MatchQ[inner,
          _GraphicsBox | _Graphics3DBox | _RasterBox | _DynamicModuleBox]
      ];

      If[!hasGraphics,
        skipped++;
        Print["  skip[", i, "] non-graphics output"];
        Continue[]
      ];

      count++;
      fname = FileNameJoin[{outDir,
        "output_" <> IntegerString[count, 10, 3] <> ".png"}];

      img = Rasterize[cellExpr, ImageResolution -> 150];
      Export[fname, img];
      Print["  [", count, "] ", fname,
        "  (", ImageDimensions[img][[1]], "x", ImageDimensions[img][[2]], ")"];
    ],
    {i, Length[cells]}
  ];

  Print["Skipped ", skipped, " non-graphics output(s)"];

  NotebookClose[nb];
];

Print["Done: ", count, " image(s) exported to ", outDir];
