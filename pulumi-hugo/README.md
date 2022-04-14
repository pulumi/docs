# pulumi-hugo

A [Hugo](https://gohugo.io) module containing content and layouts used on pulumi.com, including hand-authored docs, the Pulumi blog, and Learn Pulumi.

This repository is consumed by https://github.com/pulumi/docs to produce the website you see at https://pulumi.com. If you're interested in contributing some docs or a blog post at https://pulumi.com/blog, you've come to the right place! 🙌

## Contributing

First, be sure to read our [contributing guide](CONTRIBUTING.md) and review our [code of conduct](CODE_OF_CONDUCT.md).

## Toolchain

We build the Pulumi website statically with Hugo, manage our Node.js dependencies with Yarn, and write most of our documentation in Markdown. Below is a list of the tools you'll need to run the website locally:

* [Go](https://golang.org/) (>= 1.15)
* [Hugo](https://gohugo.io) (>= 0.92)
* [Node.js](https://nodejs.org/en/) (>= 1.14)
* [Yarn](https://classic.yarnpkg.com/en/) (1.x)

### VS Code devcontainer

Alternatively you can use the [devcontainer environment](https://code.visualstudio.com/docs/remote/create-dev-container) included in this repo. Open this folder in [VS Code](https://code.visualstudio.com/) and run the `Remote-Containers: Reopen in container` command in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

Within the container you can run the various make commands explained below. Port 1313 is forwarded into the container so you can use your normal browser to access the results of `make serve` at http://localhost:1313.

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

You can browse the development server at http://localhost:1313, and any changes you make to content or layouts should be reloaded automatically.

## Linting and testing

To check your code and your Markdown files for issues before submitting, run:

```
make lint
```

## Tidying up

To clear away any module caches or build artifacts, run:

```
make clean
```

## About this repository

This repository is a [Hugo module](https://gohugo.io/hugo-modules/) that doubles as a development server. **It does not contain every page of the Pulumi website**, because most of those pages (e.g., those comprising our CLI and SDK docs) are generated from source code, so they aren't meant to be edited by humans directly.

Because of this, many of the links you follow when browsing around on the development server (to paths underneath `/docs/reference` for example) will fail to resolve because their content files are are checked into a different repository &mdash; most likely https://github.com/pulumi/docs. When we build the Pulumi website, we merge this module along with any others into a single build artifact, but when you're working within an individual module like this one, you may find you're unable to reach certain pages or verify the links you may want to make to them.

If you want to link to a page that exists on https://pulumi.com but not in this repository, just use the page's **relative path** with a [Hugo `relref`](https://gohugo.io/content-management/shortcodes/#ref-and-relref) in the usual way, and we'll make sure all links resolve properly at build-time. For example, to link to the [Digital Ocean Droplet](https://www.pulumi.com/docs/reference/pkg/digitalocean/droplet/) page (a page that doesn't exist in this repository but that would exist in an integration build), you'd use:

```
{{< relref /docs/reference/pkg/digitalocean/droplet >}}
```

This works because we've suppressed Hugo's built-in `relref` validation to keep the module-development workflow as lightweight as possible.

### What's in this repo

* All hand-authored content and documentation, including top-level pages, guides, blog posts, and some tutorials
* Most Hugo module components, including archetypes, layouts, partials, shortcodes, data, etc.

You'll find all of these files in `themes/default`.

### What's not in this repo

* CSS and JavaScript. You'll find these at https://github.com/pulumi/theme.
* Generated documentation for the Pulumi CLI and SDK. You'll find this at https://github.com/pulumi/docs.
* Generated tutorials. You'll find these at https://github.com/pulumi/examples).
* Templates used for generating resource documentation. You'll find these at https://github.com/pulumi/pulumi.

## Merging and releasing

When a pull request is merged into the default branch of this repository, a follow-up PR is triggered on [pulumi/docs](https://github.com/pulumi/docs) that produces an integration build. Once that build completes and is approved and merged into pulumi/docs, the changes are deployed to pulumi.com.

## Blogging

Interested in writing a blog post? See the [blogging README](BLOGGING.md) for details.

## Writing Docs

The following are guidelines to follow when authoring docs:

* When directing the user to interact with a button on a page, use "select" instead of "click" so that is not
  pointer-specific (for ex: for mobile phones, screen readers etc.)
* Try to use "navigate" instead of "go to"
* Avoid directional words, as folks that use screen readers do not have the same information about where things are
  placed on the page directionally.

## Shortcodes and web components

We use number of Hugo shortcodes and web components in our pages. You can read more about many of them in the [components README](themes/default/components).

## Search and Swiftype

Swiftype is how we manage our search experience for docs and Registry.  The [Swiftype docs](https://swiftype.com/documentation/site-search/site_search) have a lot of useful information.  A few items to keep in mind if you are updating search results or behavior:

### Swiftype console

Visit [the Swiftype console](https://app.swiftype.com/) for information specific to our search implementation: the date and time of the most recent crawl, any customizations we have done of result rankings for specific search terms, synonyms we have set for specific search terms, or weighting of custom meta tags.

### Result rankings

[Rankings](https://swiftype.com/documentation/site-search/guides/result-rankings) let us manually customize how results appear for any query.  Using the console, you can enter a query, and pin certain results to the top or delete results.


### Fields, meta tags, and weights

Fields are the set of places where the crawler extracts content from our pages.   There are a set of default fields (title, body, etc).  We can add fields by [adding custom meta tags](https://swiftype.com/documentation/site-search/crawler-configuration/meta-tags), either in the head or the body of a document.  It's worth noting that these are different than SEO meta tags, and the crawler does not capture those meta tags. Once a custom field is added and has been re-crawled (about a day after code has been merged), we can use the field to adjust results using weights.

[Weights](https://swiftype.com/documentation/site-search/guides/weights) are a way for us to impact search result relevance, by telling the engine that matches in a certain field of the document matter more than matches elsewhere.  In the Swiftype console, we can adjust the weights of any field.  By giving a certain field more weight, we can affect the ranking of search results.

### Synonyms

[Synonyms](https://swiftype.com/documentation/site-search/guides/synonyms) allow us to connect common search terms to each other.  If we know some users refer to a provider as “ReallyAwesome,” but our docs use the name “RA”, we can set those as synonyms in our Swiftype console.  This will ensure that users get the same set of results using either term, and that those results are relevant regardless of which name we use in our docs.


### UI and Layout

Swiftype is opinionated about the layout of search results, search behavior, and the UI styling of the search box.  Within the Swiftype console, [we can customize elements](https://swiftype.com/documentation/site-search/guides/design-and-customization) such as the style of search results, the result count per page, or text colors.  In order to override the search input styles (text color, border styles, etc) we need to directly update our styles for the `st-default-search-input` class.
