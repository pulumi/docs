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

Apply [`shared-criteria.md`](shared-criteria.md) first. Then the following program-specific checks.

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

### Imports

- **Resolve.** Every imported package / module exists in the dependency manifest.
- **Package names are correct.** TypeScript imports from `@pulumi/aws`, not `@pulumi/pulumi-aws`. Python imports `pulumi_aws`, not `pulumi-aws`. Go imports the module path declared in `go.mod`.
- **Symbols exist in the package.** `new aws.s3.BucketV2(...)` requires `BucketV2` in `@pulumi/aws`. A typo or a v2-only symbol used in a v1-pinned project is a 🚨 finding.
- **No unused imports.** A teaching example with an unused import is confusing and a lint failure waiting to happen.

### Idiomatic per language

Per the AGENTS.md rules:

- **TypeScript hand-written constructor style.** Resource name and opening `{` on the same line; `}, {` inline when an opts argument follows. Do NOT accept or propose Prettier's multi-arg style (each argument on its own indented line).
  ```typescript
  const r = new SomeResource("name", {
      prop: value,
  }, {
      provider: p,
  });
  ```
- **Python:** context managers for resources that support them; `pulumi_aws.s3.BucketV2(...)` call style; type hints where they aid reading.
- **Go:** `pulumi.Run(func(ctx *pulumi.Context) error { ... })` top-level; `ctx.Error()` / `return` on errors; `pulumi.String(...)` / `pulumi.StringArray(...)` wrappers for resource arguments.
- **C#:** `Pulumi.Deployment.RunAsync<MyStack>()` pattern; `Output<T>` / `Input<T>` correctly typed.
- **Java:** `Pulumi.run(ctx -> { ... })` top-level; `Output.of(...)` wrappers where needed.
- **YAML:** follows the current Pulumi YAML schema; no deprecated keys.

Don't flag cosmetic style (line length, trailing commas when the language allows them, brace placement when it matches the AGENTS.md convention). Flag actual anti-patterns that would teach the reader wrong habits.

### Provider API currency

- **Resource types exist.** `aws.s3.BucketV2` vs `aws.s3.Bucket` -- current provider major versions have deprecated the bare `Bucket` in favor of `BucketV2`. A program using the deprecated form is a pre-existing finding at minimum.
- **Required properties set.** Every resource's constructor must supply the properties the provider's schema marks as required.
- **Enum values valid.** `InstanceType`, `StorageClass`, and similar enum-typed properties must use values the provider schema accepts.
- **Verify against the schema.** For any resource API claim, cross-reference against the provider's current schema source (`gh api repos/pulumi/pulumi-<provider>/contents/provider/cmd/...`). Don't reason from memory.

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
