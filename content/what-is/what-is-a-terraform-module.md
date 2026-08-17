---
title: What Is a Terraform Module?
meta_desc: "A Terraform module is a reusable container for a group of related resources, defined once and called with different inputs. Learn how modules work."
type: what-is
page_title: "What Is a Terraform Module?"
authors: ["alex-leventer"]
---

**A Terraform module is a container for multiple resources that are used together: a reusable, self-contained group of `.tf` configuration files that expose input variables, provision a set of resources, and return output values. Instead of copying the same block of HCL into every project that needs a virtual private cloud, a database, or a Kubernetes cluster, you package that configuration once as a module and call it wherever you need it, passing different inputs each time.** A module is the primary unit of reuse and encapsulation in Terraform.

Every Terraform configuration is already a module: the directory you run `terraform apply` in is the root module. Modules become powerful when the root module calls other modules (child modules) to compose larger systems from smaller, tested building blocks. The same discipline that makes functions useful in a programming language, defining a boundary once and reusing it with different arguments, is what a module brings to infrastructure configuration.

In this article, we'll cover the key questions about Terraform modules:

* What is a Terraform module?
* What is a Terraform module made of?
* How do Terraform modules work?
* What is the Terraform Registry?
* Module vs. resource: what's the difference?
* What are best practices for Terraform modules?
* What are the limitations of Terraform modules?
* How does Pulumi handle reuse?
* Frequently asked questions about Terraform modules

## What is a Terraform module?

A Terraform module is a collection of `.tf` files kept together in a single directory that define a set of resources meant to be provisioned as a unit. A module takes typed inputs (input variables), creates resources, and returns outputs that callers can consume. That interface (inputs in, outputs out) lets a module hide its internal complexity behind a small, stable surface.

Modules exist to solve a problem every growing infrastructure codebase runs into: the same patterns appear over and over. Most teams provision networks, databases, load balancers, and clusters that look nearly identical from one environment or application to the next. Without modules, that configuration gets copied and pasted, and every copy drifts as people tweak it in place. A module captures the pattern once so that a fix or an improvement made in the module propagates to every caller.

There are two roles a module can play:

* **Root module.** The directory where you run Terraform commands. Terraform always operates on a root module, even if that module never calls another one.
* **Child module.** A module called by another module through a `module` block. A child module is reusable configuration invoked with a specific set of input values.

The same module code can serve as either. A module you publish for others to consume is a child module in their configuration, but if you `cd` into its directory and run `terraform apply`, it becomes a root module.

## What is a Terraform module made of?

A module is just a directory of Terraform configuration, but three kinds of files give it a clean interface. By convention these live in separate files, though Terraform only cares that the declarations exist somewhere in the directory.

* **Input variables (`variables.tf`).** Declared with `variable` blocks, these are the arguments a caller passes in. Each variable can specify a type, a default, a description, and validation rules. Input variables are how one module produces many different results.
* **Resources (`main.tf`).** The `resource` and `data` blocks that do the actual work: creating a bucket, a subnet, a database. This is the module's implementation, and callers never touch it directly.
* **Output values (`outputs.tf`).** Declared with `output` blocks, these are the return values a module exposes to whatever called it, such as a generated bucket name, an IP address, or a connection string.

Here is a minimal module that creates an S3 bucket. These files live together in a directory, for example `modules/s3-bucket/`:

```hcl
# modules/s3-bucket/variables.tf
variable "bucket_name" {
  type        = string
  description = "The name of the S3 bucket to create."
}

variable "versioning_enabled" {
  type        = bool
  description = "Whether to enable object versioning."
  default     = false
}

# modules/s3-bucket/main.tf
resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id

  versioning_configuration {
    status = var.versioning_enabled ? "Enabled" : "Suspended"
  }
}

# modules/s3-bucket/outputs.tf
output "bucket_arn" {
  value       = aws_s3_bucket.this.arn
  description = "The ARN of the created bucket."
}
```

The `this` resource-naming convention is common in reusable modules: because the module already gives the resources context, a generic local name reads cleanly.

