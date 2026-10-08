---
title: "Pulumi Registry"
# This file is a build-time placeholder only (see the readme note below); the
# CloudFront/S3 trick means Google never actually sees the HTML Hugo renders
# from it. The real https://www.pulumi.com/registry/ page is served by, and
# already listed with an accurate lastmod in the sitemap of, the Registry app
# (github.com/pulumi/registry). Without sitemap_exclude, this placeholder's own
# git-derived lastmod (frozen since the 2023-12-11 commit that introduced it)
# competes with the Registry sitemap's entry for the same canonical URL, and
# consistently wins the "oldest URL in the whole sitemap" contest. Do not
# remove sitemap_exclude without also removing the duplicate from one side.
sitemap_exclude: true
readme: |
    This page is intentionally left blank, which may seem strange, but is actually necessary because
    of how the CloudFront CDN is configured to serve https://www.pulumi.com/registry/.

    If we didn't put this page here, requests for "/registry" (sans trailing slash) would prompt S3 to
    go looking in the currently deployed bucket for an object named `registry` (which it'd fail to find,
    because such an object wouldn't exist), then go looking for an object named `registry/index.html`
    (because `index.html` is defined as the bucket's `indexDocument`). On failing to find both, S3 would
    return the bucket's `errorDocument` (i.e., our 404 page) and an error code to CloudFront instead --
    which CloudFront would finally return to the user.

    Instead, by including this document, we give S3 an object to deliver to Cloudfront (our intentionally
    blank `registry/index.html`), but allow CloudFront to forward the request on to the Registry, which is
    configured to handle all requests for `/registry/*` (including `/registry/index.html`).

    More info here:
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html#DefaultRootObjectHow
---
