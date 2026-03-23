# Shortcode Audit for Markdown Output Format

Audit of all 108 Hugo shortcodes in pulumi/docs, categorized for markdown output conversion.
Generated 2026-03-23 for hackathon Sessions 2–4.

## Complexity tiers

| Tier | Label | Markdown template strategy | Count |
|------|-------|---------------------------|-------|
| 1 | Passthrough | Emit `.Inner` as-is or with markdown formatting (e.g., `> **Note:**`) | 42 |
| 2 | Chooser | Emit `<!-- chooser -->` / `<!-- option -->` HTML comment delimiters | 40 |
| 3 | Content resolution | Read files from disk, emit as fenced code blocks | 8 |
| 4 | Structural/nav | Simplify to link list or use fallback "view on web" template | 18 |

## Master table

Sorted by docs usage count descending. Session column: 2 = scaffold only, 3 = chooser session, 4 = remaining high-priority, skip = use fallback template.

| Shortcode | Tier | Docs | Blog | Other | Total | Session | Notes |
|-----------|------|------|------|-------|-------|---------|-------|
| notes | 1 | 214 | 194 | 34 | 442 | 4 | Highest usage; blockquote with type prefix |
| choosable | 2 | 134 | 123 | 28 | 285 | 3 | Pairs with chooser |
| chooser | 2 | 113 | 123 | 28 | 264 | 3 | Core tab infrastructure |
| get-started-stepper | 4 | 51 | 0 | 0 | 51 | 4 | Prev/next nav; simplify to markdown links |
| example-program | 3 | 16 | 0 | 7 | 23 | 4 | Reads files by language from static/programs/ |
| langfile | 2 | 13 | 5 | 22 | 40 | 4 | Hardcoded chooser for entry-point filenames |
| get-started | 4 | 7 | 6 | 0 | 13 | skip | Card grid with cloud logos; fallback |
| cli-note | 1 | 4 | 0 | 0 | 4 | 4 | Static note about Pulumi Cloud login |
| compfile | 2 | 4 | 0 | 0 | 4 | 4 | Hardcoded chooser for component filenames |
| get-started-install-body | 1 | 4 | 0 | 0 | 4 | 4 | Static install heading + inner content |
| get-started-next-step | 1 | 4 | 0 | 0 | 4 | 4 | Parameterized anchor button |
| auto-naming-note | 1 | 4 | 0 | 0 | 4 | 4 | Static info note |
| saml-warning | 1 | 4 | 0 | 0 | 4 | 4 | Static info note |
| get-started-esc | 4 | 3 | 0 | 0 | 3 | skip | Tiled card grid; fallback |
| latest-version-esc | 3 | 2 | 0 | 1 | 3 | 4 | Reads static/esc/latest-version |
| latest-version | 3 | 2 | 1 | 0 | 3 | 4 | Reads static/latest-version |
| install-pulumi | 3 | 2 | 0 | 0 | 2 | 4 | Reads latest-version, chooser-based install cmds |
| install-python | 1 | 2 | 0 | 0 | 2 | 4 | Static install instructions |
| install-java | 1 | 2 | 0 | 0 | 2 | 4 | Static install instructions |
| example-program-snippet | 3 | 2 | 4 | 13 | 19 | 4 | Reads files with line range support |
| pulumi-apply | 2 | 2 | 0 | 0 | 2 | skip | Hardcoded chooser; 1 page; batch later |
| pulumi-command | 3 | 2 | 0 | 0 | 2 | skip | Reads CLI command file |
| pulumi-config-getsecret | 2 | 2 | 0 | 0 | 2 | skip | Hardcoded chooser; 1 page |
| pulumi-config-requiresecret | 2 | 2 | 0 | 0 | 2 | skip | Hardcoded chooser; 1 page |
| sso-scim-limits-info | 1 | 2 | 0 | 0 | 2 | 4 | Static parameterized text |
| video | 1 | 2 | 32 | 22 | 56 | skip | HTML video element; no markdown equiv |
| absurl | 1 | 1 | 0 | 0 | 1 | 4 | Pure text, trivial |
| changelog-table-row | 4 | 1 | 0 | 0 | 1 | skip | Complex table row; auto-generated content |
| esc-get-started-note | 1 | 1 | 0 | 0 | 1 | 4 | Static info note |
| get-started-note | 1 | 1 | 0 | 0 | 1 | 4 | Static info note |
| glossary | 4 | 1 | 0 | 0 | 1 | skip | Data-driven term list |
| identities | 4 | 1 | 0 | 0 | 1 | skip | Identity provider logo grid |
| install-dotnet | 1 | 1 | 0 | 0 | 1 | 4 | Static install instructions |
| install-go | 1 | 1 | 0 | 0 | 1 | 4 | Static install instructions |
| install-node | 1 | 1 | 0 | 0 | 1 | 4 | Static install instructions |
| kubernetesx-deprecated | 1 | 1 | 0 | 0 | 1 | skip | Deprecation warning; 1 page |
| language-null | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| md | 1 | 1 | 0 | 0 | 1 | 4 | Pure passthrough (.Inner → markdownify) |
| pulumi-all | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-bucket | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-config | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-config-get | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-config-require | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-getproject | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-getstack | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-host | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-language | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-new-bucket | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-output | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| pulumi-secret-new | 2 | 1 | 0 | 0 | 1 | skip | Hardcoded chooser; 1 page |
| skip-version-check | 1 | 1 | 0 | 0 | 1 | skip | Static note; 1 page |
| details | 1 | 0 | 0 | 1 | 1 | 4 | HTML details/summary → markdown |
| loadcode | 3 | 0 | 0 | 1 | 1 | 4 | Reads page resource, emits raw content |
| cleanup | 1 | 0 | 0 | 13 | 13 | 4 | Static teardown instructions (tutorials) |
| code-filename | 1 | 0 | 1 | 2 | 3 | 4 | Filename header + inner content |
| templates/pulumi-new | 4 | 0 | 0 | 17 | 17 | skip | Language chooser from frontmatter |
| tutorials/stepper | 4 | 0 | 0 | 17 | 17 | skip | Prev/next nav (tutorials dir) |
| blog/cta-button | 1 | 0 | 23 | 0 | 23 | skip | Blog-only CTA link |
| related-posts | 4 | 0 | 23 | 0 | 23 | skip | Blog-only; reads data/related.yaml |
| asciicast | 1 | 0 | 5 | 0 | 5 | skip | Blog-only; asciinema embed |
| github-card | 4 | 0 | 5 | 0 | 5 | skip | Blog-only; styled card |
| figcaption | 1 | 0 | 4 | 0 | 4 | skip | Blog-only; figure caption |
| gist | 1 | 0 | 3 | 0 | 3 | skip | Blog-only; GitHub gist embed |
| langhost | 2 | 0 | 1 | 1 | 2 | skip | Hardcoded chooser; 0 docs |
| langname | 2 | 0 | 1 | 1 | 2 | skip | Hardcoded chooser; 0 docs (extensionless file) |
| neo-card | 4 | 0 | 1 | 0 | 1 | skip | Blog-only; styled card |
| tutorials/create-new-proj | 1 | 0 | 0 | 2 | 2 | skip | Static paragraph; tutorials only |
| audio | 1 | 0 | 1 | 0 | 1 | skip | Blog-only; HTML audio |
| choosable-inline | 2 | 0 | 0 | 0 | 0 | 3 | Implement alongside chooser (0 current usage) |
| aws-eks-prereqs | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| aws-js-prereqs | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| aws-resource-note | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| azure-aks-prereqs | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| button-card | 4 | 0 | 0 | 0 | 0 | skip | Dead code (may be layout type) |
| button-cards | 4 | 0 | 0 | 0 | 0 | skip | Dead code (may be layout type) |
| challenge/open-form-button | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| cloud-intro | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| configure-gcp | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| console-note | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| example | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| examples | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| github-buttons | 4 | 0 | 0 | 0 | 0 | skip | Dead code |
| install-yaml | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| langcode | 2 | 0 | 0 | 0 | 0 | skip | Dead code (extensionless file) |
| language-int32 | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| multilang-tutorial-prereqs | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-args-getconfig | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-configschema | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-enforcementlevel-advisory | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-enforcementlevel-disabled | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-enforcementlevel-mandatory | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-enforcementlevel-remediate | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-reportviolation | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| policy-validateresource | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-componentresource | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-componentresource-registeroutputs | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-config-getnumber | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-config-getobject | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-customresource | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-input | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-input-nohref | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-log | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-new | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-output-nohref | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| pulumi-resource | 2 | 0 | 0 | 0 | 0 | skip | Dead code |
| resource-docs-alert | 3 | 0 | 0 | 0 | 0 | skip | Dead code |
| resource-providers | 4 | 0 | 0 | 0 | 0 | skip | Dead code |
| summary | 1 | 0 | 0 | 0 | 0 | skip | Dead code |
| templates/cloud-links | 4 | 0 | 0 | 0 | 0 | skip | Dead code |
| templates/service-links | 4 | 0 | 0 | 0 | 0 | skip | Dead code |

