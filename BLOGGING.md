# Writing and Publishing a Pulumi Blog Post

So you're interested in contributing to the Pulumi blog? Great! Follow these
steps to make it happen.

## Quick Start: Creating a Blog Post with Claude Code

The easiest way to create a new blog post is with the `/new-blog-post` command in Claude Code. This command guides you step-by-step through creating a post, generating the required files and frontmatter automatically.

If you're using Claude Code, run `/new-blog-post` and then jump to [Write Your Post](#write-your-post) to learn about formatting and media. Otherwise, follow the manual instructions in the next section.

## Set Up Your Development Environment

If you haven't already, clone this repository and [follow the instructions in the README](https://github.com/pulumi/docs) to set up your environment and run the development web server.

Once you're able to run:

```zsh
make serve
```

If you can browse the site locally at <http://localhost:1313/> then you are ready to
proceed to the next section.

## Creating a Blog Post

> **Note**: [The `/new-blog-post` command](#quick-start-creating-a-blog-post-with-claude-code) is recommended for most contributors as it simplifies the process significantly. This section documents the manual process for reference or for contributors who don't have access to Claude Code.

### Manual Steps

1. Move onto a new branch for your blog post using `git checkout -b initials/your-blog-post` (replace initials with your initials, and replace your-blog-post with the name of your blog post).

1. Resist the temptation to copy-and-tweak an existing post! Instead, run the following command into the terminal (at the root of the project). This will generate a new file, including all the required frontmatter parameters.

   ```zsh
   make new-blog-post
   ```

   This will prompt you for a "slug" (a URL-friendly path) for your post and create a minimal post that you can browse to at <http://localhost:1313/blog/>. You'll find the new post's source file at `content/blog/[your-slug]/_index.md` containing the set of [Hugo front matter](https://gohugo.io/content-management/front-matter/) properties you'll need to get started:

   ```yaml
   ---
   title: "My New Post"
   date: 2019-07-17T14:26:50-07:00
   feature_image:
   authors:
       - joe-duffy
   tags:
       - some-tag
   ---
   ```

   Adjust the title and authors and add tags as appropriate (see the subsections below for more details). To change the post's URL, simply rename the folder containing `_index.md`; changing the folder name to `my-awesome-post`, for example, would result in a post ultimately published at <https://www.pulumi.com/blog/my-awesome-post>.

### Frontmatter Fields

**Title**

The `title` will populate the `<title>` tag of the page, the `<h1>`, and the display value if it is linked to internally. This field has a strict 60 character limit because of SEO related limitations. If you would like to have a longer display title (i.e. the `<h1>` tag) then you will need to specify it by adding `allow_long_title: True` to the front matter. If you would like to display different text on internal links than what the `title` value is, you can also specify a `linktitle` value. Both the `allow_long_title` and `linktitle` values can be of any length. Below is an example of this:

```yaml
---
title: This a Page Title
allow_long_title: true
linktitle: This is the link text
...
---
```

**Category**

Category is the *kind of post* axis — distinct from topical tags and from reading-path series — and it is a **closed set**. It is **required** and **singular**: every post declares exactly one `category:` scalar value (e.g. `category: product`), never a list. Apply the single best-fitting kind when the post clearly fits one of the specific kinds below; if it doesn't fit cleanly (for example, an SEO-oriented comparison like *Pulumi vs. Terraform* or a *What is X* explainer), use **`general`** — the default catch-all — and rely on its tags to place it in a subject area. If a post seems to span two kinds, pick the dominant one. `make lint` fails any blog post whose `category` is missing, is a list, or is a value outside the allowed set.

The allowed categories are the single source of truth in [`data/blog_categories.yaml`](./data/blog_categories.yaml):

| id | use when |
|---|---|
| `product` | Releases, new features, announcements, launch recaps, roadmaps |
| `engineering` | How we built it, deep technical dives, performance, internals |
| `community` | Events, meetups, webinars, hackathons, guest posts, open source, interns |
| `best-practices` | Architecture, IaC, platform-engineering, and security/governance patterns and guidance |
| `tutorials` | Step-by-step how-tos and getting-started guides |
| `customers` | Customer stories and case studies centered on a named customer |
| `perspectives` | Thought leadership and opinion — an original argument in the author's voice |
| `company` | Company news: funding, hiring, partnerships, brand, year-in-review |
| `general` | **Default.** Catch-all for posts that don't fit a specific kind (SEO comparisons, "what is X" explainers, listicles) |

Do **not** invent categories or add ad-hoc values to a post. To propose a new category (or rename/retire one), edit `data/blog_categories.yaml` in a PR and raise it in [#blogs](https://pulumi.slack.com/archives/CCBFCGU94) first. Topical buckets (clouds, languages, products) are *tags*, not categories — keep this axis tight.

**Tags**

Tags are the *topical* axis (subjects: clouds, languages, products, scenarios). Every tag added makes the overall tagging system harder to quickly grok, so we strongly prefer reusing an existing tag. The canonical, deduplicated vocabulary lives in [`data/blog_tags.yaml`](./data/blog_tags.yaml) — **pick a tag from there and avoid near-duplicates** (use `kubernetes`, not `k8s`; `infrastructure-as-code`, not `iac`; `pulumi-cloud`, not `pulumi-service`; `announcements`, not `pulumi-news`; `dotnet`, not `c#`/`.net`; `google-cloud`, not `gcp`). Tags are lowercase and hyphen-delimited. Unlike categories, the tag list is curated-but-open: only mint a new tag when nothing in the vocabulary fits, and only add a cloud-provider or feature tag if we expect multiple posts about it.

The vocabulary is grouped roughly as:

- **Pulumi:** `pulumi-cloud`, `pulumi-enterprise`, `pulumi-neo`, `copilot`, `esc`, `insights`, `automation-api`, `crossguard`, `announcements` (company news), `pulumi-events`, `pulumi-interns`, `releases`, `features`
- **Cloud providers** (multiple-posts rule): `aws`, `azure`, `google-cloud`, `digitalocean`
- **Languages:** `typescript`, `javascript`, `nodejs`, `python`, `go`, `dotnet`, `java`, `yaml`
- **AI:** `ai`, `ai-agents`, `llm`, `ml`, `mlops`, `claude`, `claude-code`, `mcp`
- **Kubernetes & containers:** `kubernetes`, `containers`, `docker`, `helm`, `eks`, `aks`, `gke`, `gitops`
- **Platform engineering:** `platform-engineering`, `internal-developer-platform`, `developer-portals`, `developer-experience`, `cloud-engineering`, `infrastructure-as-code`, `best-practices`
- **Security & governance:** `security`, `secrets`, `policy-as-code`, `compliance`, `governance`, `iam`, `rbac`, `oidc`
- **Scenarios:** `serverless`, `continuous-delivery`, `ci-cd`, `github-actions`, `devops`, `migration`, `testing`

**Series**

A *series* is an ordered reading path across multiple posts (the third axis, alongside categories and tags). Series are defined in [`data/blog_series.yml`](./data/blog_series.yml) and surfaced at [`/blog/series/`](https://www.pulumi.com/blog/series/). To add a post to an existing series, set its `series` front-matter value to the series `slug` — that single key is all that's needed. It drives the in-post "In This Series" sidebar (siblings are found via `.Params.series`), the `<Series Title>: Part N` badge shown on the post hero in place of the category badge, and membership on the series landing page at `/blog/series/<slug>/` (the `series` taxonomy generates that page automatically; `/blog/series/` links to it). Do **not** also add the slug to `tags` — that was the old workaround for building the landing page under the tags taxonomy, and `make lint` now fails if a series slug appears as a tag (it also fails if a post's `series` value isn't defined in the data file). To create a new series, add an entry to `data/blog_series.yml` (with `slug`, `title`, `description`, and optionally `prefix`/`meta_image`) and set `series` on each member post. Series are optional — most posts don't belong to one.

**Canonical link**

If you are posting a blog that originated somewhere else (for example, a syndicated community post) you will want to add the setting `canonical_url` for the URL where the blog post originated.

Additionally, if you're writing a blog post to announce a new product or feature that is also documented in our docs, you should set the `canonical_url` to point from the blog post to the relevant docs page. This helps consolidate optimization signals and ensures the docs page remains the primary source of truth in search engines.

**Pulumi Cloud availability**

If the post announces a feature that needs a paid Pulumi Cloud edition, set `pulumi_cloud_feature` to that feature's id from [`data/pulumi_pricing.yaml`](./data/pulumi_pricing.yaml):

```yaml
pulumi_cloud_feature: context-api
```

That renders the same violet availability callout the docs use ("This Pulumi Cloud feature is available in the Enterprise and Business Critical editions"), at the foot of the post. The edition it names is derived from the pricing data, so it can't drift from `/pricing/` the way a hand-written sentence does — **delete the sentence it replaces** rather than saying it twice. If the feature isn't in the data file yet, add it there first (with `hidden: true` if it isn't a marketed line item on `/pricing/`). An unknown id, an edition id, or a feature available on the Individual edition all fail `make lint`.

**Schema type (structured data)**

Blog posts automatically get BlogPosting schema for SEO. You can optionally override this with `schema_type` in frontmatter if needed (rare). See [SCHEMA.md](./SCHEMA.md) for details.

**Resource links**

To render a list of labeled, icon-accompanied links at the bottom of the post — docs, GitHub repo, feature request, community Slack, video, and so on — use the optional `resource_links` list. Each entry has a `type` (which maps to an icon and default label), a `url`, and an optional `text` to override the label:

```yaml
resource_links:
    - type: documentation
      url: /docs/iac/cli/
    - type: github
      url: https://github.com/pulumi/pulumi
    - type: slack
      url: https://slack.pulumi.com/
    - type: feature-request
      url: https://github.com/pulumi/pulumi/issues/new
      text: "Request this feature"      # optional; overrides the default label
```

The available `type` values and their icons/default labels are the single source of truth in [`data/blog_link_types.yaml`](./data/blog_link_types.yaml) (currently `documentation`, `registry`, `feature-request`, `issue`, `slack`, `github`, `video`, `discussion`). External URLs open in a new tab; internal ones don't. To add a new link type, add an entry to that data file. Prefer this over hand-writing a bulleted list of links at the end of the post.

**Updated date**

Set `updated: YYYY-MM-DD` to show an "Updated \<date\>" line next to the publish date in the hero. Use it when you materially revise an older post — leave the original `date` unchanged.

Use `updated`, **not** `lastmod`, for this. `updated` is the reader-facing field this site renders; `lastmod` is a generic Hugo built-in that only feeds the sitemap and schema.org `dateModified`, which the site already derives automatically from the commit date (`enableGitInfo: true`). A hand-stamped `lastmod` is invisible to readers and redundant with git, so don't add one.

**Draft**

Set `draft: true` to keep a post out of the built site. Note that a draft is visible **only** on your local dev server (`make serve`) — it's excluded from both PR previews and production, so it isn't a good way to share a post for review. See [How `draft` and `date` behave across environments](#how-draft-and-date-behave-across-environments) for the full matrix of how `draft` and `date` interact with local dev, PR previews, and production.

**Related posts**

The bottom of every post shows up to four related posts, auto-selected by Hugo's Related Content. To pin specific posts first, set `related_posts` to a list of post slugs (the folder names under `content/blog/`); Hugo fills any remaining slots automatically:

```yaml
related_posts:
    - my-earlier-post
    - another-relevant-post
```

**Author roles**

To label an author's role on the byline (for example, an interviewee credited "as told to"), set `author_roles` as a map of author id → label:

```yaml
author_roles:
    adam-gordon-bell: "as told to"
```

### Creating Author Profiles

If you don't already have a [TOML](https://github.com/toml-lang/toml) file [in the `team` directory](https://github.com/pulumi/docs/tree/master/data/team/team) of the repo, create one now. For Pulumi employees, that file should look something like this (your `id` can be any string, but we recommend `firstname-lastname`):

```toml
id = "christian-nunciato"
name = "Christian Nunciato"
title = "Software Engineer"
status = "active"

[social]
github = "cnunciato"
linkedin = "cnunciato"
x = "cnunciato"
```

For community contributors, it's mostly the same, but with a `status` of `guest`, and a more informative `title`:

```toml
id = "mikhail-shilkov"
name = "Mikhail Shilkov"
title = "Microsoft Azure MVP and early Pulumi user"
status = "guest"
...
```

The `social` section, and the items within it, are optional.

Once your team-member file's been created, add your author image at [`static/images/team`](https://github.com/pulumi/docs/tree/master/static/images/team). The image should be a square JPG (400x400 max) named with your author `id` (e.g., `christian-nunciato.jpg`).

Update the new post's `authors` property to use your author `id`. If you're still running the development server, you should see the change reflected in the browser immediately.

## Write Your Post

Once you've created your post structure with `/new-blog-post`, focus on writing great content. Posts are written in [Markdown](https://daringfireball.net/projects/markdown/) and rendered with [BlackFriday](https://github.com/russross/blackfriday), Hugo's default Markdown processor. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) guide is a helpful syntax reference if you need it. You can also include HTML in your posts, if you need greater control over the output than Markdown can provide.

For formatting guidelines, see [the Style Guide](./STYLE-GUIDE.md).

### Code Blocks

There are a couple of ways to do [syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/) in Hugo, but we generally recommend [code fences](https://gohugo.io/content-management/syntax-highlighting/#highlight-in-code-fences), along with an optional language specifier &mdash; e.g., for TypeScript:

<pre>
```typescript
let bucket = new aws.s3.BucketV2("stuff");
...
```
</pre>

[Additional languages are available](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages) as well.

### Media

#### Inline Images

To add images to the body of your post, first place them within the folder containing the post's Markdown file (e.g., at `blog/my-new-post/platypus.png`), then reference them relatively:

```
![The humble platypus](platypus.png)
```

Readers can click an image to see it full size in an overlay, but only where that actually helps: an image gets the treatment when the overlay could draw it meaningfully bigger than the post does, so screenshots and other detail-heavy images become clickable while icons, badges, and images already shown at their full size stay plain. That's decided in the browser from the image's own dimensions — there's nothing to add to your Markdown. If you have an image that qualifies but shouldn't be clickable, add `data-no-lightbox` to it (or to a wrapping element) in raw HTML.

The same applies to videos added with the [`video` shortcode](#video) below, which is worth knowing when you record one: a clip shot at 1080p is being squeezed into the ~768px content column, and readers can open it at full size, so record at a comfortably higher resolution than the column rather than at the column's width. The enlarged copy always gets playback controls, even though the clip in the post body has none, so readers can pause and scrub there. Clips you give `controls="true"` are left out of this altogether — their controls already include a fullscreen button.

#### Social ("Meta") and Feature Images

> [!IMPORTANT]
> If you are adding _any_ logos to the images, you must absolutely ensure these are current. Using a wrong or outdated logo can have a severe negative impact on social sharing timelines due to caching.

When you generate a new post, the `feature_image` field is included but left blank:

- **`feature_image`** — A high-resolution hero image (1884×1256) displayed in the blog listing and at the top of the blog post page. It also drives the post's **social/OpenGraph card** (the 1200×628 image used in Twitter cards, unfurled Slack links, etc. and on the blog home page), which is generated on-brand at **build time** from the post title + feature image. You no longer create or commit a separate `meta_image` — leave it blank.

**Every published post needs a feature image**, with two exceptions: posts in the catch-all `general` category (SEO comparisons, "what is X" explainers — lower-touch by design) and drafts (`draft: true`), where the image lands before you undraft. Without one, the post-page hero and the listing cards show **no image** — the title and metadata simply span the full width (most pre-redesign posts are like this, and those are grandfathered). Only the build-time social card falls back to a generic branded plate; the on-page layout no longer shows a placeholder.

If you'd like a custom-designed feature image, label your PR with `needs-design` and a designer will create one for your post. Alternatively, use the `/blog-feature-image` command in Claude Code to generate one automatically from a curated set of branded templates.

| Field           | Recommended Size | Aspect Ratio | Format | Background               |
| --------------- | ---------------- | ------------ | ------ | ------------------------ |
| `feature_image` | 1884×1256        | 3:2          | PNG    | Opaque (No Transparency) |

Add your image to the post's directory and set `feature_image` to its filename before submitting your post. Never commit a placeholder image.

> [!NOTE]
> **Don't set a custom `meta_image`.** You should almost never need one — the build-time card covers virtually every post and keeps social previews on-brand automatically, including when the brand evolves. A hand-made override is frozen in time: it drifts off-brand silently, which is exactly why hundreds of older posts needed cleanup. If you want a nicer card, invest in a better feature image (label your PR `needs-design` for a custom-designed one). If the generated card genuinely doesn't work for your post, raise it in [#blogs](https://pulumi.slack.com/archives/CCBFCGU94) before committing an override.

> **Archived images:** older posts that shipped an off-brand `meta_image` have had it renamed to `meta-legacy.png` and removed from front matter; it now appears in a collapsed "Archived feature image" panel at the bottom of the post.

#### Video

To embed a YouTube video, you can use Hugo's built-in [`youtube` shortcode](https://gohugo.io/content-management/shortcodes/#youtube), which takes the video's YouTube ID, obtainable from its public URL on youtube.com:

```plain
{{< youtube "kDB-YRKFfYE?rel=0" >}}
```

For videos belonging to the [Pulumi YouTube channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), you'll usually want to append the `?rel=0` query parameter as well (as above), which tells YouTube to limit the suggestions it makes at the end of a video to those from the same YouTube channel. [Learn more about player parameters here](https://developers.google.com/youtube/player_parameters).

#### GitHub Repository Cards

To embed a GitHub repository preview card, use the `github-card` shortcode with the repository in `owner/repo` format:

```plain
{{< github-card repo="pulumi/pulumi" >}}
```

This renders a clickable card showing the repository's Open Graph image, which includes the repository name, description, stars, language, and other metadata. The card links directly to the repository on GitHub.

#### Neo Cards

To embed a card linking to Pulumi Neo with a pre-filled prompt, use the `neo-card` shortcode:

```plain
{{< neo-card title="Migrate your CDK application" >}}
{{< neo-card title="Migrate your CDK application" prompt="Leverage the cdk-to-pulumi skill to migrate my CDK application to a Pulumi application" >}}
{{< neo-card title="Try Neo" subtitle="Get started" prompt="Help me create infrastructure" >}}
```

**Parameters:**

- `title` (required): The main text displayed on the card
- `prompt` (optional): The prompt sent to Neo (defaults to title if not specified)
- `subtitle` (optional): The smaller text above title (default: "Start a Neo task")

This renders a card with the Neo icon, subtitle, title, and a chevron arrow. Clicking the card opens Pulumi Neo with the specified prompt.

#### CTA Cards

To place a "Program the Cloud" call-to-action card in the body of a post, use the `blog/cta-card` shortcode. Every parameter is optional, so a bare, self-closed shortcode renders the generic get-started card (the self-closing `/>` is required when you omit the body):

```plain
{{< blog/cta-card />}}
```

Add a contextual title, body copy, and/or button to tailor the ask to the post's topic:

```plain
{{< blog/cta-card title="Ship Kubernetes faster" label="Get started free" href="/docs/get-started/" >}}
Manage your clusters with real code — loops, functions, and your IDE, not YAML templates.
{{< /blog/cta-card >}}
```

**Parameters:**

- `title` (optional): The card's eyebrow heading (default: "Program the Cloud")
- `label` (optional): The button label (default: the site's primary CTA, "Get started")
- `href` (optional): The button destination (default: the site's primary CTA link)
- Body (optional): The card's body copy; falls back to the default get-started copy when empty.

Place the card yourself, wherever it reads best — usually at a natural section break past the middle of the post. There's no auto-insertion; a post gets a card only if you add one.

**When to add one:** the card suits evergreen, search-and-discovery content (comparisons, best-practices guides, how-to tutorials, explainers) of at least ~800 words. Skip it on very short posts, where it overwhelms the content, and on time-bound announcement or news content — funding, partnerships, brand milestones, year-in-review recaps, and `category: company` posts generally — where a "get started" ask is off-topic.

#### Event and Post Cards

To point readers at an event or another blog post, embed its card with the `blog/card` shortcode instead of describing it in a CTA card. Pass one content path:

```plain
{{< blog/card "/events/neo-in-a-docker-sandbox/" >}}
{{< blog/card "/blog/pulumi-neo/" >}}
```

This is the same tile the [events list](/events/) and the blog homepage use, so the card pulls its title, date, location, presenters, and blurb from the target page — nothing to restate and nothing to go stale. An event card also flips its own CTA from "Register" to "Watch" once a recording is added to the event page, so a post that outlives the event still links somewhere useful.

A card is always full width, so it's one card per shortcode — several in a row is simply several shortcodes. The path is the only parameter: there's no title or body copy to set, so anything you want to say about a card goes in the prose around it. Paths must be absolute and resolve to a page under `/events/` or `/blog/` — a typo fails the build rather than dropping the card silently.

Reach for `blog/cta-card` instead when you're linking somewhere without a card (docs, a product page, a signup) or writing a generic get-started ask.

#### Animated GIFs

GIFs are welcome, but should be optimized. In general, animated GIFs should be no more than 1200 pixels wide and 3 MB in size. If you need help optimizing your GIF, consider [Gifsicle](https://www.lcdf.org/gifsicle/); it's available through Homebrew and has an easy-to-use command-line API. For example, to resize (e.g., downscale) and optimize a GIF in place:

```bash
gifsicle ./my-animation.gif --resize-width=1200 --optimize=3 --batch
```

## Review and Publish

Before submitting your post:

1. **Review for quality**: Run `/docs-review` in Claude Code to check for style and content issues
2. **Add borders to images**: If you have screenshots, run `/add-borders` to add 1px grey borders for better visual clarity
3. **Preview locally**: Run `make serve` and check your post at <http://localhost:1313/blog/[your-slug>]
4. **Add a feature image**: Add a 1884×1256 hero image (or run `/blog-feature-image`) and set `feature_image` to its filename; it also drives the build-time social card (see [feature image guidelines](#social-meta-and-feature-images) above)
5. **Submit for review**: Create a Pull Request against the `master` branch
6. **Publicize**: Before merge, reach out in [#blogs](https://pulumi.slack.com/archives/CCBFCGU94) so Marketing can help broadcast your post

Once merged to master, your post will go live on <https://www.pulumi.com/> (after its publish date).

## A Note on Dates and Scheduling for Future Publishing

### How `draft` and `date` behave across environments

Two front-matter fields decide whether a post is visible: `draft` (a boolean) and `date` (the publish timestamp). What they do depends on *where* the site is being built, because each environment passes Hugo a different combination of `--buildDrafts` and `--buildFuture`:

| Environment | Command | `draft: true` | Future `date` |
|---|---|---|---|
| **Local dev** (`make serve`) | `hugo server --buildDrafts --buildFuture` | Visible | Visible |
| **PR preview** (and the `testing` deploy) | `hugo --buildFuture` | Hidden | Visible |
| **Production** (`www.pulumi.com`) | `hugo` (no draft/future flags) | Hidden | Hidden |

So, in practice:

- **`draft: true`** shows up only on your local dev server. It is excluded from PR previews and production alike, which makes it a poor way to share work-in-progress for review — a reviewer looking at the PR preview URL won't see the post at all. Remove `draft` (or set it to `false`) before you expect the post to appear on the preview.
- **A future `date`** shows up locally and in PR previews, but **not** in production. This is Hugo's standard "future publishing" behavior: production is built without `--buildFuture`, so a post dated ahead of the build time is simply left out until its date arrives.

To preview a future-dated post locally *as production would render it* (future content hidden), run the dev server with future builds disabled:

```zsh
BUILD_FUTURE=false make serve
```

### Why you can't schedule to a precise time

Because the website is deployed in response to a commit to pulumi/docs `master`, it isn't possible to schedule a post to publish automatically at a precise date and time. A future `date` keeps the post out of production, but production only rebuilds when something lands on `master` — so the post goes live at the **next build that happens after its date has passed**, not at the moment the clock ticks over. To publish a future-dated post on time, you (or a scheduled/manual deploy) must trigger a build once the date is in the past. See the [Merging and Releasing section of the README](README.md#merging-and-releasing) for details.

## Publishing Checklist

- [ ] Use `/new-blog-post` in Claude Code to create your post (or see [Appendix](#appendix-creating-blog-posts-manually) for manual method)
- [ ] Check for a break `<!--more-->` after the first paragraph, and ensure that your post's introduction looks right on the blog home page
- [ ] Run `/docs-review` to check for style and content issues
- [ ] Run `/add-borders` if your post includes images
- [ ] Set a `feature_image` (required unless the post is `category: general` or `draft: true`), and check that it appears properly on the blog home page and at the top of the post. Do not use animated GIFs
- [ ] If your feature image includes logos, confirm they are the current Pulumi/partner logos (the build-time social card is generated from the feature image)
- [ ] Preview locally with `make serve`. Check formatting, links, and images for appearance
- [ ] Use the [Twitter card validator](https://cards-dev.twitter.com/validator) to check how the blog appears in a tweet (use the preview provided in the PR)
- [ ] Reach out in [#blogs](https://pulumi.slack.com/archives/CCBFCGU94) to make Marketing aware that your post is about to go live!
