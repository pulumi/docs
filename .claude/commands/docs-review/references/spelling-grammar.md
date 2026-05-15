---
user-invocable: false
description: Spelling and grammar rules for user-facing prose. Protected-token allowlist, flag list, do-not-flag list.
---

# Spelling and grammar

Concrete rules for catching misspellings and grammar errors in user-facing prose. Quote-and-rewrite mandate: every finding names the location, the offending token or phrase, and the suggested correction.

## Protected tokens — never flag

A token is **protected** if any of the following holds. Skip it as a misspelling, capitalization, or grammar candidate. Treat as protected when in doubt.

- **Mixed-case identifiers.** `IaC`, `getStackOutput`, `mTLS`, `BlogPost`.
- **All-caps two-or-more-letter acronyms.** `ESC`, `IDP`, `IAM`, `RBAC`, `OIDC`, `SCIM`, `SAML`, `SDK`, `CLI`, `API`, `AWS`, `GCP`, `JSON`, `YAML`, `TOML`, `HTTP`, `HTTPS`, `TLS`, `S3`, `RDS`, `EKS`, `GKE`, `AKS`, `OSS`, `K8s`.
- **Tokens with digits, underscores, hyphens joining lowercase words, slashes, dots, or backticks.** `snake_case`, `kebab-case`, `no-fail-on-create`, `app.pulumi.com`, `--yes`.
- **Pulumi product names and concepts.** Pulumi, Pulumi IaC, Pulumi ESC, Pulumi IDP, Pulumi Insights, Pulumi Cloud, Pulumi Policies, stack(s), provider(s), component(s), project(s), program(s), resource(s), inputs, outputs, config(s), secrets, stack references, dynamic providers, ESC environments.
- **Tool, language, runtime, registry, or service names.** Kubernetes, Terraform, kubectl, helm, npm, pnpm, Yarn, PyPI, NuGet, Maven, Hugo, Docker, GitHub, GitLab, Anthropic.
- **File paths, URLs, command names, flags, environment variable names.**

## Flag

- **Misspelled common English words.** "recieve" → "receive"; "seperate" → "separate"; "occured" → "occurred"; "definately" → "definitely"; "accomodate" → "accommodate".
- **Wrong-word substitutions** (high confidence only): their/there/they're, its/it's, affect/effect, loose/lose, then/than, your/you're, principal/principle, complement/compliment.
- **Subject-verb disagreement** when both subject and verb are common English words: "Pulumi support" → "Pulumi supports"; "the team are" → "the team is" (US English).
- **Missing article** when a singular countable English noun obviously needs one: "deploy stack" → "deploy a stack". Skip when the noun is protected.
- **Doubled words.** "the the", "to to", "and and".
- **UK spellings.** This repo uses American English. Convert by pattern: `-our` → `-or` ("colour" → "color", "behaviour" → "behavior", "favourite" → "favorite", "labour" → "labor", "honour" → "honor"); `-ise`/`-yse` verbs → `-ize`/`-yze` ("organise" → "organize", "realise" → "realize", "analyse" → "analyze", "optimise" → "optimize", "customise" → "customize"); `-tre` → `-ter` ("centre" → "center", "theatre" → "theater"); doubled-l past tense → single-l ("travelled" → "traveled", "cancelled" → "canceled", "labelling" → "labeling", "modelled" → "modeled"); specific cases: "defence" → "defense", "licence" (as noun) → "license", "practise" (as verb) → "practice".
- **Missing Oxford comma** in a list of three or more items. "stacks, providers and components" → "stacks, providers, and components"; "deploy, preview or destroy" → "deploy, preview, or destroy". Required before "and" or "or" in the final item.

## Do not flag

- Anything matching a protected token.
- **Sentence fragments used for emphasis** in titles, headings, or marketing copy. "Faster, simpler." in a `meta_desc` is intentional, not a missing verb.
- **Em-dash, en-dash, hyphen, or punctuation density.** Style choice, not error.
- **"Punctuation that changes meaning"** unless you can quote the exact missing or extra mark AND explain how the meaning literally inverts. If you have to reach, skip.
- **Style, rewording, tone, or clarity.** Out of scope.