## Session assignments

### Session 2: Scaffold (no individual shortcodes)

- Hugo output format config (`config/_default/config.yml`)
- `layouts/docs/single.md` and `layouts/docs/list.md` base templates
- Fallback shortcode template (renders "view on web" link for unimplemented shortcodes)

### Session 3: Chooser family (3 shortcodes, 264+ files)

| Shortcode | Docs files |
|-----------|-----------|
| chooser | 113 |
| choosable | 134 |
| choosable-inline | 0 (implement for completeness) |

These three unlock markdown rendering for the majority of docs pages.

### Session 4: High-priority shortcodes (priority order)

| Priority | Shortcode | Tier | Docs files | Effort |
|----------|-----------|------|-----------|--------|
| 1 | notes | 1 | 214 | Trivial — blockquote with type prefix |
| 2 | get-started-stepper | 4 | 51 | Medium — prev/next as markdown links |
| 3 | example-program | 3 | 16 | Hard — file reading + language chooser |
| 4 | langfile | 2 | 13 | Easy — hardcoded chooser, new delimiters |
| 5 | cleanup | 1 | 0 docs / 13 tutorials | Trivial — static text passthrough |
| 6 | compfile | 2 | 4 | Easy — hardcoded chooser |
| 7 | example-program-snippet | 3 | 2 | Medium — follows example-program pattern |
| 8 | cli-note | 1 | 4 | Trivial |
| 9 | auto-naming-note | 1 | 4 | Trivial |
| 10 | saml-warning | 1 | 4 | Trivial |
| 11 | install-pulumi | 3 | 2 | Medium — reads version file + chooser |
| 12 | details | 1 | 1 | Trivial — details/summary |
| 13 | Remaining Tier 1 notes | 1 | 1-2 each | Trivial — batch convert |
| 14 | latest-version / latest-version-esc | 3 | 2 each | Easy — read file, emit string |
| 15 | loadcode | 3 | 1 | Easy — read page resource |
| 16 | install-* family | 1 | 1-2 each | Trivial |
| 17 | code-filename | 1 | 0 docs / 3 other | Trivial |

