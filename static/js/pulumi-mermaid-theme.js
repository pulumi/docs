/**
 * Pulumi-brand Mermaid theme — portable and dependency-free.
 *
 * Drop into any Mermaid v11 setup (docs site, slide deck, app, notebook):
 *
 *   import { pulumiMermaidLight, pulumiMermaidDark } from "./pulumi-mermaid-theme.js";
 *   import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
 *   mermaid.initialize({ startOnLoad: true, ...pulumiMermaidLight });
 *
 * For dark mode, initialize (or re-initialize and re-run) with pulumiMermaidDark.
 * Every color is a Pulumi brand token (theme/src/scss/_theme.scss). The objects
 * are plain Mermaid config, so they also work verbatim in a ```mermaid``` block's
 * `--- config ---` front matter.
 *
 * Both modes share one structure; only the MODES palette below differs. The
 * guiding rule: fills are light (dark text) in light mode and dark/saturated
 * (light text) in dark mode — matching the flowchart node treatment — while
 * lines/branches invert so they stay visible against the page background.
 */

const INTER = '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';

// Build `prefix0..N` (or `prefix1..N`) themeVariable maps from a palette.
const series = (prefix, start, palette) =>
    Object.fromEntries(palette.map((color, i) => [`${prefix}${i + start}`, color]));

const MODES = {
    light: {
        bg: '#ffffff',          // white (page background)
        surface: '#f5f5ff',     // violet-50  (node/actor fill)
        surface2: '#ebebff',    // violet-100 (secondary / activation)
        fg: '#1f1b21',          // service-black (text on light fills)
        border: '#9077f3',      // violet-500 (node/actor border)
        softBorder: '#c3bdff',  // violet-300 (cluster/note/label borders, lifelines)
        line: '#6a6675',        // gray-700 (edges, signals)
        title: '#5a30c5',       // violet-700
        // Multi-series. fill = data cells with text; branch = git lines; cScale =
        // sequential fills (kanban/timeline/mindmap).
        fill: ['#c3bdff', '#9077f3', '#7952e5', '#a697fc', '#5a30c5', '#dedbff', '#492e8e', '#ebebff'],
        cScale: ['#ebebff', '#dedbff', '#c3bdff', '#a697fc', '#9077f3', '#7952e5', '#5a30c5', '#492e8e'],
        branch: ['#5a30c5', '#9077f3', '#7952e5', '#a697fc', '#492e8e', '#c3bdff', '#392960', '#dedbff'],
        // Chart accents
        chartLine: '#5a30c5',   // xychart line, radar stroke (dark violet on white)
        bars: ['#c3bdff', '#9077f3', '#7952e5'],
        radarFill: '#9077f3',
        leaf: '#c3bdff',        // treemap leaf
        seriesText: '#1f1b21',  // text on pie/data fills
        grid: '#e0dfe2',        // radar graticule (gray-200)
        // Kanban column fills, set directly (Mermaid heavily lightens cScale).
        kanban: ['#f5f5ff', '#ebebff', '#dedbff', '#c3bdff'], // violet 50/100/200/300
    },
    dark: {
        bg: '#1f1b21',          // service-black (page background)
        surface: '#231f33',     // violet-950 (node/actor fill)
        surface2: '#392960',    // violet-900 (secondary / activation)
        fg: '#efeff0',          // gray-100 (text on dark fills)
        border: '#9077f3',      // violet-500
        softBorder: '#492e8e',  // violet-800
        line: '#9997a0',        // gray-500
        title: '#c3bdff',       // violet-300
        // Dark fills are medium-dark violets so light text reads on all of them.
        fill: ['#7952e5', '#5a30c5', '#9077f3', '#492e8e', '#a697fc', '#392960', '#c3bdff', '#dedbff'],
        cScale: ['#392960', '#492e8e', '#5a30c5', '#7952e5', '#9077f3', '#a697fc', '#c3bdff', '#dedbff'],
        branch: ['#c3bdff', '#a697fc', '#dedbff', '#9077f3', '#ebebff', '#7952e5', '#f5f5ff', '#5a30c5'],
        chartLine: '#c3bdff',   // light violet on dark
        bars: ['#7952e5', '#9077f3', '#c3bdff'],
        radarFill: '#9077f3',
        leaf: '#5a30c5',
        seriesText: '#efeff0',
        grid: '#392960',        // radar graticule (violet-900, subtle on dark)
        kanban: ['#392960', '#492e8e', '#5a30c5', '#7952e5'], // dark → lighter violets
    },
};

