// Copyright 2026, Pulumi Corporation.  All rights reserved.

// Behavior order matters; invalidate-marketing-web-cache.yml reads this list from the stack output.
export const marketingWebPaths = [
    "/dev*",
    // The Dev Center's root-relative CSS/JS/images; this repo serves its own from /css and /js.
    "/assets*",
    // Exact paths: /community* would also take /community/team/* and the redirects under /community/ off S3.
    "/community",
    "/community/",
    "/community.md",
    "/community/puluminaries*",
    // Exact paths: /pricing* would also take the /pricing/open-source-free-tier/ redirect off S3.
    "/pricing",
    "/pricing/",
    "/pricing.md",
    // Exact paths: /up* would also take the /updateplans/ alias off S3.
    "/up",
    "/up/",
    "/up/*",
    // Also takes /topics/containers/ off S3, so its old 301 to the Kubernetes docs no longer fires.
    "/topics*",
];
