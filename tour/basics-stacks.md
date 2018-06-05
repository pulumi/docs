---
title: Stacks
---

A stack is an instance of your Pulumi program.

Stacks are one of the most important concepts in Pulumi.  You'll create and manipulate them frequently.

Why would a program have more than one stack?  This is very common:

* Shared environments like `prod`, `staging`, and `dev`
* Replicated instances within an environment like `prod-na-east`, `prod-na-west`, and `prod-asia`
* Single tenanted instances of a SaaS product like `acmecorp`, `contoso`, and `northwind` 
* Individual developer stacks
* Test stacks

Each stack is entirely isolated from all other stacks, enabling concurrent deployments and fine-grained access controls.

The [`pulumi stack`](/reference/cli/pulumi_stack) command manages all things stacks.

`ls` shows us this project's stacks, how many resources each contains, and URLs on the Pulumi.com dashboard:

```bash
$ pulumi stack ls
NAME                   RESOURCE COUNT     URL
broomllc/prod          73                 https://app.pulumi.com/broomllc/prod
broomllc/staging*      88                 https://app.pulumi.com/broomllc/staging
```

The `*` next to `staging` indicates that's the stack we're on.  Most CLI commands are contextual depending on the
selected stack.

To select a different stack, we can use `select`:

```
$ pulumi stack select prod
```

We can create a new stack, and then we can remove it afterwards:

```
$ pulumi stack init cbroom-dev
$ pulumi stack rm cbroom-dev --yes
```

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-packages.html" title="Packages">◀</a>
    <span class="tour-index"><strong>6</strong>/9</span>
    <a class="tour-button enabled" href="basics-configuration.html" title="Configuration">▶</a>
</div>