const themeCSS = m => `
    /* Inter + brand ligature/stylistic-set features on all diagram text. */
    text, tspan, p, span, foreignObject div { font-feature-settings: "liga" 1, "calt" 1, "cv11" 1; }
    /* Some diagrams (e.g. journey) hardcode Trebuchet via an inline attribute,
       overriding the fontFamily themeVariable — force Inter and a themed fill. */
    text[font-family*="trebuchet"] { font-family: ${INTER}; fill: ${m.fg}; }

    .node rect, .node polygon { rx: 6px; ry: 6px; }
    .node rect, .node circle, .node polygon, .node path { stroke-width: 1.5px; }
    .flowchart-link { stroke-width: 1.5px; }
    .cluster rect { rx: 10px; ry: 10px; stroke-dasharray: 4 4; stroke-width: 1.5px; }
    .cluster-label foreignObject { transform: translateY(0.2em); }
    .cluster-label p { font-weight: 600; }
    .edgeLabel p { background-color: transparent; }
    .labelBkg { background-color: ${m.bg}; }
    .actor { stroke-width: 1.5px; }
    text.sequenceNumber { fill: ${m.bg}; }

    /* Git branch labels: the pill defaults to the branch (git) color, which
       spans the full violet range, so the body-colored label text collides on
       same-polarity pills (every label in dark mode; the dark branches in
       light). Knock the pill out to the page background — the text then reads
       at full contrast and the colored branch line still identifies it. */
    .branchLabelBkg { fill: ${m.bg}; }

    /* Mindmap root: keep the saturated title-violet fill for emphasis, but its
       label text defaults to the body color (same polarity → low contrast), so
       punch the text out in the page background (white on the dark-violet root
       in light mode, service-black on the light-violet root in dark). */
    .section-root text, .section-root span { fill: ${m.bg}; color: ${m.bg}; }

    /* Diagram titles + treemap labels: semibold, tracked in (incl. classless
       Trebuchet titles). */
    .pieTitleText, .titleText, text.flowchartTitleText, .chart-title text, .title text,
    .treemapLabel, text[font-family*="trebuchet"][font-weight="bold"] { font-weight: 600; letter-spacing: -0.02em; }

    /* User-journey sections + task boxes: same fill + outline as flowchart nodes. */
    .task, .journey-section { fill: ${m.surface}; stroke: ${m.border}; stroke-width: 1.5px; }
    /* User-journey actor dots: brand-palette accents (defaults are off-brand greens). */
    .actor-0 { fill: #9077f3; } /* violet-500 */
    .actor-1 { fill: #21c45d; } /* green-500  */
    .actor-2 { fill: #5296ff; } /* blue-500   */
    .actor-3 { fill: #f49709; } /* yellow-500 */
    .actor-4 { fill: #f96c0b; } /* orange-500 */
    .actor-5 { fill: #fb2c36; } /* red-500    */

    /* Timeline section connector lines default to off-brand green. */
    [class*="node-line"] { stroke: ${m.softBorder} !important; }

    /* xychart bars/lines (default palette is cream) → mode-aware violets. */
    .bar-plot-0 rect { fill: ${m.bars[0]}; }
    .bar-plot-1 rect { fill: ${m.bars[1]}; }
    .bar-plot-2 rect { fill: ${m.bars[2]}; }
    .line-plot-0 path, .line-plot-1 path, .line-plot-2 path { stroke: ${m.chartLine}; }

    /* Radar curves pull from cScale — set saturated violets (fill ~0.5 opacity). */
    .radarCurve-0 { fill: ${m.radarFill}; stroke: ${m.chartLine}; }
    .radarCurve-1 { fill: ${m.bars[0]}; stroke: ${m.title}; }
    .radarCurve-2 { fill: ${m.bars[2]}; stroke: ${m.softBorder}; }

    /* Radar grid rings default to light gray (harsh on dark) → subtle outlines. */
    .radarGraticule { stroke: ${m.grid}; fill: none; }

    /* Treemap leaves pull from cScale (too light to read) → standout violet. */
    .treemapLeaf { fill: ${m.leaf}; }

    /* ER attribute rows: the renderer lightens primaryColor for odd rows, which
       goes light (invisible text) in dark mode. Set both mode-aware. */
    .row-rect-odd path { fill: ${m.surface2}; }
    .row-rect-even path { fill: ${m.surface}; }

    /* Kanban columns (.section-N is kanban-specific): set fills directly because
       Mermaid heavily lightens cScale, and drop the flowchart dashed border. */
    .section-1 rect, .section-2 rect, .section-3 rect, .section-4 rect { stroke-dasharray: none; }
    .section-1 rect { fill: ${m.kanban[0]}; }
    .section-2 rect { fill: ${m.kanban[1]}; }
    .section-3 rect { fill: ${m.kanban[2]}; }
    .section-4 rect { fill: ${m.kanban[3]}; }

    /* Packet: field blocks default to gray; style like nodes with themed text. */
    .packetBlock { fill: ${m.surface}; stroke: ${m.border}; stroke-width: 1px; }
    .packetByte, .packetLabel, .packetTitle { fill: ${m.fg}; }
`;

const build = m => ({
    theme: 'base',
    flowchart: { padding: 14 },
    themeVariables: {
        fontFamily: INTER,
        fontSize: '14px',
        background: m.bg,
        primaryColor: m.surface,
        mainBkg: m.surface,
        primaryBorderColor: m.border,
        nodeBorder: m.border,
        primaryTextColor: m.fg,
        lineColor: m.line,
        secondaryColor: m.surface2,
        tertiaryColor: m.surface,
        titleColor: m.title,
        edgeLabelBackground: m.bg,
        clusterBkg: m.bg,
        clusterBorder: m.softBorder,
        actorBkg: m.surface,
        actorBorder: m.border,
        actorTextColor: m.fg,
        actorLineColor: m.softBorder,
        signalColor: m.line,
        signalTextColor: m.fg,
        labelBoxBkgColor: m.surface,
        labelBoxBorderColor: m.softBorder,
        labelTextColor: m.fg,
        loopTextColor: m.title,
        noteBkgColor: m.surface,
        noteBorderColor: m.softBorder,
        noteTextColor: m.fg,
        activationBkgColor: m.surface2,
        activationBorderColor: m.border,
        // Pie: thin slice separators matching the page; text on light/dark fills.
        pieStrokeColor: m.bg,
        pieStrokeWidth: '1px',
        pieOuterStrokeWidth: '0px',
        pieSectionTextColor: m.seriesText,
        // Multi-series palettes (pie/fillType cells, git branches, sequential cScale).
        ...series('pie', 1, m.fill),
        ...series('fillType', 0, m.fill),
        ...series('git', 0, m.branch),
        ...series('cScale', 0, m.cScale),
    },
    themeCSS: themeCSS(m),
});

export const pulumiMermaidLight = build(MODES.light);
export const pulumiMermaidDark = build(MODES.dark);