## Skip list

### Blog-only (0 docs usage)

`blog/cta-button`, `related-posts`, `asciicast`, `github-card`, `figcaption`, `gist`, `neo-card`, `audio`

### Visual/interactive with no markdown equivalent

`video` (2 docs), `changelog-table-row` (1 docs), `glossary` (1 docs), `identities` (1 docs), `get-started` (7 docs — card grid), `get-started-esc` (3 docs — card grid)

### Low-usage Tier 2 (hardcoded choosers, 0-2 docs pages each)

All `pulumi-*` shortcodes (30 total), all `policy-*` shortcodes (8 total), `langhost`, `langname`, `langcode`, `language-int32`, `language-null`, `example`, `examples`. These are used on 0-2 docs pages each. If the chooser family (Session 3) works correctly, these will automatically work since they just hardcode chooser markup — the fallback template will handle them until batch-converted.

### Dead code (0 total usage)

`aws-eks-prereqs`, `aws-js-prereqs`, `aws-resource-note`, `azure-aks-prereqs`, `button-card`, `button-cards`, `challenge/open-form-button`, `cloud-intro`, `configure-gcp`, `console-note`, `example`, `examples`, `github-buttons`, `install-yaml`, `langcode`, `language-int32`, `multilang-tutorial-prereqs`, `summary`, `templates/cloud-links`, `templates/service-links`, `resource-docs-alert`, `resource-providers` + 20 `pulumi-*`/`policy-*` shortcodes with 0 usage.

## Gotchas

1. **Hugo shortcode output format selection**: Hugo uses `{shortcode}.{outputformat}.html` naming convention (e.g., `chooser.markdown.html`). There is no single "default fallback" shortcode template — each shortcode that needs markdown output needs its own `.markdown.html` file. For the fallback strategy, Session 2 will need to generate stub files for every shortcode.

1. **Extensionless files**: `langcode` and `langname` have no `.html` extension — verify Hugo handles output format variants for these.

1. **Tier 2 shortcodes embed chooser HTML directly**: Shortcodes like `langfile`, `compfile`, `pulumi-*`, and `policy-*` hardcode `<pulumi-chooser>` / `<pulumi-choosable>` web component markup rather than nesting `{{< chooser >}}` / `{{< choosable >}}`. Their markdown variants need to emit the comment delimiters directly, independent of the chooser shortcode template.

1. **`templates/pulumi-new`**: Used in 17 "other" files (template pages). Generates chooser from frontmatter data. Worth investigating in Session 4 if time permits.

1. **Joe's removed work**: Commits `de3e8a22e7` (add) and `0d83a565d2` (remove) contain the prior markdown output format implementation. Useful reference for Session 2 scaffolding.
