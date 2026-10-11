// Joins soft-wrapped paragraph lines in generated markdown output files.
//
// Markdown treats a single newline within a paragraph as a space when rendered
// to HTML, but terminal markdown renderers (like glamour) display lines as-is.
// This causes awkward word wrapping when the source content was hard-wrapped at
// 80 columns. This script joins those soft-wrapped lines into single long lines
// while preserving code blocks, blank lines, and block-level elements.

const fs = require("fs");
const path = require("path");
const glob = require("glob");

const docsDir = path.resolve(__dirname, "../public/docs");
const pattern = path.join(docsDir, "**/index.md");
const files = glob.sync(pattern);

let totalFixed = 0;

for (const file of files) {
    const original = fs.readFileSync(file, "utf8");
    const result = joinParagraphLines(original);

    if (result !== original) {
        fs.writeFileSync(file, result, "utf8");
        totalFixed++;
    }
}

console.log(`Joined soft-wrapped lines in ${totalFixed} of ${files.length} markdown files.`);

function joinParagraphLines(content) {
    const lines = content.split("\n");
    const output = [];
    let inCodeBlock = false;
    let inFrontmatter = false;
    let lineIndex = 0;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        // Track YAML frontmatter (--- delimited at start of file).
        if (i === 0 && line === "---") {
            inFrontmatter = true;
            output.push(line);
            continue;
        }
        if (inFrontmatter) {
            output.push(line);
            if (line === "---") {
                inFrontmatter = false;
            }
            continue;
        }

        // Track fenced code blocks.
        if (line.startsWith("```")) {
            inCodeBlock = !inCodeBlock;
            output.push(line);
            continue;
        }

        // Inside code blocks, preserve lines exactly.
        if (inCodeBlock) {
            output.push(line);
            continue;
        }

        // Blank lines: preserve as-is (paragraph breaks).
        if (line.trim() === "") {
            output.push(line);
            continue;
        }

        // Block-level elements that must start on their own line.
        if (isBlockElement(line)) {
            output.push(line);
            continue;
        }

        // Paragraph continuation: join with the previous line if it was also
        // a prose line (not blank, not a block element, not a code fence).
        const prev = output.length > 0 ? output[output.length - 1] : null;
        if (prev !== null && prev.trim() !== "" && !isBlockElement(prev) && !prev.startsWith("```")) {
            // Join: replace the previous line with the concatenation.
            output[output.length - 1] = prev + " " + line;
        } else {
            output.push(line);
        }
    }

    return output.join("\n");
}

function isBlockElement(line) {
    // Headings
    if (line.startsWith("#")) return true;
    // Blockquotes
    if (line.startsWith(">")) return true;
    // Unordered list items
    if (/^[\-*+] /.test(line)) return true;
    // Ordered list items
    if (/^\d+\. /.test(line)) return true;
    // Tables
    if (line.startsWith("|")) return true;
    // HTML comments (chooser delimiters)
    if (line.startsWith("<!--")) return true;
    // Horizontal rules
    if (/^(-{3,}|\*{3,}|_{3,})$/.test(line)) return true;

    return false;
}
