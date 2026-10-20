// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// CloudFront path patterns for the pages pulumi/marketing-web serves through this distribution.
export const marketingWebPagePaths = [
    "/dev*",
    // Exact paths: /community* would also take /community/team/* and the /community/community-engineering/* redirects away from S3.
    "/community",
    "/community/",
    "/community.md",
    "/community/puluminaries*",
    // Exact paths: /pricing* would also take the /pricing/open-source-free-tier/ redirect off S3.
    "/pricing",
    "/pricing/",
    "/pricing.md",
];

// The Dev Center's root-relative CSS, JS, and images; pulumi/docs keeps its own under /css and /js.
export const marketingWebAssetPaths = ["/assets*"];
