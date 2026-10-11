// Regenerates the colored text runs in data/hero_agent_loop.yaml from the
// plain-text sources at the top of that file, using shiki — each editor
// language's own grammar, bash for the terminal — under whichever theme that
// file's "dark_code:" flag selects. Run with:
//
//   yarn --cwd theme gen:hero-text
//
// shiki is a devDependency used only here; nothing from it ships in a bundle.

import { createHighlighter } from "shiki";
import fs from "fs";

const FILE = new URL("../../data/hero_agent_loop.yaml", import.meta.url).pathname;
const OUT_FILE = new URL("../../data/hero_agent_loop_generated.yaml", import.meta.url).pathname;

const SHIKI_LANGS = {
    typescript: "ts",
    python: "python",
    go: "go",
    csharp: "csharp",
    java: "java",
    hcl: "hcl",
    yaml: "yaml",
};

// The two code treatments, chosen by "dark_code:" in data/hero_agent_loop.yaml.
// Each names a shiki theme plus stable, readable keys for the colors that theme
// actually produces on our sources; anything new falls back to a hex-derived
// key. Only the syntax colors live here — the panel the code sits on is the
// hero partial's business, keyed off the dark_code flag this script copies into
// the generated file.
const THEMES = {
    light: {
        shiki: "min-light",
        keys: {
            "#D32F2F": "kw",
            "#1976D2": "id",
            "#22863A": "str",
            "#6F42C1": "mem",
            "#24292E": "txt",
            "#212121": "pun",
            "#2B5581": "tbl",
            "#C2C3C5": "dim",
        },
        notes: {
            kw: "keywords",
            id: "identifiers, numbers",
            str: "strings",
            mem: "members, methods; terminal commands",
            txt: "plain text",
            pun: "punctuation",
            tbl: "terminal arguments, table text",
            dim: "comments, faint punctuation",
        },
    },
    dark: {
        shiki: "min-dark",
        keys: {
            "#F97583": "kw",
            "#79B8FF": "id",
            "#FFAB70": "str",
            "#B392F0": "mem",
            "#F8F8F8": "txt",
            "#BBBBBB": "pun",
            "#9DB1C5": "tbl",
            "#6A737D": "dim",
        },
        notes: {
            kw: "keywords",
            id: "numbers, operators",
            str: "strings",
            mem: "identifiers, members; terminal commands",
            txt: "plain text",
            pun: "punctuation",
            tbl: "terminal arguments, table text",
            dim: "comments, faint punctuation",
        },
    },
};

function editorSources(src) {
    const section = src.match(/^editor_sources:\n([\s\S]*?)(?=^\w)/m);
    if (!section) {
        throw new Error(`missing "editor_sources:" section in ${FILE}`);
    }
    const out = {};
    const re = /^  (\w+): \|\n((?:    .*\n|\n)*)/gm;
    let m;
    while ((m = re.exec(section[1]))) {
        out[m[1]] = m[2].replace(/^    /gm, "").replace(/\n+$/, "");
    }
    return out;
}

function terminalSource(src) {
    const m = src.match(/^terminal_source: \|\n((?:  .*\n|\n)*)/m);
    if (!m) {
        throw new Error(`missing "terminal_source: |" block in ${FILE}`);
    }
    return m[1].replace(/^  /gm, "").replace(/\n+$/, "");
}

function darkCode(src) {
    const m = src.match(/^dark_code: *(true|false) *$/m);
    if (!m) {
        throw new Error(`missing "dark_code: true|false" in ${FILE}`);
    }
    return m[1] === "true";
}