## How do Terraform modules work?

A module becomes useful when another configuration calls it. You invoke a child module with a `module` block, giving it a local name, a `source` that tells Terraform where to find the module's code, and values for its input variables:

```hcl
# root module: main.tf
module "logs_bucket" {
  source = "./modules/s3-bucket"

  bucket_name        = "my-app-logs"
  versioning_enabled = true
}

module "backups_bucket" {
  source = "./modules/s3-bucket"

  bucket_name = "my-app-backups"
}

output "logs_bucket_arn" {
  value = module.logs_bucket.bucket_arn
}
```

Both `module` blocks reuse the same code with different inputs, and the root module reads a child module's outputs with `module.<name>.<output>`. The `source` argument determines where Terraform loads the module from, and it accepts several kinds of location:

* **Local paths** (`./modules/s3-bucket`) for modules that live in the same repository.
* **The public Terraform Registry** (`terraform-aws-modules/vpc/aws`) for community and vendor modules.
* **Git repositories** (`git::https://github.com/org/repo.git`), including private repositories over SSH.
* **Generic and cloud storage sources** such as HTTP URLs, Amazon S3, or Google Cloud Storage.

When you run `terraform init`, Terraform downloads any remote modules into a local `.terraform/modules` directory. On `terraform plan` and `terraform apply`, it expands each `module` block into its underlying resources and manages them as part of your configuration. The module boundary is a source-code and interface boundary: at apply time, the resources a module declares are provisioned in the same [state](/what-is/what-is-terraform-state/) as the root module.

You can also provision multiple instances of a module with `count` or `for_each` on the `module` block, the same meta-arguments you use on resources.

## What is the Terraform Registry?

