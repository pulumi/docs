---
title: "Converting Terraform to Pulumi Just Got Easier"
date: 2025-03-04
meta_desc: "Pulumi's conversion tools now automatically handle any Terraform provider,
  making migration easier than ever"
meta_image: meta.png
authors:
  - brandon-pollack
  - meagan-cojocar
tags:
  - terraform
  - features
search:
  keywords:
    - Terraform
    - conversion
    - Terraform provider
    - infrastructure modernization
---

Big news for infrastructure teams looking to migrate – we've just supercharged Pulumi's Terraform conversion capabilities, making it easier than ever to modernize your infrastructure as code.

Pulumi already lets you use [any Terraform/OpenTofu provider](/blog/any-terraform-provider/) in your existing projects, and now we've taken it to the next level. With [Pulumi CLI version 3.153.0](https://github.com/pulumi/pulumi/releases/tag/v3.153.0) and above, you can now automatically convert **ANY** Terraform project to Pulumi _and_ import its resources - even if it uses providers that don't have native Pulumi equivalents!

<!--more-->

This means you can finally:

- Convert your entire Terraform codebase without provider limitations
- Maintain access to the Terraform providers you leverage
- Modernize your infrastructure deployment while keeping your existing resources

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

This will download the necessary plugins, run the conversion and output it in the current directory, generating all necessary project files.

You can then run `pulumi preview` to see if the project can deploy successfully.

## See It In Action: A Real-World Example

