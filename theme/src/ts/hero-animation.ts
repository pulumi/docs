// Homepage hero animation: the agentic loop (see
// layouts/partials/template-partials/hero-animation/agent-loop.html for the
// scene markup and the geometry provenance).
//
// The SVG is authored in its finished state (storyboard frame 7). This script
// resets it to the opening state and plays one ~20s pass, holds on the
// finished diagram, then loops. Under prefers-reduced-motion it only unhides
// the scene, so the finished frame renders statically with no layout shift.

import { gsap } from "gsap";

// Monaspace Neon advance width at font-size 12 (from the Figma export metrics)
// and at the prompt's font-size 14 with -0.05em tracking.
const CW = 7.44141;
const CW_PROMPT = 14 * (CW / 12) - 0.7;

const PROMPT_TEXT_X = 213;
const CODE_TEXT_X = 122;

// Shell geometry (storyboard measurements).
const TILE_FILL = { x: 209.5, y: 165.5, width: 98.813, height: 99.213, rx: 15.5 };
const TILE_OUTER = { x: 203.5, y: 159.5, width: 111.581, height: 112.032, rx: 19.5 };
const PANEL_FILL = { x: 112, y: 157, width: 520, height: 257, rx: 16 };
const PANEL_STROKE = { x: 112.5, y: 157.5, width: 519, height: 256, rx: 15.5 };
const PANEL_OUTER = { x: 104.5, y: 149.5, width: 535, height: 272, rx: 21.5 };
const PILL_BOTTOM = 521.5; // shared bottom anchor: CI pill bottom edge
const CI_ROW_RIDE = 62; // how far the CI row rides between panel and pill state
const SLOT_REDISTRIBUTE = 10; // status slots shift left this much in the pill

// The glyph is authored at its code-panel position (y=100); these are the
// translations to its other stations.
const GLYPH_IN_TILE = { x: -112.605, y: 96.661 };
const GLYPH_AT_TAB = -30; // pushed up by the ROLE tab
const GLYPH_AT_PLATE = -70; // pushed up by the isometric plate

