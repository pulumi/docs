// Unit tests for the .md redirect duplication in scripts/make-s3-redirects.js.
//
// A moved page's .md key used to redirect to the new page's HTML URL, so a
// .md-suffix markdown client followed the 301 and landed on HTML
// (pulumi/docs#20594). These tests pin the fix: .md redirects whose target is a
// markdown-enabled page on this site point at that page's index.md artifact, and
// everything else keeps the HTML location it had before.

const { test } = require("node:test");
const assert = require("node:assert/strict");

const { buildMarkdownRedirects, markdownLocation } = require("./make-s3-redirects.js");

test("site-relative docs page target gets its index.md artifact", () => {
    assert.equal(markdownLocation("/docs/get-started/"), "/docs/get-started/index.md");
});

test("same-origin absolute target is rewritten and keeps its origin", () => {
    assert.equal(
        markdownLocation("https://www.pulumi.com/docs/iac/operations/continuous-delivery/"),
        "https://www.pulumi.com/docs/iac/operations/continuous-delivery/index.md",
    );
});

test("fragment and query survive after index.md", () => {
    assert.equal(markdownLocation("/docs/iac/concepts/stacks/#outputs"), "/docs/iac/concepts/stacks/index.md#outputs");
    assert.equal(markdownLocation("/what-is/what-is-iac/?x=1"), "/what-is/what-is-iac/index.md?x=1");
});

test("homepage, what-is and product targets are markdown-enabled", () => {
    assert.equal(markdownLocation("/"), "/index.md");
    assert.equal(markdownLocation("/what-is/what-is-iac/"), "/what-is/what-is-iac/index.md");
    assert.equal(markdownLocation("/product/neo/"), "/product/neo/index.md");
});

test("targets without a markdown artifact are left alone", () => {
    for (const location of [
        "https://github.com/pulumi/pulumi",          // external
        "https://example.com/docs/foo/",              // external, docs-shaped path
        "//www.pulumi.com/docs/foo/",                 // protocol-relative
        "/docs/reference/pkg/nodejs/pulumi/awsx/modules/classic.acmpca.html", // file target
        "/docs/reference/pkg/python/pulumi/",         // generated API reference
        "/docs/versioned/v3/",                        // versioned archive
        "/blog/some-post/",                           // section without markdown output
        "/registry/packages/aws/",                    // proxied elsewhere
        "/docs/iac/get-started",                      // not a page URL (no trailing slash)
    ]) {
        assert.equal(markdownLocation(location), null, location);
    }
});

test("moved docs page: .md key points at the markdown artifact (#20594 repro)", () => {
    const md = buildMarkdownRedirects(["docs/iac/get-started/index.html|/docs/get-started/"]);
    assert.deepEqual(md, ["docs/iac/get-started/index.md|/docs/get-started/index.md"]);
});

test("docs source with a non-markdown target keeps the HTML location", () => {
    const md = buildMarkdownRedirects([
        "docs/old/index.html|https://github.com/pulumi/pulumi",
        "docs/older/index.html|/registry/packages/aws/",
    ]);
    assert.deepEqual(md, [
        "docs/old/index.md|https://github.com/pulumi/pulumi",
        "docs/older/index.md|/registry/packages/aws/",
    ]);
});

test("what-is and product sources get .md duplicates too", () => {
    const md = buildMarkdownRedirects([
        "what-is/old-name/index.html|/what-is/new-name/",
        "product/old/index.html|/blog/announcing-new/",
    ]);
    assert.deepEqual(md, [
        "what-is/old-name/index.md|/what-is/new-name/index.md",
        "product/old/index.md|/blog/announcing-new/",
    ]);
});

test("top-level alias gets a .md duplicate only when its target has markdown", () => {
    const md = buildMarkdownRedirects([
        "get-started/index.html|/docs/get-started/",
        "puluminaries/index.html|/community/puluminaries/",
        "blog/old/index.html|/blog/new/",
    ]);
    assert.deepEqual(md, ["get-started/index.md|/docs/get-started/index.md"]);
});

test("non-.html keys produce no .md duplicates", () => {
    assert.deepEqual(buildMarkdownRedirects(["docs/some/file.pdf|/docs/other/"]), []);
});

test("API reference sources keep their HTML-target .md duplicates", () => {
    const md = buildMarkdownRedirects([
        "docs/reference/pkg/nodejs/pulumi/awsx/apigateway/index.html|/docs/reference/pkg/nodejs/pulumi/awsx/classic.apigateway.html",
    ]);
    assert.deepEqual(md, [
        "docs/reference/pkg/nodejs/pulumi/awsx/apigateway/index.md|/docs/reference/pkg/nodejs/pulumi/awsx/classic.apigateway.html",
    ]);
});

test("non-page sources outside the markdown sections get no .md duplicate", () => {
    const md = buildMarkdownRedirects(["compliance/aws-cis.html|/docs/iac/"]);
    assert.deepEqual(md, []);
});
