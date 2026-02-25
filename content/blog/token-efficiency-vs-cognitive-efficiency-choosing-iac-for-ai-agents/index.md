---
title: "Token Efficiency vs Cognitive Efficiency: Choosing IaC for AI Agents"
allow_long_title: true
date: 2026-02-25
draft: false
meta_desc: "We benchmarked Terraform HCL and Pulumi TypeScript across two LLMs. HCL uses fewer tokens, but Pulumi's total pipeline cost is 41% lower."
meta_image: meta.png
authors:
    - engin-diri
tags:
    - ai
    - infrastructure-as-code
    - llm
social:
    twitter: "We benchmarked AI agents generating Terraform HCL and Pulumi TypeScript across two models. HCL uses fewer tokens per resource, but Opus + Pulumi had a 41% lower total pipeline cost because it deployed clean on the first pass with zero repairs. #InfrastructureAsCode #AI #Pulumi"
    linkedin: |
        When AI agents generate infrastructure code, two optimization targets compete: token efficiency and cognitive efficiency.

        We ran a controlled benchmark across Claude Opus 4.6 and GPT-5.2-Codex, measuring token consumption, cost, and deployability for both Terraform HCL and Pulumi TypeScript.

        The results:
        - HCL uses 21-33% fewer tokens for simple generation
        - But Opus + Pulumi produced deployable code for both generation AND refactoring with zero repairs
        - Opus + Terraform needed repair cycles for every refactoring run, driving total cost up 70%
        - Total pipeline: Opus + Pulumi cost $0.146, Opus + Terraform cost $0.249

        The full analysis with reproducible benchmark code is in the post.
---

When an AI agent writes infrastructure code, two things matter: how compact the output is (token efficiency) and how well the model actually reasons about what it's writing (cognitive efficiency). HCL produces fewer tokens for the same resource. But does that make it the better choice when agents need to refactor, debug, and iterate? We ran a benchmark across [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) and [GPT-5.2-Codex](https://platform.openai.com/docs/models) to find out.

<!--more-->

## These two goals pull in opposite directions

You might assume that the language producing fewer tokens is also the one models reason about best. Research into LLM-driven infrastructure generation suggests otherwise.

## Where HCL wins on tokens

HCL is declarative and minimal. It requires no imports, no runtime constructs, and no language scaffolding. For simple infrastructure generation, HCL leads to fewer tokens and lower generation cost.

For a straightforward resource definition, HCL gets straight to the point:

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
}
```

Compare that with the Pulumi TypeScript equivalent:

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("example", {
    bucket: "my-bucket",
});
```

The HCL version requires fewer tokens. No import statement, no variable declaration, no constructor syntax. For single-shot generation of simple resources, that compactness matters. But the picture changes once you account for deployability and refactoring.

## What the data shows

HCL's token advantage is real for simple generation. But agents don't just generate once. They validate, repair failures, and refactor. We built a benchmark that measures the full cycle: an open-source tool that sends identical prompts to Claude Opus 4.6 (`claude-opus-4-6`) and OpenAI GPT-5.2-Codex (`gpt-5.2-codex`), requesting both Terraform HCL and Pulumi TypeScript for the same AWS infrastructure (VPC with public and private subnets across 2 AZs, an EC2 instance with security groups for SSH and HTTP, and an RDS PostgreSQL instance with a security group allowing port 5432 only from the EC2 security group, plus all networking: internet gateway, NAT gateway, route tables, and associations). We measured token consumption, cost, and deployability across two scenarios: initial generation and refactoring into reusable components.

