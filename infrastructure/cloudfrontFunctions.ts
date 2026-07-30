// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";

// CloudFront Function that rewrites docs request URIs to serve clean markdown,
// either via Accept: text/markdown content negotiation or via a .md URL suffix.
// Both paths target the per-page index.md artifact Hugo emits alongside index.html.
//
// The function runs at viewer-request (before the cache lookup), so the rewritten
// URI becomes the cache key — no cache policy changes are needed. The .md suffix
// and the Accept-header form rewrite to the same artifact, so they share a cache
// entry per page.
const markdownNegotiationFunctionCode = `
function handler(event) {
    var request = event.request;
    var accept = request.headers['accept'] ? request.headers['accept'].value : '';
    var uri = request.uri;

    // .md URL-suffix convention (header-free). /docs/foo.md → /docs/foo/index.md.
    // Skip if the URI already ends in /index.md (the literal artifact path).
    if (uri.endsWith('.md') && !uri.endsWith('/index.md')) {
        request.uri = uri.replace(/\\.md$/, '/index.md');
        return request;
    }

    // Accept: text/markdown content negotiation.
    if (accept.indexOf('text/markdown') !== -1) {
        if (uri.endsWith('/index.html')) {
            request.uri = uri.replace(/index\\.html$/, 'index.md');
        } else if (uri.endsWith('/')) {
            request.uri = uri + 'index.md';
        }
    }

    return request;
}
`;

const markdownNegotiationFunction = new aws.cloudfront.Function("markdown-negotiation", {
    runtime: "cloudfront-js-2.0",
    code: markdownNegotiationFunctionCode,
    comment: "Rewrites docs URIs to serve index.md via Accept: text/markdown or .md URL suffix.",
});

export function getMarkdownNegotiationFunctionAssociation(): aws.types.input.cloudfront.DistributionOrderedCacheBehaviorFunctionAssociation {
    return {
        eventType: "viewer-request",
        functionArn: markdownNegotiationFunction.arn,
    };
}

// Same negotiation for the marketing pages that ride the default cache behavior.
// Unlike /docs/* — where every page emits an index.md artifact — the default
// behavior serves many paths with no markdown variant, so this function rewrites
// only an allowlist of prefixes known to emit index.md (via `outputs`/`cascade`
// front matter in content/): the homepage, /what-is/, /product/, and /pricing/.
// Rewriting a path with no artifact would turn a valid HTML page into a 404 for
// markdown-accepting clients, so extend the allowlist only together with the
// corresponding Hugo output changes.
const marketingMarkdownNegotiationFunctionCode = `
function handler(event) {
    var request = event.request;
    var accept = request.headers['accept'] ? request.headers['accept'].value : '';
    var uri = request.uri;

    var eligible = uri === '/' || uri === '/index.html' ||
        uri === '/what-is.md' || uri === '/product.md' || uri === '/pricing.md' ||
        uri.indexOf('/what-is/') === 0 ||
        uri.indexOf('/product/') === 0 ||
        uri.indexOf('/pricing/') === 0;
    if (!eligible) {
        return request;
    }

    // .md URL-suffix convention (header-free). /product/neo.md → /product/neo/index.md.
    if (uri.endsWith('.md') && !uri.endsWith('/index.md')) {
        request.uri = uri.replace(/\\.md$/, '/index.md');
        return request;
    }

    // Accept: text/markdown content negotiation.
    if (accept.indexOf('text/markdown') !== -1) {
        if (uri === '/') {
            request.uri = '/index.md';
        } else if (uri.endsWith('/index.html')) {
            request.uri = uri.replace(/index\\.html$/, 'index.md');
        } else if (uri.endsWith('/')) {
            request.uri = uri + 'index.md';
        }
    }

    return request;
}
`;

const marketingMarkdownNegotiationFunction = new aws.cloudfront.Function("marketing-markdown-negotiation", {
    runtime: "cloudfront-js-2.0",
    code: marketingMarkdownNegotiationFunctionCode,
    comment: "Serves index.md for the homepage, /what-is/, /product/, and /pricing/ via Accept: text/markdown or .md URL suffix.",
});

export function getMarketingMarkdownNegotiationFunctionAssociation(): aws.types.input.cloudfront.DistributionDefaultCacheBehaviorFunctionAssociation {
    return {
        eventType: "viewer-request",
        functionArn: marketingMarkdownNegotiationFunction.arn,
    };
}

// CloudFront Function that stamps the correct Content-Type on the RFC 9727 API
// catalog. The catalog is served from S3 as the extensionless object
// /.well-known/api-catalog, so S3 hands it back as binary/octet-stream; agents
// expect application/linkset+json. Runs at viewer-response and only rewrites
// that single path, so every other response on the behavior is untouched.
const apiCatalogContentTypeFunctionCode = `
function handler(event) {
    var response = event.response;
    if (event.request.uri === '/.well-known/api-catalog') {
        response.headers['content-type'] = { value: 'application/linkset+json' };
    }
    return response;
}
`;

const apiCatalogContentTypeFunction = new aws.cloudfront.Function("api-catalog-content-type", {
    runtime: "cloudfront-js-2.0",
    code: apiCatalogContentTypeFunctionCode,
    comment: "Sets Content-Type: application/linkset+json on /.well-known/api-catalog.",
});

export function getApiCatalogContentTypeFunctionAssociation(): aws.types.input.cloudfront.DistributionDefaultCacheBehaviorFunctionAssociation {
    return {
        eventType: "viewer-response",
        functionArn: apiCatalogContentTypeFunction.arn,
    };
}
