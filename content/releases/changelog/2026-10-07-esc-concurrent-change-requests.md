---
title: "Concurrent change requests in Pulumi ESC"
date: 2026-10-07
meta_desc: Multiple people can now open change requests on the same Pulumi ESC environment at the same time, without blocking one another.
authors:
    - christian-nunciato
---

Pulumi ESC [change requests](/docs/esc/concepts/approvals/) now support concurrent edits. More than one person can open a change request against the same environment at the same time, review and approve independently, and apply their changes without waiting for someone else's request to land first.

This makes change requests far more practical for busy teams sharing a single environment, where several people often need to propose updates in parallel.

To learn more, read the [announcement post](/blog/esc-concurrent-change-requests/).
