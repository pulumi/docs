// Regenerates the colored text runs in data/hero_agent_loop.yaml from the
// plain-text sources at the top of that file, using shiki with the min-light
// theme (TypeScript for the editor, bash for the terminal) — the same
// highlighting the design's storyboards used. Run with:
//
//   yarn --cwd theme gen:hero-text
//
// shiki is a devDependency used only here; nothing from it ships in a bundle.

import { createHighlighter } from "shiki";
import fs from "fs";

const FILE = new URL("../../data/hero_agent_loop.yaml", import.meta.url).pathname;

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
};
const COLOR_NOTES = {
    kw: "keywords",
    id: "identifiers, numbers",
    str: "strings",
    mem: "members, methods; terminal commands",
    txt: "plain text",
    pun: "punctuation",
    tbl: "terminal arguments, table text",
};

function literalBlock(src, key) {
    const re = new RegExp(`^${key}: \\|\\n((?:  .*\\n|\\n)*)`, "m");
    const m = src.match(re);
    if (!m) {
        throw new Error(`missing "${key}: |" block in ${FILE}`);
    }
    return m[1].replace(/^  /gm, "").replace(/\n$/, "");
}

function normalizeColor(color) {
    return (color || "#24292E").toUpperCase().replace(/FF$/, "");
}

function toRuns(highlighter, code, lang, palette) {
    const { tokens } = highlighter.codeToTokens(code, { lang, theme: "min-light" });
    return tokens.map(line => {
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
}

function yamlSection(name, lines) {
    const buf = [`${name}:`];
    for (const line of lines) {
        if (!line.length) {
            buf.push("  - []");
            continue;
        }
        buf.push(`  - - [${line[0][0]}, ${JSON.stringify(line[0][1])}]`);
        for (const item of line.slice(1)) {
            buf.push(`    - [${item[0]}, ${JSON.stringify(item[1])}]`);
        }
    }
    return buf.join("\n");
}

const src = fs.readFileSync(FILE, "utf8");
const editorSource = literalBlock(src, "editor_source");
const terminalSource = literalBlock(src, "terminal_source");

function trimTrailingBlanks(lines) {
    while (lines.length && !lines[lines.length - 1].length) {
        lines.pop();
    }
    return lines;
}

const highlighter = await createHighlighter({ themes: ["min-light"], langs: ["ts", "bash"] });
const palette = {};
const editor = trimTrailingBlanks(toRuns(highlighter, editorSource, "ts", palette));
const terminal = trimTrailingBlanks(toRuns(highlighter, terminalSource, "bash", palette));

const colors = ["colors:"].concat(Object.keys(palette).map(key => `  ${key}: "${palette[key]}"${COLOR_NOTES[key] ? " # " + COLOR_NOTES[key] : ""}`)).join("\n");

const cut = src.indexOf("\ncolors:");
if (cut === -1) {
    throw new Error(`missing "colors:" section in ${FILE}`);
}
const head = src.slice(0, cut + 1);
fs.writeFileSync(FILE, head + colors + "\n\n" + yamlSection("editor", editor) + "\n\n" + yamlSection("terminal", terminal) + "\n");
console.log(`wrote ${FILE}: ${editor.length} editor rows, ${terminal.length} terminal rows, ${Object.keys(palette).length} colors`);