The [Terraform Registry](https://registry.terraform.io/) is a public catalog of shareable modules (and providers) that HashiCorp hosts. It lets you consume community- and vendor-maintained modules by referencing a short `source` address instead of copying code.

Registry module sources follow a `<NAMESPACE>/<NAME>/<PROVIDER>` format. To use a well-known AWS VPC module from the registry, you reference it by that address and pin a version:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}
```

The registry displays each module's inputs, outputs, dependencies, and versions, and modules are versioned so you can pin to a known-good release with the `version` argument. Organizations that don't want to publish publicly can run a **private registry**, either through HCP Terraform (HashiCorp's hosted platform) or a self-hosted implementation, to distribute internal modules with the same referencing model. Git and local sources remain available for teams that prefer to distribute modules without a registry at all.

## Module vs. resource: what's the difference?

These are two different levels of abstraction, and it helps to keep them distinct.

A **resource** is a single infrastructure object managed by a provider, declared with a `resource` block. An `aws_s3_bucket`, an `aws_instance`, or a `google_sql_database_instance` is a resource. It maps to one thing the provider knows how to create, read, update, and delete.

A **module** is a container for a group of resources, invoked with a `module` block. A module might create a bucket plus its versioning configuration plus a bucket policy plus an IAM role, and expose all of that behind a handful of inputs and outputs. Modules can also call other modules, nesting to compose larger systems.

| Aspect | Resource | Module |
|---|---|---|
| Declared with | `resource` block | `module` block |
| Represents | A single infrastructure object | A group of resources used together |
| Defined by | A Terraform provider | Terraform configuration (`.tf` files) |
| Referenced as | `aws_s3_bucket.this.id` | `module.logs_bucket.bucket_arn` |
| Purpose | Create/manage one object | Encapsulate and reuse a pattern |
| Can contain | Provider-defined attributes | Resources, data sources, and other modules |

A useful mental model: resources are the primitives a provider gives you, and modules are the reusable compositions you build from those primitives.

## What are best practices for Terraform modules?

A few conventions make modules easier to consume and maintain:

* **Keep modules focused.** A module should do one thing (a network, a database, a service) rather than trying to provision an entire environment. Small, composable modules are easier to test and reuse than one large monolith.
* **Design a clear interface.** Give every input variable a `type`, a `description`, and, where appropriate, `validation` rules and a sensible `default`. Expose only the outputs callers actually need.
* **Pin module and provider versions.** Use the `version` argument on registry modules and version constraints on providers so an upstream change can't alter your infrastructure unexpectedly.
* **Document the module.** A `README.md` describing inputs, outputs, and an example call makes a module usable by people who didn't write it.
* **Don't over-modularize early.** A thin wrapper around a single resource often adds indirection without much benefit. Extract a module when a pattern has proven itself by repeating, not on the first occurrence.
* **Follow the standard file layout.** The `main.tf`, `variables.tf`, `outputs.tf` convention makes any module immediately navigable to another Terraform user.

## What are the limitations of Terraform modules?

Modules are the right tool for reuse in Terraform, but they operate within the constraints of HCL, which is a declarative configuration language rather than a general-purpose programming language.

* **Logic is expressed in HCL.** Conditionals become ternary expressions, iteration becomes `count` and `for_each`, and there are no user-defined functions. Complex composition can push HCL past what it reads cleanly.
* **No true encapsulation of state.** A module doesn't get its own isolated state; its resources land in the caller's state file. Splitting state is a separate concern handled with multiple root modules and backends, not with child modules.
* **Versioning and distribution are conventions.** Registry versioning helps, but there's no compiler or type system across the module boundary spanning multiple languages; the contract is the set of variables and outputs plus documentation.
* **Testing requires additional tooling.** Validating a module typically means standing up real or simulated infrastructure with tools such as Terraform's built-in test framework or Terratest, rather than unit-testing plain functions.

None of these make modules a poor choice; they're the natural boundaries of a domain-specific configuration language. They do explain why some teams prefer an approach built on general-purpose programming languages, which is where Pulumi takes a different path.

## How does Pulumi handle reuse?

Pulumi is an [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform that takes a different approach to the same reuse problem. Instead of a configuration language with a module system layered on top, Pulumi lets you define infrastructure in general-purpose programming languages — TypeScript, JavaScript, Python, Go, .NET, and Java — so the reuse mechanisms are the ones those languages already provide: functions, classes, and packages.

The closest analog to a Terraform module is a Pulumi **component**. A [component resource](/docs/iac/concepts/components/) is a class that groups multiple child resources behind a constructor, taking typed arguments and exposing typed outputs, the same inputs-in, outputs-out contract a module has, but expressed as a real class in your language:

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

export class S3Bucket extends pulumi.ComponentResource {
    public readonly bucketArn: pulumi.Output<string>;

    constructor(name: string, args: { versioningEnabled?: boolean }, opts?: pulumi.ComponentResourceOptions) {
        super("myorg:storage:S3Bucket", name, {}, opts);

        const bucket = new aws.s3.BucketV2(name, {}, { parent: this });

        new aws.s3.BucketVersioningV2(name, {
            bucket: bucket.id,
            versioningConfiguration: {
                status: args.versioningEnabled ? "Enabled" : "Suspended",
            },
        }, { parent: this });

        this.bucketArn = bucket.arn;
        this.registerOutputs({ bucketArn: this.bucketArn });
    }
}
```

Because a component is ordinary code, you get the reuse tools of the host language for free: loops, conditionals, functions, unit tests with your normal test framework, and package managers (npm, PyPI, NuGet, Maven) for distribution. A component packaged as a [Pulumi package](/docs/iac/concepts/packages/) can be published with a Pulumi plugin so that Pulumi generates SDKs for it in every supported language, letting a component authored in one language be consumed from another.

Pulumi also interoperates with the Terraform ecosystem rather than replacing it. You can [consume an existing Terraform module directly from a Pulumi program](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), which lets teams reuse modules they've already written while adopting Pulumi. For a side-by-side of the two tools' models and terminology, see the [Pulumi and Terraform comparison](/docs/iac/comparisons/terraform/).

