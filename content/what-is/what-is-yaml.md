---
title: What is YAML?
meta_desc: "YAML is a human-readable data serialization language used for configuration files. Learn its syntax, common pitfalls, and how to use it with Pulumi."
meta_image: /images/what-is/what-is-yaml-meta.png
type: what-is
page_title: "What is YAML?"

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
authors: ["kat-cosgrove"]
---

**YAML is a human-readable data serialization language used primarily for configuration files, data exchange between programs, and declarative tooling.** It uses indentation and a small set of punctuation characters to express maps, lists, and scalar values, which makes structured data easy for humans to read and write while remaining parseable by machines.

YAML stands for "YAML Ain't Markup Language" (a recursive acronym; the project was originally called "Yet Another Markup Language"). The first specification shipped in 2001, and the current stable revision is YAML 1.2.2, published in 2021. Today YAML is the de facto configuration format for Kubernetes, GitHub Actions, GitLab CI, Ansible, Docker Compose, OpenAPI, Helm charts, and many [infrastructure as code](/what-is/what-is-infrastructure-as-code/) tools, including Pulumi.

In this article, we'll cover the key questions about YAML:

* Why is YAML so widely used?
* What does YAML syntax look like?
* How is YAML different from JSON and TOML?
* What are the common pitfalls and gotchas?
* How do you use YAML with Pulumi?
* When should you reach for a real programming language instead?
* Frequently asked questions about YAML

## Why is YAML so widely used?

YAML became the default configuration format for cloud-native tooling for a few practical reasons.

### It's optimized for humans first

Unlike XML, which is verbose, or JSON, which is strict about quotes, commas, and brackets, YAML reads close to plain English with indentation. That low syntactic overhead matters when a config file is the primary interface between a tool and its users — Kubernetes manifests, CI pipelines, and Ansible playbooks are all read and edited dozens of times a day.

### It's a strict superset of JSON

Every valid JSON document is also valid YAML 1.2. That means any tool that already speaks JSON can adopt YAML with minimal effort, and developers can paste JSON into a YAML file when they need to.

### It supports rich structure without ceremony

YAML expresses maps, lists, scalars, multi-line strings, anchors and aliases (reusable nodes), and explicit types in a compact form. For configuration that has to describe nested objects (a Kubernetes Deployment with containers, volumes, probes, and environment variables) this is significantly more readable than the equivalent JSON.

### It dominates the cloud-native ecosystem

Kubernetes alone made YAML the lingua franca of modern operations. Once kubectl, Helm, and the CNCF tool catalog standardized on YAML, every adjacent tool followed: Argo CD, Crossplane, Backstage, Tekton, GitHub Actions, GitLab CI, and so on.

## What does YAML syntax look like?

Here is a YAML document that exercises the most common constructs:

```yaml
# An easy-to-read set of data on the Pulumi mascot, in YAML
name: Pulumipus
breed: platypus
color: purple
mascot: true
age: 5
hobbies:
  - kayaking
  - bouldering
  - reading
  - coding
languages:
  python:
    level: expert
    version: "3.12"
  typescript:
    level: expert
  go:
    level: expert
```

A few things to notice:

* **Documents** can begin with `---` and end with `...`, though both markers are optional for single-document files.
* **Key-value pairs** use `key: value`. The space after the colon is required.
* **Strings** don't need quotes for simple values. Quote with `"..."` or `'...'` when a value would otherwise be parsed as another type (a boolean, a number, a date, or `null`).
* **Lists** use a leading `-` on indented items, or compact flow style `[a, b, c]`.
* **Maps** are sets of key-value pairs, nested by indentation, or compact flow style `{key: value}`.
* **Comments** start with `#` and run to the end of the line.

### Booleans, nulls, and the "Norway problem"

YAML 1.1 (still used by some parsers, notably PyYAML by default) treats a long list of words as booleans: `yes`, `no`, `on`, `off`, `y`, `n`, `true`, `false`, plus case variations. That produces a famous surprise where the two-letter country code for Norway, `NO`, parses as `false`. YAML 1.2 narrowed the list to `true` and `false` only. If you're targeting older parsers, quote any ambiguous string: `country: "NO"`.

### Multi-line strings

YAML offers two block scalar styles for multi-line text:

```yaml
literal: |
  line one
  line two
  preserves newlines

folded: >
  this paragraph
  folds line breaks
  into spaces
```

`|` preserves newlines; `>` folds them into spaces. Both are heavily used for shell scripts in CI configs and embedded templates.

### Anchors and aliases

Anchors (`&`) and aliases (`*`) let you reuse a node:

