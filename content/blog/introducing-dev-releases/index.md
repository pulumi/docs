---
title: "Introducing Dev Releases for the Pulumi CLI and SDKs"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-04-02

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: 'Introducing Dev Releases for the Pulumi CLI and SDKs: early releases to enable customers to access changes as soon as they have been merged.'

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - thomas-gummerer

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - cli
  - sdk
  - pre-release
---

At Pulumi, the stability of our CLI and SDK releases is critically important.  A lot of infrastructure is built and deployed using Pulumi, and any bugs in how that infrastructure is deployed can cause outages.  While we put a lot of emphasis on unit and integration testing, we are also constantly investing in new ways to provide additional safeguards to ensure we always deliver stable releases.  To that end, we are introducing new dev releases of our CLI and SDKs, which will enable users who want to work with the very latest bits to try them out before they are deployed widely to the entire Pulumi user base.  This blog post will walk you through how we are using them internally, and how you can too!

<!--more-->

## What are dev releases?

On every push to the main branch, in other words every time a pull request is merged, we publish a new dev release for both the CLI and the Pulumi core SDKs.  For the CLI, we publish the binaries for all supported platforms to S3, while for the SDKs we create pre-release versions in whatever form the various package managers support.

This means these dev releases always include all the latest features and bug fixes, that will be in the next stable release.  And while it was always possible to get the latest CLI or SDKs with some moderate effort depending on the platform and language, having these be proper releases makes for a much more standardized experience on how to install them.

Dev releases of the CLI can be [installed](/docs/install/#installing-dev-releases) on Linux, macOS, and Windows. For example, on Linux or macOS:

```bash
$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev
```

Dev SDKs are currently available for [Node.js](/docs/languages-sdks/javascript/#dev-versions), [Python](/docs/languages-sdks/python/#dev-versions), [.NET](/docs/languages-sdks/dotnet/#dev-versions), and [Go](/docs/languages-sdks/go/#dev-versions). For example, installing the dev release of the Node.js SDK with `npm`:

```bash
$ npm add @pulumi/pulumi@dev
```

## How are we using them internally at Pulumi?

At Pulumi we are not only developers of our product, but we also love using it internally.  All deploys for Pulumi Cloud are orchestrated by Pulumi.  In addition we use Pulumi for managing other things such as this blog, and even access management to services we are using is partly done with Pulumi.  All of these are a great way for us to test our software in real world use cases, before releasing it.

In addition to that, we also use the dev releases for testing both our [templates](https://github.com/pulumi/templates/) and [examples](https://github.com/pulumi/examples/).  This is a huge set of Pulumi programs, that can help figure out problems early.

## How you can leverage dev releases

In addition to making it easier for us to test new code that gets merged, and making sure we can release the most stable software possible, we also wanted to make it easier for users to use these dev releases.  There's a couple reasons why these could help your organization:

- A bug fix has been merged, but not yet released?  You can get it a few minutes after it is merged via the dev release channel
- You want to make sure your production stacks work well with the latest version of Pulumi?  Use dev releases with your dev stacks for some early testing.  We'd be delighted with any bugs that are reported before they make it into a release.

## How to get started

For instructions on how to use the CLI dev releases see the [Install Docs](/docs/install/#installing-dev-releases), and for pre-release versions of dev SDKs see the docs for [Node.js](/docs/languages-sdks/javascript/#dev-versions), [Python](/docs/languages-sdks/python/#dev-versions), [.NET](/docs/languages-sdks/dotnet/#dev-versions), and [Go](/docs/languages-sdks/go/#dev-versions).

Happy building!
