---
title_tag: "Editing Pulumi State Files"
meta_desc: "Learn how to edit state files as a last resort for fixing corrupted stacks."
title: Editing state files
h1: Editing state files
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Editing State Files
        parent: iac-troubleshooting-debugging
        weight: 30
aliases:
    - /docs/troubleshooting/#editing-your-deployment
    - /docs/iac/troubleshooting/common-issues/manual-state-editing/
---

Sometimes the only recourse for fixing a stack that is unable to complete deployments is to edit the deployment directly. We would love to hear about the issues you are experiencing that you can't resolve, both so we can assist you in fixing your stack and also to fix the issues in Pulumi that made it impossible for you to recover your stack in any other way.

The Pulumi engine uses both your program and your stack's existing state to make decisions about what resources to create, read, update, or delete. The most common problem that makes it impossible to make changes to your stack is that the stack's state has been corrupted in some way. There are a variety of ways that a stack's state could be corrupted, but in almost all cases it is possible to manually edit the stack's state to fix the issue.

This is an advanced operation and should be an absolute last resort. We recommend you check in with the [Pulumi Community Slack](https://slack.pulumi.com) first before editing your snapshot.

If you intend to unprotect or delete a resource, consider using the [`pulumi state`](/docs/cli/commands/pulumi_state) command instead of editing your state directly. `pulumi state` makes fixes to your state without requiring you to edit the JSON representation of your stack's current state.

To get a JSON representation of your stack's current state, export your current stack to a file:

```bash
$ pulumi stack export --file state.json
```

This file contains a lot of information. At the top level, this JSON object has two fields:

| Field | Description |
| - | - |
| `version` | The version of the file format. This should not be changed. |
| `deployment` | The last deployment state of the stack. |

The `deployment` object itself has three fields:

| Field | Description |
| - | - |
| `manifest` | Metadata about the previous deployment. This should not be changed. |
| `pending_operations` | List of the operations that the Pulumi engine started but has not finished. |
| `resources` | List of resources that Pulumi knows about. |

The possible fields of a resource are:

| Field |  Description |
| - | - |
| `urn` | The resource URN, which is a Pulumi-specific universal resource identifier. |
| `custom` | A boolean indicating whether or not this resource is a `custom` resource, which means that it uses a resource provider to operate. Component resources are not `custom`. |
| `delete` | A boolean indicating whether or not this resource is pending deletion. |
| `id` | This resource's ID, which is a provider-specific resource identifier. This often corresponds to a cloud provider's identifier for a resource. |
| `type` | The Pulumi type of this resource. |
| `inputs` | A map of inputs for this resource. Inputs are the set of key-value pairs used as an input to a resource provider. |
| `outputs` | A map of outputs for this resource. Outputs are the set of key-value pairs that were given to Pulumi by a resource provider after a resource has been provisioned. |
| `parent` | A URN for this resource's parent resource. |
| `protect` |  A boolean indicating whether or not this resource is protected. Protected resources can not be deleted. |
| `external` | A boolean indicating whether or not this resource is external to Pulumi. If a resource is external, Pulumi does not own its life cycle and it will not ever delete or update the resource. Resources that are read using the `get` function are external. |
| `dependencies` | A list of URNs indicating the resources that this resource depends on. Pulumi tracks dependencies between resources. It is important that this list be the full list of resources upon which this resource depends. |
| `initErrors` | A list of errors that occurred that prevented the resource from initializing. Some resource providers (most notably Kubernetes) populate this field to indicate that a resource was created but failed to initialize. |
| `provider` | Reference to the provider responsible for the resource. |

The `resources` field is a list, not a set. The order of resources in the list is important and is enforced by the Pulumi engine. Resources in a deployment must be in *dependency order* - if resource A depends on resource B, resource A *must* appear after resource B in the list.

Import your changes by running:

```bash
$ pulumi stack import --file state.json
```
