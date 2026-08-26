/**
 * Guards against new internal links to the retired `/docs/concepts/*` URL
 * space. Those pages moved to `/docs/iac/concepts/*` a while back (see
 * PR #21072), and every few weeks a fresh crop of stale internal links to the
 * old path turns up again in a new content PR, each one a redirect hop for
 * every visitor and crawler that follows it. See PR #21138 and PR #21145 for
 * the most recent cleanup pass.
 *
 * This script scans the site's own content and templates for internal
 * references to `/docs/concepts/...` and fails when it finds one that is not
 * an intentional `aliases:` redirect stub. It is deliberately conservative
 * about what counts as "internal": a link is only flagged when it targets
 * pulumi.com itself, never when `/docs/concepts/` merely happens to appear
 * inside someone else's URL (kubernetes.io, HashiCorp's docs, Okta's docs all
 * have their own unrelated `/docs/concepts/` paths) or inside an unrelated
 * path like an image asset (`/images/docs/concepts/foo.png`).
 *
 * Usage:
 *   node scripts/lint/check-concepts-links.js              # scan the repo
 *   node scripts/lint/check-concepts-links.js <file> ...    # scan specific files
 *   node scripts/lint/check-concepts-links.js --self-test    # run built-in fixtures
 *
 * Exceptions: the ratchet baseline lives in
 * scripts/lint/concepts-links-baseline.json. Once PR #21138 and PR #21145
 * both merge, every entry in that baseline file becomes stale and the whole
 * file (plus its check here) can be deleted -- see the baseline file's own
 * header comment.
 */

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "../..");
const BASELINE_PATH = path.join(__dirname, "concepts-links-baseline.json");

const SCAN_ROOTS = ["content", "layouts", "theme", "assets", "data"];

const EXCLUDED_DIR_SEGMENTS = [
    "node_modules",
    ".git",
    "dist",
    "public",
    "static-prebuilt",
    path.join("theme", "stencil", "www"),
    path.join("theme", "stencil", "dist"),
];

const SCANNABLE_EXTENSIONS = new Set([
    ".md",
    ".mdx",
    ".html",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".yaml",
    ".yml",
]);

const TARGET = "/docs/concepts";

// Characters that can appear inside a URL-ish token (path, query, host).
const URL_CHAR = /[A-Za-z0-9\-._~:/%?&=+]/;

const INTERNAL_HOSTS = new Set(["pulumi.com", "www.pulumi.com"]);

/**
 * Walks backwards from `index` in `line`, returning the start index of the
 * contiguous run of URL-ish characters that `index` sits inside of.
 */
function findTokenStart(line, index) {
    let start = index;
    while (start > 0 && URL_CHAR.test(line[start - 1])) {
        start -= 1;
    }
    return start;
}

/**
 * Decides whether the `/docs/concepts` occurrence at `index` in `line` is an
 * internal Pulumi reference worth flagging.
 */
function isInternalReference(line, index) {
    const tokenStart = findTokenStart(line, index);

    if (tokenStart === index) {
        // Nothing URL-ish immediately precedes it: a bare root-relative
        // reference like `(/docs/concepts/stacks/)` or `href="/docs/concepts/x/"`.
        return true;
    }

    const prefix = line.slice(tokenStart, index);
    const schemeIndex = prefix.indexOf("://");
    if (schemeIndex === -1) {
        // There is a longer path token, but no scheme: this means another
        // path segment sits directly before `/docs/concepts`, e.g.
        // `/images/docs/concepts/foo.png`. That is not our /docs/concepts/*
        // route at all.
        return false;
    }

    const afterScheme = prefix.slice(schemeIndex + 3);
    const host = afterScheme.split("/")[0].toLowerCase();
    return INTERNAL_HOSTS.has(host);
}

/**
 * Finds every `/docs/concepts` occurrence in `line`, returning the internal
 * (flagged) ones. Requires the occurrence to be followed by `/`, end of
 * line, or a small set of terminators, so `/docs/concepts-overview` (a
 * different page) is not matched.
 */
