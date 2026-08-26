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
 * path like an image asset (`/images/docs/concepts/foo.png`). It also skips
 * webpack's own generated JS bundles under static/js/ -- a stale link
 * surviving in the compiled output was already caught in its
 * theme/src/**\/*.ts source, which this guard scans directly -- but only
 * when git itself confirms the specific path is ignored build output, not
 * merely by filename pattern, since a few checked-in files under
 * static/js/ happen to match the same naming convention. See
 * `isGeneratedBundle` for the full rationale. (Generated CSS isn't in scope
 * either way: `SCANNABLE_EXTENSIONS` below has no `.css` entry, so `walk()`
 * never reaches a stylesheet, generated or hand-authored.)
 *
 * Usage:
 *   node scripts/lint/check-concepts-links.js              # scan the repo
 *   node scripts/lint/check-concepts-links.js <file> ...    # scan specific files
 *   node scripts/lint/check-concepts-links.js --self-test    # run built-in fixtures
 *   node scripts/lint/check-concepts-links.js --print-baseline  # print a fresh
 *       baseline (in the same {_note, files} envelope loadBaseline() reads) for
 *       every currently-scanned file with a violation
 *
 * Exceptions: the ratchet baseline lives in
 * scripts/lint/concepts-links-baseline.json. PR #21138 and PR #21145 both
 * merged, so it is empty today ({}) -- any new entry is a fresh, justified
 * exception, not leftover cleanup debt. See the baseline file's own header
 * comment.
 */

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const REPO_ROOT = path.resolve(__dirname, "../..");
const BASELINE_PATH = path.join(__dirname, "concepts-links-baseline.json");

const SCAN_ROOTS = ["content", "layouts", "theme", "assets", "data", "archetypes", "static", "scripts"];

const EXCLUDED_DIR_SEGMENTS = [
    "node_modules",
    ".git",
    "dist",
    "public",
    "static-prebuilt",
    path.join("theme", "stencil", "www"),
    path.join("theme", "stencil", "dist"),
];

// This guard's own source file: its doc comments, usage examples, and
// --self-test fixtures all contain the literal string /docs/concepts/ on
// purpose, and scanning it would be 100% self-referential noise, not a
// real link anyone will ever click. Scoped to this one file rather than
// all of scripts/lint/, so lint-markdown.js and any future script in that
// directory that emits a genuine doc URL are still scanned; and checked in
// runScan() (both the repo-walk and the explicit-file entry points) rather
// than shouldSkipDir()/walk(), so `node check-concepts-links.js
// scripts/lint/check-concepts-links.js` agrees with a full-repo run instead
// of reporting ~20 violations against the script's own fixtures.
// relativePath() always joins with "/" regardless of platform, so this set
// uses a literal posix-style path rather than path.join (which would emit
// "\\" on Windows and never match).
const EXCLUDED_FILES = new Set(["scripts/lint/check-concepts-links.js"]);

// Webpack writes its build output into static/js/ under content-hashed
// names (see .gitignore's own "webpack-generated JS entry bundles" section
// for the canonical list of these patterns). Those files are never authored
// by hand -- they are compiled from theme/src/ts/*.ts, which this guard
// already scans directly -- and CI runs `make build` before `make lint`, so
// a stale-link string surviving only in the *source* TypeScript would still
// be caught there. Scanning the generated bundle too would flag the same
// defect twice under a filename that changes on every build (the content
// hash), which a baseline entry can never pin down. Skip them by filename
// pattern rather than by excluding all of static/js outright, since that
// directory also holds genuine hand-authored, git-tracked files (e.g.
// static/js/pulumi-mermaid-theme.js) that should still be scanned.
// (.gitignore also lists a `styles.*.css` bundle under static/css/, but
// SCANNABLE_EXTENSIONS below has no `.css` entry -- walk() never reaches a
// stylesheet at all, generated or not -- so that pattern and a static/css
// directory entry would both be unreachable dead code here. Omitted
// rather than carried along for symmetry; see SCANNABLE_EXTENSIONS if CSS
// scanning is ever added.)
//
// A filename pattern alone is not proof a given file is actually generated:
// static/js/consent-manager.cbf13435.js, static/js/consent-manager.e2d01ae6.js,
// static/js/marketing-homepage.31d6cfe0.js, and
// static/js/marketing-homepage.46f9fbff.js are all git-tracked on master today
// (confirmed via the GitHub contents API, since a shallow CI checkout makes
// `git log` attribute every file to the tip commit and can't tell you this) --
// they are not regenerated by `make build`, so this guard is their only
// checkpoint. Trust the same source of truth the pattern list already claims
// to mirror -- .gitignore -- over the pattern alone: a name match only skips
// the file when `git check-ignore` also treats the path as build output. The
// directory restriction additionally keeps a loose pattern like
// /^chunk-.*\.js$/ from reaching outside static/js into the other seven scan
// roots.
const GENERATED_BUNDLE_DIRS = new Set(["static/js"]);

