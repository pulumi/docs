---
title: "Resources"
---

🚧 TODO add info on:
- Properties
- Dependencies
- Components
- Resource Providers
- Checkpoints

## Names
All resources managed by a Pulumi program have a Universal Resource Name (URN), which is a logical identifier for the resource. This name must be unique among all the resources in a Pulumi program; attempting to create two resources with the same name causes an error during `pulumi update`. The URN is stored in the stack's checkpoint and is the primary key for looking up a resource's state. 

During `pulumi update`, the URN is how Pulumi maps from a resource in the program text to a resource tracked in the checkpoint file. So, whenever a program allocates a resource with a URN that is contained in the checkpoint, Pulumi assumes these are the same resource and determines whether an update or replacement should be performed.  

If a particular name **R** is present in the checkpoint file, but the Pulumi program does not perform any resource allocations for **R**, the resource **R** will be deleted at the end of the deployment. In general you should not change the components of a resource name; if an identifier changes, Pulumi creates a new resource and destroys the old one. In Pulumi, the URN is the only notion of persistent identity for a resource across `update` operations.

Note that the URN for a Pulumi resource is never compared across *different* stacks; it is only required to be unique within a particular stack.  

## How URNs are generated

🚧 TODO fill out

## What changes a URN

🚧 TODO fill out

## How to author a Pulumi component

🚧 TODO fill out
