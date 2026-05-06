---
user-invocable: false
description: Snippet-level code review criteria — syntax, imports, language idioms, API currency. Applied wherever code appears in content (docs, blogs, programs).
---

# Code Examples

Applied to any code that appears in user-facing content: inline fenced blocks in docs and blogs, and source files in `static/programs/`. The bar is the same regardless of where the code lives — wrong code is wrong whether it's in a tutorial paragraph or a standalone program.

---

## Syntax

- **No unclosed brackets, broken indentation, or obvious typos.** A code block that doesn't parse in its language is a 🚨 finding.
- **Language specifier on every fenced block.** Without it, syntax highlighting is missing and the snippet looks broken in the rendered page.

## Imports

- **Imported symbols exist in the referenced package.** A typo or a v2-only symbol used in a v1-pinned project is a 🚨 finding.
- **Package names are correct.** TypeScript imports from `@pulumi/aws`, not `@pulumi/pulumi-aws`. Python imports `pulumi_aws`, not `pulumi-aws`. Go imports the module path declared in `go.mod`.
- **No unused imports.** A teaching example with an unused import is confusing and a lint failure waiting to happen.

## Language-specific casing

Pulumi resource properties follow language conventions:

- **TypeScript / JavaScript:** camelCase (`bucketName`, `versioningConfiguration`)
- **Python:** snake_case (`bucket_name`, `versioning_configuration`)
- **C# / Go:** PascalCase (`BucketName`, `VersioningConfiguration`)

When the same property appears in multiple language tabs (or a `chooser` block), every tab must use the correct casing for that language. Only flag when the casing is wrong for the tab it's in.

## Idiomatic per language

Per AGENTS.md and STYLE-GUIDE.md:

- **TypeScript:** `async`/`await` for promise-returning APIs. Hand-written constructor style (resource name and opening `{` on the same line; `}, {` inline when an opts argument follows). Do NOT accept or propose Prettier's multi-arg style.

  ```typescript
  const r = new SomeResource("name", {
      prop: value,
  }, {
      provider: p,
  });
  ```
  
- **Python:** Context managers for resources that support them. `pulumi_aws.s3.BucketV2(...)` call style. Type hints where they aid reading.
- **Go:** `pulumi.Run(func(ctx *pulumi.Context) error { ... })` top-level. `ctx.Error()` / `return` on errors. `pulumi.String(...)` / `pulumi.StringArray(...)` wrappers for resource arguments.
- **C#:** `Pulumi.Deployment.RunAsync<MyStack>()` pattern. `Output<T>` / `Input<T>` correctly typed.
- **Java:** `Pulumi.run(ctx -> { ... })` top-level. `Output.of(...)` wrappers where needed.
- **YAML:** Follows the current Pulumi YAML schema; no deprecated keys.

Don't flag cosmetic style (line length, trailing commas when the language allows them, brace placement when it matches AGENTS.md's hand-written constructor convention). Flag actual anti-patterns that would teach the reader wrong habits.

## Provider API currency

- **Resource types exist.** `aws.s3.BucketV2` vs `aws.s3.Bucket` — current provider major versions have deprecated the bare `Bucket` in favor of `BucketV2`. A program using the deprecated form is a pre-existing finding at minimum.
- **Required properties set.** Every resource's constructor must supply the properties the provider's schema marks as required. Examples that omit a required argument should be flagged — the example won't run.
- **Optional arguments are optional.** Examples that omit *optional* arguments should NOT be flagged — that's a style preference, not an error. Docs deliberately keep starter examples minimal.
- **Enum values valid.** `InstanceType`, `StorageClass`, and similar enum-typed properties must use values the provider schema accepts. A typo here means the example fails at preview time.
- **Verify against the schema.** For any resource API claim, cross-reference against the provider's current schema source (`gh api repos/pulumi/pulumi-<provider>/contents/provider/cmd/...`). Don't reason from memory.

## Referenced static/programs/ snippets

When a doc page or blog uses `{{< example-program >}}` or similar shortcodes pointing at `static/programs/`:

- **The referenced program must exist.** Check `static/programs/<name>-<language>/` for every language variant the page advertises.
- **Each variant must compile under its language.** See `CODE-EXAMPLES.md` for the testing contract.

## Proposed fixes

