---
title: "Converting Terraform to Pulumi Just Got Easier"
date: 2025-02-25
meta_desc: "Pulumi's conversion tools now automatically handle any Terraform provider, making migration easier than ever"
meta_image: meta.png
authors:
    - brandon-pollack
    - meagan-cojocar
tags:
  - terraform
  - features
---
Big news for infrastructure teams looking to migrate-we've just supercharged Pulumi's Terraform conversion capabilities, making it easier than ever to modernize your infrastructure as code.

Pulumi already lets you use [any Terraform/OpenTofu provider](/blog/any-terraform-provider/) in your existing projects, and now we've taken it to the next level. With [Pulumi CLI version 3.145.0](https://github.com/pulumi/pulumi/releases/tag/v3.145.0), you can now automatically convert **ANY** Terraform project to Pulumi - even if it uses providers that don't have native Pulumi equivalents!

<!--more-->

This means you can finally:

- Convert your entire Terraform codebase without provider limitations
- Maintain access to the Terraform providers you leverage
- Modernize your infrastructure while keeping your existing resources

## Try It Now (It's Easy!)

Ready to see it in action? Just grab the latest version of Pulumi and run:

{{% chooser language "javascript,typescript,python,go,java,yaml" %}}

{{% choosable language javascript %}}

```shell
pulumi convert --from terraform --language nodejs
```

{{% /choosable %}}

{{% choosable language typescript %}}

```shell
pulumi convert --from terraform --language typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```shell
pulumi convert --from terraform --language python
```

{{% /choosable %}}

{{% choosable language go %}}

```shell
pulumi convert --from terraform --language go
```

{{% /choosable %}}

{{% choosable language java %}}

```shell
pulumi convert --from terraform --language java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```shell
pulumi convert --from terraform --language yaml
```

{{% /choosable %}}

{{% /chooser %}}

This will download the necessary plugins, run the conversion and output it in
the current directory, generating all necessary project files.

You can then run `pulumi preview` to see if the project can deploy
successfully.

## See It In Action: A Real-World Example

