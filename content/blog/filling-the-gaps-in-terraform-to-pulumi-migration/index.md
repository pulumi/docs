---
title: "Filling the Gaps in Terraform-to-Pulumi Migration"
date: 2026-08-31
draft: false
meta_desc: "pulumi import alone has gaps. See how pulumi-tool-import and its agent skills turn Terraform-to-Pulumi migration into a validated, repeatable workflow."
feature_image: feature.png
authors:
    - jonathan-davenport
tags:
    - terraform
    - migration
    - aws
    - ai
category: engineering
schema_type: auto

social:
    twitter: |
        A Professional Services customer has migrated more than 4,000 resources from Terraform to Pulumi on their own — using a tool we built after hitting the same gaps on every migration.

        Here's the pipeline that made it repeatable.
    linkedin: |
        Every Terraform-to-Pulumi migration we ran hit the same walls. State files full of plaintext secrets. Import IDs composed by hand, one resource at a time. A single bad ID failing the whole import. And a class of resources that cannot be imported at all, with an error message that points in the wrong direction.

        We built a tool that turns the import step into a pipeline, and an agent skill that drives it and validates every stage before moving to the next.

        A recent Professional Services customer adopted it and has since migrated more than 4,000 resources on their own, without Pulumi engineers in the loop.

        We wrote up how the pipeline works and the gap each stage closes.
    bluesky: |
        Some Terraform resources can't be imported into Pulumi at all, and the error message points in the wrong direction. That's one of five gaps we kept hitting on migrations, so we built a tool that closes them. One customer has migrated 4,000+ resources with it on their own.

        We wrote up the pipeline.
---

Migrating a live Terraform workspace to Pulumi is very doable — teams do it every day — but the import step has always carried more manual work than it should: discovering import IDs one resource at a time, extracting values from state files full of plaintext secrets, chasing down post-import diffs. None of that is deep or difficult; it's mechanical, which means it can be automated. We built [`pulumi-tool-import`](https://github.com/pulumi-proserv/pulumi-tool-import) — and a set of agent skills that drive it — to do exactly that, turning migration into a repeatable, validated pipeline. One recent customer has used it to migrate more than 4,000 resources entirely on their own.

<!--more-->

## The gaps in the import step

Pulumi already ships a capable [`pulumi import`](/docs/iac/guides/migration/import/) command, and for a handful of resources it's all you need. A real Terraform workspace — hundreds of resources, nested modules, secrets in state, years of drift — brings a few well-known gaps along with it that no single command fills:

- **Import IDs don't write themselves.** Every resource needs the right ID in the right format, and composite IDs (a Lambda permission is `FunctionName/StatementId`, Route53 records and security group rules have their own schemes) must be composed from resource attributes. Doing this by hand for a 300-resource stack is slow and error-prone.
- **Terraform state contains plaintext secrets.** Anything — or anyone, including an AI agent — that reads the state file to extract values sees database passwords and API keys in the clear.
- **One bad ID fails the whole import.** `pulumi import` commits already-succeeded steps but aborts on the first failure, so a large import becomes a loop of run, fail, fix one ID, run again.
- **The cloud API doesn't return everything.** Write-only fields, IaC-only defaults, and asset contents never come back from a provider's Read call, so freshly imported state produces diffs the program didn't cause.
- **Some resources can't be imported at all.** Association and toggle resources like `aws_iam_policy_attachment` or `aws_vpn_gateway_route_propagation` declare no importer, and `pulumi import` fails on them with a misleading `resource '<id>' does not exist`.

Bridged providers like `aws` (AWS Classic) add one more layer: the Pulumi resource model is translated from the Terraform provider's schema, so property names, nested shapes, and `MaxItems=1` flattening all differ from what's sitting in the Terraform state you're migrating from.

None of these is a reason to put off migrating. They're mechanical problems with mechanical answers — but without tooling, they're where the hours go. `pulumi-tool-import` addresses each of them directly. It's a Pulumi tool plugin whose commands form a pipeline, and it ships with agent skills that orchestrate the pipeline while an agent (or a human) hand-authors the Pulumi program the migration lands on.