- **Proposed fixes must compile.** If you suggest a code replacement, it must itself pass every check above. Don't suggest untested code as a fix.
- **When in doubt, skip the fix.** Flag the issue without proposing a replacement rather than guess.

## Do not flag

- **Property-name casing that matches the language's convention.** `bucketName` in TypeScript is correct; `bucket_name` in Python is correct.
- **Code examples that omit optional arguments.** "You could also pass `tags: {...}`" is unsolicited enrichment.
- **CLI examples without paired output.** Not every code block needs a `output` block. Flag when the prose claims specific output and the block is missing; don't flag for "completeness."
- **Prettier-style formatting on hand-written constructor code.** TypeScript constructor style is an intentional deviation from Prettier defaults.
- **"Consider adding error handling."** Example programs deliberately skip production-grade error handling. Flag when the example *claims* to handle an error (but doesn't), not when it simply doesn't demonstrate error handling.

---

## Subagent code-block dispatch

*Fresh-review path only. Re-entrant updates use `docs-review:references:update` -- don't fan specialists across a fix-response / dispute / re-verify pass; the deltas are localized and replication beats decomposition there.*

For each code block in the diff (fenced block in a content file or a file under `static/programs/`), spawn four parallel specialist subagents via the Agent tool. The slices are non-overlapping by axis; each specialist receives only its slice of the rules above plus the code block and its language declaration.

- **`syntax`** (Sonnet 4.6, `general-purpose`) -- §Syntax. Does the snippet parse in its declared language? Catches truncation, unclosed brackets, mismatched braces, broken indentation, missing language specifier on fenced blocks.
- **`imports`** (Haiku 4.5, `general-purpose`) -- §Imports. Do imported symbols exist in the cited package version? Cheap structural lookup; flag typos and v2-only-symbols-in-v1-projects.
- **`idioms`** (Sonnet 4.6, `general-purpose`) -- §Language-specific casing + §Idiomatic per language. Per-language casing on resource properties + idiomatic patterns (TypeScript `async`/`await` + hand-written constructor style; Python context managers; Go `pulumi.Run` + `pulumi.String(...)` wrappers; C# `RunAsync<MyStack>`; Java `Pulumi.run(ctx -> ...)`). Includes the §Do not flag list verbatim so the specialist knows what cosmetic differences to skip.
- **`api-currency`** (Haiku 4.5, `general-purpose`) -- §Provider API currency. Does the resource type, required property, enum value, or method/flag still exist in the current SDK / not deprecated/renamed? Verifies against `gh api repos/pulumi/pulumi-<provider>/contents/...` schema; rejects `aws.s3.Bucket` in favor of `BucketV2`-tier carve-outs.

Each subagent prompt copies *only* its slice rows verbatim, plus the code block and language declaration. Do **not** include `§Referenced static/programs/ snippets` (program-existence / per-language compilation -- main agent's combine step), `§Proposed fixes` (composition, not detection), or other axes' rows. Per-finding cap ~250 words.

### Combine step

1. **Dedup.** Key = `<file>:<line>` plus the first 40 characters of `finding_text` (lowercased, whitespace collapsed). Merge near-paraphrase matches; pick the most specific framing.
1. **Annotate.** Set `found_by: [<specialist>, ...]` from `syntax`, `imports`, `idioms`, `api-currency`. Single-specialist finds are the expected state -- the slices are non-overlapping by axis -- and are not a confidence signal. When two specialists co-fire on the same code-block range (e.g., a `syntax` truncation that also breaks `imports`), set `cross_specialist_corroboration: true` -- a positive signal for compound-bug catches.
1. **Promote per existing carve-outs.** Per `docs-review:references:output-format` §Bucket rules carve-out list:
   - `syntax` finds reaching "code does not parse in its language" -> 🚨 (always-🚨 carve-out).
   - `imports` finds reaching "imports / calls a symbol that does not exist in the referenced package version" -> 🚨 (always-🚨 carve-out).
   - All other findings default to ⚠️ unless the two-question test promotes them.
1. **Hand off.** Deduped, annotated list goes to the rendered review. Investigation-log dispatch metadata: `**Code-examples checks** -- "ran (4 specialists: syntax, imports, idioms, api-currency); N findings"` or `not run (no code blocks in diff)`.

No interim user output. Cross-block reasoning (e.g., `static/programs/<name>-<lang>/` compilation parity across language variants) stays with the main agent's combine step -- specialists see a single block at a time.