Let's look at something cool - we'll convert a project that combines Google Cloud with PlanetScale (a provider that isn't available in the Pulumi registry yet!). This example shows how the new converter handles mixed provider scenarios effortlessly.

Here is the Terraform code in a single main.tf file:

```terraform
terraform {
  required_version = ">= 1.1.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
    planetscale = {
      source  = "planetscale/planetscale"
      version = "~> 0.1.0"
    }
  }
}

# Configure the google provider using the project variables below.
provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
  zone    = var.gcp_zone
}

provider "planetscale" {
  service_token      = var.planetscale_service_token
  service_token_name = "planetscaletoken"
}

variable "gcp_project" {
  description = "GCP project ID"
  default     = "pulumi-convert-example-gcp-project"
}

variable "gcp_region" {
  description = "GCP region to use"
  default     = "us-central1"
}

variable "gcp_zone" {
  description = "GCP zone"
  default     = "us-central1-a"
}

variable "planetscale_org" {
  description = "PlanetScale organization name"
  default     = "pulumi-convert-planetscale-org"
}

variable "planetscale_service_token" {
  description = "PlanetScale service token secret"
  sensitive   = true
  default     = "test-planetscale-service-token"
}

# Create the PlanetScale database
resource "planetscale_database" "db" {
  name         = "pulumi-convert-db"
  organization = var.planetscale_org
}

# Generate a password for connecting to the DB
resource "planetscale_password" "db_password" {
  organization = "brandonpollack23"
  name         = "terraform-generated"
  database     = planetscale_database.db.name
  branch       = planetscale_database.db.default_branch
}

# Spin up a small GCE VM
resource "google_compute_instance" "vm" {
  name         = "demo-vm"
  machine_type = "e2-micro"
  zone         = var.gcp_zone

  # Minimal Debian boot disk
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  # Use the default VPC with a public IP
  network_interface {
    network = "default"
    access_config {}
  }

  # Pass PlanetScale connection info as metadata
  metadata = {
    DB_HOST = planetscale_database.db.url
    DB_USER = "root"
    DB_PASS = planetscale_password.db_password.plaintext
    DB_NAME = planetscale_database.db.name
  }
}
```

{{% notes type="warning" %}}
**Never** store secrets or keys in plain text in your code or commited
configuration files. I only have a db_password stored here in plain text for
the sake of readability.

Consider using [Pulumi ESC](https://www.pulumi.com/docs/esc/) to store these types of
secrets (and any other configuration!) and access them directly from your
Pulumi programs or as environmental variables with CLI.
{{% /notes %}}

This alone works if you run `terraform plan`--however without *real*
credentials nothing will really deploy, of course! You can set these in `.tfvars`,
environmental variables, command line, etc.  

Even if you use a `.tfvars` file, converting it is not currently supported, so
the configuration will need to be manually moved to stack files in your
new Pulumi project (eg `Pulumi.dev.yaml`, `Pulumi.prod.yaml`, etc).

You can convert this into a new project with the following command:

{{% chooser language "typescript,python,go,java,yaml" %}}

{{% choosable language typescript %}}

```shell
pulumi convert --from terraform --language typescript --out pulumi-ts-program
```

I have opted to output it to a different directory to preserve the contents of my Terraform project.

### Project structure

If we navigate to the `pulumi-ts-program` directory, we can see a few things:

- Pulumi.yaml, the pulumi configuration file.
- index.ts, our equivalent to main.tf for typescript projects.
- sdks directory, where the generated bridged provider is output.
- other node project artifacts such as package.json, node_modules, tsconfig.json, etc..

{{% /choosable %}}

{{% choosable language python %}}

```shell
pulumi convert --from terraform --language python --out pulumi-python-program
```

I have opted to output it to a different directory to preserve the contents of my Terraform project.

### Project structure

If we navigate to the `pulumi-python-program` directory, we can see a few things:

- Pulumi.yaml, the pulumi configuration file.
- \_\_main\_\_.py, our equivalent to main.tf for python projects.
- sdks directory, where the generated bridged provider is output.
- other python project artifacts (eg requirments.txt, pyproject.toml, etc).

{{% /choosable %}}

{{% choosable language go %}}

```shell
pulumi convert --from terraform --language go --out pulumi-go-program
```

### Project structure

If we navigate to the `pulumi-go-program` directory, we can see a few things:

- main.go, our equivalent to main.tf for golang projects
- sdks directory, where the generated bridged provider is output
- other golang project artifacts (go.mod, go.sum)

### Go specific cleanup

The go code generator outputs everything in the Terraform code, even if it is
unused. This is an error in a go program, so you'll have to assign the results
(or the variables which are unused) to the go special `_` for gcpProject,
region, and planetscaleServiceToken.

These are part of the converted output because in it's current iteration the code
converter will convert everything unconditionally, even if ultimately it is provider
configuration (see [cleanup](#cleanup)) and not actual code.

{{% /choosable %}}

{{% choosable language java %}}

```shell
pulumi convert --from terraform --language go --out pulumi-go-program
```

I have opted to output it to a different directory to preserve the contents of my Terraform project.

### Project structure

If we navigate to the `pulumi-go-program` directory, we can see a few things:

- main.go, our equivalent to main.tf for golang projects
- sdks directory, where the generated bridged provider is output
- other golang project artifacts (go.mod, go.sum)

### Java specific cleanup

The java code generator does not set up the maven dependencies for you so you
need to copy the code into your source directory (as the printed instructions
say) in the output directory.

```sh
cp -r sdks/planetscale/src/* src/
```

You also might notice the generated code is using the wrong overload for
setting the metadata in your GCP instance to set environmental variables.
Quickly making sure you call "toString" on all values in the map fixes the
issue.  The code generator does it's best to make compilable code from the get
go, but sometimes there is ambiguity like these types that the user needs to go
in and fix.

```diff
.metadata(Map.ofEntries(
+    Map.entry("DB_HOST", db.url().toString()),
-    Map.entry("DB_HOST", db.url()),
    Map.entry("DB_USER", "root"),
+   Map.entry("DB_PASS", dbPassword.plaintext().toString()),
-   Map.entry("DB_PASS", dbPassword.plaintext()),
+   Map.entry("DB_NAME", db.name().toString())
-   Map.entry("DB_NAME", db.name())
))

{{% /choosable %}}

{{% choosable language yaml %}}

```shell
pulumi convert --from terraform --language yaml --out pulumi-yaml-program
```

I have opted to output it to a different directory to preserve the contents of my Terraform project.

### Project structure

If we navigate to the `pulumi-yaml-program` directory, we can see a few things:

- Pulumi.yaml, the pulumi configuration file.
- Main.yaml, our equivalent to main.tf for golang projects.
- sdks directory, where the generated bridged provider is output.

{{% /choosable %}}

{{% /chooser %}}

### Cleanup

If we simply run `pulumi preview` this project unfortunately won't run right away.  
We need to create our stack configuration that contains the GCP and PlanetScale credentials.

These were part of our `main.tf` file, but the code generator doesn't
distinguish between provider config and code, so we need to handle this
part on our own (for now).

These can go in either your `Pulumi.yaml` or your stack configuration.  Places
for them are already generated, you just need to fill them in:

```yaml
name: terraform-convert-example
runtime: nodejs
config:
  gcp:project:
    value: 'TODO: var.gcp_project' # fill in here
  gcp:region:
    value: 'TODO: var.gcp_region'
  gcp:zone:
    value: 'TODO: var.gcp_zone'
  planetscale:serviceToken:
    value: 'TODO: var.planetscale_service_token'
  planetscale:serviceTokenName:
    value: planetscaletoken
```

After filling things in the `Pulumi.yaml` should look something like this:

```yaml
name: terraform-convert-example
runtime: nodejs
config:
  gcp:project:
    value: 'brandonpollack23'
  gcp:region:
    value: 'us-central1'
  gcp:zone:
    value: 'us-central1-a'
  planetscale:serviceToken:
    value: 'supersecrettoken'
  planetscale:serviceTokenName:
    value: planetscaletoken
```

{{% notes type="warning" %}}
Once again-and it is worth reiterating-**never *ever*** store secrets in a git repository
that is publicly visible. Even in a private repository, certain secrets might
not be something everyone with access to the source in your repository should
have access to.

We highly recommend you use a secrets and configuration service like [Pulumi ESC](https://www.pulumi.com/docs/esc/)
to handle this kind of thing.
{{% /notes %}}

Now if you run `pulumi preview` it successfully generates a plan, and if you
used real credentials in your Pulumi.yaml it'll deploy with `pulumi up`.

There is still more you can do, the generated code could be cleaned up a bit since there
may be some unused variables, etc-just as before `pulumi convert` is a good
starting point, but now that your infrastructure is just there is so much _more_ that you can do.

Here are some starting suggestions:

- Extract functionality that is shared into functions.
- Consider moving any functions that you will use in different infrastructure
  projects to a shared dependency or a 
  [Component Resource](/docs/iac/concepts/resources/components/#component-resources).
- Do anything you need to have your [infrastructure behave how you want](blog/next-level-iac-pulumi-runtime-logic/).
  Consolidate functionality from scripts, read information from files and
  services-the sky is the limit. A pulumi program is _just a program_!

## Importing Resources from Any Terraform Providers

With the release of [Pulumi 3.146.0](https://github.com/pulumi/pulumi/releases/tag/v3.146.0),
we have also added the ability to import resources from any Terraform provider.
These will be managed by the Pulumi Terraform parameterized provider and code
will also be generated to manage these resources from within Pulumi.  See the
[documentation for `pulumi import`](https://www.pulumi.com/docs/iac/cli/commands/pulumi_import/) for more
details.

Here is an example of importing a resource using [Backblaze](https://backblaze.com), a block storage service.

1. First create your application keys on the Backblaze portal.
1. Run `terraform apply` on the following:

    ```terraform
    terraform {
      required_version = ">= 1.0.0"
      required_providers {
        b2 = {
          source = "Backblaze/b2"
        }
      }
    }

    provider "b2" {
      application_key_id = "YOUR_KEY_ID"
      application_key = "YOUR_KEY"
    }

    resource "b2_bucket" "example_bucket" {
      bucket_name = "pulumi-import-test"
      bucket_type = "allPublic"
    }
    ```

1. Now from your Pulumi project be sure to add the Terraform provider, this is
   not automatic on import yet because the Pulumi project needs to be made
   aware of which particular package contains the providers.

    ```
    pulumi package add terraform-provider backblaze/b2
    ```

1. Configure the stack for your provider by adding the appropriate keys to the configuration:

    ```yaml
    name: pulumi_project
    description: A minimal AWS TypeScript Pulumi program
    runtime:
      name: nodejs
      options:
        packagemanager: npm
    config:
      pulumi:tags:
        value:
          pulumi:template: aws-typescript
      b2:applicationKeyId:
        value: 'YOUR_KEY_ID'
      b2:applicationKey:
        value: 'YOUR_KEY'
    ```

1. Get the `type` that you are importing, you can confirm this by inspecting the schema.

    ```
    pulumi package get-schema terraform-provider backblaze/b2
    ```

    Inside this json response you can find the "types" section and it contains
    "b2:index/bucket:Bucket", the type corresponding to "b2_bucket" in Terraform.
1. Find the internal provider ID to import into the Pulumi
   project.  This can usually be found by running `terraform show` and copying
   the ID.
1. Use this ID in the `import` command

    ```
    pulumi import "b2:index/bucket:Bucket" example_bucket "YOUR_BUCKET_ID"
    ```

1. After import, code will be generated for you to add to your project as you
   see fit to manage this resource from Pulumi.  By default it is created as
   `protected`, you can use `--protect=false` to disable that.

## Considerations

- We still have a bit of [unimplemented Terraform functionality](https://github.com/pulumi/pulumi-converter-terraform/issues/65) that we're tracking.  For now when these unimplemented functions are detected, they will require some manual intervention on the converted project.
- If you define your Terraform Module in a parent directory of your deployment code, you'll encounter a [known bug](https://github.com/pulumi/pulumi-converter-terraform/issues/194), but a simple workaround is to restructure your Terraform code before running a conversion.
- Terraform programs are dynamically typed, when converting to a type safe language sometimes the return type of certain existing Terraform functions is dynamic.  When this happens your generated code will have types erased (eg `any` in typescript, `interface{}` in golang).
- Variables and configuration are not yet converted automatically, so `.tfvars` files etc will need to be manually converted into Pulumi stack configurations.
- We have [some improvements](https://github.com/pulumi/pulumi/issues/18020) we're still working on to make the code generation as seamless as possible, so expect more updates soon!
- Many Terraform modules utilize the
  [`try`](https://developer.hashicorp.com/terraform/language/functions/try)
  function.  We hope to tackle handling converting this (very dynamic) function
  soon...stay tuned.

## What's Really New Here? 🚀

1. **Automatic Provider Bridging**: The converter now automatically handles any Terraform provider, even ones without Pulumi equivalents
1. **Increased Terraform Compatibility**: As part of this effort, we've bumped
   up our converage of built in Terraform functions to over 90% using code generation and
   our [Pulumi Std Provider](github.com/pulumi/pulumi-std)
3. **Improved Import Support**: With [Pulumi 3.146.0](https://github.com/pulumi/pulumi/releases/tag/v3.146.0), you can now import resources from any bridged provider
4. **Seamless Integration**: Generated code works right out of the box with minimal to no tweaking needed

## The Road Ahead

Stay tuned for even more improvements to make your infrastructure modernization journey smoother!