**Methodology:** Temperature 0, 5 runs per combination, randomized execution order. Each generated output goes through a three-stage validation pipeline: formatting (`terraform fmt` for HCL, `prettier` for TypeScript), static analysis (`terraform validate` for HCL, `tsc --noEmit` for TypeScript), and provider-level validation (`terraform plan` for HCL, `pulumi preview` for TypeScript). Both plan and preview check against real AWS provider schemas without creating resources, making their pass rates comparable across formats. If plan/preview fails, the benchmark feeds the error back to the model for one self-repair attempt. At temperature 0, Claude Opus 4.6 produced near-identical outputs across runs (sd=0-4 tokens). GPT-5.2-Codex showed more natural variation (sd=130-165 tokens). With 5 runs per combination the results are directional, not statistically conclusive. Costs are estimates based on published pricing as of 2026-02-22. Full methodology and reproducible code:

{{< github-card repo="dirien/iac-token-benchmark" >}}

### Scenario 1: Generation

HCL uses fewer tokens for generation:

| Provider | Format | Output tokens (mean) | LOC (mean) | Cost (mean) | Plan/Preview pass | Repairs needed |
|----------|--------|---------------------|-----------|-------------|-------------------|----------------|
| Claude Opus 4.6 | Terraform | 2,007 | 212 | $0.051 | 5/5 | 0/5 |
| Claude Opus 4.6 | Pulumi TS | 2,555 | 200 | $0.065 | 5/5 | 0/5 |
| GPT-5.2-Codex | Terraform | 1,565 | 110 | $0.022 | 2/5 | 2/5 |
| GPT-5.2-Codex | Pulumi TS | 2,322 | 147 | $0.033 | 0/5 | 5/5 |

HCL produces 21-33% fewer output tokens across both models. For simple resource generation, this translates directly to lower cost. Pulumi TypeScript uses more tokens for fewer lines of code because imports, type annotations, and constructor syntax add tokens without adding functional lines.

The Plan/Preview column tells a more complete story. Claude Opus 4.6 produced deployable code on the first pass for both formats: 5/5 for Terraform and 5/5 for Pulumi. Neither needed repairs. GPT-5.2-Codex struggled with both formats, but Terraform fared slightly better (2/5 vs 0/5).

### Scenario 2: Refactoring into reusable components

We took each model's generation output and asked it to refactor the code into a reusable module or component with parameterized environment name, instance sizes, and availability zone count.

| Provider | Format | Output tokens (mean) | LOC (mean) | Cost (mean) | Plan/Preview pass |
|----------|--------|---------------------|-----------|-------------|-------------------|
| Claude Opus 4.6 | Pulumi TS | 2,720 | 218 | $0.082 | 5/5 |
| Claude Opus 4.6 | Terraform | 3,379 | 345 | $0.095 | 5/5 |
| GPT-5.2-Codex | Pulumi TS | 2,477 | 248 | $0.038 | 4/5 |
| GPT-5.2-Codex | Terraform | 1,356 | 119 | $0.021 | 0/5 |

This is where the results get interesting. Opus + Pulumi refactoring used 20% fewer tokens, cost 14% less, and passed `pulumi preview` on every run (5/5) with zero repairs. Opus + Terraform also ended up at 5/5 for `terraform plan`, but it needed repair cycles to get there. The benchmark run log tells the story:

```console
# Pulumi refactoring: runs 29-33, sequential, no gaps = zero repairs
✓ [29/40] anthropic/pulumi-ts/refactor run 1 — 2721 tokens, $0.0817
✓ [30/40] anthropic/pulumi-ts/refactor run 2 — 2721 tokens, $0.0817
✓ [31/40] anthropic/pulumi-ts/refactor run 3 — 2721 tokens, $0.0817
✓ [32/40] anthropic/pulumi-ts/refactor run 4 — 2721 tokens, $0.0817
✓ [33/40] anthropic/pulumi-ts/refactor run 5 — 2714 tokens, $0.0816

# Terraform refactoring: 34→36→38→40→42, every run skips a number = every run triggered self-repair
✓ [34/40] anthropic/terraform/refactor run 1 — 3388 tokens, $0.0956
✓ [36/40] anthropic/terraform/refactor run 2 — 3339 tokens, $0.0944
✓ [38/40] anthropic/terraform/refactor run 3 — 3390 tokens, $0.0957
✓ [40/40] anthropic/terraform/refactor run 4 — 3388 tokens, $0.0956
✓ [42/40] anthropic/terraform/refactor run 5 — 3388 tokens, $0.0956
```

