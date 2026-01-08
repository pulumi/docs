---
title: "Introducing the Stash Resource in Pulumi IaC"
date: 2026-01-08
draft: false
meta_desc: The new Stash resource lets you save computed values directly to your stack's state, making them persist across deployments.
authors:
    - fraser-waters
    - meagan-cojocar
tags:
    - features
    - releases
    - iac

---

We're excited to announce the `Stash` resource, a new built-in Pulumi resource that lets you save arbitrary values directly to your stack's state. Whether you need to capture a computed result, record who first deployed your infrastructure, or persist configuration that should remain stable across updates, Stash provides a more simple and ergonomic solution.

<!--more-->

## Why Stash?

Infrastructure code often produces values that need to persist beyond a single deployment. Maybe you're generating a random identifier that should stay consistent, tracking which team member initially set up a stack, or caching a computed result that's expensive to recreate. Previously, you'd need workarounds like external storage, custom resources, or careful state manipulation.

The `Stash` resource helps with that. It takes an input value, stores it in your stack's state, and makes it available as an output property. The key insight is that the `output` property preserves the *original* value even when the `input` changes in subsequent deployments. This makes Stash perfect for "first-run" scenarios where you want to capture and preserve a value from the initial deployment.

## Using Stash

Creating a Stash is straightforward. Here's how you'd capture the username of whoever first deploys the stack:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as os from "os";

const firstDeployer = new pulumi.Stash("firstDeployer", {
    input: os.userInfo().username,
});

export const originalDeployer = firstDeployer.output;
```

The first time this runs, both `input` and `output` will show the current user. On subsequent deployments by different users, `input` will update to show the new user, but `output` will continue returning the original deployer's name.

Stash supports any value type—strings, numbers, objects, arrays, and nested structures. It also respects secret annotations, so if you stash a secret value, it stays encrypted in your state.

## When to replace

Since Stash preserves the original value by design, updating the stored value requires a replacement. You have several options: use `--target-replace` during `pulumi up`, run `pulumi state taint` to mark the resource for replacement, or use the `TriggerReplacement` resource option to automate replacements based on value changes.

## Learn more

The Stash resource is available now in Pulumi v3.208.0 and later across all supported languages. Check out the [Stash documentation](/docs/iac/concepts/stash/) for detailed examples in TypeScript, Python, Go, C#, Java, and YAML.

We'd love to hear how you're using Stash and any feedback you have on it! Share your use cases in our [Community Slack](https://slack.pulumi.com/) or open an issue if you see any on [pulumi/pulumi](https://github.com/pulumi/pulumi/issues).

Happy hacking!
