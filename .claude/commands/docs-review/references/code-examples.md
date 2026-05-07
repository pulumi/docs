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

## Cross-reference body-vs-code coverage

When a doc page's body advertises support for a language — via a comparison-table column header (`| TypeScript | Python | Go | C# | Java | YAML |`), a "Languages: TypeScript, Python, Go, C#, Java, YAML" prose row, or a recommendations list ("Pulumi supports authoring in X, Y, and Z") — the page must provide a runnable snippet for each advertised language. The snippet may live inline as a fenced code block in the page itself, OR via a `static/programs/<name>-<language>/` directory referenced from the body (e.g., through `{{< example-program >}}`).

A column or list claiming language support **without** a corroborating snippet is 🚨 (always-🚨 carve-out: the page promises something it doesn't deliver, and a reader filtering by language lands on a dead end). Quote the offending column header / row / list item and propose either (a) adding the missing snippet or (b) removing the language claim.

The `static/programs/` exemption from per-block specialist dispatch (§Subagent code-block dispatch below) does NOT block this cross-reference check. The specialist may inspect `static/programs/<name>-<language>/` directory contents to confirm a body claim — exemption applies to the per-snippet language-correctness review of each program file, not to the body-claim verification check that uses the program's existence as evidence.

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

For each fenced code block in a content file in the diff, spawn two parallel specialist subagents via the Agent tool. The split is by reasoning shape, not by axis: `structural` does language-level reasoning over the code-block context; `existence` does symbol/schema lookups against `pulumi/pulumi-<provider>` schema. Each specialist receives only its slice of the rules above plus the code block and its language declaration.

Files under `static/programs/` are **exempt** from specialist dispatch -- CI runs the test harness on every variant (parse + compile + import existence), which closes the always-🚨 carve-outs. The residual ⚠️-tier coverage (deprecation, idiomatic patterns, language-mismatched casing) is not worth the per-language-variant fan-out cost on PRs that touch many programs at once.

- **`structural`** (Sonnet 4.6, `general-purpose`) -- §Syntax + §Language-specific casing + §Idiomatic per language. Does the snippet parse in its declared language? Does property casing match the language convention in its tab? Do TypeScript constructors use the hand-written style; Python use context managers; Go use `pulumi.Run` + `pulumi.String(...)`; C# use `RunAsync<MyStack>`; Java use `Pulumi.run(ctx -> ...)`? Catches truncation, unclosed brackets, mismatched braces, broken indentation, missing language specifier on fenced blocks, language-mismatched casing, and non-idiomatic constructor/wrapper patterns. Includes the §Do not flag list verbatim so the specialist knows what cosmetic differences to skip.
- **`existence`** (Haiku 4.5, `general-purpose`) -- §Imports + §Provider API currency + §Cross-reference body-vs-code coverage. Do imported symbols exist in the cited package version? Do resource types, required properties, enum values, and methods/flags still exist in the current SDK and not as deprecated/renamed names? Verifies against `gh api repos/pulumi/pulumi-<provider>/contents/...` schema; flags typos, v2-only-symbols-in-v1-projects, and rejects `aws.s3.Bucket` in favor of `BucketV2`-tier carve-outs. Additionally checks **cross-reference coverage**: when the body or a comparison table advertises support for language X (a column header, a "Languages: TypeScript, Python, Go, C#, Java, YAML" row, a prose mention of supported languages), the specialist verifies a runnable X snippet exists — either inline in the page as a fenced block, or via a `static/programs/` directory referenced from the body. A column or list claiming support without a corroborating snippet is 🚨 (the static/programs/ exemption above does NOT block this cross-reference check; the specialist still inspects `static/programs/` *content* when needed to confirm a body claim).

Each subagent prompt copies *only* its slice rows verbatim, plus the code block and language declaration. Do **not** include `§Referenced static/programs/ snippets` (program-existence / per-language compilation -- main agent's combine step), `§Proposed fixes` (composition, not detection), or the other specialist's rows. Per-finding cap ~250 words.

### Combine step

1. **Dedup.** Key = `<file>:<line>` plus the first 40 characters of `finding_text` (lowercased, whitespace collapsed). Merge near-paraphrase matches; pick the most specific framing.
1. **Annotate.** Set `found_by: [<specialist>, ...]` from `structural`, `existence`. Single-specialist finds are the expected state -- the split is by reasoning shape, not redundancy -- and are not a confidence signal. When both specialists co-fire on the same code-block range (e.g., a `structural` truncation that also breaks `existence` on a now-missing import), set `cross_specialist_corroboration: true` -- a positive signal for compound-bug catches.
1. **Promote per existing carve-outs.** Per `docs-review:references:output-format` §Bucket rules carve-out list:
   - `structural` finds reaching "code does not parse in its language" -> 🚨 (always-🚨 carve-out).
   - `existence` finds reaching "imports / calls a symbol that does not exist in the referenced package version" -> 🚨 (always-🚨 carve-out).
   - All other findings default to ⚠️ unless the two-question test promotes them.
1. **Hand off.** Deduped, annotated list goes to the rendered review. Investigation-log dispatch metadata: `**Code-examples checks** -- "ran (2 specialists: structural, existence); N findings"` or `not run (no fenced code blocks in content files)`. When the diff contains only `static/programs/` changes, this is a `not run` -- CI's test harness is the gate.

No interim user output. Cross-block reasoning (e.g., `static/programs/<name>-<lang>/` compilation parity across language variants) stays with the main agent's combine step -- specialists see a single block at a time.