## The pipeline

```mermaid
flowchart LR
    A["digest"] --> B["resolve"]
    B --> C["import"]
    C --> D["patch-state"]
    D --> E["zero-diff preview"]
```

Each command produces an artifact the next one consumes, which makes every step inspectable, repeatable, and resumable — properties that matter twice over when an AI agent is driving, because the agent can validate its work at each stage instead of hoping a monolithic migration lands.

### Digest: read state once, safely

`digest tf` analyzes the Terraform configuration and state (from a local file or a TFC-compatible remote backend like Terraform Cloud or Scalr) into a single JSON sidecar: module instances, their input/output interfaces, and every resource with its attributes and import ID.

Two things happen here that solve real problems:

**Secrets never touch the agent.** The digest discovers every attribute the provider schema marks sensitive, redacts it as `"(sensitive)"`, and sets the actual value as an encrypted Pulumi stack config secret via `pulumi config set --secret` — reading the state into memory only. The agent orchestrating the migration works entirely from the redacted digest and never sees a secret value. For secrets that live outside Terraform state, a standalone `set-secrets` command does the same thing from a mapping the agent supplies: config key on one side, Terraform address and attribute on the other, value never in the loop.

**Unimportable resources are detected up front.** Importability isn't recorded in any schema — it's a Go struct field on the provider's resource definition that the schema RPC never returns. So the digest asks the provider directly: it loads the Terraform provider pinned in `.terraform.lock.hcl` and probes `ImportResourceState` once per resource type with a dummy ID (unconfigured, no credentials, no API calls). Types that answer "doesn't support import" get flagged `nonImportable` in the digest so the rest of the pipeline can route around them.

### Resolve: reproducible import files

`pulumi preview --import-file import.json` generates a skeleton with placeholder IDs. `resolve tf` fills it in by matching each entry to a digest resource — by type and name within each mapped module/component pair — and composing composite IDs from the digest's attributes.

The matching is driven by a mappings file that records which Pulumi component instance corresponds to which Terraform module path:

```yaml
modules:
  "module.core_rds": "core_rds"
  "module.console_ui[\"mysvc\"]": "console_ui[\"mysvc\"]"
resources:
  "aws_s3_bucket.my_bucket": "my_bucket"
```

Because the digest and the mappings file fully determine the output, import file creation is reproducible: rerun `resolve` after renaming a component or fixing a mapping and you get a corrected import file, not a hand-edited one that's drifted from its inputs. Resources flagged `nonImportable` are held out of the import file — where they would be guaranteed failures — and written to a sidecar for later state injection.

### Import: batched, failure-isolating

The `import` command runs the prepared import file in batches (100 resources by default). When a batch doesn't fully land, it re-imports the batch's missing resources one at a time to identify exactly which IDs failed, records them, and carries on. One run surfaces *every* bad import ID instead of just the first, and because success is determined by reading stack state afterward, a rerun after fixing IDs skips everything already imported. Batching also keeps large imports from hammering cloud APIs into rate-limiting territory.

### Patch state: eliminate the diffs you didn't cause

After import, `pulumi preview` should be a no-op — but write-only fields (passwords, tokens), IaC-only defaults, and asset sentinels aren't returned by the cloud API, so they show up as phantom diffs. `patch-state tf` patches the exported stack state using a curated per-resource-type fields file that records which fields the API doesn't return and how to fill them: from the digest's attribute for that resource if present, else from the fields file default. It can also read a stack's secret config so secret fields are patched without decrypting anything into the open.

### State injection: the resources that can't be imported

Those `nonImportable` resources from the digest still exist in the cloud, and letting the next `pulumi up` try to create them is not a safe fallback — for association and toggle resources, a create against a pre-existing object fails partway through the deployment. Instead, `patch-state tf --non-importable` injects them directly into state: it takes each resource's URN, parent, provider, and dependencies from a preview of the program you've already written, fills in the ID and outputs from the sidecar, and verifies the result with a second preview — restoring its backup automatically if any injected resource doesn't preview as unchanged.

