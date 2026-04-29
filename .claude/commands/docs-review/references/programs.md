---
user-invocable: false
description: Review criteria for testable example programs under static/programs/.
---

# Review — Programs

Applied to changes touching `static/programs/`. These are real, testable Pulumi programs -- the bar is compilability and correctness, not just style. See `CODE-EXAMPLES.md` for the testing harness and directory conventions.

---

## Scope

- **Whole-program read** is mandatory whenever a program file is changed. Compilability cascades -- a missing import in one file breaks the whole project.
- Pre-existing extraction is **always on** for touched programs.

## Criteria

Apply `docs-review:references:shared-criteria` first, plus `docs-review:references:code-examples` for snippet-level concerns (imports, language idioms, API currency, casing). Then the following program-specific checks.

### Project structure

- **`Pulumi.yaml` present** at the program root, with a `name`, `runtime`, and (if applicable) `description`.
- **Dependency manifest present** per language:
  - TypeScript/JavaScript: `package.json` (+ `package-lock.json` or `yarn.lock`)
  - Python: `requirements.txt` or `Pipfile`
  - Go: `go.mod` and `go.sum`
  - C#: `*.csproj`
  - Java: `pom.xml`
- **All source files present.** The file for the default entry point (`index.ts`, `__main__.py`, `main.go`, `Program.cs`, `src/main/java/myproject/App.java`, `Pulumi.yaml` for YAML) must exist.
- **Language-suffix directory convention.** Programs live under `<name>-<language>` directories (see `CODE-EXAMPLES.md` §Directory naming conventions). If a PR adds a new language variant, the directory naming and the Hugo shortcode reference both must line up.

### Multi-language consistency

When a PR adds a new language variant of an existing program:

- Sibling-program naming and structure match (same `<name>` prefix, same file layout per language).
- The new variant implements the **same resources** with the **same properties**. Drift here produces multi-language chooser widgets that show materially different programs.
- The Hugo shortcode reference in the docs page picks up all language variants via the `path=` parameter; no separate per-language shortcode calls.

## Pre-existing issues (always on)

Compilability cascades. If one file in a program is broken, the program doesn't build -- so pre-existing extraction is always on for touched programs. Render findings in 💡 per [`output-format.md`](output-format.md); cap at 15 per file.

Scope of pre-existing findings for programs: broken/unused imports, out-of-date provider API surface, missing project-structure files, mismatched resource properties across language variants.

## Compilability check

If the touched program is **not** in `scripts/programs/ignore.txt`, the interactive entry point ([`SKILL.md`](../SKILL.md)) may run:

```bash
ONLY_TEST="program-name" ./scripts/programs/test.sh
```

The CI entry point ([`ci.md`](../ci.md)) does **not** run program tests directly -- those run as part of the main `make test` job. Cite that job's result in the review if available; do not re-run.

## Fact-check

Invoke [`fact-check.md`](fact-check.md) with:

- **Files:** the changed `static/programs/**` files (and any README/docs that reference them, if changed in the same PR)
- **Scrutiny:** `heightened` (code correctness matters)

CI fact-check is public-sources-only -- see `ci.md`.

## Do not flag

- **Prettier-style formatting on hand-written constructor code.** The TypeScript constructor style is an intentional deviation from Prettier defaults (see AGENTS.md). Don't "fix" it; don't propose Prettier refactors.
- **Dependency pins that match sibling programs' pins.** If `aws-s3-bucket-typescript` pins `@pulumi/aws` to `^6.0.0` and this PR's new variant does the same, don't flag -- it's a deliberate choice for consistency.
- **Idiomatic patterns for the language.** If the program uses `async`/`await` in TypeScript and you'd personally prefer `.then()` chains, that's a preference, not a finding.
- **"Consider adding error handling."** Example programs deliberately skip production-grade error handling to keep the example readable. Flag when the example *claims* to handle an error (but doesn't), not when it simply doesn't demonstrate error handling.
- **Extra resources that would "round out" the example.** `static/programs/` is scoped to the minimum-reproducible demo; don't propose additional resources that aren't in the program's name or description.
- **Provider-schema deltas already accepted in sibling programs.** If sibling programs under the same name already use a deprecated property form and haven't been updated, flag at most once (or surface as a pre-existing issue) -- do not flag every sibling.
