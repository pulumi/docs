// Regenerates the colored text runs in data/hero_agent_loop.yaml from the
// plain-text sources at the top of that file, using shiki with the min-light
// theme — each editor language's own grammar, bash for the terminal — the
// same highlighting the design's storyboards used. Run with:
//
//   yarn --cwd theme gen:hero-text
//
// shiki is a devDependency used only here; nothing from it ships in a bundle.

import { createHighlighter } from "shiki";
import fs from "fs";

const FILE = new URL("../../data/hero_agent_loop.yaml", import.meta.url).pathname;

const SHIKI_LANGS = {
    typescript: "ts",
    python: "python",
    go: "go",
    csharp: "csharp",
    java: "java",
    hcl: "hcl",
    yaml: "yaml",
};

// Stable, readable keys for min-light's palette; anything new falls back to a
// hex-derived key.
const COLOR_KEYS = {
    "#D32F2F": "kw",
    "#1976D2": "id",
    "#22863A": "str",
    "#6F42C1": "mem",
    "#24292E": "txt",
    "#212121": "pun",
    "#2B5581": "tbl",
    "#C2C3C5": "dim",
};
const COLOR_NOTES = {
    kw: "keywords",
    id: "identifiers, numbers",
    str: "strings",
    mem: "members, methods; terminal commands",
    txt: "plain text",
    pun: "punctuation",
    tbl: "terminal arguments, table text",
    dim: "comments, faint punctuation",
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

function normalizeColor(color) {
    return (color || "#24292E").toUpperCase().replace(/FF$/, "");
}

function toRuns(highlighter, code, lang, palette) {
    const { tokens } = highlighter.codeToTokens(code, { lang, theme: "min-light" });
    const lines = tokens.map(line => {
        // Per-character colors, spaces unassigned, trailing whitespace dropped.
        const chars = [];
        for (const token of line) {
            for (const ch of token.content) {
                chars.push({ ch, color: ch === " " ? null : normalizeColor(token.color) });
            }
        }
        while (chars.length && chars[chars.length - 1].color === null) {
            chars.pop();
        }
        // Spaces join the run that follows them, matching the hand-authored
        // leading-pad style the renderer has always consumed.
        for (let i = chars.length - 1; i >= 0; i--) {
            if (chars[i].color === null) {
                chars[i].color = chars[i + 1] ? chars[i + 1].color : null;
            }
        }
        const runs = [];
        for (const c of chars) {
            let key = COLOR_KEYS[c.color];
            if (!key) {
                key = "c" + c.color.slice(1);
                COLOR_KEYS[c.color] = key;
            }
            palette[key] = c.color;
            const last = runs[runs.length - 1];
            if (last && last[0] === key) {
                last[1] += c.ch;
            } else {
                runs.push([key, c.ch]);
            }
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
        buf.push(`${indent}- - [${line[0][0]}, ${JSON.stringify(line[0][1])}]`);
        for (const item of line.slice(1)) {
            buf.push(`${indent}  - [${item[0]}, ${JSON.stringify(item[1])}]`);
        }
    }
    return buf.join("\n");
}

const src = fs.readFileSync(FILE, "utf8");
const sources = editorSources(src);
const terminal = terminalSource(src);

const highlighter = await createHighlighter({
    themes: ["min-light"],
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

const colors = ["colors:"].concat(Object.keys(palette).map(key => `  ${key}: "${palette[key]}"${COLOR_NOTES[key] ? " # " + COLOR_NOTES[key] : ""}`)).join("\n");

const cut = src.indexOf("\ncolors:");
if (cut === -1) {
    throw new Error(`missing "colors:" section in ${FILE}`);
}
const head = src.slice(0, cut + 1);
fs.writeFileSync(FILE, head + colors + "\n\neditors:\n" + editorSections.join("\n") + "\n\nterminal:\n" + yamlLines(terminalRuns, "  ") + "\n");
console.log(`wrote ${FILE}: ${Object.keys(sources).length} editors, ${terminalRuns.length} terminal rows, ${Object.keys(palette).length} colors`);
