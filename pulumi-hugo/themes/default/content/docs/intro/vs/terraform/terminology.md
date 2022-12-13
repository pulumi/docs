---
title_tag: "Pulumi vs. Terraform: Terminology and Commands"
title: "Terminology and Commands"
meta_desc: Many of the terms you may know from working with Terraform have direct equivalents in Pulumi. Here is a list of common terms and how they relate to Pulumi.
---

<style>
    main table {
        font-size: 0.94em;
        width: 100%;
    }

    main table th:first-child,
    main table td:first-child {
        width: 33%;
    }
</style>

If you're already familiar with Terraform, learning Pulumi terminology and commands is simple. Many of the existing Terraform vocabulary and commands that you already know have direct equivalents in Pulumi. The table below lists common Terraform terms and CLI commands along with their Pulumi equivalents.

## Terminology

| Terraform | Pulumi |
| --------- | ------ |
| Workspace | [Stack](/docs/intro/concepts/stack/) |
| Variables | [Stack Config](/docs/intro/concepts/config/) |
| Directory | [Project](/docs/intro/concepts/project/) |
| Module | [Component](/docs/intro/concepts/resources/components/) |
| Resource | [Resource](/docs/intro/concepts/resources/) |
| Interpolation | [Interpolation](/docs/intro/concepts/inputs-outputs#outputs-and-strings) |
| Run | [Up](/docs/reference/cli/pulumi_up/) |
| Output Values | [Outputs](/docs/intro/concepts/inputs-outputs/) |
| State | [State](/docs/intro/concepts/state/) |
| State Version | [Update Events](/docs/reference/service-rest-api#list-update-events) |
| Backend | [Backend](/docs/intro/concepts/state/) |
| Deposed | [Pending Operations](/docs/support/troubleshooting#interrupted-update-recovery) |

## Commands

| Terraform | Pulumi |
| --------- | ------ |
| `init` | `pulumi new` |
| `validate` | Validation is performed with the inherent syntax checking and testing frameworks in the supported programming languages |
| `plan` | `pulumi preview` |
| `apply` | `pulumi up` |
| `destroy` | `pulumi destroy` |
| `console` | Pulumi commands can be evaluated in a standard programming language shell |
| `fmt` | Standard programming language linting tools checks for format and style |
| `force-unlock` | `pulumi cancel` |
| `get` | Reusable modules are directly imported as a library in the programming language |
| `graph` | `pulumi stack graph` |
| `import` | `pulumi import -f resources.json` |
| `login` | `pulumi login` |
| `logout` | `pulumi logout` |
| `output` | `pulumi stack output` |
| `providers` | `pulumi plugin` |
| `refresh` | `pulumi refresh` |
| `show` | `pulumi stack` |
| `state` | `pulumi state` |
| `version` | `pulumi version` |
| `workspace` | `pulumi stack` |