```yaml
defaults: &defaults
  retries: 3
  timeout: 30s

dev:
  <<: *defaults
  endpoint: dev.example.com

prod:
  <<: *defaults
  endpoint: prod.example.com
```

This is convenient, but it's also the source of many bugs: anchors aren't visible across files, and the merge key `<<` is an extension that some YAML 1.2 parsers don't support. Most production teams use templating engines (Helm, Jsonnet, CUE) or programmatic IaC instead of relying on anchors.

## How is YAML different from JSON and TOML?

| Dimension | YAML | JSON | TOML |
|---|---|---|---|
| Primary use | Configuration, manifests | Data exchange, APIs | Application config |
| Readability | High | Medium | High for flat data |
| Comments | Yes (`#`) | No | Yes (`#`) |
| Multi-line strings | Yes (block scalars) | No (escape sequences) | Yes (triple-quoted) |
| Anchors / refs | Yes | No | No |
| Strict typing | Loose | Strict | Strict |
| Indentation-sensitive | Yes | No | No |
| Superset of | JSON | — | — |
| Best for | Human-edited configs | Machine-to-machine | Small flat configs |

YAML's superpower is human readability of deeply nested structures. JSON's superpower is unambiguous machine parsing. TOML's superpower is being obvious for flat or shallowly nested application configuration (Cargo, pyproject.toml). Pick the one that matches the audience: humans editing complex structure leans YAML; programs exchanging data leans JSON; small flat app config leans TOML.

## What are the common pitfalls and gotchas?

YAML's flexibility is also its sharpest edge. A few traps to know:

* **Indentation must be spaces, not tabs.** Tabs are explicitly forbidden by the spec. Many editors silently convert tabs to spaces, but the moment yours doesn't, you'll get a parse error with no obvious cause.
* **Inconsistent indentation breaks things silently.** A list nested under the wrong key may parse without error and produce the wrong structure.
* **The Norway problem.** `country: NO` becomes `country: false` in YAML 1.1. Quote ambiguous values.
* **Numbers with leading zeros.** `version: 010` may parse as octal (`8`) in YAML 1.1. Quote it.
* **Times and dates.** `version: 1.10` is a float, not a string. `date: 2024-01-15` becomes a date object in some parsers. Quote when you mean a string.
* **Duplicate keys aren't always errors.** The spec says they should be, but several popular parsers silently drop one. Lint your files.
* **Anchors and aliases don't cross files.** Multi-file refactors are awkward.
* **YAML is Turing-incomplete by design.** Once your "config" needs loops, conditionals, or imports, you've outgrown it — that's the cue to move to Helm, Jsonnet, CUE, or a real programming language.

The cumulative weight of these gotchas is why teams managing large amounts of YAML often end up generating it from code rather than editing it directly.

## How do you use YAML with Pulumi?

[Pulumi](/) supports YAML as a first-class language for defining cloud infrastructure. A Pulumi YAML program looks like this:

```yaml
name: simple-bucket
runtime: yaml
description: A static website on S3
resources:
  site:
    type: aws:s3:Bucket
  site-ownership:
    type: aws:s3:BucketOwnershipControls
    properties:
      bucket: ${site.id}
      rule:
        objectOwnership: ObjectWriter
  site-public-access:
    type: aws:s3:BucketPublicAccessBlock
    properties:
      bucket: ${site.id}
      blockPublicAcls: false
  site-acl:
    type: aws:s3:BucketAclV2
    properties:
      bucket: ${site.bucket}
      acl: public-read
    options:
      dependsOn:
        - ${site-ownership}
        - ${site-public-access}
  site-website:
    type: aws:s3:BucketWebsiteConfigurationV2
    properties:
      bucket: ${site.bucket}
      indexDocument:
        suffix: index.html
  index:
    type: aws:s3:BucketObject
    properties:
      bucket: ${site.id}
      key: index.html
      source:
        fn::stringAsset: "<h1>Hello from Pulumi YAML</h1>"
      acl: public-read
      contentType: text/html
outputs:
  url: http://${site-website.websiteEndpoint}
```

A few Pulumi-specific things are happening here:

* `name` and `runtime: yaml` identify this as a Pulumi YAML program.
* `resources` is a map of resource names to declarations. Each declaration has a `type` (in the form `<provider>:<module>:<resource>`) and `properties` matching the underlying provider schema.
* `${name.property}` is Pulumi's interpolation syntax. It references outputs from other resources and creates an implicit dependency edge.
* `options.dependsOn` adds an explicit dependency edge for cases where Pulumi can't infer one.
* `fn::stringAsset`, `fn::readFile`, and other functions provide computed inputs without leaving YAML.

