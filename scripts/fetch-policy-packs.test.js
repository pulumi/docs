// Regression coverage for the registry gate in fetch-policy-packs.js — the check that
// decides which pre-built policy packs get a public reference page.
//
// It is worth testing because the failure is silent and outward-facing: getting it wrong
// once already put a private pack (hitrust-awsnative) on the public site, and the reverse
// direction fails *open* when the listing is read incompletely, so a product nobody
// documented would slip past the check written to catch exactly that.
//
// Run: node --test scripts/fetch-policy-packs.test.js   (also via scripts/run-unit-tests.sh)

const test = require("node:test");
const assert = require("node:assert");

const { parseRegistryListing, auditAllowlist } = require("./fetch-policy-packs.js");

// Shapes taken from the live listing for the `pulumi` org, 2026-08-25.
const product = (name) => ({ name, source: "pulumi", publisher: "pulumi", version: "1.0.0" });
const private_ = (name) => ({ name, source: "private", publisher: "pulumi", version: "1.0.0" });
const listing = (...rows) => ({ policyPacks: rows });

const audit = (opts) =>
    auditAllowlist({
        org: "pulumi",
        packs: [],
        allowlistUndocumented: [],
        products: new Set(),
        nonProducts: new Map(),
        warn: () => {},
        ...opts,
    });

test("parseRegistryListing separates products from privately published packs", () => {
    const { products, nonProducts } = parseRegistryListing(
        listing(product("cis-aws"), private_("super-policy")),
        "pulumi",
    );
    assert.deepStrictEqual([...products], ["cis-aws"]);
    assert.strictEqual(nonProducts.get("super-policy"), "private");
});

test("parseRegistryListing rejects an envelope it does not recognize", () => {
    // The spec pins `policyPacks`; anything else means the API changed under us.
    for (const body of [[product("cis-aws")], { items: [product("cis-aws")] }, {}, null]) {
        assert.throws(() => parseRegistryListing(body, "pulumi"), /policyPacks/);
    }
});

test("parseRegistryListing refuses a paginated response instead of reading page one", () => {
    // A partial read fails documented packs that are fine AND hides undocumented products.
    assert.throws(
        () => parseRegistryListing({ ...listing(product("cis-aws")), continuationToken: "x" }, "pulumi"),
        /paginated/,
    );
});

test("parseRegistryListing blames the shape, not the allowlist, when no row is a product", () => {
    // If `source` is renamed upstream, the honest error is "the API changed" — not the
    // allowlist error naming every documented pack as privately published.
    assert.throws(
        () => parseRegistryListing(listing({ name: "cis-aws" }, { name: "nist-aws" }), "pulumi"),
        /source/,
    );
});

test("parseRegistryListing distinguishes a missing source field from an absent pack", () => {
    const { nonProducts } = parseRegistryListing(
        listing(product("cis-aws"), { name: "odd-one" }),
        "pulumi",
    );
    assert.strictEqual(nonProducts.get("odd-one"), "(no source field)");
});

test("an empty listing is not treated as every pack being unpublished", () => {
    const { products } = parseRegistryListing(listing(), "pulumi");
    assert.strictEqual(products.size, 0);
});

test("forward: a documented pack that is not a product fails, naming its real source", () => {
    // The hitrust-awsnative case, and the live cis-kubernetes-gcp one.
    assert.throws(
        () =>
            audit({
                packs: ["cis-kubernetes-gcp"],
                products: new Set(["cis-kubernetes-google-cloud"]),
                nonProducts: new Map([["cis-kubernetes-gcp", "private"]]),
            }),
        /cis-kubernetes-gcp \(source: private\)/,
    );
});

test("forward: a documented pack absent from the listing says so", () => {
    assert.throws(
        () => audit({ packs: ["deleted-pack"], products: new Set(["cis-aws"]) }),
        /absent from the listing/,
    );
});

test("reverse: a product with no page and no exemption fails", () => {
    assert.throws(
        () => audit({ packs: ["cis-aws"], products: new Set(["cis-aws", "brand-new-product"]) }),
        /brand-new-product/,
    );
});

test("reverse: an exempted product passes", () => {
    assert.doesNotThrow(() =>
        audit({
            packs: ["cis-aws"],
            allowlistUndocumented: [{ pack: "aws-organizations-tag-policies", why: "hand-written page" }],
            products: new Set(["cis-aws", "aws-organizations-tag-policies"]),
        }),
    );
});

test("an exemption without a why: cannot silence the check", () => {
    assert.throws(
        () =>
            audit({
                allowlistUndocumented: [{ pack: "quietly-hidden" }],
                products: new Set(["quietly-hidden"]),
            }),
        /"why:"/,
    );
});

test("a bare-string exemption is rejected rather than silently ignored", () => {
    // `- foo` parses to a string, so `e.pack` is undefined: the pack stays unaccounted
    // for and the check would otherwise fire naming a pack the author just listed.
    assert.throws(
        () => audit({ allowlistUndocumented: ["quietly-hidden"], products: new Set(["quietly-hidden"]) }),
        /"pack:"/,
    );
});

test("a pack cannot be both documented and exempted", () => {
    assert.throws(
        () =>
            audit({
                packs: ["cis-aws"],
                allowlistUndocumented: [{ pack: "cis-aws", why: "leftover" }],
                products: new Set(["cis-aws"]),
            }),
        /also have\n?\s*a page above/,
    );
});

test("an exemption for a pack that stopped being a product warns but does not fail", () => {
    const warnings = [];
    assert.doesNotThrow(() =>
        audit({
            allowlistUndocumented: [{ pack: "was-a-product", why: "superseded" }],
            products: new Set(),
            warn: (m) => warnings.push(m),
        }),
    );
    assert.match(warnings.join("\n"), /no longer\n?\s*published products: was-a-product/);
});

test("the happy path stays quiet", () => {
    const warnings = [];
    assert.doesNotThrow(() =>
        audit({
            packs: ["cis-aws", "nist-aws"],
            allowlistUndocumented: [{ pack: "aws-organizations-tag-policies", why: "hand-written page" }],
            products: new Set(["cis-aws", "nist-aws", "aws-organizations-tag-policies"]),
            warn: (m) => warnings.push(m),
        }),
    );
    assert.deepStrictEqual(warnings, []);
});
