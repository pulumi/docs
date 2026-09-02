# AGENTS.md — Pulumi website (Hugo): docs, blog, marketing, and example programs

---

## Build / Test / Lint Workflow

> **Note:** For comprehensive details on the build system, deployment infrastructure, and CI/CD workflows, see `BUILD-AND-DEPLOY.md`. This file is large, so read only specific sections as needed to conserve tokens.

> **Never push directly to `master`.** Always create a branch and open a PR. Direct pushes to `master` bypass review and CI checks. (Server-side branch protection is planned but not yet in place.)

Agents must use these exact commands:

- Install deps: `make ensure`
- Build site: `make build`
- Serve locally on port 1313 (accessible with curl):  
  - Normal: `make serve` 
  - With asset rebuilds: `make serve-all`
- Lint: `make lint` (must pass before commit/merge)
- Lint prose: `make lint-prose` (Vale; nags, never blocks. Also surfaces in pinned PR reviews.)
- Format: `make format`
- Run all tests: `make test`
- Run the review pipelines' own test suites: `make test-review-pipeline` (pytest + standalone harnesses + every `--self-test`; required if you touch `scripts/content-review/`, `scripts/blog-review/`, or `.claude/commands/docs-review/scripts/`)
- Run specific program test:  
  `ONLY_TEST="program-name" ./scripts/programs/test.sh`
- Fix trailing spaces:  
  `sed -i '' 's/[[:space:]]*$//' file1.md file2.md ...`

Do not substitute other tools or commands, or change `package.json` to use pnpm (Yarn/npm only).

---

## Code & Content Rules

For all content files, Pulumi's **voice, tone, prose, product naming, and grammar** are defined in the **Pulumi brand guide** ([brand.pulumi.com](https://brand.pulumi.com/)), which is also exposed to agents through the public **brand MCP server**. Consult the relevant section (voice, writing style, or terminology) before writing or reviewing — the **terminology** section is the canonical reference for product/feature names and the retired names never to use again. `STYLE-GUIDE.md` covers only this site's Hugo/repo mechanics (shortcodes, links, navigation, code fences, etc.) and points to the brand guide for each topic it doesn't own. If the brand MCP is unavailable, fall back to the offline Vale mirror in `styles/Pulumi/` — which mirrors the same terminology — and say so in your review or PR body rather than working from memory. If a rule is in neither, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style). Do not invent new style conventions; ask for clarification if something is ambiguous.

**Precedence:** wherever the brand guide overlaps with anything in this repo — these conventions, `STYLE-GUIDE.md`, or any skill (including the social, SEO, and AEO guidance that still lives in this repo), the brand guide takes priority. That specialized guidance stays in the repo for now; if the brand guide later grows its own, the brand guide's version wins.

Meta files like this one, `BUILD-AND-DEPLOY.md`, and agent instruction/skill files (e.g., `.claude/commands/*.md`) are exempt from formatting rules (heading case, trailing newlines, etc.).

For all content files (docs, blogs, changelog entries, etc.):

- **Markdown**: Must always end with a newline.
- **Headings**: Sentence case at every level (H1 included), and sentence case for nav menu labels. See the brand guide's [writing style](https://brand.pulumi.com/voice/writing-style/) section. Hugo heading mechanics (one H1, FAQ `?` exception) live in `STYLE-GUIDE.md`.
- **TypeScript/JavaScript**: Must follow `tsconfig.json` settings. No comments unless explicitly requested.
- **TypeScript program files** (`static/programs/`): Use hand-written constructor style — resource name and opening `{` on the same line, `}, {` inline when an opts argument follows:
  ```typescript
  const r = new SomeResource("name", {
      prop: value,
  }, { 
      provider: p,
  });
  ```
  Do NOT use Prettier's multi-arg style where name, props, and opts are each on separate indented lines.
- **File Placement**:  
  - Docs go under `content/docs/...`
  - Blog posts go under `content/blog/...`
  - Other content goes into appropriate `content/...` subdirectory
  - Code examples go under `/static/programs` with a language suffix in the filename.  
  - Mirror the structure of existing content; do not invent new layouts.
