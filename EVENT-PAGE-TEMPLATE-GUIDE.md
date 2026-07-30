# Event Landing Page Guide

Widget-based event marketing landing pages (e.g. `content/kubecon/`, `content/google-cloud-next/`) are **not** a separate system — they use the shared **template-page** section system, the same one that drives product pages under `content/product/`.

> For the workshop/webinar event *bundles* under `content/events/` (a different thing), see [EVENT-SOCIAL-CARDS.md](./EVENT-SOCIAL-CARDS.md).

## How it works

1. Set `type: page` and `layout: template-page` in the frontmatter.
2. Add a `sections:` array. Each item has a `type:` field (the section block to render) plus that block's fields. Sections render top-to-bottom in array order.
3. `layouts/page/template-page.html` → `layouts/partials/template-page-content.html` loops the array and dispatches each item to `layouts/partials/template-partials/template-<type>.html`.

The authoritative list of section `type`s and their fields is the header comment in [`layouts/partials/template-page-content.html`](layouts/partials/template-page-content.html). Section types commonly used on event pages: `hero`, `logo_banner`, `features`, `two_column`, `promo_banner`, `three_column`, `testimonial`, `location`.

## Example

```yaml
---
title: Meet the Pulumi team at KubeCon Europe | Booth 784
type: page
layout: template-page

sections:
  - type: hero
    layout: split
    title: Tame Kubernetes complexity with code
    # ...hero fields

  - type: logo_banner
    text: Trusted by over 4,000 innovative companies
    logos:
      - src: /logos/customers/deloitte.svg
        alt: Deloitte

  # ...more sections
---
```

See [content/kubecon/_index.md](content/kubecon/_index.md) for a complete, live example.

## Related

- **Section blocks**: [layouts/partials/template-partials/](layouts/partials/template-partials/) — one `template-<type>.html` per section type.
- **Building from a Figma design**: the [`figma-to-template-page`](.claude/commands/figma-to-template-page.md) skill maps a design to these sections and wires up the frontmatter.
