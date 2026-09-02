// The homepage hero's agent-loop animation: one GSAP timeline driving the
// inline SVG authored in
// layouts/partials/template-partials/hero-animation/agent-loop.html. That
// markup is the finished frame — also the reduced-motion and no-JS rendering —
// so this file's first job is reset(), which winds it back to the opening
// state. From there one pass plays out (a weighted-random agent, a
// weighted-random language) and the timeline repeats forever.
//
// The loop is what makes this file subtle. Every rule below exists because
// breaking it still renders a flawless first pass:
//
//   - reset() owns every value that differs between passes, including
//     everything the closing beats fade or move. Prefer it to a zero-duration
//     tl.set() at time 0, which rewinds to the value it recorded before first
//     running when the playhead wraps.
//   - gsap.killTweensOf() kills timeline children too, and permanently. It is
//     safe only on targets tweened exclusively by callback-spawned tweens.
//   - Every proxy object a tween mutates has to be rewound by reset(); that is
//     what trackProxy registers.
//   - Per-target function values don't reliably re-evaluate under
//     repeatRefresh on multi-target tweens. Tween a proxy 0 -> 1 and place the
//     elements from current-pass data in onUpdate.
//   - Timeline children need fixed targets, so anything chosen per pass is
//     routed through reset(), a re-parenting callback, or a proxy.
//
// To verify, step loops 2 and 3 rather than watching loop 1. Chrome's
// --virtual-time-budget can't scrub GSAP — lag smoothing clamps the jumps —
// so expose tl behind a temporary debug hook and drive it with
// `tl.pause(); for (t = 0; t <= T; t += 0.04) tl.totalTime(t, false)`, having
// stubbed Math.random beforehand to pin the agent and the language. Spawned
// tweens don't advance while stepping; force them complete before trusting a
// still.

import { gsap } from "gsap";

const CW = 7.44141;
const CW_PROMPT = 13.5 * (CW / 12) - 0.675;

const PROMPT_TEXT_X = 213;
const CODE_TEXT_X = 122;

const HALO_PAD = 6;
const HALO_GROW = 12.8;
const HALO_RX = 19.5;
const PANEL_FILL = { x: 112, y: 157, width: 520, height: 257, rx: 16 };
const PANEL_STROKE = { x: 112.5, y: 157.5, width: 519, height: 256, rx: 15.5 };
const PANEL_OUTER = { x: 104.5, y: 149.5, width: 535, height: 272, rx: 21.5 };
const PILL_BOTTOM = 521.5;
const CI_ROW_RIDE = 62;
const SLOT_REDISTRIBUTE = 10;

const PERCH = { x: 371.5, bottom: 136.89 };
const GLYPH_AT_TAB = -30;
const GLYPH_AT_PLATE = -70;

const AGENT_WEIGHTS: { [agent: string]: number } = {
    "claude-code": 66,
    "codex": 15,
    "cursor": 8,
    "copilot": 3.5,
    "neo": 3.5,
    "opencode": 4,
};

// Per-pass language odds: real usage share, with brand-new HCL boosted to
// just above YAML and Java at the floor.
const LANG_WEIGHTS: { [lang: string]: number } = {
    typescript: 40,
    python: 30,
    go: 10,
    csharp: 10,
    hcl: 7,
    yaml: 2,
    java: 1,
};

// Unselected agent and language logos recede to violet-400 when the choice
// lands; everything is authored (and reset to) the full violet-700.
const LOGO_FILL = "#5A30C5";
const LOGO_DIM_FILL = "#9077F3";

// Where the chosen language's icon parks in the code panel: tucked into the
// top-right corner and kept small so a long second code line never runs
// underneath it (the storyboard's 23.4px icon at 596,168 sat lower and
// larger).
const PANEL_LANG_CENTER = { x: 615.5, y: 172.5 };
const PANEL_LANG_SIZE = 15;

// The language pill's flow layout (storyboard frame 1): labels at font-size 10
// with 0.05em tracking, centered in the pill with a constant gap; the chosen
// item grows an 18px icon prefix and a ring with asymmetric padding.
const LANG_ADV = 10 * (CW / 12) + 0.5;
const LANG_PILL = { x: 203, width: 338, gap: 18.6, minPad: 10, restPad: 22 };
const LANG_ICON = { size: 18, gap: 7, centerY: 426 };
const LANG_RING_PAD = { left: 10.5, right: 9.5 };

// The write beat always takes the same wall time; per-character speed adapts
// to the chosen language's example. Bursts (blank-line groups in the source)
// pause for a fixed number of character-units.
const TYPE_SECONDS = 1.5;
const TYPE_PAUSE_UNITS = 50;
const TYPE_CHUNK_MIN = 5;
const TYPE_CHUNK_MAX = 13;

// The hidden state of a draw-on stroke. Parking it exactly on the pattern
// boundary (dasharray "1", offset 1) lets antialiasing show slivers of the
// rounded corners, so the pattern carries margin; once a draw completes its
// beat sets stroke-dasharray to none so the resting stroke is plain.
const DASH_HIDDEN = { "stroke-dasharray": "1 2", "stroke-dashoffset": "1.5" };

// The PR icon's resting x. GSAP's x replaces the authored transform's
// translate rather than adding to it, so tween endpoints have to land on the
// markup's offset instead of on 0.
const CI_PR_REST_X = -10;

const CUBE_H = 84.752;
const TERM_SCROLL_END = -898;
const TERM_FOLD_Y = 410;

// The finished frame holds — cubes bobbing gently — then the scene fades and
// the next pass, a fresh agent and a fresh language, starts over.
const REST_SECONDS = 10;
const FADE_SECONDS = 0.6;

// The cubes drift on the same ambient bob as the agent glyph, each on its own
// amplitude, period, and starting phase (in DOM order: the back cube, then
// front-left, then front-right) so the three never march in step. The label
// rides along inside the cube's group. They run for the whole timeline; nobody
// sees them until the diagram lands.
const CUBE_BOB = [
    { y: -4.5, duration: 2.4, offset: 0 },
    { y: -3.5, duration: 2, offset: 0.9 },
    { y: -4, duration: 2.8, offset: 1.7 },
];

