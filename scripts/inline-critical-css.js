const fs = require("fs");
const Beasties = require("beasties");

// Curated allowlist, not a blanket public/**/*.html glob: critical-CSS extraction
// costs real build time per page (docs pages with large nav trees run noticeably
// slower than short marketing pages), so this list is bounded to pages that
// actually carry organic sessions today, prioritized by search-console click
// volume and capped to keep the added build step well under a couple of minutes.
//
// This list is kept current by a scheduled automated check (monthly), not by
// informal habit: it pulls Search Console click data, compares it against this
// array, and opens a pull request proposing additions/removals when the top-
// traffic set has drifted. That PR is reviewed and merged by a human like any
// other change here; the automation proposes, it never merges its own diff.
// The warning below (when most of this list goes missing from a build) is a
// second, independent signal of drift between scheduled runs.
const pages = [
    "public/index.html",
    "public/docs/iac/comparisons/terraform/index.html",
    "public/docs/install/index.html",
    "public/blog/top-8-claude-skills-devops-2026/index.html",
    "public/pricing/index.html",
    "public/blog/claude-code-orchestration-frameworks/index.html",
    "public/careers/index.html",
    "public/docs/iac/concepts/state-and-backends/index.html",
    "public/docs/iac/concepts/secrets/index.html",
    "public/docs/index.html",
    "public/product/neo/index.html",
    "public/what-is/opentofu-vs-terraform/index.html",
    "public/docs/iac/cli/index.html",
    "public/docs/iac/concepts/stacks/index.html",
];

async function inlineCriticalCSS() {
    const beasties = new Beasties({
        path: "public/",
        preload: "swap",
        reduceInlineStyles: true,
        // Keep original CSS files intact; the full stylesheet is still loaded
        // async so uncovered rules still apply after page load.
        pruneSource: false,
    });

    const skipped = [];

    for (const page of pages) {
        if (!fs.existsSync(page)) {
            // The homepage is a build invariant, so its absence is a real failure.
            // Everything else in this list is a specific URL (a blog post, a doc
            // page) that can be renamed or retired independent of this script; skip
            // it rather than breaking every build over stale critical-CSS scoping.
            if (page === "public/index.html") {
                throw new Error(`Expected ${page} to exist after Hugo build`);
            }
            skipped.push(page);
            console.warn(`Skipping critical CSS for ${page}: not found in this build (moved or removed?)`);
            continue;
        }

        const html = fs.readFileSync(page, "utf-8");
        const inlined = await beasties.process(html);
        fs.writeFileSync(page, inlined);
        console.log(`Inlined critical CSS: ${page}`);
    }

    // A handful of stale entries is expected as content gets renamed. A large
    // fraction going stale at once is a signal this allowlist needs a refresh,
    // so surface it loudly in build logs rather than letting it go unnoticed.
    if (skipped.length > 0) {
        console.warn(
            `\n${skipped.length} of ${pages.length} allowlisted pages in scripts/inline-critical-css.js were ` +
                "not found in this build. If this list is going stale, update it to match current top " +
                "organic landing pages.",
        );
    }
}

inlineCriticalCSS().catch((err) => {
    console.error("Failed to inline critical CSS:", err);
    process.exit(1);
});
