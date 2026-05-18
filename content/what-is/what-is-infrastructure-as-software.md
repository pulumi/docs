---
title: What Is Infrastructure as Software?
meta_desc: "Infrastructure as Software is IaC written in general-purpose programming languages. Learn how it differs from DSL-based IaC and where it fits in practice."

type: what-is
page_title: "Infrastructure as Software: The Next Step in Cloud Management"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
authors: ["zack-chase"]
---

**Infrastructure as Software (IaS) is the practice of defining cloud infrastructure in general-purpose programming languages and applying the full toolchain of modern software engineering to it: real types, real abstractions, real tests, real package management, real APIs, and real CI/CD.** It's the natural next step after [infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/), which uses domain-specific languages (DSLs) or markup formats like HCL, JSON, and YAML, and which makes most of these engineering practices either awkward or unavailable.

The two terms overlap in intent. They both aim to replace manual cloud operations with reviewable, automated, reproducible code. They differ in *how much code engineering* you can do once your infrastructure is in code. IaS treats every cloud resource as a software object whose lifecycle can be programmed, abstracted, tested, packaged, and called from other programs. That last property is the one that opens up automation patterns DSL-based IaC can't reach: building self-service portals, embedding `pulumi up` inside a SaaS product, and using the same APIs internally that Pulumi itself uses.

In this article, we'll cover the key questions about infrastructure as software:

* What problems is infrastructure as software solving?
* How is IaS different from DSL-based IaC?
* What engineering capabilities does IaS add?
* Where does IaS shine in practice?
* What does the automation API enable?
* What are the trade-offs of IaS?
* How does Pulumi support infrastructure as software?
* Frequently asked questions about infrastructure as software

## What problems is infrastructure as software solving?

DSL-based IaC was a big jump forward in the 2010s. It introduced versioning, code review, and reproducible environments to cloud operations. Three pressures since then have stretched its limits and motivated the move toward IaS:

* **Sophisticated, multi-layer architectures.** A typical service today spans containers, Kubernetes, serverless functions, managed databases, message brokers, secrets, IAM, DNS, and CDN. Composing all of those in a DSL turns into thousands of lines of templates and external glue. A general-purpose language can express the same composition in dozens of lines of typed code.
* **Ephemeral and dynamic infrastructure.** Cloud resources change daily or hourly. Templating engines and string interpolation in YAML weren't designed for that pace; real loops, conditionals, and types are.
* **Self-service platforms.** Platform engineering teams need to expose cloud capabilities to product teams through forms, APIs, and chat commands, not by handing them HCL files. Doing that on top of a DSL means writing a templating shim; doing it on top of a programming language means importing the IaC as a library.

## How is IaS different from DSL-based IaC?

Both describe the desired state of cloud resources. The difference is what's around the description.

| Dimension | DSL-based IaC (HCL, YAML, ARM) | Infrastructure as Software |
|---|---|---|
| Language | Domain-specific | TypeScript, Python, Go, C#, Java, etc. |
| Types | Limited or none | Full static types over cloud APIs |
| Abstractions | Modules, limited generics | Classes, functions, packages, generics |
| Sharing | Per-tool registry (Terraform Registry, etc.) | Standard package managers (npm, PyPI, etc.) |
| Testing | Limited unit testing, mostly integration | Standard test runners, mocks, full TDD |
| IDE support | Good | Excellent (autocomplete, jump-to-definition, refactor) |
| Programmable lifecycle | Limited | Full programmatic API for `up` / `preview` / `destroy` |
| Conditional and looped logic | Restricted (`for_each`, `count`) | Native language constructs |
| Onboarding for software engineers | New language to learn | Same language they already use |