const GENERATED_BUNDLE_PATTERNS = [
    /^bundle\.(min\.)?[0-9a-f]+\.js$/,
    /^algolia\.[0-9a-f]+\.js$/,
    /^marketing(-homepage)?\.[0-9a-f]+\.js$/,
    /^homepage\.[0-9a-f]+\.js$/,
    /^chunk-.*\.js$/,
    /^consent-manager\.[0-9a-f]+\.js$/,
    /^header-nav\.[0-9a-f]+\.js$/,
];

/**
 * True when `fullPath` both looks like a generated bundle (by directory and
 * filename pattern) and git itself treats it as ignored build output. Takes
 * an injectable `checkIgnore` so --self-test can exercise this against a
 * throwaway repo instead of the real one.
 */
function isGeneratedBundle(fullPath, checkIgnore = gitCheckIgnore) {
    const rel = relativePath(fullPath);
    const dir = path.posix.dirname(rel);
    if (!GENERATED_BUNDLE_DIRS.has(dir)) return false;
    const base = path.posix.basename(rel);
    if (!GENERATED_BUNDLE_PATTERNS.some((re) => re.test(base))) return false;
    return checkIgnore(fullPath);
}

/**
 * Shells out to `git check-ignore` to ask whether git's own rules (the same
 * .gitignore this guard's rationale already leans on) treat `fullPath` as
 * generated/ignored output. `check-ignore` exits 0 when ignored and 1 when
 * not -- both are expected outcomes, not errors. Any other exit (missing
 * git, not a repo, etc.) fails closed: treat the file as NOT ignored so it
 * still gets scanned rather than silently skipped.
 */
