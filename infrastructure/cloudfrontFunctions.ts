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