function findInternalOccurrencesInLine(line) {
    const results = [];
    let searchFrom = 0;
    while (true) {
        const idx = line.indexOf(TARGET, searchFrom);
        if (idx === -1) break;
        const after = line[idx + TARGET.length];
        const validTerminator =
            after === undefined || "/\"'`)#? \t,".includes(after);
        if (validTerminator && isInternalReference(line, idx)) {
            results.push(idx);
        }
        searchFrom = idx + TARGET.length;
    }
    return results;
}

/**
 * Scans a single file's text, returning flagged {line, text} entries.
 * Skips occurrences inside a frontmatter `aliases:` block, which are
 * intentional redirect stubs from the old URL to the new one.
 */
function scanFileContent(text) {
    const lines = text.split("\n");
    const violations = [];

    let inFrontmatter = false;
    let frontmatterDelimiters = 0;
    let inAliasesBlock = false;

    for (let i = 0; i < lines.length; i += 1) {
        const line = lines[i];
        const trimmed = line.trim();

        if (i === 0 && trimmed === "---") {
            inFrontmatter = true;
            frontmatterDelimiters = 1;
            continue;
        }
        if (inFrontmatter && trimmed === "---") {
            frontmatterDelimiters += 1;
            if (frontmatterDelimiters >= 2) {
                inFrontmatter = false;
                inAliasesBlock = false;
            }
            continue;
        }

        if (inFrontmatter) {
            if (/^aliases:/i.test(trimmed)) {
                inAliasesBlock = true;
                if (trimmed.includes("[")) {
                    // Inline array form: aliases: [/docs/concepts/x, ...]
                    // The whole line is the aliases declaration itself.
                    continue;
                }
                continue;
            }
            if (inAliasesBlock) {
                if (/^-\s/.test(trimmed) || trimmed === "") {
                    // Still inside the aliases list.
                    continue;
                }
                // A new frontmatter key ends the aliases block.
                inAliasesBlock = false;
            }
        }

        const hits = findInternalOccurrencesInLine(line);
        for (const idx of hits) {
            violations.push({ line: i + 1, text: line.trim() });
        }
    }

    return violations;
}

function shouldSkipDir(fullPath) {
    return EXCLUDED_DIR_SEGMENTS.some(seg =>
        fullPath.split(path.sep).includes(seg) || fullPath.includes(`${path.sep}${seg}${path.sep}`) || fullPath.endsWith(`${path.sep}${seg}`)
    );
}

