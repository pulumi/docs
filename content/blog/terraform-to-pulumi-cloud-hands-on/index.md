---
title: "Terraform state, modules, and HCL: A guided tour"
date: 2026-08-04
draft: false
meta_desc: "A hands-on walkthrough of our new Terraform support: migrate state to Pulumi Cloud, publish and consume modules, and run HCL natively."
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

Today's release is a big step forward, and it's all [generally available](/releases/terraform-state-backend-modules-hcl/): a whole set of ways to bring the Terraform you already run into Pulumi — your state, your modules, and HashiCorp Configuration Language (HCL) itself — without rewriting any of it. So many of you come to us wanting to adopt Pulumi without throwing away the Terraform you've built, and you shouldn't have to. The [announcement post](/blog/bring-your-terraform-estate-into-the-agentic-era/) covers the what and the why; this one is the hands-on tour.

It all falls into three buckets:

1. **Terraform state backend support**, including remote execution on Pulumi Cloud.
1. **Terraform module support** — publish your modules to Pulumi Cloud and consume them from any Pulumi language, as native Pulumi components.
1. **First-class support for HCL**, running natively on the Pulumi engine.

Seeing how all of that fits together end to end can be hard, so I've put together a quick, brisk walkthrough you can follow from start to finish — with nothing but a free Pulumi account and a free trial. We'll start with a Terraform project you've already deployed — state in a cloud storage bucket, in HCP Terraform, in Terraform Enterprise, wherever — and, one step at a time, bring the whole thing into Pulumi Cloud. Let's go.

<!--more-->

## Start with a Terraform project

To keep the moving parts to a minimum, we'll work from a small starter project. It provisions a single Amazon S3 bucket and includes a local module we'll publish later. Create your own copy from the template:

```bash
$ gh repo create my-tf-project \
    --template cnunciato/simple-tf-template \
    --public \
    --clone && cd my-tf-project

```

We'll use the local Terraform backend to start. Set your AWS credentials, then deploy with Terraform or OpenTofu. (This walkthrough uses the `terraform` CLI throughout; every command has an `opentofu` equivalent.)

```bash
$ terraform init && terraform apply
...

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

bucket_arn = "arn:aws:s3:::my-tf-project-bucket-14d19ece"
bucket_name = "my-tf-project-bucket-14d19ece"
```

You're off and running with a local backend and a baseline to work from.

Now let's move it to Pulumi Cloud.

## Migrate the state to Pulumi Cloud

First, [create a Pulumi Cloud account](https://app.pulumi.com/signup) if you don't have one — it's free for individuals — and sign in. Then add a `backend` block to `main.tf`, changing `<your-org>` to your Pulumi Cloud account or organization name:

```hcl
terraform {
  # ...

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
$ terraform login tf.pulumi.com
```

Choose yes when prompted, and you'll be taken to Pulumi Cloud. Create a [personal access token](/docs/administration/access-identity/access-tokens/#personal-access-tokens), paste it into the prompt, and you'll be authenticated:

![Creating a personal access token in the Pulumi Cloud console](./token.png)

```
Success! Logged in to Terraform Enterprise (tf.pulumi.com)
```

With the `backend` block in place and your `terraform` CLI signed in to Pulumi Cloud, you're ready to complete the migration:

```bash
$ terraform init -migrate-state
```

Terraform notices the backend change and offers to copy your existing state:

```
Do you want to copy existing state to the new backend?
  Pre-existing state was found while migrating the previous "local" backend
  to the newly configured "remote" backend. [...] Enter "yes" to copy and
  "no" to start with an empty state.

  Enter a value: yes
```

Answer `yes`, and you're done:

```
Successfully configured the backend "remote"! Terraform will automatically
use this backend unless the backend configuration changes.
```

Note that nothing about your deployed infrastructure has changed; all we did was migrate your state to Pulumi Cloud. Here, we migrated from a local backend, but the process is the same whether you're moving from S3, Azure, Google Cloud, or HCP Terraform or Terraform Enterprise. See [Store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) for details.

Now hop over to the Pulumi Cloud console, choose **Stacks**, and you'll see your new stack in the list, along with its first update:

![The migrated Terraform stack and its first update in the Pulumi Cloud console](./new-tf-stack.png)

### Runs happen remotely by default

One thing to note is that Terraform stacks backed by Pulumi Cloud run *remotely* by default, just as they do in HCP Terraform and Terraform Enterprise. Plans and applies are executed on a Pulumi-hosted runner, and the output streams back to your terminal. Try making a small change to `main.tf` — adding a tag, say — and run `terraform apply`:

```diff
  tags = {
    Environment = "dev"
+   Owner       = "me"
  }
```

```bash
$ terraform apply
...

Running apply in the remote backend. Output will stream here.

To view this run in a browser, visit:
https://tf.pulumi.com/app/cnunciato/my-tf-project_dev/runs/run-8a635542-334f-4367-b188-8b4b442b2550
...
```

Confirm the apply, and you'll notice it *fails* — which should make sense, considering the runner doesn't have AWS credentials for you yet. That's where [Pulumi ESC](/docs/esc/) comes in.

### Configure cloud credentials with ESC

When you create a new Terraform stack, Pulumi Cloud creates a linked ESC environment for you with the same name as the stack. You can use this environment to configure settings of all kinds, including cloud credentials and other encrypted secrets, and make those settings available automatically to the stack.

Open your stack's **Overview** tab, click the linked `my-tf-project/dev` environment, and you can either set your AWS credentials directly in the editor or wire up an OIDC connection by choosing **Add new** → **Login provider/configuration** and following the steps for your particular cloud.

Since I've already defined an environment containing my AWS credentials (which I've named `default/personal`), I can simply [import that environment](/docs/esc/concepts/imports/) into this one and start using it:

```yaml
imports:
- default/personal
```

Try this yourself, then run the `apply` again, and this time, see that it succeeds:

```bash
$ terraform apply -auto-approve
...

OpenTofu will perform the following actions:

  # module.s3-bucket.aws_s3_bucket.this will be updated in-place
  ~ resource "aws_s3_bucket" "this" {
        id                          = "my-tf-project-bucket-b64b8e37"
      ~ tags                        = {
            "Environment" = "dev"
          + "Owner"       = "me"
        }
      ~ tags_all                    = {
          + "Owner"       = "me"
        }
    }

Plan: 0 to add, 1 to change, 0 to destroy.
...

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

bucket_arn = "arn:aws:s3:::my-tf-project-bucket-b64b8e37"
bucket_name = "my-tf-project-bucket-b64b8e37"
```

Remote execution is powered by [Pulumi Deployments](/docs/deployments/), so your Terraform stacks also get VCS triggers — plans and applies on PRs and pushes to GitHub, GitLab, and others — plus manual approvals. To wire it up:

1. Under **Management → Version Control** in the Pulumi console, configure your VCS provider and add the `my-tf-project` repo.
1. In your stack's **Settings → Deploy**, pick that repo and the base branch to build from (e.g., `main`), and save.
1. Push a commit to that branch.

A new plan appears in the **Deployments** tab, and once it finishes, you're prompted to confirm or discard the run:

![A deployment run awaiting confirmation in the Pulumi Cloud console](./confirm.png)

Click **Confirm**, and you're off and running.

And that's it! Your Terraform stacks are now first-class citizens in Pulumi Cloud, with [access control](/docs/administration/access-identity/rbac/), [Neo code reviews](/docs/ai/neo/code-reviews/), and [Pulumi Policies](/docs/insights/policy/) all available to them — [audit policies](/docs/iac/get-started/terraform/terraform-state-backend/#audit-policies) can run on any Terraform stack, and preventative policies block non-compliant applies on remote runs.

Next up: modules.

## Publish a Terraform module

If you've got a pile of Terraform lying around, you've almost certainly got modules, and you need somewhere to keep them. Alongside its role as a state backend, Pulumi Cloud now includes a [private registry](/docs/idp/concepts/terraform-modules/) that hosts your Terraform modules and makes them available across your organization.

Module publishing requires an Enterprise or Business Critical subscription, so you'll need an organization for this part — but you can easily [create one](https://app.pulumi.com) and start a free trial if you don't have one already. In the Pulumi console, open the organization menu, choose **Create organization**, and give it a name.

