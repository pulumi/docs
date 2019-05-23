---
title: Custom configuration
aliases: ["programs-configuration.html"]
expanded_url: /tour/programs/
menu:
  tour:
    parent: programs
    weight: 6
---

Pulumi programs can be configurable.

Configuration allows you to easily author code that is conditional on CLI incantations, without having to edit your code.

Any code run by Pulumi -- packages included -- can define configuration variables.

Each stack contains its own bag of configuration key/value pairs.

For instance, we may want `prod` and `staging` to use different database instance sizes or container replica counts.
We might put `prod-na-east` and `prod-na-west` into different regions.  Both are perfect use cases for configuration.

Configuration values like passwords or authorization tokens can be encrypted as **secrets**.

A package or program can accept configuration by creating a `pulumi.Config` object:

```typescript
import {Config} from "@pulumi/pulumi";
let config = new Config("ahoy-pulumi");
```

The constructor takes the name of the current package.  This scopes the keys and avoids naming collisions.

Each configuration setting has a key.  Because of package scoping, all keys are of the form
`<PACKAGE>:<NAME>`.  For instance, the `aws` package's `region` variable has `aws:region` as its key.

Our program can then read the stack's values using `require` (for required) or `get` (for optional):

```typescript
let dbInstanceSize: string = config.require("dbInstanceSize");
let replicaCount: string | undefined = config.get("replicaCount");
```

There are helper functions to turn settings into numbers or booleans:

```typescript
let dbInstanceSize: number = config.requireNumber("dbInstanceSize");
let replicaCount: number | undefined = config.getNumber("replicaCount");
```

It's common to use default values for optional variables; for instance, 4 replicas by default:

```typescript
let replicaCount: number = config.getNumber("replicaCount") || 4;
```

***



<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs-properties.md" >}}" title="Resource properties">◀</a>
    <span class="tour-index"><strong>7</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "programs-exports.md" >}}" title="Stack exports">▶</a>
</div>
