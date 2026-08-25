import { gsap } from "gsap";

const CW = 7.44141;
const CW_PROMPT = 14 * (CW / 12) - 0.7;

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

const DASH_HIDDEN = { "stroke-dasharray": "1 2", "stroke-dashoffset": "1.5" };

const CI_PR_REST_X = -10;

const CUBE_H = 84.752;
const TERM_SCROLL_END = -592;
const TERM_FOLD_Y = 410;

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
    const caret = q<SVGRectElement>(root, "[data-caret]");

    const termClip = q<SVGGElement>(root, "[data-term-clip]");
    const termScroll = q<SVGGElement>(root, "[data-term-scroll]");
    const termLines = qa<SVGTextElement>(root, "[data-term-line]");
    const tab = q<SVGGElement>(root, "[data-tab]");

    const ciRow = q<SVGGElement>(root, "[data-ci-row]");
    const ciPr = q<SVGGElement>(root, "[data-ci-pr]");
    const ciMerge = q<SVGGElement>(root, "[data-ci-merge]");
    const ciSlots = qa<SVGGElement>(root, "[data-ci-slot]");
    const ciSpins = qa<SVGGElement>(root, "[data-ci-spin]");
    const ciArcs = qa<SVGPathElement>(root, "[data-ci-arc]");
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

    let chosen = 0;
    const perch = { x: 0, y: 0 };

    const tileWeights = tiles.map(tile => AGENT_WEIGHTS[tile.getAttribute("data-agent") || ""] || 0);

    function pickAgent(): number {
        let r = Math.random() * 100;
        for (let i = 0; i < tileWeights.length; i++) {
            r -= tileWeights[i];
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

    function reset(): void {
        for (let i = 0; i < tileLogos.length; i++) {
            if (tileLogos[i].parentNode !== tiles[i]) {
                tiles[i].appendChild(tileLogos[i]);
            }
        }
        chosen = pickAgent();
        const bb = tileLogos[chosen].getBBox();
        perch.x = PERCH.x - (bb.x + bb.width / 2);
        perch.y = PERCH.bottom - (bb.y + bb.height);

        gsap.set(tiles, { autoAlpha: 0, scale: 0.9, transformOrigin: "50% 50%" });
        gsap.set(prompt, { autoAlpha: 0, scale: 0.96, transformOrigin: "50% 50%" });
        gsap.set(promptClip, { attr: { width: 0 } });
        gsap.set(promptCaret, { opacity: 0, attr: { x: PROMPT_TEXT_X } });

        const cf = cellFill();
        gsap.set(aFill, { autoAlpha: 0, scale: 1, attr: cf });
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
        gsap.set(codeLines, { y: 0, opacity: 1 });
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
        gsap.set(termClip, { opacity: 0 });
        gsap.set(termScroll, { y: 0 });
        gsap.set(termLines, { opacity: 0 });

        gsap.set(ciRow, { autoAlpha: 1, y: -CI_ROW_RIDE });
        gsap.set(badgeTests, { autoAlpha: 1, y: -CI_ROW_RIDE });
        gsap.set(badgePolicy, { autoAlpha: 1 });
        ciSlots.forEach((slot, i) => gsap.set(slot, { x: slotX[i] + SLOT_REDISTRIBUTE }));
        gsap.set(ciPr, { autoAlpha: 0 });
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

        gsap.set(diagram, { autoAlpha: 1 });
        gsap.set(plate, { autoAlpha: 0, scale: 0.85, svgOrigin: "372 260" });
        gsap.set(plateDetail, { autoAlpha: 0 });
        gsap.set(cubes, { autoAlpha: 0 });
        gsap.set(qa(root as HTMLElement, "[data-cube-top]"), { y: CUBE_H });
        gsap.set(qa(root as HTMLElement, "[data-cube-edge]"), { scaleY: 0.001, transformOrigin: "50% 100%" });
        gsap.set(cubeLabels, { autoAlpha: 0 });
    }

    const ambient: any[] = [];

    ambient.push(gsap.to(glyphFloat, { y: -2, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: -1 }));
    ambient.push(gsap.to(plateFill, { opacity: 0.55, duration: 2, ease: "sine.inOut", yoyo: true, repeat: -1 }));

    const SPIN_PHASE = [0, 137, 244, 71];
    const spin = { a: 0 };
    ambient.push(
        gsap.to(spin, {
            a: 360,
            duration: 1,
            ease: "none",
            repeat: -1,
            onUpdate: () => {
                for (let i = 0; i < ciArcs.length; i++) {
                    ciArcs[i].setAttribute("transform", "rotate(" + (spin.a + SPIN_PHASE[i % SPIN_PHASE.length]) + ")");
                }
            },
        }),
    );

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
    const promptChars = 39;
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
                promptCaret.setAttribute("x", String(PROMPT_TEXT_X + w + 1));
            },
        },
        0.75,
    );
    tl.call(() => blink(promptBlink, promptCaret, true), undefined, 1.8);

    tl.set(aStroke, { autoAlpha: 1 }, 1.95);
    tl.to(aStroke, { attr: { "stroke-dashoffset": "0" }, duration: 0.35, ease: "power1.inOut" }, 1.95);
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

    tl.call(adoptProtagonist, undefined, 2.44);
    tl.call(() => blink(promptBlink, promptCaret, false), undefined, 2.45);
    tl.to([tiles[5], tiles[3], tiles[2], tiles[4], tiles[1], tiles[0], prompt], { autoAlpha: 0, scale: 0.85, duration: 0.2, stagger: 0.04, ease: "power2.in" }, 2.45);
    tl.to(aFill, { attr: PANEL_FILL, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(aStroke, { attr: PANEL_STROKE, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(aOuter, { attr: PANEL_OUTER, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(glyph, { x: () => perch.x, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(glyph, { y: () => perch.y, duration: 0.75, ease: "power2.out" }, 2.55);

    const CHAR_T = 0.0075;
    const bursts: number[][] = [
        [0, 1],
        [2, 3],
        [4, 5, 6, 7, 8, 9, 10],
    ];
    let cursor = 3.4;
    bursts.forEach((burst, b) => {
        tl.call(() => blink(caretBlink, caret, false), undefined, cursor);
        burst.forEach(k => {
            const chars = parseInt(codeLines[k].getAttribute("data-chars") || "0", 10);
            const clip = lineClips[k];
            const rowTop = clip.getAttribute("y");
            const type = trackProxy({ c: 0 });
            tl.call(() => gsap.set(caret, { opacity: 1, attr: { y: rowTop as string, x: CODE_TEXT_X } }), undefined, cursor);
            tl.to(
                type,
                {
                    c: chars,
                    duration: chars * CHAR_T,
                    ease: "none",
                    snap: { c: 1 },
                    onUpdate: () => {
                        const w = type.c * CW;
                        clip.setAttribute("width", String(w + 2));
                        caret.setAttribute("x", String(CODE_TEXT_X + w));
                    },
                },
                cursor,
            );
            cursor += chars * CHAR_T;
        });
        if (b < bursts.length - 1) {
            tl.call(() => blink(caretBlink, caret, true), undefined, cursor + 0.01);
            cursor += 0.35;
        }
    });
    tl.call(() => blink(caretBlink, caret, true), undefined, cursor + 0.01);
    const doneWriting = cursor + 0.4;

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
    tl.to(ciPr, { autoAlpha: 0, duration: 0.2 }, mergedAt);
    tl.fromTo(ciMerge, { autoAlpha: 0, scale: 0.8, transformOrigin: "50% 50%" }, { autoAlpha: 1, scale: 1, duration: 0.3, ease: "back.out(1.7)" }, mergedAt);

    const testsBadgeAt = mergedAt + 0.35;
    tl.to(badgeRects[0], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, testsBadgeAt);
    tl.set(badgeRects[0], { attr: { "stroke-dasharray": "none" } }, testsBadgeAt + 0.45);
    tl.to(badgeBodies[0], { autoAlpha: 1, duration: 0.3 }, testsBadgeAt + 0.15);

    const rollA = testsBadgeAt + 0.75;
    tl.to(codeLines, { y: -22, opacity: 0, duration: 0.2, stagger: 0.02, ease: "power1.in" }, rollA - 0.15);
    tl.to(aFill, { autoAlpha: 0, duration: 0.35 }, rollA);
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
    tl.to(aboveFold, { opacity: 1, duration: 0.05, stagger: 0.045 }, streamAt);
    tl.set(belowFold, { opacity: 1 }, streamAt + 0.5);

    const polAt = streamAt + 0.6;
    tl.to(polShield, { autoAlpha: 1, x: 0, duration: 0.3, ease: "power2.out" }, polAt);
    tl.to(polStacks, { autoAlpha: 1, scale: 1, duration: 0.3, stagger: 0.06, ease: "back.out(1.4)" }, polAt + 0.1);

    const polFlipsAt = polAt + 1.0;
    polStacks.forEach((_stack, i) => {
        const at = polFlipsAt + i * 0.45;
        tl.to(polFiles[i], { opacity: 1, attr: { fill: "#21C45D" }, duration: 0.3 }, at);
        tl.fromTo(polChecks[i], { scale: 0.6, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.35, ease: "back.out(1.7)" }, at);
        tl.to(polChecks[i], { attr: { fill: "#1C7D41" }, duration: 0.25 }, at);
    });

    const scrollAt = polFlipsAt + 0.7;
    tl.to(termScroll, { y: TERM_SCROLL_END, duration: 2, ease: "power1.inOut" }, scrollAt);

    const packsAt = scrollAt + 2.15;
    tl.to(badgeRects[1], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, packsAt);
    tl.set(badgeRects[1], { attr: { "stroke-dasharray": "none" } }, packsAt + 0.45);
    tl.to(badgeBodies[1], { autoAlpha: 1, duration: 0.3 }, packsAt + 0.15);

    const rollB = packsAt + 0.7;
    tl.to(termClip, { opacity: 0, duration: 0.25 }, rollB - 0.1);
    tl.to(tab, { y: 34, duration: 0.3, ease: "power2.in" }, rollB - 0.1);
    tl.to([bFill, bStroke], { autoAlpha: 0, duration: 0.3 }, rollB);
    tl.to(bOuter, { attr: { y: 421.5, height: 42, rx: 21 }, duration: 0.8, ease: "power2.inOut" }, rollB);

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

    const outAt = cubesAt + 1.1 + 2.0;
    tl.to([diagram, aOuter, bOuter, ciRow, ciMerge, badgeTests, badgePolicy, policyRow, glyph], { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, outAt);
    tl.to(root, { autoAlpha: 1, duration: 0.3 }, outAt + 0.5);

    root.classList.remove("hal-pending");

    let inView = true;
    function updatePlayState(): void {
        const running = inView && document.visibilityState !== "hidden";
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
