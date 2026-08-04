---
title: "Bring Your Terraform to Pulumi Cloud: A Hands-On Walkthrough"
date: 2026-08-04T10:00:00-07:00
draft: true
meta_desc: "A hands-on walkthrough of Pulumi's new Terraform support: migrate state to Pulumi Cloud, publish and consume modules, and run HCL natively."
feature_image: feature.png
authors:
    - christian-nunciato
tags:
    - terraform
    - hcl
    - pulumi-cloud
    - infrastructure-as-code
    - modules
category: tutorials
---

Today's release is a big one, and it's all [generally available](/releases/terraform-state-backend-modules-hcl/): a whole set of ways to bring the Terraform you already run into Pulumi — your state, your modules, and HCL itself — without rewriting any of it. So many of you come to us wanting to adopt Pulumi without throwing away the Terraform you've built, and you shouldn't have to. The [announcement post](/blog/bring-your-terraform-estate-into-the-agentic-era/) covers the what and the why; this one is the hands-on tour.

It all falls into three buckets:

1. **Terraform state backend support**, including remote execution on Pulumi Cloud.
1. **Terraform module support** — publish your modules to Pulumi Cloud and consume them from any Pulumi language, as native Pulumi components.
1. **First-class support for HCL**, running natively on the Pulumi engine.

Seeing how all of that fits together end to end can be hard, so I've put together a quick, brisk walkthrough you can follow from start to finish — with nothing but a free Pulumi account and a free trial. We'll start with a Terraform project you've already deployed — state in a cloud storage bucket, in HCP Terraform, in Terraform Enterprise, wherever — and, one step at a time, bring the whole thing into Pulumi Cloud. Let's go.

<!--more-->

## Start with a Terraform project

To keep the moving parts to a minimum, we'll work from a small starter project. It provisions a single Amazon S3 bucket and includes a local module we'll publish later. Create your own copy from the template:

```bash
gh repo create my-tf-project \
    --template cnunciato/simple-tf-template \
    --public \
    --clone

cd my-tf-project
```

We'll use the local Terraform backend to start. Set your AWS credentials, then deploy with Terraform or OpenTofu. (This walkthrough uses the `terraform` CLI throughout; every command has an `opentofu` equivalent.)

```bash
terraform init && terraform apply
```

You're off and running with a local backend and a baseline to work from. Now let's move it to Pulumi Cloud.

## Migrate the state to Pulumi Cloud

