# pulumi-hugo

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pulumi/pulumi-hugo)

A [Hugo](https://gohugo.io) module containing content and layouts used on pulumi.com, including hand-authored docs, the Pulumi blog, and Learn Pulumi.

This repository is consumed by https://github.com/pulumi/docs to produce the website you see at https://pulumi.com. If you're interested in contributing some docs or a blog post at https://pulumi.com/blog, you've come to the right place! 🙌

## Contributing

First, be sure to read our [contributing guide](CONTRIBUTING.md) and review our [code of conduct](CODE-OF-CONDUCT.md).

## Toolchain

We build the Pulumi website statically with Hugo, manage our Node.js dependencies with Yarn, and write most of our documentation in Markdown. Below is a list of the tools you'll need to run the website locally:

* [Go](https://golang.org/) (>= 1.15)
* [Hugo](https://gohugo.io) (>= 0.92)
* [Node.js](https://nodejs.org/en/) (>= 18)
* [Yarn](https://classic.yarnpkg.com/en/) (1.x)

### VS Code devcontainer

Alternatively you can use the [devcontainer environment](https://code.visualstudio.com/docs/remote/create-dev-container) included in this repo. Open this folder in [VS Code](https://code.visualstudio.com/) and run the `Remote-Containers: Reopen in container` command in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

Within the container you can run the various make commands explained below. Port 1313 is forwarded into the container so you can use your normal browser to access the results of `make serve` or `make serve-all` at http://localhost:1313.

## Installing prerequisites

Run `make ensure` to check for the appropriate tools and versions and install any dependencies. The script will let you know if you're missing anything important.

```
make ensure
```

## Running Hugo locally

Once you've run `make ensure` successfully, you're ready to run the development server. If you're only planning on writing Markdown or working with Hugo layouts, this command should be all you need:

```
make serve
```

If you are planning on making CSS or JS changes you will need to run:

```
make serve-all
```

You can browse the development server at http://localhost:1313, and any changes you make to content or layouts should be reloaded automatically.

## Linting and formatting

To check your code and your Markdown files for issues before submitting, run:

```
make lint
```

This repo uses Prettier for code formatting, to keep styling + formatting issues aligned without the need to be reviewed in PRs.  To see what files have formatting diffs, you can run `make format` from the project root, which will update all files to conform to our formatting standards.  To check the diffs without fixing them, a check runs as part of `make lint`.

Prettier is easiest to use when you run it automatically on save in your editor - see the docs here: https://prettier.io/docs/en/editors.html.  If you set your editor to format on save, you should be staying aligned with formatting without needing to run any of the above commands.

## Tidying up

To clear away any module caches or build artifacts, run:

```
make clean
```

## About this repository

This repository is a [Hugo module](https://gohugo.io/hugo-modules/) that doubles as a development server. **It does not contain every page of the Pulumi website**, because most of those pages (e.g., those comprising our CLI and SDK docs) are generated from source code, so they aren't meant to be edited by humans directly.

Because of this, many of the links you follow when browsing around on the development server (to paths underneath `/registry` or `/docs/reference`, for example) will fail to resolve because they originate from another repository &mdash; most likely https://github.com/pulumi/registry or https://github.com/pulumi/docs. When we build the Pulumi website, we merge this module along with any others into a single build artifact, but when you're working within an individual module like this one, you may find you're unable to reach certain pages or verify the links you may want to make to them.

If you want to link to a page that exists on https://pulumi.com but not in this repository, use the page's path **starting at the root** in a Markdown or HTML link. For example, in a Markdown file, to link to the [Digital Ocean Droplet](https://www.pulumi.com/registry/packages/digitalocean/api-docs/droplet/) page (a page that doesn't exist in this repository, but that would exist in an integration build), you'd use:

```markdown
[Digital Ocean Droplet](/registry/packages/digitalocean/api-docs/droplet/)
```

### What's in this repo

* All hand-authored content and documentation, including top-level pages, guides, blog posts, and some tutorials
* Most Hugo module components, including archetypes, layouts, partials, shortcodes, data, etc.
* All the SCSS, TS, and Stencil files used to build our CSS/JSS assets.

You'll find all of these files in `themes/default`.

### What's not in this repo

* Generated documentation for the Pulumi CLI and SDK. You'll find this at https://github.com/pulumi/docs.
* Generated tutorials. You'll find these at https://github.com/pulumi/examples.
* Templates used for generating resource documentation. You'll find these at https://github.com/pulumi/pulumi.
* The Pulumi Registry. You'll find this at https://github.com/pulumi/registry.

## Merging and releasing

When a pull request is merged into the `master` branch of this repository, the content of the pull request isn't published immediately. Instead, it's published at some point later, typically as a result of an [hourly GitHub Actions job in pulumi/docs](https://github.com/pulumi/docs/actions/workflows/update-theme.yml) that checks this repository and others for new content. When that job (which runs every 15 minutes) finds new content to be published, it creates a new pull request (or updates an existing one) on pulumi/docs, builds and tests a full site preview, and merges that pull request automatically after the tests pass, triggering the website to be republished.

The typical timeline looks something like this:

* 8:59 AM: A PR is merged into pulumi-hugo `master`.
* 9:00 AM: The [`Scheduled Jobs: Update Hugo modules`](https://github.com/pulumi/docs/actions/workflows/update-theme.yml) workflow runs in pulumi/docs.
* 9:02 AM: The workflow detects the newly merged pulumi-hugo content and generates a new PR on pulumi/docs.
* 9:08 AM: The pulumi/docs PR build completes and is automatically merged into `master`, triggering a redeployment of pulumi.com.
* 9:18 AM: The new content is live.

In other words, it generally takes between 15 and 30 minutes for a change merged into this repository to appear on pulumi.com. Note, however, that despite that we schedule the module-update job to run every 15 minutes, GitHub doesn't guarantee that this happens precisely on time; delays of up to several minutes are unfortunately fairly common.

If having more direct control over release timing is important, you can opt to trigger the module-update job manually to save some time. To do that, [navigate to the workflow](https://github.com/pulumi/docs/actions/workflows/update-theme.yml) and choose **Run Workflow** to kick it off immediately:

![image](https://user-images.githubusercontent.com/274700/168188720-e4b2ee56-4b84-4c4f-ad3a-68e145d69124.png)

The behavior in this case is no different than if you'd allowed the job to run on its own, and once it completes, the remaining steps will complete in the usual way.

## Blogging

Interested in writing a blog post? See the [blogging README](BLOGGING.md) for details.

## Search

We use [Algolia](https://www.algolia.com/) for search, and we update the Algolia search index [on every deployment](https://github.com/pulumi/docs/blob/master/scripts/ci-push.sh#L13) of the website. Whether you're adding a new page or updating an existing one, your changes will be reflected in search results within a few seconds of release.

### Creating findable content

We currently index every page of the website, including the blog and the Registry. However, we do not index all of the content of every page &mdash; we only index certain properties of the page. These include:

* Page titles (specifically the `title` and `h1` frontmatter params)
* Page descriptions (specifically the `meta_desc` param)
* Second-level headings (e.g., those prefixed with `##` in Markdown files)
* Keywords, if any (via the `search.keywords` param)
* Authors, if any (via the `authors` param)
* Tags, if any (via the `tags` param)

Because of this, it's important to be thoughtful about the terms you use for these fields, especially titles, keywords, descriptions, and H2 headings. If you want your content to be findable by specific terms, you must make sure those terms exist in one or more of the fields listed above.

For example, if you were writing a guide to building an ETL pipeline with Redshift, and you wanted to make sure the page would be surfaced for queries like `redshift data warehouse etl`, you might construct the page's frontmatter in the following way:

```yaml
title: Build an ETL pipeline with Redshift and AWS Glue
meta_desc: Learn how to combine AWS Glue and Amazon Redshift to build a fully-automated ETL pipeline with Pulumi.
search:
    keywords:
        - data warehouse
```

In this case, the optional `search.keywords` field is included to cover the terms `data warehouse`, as those terms don't exist in the page's title or description. If it weren't, queries for `data warehouse` would fail to match this particular page.

Certain fields also rank higher than others in terms of their overall relevance. (Titles and keywords, for example, are considered more relevant than descriptions.) For a full list of these rankings, along with all of the rules we apply to the search index, see the [search app in pulumi/docs](https://github.com/pulumi/docs/blob/master/scripts/search/settings.js).

### Keeping pages out of search results

To keep a page from showing up in search results (including on Google, etc.), use the `block_external_search_index` frontmatter parameter:

```yaml
title: My page
...
block_external_search_index: true
```

## Style Guide

We try and align Pulumi documentation to the [Pulumi Docs Style Guide](STYLE-GUIDE.md).

## Shortcodes and web components

We use number of Hugo shortcodes and web components in our pages. You can read more about many of them in the [components README](https://github.com/pulumi/theme/tree/master/stencil).