Pulumi Cloud's Terraform registry API is wire-compatible with HCP Terraform's, which means the tools you already use for publishing — e.g., the [`go-tfe`](https://github.com/hashicorp/go-tfe) library or the [`hashicorp/tfe`](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs) Terraform provider — need only be pointed at `tf.pulumi.com`. The project we've been working with includes a small `go-tfe` program that does exactly that. Set a Pulumi access token (you may need to obtain a new one) in your terminal, then run it from the repo root, passing your organization name:

```bash
$ export PULUMI_ACCESS_TOKEN=<your-access-token>

# Install Go at https://go.dev/doc/install if you don't have it already.
$ go -C upload-module run . \
    -org <your-org> \
    -provider aws \
    -version 0.1.0 \
    -path ./modules/s3-bucket
```

You should see a confirmation:

```
creating module veridian/s3-bucket/aws
uploaded veridian/s3-bucket/aws@0.1.0
```

And then in the Pulumi console, navigate to **Platform → Private components**, and you should see the new module in the list. Open it up to see its details, versions, usage instructions, and API docs:

![The published Terraform module's detail page in the Pulumi Cloud registry](./module.png)

With the module now hosted in Pulumi Cloud, you can update the project to use the hosted version instead. Delete the `./modules` folder entirely, and then in `main.tf`, update the `source` and add a `version`, replacing `<your-org>` with your newly created org name:

```hcl
module "s3-bucket" {
  source  = "tf.pulumi.com/<your-org>/s3-bucket/aws"
  version = "0.1.0"

  # ...
}
```

Now run `terraform plan` and see that the module is downloaded and the plan produces no changes:

```bash
$ terraform plan
...

Initializing modules...
Downloading tf.pulumi.com/veridian/s3-bucket/aws 0.1.0 for s3-bucket...
...

No changes. Your infrastructure matches the configuration.
```

Now let's have a look at how you can use this module in other ways.

## Consume the module from a Pulumi program

Teams put real thought into their Terraform modules, and the point of a shared registry is to help you get more mileage out of that investment. With Pulumi Cloud, you can consume a Terraform module from a *Pulumi* program — even across languages.

Let's see how this looks with a TypeScript project. If you haven't already, [install Pulumi](/docs/install/), then run:

```bash
$ mkdir ../my-typescript-project && cd $_
$ pulumi new typescript
```

Follow the prompts, accepting the defaults. Then add the converted package by name:

```bash
$ pulumi package add s3-bucket-aws
```

This generates a local TypeScript SDK in the project at `./sdks`. Open `index.ts`, and replace its contents with the following:

```typescript
import * as bucket from "./sdks/s3-bucket";

const myModule = new bucket.Module("my-module", {
    bucketPrefix: "my-new-bucket",
    tags: {},
});

export const { bucketName, bucketArn } = myModule;
```

Configure your AWS credentials as before — you can even [use the ESC environment you created earlier](/docs/esc/concepts/environments/#using-environments-with-pulumi-iac) if you set one up — then run `pulumi up` to deploy in the usual way:

```bash
$ pulumi up

Updating (dev)

     Type                       Name                       Status
 +   pulumi:pulumi:Stack        my-typescript-project-dev  created (8s)
 +   └─ s3-bucket:index:Module  my-module                  created (5s)
 +      ├─ random:index:Id      my-module-suffix           created (0.21s)
 +      └─ aws:index:S3Bucket   my-module-this             created (2s)

Outputs:
    bucketArn : "arn:aws:s3:::my-new-bucket-bbfa52db"
    bucketName: "my-new-bucket-bbfa52db"

Resources:
    + 4 created
```

Having a language-specific, locally managed SDK at hand comes with a handful of benefits, including typed inputs and outputs, but there may be times when you need a simpler or more dynamic option. To handle these situations, you can choose to load the module at runtime.

In TypeScript, you can do that with the `@pulumi-labs/hcl` module. Try that now by installing it in your project:

```bash
$ npm install @pulumi-labs/hcl
```

... and using it in your program:

```typescript
import * as hcl from "@pulumi-labs/hcl";

const myModule = new hcl.Module("my-module", {
    source: "tf.pulumi.com/<your-org>/s3-bucket/aws",
    version: "0.1.0",
    inputs: {
        bucket_prefix: "my-new-bucket",
        tags: {},
    },
});

export const { bucket_name, bucket_arn } = myModule.outputs;
```

Because this approach uses untyped references, you'll trade a little safety for flexibility. But either way, the modules you've already invested in can continue to be used, and you can use them to build *new* infrastructure in general-purpose languages, migrating over on whatever schedule works best for you.

## Write and run HCL, natively

For as much flexibility as general-purpose languages offer, some teams simply prefer HCL. So as of today, HCL is now a first-class language in the Pulumi engine, right alongside TypeScript, Python, Go, C#, Java, and YAML — and fully compatible with [OpenTofu](https://github.com/opentofu/opentofu).

The easiest way to get a feel for it is to start from a template:

```bash
$ mkdir ../my-hcl-project && cd $_
$ pulumi new aws-hcl
```

As before, step through the prompts, then open the generated Pulumi project and `main.tf`:

```hcl
terraform {
  required_providers {
    aws = {
      source = "pulumi/aws"
    }
  }
}

# Create an AWS resource (S3 Bucket)
resource "aws_s3_bucket" "my-bucket" {}

# Export the name of the bucket
output "bucket_name" {
  value = aws_s3_bucket.my-bucket.id
}
```

You can deploy this out of the box (after setting your AWS credentials again, of course) if you'd like to see the magic happen:

```bash
$ pulumi up

Updating (dev)

     Type                 Name                Status
 +   pulumi:pulumi:Stack  my-hcl-project-dev  created (6s)
 +   └─ aws:s3:Bucket     my-bucket           created (3s)

Outputs:
    bucket_name: "my-bucket-7282e67"

Resources:
    + 2 created

Duration: 7s
```

This template happens to use the `pulumi/aws` provider, but you're free to pull in others just as easily — native Pulumi providers, any `hashicorp/*` Terraform provider, local modules, and the modules you've published to your Pulumi Cloud registry. In fact, you can try that now by replacing the code in `main.tf` with the same code you used in the Terraform program you left off with earlier — only without the `terraform > backend` block, as it's no longer needed:

```hcl
module "s3-bucket" {
  source  = "tf.pulumi.com/<your-org>/s3-bucket/aws"
  version = "0.1.0"
  bucket_prefix = "my-tf-project-bucket"
  tags = {}
}

output "bucket_name" {
  value = module.s3-bucket.bucket_name
}

output "bucket_arn" {
  value = module.s3-bucket.bucket_arn
}
```

Run `pulumi up` again, and you'll see the module get picked up and used, just as before:

```bash
$ pulumi up

Updating (dev)

     Type                                  Name                Status
 +   pulumi:pulumi:Stack                   my-hcl-project-dev  created (10s)
 +   └─ components:index:C619d883588c0366  s3-bucket           created (8s)
 +      ├─ random:index:Id                 s3-bucket.suffix    created (0.22s)
 +      └─ aws:index:S3Bucket              s3-bucket.this      created (3s)

Outputs:
    bucket_arn : "arn:aws:s3:::my-tf-project-bucket-f61cea35"
    bucket_name: "my-tf-project-bucket-f61cea35"

Resources:
    + 4 created

Duration: 12s
```

Don't forget to clean up both projects with a `terraform destroy` and `pulumi destroy`.

## Where to go next

And with that, you've seen it all come together: You can back your Terraform state with Pulumi Cloud, publish and share your modules, consume those modules from any Pulumi language, and write HCL that runs natively — all without rewriting what you already have.

To keep going, a few good starting points:

- [Store Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/)
- [Use Terraform modules in Pulumi](/docs/iac/get-started/terraform/terraform-modules/)
- [The HCL language reference](/docs/iac/languages-sdks/hcl/)
- [Browse the templates](/templates/) to start a new project in minutes

We'd genuinely love for you to kick the tires on all of this and tell us what you think. Pulumi HCL, like the engine it runs on, is open source under the Apache 2.0 license, so if something's missing or doesn't behave the way you'd expect, [open an issue](https://github.com/pulumi/pulumi-hcl/issues) and let us know. Bring it back to your teams, tell us what you'd like to see that we haven't built yet, and come say hello in the [Community Slack](https://slack.pulumi.com/) or [get in touch](/contact/?form=sales). We're looking forward to building the rest of this with you.
