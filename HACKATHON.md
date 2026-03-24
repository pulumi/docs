# Hackathon: Docs Markdown Output (March 2026)

## Goal

Make Pulumi docs serve clean markdown for AI agents and terminal users. Add a Hugo custom output format that renders docs pages as markdown instead of HTML, with a fallback for unimplemented shortcodes. Addresses [#17898](https://github.com/pulumi/docs/issues/17898).

## Branch

`CamSoper/hackathon` in pulumi/docs

## Architecture

### Hugo custom output format

Each shortcode gets a `.markdown.md` template variant (naming convention: `{name}.{formatName}.{mediaTypeSuffix}`). Hugo selects the variant based on the output format being rendered. The base page templates (`layouts/docs/single.md`, `layouts/docs/list.md`) use `{{ .RenderShortcodes }}` to emit raw markdown with shortcodes resolved, then apply a 6-phase regex pipeline to convert any remaining HTML to markdown.

Config adds a `markdown` output format:

```yaml
outputFormats:
  markdown:
    mediaType: text/markdown
    baseName: index
    isPlainText: true
    notAlternative: true
```

### Chooser delimiter convention

The chooser/choosable shortcodes use standardized HTML comment delimiters that the CLI can parse:

```
<!-- chooser: language -->
<!-- option: typescript -->
...content...
<!-- /option -->
<!-- option: python -->
...content...
<!-- /option -->
<!-- /chooser -->
```

Choosers are general-purpose (language, OS, cloud provider) — not just language tabs. The CLI prompts the user to select; non-interactive mode renders all options with headers.

### Fallback template

Unimplemented shortcodes render:

```
> This content is best viewed on the web. See: [Page Title](https://www.pulumi.com/path/)
```

This allows incremental rollout without implementing all 108 shortcodes at once.

### Content resolution

Shortcodes that include files (`example-program`, `loadcode`, `langfile`, `compfile`) must fully resolve their content. Hugo handles the include graph at build time — the markdown templates just need to emit fenced code blocks instead of `<div class="highlight">` HTML.

## Session plan

| Session | Scope | Status |
|---------|-------|--------|
| 1 | Shortcode audit (see `SHORTCODE-AUDIT.md`) | Complete |
| 2 | Scaffold output format, base templates, 28 real shortcode templates, dead code cleanup | Complete |
| 3 | Chooser/choosable family with HTML comment delimiters | Complete |
| 4 | Remaining shortcodes, HTML-to-markdown pipeline, LLM menu rewrite | Complete |
| 5 | `pulumi docs` CLI command (pulumi/pulumi repo) | Not started |

## Discoveries

- **Shortcode template naming**: Hugo uses `{name}.{formatName}.{mediaTypeSuffix}` — for `text/markdown` that's `.markdown.md`, not `.markdown.html`.
- **Dead shortcodes**: 41 shortcodes had zero usage across all content and were deleted.
- **`.RenderShortcodes`**: Hugo 0.117+ method that renders shortcodes through their output format-specific templates without running goldmark on the surrounding markdown. This is the key to clean output.
- **Markdown output scoping**: Output format must be enabled per-section via `cascade` in `content/docs/_index.md`, not globally — otherwise Hugo warns about missing layout files for marketing/blog pages.
- **LLM menu**: Replaced client-side TurndownService (~250 lines of DOM conversion) with `fetch()` to server-side `index.md`.

## Current state

- **760 markdown files** generated under `public/docs/`
- **13 pages** still have "best viewed on web" fallback (card grids, glossary, data-driven content)
- **69 live shortcodes** with `.markdown.md` templates (41 dead ones deleted)
- Separate PR for duplicate menu fix: [#18192](https://github.com/pulumi/docs/pull/18192)

## Key files

- `SHORTCODE-AUDIT.md` — full shortcode inventory with tiers, usage counts, session assignments
- `config/_default/config.yml` (lines 34–46) — output format config
- `content/docs/_index.md` — cascade enabling markdown output for docs section
- `layouts/docs/single.md` / `list.md` — markdown base templates with HTML-to-markdown pipeline
- `layouts/shortcodes/*.markdown.md` — 69 shortcode markdown templates
- `theme/stencil/src/components/llm-menu/llm-menu.tsx` — rewritten LLM menu component
