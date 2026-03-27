// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";

// CloudFront Function that rewrites the request URI to serve index.md instead of
// index.html when the client sends Accept: text/markdown. This enables content
// negotiation for docs pages, allowing LLMs and other markdown-aware clients to
// receive clean markdown instead of HTML.
//
// The function runs at viewer-request (before the cache lookup), so the rewritten
// URI becomes the cache key — no cache policy changes are needed.
const markdownNegotiationFunctionCode = `
function handler(event) {
    var request = event.request;
    var accept = request.headers['accept'] ? request.headers['accept'].value : '';
    var uri = request.uri;

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
    comment: "Rewrites docs URIs to serve index.md when Accept: text/markdown is present.",
});

export function getMarkdownNegotiationFunctionAssociation(): aws.types.input.cloudfront.DistributionOrderedCacheBehaviorFunctionAssociation {
    return {
        eventType: "viewer-request",
        functionArn: markdownNegotiationFunction.arn,
    };
}
