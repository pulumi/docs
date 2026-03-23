# Hackathon: Docs Markdown Output (March 2026)

## Goal

Make Pulumi docs serve clean markdown for AI agents and terminal users. Add a Hugo custom output format that renders docs pages as markdown instead of HTML, with a fallback for unimplemented shortcodes. Addresses [#17898](https://github.com/pulumi/docs/issues/17898).

## Branch

`CamSoper/hackathon` in pulumi/docs

## Architecture

### Hugo custom output format

Each shortcode gets a `.markdown.html` template variant. Hugo selects the variant based on the output format being rendered. The base page templates (`layouts/docs/single.md`, `layouts/docs/list.md`) emit raw markdown content.

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
| 2 | Scaffold output format, base templates, fallback stubs | Not started |
| 3 | `chooser`, `choosable`, `choosable-inline` templates | Not started |
| 4 | High-priority shortcodes: `notes`, `get-started-stepper`, `example-program`, `langfile`, `cleanup`, etc. | Not started |
| 5 | `pulumi docs` CLI command (pulumi/pulumi repo, parallel) | Not started |

## Key gotchas

- **No single fallback**: Hugo requires a `.markdown.html` file per shortcode — Session 2 must generate stubs for all 108.
- **Extensionless shortcodes**: `langcode` and `langname` have no `.html` extension. Verify Hugo handles output format variants for these.
- **Hardcoded chooser markup**: ~40 shortcodes (`pulumi-*`, `policy-*`, `langfile`, `compfile`, etc.) embed `<pulumi-chooser>` HTML directly rather than nesting `{{< chooser >}}`. Their markdown variants must emit comment delimiters independently.
- **Prior work**: Joe Duffy's PR [#16998](https://github.com/pulumi/docs/pull/16998) added then removed a markdown output format. Commits `de3e8a22e7` (add) and `0d83a565d2` (remove) are useful reference for Session 2.

## Key files

- `SHORTCODE-AUDIT.md` — full shortcode inventory with tiers, usage counts, session assignments
- `config/_default/config.yml` (lines 34–54) — existing output format config
- `layouts/index.txtfull.txt` — existing non-HTML output format (pattern reference)
- `layouts/shortcodes/` — all 108 shortcode templates
- `layouts/docs/single.html` / `list.html` — current HTML page templates