First, [create a Pulumi Cloud account](https://app.pulumi.com/signup) if you don't have one — it's free for individuals — and sign in. Then add a `backend` block to `main.tf`, changing `organization` to your Pulumi Cloud account or organization name:

```hcl
terraform {
  backend "remote" {
    hostname     = "tf.pulumi.com"
    organization = "<your-org>"

    workspaces {
      name = "my-tf-project_dev"
    }
  }
}
```

The workspace name maps directly onto Pulumi's model: the first part (`my-tf-project`) is the [project](/docs/iac/concepts/projects/) and the second (`dev`) is the [stack](/docs/iac/concepts/stacks/). A single project can have as many stacks as you like.

Next, log in to Pulumi Cloud with the CLI:

```bash
terraform login tf.pulumi.com
```

Create a token, paste it into the prompt, and you're authenticated:

```
Success! Logged in to Terraform Enterprise (tf.pulumi.com)
```

With the backend block in place and the CLI authenticated, you're ready to migrate. If you're moving production state, back it up first — `terraform state pull > backup.tfstate` — then run the migration, which is a single command:

```bash
terraform init -migrate-state
```

Terraform notices the backend change and offers to copy your existing state:

```
Do you want to copy existing state to the new backend?
  Pre-existing state was found while migrating the previous "local" backend
  to the newly configured "remote" backend. [...] Enter "yes" to copy and
  "no" to start with an empty state.

  Enter a value: yes
```

Answer `yes`, and you're migrated:

```
Successfully configured the backend "remote"! Terraform will automatically
use this backend unless the backend configuration changes.
```

Nothing about your infrastructure changed here — only where its state lives. Run `terraform plan` to confirm you see no changes. We used a local backend to keep things concrete, but the same move works from an S3, Azure, or GCS bucket, and from HCP Terraform or Terraform Enterprise; see [Store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) for the backend-specific steps.

In the Pulumi Cloud console, choose **Stacks**, and you'll see your new stack in the list, along with its first update and the resources now under management. Those resources are searchable, too — press <kbd>⌘K</kbd> and start typing.

<!-- SCREENSHOT: Stacks list showing the newly migrated my-tf-project/dev stack. -->

### Runs happen remotely by default

One thing to know: new Terraform stacks backed by Pulumi Cloud run *remotely* by default, the same way HCP Terraform and Terraform Enterprise do. Plans and applies execute on a Pulumi-hosted runner, and the output streams back to your terminal. Make a small change to `main.tf` — say, adding a tag — and run `terraform apply` again:

```hcl
tags = {
  Environment = "dev"
  Owner       = "me"
}
```

```bash
terraform apply
```

```
Running apply in the remote backend. Output will stream here. [...]

To view this run in a browser, visit:
https://tf.pulumi.com/app/<your-org>/my-tf-project_dev/runs/run-...
```

Confirm the apply, and you'll notice it *fails* — the remote runner doesn't have AWS credentials yet. That's expected, and it's where [Pulumi ESC](/docs/esc/) comes in.

### Configure credentials with ESC

When you create a Terraform stack through the CLI, Pulumi Cloud provisions a linked ESC environment with the same name as the stack. Open the stack's **Overview** tab, open the linked `my-tf-project/dev` environment, and you can either set your AWS credentials directly as encrypted secrets or wire up an OIDC connection with **Add new → Login provider/configuration**. If you already have a login environment, import it:

```yaml
values:
  imports:
    - default/personal
```

With ESC, you build and share configuration and secrets across as many Terraform and Pulumi projects as you like, and stack outputs are exposed through ESC so projects can share computed values. Run the apply once more, and this time it succeeds:

```bash
terraform apply -auto-approve
```

Remote execution is powered by [Pulumi Deployments](/docs/deployments/), which also supports VCS triggers — pull requests and pushes to GitHub, GitLab, and others — and manual approvals for your Terraform stacks. If you'd like to try it, wire up the Pulumi GitHub app under **Settings → Deploy** in the console, add the `my-tf-project` repo, then push a change. The console will wait for you to **Confirm** or **Discard** the run.

<!-- SCREENSHOT: Console showing a VCS-triggered run awaiting Confirm/Discard. -->

That's the lift-and-shift. Your Terraform stacks are now first-class citizens in Pulumi Cloud, with [access control](/docs/administration/access-identity/rbac/), [Neo code reviews](/docs/ai/neo/code-reviews/), and [Pulumi policies](/docs/insights/policy/) all available to them — [audit policies](/docs/iac/get-started/terraform/terraform-state-backend/#audit-policies) can run on any Terraform stack, and preventative policies block non-compliant applies on remote runs. Next up: modules.

## Publish a Terraform module

If you've got a pile of Terraform lying around, you've almost certainly got modules, and you need somewhere to keep them. Alongside its role as a state backend, Pulumi Cloud now includes a [private registry](/docs/idp/concepts/terraform-modules/) that hosts your Terraform modules and makes them available across your organization.

Module publishing is an Enterprise or Business Critical capability, so you'll want an organization for this part. You can [create one](https://app.pulumi.com) and start a free trial if you don't have one already. Open the organization switcher, choose **Create organization**, and pick a name. As a fan of the short-lived sitcom *Better Off Ted*, I went with `veridian`, but choose whatever makes you smile.

Our starter project includes a small module at `./modules/s3-bucket` that provisions a bucket and returns its ARN. The registry's publish API is wire-compatible with HCP Terraform's, which means the tools you already use — the [go-tfe](https://github.com/hashicorp/go-tfe) library or the [`hashicorp/tfe`](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs) Terraform provider — work unchanged when you point them at `tf.pulumi.com`. The repo ships a small go-tfe program that does exactly that. Set your Pulumi access token, then run it from the repo root, passing your organization name:

```bash
export PULUMI_ACCESS_TOKEN=<your-access-token>

go -C upload-module run . \
    -org <your-org> \
    -provider aws \
    -version 0.1.0 \
    -path ./modules/s3-bucket
```

```
creating module veridian/s3-bucket/aws
uploaded veridian/s3-bucket/aws@0.1.0
```

In the Pulumi Cloud console, navigate to **Platform → Terraform Modules** and you'll find the new module in the list; open it to see its inputs, outputs, and versions.

<!-- SCREENSHOT: registry module list + module detail page. -->

Now point the project at the published module instead of the local copy. Back in `main.tf`, delete `./modules` and update the `source`, swapping in your own organization name:

```hcl
module "s3-bucket" {
  source  = "tf.pulumi.com/veridian/s3-bucket/aws"
  version = "0.1.0"

  bucket_name = "my-infra-example-bucket"
  tags = {
    Environment = "dev"
  }
}
```

Run `terraform apply` once more. Terraform downloads the module from the registry, and because nothing about the infrastructure changed, you'll see no changes to apply:

```bash
terraform apply
```

```
Initializing modules...
Downloading tf.pulumi.com/veridian/s3-bucket/aws 0.1.0 for s3-bucket...
```

Publish as many module versions as you need. That's the whole loop: publish, reference, apply.

## Consume the module from a Pulumi program

Teams put real thought into their Terraform modules, and the point of a shared registry is to get more mileage out of that investment. So Pulumi Cloud also lets you consume a Terraform module from a *Pulumi* program — even across languages. There are a few ways to do it, and which one you reach for depends on how much type safety you want and where the module lives.

The most direct path: every module version you publish is also converted into a Pulumi package, named after the module. Our `s3-bucket/aws` module becomes a package called `s3-bucket-aws`, with a generated SDK in whatever language your project uses. Let's create a quick TypeScript program and add it. If you haven't already, [install Pulumi](/docs/install/), then:

```bash
mkdir ../my-typescript-project && cd $_
pulumi new typescript
```

Follow the prompts, accepting the defaults. Then add the converted package by name:

```bash
pulumi package add s3-bucket-aws 0.1.0
```

This generates a local SDK under `./sdks`. Open `index.ts` and replace its contents with the following:

```typescript
import * as bucket from "./sdks/s3-bucket";

const myModule = new bucket.Module("my-module", {
    bucketName: "my-new-bucket-name",
    tags: {},
});

export const { bucketArn } = myModule;
```

Run `pulumi up` to deploy. The module's variables show up as typed inputs, its outputs as typed outputs, and the resources it creates appear individually in the preview rather than as one opaque blob.

If a version is still converting, or you'd rather load a module directly by address, you can run the conversion locally with the `hcl` provider instead:

```bash
pulumi package add hcl module tf.pulumi.com/veridian/s3-bucket/aws 0.1.0
```

There's also a dynamic loader for when you don't want to generate an SDK at all — handy when the module lives somewhere external (the OpenTofu registry, GitHub), or when you don't know every input up front and want to assemble things with a bit of logic at runtime. Install the package for your language:

```bash
npm install @pulumi-labs/hcl
```

(This package moves to `@pulumi/hcl` in the next release.)

Then use the loader in your program:

```typescript
import * as hcl from "@pulumi-labs/hcl";

const bucketModule = new hcl.Module("my-module", {
    source: "tf.pulumi.com/veridian/s3-bucket/aws",
    version: "0.1.0",
    inputs: {
        bucket_name: "my-new-bucket-name",
        tags: {},
    },
});

export const { outputs } = bucketModule;
```

This one uses untyped references, which trades a little safety for flexibility. Run `pulumi up`, and — since the bucket already exists — you'll see no changes. Whichever route you choose, the takeaway is the same: the modules you've already built keep working, and you get to build the *new* stuff in a general-purpose language, migrating on whatever schedule suits you.

## Write and run HCL, natively

Maybe your team just prefers HCL. As of today, HCL is a first-class language in the Pulumi engine, right alongside TypeScript, Python, Go, C#, Java, and YAML — and it's 100% [OpenTofu](https://github.com/opentofu/opentofu) compatible, with no syntactical differences.

So why run HCL on Pulumi rather than on Terraform or OpenTofu directly? You get the whole Pulumi ecosystem in a language your team already knows. Reach for a [native Pulumi provider](/docs/iac/languages-sdks/hcl/hcl-language-reference/) by giving its source the `pulumi/` namespace — `pulumi/kubernetes`, say — right alongside your bridged Terraform providers; consume Pulumi components and Terraform modules from the same program; and lean on Pulumi Cloud, ESC, and policies throughout. Pulumi HCL is a *superset* of Terraform HCL, too, so you can express things plain HCL can't — my colleague Ian's [deep dive on mapping Terraform onto the Pulumi engine](/blog/terraforms-data-model-on-pulumis-engine/) is a good tour of what that opens up.

Start from a template:

```bash
pulumi new aws-hcl
```

Open the generated project. You'll find familiar `.tf` files and a `Pulumi.yaml` that sets `runtime: hcl`. There's no conversion step — the Pulumi CLI runs the HCL directly, so you get Pulumi's state management, secrets handling, and deployment engine while writing the HCL you already know. Run it:

```bash
pulumi up
```

Because HCL is a real Pulumi language here, it can reach the same registry we've been using. Reference the module you published earlier with a standard `module` block:

```hcl
module "s3-bucket" {
  source  = "tf.pulumi.com/veridian/s3-bucket/aws"
  version = "0.1.0"

  bucket_name = "my-hcl-bucket-name"
}

output "bucket_arn" {
  value = module.s3-bucket.bucket_arn
}
```

Run `pulumi up` again, and there it is: an HCL program, running on the Pulumi engine, consuming a Terraform module from the Pulumi Cloud registry.

And if you'd rather not stay in HCL, [`pulumi convert`](/docs/iac/get-started/terraform/convert-hcl/) translates it into TypeScript, Python, Go, C#, Java, or YAML — so you can adopt a general-purpose language when you're ready, not because a migration forced the timing.

## Where to go next

Put it all together and it comes to one thing: Pulumi is now fully interoperable with Terraform and the wider Terraform ecosystem. You can back your Terraform state with Pulumi Cloud, publish and share your modules, consume those modules from any Pulumi language, and write HCL that runs natively — all without rewriting what you already have.

To keep going, a few good starting points:

- [Store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/)
- [Use Terraform modules in Pulumi](/docs/iac/get-started/terraform/terraform-modules/)
- [The HCL language reference](/docs/iac/languages-sdks/hcl/)
- [Browse the templates](/templates/) to start a new project in minutes

We'd genuinely love for you to kick the tires on all of this and tell us what you think. Pulumi HCL, like the engine it runs on, is open source under the Apache 2.0 license, so if something's missing or doesn't behave the way you'd expect, [open an issue](https://github.com/pulumi/pulumi-hcl/issues) and let us know. Bring it back to your teams, tell us what you'd like to see that we haven't built yet, and come say hello in the [Community Slack](https://slack.pulumi.com/) or [get in touch](/contact/?form=sales). We're looking forward to building the rest of this with you.