The skipped numbers (35, 37, 39, 41) are self-repair turns where the model received `terraform plan` errors and regenerated the code. Each repair consumed additional tokens that do not show up in the first-generation cost but do show up in the total pipeline cost.

GPT-5.2-Codex tells a different story. Both formats needed repair on every run, but what happened after repair is what matters:

```console
# Codex + Terraform refactoring: repaired, but still failed plan (0/5 deployable)
terraform run 1 turn 2: plan_valid=False  tokens=1559
terraform run 2 turn 2: plan_valid=False  tokens=1165
terraform run 3 turn 2: plan_valid=False  tokens=1068
terraform run 4 turn 2: plan_valid=False  tokens=1134
terraform run 5 turn 2: plan_valid=False  tokens=1101

# Codex + Pulumi refactoring: repaired, and preview passed (4/5 deployable)
pulumi-ts run 1 turn 2: plan_valid=True   tokens=2246
pulumi-ts run 2 turn 2: plan_valid=True   tokens=2567
pulumi-ts run 3 turn 2: plan_valid=True   tokens=2187
pulumi-ts run 4 turn 2: plan_valid=True   tokens=2531
pulumi-ts run 5 turn 2: plan_valid=False  tokens=2647
```

Codex + Terraform used fewer tokens but produced zero deployable refactored code after repair. Codex + Pulumi used more tokens but recovered to deployable code 4 out of 5 times. TypeScript's type errors gave the model enough information to fix the problems. HCL's plan errors did not.

### Total pipeline cost

This is the number that matters for production agent workflows. It includes generation, any self-repair cycles, and refactoring:

| Provider | Format | Total tokens (mean) | Total cost (mean) |
|----------|--------|--------------------|--------------------|
| Claude Opus 4.6 | Pulumi TS | 8,183 | $0.146 |
| Claude Opus 4.6 | Terraform | 14,669 | $0.249 |
| GPT-5.2-Codex | Terraform | 8,723 | $0.084 |
| GPT-5.2-Codex | Pulumi TS | 15,211 | $0.138 |

Opus + Pulumi had the lowest total pipeline cost at $0.146, 41% cheaper than Opus + Terraform at $0.249. The difference comes entirely from repair cycles: Pulumi needed zero repairs across both scenarios, while Terraform refactoring triggered self-repair on every run.

With Codex, Terraform had the lower pipeline cost ($0.084 vs $0.138), driven by its smaller token output. But Codex + Terraform produced zero deployable refactored code (0/5 plan pass), while Codex + Pulumi produced deployable code 4 out of 5 times.

### What this means

1. **HCL uses fewer tokens per generation.** For single-shot resource creation, HCL's compactness saves 21-33% on output tokens. That advantage is consistent across both models.
1. **Pulumi produces deployable refactored code more reliably.** With Opus, Pulumi refactoring passed preview 5/5 with zero repairs. Codex + Pulumi passed 4/5. Codex + Terraform passed 0/5.
1. **Total pipeline cost favors Pulumi with Opus.** Opus + Pulumi cost 41% less than Opus + Terraform across the full pipeline ($0.146 vs $0.249), because Terraform refactoring needed repair cycles that Pulumi did not.
1. **The tradeoff depends on your model and workflow.** Codex + Terraform is cheapest on raw tokens but produces no deployable refactored code. Codex + Pulumi costs more per token but actually deploys. Opus + Pulumi is the best of both: fewer refactoring tokens and zero repairs.

## Why Pulumi refactoring deploys cleaner

