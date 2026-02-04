---
user-invocable: false
---

# Frontmatter Templates

Complete YAML frontmatter templates for creating regular and index documentation pages.

## Regular Page Template

Use this template when creating standard documentation pages:

```yaml
---
title_tag: "{title_tag}"
meta_desc: "{meta_desc}"
title: {title}
h1: {title}
meta_image: {meta_image}
menu:
  {section}:
    name: {title}
    parent: {parent_identifier}
    weight: {weight}
aliases: []
---

## Overview

[Start writing here]

## Next steps

- [Related page 1](#)
- [Related page 2](#)
```

## Index Page Template

Use this template when creating index pages (_index.md) with sections:

```yaml
---
title: {title}
linktitle: {linktitle}
docs_home: true
notitle: true
norightnav: true
menu:
  {section}:
    identifier: {identifier}
    weight: {weight}
    parent: {parent}  # Only if subsection
meta_desc: "{meta_desc}"
meta_image: {meta_image}
h1: {h1}
description: {description_html}
link_buttons:
  primary:
    label: {primary_label}
    link: {primary_link}
  secondary:  # Only if provided
    label: {secondary_label}
    link: {secondary_link}
sections:
- type: button-cards
  heading: {heading}
  cards:
  - emoji: {emoji}
    heading: {card_heading}
    description: {card_description}
    link: {card_link}
---
```

## Usage Notes

- Replace all `{variable}` placeholders with actual values gathered during workflow
- For index pages, ensure these flags are set: `docs_home: true`, `notitle: true`, `norightnav: true`
- Menu section = first directory under `/docs/` (e.g., `/docs/iac/...` → section: `iac`)
- Aliases array should be empty `[]` for new pages (only populated for moved files)
- Weight should be multiples of 10 for easy insertion of pages later
- Secondary button is optional - omit the entire `secondary:` block if not needed