const CUBE_H = 84.752; // vertical edge length of the subnet cubes (extrusion height)
const TERM_SCROLL_END = -466; // lands the stream on Outputs / Duration
const TERM_FOLD_Y = 410; // stream lines with baselines beyond this start below the fold

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

    // ------------------------------------------------------------------
    // Reset: put the finished-state markup into the opening state. Runs once
    // up front and again on every loop (the closing collapse leaves the stage
    // dark; this brings the agent grid back).
    // ------------------------------------------------------------------
    function reset(): void {
        gsap.set(tiles, { autoAlpha: 0, scale: 0.9, transformOrigin: "50% 50%" });
        gsap.set(prompt, { autoAlpha: 0, scale: 0.96, transformOrigin: "50% 50%" });
        gsap.set(promptClip, { attr: { width: 0 } });
        gsap.set(promptCaret, { opacity: 0, attr: { x: PROMPT_TEXT_X } });

        gsap.set(aFill, { autoAlpha: 0, scale: 0.9, transformOrigin: "50% 50%", attr: TILE_FILL });
        // Hidden dash state carries margin on both sides ("1 2" pattern,
        // offset 1.5) — parking the offset exactly at the pattern boundary
        // leaves antialiased slivers of the stroke's rounded corners visible.
        gsap.set(aStroke, {
            autoAlpha: 0,
            attr: {
                "x": TILE_FILL.x,
                "y": TILE_FILL.y,
                "width": TILE_FILL.width,
                "height": TILE_FILL.height,
                "rx": TILE_FILL.rx,
                "stroke-dasharray": "1 2",
                "stroke-dashoffset": "1.5",
            },
        });
        gsap.set(aOuter, { autoAlpha: 0, attr: TILE_OUTER });

        gsap.set(glyph, { x: GLYPH_IN_TILE.x, y: GLYPH_IN_TILE.y, autoAlpha: 0 });

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

        gsap.set(ciRow, { y: -CI_ROW_RIDE });
        gsap.set(badgeTests, { y: -CI_ROW_RIDE });
        ciSlots.forEach((slot, i) => gsap.set(slot, { x: slotX[i] + SLOT_REDISTRIBUTE }));
        gsap.set(ciPr, { autoAlpha: 0 });
        gsap.set(ciMerge, { autoAlpha: 0 });
        gsap.set(ciSpins, { autoAlpha: 0, scale: 0.6, transformOrigin: "50% 50%" });
        gsap.set(ciChecks, { autoAlpha: 0 });

        gsap.set(badgeRects, { attr: { "stroke-dasharray": "1 2", "stroke-dashoffset": "1.5" } });
        gsap.set(badgeBodies, { autoAlpha: 0 });

        gsap.set(policyRow, { autoAlpha: 1 });
        gsap.set(polShield, { autoAlpha: 0, x: -12 });
        gsap.set(polStacks, { autoAlpha: 0, scale: 0.85, transformOrigin: "50% 50%" });
        gsap.set(polFiles, { opacity: 0.5, attr: { fill: "#1F1B21" } });
        gsap.set(polChecks, { attr: { fill: "#F49709" }, scale: 1, transformOrigin: "50% 50%" });

        gsap.set(diagram, { autoAlpha: 1 });
        gsap.set(plate, { autoAlpha: 0, scale: 0.85, svgOrigin: "372 260" });
        gsap.set(plateDetail, { autoAlpha: 0 });
        // Cubes start flattened onto the plate: top face dropped onto the
        // bottom face, vertical edges at zero height.
        gsap.set(cubes, { autoAlpha: 0 });
        gsap.set(qa(root as HTMLElement, "[data-cube-top]"), { y: CUBE_H });
        gsap.set(qa(root as HTMLElement, "[data-cube-edge]"), { scaleY: 0.001, transformOrigin: "50% 100%" });
        gsap.set(cubeLabels, { autoAlpha: 0 });
    }

    // ------------------------------------------------------------------
    // Ambient layer: idle float, caret blinks, spinner rotation, plate
    // breathe. These run as their own loops (never inside the master
    // timeline) so they survive repeats; visibility is governed by their
    // parents.
    // ------------------------------------------------------------------
    const ambient: any[] = [];

    ambient.push(gsap.to(glyphFloat, { y: -2, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: -1 }));
    ambient.push(gsap.to(plateFill, { opacity: 0.55, duration: 2, ease: "sine.inOut", yoyo: true, repeat: -1 }));

    const spin = { a: 0 };
    ambient.push(
        gsap.to(spin, {
            a: 360,
            duration: 1,
            ease: "none",
            repeat: -1,
            onUpdate: () => {
                for (let i = 0; i < ciArcs.length; i++) {
                    ciArcs[i].setAttribute("transform", "rotate(" + spin.a + ")");
                }
            },
        }),
    );

    // The caret blinks are deliberately not in the ambient list — the story
    // timeline pauses and resumes them itself, so the play-state manager must
    // not fight it. A blink ticking behind a hidden tab costs nothing.
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

    // ------------------------------------------------------------------
    // The master timeline. One pass through the story, then a hold on the
    // finished diagram, a quick collapse, and a repeat (onRepeat re-runs
    // reset(), which restores the opening state).
    // ------------------------------------------------------------------
    reset();
    const tl = gsap.timeline({ repeat: -1, paused: true, onRepeat: reset });

    // -- Agent grid staggers in, centre-out (tile 1 is the shell trio).
    const gridIn: Array<{ targets: gsap.TweenTarget; delay: number }> = [
        { targets: tiles[0], delay: 0 }, // Codex (closest to centre)
        { targets: tiles[3], delay: 0.06 }, // Pulumi Neo
        { targets: [aFill, glyph], delay: 0.12 }, // Claude Code
        { targets: tiles[1], delay: 0.18 }, // Cursor
        { targets: tiles[2], delay: 0.24 }, // Copilot
        { targets: tiles[4], delay: 0.3 }, // opencode
    ];
    gridIn.forEach(entry => {
        tl.to(entry.targets, { autoAlpha: 1, scale: 1, duration: 0.35, ease: "back.out(1.4)" }, entry.delay);
    });

    // -- Prompt pill appears and the ask types in.
    tl.to(prompt, { autoAlpha: 1, scale: 1, duration: 0.3, ease: "power2.out" }, 0.5);
    const promptChars = 39;
    const promptType = { c: 0 };
    // Caret visibility is driven by callbacks, never by timeline children:
    // zero-duration sets rewind to their recorded prior values when the
    // playhead wraps for the loop, which is what left a stray block cursor
    // floating on the next iteration's opening frame.
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

    // -- Execute: the Claude Code tile takes the double outline. The inner
    //    #5A30C5 stroke is the "agent is working" flag; the outer shell
    //    scales out from it.
    tl.set(aStroke, { autoAlpha: 1 }, 1.95);
    tl.to(aStroke, { attr: { "stroke-dashoffset": "0" }, duration: 0.35, ease: "power1.inOut" }, 1.95);
    // Once drawn, drop the dash entirely — a plain solid stroke can't leak
    // dash-boundary artifacts (and stays immune to non-scaling-stroke's
    // screen-space dash units).
    tl.set(aStroke, { attr: { "stroke-dasharray": "none" } }, 2.32);
    tl.fromTo(aOuter, { autoAlpha: 0, attr: TILE_FILL }, { autoAlpha: 1, attr: TILE_OUTER, duration: 0.3, ease: "power2.out" }, 2.1);

    // -- The other agents bow out; the tile morphs into the code panel and
    //    the glyph detaches and arcs up to its perch.
    tl.call(() => blink(promptBlink, promptCaret, false), undefined, 2.45);
    tl.to([tiles[4], tiles[2], tiles[1], tiles[3], tiles[0], prompt], { autoAlpha: 0, scale: 0.85, duration: 0.2, stagger: 0.04, ease: "power2.in" }, 2.45);
    tl.to(aFill, { attr: PANEL_FILL, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(aStroke, { attr: PANEL_STROKE, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(aOuter, { attr: PANEL_OUTER, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(glyph, { x: 0, duration: 0.7, ease: "power2.inOut" }, 2.6);
    tl.to(glyph, { y: 0, duration: 0.75, ease: "power2.out" }, 2.55);

    // -- The agent writes the program: three bursts, block caret tracking the
    //    head, blinking through the beats between bursts.
    const CHAR_T = 0.0075;
    const bursts: number[][] = [
        [0, 1], // imports
        [2, 3], // resources
        [4, 5, 6, 7, 8, 9, 10], // the map body
    ];
    let cursor = 3.4;
    bursts.forEach((burst, b) => {
        tl.call(() => blink(caretBlink, caret, false), undefined, cursor);
        burst.forEach(k => {
            const chars = parseInt(codeLines[k].getAttribute("data-chars") || "0", 10);
            const clip = lineClips[k];
            const rowTop = clip.getAttribute("y");
            const type = { c: 0 };
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
    const doneWriting = cursor + 0.4; // ~6.7

    // -- Writing is done: the working stroke drops, the shell opens room
    //    below the code surface for the CI row.
    tl.to(aStroke, { autoAlpha: 0, duration: 0.25 }, doneWriting);
    // Stop the blink before fading the caret — a paused blink can't relight
    // it. The fade itself runs outside the timeline (see the caret note above).
    tl.call(() => blink(caretBlink, caret, false), undefined, doneWriting - 0.02);
    tl.call(() => gsap.to(caret, { opacity: 0, duration: 0.15 }), undefined, doneWriting);
    tl.to(aOuter, { attr: { height: 310 }, duration: 0.45, ease: "power2.out" }, doneWriting + 0.05);

    const ciAt = doneWriting + 0.45; // ~7.15
    // The PR icon rests 10px left of its export position (its authored
    // translate) — GSAP's x is absolute over that, so the slide-in must land
    // on -10, not 0.
    tl.fromTo(ciPr, { autoAlpha: 0, x: -26 }, { autoAlpha: 1, x: -10, duration: 0.35, ease: "power2.out" }, ciAt);
    tl.to(ciSpins, { autoAlpha: 1, scale: 1, duration: 0.3, stagger: 0.06, ease: "back.out(1.7)" }, ciAt + 0.15);

    // -- Checks flip one by one, then the PR merges.
    const flipsAt = ciAt + 0.75;
    ciSlots.forEach((_slot, i) => {
        const at = flipsAt + i * 0.35;
        tl.to(ciSpins[i], { autoAlpha: 0, duration: 0.15 }, at);
        tl.fromTo(ciChecks[i], { autoAlpha: 0, scale: 0.6, transformOrigin: "50% 50%" }, { autoAlpha: 1, scale: 1, duration: 0.35, ease: "back.out(1.7)" }, at + 0.05);
    });
    const mergedAt = flipsAt + 4 * 0.35 + 0.1;
    tl.to(ciPr, { autoAlpha: 0, duration: 0.2 }, mergedAt);
    tl.fromTo(ciMerge, { autoAlpha: 0, scale: 0.8, transformOrigin: "50% 50%" }, { autoAlpha: 1, scale: 1, duration: 0.3, ease: "back.out(1.7)" }, mergedAt);

    // -- ALL TESTS PASSED: border draws left to right, label fades in.
    const testsBadgeAt = mergedAt + 0.35;
    tl.to(badgeRects[0], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, testsBadgeAt);
    tl.set(badgeRects[0], { attr: { "stroke-dasharray": "none" } }, testsBadgeAt + 0.45);
    tl.to(badgeBodies[0], { autoAlpha: 1, duration: 0.3 }, testsBadgeAt + 0.15);

    // -- Roll up: the code wipes, the shell collapses onto its bottom edge
    //    and parks as the CI pill; the row and badge ride the same tween.
    const rollA = testsBadgeAt + 0.75; // ~10.1
    tl.to(codeLines, { y: -22, opacity: 0, duration: 0.2, stagger: 0.02, ease: "power1.in" }, rollA - 0.15);
    tl.to(aFill, { autoAlpha: 0, duration: 0.35 }, rollA);
    const shellA = { top: PANEL_OUTER.y, h: 310, rx: 21.5 };
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

    // -- The terminal unfolds beneath the glyph, top-anchored, working stroke
    //    on; the ROLE tab pops out from behind the top edge and shoves the
    //    glyph up, trailing 60ms behind.
    const unfoldAt = rollA + 0.85; // ~10.95
    tl.set([bOuter, bFill, bStroke], { autoAlpha: 1 }, unfoldAt);
    tl.to(bOuter, { attr: { height: 319 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(bFill, { attr: { height: 257 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(bStroke, { attr: { height: 256 }, duration: 0.7, ease: "power3.out" }, unfoldAt);
    tl.to(tab, { y: 0, duration: 0.35, ease: "power2.out" }, unfoldAt + 0.1);
    tl.to(glyph, { y: GLYPH_AT_TAB, duration: 0.35, ease: "power2.out" }, unfoldAt + 0.16);
    tl.set(termClip, { opacity: 1 }, unfoldAt + 0.1);

    // -- pulumi up streams: lines land whole; the rest of the stream sits
    //    below the fold and is revealed by the scroll.
    const streamAt = unfoldAt + 0.55;
    const aboveFold = termLines.filter(line => parseFloat(line.getAttribute("y") || "0") <= TERM_FOLD_Y);
    const belowFold = termLines.filter(line => parseFloat(line.getAttribute("y") || "0") > TERM_FOLD_Y);
    tl.to(aboveFold, { opacity: 1, duration: 0.05, stagger: 0.045 }, streamAt);
    tl.set(belowFold, { opacity: 1 }, streamAt + 0.5);

    // -- Policies load pending, then pass one by one while the stream scrolls
    //    underneath (the one deliberate overlap in the piece).
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

    // -- ALL POLICY PACKS RUN.
    const packsAt = scrollAt + 2.15;
    tl.to(badgeRects[1], { attr: { "stroke-dashoffset": "0" }, duration: 0.4, ease: "power1.inOut" }, packsAt);
    tl.set(badgeRects[1], { attr: { "stroke-dasharray": "none" } }, packsAt + 0.45);
    tl.to(badgeBodies[1], { autoAlpha: 1, duration: 0.3 }, packsAt + 0.15);

    // -- Roll up: the terminal wipes and the shell closes onto the policy
    //    row, parking above the CI pill. The row itself never moves.
    const rollB = packsAt + 0.7;
    tl.to(termClip, { opacity: 0, duration: 0.25 }, rollB - 0.1);
    tl.to(tab, { y: 34, duration: 0.3, ease: "power2.in" }, rollB - 0.1);
    tl.to([bFill, bStroke], { autoAlpha: 0, duration: 0.3 }, rollB);
    tl.to(bOuter, { attr: { y: 421.5, height: 42, rx: 21 }, duration: 0.8, ease: "power2.inOut" }, rollB);

    // -- The plate grows in place; its taller top edge pushes the glyph up.
    const plateAt = rollB + 0.9;
    tl.to(plate, { autoAlpha: 1, scale: 1, duration: 0.6, ease: "power3.out" }, plateAt);
    tl.to(plateDetail, { autoAlpha: 1, duration: 0.4 }, plateAt + 0.15);
    tl.to(glyph, { y: GLYPH_AT_PLATE, duration: 0.5, ease: "power2.out" }, plateAt + 0.05);

    // -- The subnet cubes extrude up out of the plate: the bottom face fades
    //    in flat, then the top face rises while the vertical edges stretch in
    //    lockstep (same ease, both linear in progress, so the corners stay
    //    joined through the overshoot). Each AZ label lands after its cube.
    // DOM order is paint order (us-east-2b sits behind us-east-2a, so it comes
    // first in the markup); data-order carries the left-to-right stagger.
    const cubesAt = plateAt + 0.6;
    cubes.forEach((cube, i) => {
        const at = cubesAt + parseInt(cube.getAttribute("data-order") || String(i), 10) * 0.15;
        tl.to(cube, { autoAlpha: 1, duration: 0.2 }, at);
        tl.to(qa(cube, "[data-cube-top]"), { y: 0, duration: 0.55, ease: "back.out(1.2)" }, at + 0.1);
        tl.to(qa(cube, "[data-cube-edge]"), { scaleY: 1, duration: 0.55, ease: "back.out(1.2)" }, at + 0.1);
        tl.to(cubeLabels[i], { autoAlpha: 1, duration: 0.25 }, at + 0.5);
    });

    // -- Hold on the finished infrastructure, then collapse out and loop.
    const outAt = cubesAt + 1.1 + 2.0;
    tl.to([diagram, aOuter, bOuter, ciRow, ciMerge, badgeTests, badgePolicy, policyRow, glyph], { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, outAt);
    tl.to(root, { autoAlpha: 1, duration: 0.3 }, outAt + 0.5); // beat of dark before the grid returns

    // ------------------------------------------------------------------
    // Visibility: reveal the scene, then only animate while the hero is on
    // screen and the tab is visible.
    // ------------------------------------------------------------------
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