function gitCheckIgnore(fullPath) {
    try {
        execFileSync("git", ["-C", REPO_ROOT, "check-ignore", "-q", "--", fullPath], {
            stdio: "ignore",
        });
        return true;
    } catch (e) {
        // Two distinct failures land here and are deliberately not told
        // apart by return value: exit 1 ("git says this path is not
        // ignored", the routine case for every hand-authored file) and any
        // other outcome (git missing from PATH, not a work tree, spawn
        // failure). Both fail closed to `false` -- scan the file rather
        // than silently skip it -- but an atypical failure still deserves
        // a one-line signal on stderr so a red build in an environment
        // without git points at its actual cause instead of looking like
        // ~30 ordinary stale-link violations in files nobody touched.
        if (!(typeof e.status === "number" && e.status === 1)) {
            console.warn(`check-concepts-links: \`git check-ignore\` failed unexpectedly for ${fullPath}: ${e.message}`);
        }
        return false;
    }
}

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
            if (SCANNABLE_EXTENSIONS.has(path.extname(entry.name)) && !isGeneratedBundle(full)) {
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

const DEFAULT_BASELINE_NOTE =
    "Ratchet baseline for scripts/lint/check-concepts-links.js. Every entry here " +
    "is a KNOWN, already-fixed occurrence of an internal link to the retired " +
    "/docs/concepts/* URL space, tracked while its fix is still open for review. " +
    "Once the fix merges, that entry drops to 0 real occurrences and should be " +
    "pruned. Do not add new entries here to silence a real finding -- fix the " +
    "link instead. A file's count going lower than what is recorded here only " +
    "prints a warning, never fails; going higher fails the build. Note: this is " +
    "a count-only ratchet, not a line-level one -- swapping one stale link for a " +
    "different stale link in the same file keeps the count unchanged and passes.";

function loadBaseline() {
    try {
        const parsed = JSON.parse(fs.readFileSync(BASELINE_PATH, "utf8"));
        return parsed.files || {};
    } catch (e) {
        return {};
    }
}

function loadBaselineNote() {
    try {
        const parsed = JSON.parse(fs.readFileSync(BASELINE_PATH, "utf8"));
        return parsed._note || DEFAULT_BASELINE_NOTE;
    } catch (e) {
        return DEFAULT_BASELINE_NOTE;
    }
}

function relativePath(filePath) {
    return path.relative(REPO_ROOT, filePath).split(path.sep).join("/");
}

function runScan(files) {
    /** @type {Map<string, {line: number, text: string}[]>} */
    const byFile = new Map();
    for (const file of files) {
        const rel = relativePath(file);
        if (EXCLUDED_FILES.has(rel)) continue;
        let text;
        try {
            text = fs.readFileSync(file, "utf8");
        } catch (e) {
            continue;
        }
        const violations = scanFileContent(text);
        if (violations.length > 0) {
            byFile.set(rel, violations);
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
    const explicitFiles = args.filter(a => !a.startsWith("--")).map(f => path.resolve(process.cwd(), f));
    // Apply the same generated-bundle exclusion whichever way files were
    // selected, so `node check-concepts-links.js static/js/bundle.<hash>.js`
    // and a full repo walk agree on what counts as scannable.
    const files =
        explicitFiles.length > 0 ? explicitFiles.filter(f => !isGeneratedBundle(f)) : collectDefaultFiles();

    const byFile = runScan(files);

    if (printBaseline) {
        const counts = {};
        for (const file of [...byFile.keys()].sort()) {
            counts[file] = byFile.get(file).length;
        }
        console.log(JSON.stringify({ _note: loadBaselineNote(), files: counts }, null, 4));
        return;
    }

    const baseline = loadBaseline();

    let failed = false;
    const staleFiles = [];
    const overLimitReport = [];

    for (const [file, violations] of byFile.entries()) {
        const allowed = baseline[file] || 0;
        if (violations.length > allowed) {
            failed = true;
            overLimitReport.push({ file, violations, allowed });
        }
    }

    for (const [file, allowed] of Object.entries(baseline)) {
        const found = byFile.get(file);
        const foundCount = found ? found.length : 0;
        if (foundCount < allowed) {
            staleFiles.push(`${file}: baseline allows ${allowed}, found ${foundCount}`);
        }
    }

    if (!failed) {
        // Green run: a single summary line. The full per-file, per-occurrence
        // detail below is only useful when something needs fixing, and
        // printing it every time on every passing run buries that signal
        // under ~50+ lines of baselined-and-fine noise.
        console.log(
            `No new /docs/concepts/* internal links found (${byFile.size} file(s) with baselined occurrences, all within their allowance).`
        );
    } else {
        for (const { file, violations, allowed } of overLimitReport) {
            console.log(`\n${file} (${violations.length} occurrence(s), ${allowed} allowed by baseline):`);
            for (const v of violations) {
                console.log(`  ${file}:${v.line}: ${v.text}`);
            }
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

    // isGeneratedBundle takes an injectable checkIgnore so these run against
    // a fake git-ignore answer instead of shelling out to the real repo --
    // fast, hermetic, and able to cover both an actually-generated bundle
    // and a checked-in file that merely matches the naming pattern (the
    // real-world case of static/js/consent-manager.<hash>.js, which is
    // git-tracked, not build output).
    const bundleCases = [
        {
            desc: "gitignored bundle under static/js/ matching the pattern",
            fullPath: path.join(REPO_ROOT, "static", "js", "bundle.b15c1961.js"),
            checkIgnore: () => true,
            expectGenerated: true,
        },
        {
            desc: "git-tracked file under static/js/ that merely matches the pattern",
            fullPath: path.join(REPO_ROOT, "static", "js", "consent-manager.cbf13435.js"),
            checkIgnore: () => false,
            expectGenerated: false,
        },
        {
            desc: "pattern match outside static/js is never generated",
            fullPath: path.join(REPO_ROOT, "content", "blog", "chunk-abc.js"),
            checkIgnore: () => true,
            expectGenerated: false,
        },
        {
            desc: "hand-authored file under static/js/ that doesn't match any pattern",
            fullPath: path.join(REPO_ROOT, "static", "js", "pulumi-mermaid-theme.js"),
            checkIgnore: () => true,
            expectGenerated: false,
        },
    ];

    for (const c of bundleCases) {
        const got = isGeneratedBundle(c.fullPath, c.checkIgnore);
        const pass = got === c.expectGenerated;
        if (!pass) ok = false;
        console.log(`[${pass ? "PASS" : "FAIL"}] ${c.desc} -> ${got} (expected ${c.expectGenerated})`);
    }

    if (!ok) {
        console.log("\nSelf-test FAILED.");
        process.exit(1);
    }
    console.log("\nSelf-test passed.");
}

main();
