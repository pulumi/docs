---
title: "Change your components, keep your infrastructure"
date: 2026-09-25
meta_desc: Pulumi now supports state migrations for components, so you can evolve a reusable component without replacing the infrastructure it manages.
authors:
    - christian-nunciato
---

You can now ship breaking changes to a reusable Pulumi [component](/docs/iac/concepts/components/) without forcing a replacement of the infrastructure it manages. Component *state migrations* let you attach a callback to a component that rewrites its state as the component's shape changes — splitting a resource in two, renaming a child, or moving managed state around — so existing stacks upgrade cleanly instead of destroying and recreating resources.

Migrations are available through resource options in Go, Python, and Node.js, run automatically on the next update, and are reported as part of your regular preview and update diagnostics.

To learn more, read the [announcement post](/blog/component-state-migrations/) or the [state migrations documentation](/docs/iac/guides/building-extending/components/state-migrations/).