YAML is a good fit for Pulumi when your program is mostly declarative and you don't need conditionals, loops, or complex abstractions. Pulumi YAML programs work with the full Pulumi Cloud, state, secrets, [policy as code](/docs/insights/policy/), and [Pulumi ESC](/product/esc/) toolchain — the same as programs written in TypeScript, Python, Go, C#, or Java.

To get started, install the Pulumi CLI and create a new YAML project:

```bash
curl -fsSL https://get.pulumi.com | sh
pulumi new aws-yaml
```

See the [Pulumi YAML language reference](/docs/iac/languages-sdks/yaml/) for the full syntax.

## When should you reach for a real programming language instead?

YAML is fine for small, mostly-static configurations. It starts to crack when you need any of the following:

* **Conditionals and loops.** Spinning up `N` identical resources or branching on environment.
* **Reusable abstractions.** Wrapping common patterns into [components](/docs/iac/concepts/components/) that other teams consume.
* **Strong typing and IDE support.** Catching mistakes at edit time instead of at apply time.
* **Testing.** Unit tests against your infrastructure code with real assertions.
* **Sharing logic with application code.** Calling existing libraries, reading from APIs, computing derived values.

When those needs appear, Pulumi lets you stay on the same engine and the same Pulumi Cloud but switch the program language to TypeScript, Python, Go, C#, or Java. Many teams keep a small YAML config alongside a typed program for the same project.

For a deeper comparison of YAML against other Pulumi languages, see [Pulumi languages and SDKs](/docs/iac/languages-sdks/).

## Frequently asked questions about YAML

### What does YAML stand for?

YAML is a recursive acronym for "YAML Ain't Markup Language." The original name was "Yet Another Markup Language," but it was changed in 2002 to clarify that YAML is a data serialization format, not a document markup language like HTML or XML.

### Is YAML a programming language?

No. YAML is a data serialization language. It can represent maps, lists, scalars, and a few other types, but it has no functions, conditionals, loops, or runtime. To do anything beyond declaring data, you need a templating engine, a code generator, or a real programming language.

### Is YAML faster than JSON?

JSON parses faster in almost every implementation because its grammar is simpler. YAML's extra features (anchors, multiple document streams, implicit typing) cost CPU and memory. For machine-to-machine traffic where humans never read the data, JSON is the better choice.

### Can YAML files include other YAML files?

Not natively. The YAML spec has no `import` or `include` directive. Most tools that need this (Ansible, Helm, GitHub Actions reusable workflows) layer their own include semantics on top of YAML. Anchors and aliases let you reuse nodes within a single document but not across files.

### What is the difference between YAML 1.1 and YAML 1.2?

YAML 1.2 (2009, with a 2021 erratum revision) aligned the spec with JSON, narrowed the list of boolean keywords to `true` and `false`, and removed several implicit type quirks (octal numbers with leading zeros, sexagesimal numbers, country-code-as-boolean). Several popular libraries (notably older versions of PyYAML) still default to 1.1, which is the source of many "it works in CI but not locally" bugs.

### Why are tabs forbidden in YAML?

Because YAML uses indentation for structure, and tab width is editor-dependent. Mixing tabs and spaces would make a file's meaning depend on rendering settings rather than its contents. The spec rejects tabs at the start of a structural line to keep parsing unambiguous.

### How do I validate a YAML file?

Use `yamllint` for style and syntax, plus a schema validator for the specific tool you're targeting (`kubeval` or `kube-linter` for Kubernetes, `actionlint` for GitHub Actions, schema-aware editors like VS Code with the Red Hat YAML extension for general schemas). For Pulumi YAML programs, `pulumi preview` validates the program against the provider schemas.

### Should I use YAML or HCL for infrastructure as code?

YAML is widely supported and a strict superset of JSON, so any tool can read it. HCL is HashiCorp-specific and requires a dedicated parser. The deeper question, though, is whether either is the right fit: both struggle once your infrastructure needs reusable abstractions and tests. Pulumi lets you start in YAML and graduate to a real language without changing platforms. See [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/).

### Is Pulumi YAML production-ready?

Yes. Pulumi YAML is generally available and supports the full Pulumi feature set: providers, components, secrets, [Pulumi ESC](/product/esc/), [policy as code](/docs/insights/policy/), state management, and [CI/CD integration](/docs/iac/guides/continuous-delivery/). Teams use it for everything from quickstarts to large production workloads.

## Learn more

Pulumi lets infrastructure, developer, and security teams ship cloud infrastructure as code in YAML, TypeScript, Python, Go, C#, or Java, using the same engine and the same Pulumi Cloud. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
* [Pulumi YAML language reference](/docs/iac/languages-sdks/yaml/)