function walk(dir, out) {
    let entries;
    try {
        entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch (e) {
        return;
    }
    for (const entry of entries) {
        const full = path.join(dir, entry.name);
        if (shouldSkipDir(full)) continue;
        if (entry.isDirectory()) {
            walk(full, out);
        } else if (entry.isFile()) {
            if (SCANNABLE_EXTENSIONS.has(path.extname(entry.name))) {
                out.push(full);
            }
        }
    }
}

function collectDefaultFiles() {
    const files = [];
    for (const root of SCAN_ROOTS) {
        walk(path.join(REPO_ROOT, root), files);
    }
    return files;
}

function loadBaseline() {
    try {
        const parsed = JSON.parse(fs.readFileSync(BASELINE_PATH, "utf8"));
        return parsed.files || {};
    } catch (e) {
        return {};
    }
}

function relativePath(filePath) {
    return path.relative(REPO_ROOT, filePath).split(path.sep).join("/");
}

function runScan(files) {
    /** @type {Map<string, {line: number, text: string}[]>} */
    const byFile = new Map();
    for (const file of files) {
        let text;
        try {
            text = fs.readFileSync(file, "utf8");
        } catch (e) {
            continue;
        }
        const violations = scanFileContent(text);
        if (violations.length > 0) {
            byFile.set(relativePath(file), violations);
        }
    }
    return byFile;
}

function main() {
    const args = process.argv.slice(2);

    if (args.includes("--self-test")) {
        return runSelfTest();
    }

    const printBaseline = args.includes("--print-baseline");
    const explicitFiles = args.filter(a => !a.startsWith("--"));
    const files =
        explicitFiles.length > 0
            ? explicitFiles.map(f => path.resolve(process.cwd(), f))
            : collectDefaultFiles();

    const byFile = runScan(files);

    if (printBaseline) {
        const counts = {};
        for (const [file, violations] of byFile.entries()) {
            counts[file] = violations.length;
        }
        console.log(JSON.stringify(counts, Object.keys(counts).sort(), 4));
        return;
    }

    const baseline = loadBaseline();

    let failed = false;
    const staleFiles = [];

    for (const [file, violations] of byFile.entries()) {
        const allowed = baseline[file] || 0;
        console.log(`\n${file} (${violations.length} occurrence(s), ${allowed} allowed by baseline):`);
        for (const v of violations) {
            console.log(`  ${file}:${v.line}: ${v.text}`);
        }
        if (violations.length > allowed) {
            failed = true;
        }
    }

    for (const [file, allowed] of Object.entries(baseline)) {
        const found = byFile.get(file);
        const foundCount = found ? found.length : 0;
        if (foundCount < allowed) {
            staleFiles.push(`${file}: baseline allows ${allowed}, found ${foundCount}`);
        }
    }

    if (staleFiles.length > 0) {
        console.log(
            "\nWarning: the following baseline entries are stale (fewer occurrences than recorded) -- please prune scripts/lint/concepts-links-baseline.json:"
        );
        for (const line of staleFiles) {
            console.log(`  ${line}`);
        }
    }

    if (failed) {
        console.log(
            "\nFound new internal link(s) to the retired /docs/concepts/* URL space.\n" +
                "Fix: point the link at the current /docs/iac/concepts/... path instead " +
                "of the old /docs/concepts/... path (a redirect covers old links, but " +
                "every hop costs a round trip for readers and crawlers).\n" +
                "If this is an intentional exception, add it to scripts/lint/concepts-links-baseline.json " +
                "with a comment explaining why."
        );
        process.exit(1);
    }

    console.log("\nNo new /docs/concepts/* internal links found.");
}

function runSelfTest() {
    const cases = [
        { text: "See [stacks](/docs/concepts/stacks/) for more.", expectViolations: 1 },
        { text: "[ref]: /docs/concepts/resources/", expectViolations: 1 },
        { text: '<a href="/docs/concepts/x/">link</a>', expectViolations: 1 },
        { text: "Read https://www.pulumi.com/docs/concepts/stacks/ for details.", expectViolations: 1 },
        { text: "See https://kubernetes.io/docs/concepts/x/ for the upstream docs.", expectViolations: 0 },
        { text: "See https://developer.hashicorp.com/vault/docs/concepts/policies for details.", expectViolations: 0 },
        { text: "See https://developer.okta.com/docs/concepts/scim/ for details.", expectViolations: 0 },
        { text: "![diagram](/images/docs/concepts/stack-config-tags.png)", expectViolations: 0 },
    ];

    const frontmatterCase = [
        "---",
        "title: Something",
        "aliases:",
        "- /docs/concepts/config",
        "- /docs/concepts/config/",
        "---",
        "Body text with no links.",
    ].join("\n");

    let ok = true;

    for (const c of cases) {
        const found = scanFileContent(c.text).length;
        const pass = found === c.expectViolations;
        if (!pass) ok = false;
        console.log(`[${pass ? "PASS" : "FAIL"}] "${c.text}" -> ${found} (expected ${c.expectViolations})`);
    }

    const frontmatterFound = scanFileContent(frontmatterCase).length;
    const frontmatterPass = frontmatterFound === 0;
    if (!frontmatterPass) ok = false;
    console.log(
        `[${frontmatterPass ? "PASS" : "FAIL"}] aliases frontmatter block -> ${frontmatterFound} (expected 0)`
    );

    if (!ok) {
        console.log("\nSelf-test FAILED.");
        process.exit(1);
    }
    console.log("\nSelf-test passed.");
}

main();