Let's look at something cool – we'll convert a project that combines Google Cloud with PlanetScale (a provider that isn't available in the Pulumi registry yet!). This example shows how the new converter handles mixed provider scenarios effortlessly.

Here is the Terraform code in a single `main.tf` file:

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
**Never** store secrets or keys in plain text in your code or configuration files committed to a code repository. We are only storing a `db_password` here in plain text for the sake of readability.

Consider using [Pulumi ESC](https://www.pulumi.com/docs/esc/) to store these types of secrets (and any other configuration!) and access them directly from your Pulumi programs or as environment variables with the CLI.
{{% /notes %}}

Note that while this program will `terraform plan` successfully, you'll need *real* credentials in order to actually `apply` and deploy it. You can set these in `.tfvars`, environment variables, or on the command line, for instance.

We'll convert this into a new Pulumi project with the following command:

{{% chooser language "typescript,python,go,java,yaml" %}}

{{% choosable language typescript %}}

```shell
pulumi convert --from terraform --language typescript --out pulumi-ts-program
```

Here we've opted to output generated code to a different directory (`pulumi-ts-program`) to preserve the contents of our Terraform project.

### Project structure

If we navigate to the `pulumi-ts-program` directory, we can see a few things:

- `Pulumi.yaml`, the Pulumi configuration file.
- `index.ts`, our equivalent to `main.tf` for TypeScript projects.
- An `sdks` directory, where generated code for providers not in the Pulumi registry (in this case, `planetscale`) has been placed.
- Other Node.js project artifacts such as `package.json`, `node_modules`, `tsconfig.json`, and so on.

{{% /choosable %}}

{{% choosable language python %}}

```shell
pulumi convert --from terraform --language python --out pulumi-python-program
```

Here we've opted to output generated code to a different directory (`pulumi-python-program`) to preserve the contents of our Terraform project.

### Project structure

If we navigate to the `pulumi-python-program` directory, we can see a few things:

- `Pulumi.yaml`, the Pulumi configuration file.
- `__main__.py`, our equivalent to `main.tf` for Python projects.
- An `sdks` directory, where generated code for providers not in the Pulumi registry (in this case, `planetscale`) has been placed.
- Other Python project artifacts such as `requirements.txt` or `pyproject.toml`.

{{% /choosable %}}

{{% choosable language go %}}

```shell
pulumi convert --from terraform --language go --out pulumi-go-program
```

Here we've opted to output generated code to a different directory (`pulumi-go-program`) to preserve the contents of our Terraform project.

### Project structure

If we navigate to the `pulumi-go-program` directory, we can see a few things:

- `Pulumi.yaml`, the Pulumi configuration file.
- `main.go`, our equivalent to `main.tf` for Go projects.
- An `sdks` directory, where generated code for providers not in the Pulumi registry (in this case, `planetscale`) has been placed.
- Other Go project artifacts such as `go.mod` and `go.sum`.

### Go-specific cleanup

Pulumi's Go code generation currently produces code for everything in the Terraform code, even if it is unused. This is an error in a Go program, so we'll have to rename variables such as `gcpProject`, `region`, and `planetscaleServiceToken` to the special `_` identifier in order to avoid compilation errors. We plan on continuing to polish the Go experience to remove manual steps like this.

{{% /choosable %}}

{{% choosable language java %}}

```shell
pulumi convert --from terraform --language java --out pulumi-java-program
```

Here we've opted to output generated code to a different directory (`pulumi-java-program`) to preserve the contents of our Terraform project.

### Project structure

If we navigate to the `pulumi-java-program` directory, we can see a few things:

- `Pulumi.yaml`, the Pulumi configuration file.
- An `App.java` file under the `src/main/java/generated_program` directory, our equivalent to `main.tf` for Java projects.
- An `sdks` directory, where generated code for providers not in the Pulumi registry (in this case, `planetscale`) has been placed.
- Other Java project artifacts such as `pom.xml`.

### Java-specific cleanup

Pulumi's Java code generation currently does not set up Maven project dependencies for you when generating SDKs for Terraform providers not in the Pulumi registry. As a result you will need to follow the printed instructions and copy the relevant SDK code into your source directory:

```sh
cp -r sdks/planetscale/src/* src/
```

You might also notice that the generated Java code is using the wrong overload for setting the metadata in our GCP instance to set environment variables. We can fix this by modifying the relevant calls to invoke `toString` on the values being passed:

```diff
.metadata(Map.ofEntries(
-    Map.entry("DB_HOST", db.url()),
+    Map.entry("DB_HOST", db.url().toString()),
     Map.entry("DB_USER", "root"),
-    Map.entry("DB_PASS", dbPassword.plaintext()),
+    Map.entry("DB_PASS", dbPassword.plaintext().toString()),
-    Map.entry("DB_NAME", db.name())
+    Map.entry("DB_NAME", db.name().toString())
))
```

While Pulumi's code generation does its best to infer the correct types from what can be quite dynamic Terraform code, there are some cases like these where manual intervention is required. We plan on continuing to polish the Java experience to remove work like this.

{{% /choosable %}}

{{% choosable language yaml %}}

```shell
pulumi convert --from terraform --language yaml --out pulumi-yaml-program
```

Here we've opted to output generated code to a different directory (`pulumi-yaml-program`) to preserve the contents of our Terraform project.

### Project structure

If we navigate to the `pulumi-yaml-program` directory, we can see a few things:

- `Pulumi.yaml`, the Pulumi configuration file.
- `Main.yaml`, our equivalent to `main.tf` for YAML projects.
- An `sdks` directory, where generated code for providers not in the Pulumi registry (in this case, `planetscale`) has been placed.

{{% /choosable %}}

{{% /chooser %}}

### Configuration

While our project's code is now ready to go, if we simply run `pulumi up` things won't work right away. We first need to create a stack configuration containing our GCP and PlanetScale credentials (you may have noticed some warnings to the tune of `warning: /Users/PulumiUser/src/MyAwesomeProject/deployment/main.tf:16,1-18: Failed to evaluate provider config; Could not evaluate expression for gcp:project` that indicate these configuration values need to be set up in Pulumi). This is akin to using e.g. `.tfvars` files in Terraform.

Pulumi has generated placeholders in the `Pulumi.yaml` file for these values, so we just need to fill them in:

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

After replacing all the placeholders we have something like this:

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
Once again—and it is worth reiterating—**never, ever** store secrets or keys in plain text in your code or configuration files committed to a code repository. Even in a private repository, certain secrets might not be something everyone with access to the source in your repository should have access to. Consider using [Pulumi ESC](https://www.pulumi.com/docs/esc/) to store these types of secrets, or consult the documentation on Pulumi's [rich set of built-in features](https://www.pulumi.com/docs/iac/concepts/secrets/) for working with secrets and encrypted configuration values.
{{% /notes %}}

Now we can run `pulumi preview` to see the proposed updates. With real credentials, we can follow that command with `pulumi up` to deploy our infrastructure.

Of course, the code generated by `pulumi convert` is just a starting point – from here there is so much _more_ that we can do! Here are some suggestions:

- Abstract functionality that is shared, perhaps by extracting it into reusable functions or classes.
- Consider moving any functions that you will use in different infrastructure projects to a shared dependency or a [Component Resource](/docs/iac/concepts/resources/components/#component-resources).
- Customize your infrastructure however you need: consolidate functionality
  from development scripts, read data from files and services, and more! You can do
  anything the language can do because a Pulumi program is _just a program_!

## Importing Resources from Any Terraform Provider

With the release of [Pulumi 3.153.0](https://github.com/pulumi/pulumi/releases/tag/v3.153.0), we have also added the ability to import resources from any Terraform provider. See the [documentation for `pulumi import`](https://www.pulumi.com/docs/iac/cli/commands/pulumi_import/) for more details. As an example, let's import a resource from [Backblaze](https://backblaze.com), a block storage service that doesn't have a native Pulumi provider:

1. First, we'll create our application keys on the Backblaze portal.
1. Next, we'll run `terraform apply` on the following `main.tf` file to create some infrastructure that we can later import into Pulumi:

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

1. From our Pulumi project, we'll use Pulumi's support for any Terraform provider to add Backblaze support to our project:

    ```
    pulumi package add terraform-provider backblaze/b2
    ```

1. We can then configure the provider in our Pulumi stack by adding the appropriate keys to our `Pulumi.yaml`:

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

1. To import a resource, we'll need both its Pulumi `type` and the internal ID used by the cloud provider (here, Backblaze) to identify the resource. We'll start with the Pulumi `type`, which we can find by inspecting the provider's schema:

    ```shell
    pulumi package get-schema terraform-provider backblaze/b2
    ```

    Inside the JSON response we can find the `resources` section and from here extract the type corresponding to the resource we want to import. In this case, the type we're after is `b2:index/bucket:Bucket`.

    For the internal provider ID, we can exploit the fact that this is part of
    the Terraform state and use the `terraform show` command to find it.

1. With all the pieces in hand, we run `pulumi import`:

    ```shell
    pulumi import "b2:index/bucket:Bucket" example_bucket "YOUR_BUCKET_ID"
    ```

1. During the import Pulumi generates code for you to add to your project that will
   allow you to manage the newly imported resource as needed. By default,
   Pulumi will set the `protect` option when generating code, which prevents
   the resources from being deleted by Pulumi; you can use `--protect=false` to
   disable this.

## Considerations

- While Pulumi's [coverage of Terraform functionality](https://github.com/pulumi/pulumi-converter-terraform/issues/65) is fairly mature at this point, some functions are still not fully implemented and may require manual intervention.
- If you define your Terraform Module in a parent directory of your deployment code, you'll encounter a [known bug](https://github.com/pulumi/pulumi-converter-terraform/issues/194) when converting. You can work around this issue by restructuring your Terraform code before starting a conversion.
- Terraform programs are dynamically typed. When converting to a type-safe language such as TypeScript or Go, it may be necessary to use "catch-all" types such as `any` in TypeScript or `interface{}` in Go in order to capture the full range of behaviour supported by the source program.
- Variables and configuration are not yet converted automatically, so `.tfvars` files etc will need to be manually converted into Pulumi stack configurations.
- We have [some improvements](https://github.com/pulumi/pulumi/issues/18020) we're still working on to make the code generation as seamless as possible, so expect more updates soon!
- A large number of Terraform modules utilize the [`try`](https://developer.hashicorp.com/terraform/language/functions/try) function.  We hope to tackle handling converting this (very dynamic) function soon – stay tuned!

## What's Really New Here? 🚀

1. **Automatic Provider Bridging**: The converter now automatically handles any Terraform provider, even ones without Pulumi equivalents
1. **Increased Terraform Compatibility**: As part of this effort, we've bumped up our coverage of built in Terraform functions to over 90% using code generation and our [`pulumi-std` Provider](github.com/pulumi/pulumi-std)
1. **Improved Import Support**: With [Pulumi 3.153.0](https://github.com/pulumi/pulumi/releases/tag/v3.153.0), you can now import resources from any Terraform provider
1. **Seamless Integration**: Generated code works right out of the box with minimal to no tweaking needed

## The Road Ahead

Stay tuned for even more improvements to make your infrastructure modernization journey smoother!

If you're new to Pulumi, check out our [getting started guide](/docs/iac/download-install/)
to get up and running in just a few minutes.