The [TerraFormer project](https://arxiv.org/abs/2601.08734) identified what they call the **correctness-congruence gap**: LLMs generate configurations that look valid but fail to match the user's architectural intent. An [error taxonomy study](https://arxiv.org/abs/2512.14792) cataloged the same pattern across models. A [survey of LLMs for IaC](https://arxiv.org/html/2404.00227v1) found the gap between syntax validity and architectural correctness widens with infrastructure complexity.

Refactoring is where this gap bites hardest. Turning a flat resource list into a parameterized, reusable module requires the model to restructure dependencies, introduce variables, and compose abstractions. With Pulumi, the model can use TypeScript's standard refactoring patterns: extract a class, add typed constructor parameters, compose functions. These are patterns it has practiced across millions of repositories during training. With HCL, the same refactoring requires `count`, `for_each`, `dynamic` blocks, and module variable plumbing, domain-specific constructs that have far less representation in training data.

Our benchmark confirms this directly. Opus produced 2,720 tokens for Pulumi refactoring versus 3,379 for Terraform, a 20% reduction, and every Pulumi run passed `pulumi preview` without repair. The Terraform refactoring runs all triggered self-repair because the restructured HCL modules had issues that `terraform plan` caught.

Training data distribution makes this structural. LLMs have far more TypeScript than HCL in their corpora. A model refactoring TypeScript draws on patterns from the entire open-source ecosystem. A model refactoring HCL modules has a much smaller pool. Since general-purpose languages dominate new code production, this gap will widen over time.

{{< notes type="info" >}}
Tooling can close the gap further. The [Pulumi MCP server](/docs/iac/using-pulumi/mcp-server/) gives AI agents direct access to resource schemas at generation time. A tool like `get-resource` returns every property, type, and required field for a given cloud resource. The agent does not have to guess from what it memorized during training. It can look up the correct schema before writing a single line of code.

This changes the workflow from "generate, fail, read error, retry" to "look up schema, generate correctly." Agent skills push this further by encoding working Pulumi idioms as structured prompts, so the model starts from a known-good baseline. Terraform has no equivalent to this MCP-based schema lookup. That difference matters more with every iteration.
{{< /notes >}}

## Where the industry is heading

One way to think about IaC language choice is through the lens of [AI engineering maturity levels](https://www.principalengineer.com/p/the-7-levels-of-software-engineering). At Level 3 (agentic coding), agents generate infrastructure from prompts. HCL's 21-33% token savings on generation matters here. At Levels 4-5, agents iterate on specifications, refactor code, and maintain systems over time. Our benchmark shows this is where Pulumi pulls ahead: 41% lower total pipeline cost with Opus, and more deployable refactored output with both models.

The industry is moving toward Levels 4-5. Agents are taking on refactoring, feature flags, environment parameterization. [43% of DevOps teams need four or more deployment iterations](https://overmind.tech/blog/the-best-ai-for-terraform) before infrastructure is production-ready. The first-generation token advantage HCL holds applies to the task that is shrinking as a share of agent workloads. The refactoring and deployability advantages that Pulumi offers apply to the tasks that are growing.

## Choosing based on your workflow

If your agents primarily generate well-scoped resource definitions, HCL saves 21-33% on output tokens. That advantage is real and consistent.

If your agents need deployable output on the first pass (which avoids repair costs entirely), our data shows Opus + Pulumi is the strongest combination: 5/5 plan/preview pass for both generation and refactoring, zero repairs, lowest total pipeline cost.

If your agents evolve infrastructure over time through refactoring and modularizing, Pulumi produced deployable refactored code more reliably across both models we tested (5/5 and 4/5 vs 5/5 and 0/5 for Terraform).

Pulumi covers the full iteration loop, from generation through repair to refactoring, using the same language patterns and tooling that models already know.

## Get started

Ready to explore how AI agents work with Pulumi? Check out [Pulumi AI](/ai/) to see LLM-powered infrastructure generation in action, or get started with [Pulumi's documentation](/docs/get-started/).

Join the conversation in the [Pulumi Community Slack](https://slack.pulumi.com/) or [Pulumi Community Discussions](https://github.com/pulumi/pulumi/discussions).
