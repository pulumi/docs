# OpenAPI Tag Intros

Markdown fragments rendered at the top of each generated tag page under
`/docs/reference/cloud-rest-api/{tag}/`, above the endpoint list.

## Convention

- One file per tag, named `<slug>.md` where the slug is the tag's URL slug —
  the same slug used in the tag-page URL. The page generator runs tags
  through `urlize` after inserting spaces into CamelCase names (e.g.
  `CloudSetup` -> `Cloud Setup` -> `cloud-setup`), so the file for the
  `CloudSetup` tag must be `cloud-setup.md`.
- YAML frontmatter holds a `meta_desc` field — a 1-2 sentence description
  of the API area, used as the tag page's `<meta name="description">` and
  as the list-item description on the cloud-rest-api landing page. Keep
  `meta_desc` to plain text (no Markdown links) — it renders unescaped.
- Body is Markdown. Headings (`##`, `###`) and lists are fine; they render
  inside the page above the auto-generated endpoint sections.
- Keep the body editorial: purpose of the API area, when to use it, links
  to related conceptual docs. Endpoint descriptions belong in the OpenAPI
  spec itself.

Example:

```markdown
---
meta_desc: Short 1-2 sentence summary used by SEO and the landing-page list.
---

Longer editorial intro that renders at the top of the tag page.

See [related concept docs](/docs/...) for getting-started guides.
```

## Orphan checks

The build warns (via Hugo `warnf`) when:

1. A tag in the spec has no matching intro file (prose gap).
2. An intro file has no matching tag in the spec (dead file — tag was
   renamed or removed).

Grep the build output for `openapi:` to see current gaps.