## The skills: a workflow the agent can follow and validate

The tool's commands run standalone, but they're designed to be driven by the agent skills that ship in the repo. The [`pulumi-terraform-workspace-migration`](https://github.com/pulumi-proserv/pulumi-tool-import/blob/main/skills/pulumi-terraform-workspace-migration/SKILL.md) skill turns the pipeline into a full migration workflow with validation gates:

- **Node-by-node, zero-diff gated.** The migration proceeds through modules and resources in dependency order, and each node must reach a zero-diff targeted preview before the next one starts. The agent can't sprint ahead of its own verification.
- **Every value traces to its source.** The skill's value-tracing rules map each Terraform construct to its Pulumi equivalent — `var.foo` to stack config, locals to in-program derivations, `terraform_remote_state` to ESC environment references — and the digest makes violations obvious: if the program hardcodes a value the Terraform code computes from variables, that's a bug the diff will surface.
- **When sources of truth disagree, deployed state wins.** Terraform code, Terraform state, and the live cloud drift apart over years. The skill's rule is that the deployed state is the source of truth: manual drift that exists in the cloud but not in the HCL gets *included* in the Pulumi program to preserve it, and every such decision is documented in the migration PR.
- **Modules become components.** A companion skill, `pulumi-terraform-module-to-component`, covers translating each Terraform module into an idiomatic Pulumi component — reproducing the module's *intent* (its interface of inputs and outputs) rather than transliterating its HCL — including the logical-naming convention that import matching depends on.

The result isn't a machine-translated program. It's a hand-authored, idiomatic Pulumi codebase your team keeps and grows — with the mechanical, error-prone parts of getting there automated and verified.

This isn't theoretical: a recent Professional Services customer adopted the tool and has since migrated more than 4,000 resources on their own with it — their team driving the pipeline themselves, without Pulumi engineers in the loop.

## Bonus: CDK and CloudFormation to AWS Classic

The same pipeline has a second front end. `digest cfn` reads a deployed CloudFormation stack — the live template plus stack resources, with intrinsics like `Ref` and `Fn::GetAtt` resolved against the account — and `resolve cfn` / `patch-state cfn` complete the path onto the classic `aws` provider.

We already had tooling for converting CDK and CloudFormation to the [AWS Native provider](/registry/packages/aws-native/), which is the right call for a fast automated lift-and-shift. This path serves a different goal: a hand-authored, component-structured codebase on the mature classic provider, with a provably zero-diff cutover. The [`cdk-to-pulumi-classic`](https://github.com/pulumi-proserv/pulumi-tool-import/blob/main/skills/cdk-to-pulumi-classic/SKILL.md) skill encodes the judgment calls that make it work — including using AWS Native selectively for the API Gateway family, where the classic provider's fine-grained model would explode one CloudFormation method into four or more resources.

## Getting started

Install the plugin from GitHub releases and run any command through the Pulumi plugin runner:

```bash
pulumi plugin install tool import \
  --server github://api.github.com/pulumi-proserv/pulumi-tool-import

pulumi plugin run import -- digest tf --help
```

Then point your agent at the skill matching your source — `pulumi-terraform-workspace-migration` for Terraform/OpenTofu, `cdk-to-pulumi-classic` for CDK/CloudFormation — and let it orchestrate the pipeline. The [README](https://github.com/pulumi-proserv/pulumi-tool-import#readme) documents every command for manual use as well.

A note on what this is: `pulumi-tool-import` is a Pulumi CLI tool plugin built and maintained by Pulumi Professional Services, not part of the core Pulumi product. It runs through the plugin runner and uses the Automation API under the hood, so it requires the Pulumi CLI. It's pre-v1, so pin the version you install and read the changelog before upgrading. If you're planning a larger migration and want help, [Pulumi Professional Services](/proserv/) runs these migrations every day — this tool is how we do it.