- **Includes**: Use Hugo shortcodes for shared content, never raw Markdown copy-paste.  
- **Naming**: Product, feature, and category names — canonical casing, preferred terms, retired names — come from the brand guide's terminology section. Never introduce a name from memory: check the retired-names table first (e.g. it's Pulumi Discovery now, not “Pulumi Insights”; Pulumi Neo, not “Copilot”). Non-proper nouns stay lowercase (“stack,” not “Stack”).  
- **Ordered Lists**: Every item begins with `1.` to minimize diff noise.
- **Diagrams**: Prefer Mermaid diagrams over ASCII art. The site renders Mermaid natively via a Hugo code block hook (`layouts/_default/_markup/render-codeblock-mermaid.html`). Use ` ```mermaid ` fenced code blocks. See [Mermaid docs](https://mermaid.js.org/) for syntax.
- **Images on template-driven pages**: Place new images for template-driven pages (homepage, product pages, event pages, case studies — anything rendered through `layouts/partials/template-partials/*`) under `assets/fingerprinted/`, mirroring the path you'd use under `static/`. The template partials route every `<img>` through `layouts/partials/fingerprinted-img.html`, which content-hashes filenames, converts rasters to WebP, and generates responsive `srcset`s. Frontmatter paths still look like `/images/foo.svg`; the partial resolves them. Missing assets cause a build panic, so there is no silent fallback. `meta_image` and assets used by non-template layouts can stay in `static/`.
- **Meta images**: `meta_image` is optional for `docs`, `case-studies`, `what-is`, `migrate`, `partner`, `topics`, `events`, and `blog` pages. Leave it blank and `scripts/generate-meta-images.mjs` produces an on-brand social card at build time (resolved by `layouts/partials/meta-image-url.html`). A page-level `meta_image` always wins, but custom overrides are discouraged — the generated card covers virtually every case and stays on-brand automatically. For blog posts the card is built from the post title + `feature_image` (generate the feature image with `/blog-feature-image`, or label the PR `needs-design` for a designer-made one); a post's off-brand legacy meta image, if any, was renamed to `meta-legacy.png` and shows in a collapsed "Archived feature image" panel.
- **Spelling/Grammar**: Always correct errors. Use American English spelling.

---

## Moving and Deleting Files

**⚠️ SEO CRITICAL**: Missing aliases on moved files break search rankings and external links.

Use the `/move-doc` skill for Hugo content files — it handles `git mv`, alias injection, link updates, and verification. For non-Hugo files (generated content, static assets), add S3 redirects in `/scripts/redirects/` (format: `source-path|destination-url`, place entries in topic-appropriate files). Manual move procedure and anchor-link caveats: see `.claude/commands/move-doc/SKILL.md`.

---

## Updating Internal Links

When moving documentation, aliases handle redirects automatically. Update internal links strategically:

- **DO update** links in `/content/docs/` and `/content/product/`.
- **`/content/blog/`** is historical — swap a broken link only for an equivalent replacement, and when the change is worth surfacing to readers stamp `updated: YYYY-MM-DD` (not `lastmod`); otherwise route around it with an alias/redirect. See "Dates: `updated` vs `lastmod`" below.
- **Link style**: links within `/docs/` must use the full canonical path (e.g. `/docs/iac/concepts/stacks/`). Never use parent-directory references (`../stacks/`) — they break when files move.

For find/sed implementation patterns, see `.claude/commands/move-doc/SKILL.md`.

---

## Navigation and llms.txt

The left nav is data-driven from `data/docs_menu_sections.yml`, which is consumed by `layouts/partials/docs/menu.html` (the rendered nav), `layouts/index.llms.txt` (the curated `/llms.txt` index), and `layouts/partials/llm-sitemap-walk.json` (the `/docs/llm-sitemap.json` machine-readable sitemap). When you add, remove, or reorder top-level nav sections, all three flow through automatically. Per-section descriptions in `/llms.txt` come from each landing page's `meta_desc` front-matter — edit the page if you need to change how it reads in the index.

---

## The Dev Center lives in another repo

`/dev` — tutorials, templates, community examples, and the glossary — is **not** in this repo. It ships from [pulumi/marketing-web](https://github.com/pulumi/marketing-web) (`apps/www`, an Astro build with its own S3 + CloudFront), and `infrastructure/index.ts` proxies `/dev*` to that distribution the same way it proxies `/registry` and `/guides`. Hugo's `content/tutorials/` and `content/templates/` trees were deleted when it launched; `scripts/redirects/dev-redirects.txt` 301s their URLs into `/dev`.

What that means when you work here:

- **Don't add tutorial or template content to this repo.** A new tutorial, a new template page, or a glossary term goes to pulumi/marketing-web. (The `glossary` shortcode and `data/glossary.toml` are a *different*, docs-only glossary rendered at `/docs/glossary/` — that one stays.)
- **Link to `/dev/tutorials/<slug>/`, `/dev/templates/<group>/[<cloud>/]`, and `/dev/glossary/<term>/`.** Never `/tutorials/` or `/templates/`; those only redirect.
- **`data/footer.yml` and `data/header_nav.yaml` are synced downstream.** marketing-web's `scripts/sync-content.mjs` reads both, so a nav or footer edit here also changes the Dev Center's chrome. Both carry one Dev Center entry pointing at `/dev/`; the Tutorials, Templates, and Pulumi guides entries collapsed into it.
- **Search does not cover the Dev Center.** Docs search indexes this repo and the Registry only; `/dev` has its own search at `/dev/browse`. `scripts/search/update-search-index.js` deliberately doesn't fetch `/dev/search-index.json`, and there is no Dev Center facet in the docs search UI.

---

## AI and agent positioning

Pulumi supports the full spectrum of AI agents, and content must never present Neo as the only way to use AI with Pulumi or frame Neo as an either-or choice against other coding agents.

- **Docs** (`content/docs/`, `content/what-is/`): community-centric and balanced. Third-party coding agents (Claude Code, Codex, Cursor, GitHub Copilot, etc.) working with Pulumi — through IaC, [Agent Skills](/docs/ai/skills/), and the [Pulumi MCP server](/docs/ai/mcp-server/) — are first-class. Neo is Pulumi's purpose-built infrastructure agent: the deepest integration and the fastest path to a great infrastructure agent out of the box, but one option on a spectrum, and most teams benefit from using both.
- **Product/marketing pages** (`content/product/`, homepage): may lead with Neo and sell it hard, but should still acknowledge that Pulumi's code-first approach works with the agent a reader already uses. Avoid copy that disparages other agents (e.g. "unlike generic AI tools").
- **When listing agent options** (e.g. in migration guides), follow the pattern in `content/docs/iac/guides/migration/migrating-to-pulumi/from-terraform.md`: list Neo alongside Claude Code, Cursor, and Codex as equally legitimate choices, with at most a light note on Neo's built-in advantage.

---

## Resource options

The reference pages under `content/docs/iac/concepts/resources/options/` show a classification callout (custom resource / component resource / both, plus per-SDK enforcement) rendered by the `resource-option-scope` shortcode. The classification data — and the summary table on that section's `_index.md` — is generated from `data/resource_options.yaml`, which is the single source of truth. **When you add a new resource option, you must add an entry to `data/resource_options.yaml` and place the `{{< resource-option-scope "<name>" >}}` shortcode on the new page.** That file's header comment is the authoritative step-by-step checklist; the build fails if a page references an option missing from the data file.

---

## Pulumi Cloud availability markers

Docs pages state which Pulumi Cloud edition a feature needs through a generated violet callout, not hand-written prose. A marker names a **feature**, never an edition — the edition the callout states is derived from that feature's availability in `data/pulumi_pricing.yaml` (see "Pricing data" below), so a feature that moves editions is a one-line edit that updates `/pricing/` and every marked page at once.

- **Whole page**: add `pulumi_cloud_feature: <feature-id>` to the front matter (for example `pulumi_cloud_feature: rbac`). `layouts/docs/{single,list}.{html,md}` renders the callout above the content. We only mark what a reader has to buy, so an unknown id, an *edition* id, `true`, `false`, and a feature that's available on the Individual edition are all hard lint failures (`checkPulumiCloudFeature` in `scripts/lint/lint-markdown.js`). An ungated page carries no key. The key names the feature because the value does, and to leave `cloud_feature` free for the cloud *provider* sense the word carries elsewhere.
- **One section**: put `{{< pulumi-cloud "<feature-id>" />}}` on the line **directly after** the heading it applies to. `scripts/search/page.js` relies on that adjacency to skip the callout when it builds a heading's search snippet. The no-argument form `{{< pulumi-cloud />}}` means "Pulumi Cloud, all editions" and is only for mixed pages where the reader can't otherwise tell a section needs Cloud at all; a block form with inner content renders orientation prose in the same box. `checkPulumiCloudShortcode` validates the argument against the same vocabulary as the front matter key.
- **If the feature isn't in the data file yet, add it there first.** Give it `hidden: true` when it isn't a marketed line item on `/pricing/` (gated deployments, ESC change requests, organization templates): hidden features stay out of the comparison table but remain resolvable by id.
- **Don't say it twice.** When you add a marker, delete the hand-written "only available in the Enterprise and Business Critical editions" sentence or note it replaces. The callout already links to `/pricing/`. Keep only prose that says something the callout doesn't (for example, a per-edition limit like "Enterprise allows up to 25 custom roles").
- Edition names are lowercase-noun in prose ("the Enterprise edition"). Never "Free", "Starter", or "Pro".

### Pricing data

`data/pulumi_pricing.yaml` is the single source of truth for **what Pulumi sells**: the ordered, closed set of editions (Individual, Team, Enterprise, Business Critical) with the display copy for their `/pricing/` cards, and a per-feature availability matrix. Its header comment is authoritative for the vocabulary ("edition", never "plan"/"tier"/"subscription") and for adding or renaming an edition or a feature. Everything downstream reads it: the `/pricing/` comparison table, the docs availability markers above, and the changelog `editions:` badges.

- **Availability is a map keyed by edition id**, not a positional array. `available_from: <edition>` is shorthand for false-below/true-from; `availability:` overlays specific editions on top of it. Availability must be monotone — the build fails otherwise.
- **`id` is required and unique across every category.** Names collide ("Self-hosting" appears under both IaC and ESC), so ids are not slugged from names; disambiguate with a product prefix (`esc-self-hosting`).
- **`requires:`** names the edition a marker should state when it differs from the first edition with a truthy cell — needed wherever the free column is a *limited variant* rather than the feature itself ("Manual" policy enforcement at Individual).
- **Order is the only ordering mechanism**, at every level. No `weight`, no sorting.
- **Validation is split by consumer**, matching `data/resource_options.yaml`: structural invariants (duplicate ids, unknown edition keys, non-monotone availability) are `errorf`s in `layouts/partials/pricing/data.html`, the partial that expands the file; frontmatter- and shortcode-facing invariants are in `scripts/lint/lint-markdown.js` so authors fail in `make lint` rather than in a full Hugo build. There is deliberately no third standalone validator script.
- **Grid classes on `/pricing/` are literal strings selected by edition count.** Tailwind v4 content-scans `layouts/**/*.html` as raw text and PurgeCSS is gone, so a class assembled with `printf` is never emitted and the grid collapses to one column. Adding an edition means adding a case to the dicts at the top of `layouts/page/pricing.html`.

Callout markup for all callout types (`info`, `tip`, `warning`, `cloud`, and the GitHub-alert types) comes from the shared `layouts/partials/notes.html`. The `{{% notes %}}` shortcode takes a **named** `type` argument only — `{{% notes "warning" %}}` is silently ignored and renders an info box, so always write `{{% notes type="warning" %}}`. Adding a new callout type means adding it to the `$icons` dict in that partial **and** adding a `&.note-<type>` block to both `theme/src/scss/_notes.scss` and `theme/src/scss/docs/_docs-theme.scss` — dark mode is not automatic.

**Callouts inside a list item**: use the `{{< notes >}}` form, indented to the item's continuation column. `{{%` shortcode output is spliced back into the markdown source before it is rendered, so an indented `{{% notes %}}` always lands at column 0 and splits the list in two (restarting the numbering); `{{<` is substituted after the markdown pass, so the callout stays inside the `<li>`. The shortcode strips the body's common indentation either way, so indent the body to match the tags.

---

## Blog categories and tags

Blog posts carry three taxonomy axes (`category` and `tags` are always present; `series` is optional):

- **`category`** — the *kind* of post. This is a **closed** set defined in `data/blog_categories.yaml` (the single source of truth read by `scripts/lint/lint-markdown.js`). Category is **required** and **singular**: every post declares exactly one `category:` scalar value. Use the best-fitting specific kind, or **`general`** (the default) for posts that don't fit cleanly (e.g. SEO comparisons or "what is X" explainers — those rely on tags instead). `make lint` fails on a missing value, a list value, or a value outside the set. **Do not invent categories** — pick an id from the data file. To add/rename one, edit `data/blog_categories.yaml` in a PR and raise it in #blogs. The blog docs-review additionally flags posts that landed in a specific kind but really belong in `general` (and vice versa).
- **`tags`** — the *topical* axis (clouds, languages, products, scenarios). Curated-but-open, **not** build-enforced. Reuse a tag from the canonical vocabulary in `data/blog_tags.yaml` and **avoid near-duplicates** (`kubernetes` not `k8s`, `infrastructure-as-code` not `iac`, `pulumi-cloud` not `pulumi-service`, `dotnet` not `c#`/`.net`). Tags are lowercase and hyphen-delimited.
- **`series`** — the optional *reading-path* axis. A post joins a series with a single `series: <slug>` scalar key, where the slug is defined in `data/blog_series.yml`. Series are their own taxonomy: term pages render at `/blog/series/<slug>/` and the directory at `/blog/series/`. Do **not** also add the slug to `tags` — `make lint` fails on a series slug used as a tag, and on a `series:` value that isn't defined in the data file.

See `BLOGGING.md` for the author-facing version of these rules.

Per-post optional front matter beyond the taxonomy axes — `resource_links` (icon links at the foot of the post), `related_posts` (pinned related slugs), `author_roles`, and `updated` — is documented in `BLOGGING.md`. The blog homepage is curated separately in `data/blog_home.yaml` (`featured` = the four hero/featured slots; `featured_series` = the "Popular series" strip); that file's header comment is the authoritative reference.

### Embedding events and posts in a post body

To promote an event or another post from inside a post, embed its card with `{{< blog/card "/events/<slug>/" >}}` — **do not hand-write a `blog/cta-card`** that restates the title, date, and blurb. Those copies rot: the shortcode renders the same tiles as `/events/` and the blog homepage, derived entirely from the target page, so an event card picks up a retitled session or a newly added recording (Register → Watch) on its own. A card is always full width, so it takes exactly one path — several in a row is several shortcodes — and the path is its only parameter: there is no title or body copy to set. Reserve `blog/cta-card` for destinations that have no card (docs, product pages, signup) and for generic get-started asks.

Card layouts live in `layouts/partials/blog/card/` — `medium` (grid tile), `contained` (`medium` boxed in a `.card`), `wide` (text left, square image right; the homepage feed's card view **and** in-body embeds), `small`, `featured`, `series`, `list-row`. Reuse one; don't clone its markup into a new partial. `wide` renders only its wrapper's contents and takes the wrapper's classes as a param, because the homepage row starts `hidden` (the view toggle flips it to flex) while an embed is a boxed `.card`.

### Images and videos in a post body

Post-body images and `{{< video >}}` clips open in a lightbox when — and only when — enlarging them would show the reader more. `theme/src/ts/blog-lightbox.ts` measures each one in `.blog-post-content` against the viewport (intrinsic size vs. rendered size vs. the size the overlay could draw it at) and wraps the ones that qualify in a trigger button; the overlay shell is `layouts/partials/blog/lightbox.html`, rendered by `layouts/blog/single.html`. Nothing about this is author-driven: **do not add a wrapping link, a `figure`, or a per-image opt-in** to make something clickable, and don't hand-roll a second modal. The escape hatch runs the other way — `data-no-lightbox` on the element or any ancestor keeps it plain. A post-body video that already has `controls` is skipped entirely: a wrapping button would swallow clicks meant for the control bar, and those controls already offer fullscreen. (The overlay's own copy of a video always has controls, and is exempt from click-to-close for the same reason.)

The thresholds live at the top of the TypeScript file with the reasoning for each; tune them there rather than special-casing a post. Two of them, `OVERLAY_MARGIN_X`/`OVERLAY_MARGIN_Y`, mirror the overlay's padding and its caption budget — **if you change the spacing in `lightbox.html`, change them to match**, or the script will promise an enlargement the overlay can't deliver.

### Dates: `updated` vs `lastmod`

When you revise an existing blog post, use **`updated: YYYY-MM-DD`** — not `lastmod`. This is the established convention (the vast majority of revised posts use it) and the one wired to the UI: `layouts/blog/single.html` renders `.Params.updated` as the visible "Updated \<date\>" line beside the publish date. Leave the original `date` unchanged; set `updated` to the revision date. It's the same field documented in `BLOGGING.md`.

**Do not reach for `lastmod`.** It's a Hugo built-in that only feeds the sitemap and schema.org `dateModified`, and the site already sets `enableGitInfo: true` (`config/_default/config.yml`), so Hugo derives `.Lastmod` from the commit date automatically. A hand-stamped `lastmod` is therefore invisible to readers *and* redundant with git. It's easy to default to because `lastmod` is the generic Hugo idiom for "last changed" — but on this site the reader-facing, canonical field is `updated`.

### Blog known-issues index (automated daily review)

A scheduled workflow (`.github/workflows/blog-review-index.yml`) reviews a few existing blog posts per day — selected deterministically by `scripts/blog-review/select-posts.py` (traffic/GSC-weighted staleness; oldest-unreviewed-first until the blog data exports ship) — and records structured findings (dead links, factual rot, deprecated products, thin content) into an S3 known-issues index. It is **flag-only state, not content**: nothing is committed to the repo, no fixes are applied, and no PRs are opened. State lives in the content-review ledger bucket under the `blog-review/` prefix (`ledger/`, `index/`, `runs/`, and `index/_summary.json`); the on/off/cadence switch is the `BLOG_REVIEW_COUNT` repo variable (unset = 5 posts/run, `'0'` = off). The review skill is `.claude/commands/blog-review-index/SKILL.md`; its closed issue taxonomy lives in that skill's `references/issue-taxonomy.md` and is enforced by `scripts/blog-review/validate-findings.py`. The index is evidence for a future, human-reviewed process that marks rotted, low-value posts `block_external_search_index: true` — do not add that frontmatter based on the index without going through that process.

---

## Case studies

Case studies live at `content/case-studies/<slug>.md` — scaffold a new one with `hugo new content/case-studies/<slug>.md` (uses `archetypes/case-studies.md`). Rules that trip people up:

- **`industry`** — required, singular, closed set defined in `data/case_study_industries.yaml` (`make lint` enforces it). That file's header comment is the authoritative reference.
- **Logo tile** — the cards on `/case-studies/` and the industry term pages render each logo centered on a brand-color tile, driven by optional front matter (`logo_bg_color`, `logo_style: white|dark`, `logo_size: lg`, `card_logo`), all documented in `layouts/partials/case-studies/card.html` and format-checked by `make lint`.
- **`customer_logo` is not card-only**: it also renders on **light backgrounds** in the case-study page's quote panel (`layouts/case-studies/single.html`) and the template-page partials (`layouts/partials/template-partials/template-case-study-{cards,grid}.html`). Never point it at a white/light asset — put dark-background variants in `card_logo` instead.

---

## Events

Event pages live at `content/events/<slug>/index.md` — a bundle whose content is entirely frontmatter; the schema's source of truth is `archetypes/event/index.md` (its comments are kept current). **Create a new event with the `/create-event` skill** (`.claude/commands/create-event/SKILL.md`): it collects details from the prompt or an interactive wizard, scaffolds the bundle, generates social cards via `/event-meta-image`, files the pulumi/marketing tracking issue from its issue template, and opens the docs PR. It supports `--dry-run` (writes issue/PR previews instead of touching GitHub) and delegates execution to the `event-creator` subagent (`.claude/agents/event-creator.md`). HubSpot form and Salesforce campaign IDs come back from marketing on the tracking issue — never invent them; a gated page carries TODO placeholders until they land, then a rerun of `/create-event <issue-url>` wires them in.

---

## Releases changelog entries

Individual changelog items live in `content/releases/changelog/` — one markdown file per entry, listed by month on `/releases/` and rendered at `/releases/changelog/<slug>/` (`layouts/changelog/single.html`). Shared images/videos live in the `images/` and `videos/` subfolders and are referenced by absolute path (e.g. `/releases/changelog/images/2026-06-18-foo.png`), so entry renames don't affect them.

- **Filenames must be `YYYY-MM-DD-<slug>.md`**, and the date prefix must match the frontmatter `date:`. `make lint` enforces both (`checkChangelogFilename` in `scripts/lint/lint-markdown.js`) — a mismatch or non-prefixed name is a hard build failure.
- **Assets in `images/` and `videos/` must also be date-prefixed** as `YYYY-MM-DD-<slug>.<ext>` (use the referencing entry's date). `make lint` enforces this too (`checkChangelogAssets`). Rename the asset and update its reference together.
- **Create a new entry with the `/new-changelog` skill** (or `hugo new --kind changelog content/releases/changelog/YYYY-MM-DD-<slug>.md`, which uses `archetypes/changelog.md`). The archetype derives `title` and `date` from the filename.
- **Optional `editions:`** is a YAML array marking Pulumi Cloud edition availability, rendered as badge(s) beside the date. Values are edition **ids** from the closed set in `data/pulumi_pricing.yaml` (`individual`, `team`, `enterprise`, `business-critical`), enforced by `checkChangelogEditions` in `scripts/lint/lint-markdown.js`; the templates look the id up and render the display name, so write `business-critical`, not `Business Critical`. List **every** edition the feature is available in — since a lower edition implies the ones above it, that means the lowest applicable edition and all editions above it (e.g. an Enterprise feature lists both `enterprise` and `business-critical`). The legacy `tiers:` array and singular `tier:` scalar are hard build failures: "tier" isn't a word the product uses, and the old list carried a `Free` value for an edition that doesn't exist.
- **Renaming an entry** (changing its slug) changes its URL, so add an `aliases:` entry pointing at the old `/releases/changelog/<old-slug>/` path — same SEO rule as moving any content file.

---

## Styling (CSS / SCSS / Tailwind)

The theme uses Tailwind v4 (configured in CSS, no `tailwind.config.js`) across two SCSS bundles: `theme/src/scss/main.scss` (docs/app) and `theme/src/scss/_marketing.scss` (marketing).

### Reuse the shared system first

Before writing new component CSS, use the shared design-system primitives in **`theme/src/scss/shared/`** (see `shared/README.md`). Don't reinvent a button, card, badge, or heading:

- **`.btn` button system** (`shared/_button.scss`) — `class="btn btn-primary"`, plus variants (`outline`, `secondary`, `ghost`, `ghost-primary`, `destructive`, `link`), sizes (`btn-sm`/`btn-lg`/`btn-icon`…), and `.btn-split`/`.btn-group`. The file header documents the full compose API.
- **`.card` / `.card-hover`** (`shared/_card.scss`).
- **Form system** (`shared/_forms.scss`) — `class="form-input form-input-lg"`, plus `form-textarea`/`form-select`/`form-checkbox`/`form-radio` and `form-label`/`form-help`/`form-error`. Control heights mirror the `.btn` size scale. Also exposes `@mixin`s (`form-control-base`, …) for form-consuming partials.
- **`.badge` system** (`shared/_badge.scss`) — `class="badge badge-success"`, `layouts/partials/badge.html`, or `@extend .badge; @extend .badge-<variant>;`.
- **Shared type scale** (`shared/_utilities.scss`) — the `heading-xl`/`heading-1`…`heading-6`, `body-sm`…`body-2xl`, and `font-overline` `@utility` classes. Use these instead of hand-rolling font-size/weight/tracking.

Compose them in markup, or in SCSS via `@apply`/`@extend` (prefer `@extend`ing a primitive over re-`@apply`ing its utilities).

### Order of preference for authoring styles

1. **Inline Tailwind utility classes** — including arbitrary values (`bg-[#abc123]`, `w-[42ch]`, `grid-cols-[1fr_auto]`). This is the default for one-off styling.
2. **SCSS with Tailwind `@apply` / `@extend`** — only when inline classes can't stay DRY (the same cluster of utilities repeated across many elements or templates). Reach for `@extend` on a shared primitive first.
3. **Raw CSS / SCSS** — last resort, for what Tailwind genuinely can't express.

The Dark mode section below applies these same rules to `/docs` theming (`dark:` variants and `--docs-*` tokens).

---

## Dark mode (/docs)

The `/docs` section supports a light/dark/system theme toggle. Dark is **light-first**: light is the baseline (unchanged from before) and dark is a pure override. The whole system lives in `theme/src/scss/docs/_docs-theme.scss` (read its header comment first) and is driven by semantic `--docs-*` tokens defined on `body.section-docs` and re-pointed under `html[data-theme="dark"]`. It is scoped entirely to docs pages; nothing here can affect a non-docs page.

### Design tokens (colors)

Brand color hex values come from [`@pulumi/design-tokens`](https://github.com/pulumi/pulumi-design-system) (`tokens/core/primitives.json`, `palette-semantics.json`). The Hugo theme translates JSON to Tailwind v4 CSS variables — do not edit generated files by hand.

| File | Role |
|------|------|
| `theme/scripts/build-color-theme.mjs` | Reads design-tokens JSON, writes `theme/src/generated/tailwind-v4/_theme.scss` |
| `theme/src/scss/_theme.scss` | Imports generated palette + docs-specific tokens (breakpoints, `docs-*` colors) |
| `theme/src/scss/docs/_docs-theme.scss` | Docs light/dark semantic overrides (`--docs-bg`, `--docs-fg`, etc.) |

**Regenerate after bumping `@pulumi/design-tokens`:**

```bash
cd theme && yarn install && yarn build:color-theme
```

Typography in the generated theme block is local for now — not yet sourced from design-tokens JSON. See the design-system repo `AGENTS.md` for the full token index.

**You must test both modes whenever you add or restyle a visible element on a docs page** — new partials, shortcodes, cards, callouts, buttons, icons, or any markup that introduces its own colors, backgrounds, borders, or images. Toggle dark mode (theme switcher at the bottom of the docs sidebar) and confirm the element is legible and on-brand in both. Pure content changes (prose, code samples, frontmatter, links) are safe and don't need a dark-mode pass.

When something needs dark-mode work, prefer the existing levers over hand-written one-off colors:

- **Use Tailwind `dark:` variants.** The `dark:` variant is wired to the docs `data-theme` attribute (`@custom-variant dark` in `theme/src/scss/main.scss`), so `dark:bg-gray-900`, `dark:text-white`, etc. work directly in templates and are automatically scoped to `/docs`. This is the most direct way to dark-style a new element.
- **Use the semantic tokens.** Paint with `var(--docs-fg)`, `--docs-fg-muted`, `--docs-bg`, `--docs-bg-alt`, `--docs-surface`, `--docs-border`, `--docs-card`, `--docs-link`, `--docs-ring` rather than raw `--color-*` scales — they flip automatically. For selectors shared with non-docs pages, use the `var(--docs-TOKEN, ORIGINAL)` fallback form so light source files stay untouched.
- **Lean on the automatic flips.** There are three. `--color-violet-primary` is re-pointed to `violet-300` in the dark block, so `text-violet-primary`, `bg-violet-primary`, `border-violet-primary`, and any `var(--color-violet-primary)` get dark mode for free (solid `.btn-primary` is the exception, and pins `violet-700`). `h1`–`h6` and `p` are flipped on the element itself, since `@layer base` sets their color directly. And a bare `border` / `border-t` picks up the dark hairline, because `*` re-points the preflight default border color. **Nothing else is automatic** — no other `--color-*` scale is remapped, so `text-gray-950`, `bg-white`, `bg-gray-50`, and an explicit `border-gray-200` (which beats the `*` default on specificity) all render identically in both modes and need their own `dark:` variant. Surfaces styled via Tailwind `@apply` (e.g. content `.btn-*` variants) carry no literal class either, and need their own dark override in `_docs-theme.scss`.
- **Theme-aware images:** use the `layouts/partials/docs-logo.html` partial (light asset + optional `-on-dark.svg`), not a bare `<img>`, for any logo/mark whose colors don't read on a dark background. Masked icons in `_icons.scss` tint automatically; `background:url()` colored marks do not.

---

## Workflow Skills

Before starting any documentation task, check `.claude/commands/` for a relevant skill — there are well-structured skills covering common tasks like creating docs, reviewing PRs (see `.claude/commands/docs-review/SKILL.md`), moving files, and more. To see a full inventory, run `.claude/commands/docs-tools/scripts/scrape-metadata.py`.

**Non-Claude agents**: If the user runs a slash command or issues a short command that could be a skill name (e.g., `fix-issue`, `new-doc`), look for a matching file in `.claude/commands/` to guide your actions.

---

## PR Lifecycle for AI-Assisted Contributions

Open as draft, mark ready when done. Each ready-transition fires one full review; thrashing draft → ready → draft burns budget. Leave AI authoring trailers in commits (`Co-Authored-By: Claude ...`) — stripping them is bad form and changes nothing about which review runs. Don't delete `<!-- CLAUDE_REVIEW N/M -->` comments — the re-entrant pipeline edits them in place. A small push that only touches lines carrying outstanding findings refreshes the stale review automatically; otherwise, mention `@claude #update-review` (fix-response / dispute / re-verify) or transition through draft and back to ready. Bare `@claude` (no hashtag) is for ad-hoc help, not for refreshing the review.

**Shipping a PR includes finishing its review.** A PR is done when every finding the pre-merge review raised — 🚨 blockers, ⚠️ low-confidence findings, and ✏️ style suggestions alike — has been fixed, refuted, deferred to a filed issue, or explicitly accepted with a stated reason. Clearing 🚨 and stopping is not a shortcut; it is the failure mode the pipeline's own outcome telemetry measures (`ignored_low_confidence` in `scrape-review-outcomes.py`).

Agents: treat this as expected behavior on every PR you open here, asked for or not. Use the **`/address-review`** skill (`.claude/commands/address-review/SKILL.md`) — offer to watch for the review when the PR goes ready for review, walk **every** finding with the user when it lands, and say so plainly (once, then drop it) when a merge would leave items undecided. `python3 .claude/commands/docs-review/scripts/review-worklist.py --pr <N> --state .review-worklist-<N>.json --require-clean` is the machine answer to "is anything still open?"

For the full mechanics — refresh-pattern details, short-circuit thresholds, classifier internals — see `CONTRIBUTING.md` §AI-assisted contributions.
