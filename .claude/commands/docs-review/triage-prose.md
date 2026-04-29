---
user-invocable: false
description: Triage prose-check prompt. Loaded only when triage-classify.py classifies a PR as trivial or frontmatter-only. Classification itself is deterministic and lives in triage-classify.py.
---

# PR Triage — Prose Check

You are doing a focused spelling/grammar pass on a small pull request that the triage shell has already classified as **trivial** (≤5 lines of prose-only body changes) or **frontmatter-only** (every change is inside a Hugo frontmatter block). Either way, the full review will be skipped — this is the only sanity-check pass before merge.

This is a fast, narrow pass. Output exactly one JSON object on a single line, no prose, no code fences:

```json
{"prose_concerns":["path/to/file.md:LINE — issue (suggested fix)", ...]}
```

If you find no issues, output `{"prose_concerns":[]}`.

## Protected tokens — never flag

A token is **protected** if any of the following is true. Skip it entirely as a misspelling, capitalization, or grammar candidate:

- It contains an uppercase letter after the first character (CamelCase, MixedCase, internal caps): `IaC`, `BlogPost`, `getStackOutput`, `mTLS`.
- It is two or more letters, all uppercase: `ESC`, `IDP`, `IAM`, `RBAC`, `OIDC`, `SCIM`, `SAML`, `SDK`, `CLI`, `API`, `AWS`, `GCP`, `JSON`, `YAML`, `TOML`, `HTTP`, `HTTPS`, `TLS`, `S3`, `RDS`, `EKS`, `GKE`, `AKS`, `OSS`, `K8s`.
- It contains a digit, underscore, hyphen joining lowercase words, slash, dot, or backtick: `snake_case`, `kebab-case`, `no-fail-on-create`, `app.pulumi.com`, `--yes`.
- It is a Pulumi product name or concept: Pulumi, Pulumi IaC, Pulumi ESC, Pulumi IDP, Pulumi Insights, Pulumi Cloud, Pulumi Policies, stack, stacks, provider, providers, component, components, project, projects, program, programs, resource, resources, outputs, inputs, config, configs, secrets, stack references, dynamic providers, ESC environments.
- It is the name of a tool, language, runtime, registry, or service: Kubernetes, Terraform, kubectl, helm, npm, pnpm, Yarn, PyPI, NuGet, Maven, Hugo, Docker, GitHub, GitLab, Anthropic.
- It is a file path, URL, command name, command flag, or environment variable name.

When in doubt, treat the token as protected.

## Flag

- **Misspelled common English words.** Examples: "recieve" → "receive"; "seperate" → "separate"; "occured" → "occurred"; "definately" → "definitely"; "accomodate" → "accommodate".
- **Wrong-word substitutions** (high confidence only): their/there/they're, its/it's, affect/effect, loose/lose, then/than, your/you're, principal/principle, complement/compliment.
- **Subject-verb disagreement** when both subject and verb are common English words: "Pulumi support" → "Pulumi supports"; "the team are" → "the team is" (US English).
- **Missing article** when a singular countable English noun obviously needs one: "Use Pulumi to deploy stack" → "to deploy a stack". Skip if the noun is protected.
- **Doubled words**: "the the", "to to", "and and".

## Do not flag

- Anything matching a protected token.
- **Sentence fragments used for emphasis** in titles, headings, or marketing copy. "Faster, simpler." in a `meta_desc` is intentional, not a missing verb.
- **Regional spellings.** "behaviour", "colour", "organisation", "dialogue", "favourite", "centre" — UK is valid; never flag.
- **Oxford-comma presence or absence.** Both are valid.
- **Em-dash, en-dash, hyphen, or punctuation density.** Style choice, not error.
- **"Punctuation that changes meaning"** unless you can quote the exact missing or extra mark AND explain how the meaning literally inverts. If you have to reach, skip.
- **Style, rewording, tone, or clarity suggestions.** This pass is spelling and grammar only — not editorial.

## Frontmatter-only PRs: scope

Inspect only prose-bearing fields:

- `title`, `linktitle`
- `meta_desc`, `description`
- `social_image_text`, `og_description`
- `excerpt`, `summary`

Skip data fields entirely:

- `aliases`, `slug`, `url`, `permalink`
- `tags`, `categories`, `keywords`, `topics`
- `draft`, `date`, `weight`, `expiryDate`, `publishDate`
- `author`, `authors`
- `cluster_*`, `block_*`, layout/template directives
- Any field whose value is a list of paths, URLs, identifiers, or dates.

## Examples

DO flag:

- `content/blog/foo.md:14 — "recieve" should be "receive"`
- `content/docs/bar.md:3 — "the the" doubled`
- `content/blog/baz.md:8 — "your welcome" should be "you're welcome"`
- `content/docs/qux.md:22 — "Pulumi support TypeScript" should be "Pulumi supports TypeScript"`

DO NOT flag:

- "Pulumi IaC" — Pulumi product name
- "behaviour" — UK spelling, valid
- "Faster. Simpler. Done." — intentional fragments in marketing copy
- "kubectl get pods" — command identifier
- "stack-references-doc.md" — kebab-case identifier
- "ESC" — protected acronym

## Output format

Each finding is one element in `prose_concerns`:

```text
path/to/file.md:LINE — issue (suggested fix)
```

Be specific so the author can act without re-reading the diff. One concern per element. Cap at the 5 most important findings.

Output exactly one JSON object on a single line. No prose, no code fences, no commentary.
