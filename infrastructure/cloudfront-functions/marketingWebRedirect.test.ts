// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as assert from "assert";
import { test } from "node:test";

import { marketingWebPagePaths } from "../marketingWebPaths";
import { marketingWebRedirectCode } from "./marketingWebRedirect";

const handler: (event: any) => any = new Function(`${marketingWebRedirectCode}; return handler;`)();

// Mirrors CloudFront's rawQueryString(): the text after "?", or undefined when there's no "?".
function request(url: string, accept?: string) {
    const [uri, ...rest] = url.split("?");
    const rawQuery = rest.length ? rest.join("?") : undefined;
    const headers: Record<string, { value: string }> = {};
    if (accept !== undefined) {
        headers.accept = { value: accept };
    }
    return { request: { method: "GET", uri, querystring: {}, headers, rawQueryString: () => rawQuery } };
}

function location(result: any): string {
    assert.strictEqual(result.statusCode, 301);
    return result.headers.location.value;
}

const utms = "utm_source=a&utm_campaign=b";

const pagePaths = marketingWebPagePaths.map((pattern) => pattern.replace(/\*$/, ""));
const barePagePaths = pagePaths.filter((uri) => !uri.endsWith("/") && !uri.includes("."));
const slashOrFilePagePaths = pagePaths.filter((uri) => !barePagePaths.includes(uri));

test("adds the trailing slash and keeps the query", () => {
    assert.ok(barePagePaths.length > 0);
    for (const uri of [...barePagePaths, "/dev/browse", "/dev/glossary"]) {
        assert.strictEqual(location(handler(request(`${uri}?${utms}`))), `${uri}/?${utms}`, uri);
    }
});

test("adds no ? when there is no query", () => {
    assert.strictEqual(location(handler(request("/pricing"))), "/pricing/");
    assert.strictEqual(location(handler(request("/pricing?"))), "/pricing/");
});

test("keeps the query byte for byte", () => {
    for (const query of [
        "utm_campaign=a%20b%26c",
        "q=test&tag=x&tag=y",
        "flag&empty=&utm_source=a",
        "gclid=Cj0KCQ&utm_term=caf%C3%A9+au+lait",
    ]) {
        assert.strictEqual(location(handler(request(`/pricing?${query}`))), `/pricing/?${query}`, query);
    }
});

test("redirects legacy facet URLs to the slash form in one hop, with the query", () => {
    const cases: [string, string][] = [
        ["/dev/browse/cloud/aws/", "/dev/cloud/aws/"],
        ["/dev/browse/language/python", "/dev/language/python/"],
        ["/dev/browse/tag/serverless", "/dev/tag/serverless/"],
        ["/dev/browse/collection/a/b", "/dev/collection/a/b/"],
    ];
    for (const [from, to] of cases) {
        assert.strictEqual(location(handler(request(`${from}?${utms}`))), `${to}?${utms}`, from);
    }
});

test("redirects legacy facet URLs even for markdown requests", () => {
    assert.strictEqual(location(handler(request("/dev/browse/cloud/aws", "text/markdown"))), "/dev/cloud/aws/");
});

test("passes through URLs that already end in a slash or name a file", () => {
    assert.ok(slashOrFilePagePaths.length > 0);
    for (const uri of [...slashOrFilePagePaths, "/dev/", "/dev/browse/", "/dev/foo.md", "/dev/browse/bogus/x/"]) {
        const event = request(`${uri}?${utms}`);
        assert.strictEqual(handler(event), event.request, uri);
    }
});

test("passes through markdown requests", () => {
    const event = request(`/dev/foo?${utms}`, "text/markdown, text/html;q=0.9");
    assert.strictEqual(handler(event), event.request);
});

test("sets a one-week cache-control on redirects", () => {
    assert.strictEqual(handler(request("/pricing")).headers["cache-control"].value, "max-age=604800");
});
