---
title: "Stacks"
---

Every Pulumi program is deployed to a **stack**.  A stack is an isolated, independently configurable
instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as **development**, **staging** and **production**) or feature branches (such as **feature-x-dev**, **jane-feature-x-dev**).

## Create a stack

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack.  The project that the stack is associated with is determined by finding the nearest `Pulumi.yaml` file.  

```
$ pulumi stack init staging --local
```

## Listing stacks

To see the list of stacks associated with the current project (the nearest `Pulumi.yaml` file), use `pulumi stack ls`.

```
$ pulumi stack ls
NAME                                             LAST UPDATE              RESOURCE COUNT     CLOUD
jane-dev                                         4 hours ago              97                 n/a
staging*                                         n/a                      n/a                n/a
testing                                          2 weeks ago              121                n/a
```

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

```
$ pulumi stack select jane-dev

$ pulumi stack ls
NAME                                             LAST UPDATE              RESOURCE COUNT
jane-dev*                                        4 hours ago              2             
staging                                          n/a                      n/a           
testing                                          2 weeks ago              3             
```

## View stack resources

To view details of the currently selected stack, run `pulumi stack` with no arguments.  This displays the metadata, resources and output properties associated with the stack.

```
$ pulumi stack
Current stack is jane-dev:
    Last updated 1 week ago (2018-03-02 10:26:09.850357 -0800 PST)
    Pulumi version v0.11.0
    Plugin nodejs [language] version 0.11.0
    Plugin aws [resource] version 0.11.0

Current stack resources (3):
    TYPE                                             NAME
    pulumi:pulumi:Stack                              webserver-jane-dev
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www

Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```

## View stack outputs {#outputs}

When you use [output properties](./programming-model.html#output-properties) in your Pulumi program, they become stack outputs. Stack outputs can be viewed via `pulumi stack output`.

```
$ pulumi stack output
Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197
```

The values of specific properties can also be retreived directly, which is useful when writing scripts that use these output values.

```
$ pulumi stack output publicIp
18.218.85.197
```

## Import and export a stack deployment

A stack can be exported to see the raw data associated with the stack.  This is useful when manual changes need to be applied to the stack due to changes made in the target cloud platform that Pulumi is not aware of.  The modified stack can then be imported to set the current state of the stack to the new values.  The format of the stack files is versioned, and 

*NOTE*: This is a powerful capability, which subverts the usual way that Pulumi manages resources and ensures immutable and repeatable infrastructure deployments.  Importing an incorrect stack specification could lead to orphaning of cloud resources or the inability to make future updates to the stack.  Use care when using the import and export capabilities.

```
$ pulumi stack export > stack.json

$ pulumi stack import < stack.json
```

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove the tracking information for the stack and will also delete stack settings in `Pulumi.yaml`.  

```
$ pulumi stack rm jane-dev
This will permanently remove the 'jane-dev' stack!
Please confirm that this is what you'd like to do by typing ("jane-dev"): jane-dev
Stack 'jane-dev' has been removed!
```

If a stack still has resources associated with it, they must first be deleted via `pulumi destroy`.  To force the deletion of a stack with resources still in it (and therefore to orphan the resources in the target cloud provider so that they are no longer managed by Pulumi), use `pulumi stack rm -f`.
