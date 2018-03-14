---
title: "Names"
---

All resources managed by a Pulumi program have a Universal Resource Name (URN), which is a logical identifier for the resource. This name must be unique among all the resources in a Pulumi program; attempting to create two resources with the same name causes an error during `pulumi update`. The URN is stored in the stack's [checkpoint file](./checkpoint.html) and is the primary key for looking up a resource's state. 

During `pulumi update`, the URN is how Pulumi maps from a resource in the program text to a resource tracked in the checkpoint file. So, whenever a program allocates a resource with a URN that is contained in the checkpoint, Pulumi assumes these are the same resource and determines whether an update or replacement should be performed.  

If a particular name **R** is present in the checkpoint file, but the Pulumi program does not perform any resource allocations for **R**, the resource **R** will be deleted at the end of the deployment. In general you should not change the components of a resource name; if an identifier changes, Pulumi creates a new resource and destroys the old one. In Pulumi, the URN is the only notion of persistent identity for a resource across `update` operations.

Note that the URN for a Pulumi resource is never compared across *different* stacks; it is only required to be unique within a particular stack.  

## How URNs are generated

TODO fill out

## What changes a URN

TODO fill out

## How to author a Pulumi component

TODO fill out

<!-- 

Copied from Luke's naming doc

Currently, URNs are made up of four parts - stack name, project name, type name, resource name.  For example, a URN might look like the following urn:pulumi:luke-test::unittests::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/role:Role::tests-endpointe33b8e2a and is made up of the following components (leaving out fixed strings that are the same across all Pulumi managed URNs):

Resources created in external cloud infrastructure typically also have some notion of identity assigned by the cloud provider.  This physical identifier is used by a Pulumi Resource Provider to lookup, update or delete a resource in the provider.  This is typically stored in the `id` field of a Pulumi resource, though the Pulumi engine itself does not interpret it in any way - it is an opaque identifier managed by the provider.  

For many external cloud resources, the physical name for the resource can be partially or entirely specified by the user.  For example, the `CreateFunction` API for AWS Lambda accepts a required `FunctionName` parameter.  There are a wide variety of different constraints on these names across and within providers.  Most must be within some name length limit, and must adhere to some limited alphabet or allowed regexp.  


To ensure that multiple copies of a stack can be brought up in the same cloud environment, we typically want to ensure that these physical names are unique across multiple stacks.  To do this, we must assign a physical name at creation time that is sufficiently unique.  Unfortunately, users cannot do this on their own.  If their program were to provide a fixed name in their source code, it would be the same for every instance of the stack.  If they were to use `Math.random()` it would differ across different updates of the same stack.  So instead, our terraform bridge takes care of this automatically, via a transformation that does two things to a property identified as a “name”:
- Makes it optional
- If not specified, provide a value constructed by concatenated the URN name part with a small amount of random hex.

This is done only at creation time, and the resulting name is then stored in the checkpoint with the resource and maintained across updates.

The following example creates a single Pulumi resource.
let group = new aws.ec2.SecurityGroup("web-secgrp", {
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});
This results in a resource with URN: urn:pulumi:foo::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp

And physical name: web-secgrp-8502581 -->
