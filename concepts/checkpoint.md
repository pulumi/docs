---
title: "Checkpoint files"
---

When creating or destroying cloud resources via `pulumi update` and `pulumi destroy`, Colada stores a mapping from its own logical names (Colada URNs) to those of the underlying cloud provider. This map is stored in a **checkpoint file** stored in `.pulumi/stacks/<projectName>/<stackName>.json`. 

During an `update` operation, Colada [runs your program](./programming-model.html) and determines which resources to add or remove. If there is a change to resource with a particular name, Colada passes the physical resource name to the [resource provider](./providers.html) so that the resource provider can make changes to the physical infrastructure.  

## Why a checkpoint file is necessary

You may be wondering why this mapping is stored at all; why not query the cloud provider to determine the current state of resources? TODO finish.


## Raw notes

- provider creates the resource with a target identity. Pulumi doesn't care about the physical identity, the provider is what does.
- id property is what the terraform provider has decided (up to individual resource) what is the ID. e.g., it can be ARN, but can't always be assumed to be such
- this is all opaque to pulumi
- checkpoint file maps from pulumi names to resource provider understood IDs
