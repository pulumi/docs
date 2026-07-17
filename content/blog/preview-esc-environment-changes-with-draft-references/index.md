---
title: "Preview ESC Changes with Environment Overrides"
date: 2026-07-17
draft: false
meta_desc: "Preview a proposed ESC environment change against your stack before you promote it, using draft references and the new --override-env flag."
feature_image: feature.png
authors:
    - sean-yeh
tags:
    - esc
    - features
    - configuration-management
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

[Pulumi ESC](/docs/esc/) makes it easy to store configuration and secrets for your Pulumi programs, and with [Approvals for ESC](/docs/esc/concepts/approvals/) you can stage changes before they go live. But until now, there was no easy way to see how a proposed change would actually affect your stack. With the new `--override-env` flag, you can preview any environment change, including an unapproved draft, before it becomes the latest version.

<!--more-->

## Example scenario

Let's say your team uses ESC for storing configuration for your production app, and your team decides to use Approvals for ESC for more safety and control. Every config change requires signoff by a teammate before going live, ensuring a bad value doesn't make it into your critical infrastructure. This is working great, but one part of the puzzle is missing: how can the reviewer adequately validate the config change before approving?

## Introducing: draft references and the --override-env flag

We are introducing a new `--override-env` flag to the Pulumi CLI that works for all Pulumi operations that can consume ESC environments: `preview`, `up`, `refresh`, and `destroy`. This makes it super easy to test config changes without modifying your stack config.

### Example usages

The basic usage is `--override-env <env>=<replacement>`, and you can override multiple environments at once!
In this example, we are running a `pulumi preview` with environments `app/myenv` and `app/myenv2` replaced by their draft versions (denoted by `@draft:<draft-id>`).

```
pulumi preview \
  --override-env "app/myenv=app/myenv@draft:123e4567-e89b-12d3-a456-426614174000" \
  --override-env "app/myenv2=app/myenv2@draft:123e4567-e89b-12d3-a456-426614174000"
```

The `--override-env` flag not only works with draft references, but for any environment too! Here is an example of deploying your stack with your AWS test environment:

```
pulumi up --override-env "aws-login/prod=aws-login/testing"
```

Note: `--override-env` can also override environments that are imported (directly or indirectly) from the ESC environment in your stack config. This is especially useful if you have access to an imported environment but not the root environment.

## When to use it

- Validate a draft ESC environment with your stack before approving
- Preview a proposed environment change on a PR as part of a CI check
- One-off debugging without editing stack config

## Get started

Draft references and `--override-env` are available today in the Pulumi CLI. Upgrade to the [latest release](/docs/install/) and try it out! To learn more:

- [Pulumi ESC documentation](/docs/esc/)
- [Approvals for ESC](/docs/esc/concepts/approvals/)
- [Get started with Pulumi ESC](/docs/esc/get-started/)
