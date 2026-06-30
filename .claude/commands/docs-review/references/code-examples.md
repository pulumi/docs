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

## Body↔code coverage

When a doc page's body advertises support for a language — via a comparison-table column header (`| TypeScript | Python | Go | C# | Java | YAML |`), a "Languages: TypeScript, Python, Go, C#, Java, YAML" prose row, or a recommendations list ("Pulumi supports authoring in X, Y, and Z") — the page must provide a runnable snippet for each advertised language. The snippet may live inline as a fenced code block in the page itself, OR via a `static/programs/<name>-<language>/` directory referenced from the body (e.g., through `{{< example-program >}}`).

A column or list claiming language support **without** a corroborating snippet is 🚨 (always-🚨 carve-out: the page promises something it doesn't deliver, and a reader filtering by language lands on a dead end). Quote the offending column header / row / list item and propose either (a) adding the missing snippet or (b) removing the language claim.

The `static/programs/` exemption from per-block specialist dispatch (§Subagent code-block dispatch below) does NOT block this body↔code check. The `body-code-coverage` specialist may inspect `static/programs/<name>-<language>/` directory contents to confirm a body claim — exemption applies to the per-snippet language-correctness review of each program file, not to the body-claim verification check that uses the program's existence as evidence.

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

Three specialists fan out in parallel. `structural` and `existence` dispatch **per fenced code block** (one subagent per block). `body-code-coverage` dispatches **once per content file** with the file body and the catalog of code blocks + cited `static/programs/` directories — its check is body-level, not block-level, and a per-block fan-out would lose the cross-language picture. Each specialist receives only its slice of the rules above.

Files under `static/programs/` are **exempt** from per-block specialist dispatch (`structural` + `existence`) -- CI runs the test harness on every variant (parse + compile + import existence), which closes the always-🚨 carve-outs. The residual ⚠️-tier coverage (deprecation, idiomatic patterns, language-mismatched casing) is not worth the per-language-variant fan-out cost on PRs that touch many programs at once. The exemption does NOT apply to `body-code-coverage`, which still inspects `static/programs/<name>-<language>/` directory contents to confirm body claims.

- **`structural`** (Sonnet 5, `general-purpose`) -- §Syntax + §Language-specific casing + §Idiomatic per language. Does the snippet parse in its declared language? Does property casing match the language convention in its tab? Do TypeScript constructors use the hand-written style; Python use context managers; Go use `pulumi.Run` + `pulumi.String(...)`; C# use `RunAsync<MyStack>`; Java use `Pulumi.run(ctx -> ...)`? Catches truncation, unclosed brackets, mismatched braces, broken indentation, missing language specifier on fenced blocks, language-mismatched casing, and non-idiomatic constructor/wrapper patterns. Includes the §Do not flag list verbatim so the specialist knows what cosmetic differences to skip.
- **`existence`** (Haiku 4.5, `general-purpose`) -- §Imports + §Provider API currency. Do imported symbols exist in the cited package version? Do resource types, required properties, enum values, and methods/flags still exist in the current SDK and not as deprecated/renamed names? Verifies against `gh api repos/pulumi/pulumi-<provider>/contents/...` schema; flags typos, v2-only-symbols-in-v1-projects, and rejects `aws.s3.Bucket` in favor of `BucketV2`-tier carve-outs. Body↔code coverage is **not** in this specialist's slice — it's the separate `body-code-coverage` specialist below.
- **`body-code-coverage`** (Sonnet 5, `general-purpose`) -- §Body↔code coverage. Receives the **full content body** plus a structured catalog: every fenced code block (language declaration + first 8 lines), every `{{< example-program >}}` shortcode invocation with its referenced `name`, and every `static/programs/<name>-<language>/` directory listing. Verifies in both directions: (a) every language claim in the body (table column header, prose language list, recommendations list) is corroborated by an inline fenced block or a `static/programs/<name>-<language>/` directory containing language-specific files; (b) every cited program directory's set of language variants matches what the body advertises. A column or list claiming language X without a corroborating X snippet → 🚨 (always-🚨 carve-out: the page promises something it doesn't deliver). Reciprocally, a program directory advertising languages the body doesn't reference → ⚠️ (orphan variant; usually intentional but worth surfacing for review). Quote the offending body claim verbatim and either (a) propose adding the missing variant or (b) propose removing the unsupported language claim. **Why a separate specialist:** the body↔code correspondence requires holding the entire comparison table + every language claim + every cited program in attention simultaneously; folded into `existence` (which is also doing per-block import / API checks), it gets squeezed under attention pressure — the failure mode was a persistent miss on language-column claims (e.g. a Java column with no Java snippet).

Each subagent prompt copies *only* its slice rows verbatim, plus its inputs (`structural`/`existence`: code block + language declaration; `body-code-coverage`: body + block catalog + program directories). Do **not** include `§Referenced static/programs/ snippets` (program-existence / per-language compilation -- main agent's combine step), `§Proposed fixes` (composition, not detection), or other specialists' rows. Per-finding cap ~250 words.

### Combine step

1. **Dedup.** Key = `<file>:<line>` plus the first 40 characters of `finding_text` (lowercased, whitespace collapsed). Merge near-paraphrase matches; pick the most specific framing.
1. **Annotate.** Set `found_by: [<specialist>, ...]` from `structural`, `existence`, `body-code-coverage`. Single-specialist finds are the expected state -- the split is by reasoning shape, not redundancy -- and are not a confidence signal. When two or more specialists co-fire on the same code-block range (e.g., a `structural` truncation that also breaks `existence` on a now-missing import; a `body-code-coverage` Java-column miss that also surfaces in `structural` if the missing snippet's tab is half-rendered), set `cross_specialist_corroboration: true` -- a positive signal for compound-bug catches.
1. **Promote per existing carve-outs.** Per `docs-review:references:output-format` §Bucket rules carve-out list:
   - `structural` finds reaching "code does not parse in its language" -> 🚨 (always-🚨 carve-out).
   - `existence` finds reaching "imports / calls a symbol that does not exist in the referenced package version" -> 🚨 (always-🚨 carve-out).
   - `body-code-coverage` finds reaching "body claims language X support but no snippet exists" -> 🚨 (always-🚨 carve-out: the page promises something it doesn't deliver).
   - All other findings default to ⚠️ unless the two-question test promotes them.
1. **Hand off.** Deduped, annotated list goes to the rendered review. Investigation-log dispatch metadata: `**Code-examples checks** -- "ran (3 specialists: structural, existence, body-code-coverage); N findings"` or `not run (no fenced code blocks in content files)`. When the diff contains only `static/programs/` changes, run `body-code-coverage` ONLY (the per-block exemption applies to `structural` + `existence`; the body-level body-code-coverage check runs whenever a content file is in the diff, since program-only diffs may still rebalance the language inventory of a referenced page).

No interim user output. Cross-block reasoning (e.g., `static/programs/<name>-<lang>/` compilation parity across language variants) stays with the main agent's combine step -- specialists see a single block at a time.