// Closing a panel rolls it up rather than dissolving it: the fill, the hairline
// and the window the text is clipped to all pin their bottom edge and ride the
// shell's descending top edge, so the code (or the stream) is wiped away by the
// panel closing over it. Once the window is shorter than ROLL_BLIND — a strip
// at the panel's foot that no line of text ever reaches — the content is hidden
// outright rather than left to a clip that covers no glyphs, the same WebKit
// hazard the per-line typing clips avoid.
const PANEL_TOP = PANEL_FILL.y;
const PANEL_BOTTOM = PANEL_FILL.y + PANEL_FILL.height;
const ROLL_BLIND = 24;

type Roller = { el: SVGRectElement; top: number; bottom: number };

function rollPanel(rects: Roller[], content: SVGGElement, shellTop: number): void {
    const dy = shellTop - PANEL_OUTER.y;
    for (let i = 0; i < rects.length; i++) {
        const r = rects[i];
        const y = Math.min(r.top + dy, r.bottom);
        r.el.setAttribute("y", String(y));
        r.el.setAttribute("height", String(r.bottom - y));
    }
    content.style.opacity = PANEL_BOTTOM - (PANEL_TOP + dy) > ROLL_BLIND ? "1" : "0";
}

function q<T extends Element>(root: Element, sel: string): T {
    return root.querySelector(sel) as T;
}

function qa<T extends Element>(root: Element, sel: string): T[] {
    return Array.prototype.slice.call(root.querySelectorAll(sel));
}