| Aspect | Terraform module | Pulumi component |
|---|---|---|
| Authored in | HCL configuration | TypeScript, JavaScript, Python, Go, .NET, or Java |
| Reuse unit | Directory of `.tf` files | Class extending `ComponentResource` |
| Interface | Input variables and outputs | Constructor arguments and class properties |
| Logic | HCL expressions, `count`/`for_each` | Full language: loops, functions, conditionals |
| Distribution | Terraform Registry, Git, local paths | Language package managers; Pulumi Packages for multi-language |
| Testing | Terraform test framework, Terratest | The language's native unit-testing tools |

Neither approach is universally correct. Terraform modules are a mature, widely adopted pattern with a large public registry; Pulumi components trade that ecosystem for the expressiveness and tooling of general-purpose languages. Teams choose based on which model fits their skills and their existing infrastructure.

## Frequently asked questions about Terraform modules

### What is a Terraform module in simple terms?

A Terraform module is a reusable package of infrastructure configuration. It groups a set of related resources (say, everything needed for a network) into one directory with defined inputs and outputs, so you can create that same set of resources many times with different settings instead of copying and pasting the configuration.

### What is the difference between a Terraform module and a resource?

A resource is a single infrastructure object, declared with a `resource` block and defined by a provider (for example, one `aws_s3_bucket`). A module is a container for a group of resources, invoked with a `module` block, that packages those resources behind a set of inputs and outputs. Resources are the primitives; modules are reusable compositions built from them.

### What is the Terraform Registry?

The Terraform Registry is HashiCorp's public catalog of shareable modules and providers. You reference a registry module by a short `<NAMESPACE>/<NAME>/<PROVIDER>` source address and pin a version, and Terraform downloads it on `terraform init`. Organizations can also run a private registry to distribute internal modules the same way.

### How do you create a Terraform module?

Put your Terraform configuration in a directory with three conventional files: `variables.tf` declaring the input variables, `main.tf` declaring the resources, and `outputs.tf` declaring the values to return. That directory is now a module. Any other configuration can call it with a `module` block whose `source` points at the directory (or a Git repository or registry address), passing values for the inputs.

### What is the difference between a root module and a child module?

The root module is the directory where you run Terraform commands; Terraform always operates on a root module. A child module is any module that another module calls through a `module` block. The same module code can act as either: it's a child module when called by someone else's configuration, and a root module if you run Terraform directly inside it.

### Where can Terraform modules be stored?

The `source` argument supports several locations: a local path in the same repository, the public Terraform Registry, a Git repository (including private ones over SSH), and generic or cloud object-storage sources such as HTTP URLs, Amazon S3, or Google Cloud Storage. Registry and Git sources also support version pinning.

### What is the difference between a Terraform module and a Pulumi component?

Both encapsulate a group of resources behind inputs and outputs. A Terraform module is a directory of HCL files, and a Pulumi component is a class in a general-purpose language (TypeScript, Python, Go, .NET, Java) that extends `ComponentResource`. The practical difference is expressiveness and distribution: components use the host language's loops, functions, and unit-testing tools, and can be packaged as Pulumi Packages for use across multiple languages. Pulumi can also consume existing Terraform modules directly.

### Can you use Terraform modules with Pulumi?

Yes. Pulumi can consume an existing Terraform module directly from a Pulumi program, so teams can reuse modules they've already written while adopting Pulumi's programming model. See the guide on [using a Terraform module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/).

## Learn more

Terraform modules and Pulumi components solve the same reuse problem with different tools: one uses a configuration language and a public registry, the other uses general-purpose programming languages and their package ecosystems. If you're evaluating both, the [Pulumi and Terraform comparison](/docs/iac/comparisons/terraform/) maps the concepts side by side, and you can [use your existing Terraform modules from Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) without rewriting them.

Related reading:

* [Pulumi components](/docs/iac/concepts/components/)
* [Pulumi packages](/docs/iac/concepts/packages/)
* [Pulumi resources](/docs/iac/concepts/resources/)
* [Use a Terraform module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/)
* [Pulumi and Terraform comparison](/docs/iac/comparisons/terraform/)
* [Pulumi IaC concepts](/docs/iac/concepts/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is Terraform state?](/what-is/what-is-terraform-state/)
* [What is Terragrunt?](/what-is/what-is-terragrunt/)
