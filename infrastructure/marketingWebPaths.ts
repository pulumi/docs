// Copyright 2026, Pulumi Corporation.  All rights reserved.

// Behavior order matters; invalidate-marketing-web-cache.yml reads this list from the stack output.
export const marketingWebPaths = [
    // The homepage. Exact paths: a wildcard here would also take every other
    // top-level page this repo still serves off S3.
    "/",
    "/index.html",
    "/index.md",
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
    // Hides every S3 object under /customers/, so marketing-web 301s the old case-study stubs and /customers/industry/{,blockchain/} itself.
    "/customers*",
    "/pulumi-for-startups",
    "/pulumi-for-startups/",
    "/pulumi-for-startups.md",
    "/extend-trial",
    "/extend-trial/",
    "/subscribe",
    "/subscribe/",
    "/subscribe.md",
    "/agent-start",
    "/agent-start/",
    "/agent-start.md",
    "/onboard.md",
    // marketing-web 301s /confirmation/ to / at its own CDN, as the Hugo page's redirect_to did.
    "/confirmation*",
    // Exact paths: /gads* would also take the /gads/ redirect and the retired gads pages' redirects off S3.
    "/gads/infrastructure-as-code",
    "/gads/infrastructure-as-code/",
    // One wildcard for every /try/ ad page: CloudFront caps behaviors per distribution, so a pair per page hit TooManyCacheBehaviors. Nothing here serves /try/.
    "/try/*",
    // The old /testimonials/ page; S3 301s it here (scripts/redirects/love-redirects.txt).
    "/love",
    "/love/",
    "/love.md",
    // Covers /releases/, /releases/changelog/**, both release pages, the
    // RSS/JSON feeds, and the changelog entry images/videos. marketing-web
    // 301s the old /releases/changelog/<slug>/ alias URLs at its own CDN.
    "/releases*",
    "/sitemap-www-*",
    // Hides every S3 object under /product/, so marketing-web 301s the old
    // product/waitlist and product/private-previews stubs itself.
    //
    // Appended after /sitemap-www-* (not alphabetically, between /love.md and
    // /sitemap-www-*) on purpose: pulumi/docs#22948 inserts /releases* at
    // that same gap, and this placement keeps the two PRs' diffs from
    // touching the same lines, so neither needs a merge conflict resolved
    // against the other regardless of merge order.
    "/product*",
];