// shiki hands back either #RRGGBB or #RRGGBBAA; drop a fully opaque alpha but
// leave a six-digit color that merely ends in FF alone.
function normalizeColor(color, fallback) {
    return (color || fallback).toUpperCase().replace(/^(#[0-9A-F]{6})FF$/, "$1");
}

function toRuns(highlighter, code, lang, palette) {
    const { tokens, fg } = highlighter.codeToTokens(code, { lang, theme: THEME.shiki });
    const lines = tokens.map(line => {
        const chars = [];
        for (const token of line) {
            for (const ch of token.content) {
                chars.push({ ch, color: ch === " " ? null : normalizeColor(token.color, fg) });
            }
        }
        while (chars.length && chars[chars.length - 1].ch === " ") {
            chars.pop();
        }
        // Segments are [colorKey, startColumn, text] and never begin with a
        // space or contain runs of 2+ spaces: hugo --minify collapses
        // whitespace inside the tspans, so indentation and column alignment
        // must live in explicit column offsets, with only single interior
        // spaces (which the minifier preserves) inside a segment.
        const runs = [];
        let i = 0;
        while (i < chars.length) {
            if (chars[i].ch === " ") {
                i++;
                continue;
            }
            const color = chars[i].color;
            const start = i;
            let text = "";
            let j = i;
            while (j < chars.length) {
                const c = chars[j];
                if (c.ch !== " ") {
                    if (c.color !== color) {
                        break;
                    }
                    text += c.ch;
                    j++;
                } else if (j + 1 < chars.length && chars[j + 1].ch !== " " && chars[j + 1].color === color) {
                    text += " ";
                    j++;
                } else {
                    break;
                }
            }
            let key = THEME.keys[color];
            if (!key) {
                key = "c" + color.slice(1);
                THEME.keys[color] = key;
            }
            palette[key] = color;
            runs.push([key, start, text]);
            i = j;
        }
        return runs;
    });
    while (lines.length && !lines[lines.length - 1].length) {
        lines.pop();
    }
    return lines;
}

function yamlLines(lines, indent) {
    const buf = [];
    for (const line of lines) {
        if (!line.length) {
            buf.push(`${indent}- []`);
            continue;
        }
        buf.push(`${indent}- - [${line[0][0]}, ${line[0][1]}, ${JSON.stringify(line[0][2])}]`);
        for (const item of line.slice(1)) {
            buf.push(`${indent}  - [${item[0]}, ${item[1]}, ${JSON.stringify(item[2])}]`);
        }
    }
    return buf.join("\n");
}

const src = fs.readFileSync(FILE, "utf8");
const dark = darkCode(src);
const THEME = THEMES[dark ? "dark" : "light"];
const sources = editorSources(src);
const terminal = terminalSource(src);

const highlighter = await createHighlighter({
    themes: [THEME.shiki],
    langs: Object.keys(SHIKI_LANGS)
        .map(l => SHIKI_LANGS[l])
        .concat(["bash"]),
});

const palette = {};
const editorSections = [];
for (const lang of Object.keys(sources)) {
    const shikiLang = SHIKI_LANGS[lang];
    if (!shikiLang) {
        throw new Error(`no shiki lang mapping for "${lang}"`);
    }
    const lines = toRuns(highlighter, sources[lang], shikiLang, palette);
    if (lines.length > 13) {
        throw new Error(`${lang} example is ${lines.length} rows; the code panel fits 13`);
    }
    editorSections.push(`  ${lang}:\n` + yamlLines(lines, "    "));
}
const terminalRuns = toRuns(highlighter, terminal, "bash", palette);

const colors = ["colors:"].concat(Object.keys(palette).map(key => `  ${key}: "${palette[key]}"${THEME.notes[key] ? " # " + THEME.notes[key] : ""}`)).join("\n");

const HEADER =
    "# GENERATED FILE — DO NOT EDIT.\n" +
    "# Written by theme/scripts/gen-hero-text.mjs from the plain-text sources in\n" +
    "# data/hero_agent_loop.yaml; edit those and run\n" +
    "#   yarn --cwd theme gen:hero-text\n" +
    "#\n" +
    "# dark_code mirrors the flag in the source file: it picked the shiki theme\n" +
    "# these colors come from, and the hero partial reads it to paint the panel\n" +
    "# they sit on, so the two can never disagree.\n" +
    "#\n" +
    "# Runs are [color, startColumn, text] segments; _code-lines.html positions\n" +
    "# each from its column offset (Monaspace Neon, 7.44141px advance at\n" +
    "# font-size 12). Segment text carries no leading or doubled spaces, since\n" +
    "# the production build's HTML minifier collapses whitespace inside tspans.\n";

fs.writeFileSync(
    OUT_FILE,
    HEADER + "\ndark_code: " + dark + "\n\n" + colors + "\n\neditors:\n" + editorSections.join("\n") + "\n\nterminal:\n" + yamlLines(terminalRuns, "  ") + "\n",
);
console.log(`wrote ${OUT_FILE}: ${THEME.shiki}, ${Object.keys(sources).length} editors, ${terminalRuns.length} terminal rows, ${Object.keys(palette).length} colors`);
