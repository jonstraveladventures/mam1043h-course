/* logistic-cobweb.js — interactive cobweb diagram for the logistic map.
 *
 * The widget renders the parabola P_n = r * P_{n-1} * (1 - P_{n-1})
 * together with the diagonal P_n = P_{n-1}, then draws a cobweb starting
 * from (P_0, 0) bouncing `iterations` times between them.  Three sliders
 * (r, P_0, iterations) drive a JSXGraph board.
 *
 * Mounted by a div with id="logistic-cobweb-board"; sliders live in
 * adjacent <input type="range"> elements with ids r-slider, p0-slider,
 * iter-slider.  Numeric readouts in spans with ids r-value, p0-value,
 * iter-value.
 */
(function () {
  function init() {
    if (typeof JXG === "undefined") {
      // JSXGraph not loaded yet — try again shortly.
      return setTimeout(init, 50);
    }
    const boardEl = document.getElementById("logistic-cobweb-board");
    if (!boardEl) return;

    const board = JXG.JSXGraph.initBoard("logistic-cobweb-board", {
      boundingbox: [-0.05, 1.05, 1.05, -0.05],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      keepAspectRatio: true,
      defaultAxes: {
        x: {
          name: "P_{n-1}",
          withLabel: true,
          label: { position: "rt", offset: [-25, -10] },
        },
        y: {
          name: "P_n",
          withLabel: true,
          label: { position: "rt", offset: [10, -5] },
        },
      },
    });

    const rEl = document.getElementById("r-slider");
    const p0El = document.getElementById("p0-slider");
    const itEl = document.getElementById("iter-slider");
    const rOut = document.getElementById("r-value");
    const p0Out = document.getElementById("p0-value");
    const itOut = document.getElementById("iter-value");

    // Parabola y = r x (1 - x)
    const parabola = board.create(
      "functiongraph",
      [
        function (x) {
          return parseFloat(rEl.value) * x * (1 - x);
        },
        0,
        1,
      ],
      { strokeColor: "#1f4e9c", strokeWidth: 2, fixed: true }
    );

    // Diagonal y = x
    const diagonal = board.create(
      "functiongraph",
      [function (x) { return x; }, 0, 1],
      { strokeColor: "#c0392b", strokeWidth: 2, dash: 2, fixed: true }
    );

    // Cobweb polyline — built afresh on each update.
    let cobweb = null;
    let initDot = null;

    function update() {
      const r = parseFloat(rEl.value);
      const p0 = parseFloat(p0El.value);
      const its = parseInt(itEl.value, 10);
      rOut.textContent = r.toFixed(2);
      p0Out.textContent = p0.toFixed(2);
      itOut.textContent = its;

      // Recompute cobweb path.  Starting point: (p0, 0).
      const pts = [[p0, 0]];
      let x = p0;
      for (let i = 0; i < its; i++) {
        const y = r * x * (1 - x);
        // vertical to parabola, horizontal to diagonal
        pts.push([x, y]);
        pts.push([y, y]);
        x = y;
      }

      if (cobweb) board.removeObject(cobweb);
      if (initDot) board.removeObject(initDot);

      const xs = pts.map((p) => p[0]);
      const ys = pts.map((p) => p[1]);
      cobweb = board.create("curve", [xs, ys], {
        strokeColor: "#16a085",
        strokeWidth: 1.6,
        fixed: true,
      });
      initDot = board.create("point", [p0, 0], {
        name: "(P_0, 0)",
        size: 3,
        fixed: true,
        color: "#c0392b",
        label: { offset: [10, -10] },
      });

      board.update();
    }

    [rEl, p0El, itEl].forEach((el) => {
      el.addEventListener("input", update);
    });
    update();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
