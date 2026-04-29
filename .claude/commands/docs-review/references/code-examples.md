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
- **Each variant must compile under its language.** Cross-reference to `CODE-EXAMPLES.md` for the testing contract.
- **Hugo shortcode reference picks up all language variants** via the `path=` parameter; no separate per-language shortcode calls.

## Proposed fixes

- **Proposed fixes must compile.** If you suggest a code replacement, it must itself pass every check above. Don't suggest untested code as a fix.
- **When in doubt, skip the fix.** Flag the issue without proposing a replacement rather than guess.

## Do not flag

- **Property-name casing that matches the language's convention.** `bucketName` in TypeScript is correct; `bucket_name` in Python is correct.
- **Code examples that omit optional arguments.** "You could also pass `tags: {...}`" is unsolicited enrichment.
- **CLI examples without paired output.** Not every code block needs a `output` block. Flag when the prose claims specific output and the block is missing; don't flag for "completeness."
- **Prettier-style formatting on hand-written constructor code.** TypeScript constructor style is an intentional deviation from Prettier defaults.
- **"Consider adding error handling."** Example programs deliberately skip production-grade error handling. Flag when the example *claims* to handle an error (but doesn't), not when it simply doesn't demonstrate error handling.
