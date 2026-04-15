# OpenAPI Tag Intros

Markdown fragments rendered at the top of each generated tag page under
`/docs/reference/cloud-rest-api/{tag}/`, above the endpoint list.

## Convention

- One file per tag, named `<slug>.md` where the slug is the tag's URL slug —
  the same slug used in the tag-page URL. The page generator runs tags
  through `urlize` after inserting spaces into CamelCase names (e.g.
  `CloudSetup` -> `Cloud Setup` -> `cloud-setup`), so the file for the
  `CloudSetup` tag must be `cloud-setup.md`.
- No frontmatter — just Markdown. Headings (`##`, `###`) and lists are fine;
  they render inside the page above the auto-generated endpoint sections.
- Keep it editorial: purpose of the API area, when to use it, links to
  related conceptual docs. Endpoint descriptions belong in the OpenAPI
  spec itself.

## Orphan checks

The build warns (via Hugo `warnf`) when:

1. A tag in the spec has no matching intro file (prose gap).
2. An intro file has no matching tag in the spec (dead file — tag was
   renamed or removed).

Grep the build output for `openapi:` to see current gaps.