function init(): void {
    const root = document.getElementById("hero-agent-loop");
    if (!root) {
        return;
    }

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (reduceMotion.matches) {
        root.classList.remove("hal-pending");
        return;
    }

    const tiles = qa<SVGGElement>(root, "[data-tile]");
    const tileRects = qa<SVGRectElement>(root, "[data-tile-rect]");
    const tileLogos = qa<SVGGElement>(root, "[data-tile-logo]");
    const prompt = q<SVGGElement>(root, "[data-prompt]");
    const promptClip = q<SVGRectElement>(root, "[data-prompt-clip]");
    const promptText = q<SVGTextElement>(root, "[data-prompt-text]");
    const promptCaret = q<SVGRectElement>(root, "[data-prompt-caret]");

    const aFill = q<SVGRectElement>(root, "[data-a-fill]");
    const aStroke = q<SVGRectElement>(root, "[data-a-stroke]");
    const aOuter = q<SVGRectElement>(root, "[data-a-outer]");
    const bFill = q<SVGRectElement>(root, "[data-b-fill]");
    const bStroke = q<SVGRectElement>(root, "[data-b-stroke]");
    const bOuter = q<SVGRectElement>(root, "[data-b-outer]");

    const glyph = q<SVGGElement>(root, "[data-glyph]");
    const glyphFloat = q<SVGGElement>(root, "[data-glyph-f]");
    const glyphStatic = q<SVGPathElement>(root, "[data-glyph-static]");
    if (glyphStatic && glyphStatic.parentNode) {
        glyphStatic.parentNode.removeChild(glyphStatic);
    }

    const codeLines = qa<SVGTextElement>(root, "[data-code-line]");
    const lineClips = qa<SVGRectElement>(root, "[data-lc]");
    const editorGroups = qa<SVGGElement>(root, "[data-editor-lang]");
    const caret = q<SVGRectElement>(root, "[data-caret]");

    const langRow = q<SVGGElement>(root, "[data-lang-row]");
    const langShorts = qa<SVGTextElement>(root, "[data-lang-short]");
    const langFulls = qa<SVGTextElement>(root, "[data-lang-full]");
    const langRing = q<SVGRectElement>(root, "[data-lang-ring]");
    const langIcons = q<SVGGElement>(root, "[data-lang-icons]");
    const langLogos = qa<SVGGElement>(root, "[data-lang-logo]");
    const panelLang = q<SVGGElement>(root, "[data-panel-lang]");

    const editorClip = q<SVGGElement>(root, "[data-editor-clip]");
    const editorWindow = q<SVGRectElement>(root, "#hal-clip-editor [data-panel-window]");
    const termWindow = q<SVGRectElement>(root, "#hal-clip-term [data-panel-window]");
    const termClip = q<SVGGElement>(root, "[data-term-clip]");
    const termScroll = q<SVGGElement>(root, "[data-term-scroll]");
    const termLines = qa<SVGTextElement>(root, "[data-term-line]");
    const tab = q<SVGGElement>(root, "[data-tab]");

    const ciRow = q<SVGGElement>(root, "[data-ci-row]");
    const ciPr = q<SVGGElement>(root, "[data-ci-pr]");
    const ciMerge = q<SVGGElement>(root, "[data-ci-merge]");
    const ciSlots = qa<SVGGElement>(root, "[data-ci-slot]");
    const ciSpins = qa<SVGGElement>(root, "[data-ci-spin]");
    const ciChecks = qa<SVGGElement>(root, "[data-ci-check]");
    const slotX = ciSlots.map(s => {
        const m = (s.getAttribute("transform") || "").match(/translate\(([-\d.]+)/);
        return m ? parseFloat(m[1]) : 0;
    });

    const badgeTests = q<SVGGElement>(root, "[data-badge-tests]");
    const badgePolicy = q<SVGGElement>(root, "[data-badge-policy]");
    const badgeRects = qa<SVGRectElement>(root, "[data-badge-rect]");
    const badgeBodies = qa<SVGGElement>(root, "[data-badge-body]");

    const policyRow = q<SVGGElement>(root, "[data-policy-row]");
    const polShield = q<SVGGElement>(root, "[data-pol-shield]");
    const polStacks = qa<SVGGElement>(root, "[data-pol-stack]");
    const polFiles = qa<SVGPathElement>(root, "[data-pol-file]");
    const polChecks = qa<SVGPathElement>(root, "[data-pol-check]");

    const diagram = q<SVGGElement>(root, "[data-diagram]");
    const plate = q<SVGGElement>(root, "[data-plate]");
    const plateFill = q<SVGRectElement>(root, "[data-plate-fill]");
    const plateDetail = q<SVGGElement>(root, "[data-plate-detail]");
    const cubes = qa<SVGGElement>(root, "[data-cube]");
    const cubeLabels = qa<SVGTextElement>(root, "[data-cube-label]");

    // The code panel's two fills are authored for whichever treatment
    // data/hero_agent_loop.yaml selected: shell B opens straight onto the
    // panel, while shell A starts life as the chosen agent's tile and so
    // carries the tile's lavender until it opens as the editor. Reading both
    // off the markup keeps the colors in one place — the partial.
    const CELL_FILL = { "fill": aFill.getAttribute("fill") as string, "fill-opacity": aFill.getAttribute("fill-opacity") as string };
    const PANEL_FILL_PAINT = { "fill": bFill.getAttribute("fill") as string, "fill-opacity": bFill.getAttribute("fill-opacity") as string };

    // Authored geometry is the open panel, so each rect's roll is read straight
    // off the markup before anything moves.
    const roller = (el: SVGRectElement): Roller => {
        const top = parseFloat(el.getAttribute("y") as string);
        return { el: el, top: top, bottom: top + parseFloat(el.getAttribute("height") as string) };
    };
    const editorRollers = [roller(aFill), roller(editorWindow)];
    const termRollers = [roller(bFill), roller(bStroke), roller(termWindow)];

    let chosen = 0;
    const perch = { x: 0, y: 0 };

    const tileWeights = tiles.map(tile => AGENT_WEIGHTS[tile.getAttribute("data-agent") || ""] || 0);

    function pickWeighted(weights: number[]): number {
        let sum = 0;
        weights.forEach(w => (sum += w));
        let r = Math.random() * sum;
        for (let i = 0; i < weights.length; i++) {
            r -= weights[i];
            if (r < 0) {
                return i;
            }
        }
        return 0;
    }

    function cellFill(): { x: number; y: number; width: number; height: number; rx: number } {
        const r = tileRects[chosen];
        return {
            x: parseFloat(r.getAttribute("x") || "0"),
            y: parseFloat(r.getAttribute("y") || "0"),
            width: parseFloat(r.getAttribute("width") || "0"),
            height: parseFloat(r.getAttribute("height") || "0"),
            rx: 16,
        };
    }

    function cellHalo(): { x: number; y: number; width: number; height: number; rx: number } {
        const c = cellFill();
        return { x: c.x - HALO_PAD, y: c.y - HALO_PAD, width: c.width + HALO_GROW, height: c.height + HALO_GROW, rx: HALO_RX };
    }

    // Proxies stand in wherever the timeline can't tween the real thing — a
    // per-pass layout, a shell's geometry. repeatRefresh re-captures a tween's
    // start values from whatever the proxy currently holds, so each one has to
    // be rewound by reset() or the next pass starts from the last pass's end
    // state.
    const loopProxies: Array<{ obj: any; initial: any }> = [];

    function trackProxy<T>(obj: T): T {
        loopProxies.push({ obj: obj, initial: Object.assign({}, obj) });
        return obj;
    }

    function adoptProtagonist(): void {
        glyphFloat.appendChild(tileLogos[chosen]);
        gsap.set(tiles[chosen], { autoAlpha: 0 });
        gsap.set([aFill, glyph], { autoAlpha: 1 });
    }

    // ------------------------------------------------------------------
    // The language. A uniform-random pick each pass; the chosen label gains
    // the selection ring, expands to its full name (where one exists), grows
    // its icon, and the icon travels to the code panel's corner while the
    // matching editor example types in.
    // ------------------------------------------------------------------
    let chosenLang = 0;
    const langNames = langShorts.map(t => t.getAttribute("data-language") || "");
    const langWeights = langNames.map(name => LANG_WEIGHTS[name] || 0);
    const langShortW = langShorts.map(t => (t.textContent || "").length * LANG_ADV);
    const langFullByName: { [name: string]: SVGTextElement } = {};
    langFulls.forEach(t => {
        langFullByName[t.getAttribute("data-language") || ""] = t;
    });

    const agentPaths = tileLogos.map(g => qa<SVGPathElement>(g, "path"));
    const langPaths = langLogos.map(g => qa<SVGPathElement>(g, "path"));

    // The chosen language's icon rides from the pill to the code panel's
    // corner, so it takes the panel's ink on the way rather than being
    // authored for one background or the other.
    const PANEL_INK = panelLang.getAttribute("data-ink") || LOGO_FILL;

    function dimUnselected(paths: SVGPathElement[][], keep: number): void {
        const targets: SVGPathElement[] = [];
        paths.forEach((ps, i) => {
            if (i !== keep) {
                targets.push.apply(targets, ps);
            }
        });
        gsap.to(targets, { attr: { fill: LOGO_DIM_FILL }, duration: 0.35 });
    }

    function chosenFull(): SVGTextElement | null {
        return langFullByName[langNames[chosenLang]] || null;
    }

    // Pill flow layout: labels centered with a constant gap; the chosen item
    // takes an icon prefix and (if it has one) its full name. restX/selX are
    // the label positions before and after selection.
    const restX: number[] = [];
    const selX: number[] = [];
    const ringBox = { x: 0, w: 0 };
    const iconRow = { x: 0, y: LANG_ICON.centerY };

    function layoutLangRow(): void {
        const fullEl = chosenFull();
        const fullW = fullEl ? (fullEl.textContent || "").length * LANG_ADV : langShortW[chosenLang];
        const selWidths = langShortW.slice();
        selWidths[chosenLang] = LANG_ICON.size + LANG_ICON.gap + fullW;
        const place = (ws: number[], out: number[]) => {
            let total = -LANG_PILL.gap;
            ws.forEach(w => (total += w + LANG_PILL.gap));
            let x = LANG_PILL.x + Math.max(LANG_PILL.minPad, (LANG_PILL.width - total) / 2);
            for (let i = 0; i < ws.length; i++) {
                out[i] = x;
                x += ws[i] + LANG_PILL.gap;
            }
        };
        // At rest the labels are justified across the pill; selection gathers
        // them into the tighter centered flow the storyboard shows.
        let restTotal = 0;
        langShortW.forEach(w => (restTotal += w));
        const restGap = (LANG_PILL.width - 2 * LANG_PILL.restPad - restTotal) / (langShortW.length - 1);
        let rx = LANG_PILL.x + LANG_PILL.restPad;
        for (let i = 0; i < langShortW.length; i++) {
            restX[i] = rx;
            rx += langShortW[i] + restGap;
        }
        const itemX: number[] = [];
        place(selWidths, itemX);
        for (let i = 0; i < itemX.length; i++) {
            selX[i] = itemX[i];
        }
        selX[chosenLang] = itemX[chosenLang] + LANG_ICON.size + LANG_ICON.gap;
        ringBox.x = itemX[chosenLang] - LANG_RING_PAD.left;
        ringBox.w = selWidths[chosenLang] + LANG_RING_PAD.left + LANG_RING_PAD.right;
        iconRow.x = itemX[chosenLang] + LANG_ICON.size / 2;
    }

    // The chosen language's icon is positioned by one manual transform
    // (translate + scale about the origin, placing its native bbox center),
    // so GSAP transforms must never touch panelLang — only its opacity.
    const iconT = { x: 0, y: 0, k: 1 };
    const iconCenter = { x: 0, y: 0 };
    let panelK = 1;
    let iconPop: any = null;

    function applyIconT(): void {
        const tx = iconT.x - iconT.k * iconCenter.x;
        const ty = iconT.y - iconT.k * iconCenter.y;
        panelLang.setAttribute("transform", "translate(" + tx + " " + ty + ") scale(" + iconT.k + ")");
    }

    function selectLanguage(): void {
        const fullEl = chosenFull();
        if (fullEl) {
            gsap.to(langShorts[chosenLang], { autoAlpha: 0, duration: 0.2 });
            gsap.fromTo(fullEl, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3, delay: 0.08 });
        }
        gsap.to(
            langShorts.filter((_t, i) => i !== chosenLang),
            { attr: { fill: LOGO_DIM_FILL }, duration: 0.35 },
        );
    }

    function adoptLanguage(): void {
        panelLang.appendChild(langLogos[chosenLang]);
        const kEnd = iconT.k;
        iconT.k = kEnd * 0.7;
        applyIconT();
        iconPop = gsap.to(iconT, { k: kEnd, duration: 0.35, ease: "back.out(1.7)", onUpdate: applyIconT });
        gsap.fromTo(panelLang, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.25 });
    }

    // Typing state for the active language, rebuilt each pass: per-line
    // character counts plus pause segments between blank-line bursts, mapped
    // onto one 0..1 progress tween.
    type TypeSegment = { line: number; startU: number; units: number; chunks: number[]; col: number; shown: number };
    let typeSegments: TypeSegment[] = [];
    let typeTotal = 1;
    let activeEditor: SVGGElement | null = null;
    let activeLines: SVGTextElement[] = [];
    let activeClips: SVGRectElement[] = [];

    function prepareTyping(): void {
        const lang = langNames[chosenLang];
        activeEditor = editorGroups.filter(g => g.getAttribute("data-editor-lang") === lang)[0];
        activeLines = qa<SVGTextElement>(activeEditor, "[data-code-line]");
        activeClips = qa<SVGRectElement>(root as HTMLElement, '[data-lc="' + lang + '"]');
        typeSegments = [];
        let u = 0;
        let prevRow = -1;
        for (let i = 0; i < activeLines.length; i++) {
            const row = Math.round((parseFloat(activeClips[i].getAttribute("y") || "166") - 166) / 18);
            if (prevRow >= 0 && row - prevRow > 1) {
                u += TYPE_PAUSE_UNITS;
            }
            const chars = parseInt(activeLines[i].getAttribute("data-chars") || "0", 10);
            // Text lands in chunks, like tokens streaming, rather than
            // character by character; boundaries are re-rolled each pass.
            const chunks: number[] = [];
            let c = 0;
            while (c < chars) {
                c = Math.min(chars, c + TYPE_CHUNK_MIN + Math.floor(Math.random() * (TYPE_CHUNK_MAX - TYPE_CHUNK_MIN + 1)));
                chunks.push(c);
            }
            const col = parseInt(activeLines[i].getAttribute("data-col") || "0", 10);
            typeSegments.push({ line: i, startU: u, units: chars, chunks: chunks, col: col, shown: -1 });
            u += chars;
            prevRow = row;
        }
        typeTotal = Math.max(1, u);
    }

    // A reveal that has only reached a line's leading indent covers no glyphs,
    // and WebKit drops a clip whose rect intersects nothing at all — painting
    // the whole line rather than hiding it. Keep the line out of the render
    // until the reveal reaches its first character.
    function reveal(seg: TypeSegment, width: number): void {
        // Every frame walks every line typed so far, but only one of them has
        // moved; rewriting the rest re-invalidates their clips for nothing.
        if (width === seg.shown) {
            return;
        }
        seg.shown = width;
        activeClips[seg.line].setAttribute("width", String(width));
        activeLines[seg.line].style.visibility = width > seg.col * CW ? "visible" : "hidden";
    }

    function renderTyping(p: number): void {
        const u = p * typeTotal;
        let caretClip: SVGRectElement | null = null;
        let caretChars = 0;
        for (let i = 0; i < typeSegments.length; i++) {
            const seg = typeSegments[i];
            const clip = activeClips[seg.line];
            if (u >= seg.startU + seg.units) {
                reveal(seg, seg.units * CW + 2);
                caretClip = clip;
                caretChars = seg.units;
            } else if (u > seg.startU) {
                const raw = u - seg.startU;
                let c = 0;
                for (let k = 0; k < seg.chunks.length; k++) {
                    if (raw >= seg.chunks[k]) {
                        c = seg.chunks[k];
                    } else {
                        break;
                    }
                }
                reveal(seg, c * CW + 2);
                caretClip = clip;
                caretChars = c;
            } else {
                break;
            }
        }
        if (caretClip) {
            caret.setAttribute("x", String(CODE_TEXT_X + caretChars * CW));
            caret.setAttribute("y", caretClip.getAttribute("y") || "166");
        }
    }

    function reset(): void {
        for (let i = 0; i < tileLogos.length; i++) {
            if (tileLogos[i].parentNode !== tiles[i]) {
                tiles[i].appendChild(tileLogos[i]);
            }
        }
        for (let i = 0; i < langLogos.length; i++) {
            if (langLogos[i].parentNode !== langIcons) {
                langIcons.appendChild(langLogos[i]);
            }
        }
        chosen = pickWeighted(tileWeights);
        const bb = tileLogos[chosen].getBBox();
        perch.x = PERCH.x - (bb.x + bb.width / 2);
        perch.y = PERCH.bottom - (bb.y + bb.height);

        chosenLang = pickWeighted(langWeights);
        layoutLangRow();
        if (iconPop) {
            iconPop.kill();
            iconPop = null;
        }
        const lb = langLogos[chosenLang].getBBox();
        const lSize = Math.max(lb.width, lb.height);
        iconCenter.x = lb.x + lb.width / 2;
        iconCenter.y = lb.y + lb.height / 2;
        panelK = PANEL_LANG_SIZE / lSize;
        iconT.x = iconRow.x;
        iconT.y = iconRow.y;
        iconT.k = LANG_ICON.size / lSize;
        applyIconT();
        prepareTyping();

        // The outro fades the whole scene out, so reset owns bringing it back.
        // A tl.set() at time 0 would look equivalent but rewinds to the value
        // it recorded before first running when the playhead wraps.
        gsap.set(root, { autoAlpha: 1 });

        // The agent logos, the language labels and the language icons are all
        // recolored by tweens that dimUnselected(), selectLanguage() and the
        // icon's panel recolor spawn from callbacks, and a spawned tween
        // outlives the pass that started it — hence kill, then repaint.
        // killTweensOf is safe on these three only because nothing in the
        // timeline targets them: it kills timeline children too, and
        // permanently. Kill one of those from reset() and it is gone from
        // every pass after the first, so the opening loop still looks perfect.
        const allAgentPaths: SVGPathElement[] = [];
        agentPaths.forEach(ps => {
            allAgentPaths.push.apply(allAgentPaths, ps);
        });
        gsap.killTweensOf(allAgentPaths);
        gsap.set(allAgentPaths, { attr: { fill: LOGO_FILL } });

        const allLabels = (langShorts as SVGTextElement[]).concat(langFulls);
        gsap.killTweensOf(allLabels);
        gsap.set(langShorts, { autoAlpha: 1, attr: { fill: LOGO_FILL } });
        langShorts.forEach((t, i) => gsap.set(t, { x: restX[i] }));
        gsap.set(langFulls, { autoAlpha: 0 });
        const fullEl = chosenFull();
        if (fullEl) {
            gsap.set(fullEl, { x: selX[chosenLang] });
        }

        gsap.set(langRow, { autoAlpha: 0, y: 16 });
        gsap.set(langRing, { autoAlpha: 0, attr: { x: ringBox.x, width: ringBox.w } });
        gsap.set(panelLang, { autoAlpha: 0 });

        gsap.set(editorGroups, { autoAlpha: 0 });
        if (activeEditor) {
            gsap.set(activeEditor, { autoAlpha: 1 });
        }

        gsap.set(tiles, { autoAlpha: 0, scale: 0.9, transformOrigin: "50% 50%" });
        gsap.set(prompt, { autoAlpha: 0, scale: 0.96, transformOrigin: "50% 50%" });
        gsap.set(promptClip, { attr: { width: 0 } });
        gsap.set(promptText, { visibility: "hidden" });
        gsap.set(promptCaret, { opacity: 0, attr: { x: PROMPT_TEXT_X } });

        const allLangPaths: SVGPathElement[] = [];
        langPaths.forEach(ps => {
            allLangPaths.push.apply(allLangPaths, ps);
        });
        gsap.killTweensOf(allLangPaths);
        gsap.set(allLangPaths, { attr: { fill: LOGO_FILL } });

        // Only the paint is restored here, never killed: the shell's tweens are
        // timeline children, and killing them would strip them from the
        // timeline for every pass after the first.
        const cf = cellFill();
        gsap.set(aFill, { autoAlpha: 0, scale: 1, attr: Object.assign({}, cf, CELL_FILL) });
        gsap.set(aStroke, {
            autoAlpha: 0,
            attr: {
                "x": cf.x,
                "y": cf.y,
                "width": cf.width,
                "height": cf.height,
                "rx": cf.rx,
                "stroke-dasharray": DASH_HIDDEN["stroke-dasharray"],
                "stroke-dashoffset": DASH_HIDDEN["stroke-dashoffset"],
            },
        });
        gsap.set(aOuter, { autoAlpha: 0, attr: cellHalo() });

        gsap.set(glyph, { x: 0, y: 0, autoAlpha: 0 });

        for (let i = 0; i < loopProxies.length; i++) {
            Object.assign(loopProxies[i].obj, loopProxies[i].initial);
        }

        gsap.set(lineClips, { attr: { width: 0 } });
        gsap.set(codeLines, { y: 0, opacity: 1, visibility: "hidden" });
        gsap.set(caret, { opacity: 0 });

        gsap.set(bOuter, { autoAlpha: 0, attr: { x: PANEL_OUTER.x, y: PANEL_OUTER.y, width: PANEL_OUTER.width, height: 0, rx: PANEL_OUTER.rx } });
        gsap.set(bFill, { autoAlpha: 0, attr: { x: PANEL_FILL.x, y: PANEL_FILL.y, width: PANEL_FILL.width, height: 0, rx: PANEL_FILL.rx } });
        gsap.set(bStroke, {
            autoAlpha: 0,
            attr: {
                "x": PANEL_STROKE.x,
                "y": PANEL_STROKE.y,
                "width": PANEL_STROKE.width,
                "height": 0,
                "rx": PANEL_STROKE.rx,
                "stroke-dasharray": "none",
                "stroke-dashoffset": "0",
            },
        });
        gsap.set(tab, { y: 34 });
        gsap.set([editorWindow, termWindow], { attr: { y: PANEL_TOP, height: PANEL_FILL.height } });
        gsap.set(editorClip, { opacity: 1 });
        gsap.set(termClip, { opacity: 0 });
        gsap.set(termScroll, { y: 0 });
        gsap.set(termLines, { opacity: 0 });

        gsap.set(ciRow, { autoAlpha: 1, y: -CI_ROW_RIDE });
        gsap.set(badgeTests, { autoAlpha: 1, y: -CI_ROW_RIDE });
        gsap.set(badgePolicy, { autoAlpha: 1 });
        ciSlots.forEach((slot, i) => gsap.set(slot, { x: slotX[i] + SLOT_REDISTRIBUTE }));
        gsap.set(ciPr, { autoAlpha: 0, scale: 1, transformOrigin: "50% 50%" });
        gsap.set(ciMerge, { autoAlpha: 0 });
        gsap.set(ciSpins, { autoAlpha: 0, scale: 0.6, transformOrigin: "50% 50%" });
        gsap.set(ciChecks, { autoAlpha: 0 });

        gsap.set(badgeRects, { attr: DASH_HIDDEN });
        gsap.set(badgeBodies, { autoAlpha: 0 });

        gsap.set(policyRow, { autoAlpha: 1 });
        gsap.set(polShield, { autoAlpha: 0, x: -12 });
        gsap.set(polStacks, { autoAlpha: 0, scale: 0.85, transformOrigin: "50% 50%" });
        gsap.set(polFiles, { opacity: 0.5, attr: { fill: "#1F1B21" } });
        gsap.set(polChecks, { attr: { fill: "#F49709" }, scale: 1, transformOrigin: "50% 50%" });

        gsap.set(diagram, { autoAlpha: 1, scale: 1, svgOrigin: "372 240" });
        gsap.set(plate, { autoAlpha: 0, scale: 0.85, svgOrigin: "372 260" });
        gsap.set(plateDetail, { autoAlpha: 0 });
        gsap.set(cubes, { autoAlpha: 0 });
        gsap.set(qa(root as HTMLElement, "[data-cube-top]"), { y: CUBE_H });
        gsap.set(qa(root as HTMLElement, "[data-cube-edge]"), { scaleY: 0.001, transformOrigin: "50% 100%" });
        gsap.set(cubeLabels, { autoAlpha: 0 });
    }

    // Infinite ambient loops stay out of the master timeline: the glyph's
    // float, the plate's pulse, the cubes' bob. updatePlayState is their only
    // owner — give one of these a second owner and the two fight over
    // play/pause. The caret blinks are kept separate for the same reason,
    // owned by blink() alone.
    const ambient: any[] = [];

    ambient.push(gsap.to(glyphFloat, { y: -2, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: -1 }));
    ambient.push(gsap.to(plateFill, { opacity: 0.55, duration: 2, ease: "sine.inOut", yoyo: true, repeat: -1 }));
    cubes.forEach((cube, i) => {
        const bob = CUBE_BOB[i % CUBE_BOB.length];
        ambient.push(gsap.to(cube, { y: bob.y, duration: bob.duration, ease: "sine.inOut", yoyo: true, repeat: -1 }).seek(bob.offset));
    });

    const caretBlink = gsap.to(caret, { opacity: 0, duration: 0.45, ease: "steps(1)", yoyo: true, repeat: -1, paused: true });
    const promptBlink = gsap.to(promptCaret, { opacity: 0, duration: 0.45, ease: "steps(1)", yoyo: true, repeat: -1, paused: true });

    function blink(tween: any, target: SVGRectElement, on: boolean): void {
        if (on) {
            tween.play(0);
        } else {
            tween.pause(0);
            gsap.set(target, { opacity: 1 });
        }
    }

    reset();
    const tl = gsap.timeline({ repeat: -1, paused: true, repeatRefresh: true, onRepeat: reset });

    const gridDelays = [0.12, 0, 0.18, 0.24, 0.06, 0.3];
    tiles.forEach((tile, i) => {
        tl.to(tile, { autoAlpha: 1, scale: 1, duration: 0.35, ease: "back.out(1.4)" }, gridDelays[i]);
    });

    tl.to(prompt, { autoAlpha: 1, scale: 1, duration: 0.3, ease: "power2.out" }, 0.5);
    const promptChars = 40;
    const promptType = trackProxy({ c: 0 });
    tl.call(() => gsap.set(promptCaret, { opacity: 1 }), undefined, 0.75);
    tl.to(
        promptType,
        {
            c: promptChars,
            duration: promptChars * 0.026,
            ease: "none",
            snap: { c: 1 },
            onUpdate: () => {
                const w = promptType.c * CW_PROMPT;
                promptClip.setAttribute("width", String(w));
                promptText.style.visibility = w > 0 ? "visible" : "hidden";
                promptCaret.setAttribute("x", String(PROMPT_TEXT_X + w + 1));
            },
        },
        0.75,
    );
    tl.call(() => blink(promptBlink, promptCaret, true), undefined, 1.8);

    tl.call(() => gsap.to(tiles[chosen], { scale: 0.965, duration: 0.12, yoyo: true, repeat: 1, ease: "power1.inOut", transformOrigin: "50% 50%" }), undefined, 1.8);
    tl.set(aStroke, { autoAlpha: 1 }, 1.95);
    tl.to(aStroke, { attr: { "stroke-dashoffset": "0" }, duration: 0.35, ease: "power1.inOut" }, 1.95);
    tl.call(() => dimUnselected(agentPaths, chosen), undefined, 2.0);
    tl.set(aStroke, { attr: { "stroke-dasharray": "none" } }, 2.32);
    tl.fromTo(
        aOuter,
        {
            autoAlpha: 0,
            attr: { x: () => cellFill().x, y: () => cellFill().y, width: () => cellFill().width, height: () => cellFill().height, rx: 16 },
        },
        {
            autoAlpha: 1,
            attr: { x: () => cellHalo().x, y: () => cellHalo().y, width: () => cellHalo().width, height: () => cellHalo().height, rx: HALO_RX },
            duration: 0.3,
            ease: "power2.out",
            immediateRender: false,
        },
        2.1,
    );

    tl.fromTo(langRow, { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: "power2.out", immediateRender: false }, 0.45);
    // The reflow is proxy-driven: per-target function values proved unreliable
    // under repeatRefresh on later loops, while proxies rewound by reset()
    // re-read the current pass's layout on every update.
    const slideT = trackProxy({ p: 0 });
    tl.to(
        slideT,
        {
            p: 1,
            duration: 0.4,
            ease: "power2.inOut",
            onUpdate: () => {
                for (let i = 0; i < langShorts.length; i++) {
                    gsap.set(langShorts[i], { x: restX[i] + (selX[i] - restX[i]) * slideT.p });
                }
            },
        },
        2.45,
    );
    tl.call(selectLanguage, undefined, 2.45);
    tl.fromTo(
        langRing,
        { autoAlpha: 0, attr: { x: () => ringBox.x + 5, y: 413, width: () => ringBox.w - 10, height: 26, rx: 13 } },
        {
            autoAlpha: 1,
            attr: { x: () => ringBox.x, y: 410.5, width: () => ringBox.w, height: 31, rx: 15.5 },
            duration: 0.3,
            ease: "power2.out",
            immediateRender: false,
        },
        2.55,
    );
    tl.call(adoptLanguage, undefined, 2.55);

    tl.call(adoptProtagonist, undefined, 3.5);
    tl.call(() => blink(promptBlink, promptCaret, false), undefined, 3.51);
    tl.to([tiles[5], tiles[3], tiles[2], tiles[4], tiles[1], tiles[0], prompt], { autoAlpha: 0, scale: 0.85, duration: 0.2, stagger: 0.04, ease: "power2.in" }, 3.5);
    tl.to(langRow, { autoAlpha: 0, duration: 0.25 }, 3.65);
    tl.to(iconT, { x: PANEL_LANG_CENTER.x, y: PANEL_LANG_CENTER.y, k: () => panelK, duration: 0.7, ease: "power2.inOut", onUpdate: applyIconT }, 3.65);
    tl.to(aFill, { attr: Object.assign({}, PANEL_FILL, PANEL_FILL_PAINT), duration: 0.7, ease: "power2.inOut" }, 3.65);
    // The icon's paths belong to whichever language this pass drew, so the
    // recolor spawns from a callback rather than a fixed-target child.
    tl.call(() => gsap.to(langPaths[chosenLang], { attr: { fill: PANEL_INK }, duration: 0.5 }), undefined, 3.8);
    tl.to(aStroke, { attr: PANEL_STROKE, duration: 0.7, ease: "power2.inOut" }, 3.65);
    tl.to(aOuter, { attr: PANEL_OUTER, duration: 0.7, ease: "power2.inOut" }, 3.65);
    tl.to(glyph, { x: () => perch.x, duration: 0.7, ease: "power2.inOut" }, 3.65);
    tl.to(glyph, { y: () => perch.y, duration: 0.75, ease: "power2.out" }, 3.6);

    const TYPE_START = 4.45;
    const typeProxy = trackProxy({ p: 0 });
    tl.call(
        () => {
            blink(caretBlink, caret, false);
            gsap.set(caret, { opacity: 1, attr: { x: CODE_TEXT_X, y: activeClips.length ? (activeClips[0].getAttribute("y") as string) : "166" } });
        },
        undefined,
        TYPE_START - 0.01,
    );
    tl.to(typeProxy, { p: 1, duration: TYPE_SECONDS, ease: "none", onUpdate: () => renderTyping(typeProxy.p) }, TYPE_START);
    tl.call(() => blink(caretBlink, caret, true), undefined, TYPE_START + TYPE_SECONDS + 0.01);
    const doneWriting = TYPE_START + TYPE_SECONDS + 0.35;

    tl.to(aStroke, { autoAlpha: 0, duration: 0.25 }, doneWriting);
    tl.call(() => blink(caretBlink, caret, false), undefined, doneWriting - 0.02);
    tl.call(() => gsap.to(caret, { opacity: 0, duration: 0.15 }), undefined, doneWriting);
    tl.to(aOuter, { attr: { height: 310 }, duration: 0.45, ease: "power2.out" }, doneWriting + 0.05);

    const ciAt = doneWriting + 0.45;
    tl.fromTo(ciPr, { autoAlpha: 0, x: CI_PR_REST_X - 16 }, { autoAlpha: 1, x: CI_PR_REST_X, duration: 0.35, ease: "power2.out" }, ciAt);
    tl.to(ciSpins, { autoAlpha: 1, scale: 1, duration: 0.3, stagger: 0.06, ease: "back.out(1.7)" }, ciAt + 0.15);

    const flipsAt = ciAt + 0.75;
    ciSlots.forEach((_slot, i) => {
        const at = flipsAt + i * 0.35;
        tl.to(ciSpins[i], { autoAlpha: 0, duration: 0.15 }, at);
        tl.fromTo(ciChecks[i], { autoAlpha: 0, scale: 0.6, transformOrigin: "50% 50%" }, { autoAlpha: 1, scale: 1, duration: 0.35, ease: "back.out(1.7)" }, at + 0.05);
    });
    const mergedAt = flipsAt + 4 * 0.35 + 0.1;
    tl.to(ciPr, { autoAlpha: 0, scale: 0.6, transformOrigin: "50% 50%", duration: 0.16, ease: "power2.in" }, mergedAt);
    tl.fromTo(ciMerge, { autoAlpha: 0, scale: 0.5, transformOrigin: "50% 50%" }, { autoAlpha: 1, scale: 1, duration: 0.32, ease: "back.out(1.7)" }, mergedAt + 0.1);

    const testsBadgeAt = mergedAt + 0.35;
    tl.to(badgeRects[0], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, testsBadgeAt);
    tl.set(badgeRects[0], { attr: { "stroke-dasharray": "none" } }, testsBadgeAt + 0.45);
    tl.to(badgeBodies[0], { autoAlpha: 1, duration: 0.3 }, testsBadgeAt + 0.15);

    const rollA = testsBadgeAt + 0.75;
    tl.to(panelLang, { autoAlpha: 0, duration: 0.3 }, rollA);
    const shellA = trackProxy({ top: PANEL_OUTER.y, h: 310, rx: 21.5 });
    tl.to(
        shellA,
        {
            top: 479.5,
            h: 42,
            rx: 21,
            duration: 0.8,
            ease: "power2.inOut",
            onUpdate: () => {
                aOuter.setAttribute("y", String(shellA.top));
                aOuter.setAttribute("height", String(shellA.h));
                aOuter.setAttribute("rx", String(shellA.rx));
                rollPanel(editorRollers, editorClip, shellA.top);
                const dy = shellA.top + shellA.h - PILL_BOTTOM;
                gsap.set([ciRow, badgeTests], { y: dy });
                const k = -dy / CI_ROW_RIDE;
                for (let i = 0; i < ciSlots.length; i++) {
                    gsap.set(ciSlots[i], { x: slotX[i] + SLOT_REDISTRIBUTE * k });
                }
            },
        },
        rollA,
    );

    const unfoldAt = rollA + 0.85;
    tl.set([bOuter, bFill, bStroke], { autoAlpha: 1 }, unfoldAt);
    tl.to(bOuter, { attr: { height: 319 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(bFill, { attr: { height: 257 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(bStroke, { attr: { height: 256 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(tab, { y: 0, duration: 0.35, ease: "power2.out" }, unfoldAt + 0.1);
    tl.to(glyph, { y: () => perch.y + GLYPH_AT_TAB, duration: 0.35, ease: "power2.out" }, unfoldAt + 0.16);
    tl.set(termClip, { opacity: 1 }, unfoldAt + 0.1);

    const streamAt = unfoldAt + 0.55;
    const aboveFold = termLines.filter(line => parseFloat(line.getAttribute("y") || "0") <= TERM_FOLD_Y);
    const belowFold = termLines.filter(line => parseFloat(line.getAttribute("y") || "0") > TERM_FOLD_Y);
    tl.to(aboveFold, { opacity: 1, duration: 0.04, stagger: 0.028 }, streamAt);
    tl.set(belowFold, { opacity: 1 }, streamAt + 0.35);

    const polAt = streamAt + 0.45;
    tl.to(polShield, { autoAlpha: 1, x: 0, duration: 0.3, ease: "power2.out" }, polAt);
    tl.to(polStacks, { autoAlpha: 1, scale: 1, duration: 0.3, stagger: 0.06, ease: "back.out(1.4)" }, polAt + 0.1);

    const polFlipsAt = polAt + 1.0;
    polStacks.forEach((_stack, i) => {
        const at = polFlipsAt + i * 0.45;
        tl.to(polFiles[i], { opacity: 1, attr: { fill: "#21C45D" }, duration: 0.3 }, at);
        tl.fromTo(polChecks[i], { scale: 0.6, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.35, ease: "back.out(1.7)" }, at);
        tl.to(polChecks[i], { attr: { fill: "#1C7D41" }, duration: 0.25 }, at);
    });

    const scrollAt = polFlipsAt + 0.35;
    tl.to(termScroll, { y: TERM_SCROLL_END, duration: 1.7, ease: "power1.inOut" }, scrollAt);

    const packsAt = scrollAt + 2.1;
    tl.to(badgeRects[1], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, packsAt);
    tl.set(badgeRects[1], { attr: { "stroke-dasharray": "none" } }, packsAt + 0.45);
    tl.to(badgeBodies[1], { autoAlpha: 1, duration: 0.3 }, packsAt + 0.15);

    const rollB = packsAt + 0.9;
    tl.to(tab, { y: 34, duration: 0.3, ease: "power2.in" }, rollB - 0.1);
    tl.to(
        bOuter,
        {
            attr: { y: 421.5, height: 42, rx: 21 },
            duration: 0.8,
            ease: "power2.inOut",
            onUpdate: () => rollPanel(termRollers, termClip, parseFloat(bOuter.getAttribute("y") as string)),
        },
        rollB,
    );

    const plateAt = rollB + 0.9;
    tl.to(plate, { autoAlpha: 1, scale: 1, duration: 0.6, ease: "power3.out" }, plateAt);
    tl.to(plateDetail, { autoAlpha: 1, duration: 0.4 }, plateAt + 0.15);
    tl.to(glyph, { y: () => perch.y + GLYPH_AT_PLATE, duration: 0.5, ease: "power2.out" }, plateAt + 0.05);

    const cubesAt = plateAt + 0.6;
    cubes.forEach((cube, i) => {
        const at = cubesAt + parseInt(cube.getAttribute("data-order") || String(i), 10) * 0.15;
        tl.to(cube, { autoAlpha: 1, duration: 0.2 }, at);
        tl.to(qa(cube, "[data-cube-top]"), { y: 0, duration: 0.55, ease: "back.out(1.2)" }, at + 0.1);
        tl.to(qa(cube, "[data-cube-edge]"), { scaleY: 1, duration: 0.55, ease: "back.out(1.2)" }, at + 0.1);
        tl.to(cubeLabels[i], { autoAlpha: 1, duration: 0.25 }, at + 0.5);
    });

    // Everything has landed. The finished frame rests — the cubes still bobbing
    // on their ambient tweens — then fades out, and onRepeat rebuilds the
    // opening state for a new agent and a new language.
    const restAt = cubesAt + 1.1;
    tl.to(root, { autoAlpha: 0, duration: FADE_SECONDS, ease: "power2.in" }, restAt + REST_SECONDS);

    root.classList.remove("hal-pending");

    // The master timeline and the ambient loops pause off-screen and in a
    // hidden tab. Callback-spawned tweens don't — they run on the global
    // timeline and keep going regardless, which is why they are kept short and
    // killed in reset() rather than left to finish.
    let inView = true;
    function updatePlayState(): void {
        const running = inView && document.visibilityState !== "hidden";
        (root as HTMLElement).classList.toggle("hal-idle", !running);
        if (running) {
            tl.play();
            ambient.forEach(t => t.play());
        } else {
            tl.pause();
            ambient.forEach(t => t.pause());
        }
    }

    if ("IntersectionObserver" in window) {
        new IntersectionObserver(
            entries => {
                inView = entries[0].isIntersecting;
                updatePlayState();
            },
            { threshold: 0.05 },
        ).observe(root);
    }
    document.addEventListener("visibilitychange", updatePlayState);
    updatePlayState();
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}
