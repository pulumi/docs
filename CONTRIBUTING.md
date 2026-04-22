# Contributing Pulumi Documentation

## Draft-first pull requests

Open new PRs as **drafts** while you iterate. Automated review (style, accuracy, fact-check) fires only when you mark a PR **ready for review**, so a draft-first flow:

- Keeps your branch out of the noisy "every push triggers a review" loop.
- Lets you push iteratively without spamming the PR with new comments each time.
- Means the eventual review reflects your finished thinking, not a half-finished commit.

When you're ready, use the **Ready for review** button on the PR page. Triage runs again to refresh labels, then the full review fires once and pins its findings to a single comment at the top of the PR. New commits afterward will mark the review **stale** but won't auto-rerun — mention `@claude` in a comment to refresh, or transition through draft and back to ready.

If your change is genuinely trivial (a typo, a one-line fix), opening directly as ready is fine — the pipeline will short-circuit on the `review:trivial` label.

## Documentation structure

The mapping from documentation page to section and table-of-contents (TOC) is stored largely in each page's front matter, leveraging [Hugo Menus](https://gohugo.io/content-management/menus/). Menus for the CLI commands and API reference are specified in `./config.toml`.

## Hugo tips

### Short codes

To share common content across articles, use [Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/). Place a .html file in the [layouts/shortcodes] folder. To include it in a page, use syntax `{{< my-shortcode >}}`

For example, our custom [`cleanup`](layouts/shortcodes/cleanup.html) shortcode can be included in .md files, to include common text about cleaning up stack resources:

```plain
{{< cleanup >}}
```

HTML layouts can include other layouts inside the [layouts/partials](layouts/partials) directory, e.g.:

```plain
{{ partial "head.html" . }}
```

### Front matter

Front matter is defined as a YAML block at the top of a Markdown document that defines metadata about the page. Pulumi docs pages often include the following front matter variables:

- `aliases`: A list of relative URLs that should point to the content in this page. When moving or renaming a page, you must add an `alias` entry for the old path of the page relative to the `content/` folder.
- `allow_long_title`: Set to `true` in order disable length validation on the `title` attribute.
- `block_external_search_index`: Set to `true` to prevent crawlers from indexing the page.
- `h1`: If specified, the `<h1>` at the top of the page will use this value instead of the value in the `title` attribute.
- `menu`: Specifies where a page appears in the document navigation tree.
- `meta_desc`: Required (unless `redirect_to` is set), at least 50 characters, no longer than 160 characters. This displays as the description of the page in web search results.
- `meta_image`: Blog posts only. Relative path to an OpenGraph image (1200×628) for social media previews and the blog home page. The image must be a PNG file for compatibility.
- `feature_image`: Blog posts only. Relative path to a high-resolution hero image (1884×1256) displayed at the top of the blog post page.
- `meta_title`: If specified, the meta title (for OpenGraph) will use this value instead of the value in the `title` attribute.
- `redirect_to`: The relative or absolute URL of a permanent redirect.
- `title`: Required (unless `redirect_to` is set), 60 characters or less. This controls the default value for the `<title>` tag as well at the top level `<h1>` in the document.
- `title_tag`: If specified, the `<title>` tag on the rendered call will use this value instead of the `title` attribute.

You can also define arbitrary front-matter variable in the YAML section at the top of a file and refer to that same value in the page content. For instance, the you could add the following front matter `foo: "bar"`, and then reference the variable in markdown with the syntax `{{< param foo >}}`.

For more information, see [Front Matter](https://gohugo.io/content-management/front-matter/) in the Hugo docs.
