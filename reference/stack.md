---
title: "Stacks"
---

Every Pulumi program is deployed to a **stack**.  A stack is an isolated, independently configurable
instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as **development**, **staging** and **production**) or feature branches (such as **feature-x-dev**, **jane-feature-x-dev**).


## Create a stack {#create-stack}

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack.  The project that the stack is associated with is determined by finding the nearest `Pulumi.yaml` file.  

The stack name must be unique within within your account. As a best practice, prefix the stack name with a project name. 

```bash
$ pulumi stack init myproj-staging
```

If you are using Pulumi in your organization, by default the stack will be created in your user account. To target the organization, name the stack using `orgName/stackName`:

```bash
$ pulumi stack init broomllc/myproj-staging
```

## Listing stacks

To see the list of stacks associated with the current project (the nearest `Pulumi.yaml` file), use `pulumi stack ls`.

```bash
$ pulumi stack ls
NAME                                             LAST UPDATE              RESOURCE COUNT
myproj-jane-dev                                  4 hours ago              97            
myproj-staging*                                  n/a                      n/a           
myproj-test                                      2 weeks ago              121           
```

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

```bash
$ pulumi stack select myproj-jane-dev

$ pulumi stack ls
NAME                                             LAST UPDATE              RESOURCE COUNT
myproj-jane-dev*                                 4 hours ago              97            
myproj-staging                                   n/a                      n/a           
myproj-test                                      2 weeks ago              121           
```

## Deploy a project

To deploy your project to the currently selected stack, run `pulumi update`. The operation uses the latest [configuration values](config.html) for the active stack.

## View stack resources

To view details of the currently selected stack, run `pulumi stack` with no arguments.  This displays the metadata, resources and output properties associated with the stack.

```bash
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

When you use module exports in your Pulumi program, they become stack outputs. Stack outputs can be viewed via `pulumi stack output` and are shown on the stack information page on pulumi.com.

**JavaScript code**
```js
exports.publicDns = ...
exports.publicIp  = ...
```

**CLI**

```bash
$ pulumi stack output
Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197
```

The values of specific properties can also be retrieved directly, which is useful when writing scripts that use these output values.

```bash
$ pulumi stack output publicIp
18.218.85.197
```

## Import and export a stack deployment

A stack can be exported to see the raw data associated with the stack.  This is useful when manual changes need to be applied to the stack due to changes made in the target cloud platform that Pulumi is not aware of.  The modified stack can then be imported to set the current state of the stack to the new values.  The format of the stack files is versioned, and 

> **Note:** This is a powerful capability that subverts the usual way that Pulumi manages resources and ensures immutable and repeatable infrastructure deployments.  Importing an incorrect stack specification could lead to orphaning of cloud resources or the inability to make future updates to the stack.  Use care when using the import and export capabilities.

```bash
$ pulumi stack export > stack.json

$ pulumi stack import < stack.json
```

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove all stack history from pulumi.com and will delete the stack configuration file `Pulumi.<stack-name>.yaml`.  

If a stack still has resources associated with it, they must first be deleted via `pulumi destroy`. This command uses the latest configuration values, rather than the ones that were last used when the program was deployed. 

To force the deletion of a stack that still contains resources --- potentially orphaning them --- use `pulumi stack rm --force`.  