The most consequential row is the second-to-last one. Because IaS programs are ordinary code, the IaC engine can be called from another program, which is the foundation of [Pulumi's automation API](/docs/iac/packages-and-automation/automation-api/) and the reason IaS reaches use cases DSL-based IaC structurally can't.

## What engineering capabilities does IaS add?

The everyday capabilities that come for free with IaS are the ones DSL-based IaC has to either approximate, regenerate, or hand off to external tools:

* **Real types.** A misspelled property name, a missing required field, a type mismatch, or an invalid enum value all fail at compile time rather than at `apply` time.
* **Real abstractions.** A reusable VPC pattern becomes a class whose constructor takes typed inputs. The class can be parameterized, subclassed, and shipped as a package. A repeating module becomes a `new MyVpc(...)`, not a folder of copy-pasted templates.
* **Standard package management.** Internal components ship through npm, PyPI, Go modules, NuGet, or Maven, depending on the language. Versions follow semver. Dependencies are locked.
* **Real testing.** Use the test runner that already works for your application code (Jest, pytest, `go test`, xUnit, JUnit) for your IaC. Pulumi's [test mocks](/docs/iac/using-pulumi/testing/unit/) let unit tests run in memory without touching the cloud.
* **IDE-grade tooling.** Autocomplete, jump-to-definition, refactoring, inline error squiggles. The same VS Code, JetBrains, or Neovim setup that works for the app works for the infra.
* **Policy as code in the same language.** [Pulumi CrossGuard](/docs/insights/policy/) policies can be written in TypeScript, Python, Java, or OPA's Rego against the actual resource model. The same engineers who wrote the infrastructure can write the policies that govern it.
* **Composability with non-infra code.** Pull configuration from an internal service, fetch a list of allowed regions from a database, compute a resource name from a feature-flag value. Any of those is one library call away in IaS; they require an external preprocessing step in a DSL.

## Where does IaS shine in practice?

A few use cases consistently benefit from the IaS model:

* **Cloud-native architectures.** When the topology is a graph of microservices, Kubernetes manifests, IAM roles, queues, and managed services, expressing it as typed code with shared abstractions scales better than templating.
* **Multi-cloud and SaaS-cloud setups.** A single program can mix AWS, Azure, Google Cloud, Cloudflare, Datadog, Snowflake, and GitHub in the same model.
* **Platform engineering.** Platform teams ship typed components that product teams consume. Component versioning, dependency management, and IDE assistance all work through ordinary package managers.
* **Self-service portals.** A platform team wraps Pulumi programs in a service or CLI using the automation API. Product engineers run "create a new staging environment" or "spin up a load-test cluster" through a UI rather than by editing IaC.
* **MLOps and data infrastructure.** ML pipelines, training clusters, feature stores, and serving infrastructure all touch a lot of cloud surface and benefit from the same general-purpose language used by the data team.
* **Tightly-tested infrastructure.** When a security-critical control (an IAM boundary, a network ACL, a key policy) needs unit tests for every conceivable input, the test runner that already works for your application code is the right place to run them.

## What does the automation API enable?

The automation API is the most distinctive capability that comes with IaS. It exposes the Pulumi engine as a library that other programs can call, which means infrastructure operations can be embedded in any code path you'd otherwise embed a database call in:

* **Internal developer platforms.** A web UI that lets product teams provision approved infrastructure on demand.
* **SaaS product features.** A multi-tenant SaaS that provisions per-customer infrastructure (a dedicated cluster, a per-tenant database) as part of customer onboarding.
* **Custom CI/CD.** Pipelines that run `pulumi preview`, post the diff to Slack, and apply on approval without invoking the CLI.
* **Chatbots and runbooks.** A `/deploy staging` command in Slack that calls the automation API and reports back.
* **Ephemeral environments.** A test runner that spins up an isolated environment for every PR, runs the test suite, and tears down on completion.

Doing any of these on top of a DSL-based IaC tool typically means shelling out to a CLI, parsing text output, and hoping the next CLI release doesn't break the parser. The automation API replaces all of that with a typed function call.

See [the automation API documentation](/docs/iac/packages-and-automation/automation-api/) for the supported languages and patterns.

## What are the trade-offs of IaS?

IaS isn't a free win in every direction. A few honest trade-offs:

* **A general-purpose language is more powerful than a DSL, and the same engineer can write less-readable code with it.** A poorly written TypeScript Pulumi program with nested conditionals and side effects is harder to read than a flat HCL file. Coding standards and reviewer discipline matter more, not less.
* **The team has to know the language.** A pure ops team that's been writing HCL for years has a real adoption cost. The win comes when the team already has TypeScript / Python / Go skills, or when the platform team can mediate.
* **Programmatic flexibility makes some patterns easy that you shouldn't use.** Imperative side effects inside an IaC program (talking to external systems mid-apply) are tempting and rarely a good idea. IaS programs should still describe desired state, not script imperative steps. The discipline has to come from the team.
* **DSL-based tools have a longer history and a larger module ecosystem in some categories.** Terraform's public module registry is still bigger than Pulumi's component ecosystem for many niche providers. The gap is closing, but it exists.

The pragmatic answer for most teams: start with the language they already use, write IaS programs that read like code review-ready software (small functions, typed inputs, components for repeated patterns), and treat the IaS advantages as a way to do less work, not as a license to do more.

## How does Pulumi support infrastructure as software?

Pulumi was built around the IaS model from day one.

* **First-class languages.** TypeScript, JavaScript, Python, Go, C# (.NET), Java, plus YAML for teams that want a markup format. Every language has full SDKs, full test mocks, and full ecosystem support.
* **Generated, typed SDKs for every cloud.** AWS, Azure, Google Cloud, Kubernetes, plus 100+ other providers (Cloudflare, Snowflake, Datadog, GitHub, MongoDB Atlas, etc.). Types are generated from each provider's API so they reflect the real cloud surface.
* **Component model.** Reusable [Pulumi components](/docs/iac/concepts/components/) ship as ordinary packages in your language's package manager.
* **Policy as code with CrossGuard.** Write policies in the same language as the infrastructure. Run them in CI and as a deploy gate.
* **Secrets with Pulumi ESC.** [Pulumi ESC](/product/esc/) keeps secrets out of code and state, pulled at runtime by IaS programs, CI jobs, and applications.
* **Automation API.** Embed `pulumi up`, `pulumi preview`, and `pulumi destroy` inside any program that needs to provision infrastructure programmatically.
* **CI/CD-native.** Pulumi runs in every major CI/CD system. The [continuous delivery guide](/docs/iac/guides/continuous-delivery/) covers the common patterns.

[Get started with Pulumi](/docs/get-started/) to provision and manage cloud infrastructure in the language your team already uses.

## Frequently asked questions about infrastructure as software

### What's the difference between IaC and IaS?

IaC is the broad practice of defining cloud infrastructure in code. IaS is the specific style of IaC that uses general-purpose programming languages and applies the full software-engineering toolchain (types, tests, abstractions, packages, programmatic APIs). All IaS is IaC; not all IaC is IaS.

### Is Terraform IaS?

No. Terraform's HCL is a DSL designed specifically for IaC. The CDK for Terraform (CDKTF) layer on top of Terraform is closer to IaS because it lets you write TypeScript, Python, Go, or Java that synthesizes HCL. Pulumi differs from CDKTF in that there's no HCL layer in the middle: the IaS program drives the Pulumi engine directly.

### Is CloudFormation IaS?

Plain CloudFormation YAML is a DSL. The AWS Cloud Development Kit (CDK) is an IaS-style layer on top of CloudFormation: you write TypeScript/Python/etc. that synthesizes CloudFormation templates. As with CDKTF, the synthesis step is the structural difference from Pulumi, which has no template synthesis layer.

### Do I have to be a software engineer to use IaS?

Not exclusively, but it helps. The model assumes basic competence in a programming language. Ops engineers without that background take longer to ramp up than they would on HCL. The flip side is that the same skills then carry across the whole platform; you don't have two languages to maintain.

### What about teams that write all their infrastructure in YAML?

YAML works fine for small footprints and simple configurations. Most teams that hit the limits of YAML do so when they try to express conditionals, loops, or per-environment variations and end up running YAML through a templating engine (Helm, Kustomize, jsonnet). At that point, an IaS language is usually a cleaner answer than another templating layer.

### How does IaS support testing?

The same way any other software does. Use the language's standard test runner (Jest, pytest, `go test`, xUnit), use Pulumi's test mocks to replace cloud calls in unit tests, and use the automation API to spin up ephemeral stacks for integration tests. See [how to step up cloud infrastructure testing](/what-is/how-to-step-up-cloud-infrastructure-testing/) for the layered testing model.

### Does IaS replace platform engineering tools?

No, it enables them. A platform engineering team uses IaS to build the components and automation that product teams consume. The IaS programs are the platform team's product; the automation API and components are the interface. See [What is Platform Engineering?](/what-is/what-is-platform-engineering/).

### Can I migrate from Terraform to IaS?

Yes. Pulumi can [import existing resources](/docs/iac/adopting-pulumi/import/) without recreating them, and `pulumi convert` can translate HCL source into a Pulumi program in the language of your choice. Most teams migrate incrementally: new infrastructure starts in IaS, existing HCL stays in place until it changes.

### Does IaS work for multi-cloud?

Yes. One IaS program can mix resources from AWS, Azure, Google Cloud, Kubernetes, and any of 100+ other Pulumi providers. The general-purpose language gives you a single place to express the cross-cloud dependencies and types.

### Is IaS slower than IaC at scale?

In `pulumi up` runtime, no. The engine plans and applies the same way regardless of which language the program was written in. In developer iteration speed, IaS is usually faster because the IDE tooling (autocomplete, types, jump-to-definition) shortens the edit-debug cycle on every change.

## Learn more

Pulumi is the leading platform built around infrastructure as software: full programming languages, typed cloud SDKs, real tests, real package management, and an automation API that lets you embed `pulumi up` inside any other program. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
* [Infrastructure as Code for DevOps](/what-is/infrastructure-as-code-for-devops/)
* [Infrastructure as Code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/)
* [How to Step Up Cloud Infrastructure Testing](/what-is/how-to-step-up-cloud-infrastructure-testing/)
