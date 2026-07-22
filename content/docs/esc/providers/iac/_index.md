---
title: Infrastructure as Code providers
title_tag: Pulumi ESC infrastructure as code providers
h1: Infrastructure as Code providers
meta_desc: Pulumi ESC infrastructure as code providers import Pulumi stack outputs and Terraform state outputs into your environment.
menu:
  esc:
    name: IaC
    identifier: esc-providers-iac
    parent: esc-providers
    weight: 3
aliases:
  - /docs/esc/integrations/infrastructure/
---

Infrastructure as code providers import the outputs of an existing infrastructure deployment — a Pulumi stack or a Terraform state file — into your environment. Each provider is invoked through `fn::open::<name>`, and the imported outputs can be mapped to `pulumiConfig` or `environmentVariables` and consumed by downstream stacks, programs, and tools.

Use these providers to share foundational infrastructure (VPC IDs, subnet IDs, cluster endpoints, DNS zones) across stacks and teams without copying values by hand or wiring up additional credentials.

| Provider | Description |
|---|---|
| [pulumi-stacks](/docs/esc/providers/iac/pulumi-stacks/) | Import outputs from a Pulumi stack (including Terraform state stored in Pulumi Cloud). |
| [terraform-state](/docs/esc/providers/iac/terraform-state/) | Import outputs from a Terraform state file in S3 or Terraform Cloud. |
