---
user-invocable: false
description: Review criteria for testable example programs under static/programs/.
---

# Review — Programs

Applied to changes touching `static/programs/`. These are real, testable Pulumi programs — the bar is compilability and correctness, not just style.

> **v1 status — skeleton.** Until Session 2 fills this in, fall back to the `/static/programs/` bullets in [`review-criteria.md`](review-criteria.md).

---

## Scope

- Whole-program read is mandatory whenever a program file is changed. Compilability cascades — a missing import in one file breaks the whole project.
- Pre-existing extraction is **always on** for touched programs.

## Criteria

Pending — inherits from the `/static/programs/` bullets in [`review-criteria.md`](review-criteria.md) until Session 2 fills this in. Key axes:

- Project structure complete (`Pulumi.yaml`, dependency files, all source files)
- Imports resolve (correct package names, no unused imports, no missing ones)
- Resource API surface matches the provider's current schema (property names, types, required fields)
- Language-idiomatic conventions per the AGENTS.md rules (especially the hand-written constructor style for TypeScript)
- Examples handle errors appropriately and reflect realistic usage

## Pre-existing issues (always on)

Pre-existing scope per the programs-domain plan: broken/unused imports, out-of-date provider usage, missing project-structure files. Cap at 15 per file.

## Compilability check

If the touched program is **not** in `scripts/programs/ignore.txt`, the interactive entry point (`docs-review.md`) may run:

```bash
ONLY_TEST="program-name" ./scripts/programs/test.sh
```

The CI entry point (`docs-review-ci.md`) does **not** run program tests directly — those run as part of the main `make test` job. Cite that job's result in the review if available; do not re-run.

## Fact-check

Invoke [`pr-review/references/fact-check.md`](../pr-review/references/fact-check.md) with:

- Files: the changed `static/programs/**` files (and the README/docs that reference them, if changed in the same PR)
- Scrutiny: `heightened` (code correctness matters)

CI fact-check is public-sources-only — see `docs-review-ci.md`.
