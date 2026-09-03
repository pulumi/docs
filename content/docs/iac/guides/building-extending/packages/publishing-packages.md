---
title_tag: "Publishing to the Pulumi Registry"
meta_desc: "Learn how to publish a Pulumi package to the public Pulumi Registry so it's discoverable by the Pulumi community."
title: Publishing to the Pulumi Registry
h1: Publishing to the Pulumi Registry
menu:
    iac:
        name: Publishing to the Pulumi Registry
        parent: iac-guides-packages
        weight: 30
aliases:
- /docs/guides/pulumi-packages/how-to-author/
- /docs/using-pulumi/pulumi-packages/contribute-to-pulumi-registry/
- /docs/using-pulumi/pulumi-packages/how-to-author
- /docs/using-pulumi/pulumi-packages/authoring/
- /docs/iac/packages-and-automation/pulumi-packages/authoring/
- /docs/iac/using-pulumi/pulumi-packages/authoring/
- /docs/iac/using-pulumi/extending-pulumi/publishing-packages/
- /docs/iac/extending-pulumi/publishing-packages/
- /docs/iac/build-with-pulumi/publishing-packages/
---

This page covers publishing a [Pulumi package](/docs/iac/concepts/packages/) to the public [Pulumi Registry](/registry/) so it's discoverable by the Pulumi community.

{{% notes type="info" %}}
Publishing to your organization's [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/)? Use the [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/) command, and see [Publishing Components from GitHub Actions](/docs/idp/guides/publishing-from-github-actions/) for the full workflow. This page covers the public Pulumi Registry only.
{{% /notes %}}

You can publish the following types of packages to the public Pulumi Registry:

- A [component](/docs/iac/concepts/components/) or related group of components
- A custom provider where you define the CRUD operations for each resource type
- A bridged provider, which wraps an existing Terraform provider and leverages its code to perform the CRUD operations for each resource type

{{% notes type="info" %}}
If you are a cloud or SaaS provider interested in publishing a Pulumi provider or component, [submit a general inquiry](/contact/?form=general) and ask to be put in touch with our partners team.
{{% /notes %}}

## Which path applies

Most packages are added to the Registry by pull request. That's the path for any package published with a committed `schema.json`: a component package, a native provider, or a Terraform provider you've bridged into a package of your own. You don't need to file an issue first, and the rest of this guide walks that path end to end.

An [Any Terraform Provider](#consider-any-terraform-provider-first) package is different. These are the packages consumed with `pulumi package add terraform-provider <name>`, which the Registry calls *dynamically bridged*. They have no provider repository and no committed schema, so they can't be added by pull request; their listings come from a separate Pulumi pipeline. Open a [New Package issue](https://github.com/pulumi/registry/issues/new?template=new-package.yml) to request one instead. Use the same issue to request a package you don't maintain, or to discuss a submission before opening a pull request.

For help with either path, reach out on the [Pulumi community Slack](https://slack.pulumi.com/) or [submit a general inquiry](/contact/?form=general).

### Consider Any Terraform Provider first

If a Terraform or OpenTofu provider already exists for your service, your users may not need a Pulumi package at all. With [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/), they run `pulumi package add terraform-provider <author>/<name>` and Pulumi generates a fully typed local SDK from the provider's schema. There's nothing to author, nothing to release, and nothing to keep in sync with upstream.

Bridging it into a package of your own buys you control over the package name, the documentation, and the release cadence, at the cost of a package you have to keep current with every upstream release.

Popular Terraform providers appear in the Registry as Any Terraform Provider listings, so readers can find and evaluate them there the same as any other package. [Honeycomb](/registry/packages/honeycombio/) and [Supabase](/registry/packages/supabase/) are examples.

To have a Terraform provider listed this way, open a [New Package issue](https://github.com/pulumi/registry/issues/new?template=new-package.yml) with the provider's name and repository. These listings are generated automatically and carry no logo by default; to add one, contact [Pulumi support](/support/new/) with a link to a web-accessible SVG. Wordmarks are preferred, with all surrounding whitespace removed.

## Prerequisites

{{% notes type="info" %}}
This guide assumes you're using GitHub to host your package's source code and GitHub Actions to publish various parts of your package. Using GitHub isn't a requirement, but the Registry reads your package's schema and documentation from a GitHub release, so a package hosted elsewhere needs a different arrangement. Ask on the [Pulumi community Slack](https://slack.pulumi.com/) if that's you.
{{% /notes %}}

- [Install Pulumi](/docs/install/).
- Be familiar with the Pulumi [resource and component model](/docs/iac/concepts/resources/).
- Have the toolchain for your authoring language installed. Most new packages are written in Go. If you publish per-language SDKs, you'll also need the toolchains for those languages: Node.js for TypeScript/JavaScript, Python, .NET, and a JDK for Java.
- Host your package in a public GitHub repository, and publish a GitHub release tagged with a `v`-prefixed [Semver 2.0](https://semver.org/) version (`vX.Y.Z`). The Registry reads your package at its latest release, so a package with no release can't be listed.

## Create and name your repository

Host your package in a public GitHub repository named `pulumi-<name>`, where `<name>` is the name you'll publish under. It's normally the name of the cloud or service the package configures, and it has to be unique in the Registry.

- Bridging a Terraform provider: reuse the upstream provider's name, replacing `terraform-provider-` with `pulumi-`. `terraform-provider-auth0` becomes `pulumi-auth0`.
- A native provider: name it after the service it manages, as in [`pulumi-aws`](https://github.com/pulumi/pulumi-aws) and [`pulumi-kubernetes`](https://github.com/pulumi/pulumi-kubernetes).
- A component package built on an existing provider: use the provider name followed by the component name, such as `pulumi-aws-apigateway` for an API Gateway component built on the AWS provider.

## Build your package

Three kinds of package can be listed in the Registry, and which one you're building determines where you start:

- A Terraform or OpenTofu provider already exists for your service: [bridge it](#bridge-an-existing-terraform-provider). The bridge reuses the upstream provider's schema and CRUD implementations, so this is far less work than writing a provider yourself. Weigh it against [Any Terraform Provider](#consider-any-terraform-provider-first) first, which is no work at all.
- No Terraform provider exists, or you want a Pulumi API that differs from the one the Terraform provider exposes: [write a native provider](#write-a-native-provider) and implement each resource type's create, read, update, and delete operations.
- You're packaging reusable abstractions assembled from resources that existing providers already manage: [write a component package](#write-a-component-package).

These aren't mutually exclusive. One package can expose components alongside custom resources, and a bridged provider can ship components built on the resources it bridges.

### Bridge an existing Terraform provider

Bridging is how most packages in the Registry are built. You don't implement resources: the upstream Terraform provider supplies both the schema and the CRUD implementations, and the [Pulumi Terraform Bridge](https://github.com/pulumi/pulumi-terraform-bridge) translates them into a Pulumi package.

Most of that translation is automatic. The boilerplate maps every upstream resource and data source into your package's namespace, keeps names stable across upstream versions, and derives auto-naming rules, without per-resource configuration. Your work is mostly package metadata: the name, publisher, description, logo, and the upstream provider to track. Per-resource overrides are available for the cases where the automatic mapping produces an awkward name, but you shouldn't need them to get started.

Start from [`pulumi/pulumi-tf-provider-boilerplate`](https://github.com/pulumi/pulumi-tf-provider-boilerplate) and select "Use this template". Its `README.md` walks through the setup. For background on how bridged providers differ from native ones, see [Providers](/docs/iac/concepts/providers/).

### Write a native provider

In a native provider you define the resource schema and implement create, read, update, and delete for each resource type. Write one when there's no Terraform provider for the service, or when you want your package's API to differ from the one the Terraform provider exposes, for example to model a workflow that spans more than one upstream resource.

A native provider isn't limited to custom resources. It can also expose components and [provider functions](/docs/iac/concepts/functions/) alongside them.

Start from [`pulumi/pulumi-provider-boilerplate`](https://github.com/pulumi/pulumi-provider-boilerplate) and select "Use this template". See [Building providers](/docs/iac/guides/building-extending/providers/) for the concepts, and the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/packages/pulumi-go-provider-sdk/) for the supported way to write one in Go.

### Write a component package

A component package bundles [components](/docs/iac/concepts/components/): abstractions that compose resources other providers manage. See [Packaging components](/docs/iac/guides/building-extending/components/packaging-components/) for the recommended approach.

A component package can also declare custom resources of its own, so you aren't limited to composing what other providers offer. If your components need a resource type no provider manages, you can implement it in the same package.

Components are most often distributed as [source-based plugin packages](/docs/iac/guides/building-extending/packages/source-based-plugin/), which the public Registry doesn't support. To list a component package in the public Registry, build it as an [executable plugin package](/docs/iac/guides/building-extending/packages/executable-plugin/).

### Identify your provider to the vendor's API

Set a User-Agent header on your provider's API client that identifies the provider and its version, for example `pulumi-your-package/1.2.3`.

Vendors gauge how much to invest in an integration by the traffic they can attribute to it, and a provider that sends its SDK's default user agent isn't counted. A bridged provider that falls through to the vendored HTTP client identifies itself as OpenTofu or Terraform rather than Pulumi.

Where you set it depends on the SDK you wrap; look for the client constructor's user-agent or "application name" option. Pulumi has no canonical mechanism for this, and there's no `tfbridge.ProviderInfo` field that sets it, so if you're bridging a Terraform provider and can't find a hook, ask on the [Pulumi community Slack](https://slack.pulumi.com/).

## Write the overview page

`docs/_index.md` is the only documentation page the Registry requires. It's the page a reader lands on from the Registry's package list, and where they decide whether your package does what they need.

You author it in your provider's repository, at `docs/_index.md`. The Registry's documentation generator fetches it from your release tag and publishes it; you never commit it to [`pulumi/registry`](https://github.com/pulumi/registry) yourself.

The sections below are the standard we hold overview pages to, and the order in which they should appear. They apply to every package, whether you publish per-language SDKs or your users generate one locally.

### Front matter

The file starts with a YAML front matter block. Documentation generation fails without it, with `expected file ... to start with YAML front-matter`. It's the most common reason a package's documentation fails to publish.

```yaml
---
title: Logfire
meta_desc: Use the Pulumi Logfire provider to manage projects, alerts, channels, dashboards, and API tokens.
layout: package
---
```

| Key | Notes |
|---|---|
| `title` | The package display name. Should match `displayName` in your `schema.json`. Rendered as the page's heading. |
| `meta_desc` | One sentence, used as the page's meta description. Include the package name. |
| `layout` | Use `package`. |

The generator adds a `# WARNING:` comment and an `edit_url:` key of its own when it publishes; you don't write those.

### Page structure

Use `##` for every top-level section and `###` for anything nested beneath one. Don't use `#`: the page heading comes from the front matter `title`, and a second H1 in the body competes with it.

Open with prose directly beneath the front matter, with no heading above it. The page already carries the package name as its title, so an `## Overview` heading underneath it is redundant. State what the package lets the reader do, and link the product or service:

```markdown
The Logfire provider for Pulumi lets you manage [Logfire](https://pydantic.dev/logfire) resources,
including projects, alerts, channels, dashboards, and API tokens, as part of your Pulumi programs.
```

Keep it to a short paragraph. The detail goes in the sections below.

Three markup patterns don't survive the Registry's rendering, and the automated check on your submission flags them:

| Instead of | Use |
|---|---|
| A relative image: `![](./diagram.png)` or `<img src="./diagram.png">` | An absolute URL to the image |
| A raw relative link: `<a href="./configuration">` | A Markdown link to an absolute URL |
| A link to a file: `](configuration.md)` | The published URL of the target page |

### Installation

Your page's `## Installation` section gives the installation command for each language your package supports. A command is more useful than a link, because a reader can copy it and run it.

Wrap the commands in the site's language chooser so a reader sees only the language they use. The chooser is a pair of Hugo shortcodes, `chooser` and `choosable`, and the language keys are `typescript`, `python`, `go`, `csharp`, `java`, `yaml`, and `hcl`. List in the `chooser` tag only the languages your package actually supports:

````markdown
## Installation

{{</* chooser language "typescript,python,go,csharp,java,yaml,hcl" */>}}
{{%/* choosable language typescript */%}}

```bash
npm install @your-org/your-package
```

{{%/* /choosable */%}}
{{%/* choosable language python */%}}

```bash
pip install your_org_your_package
```

{{%/* /choosable */%}}
{{%/* choosable language go */%}}

```bash
go get github.com/your-org/pulumi-your-package/sdk/go/yourpackage
```

{{%/* /choosable */%}}
{{%/* choosable language csharp */%}}

```bash
dotnet add package YourOrg.YourPackage
```

{{%/* /choosable */%}}
{{%/* choosable language java */%}}

Maven:

```xml
<dependency>
    <groupId>com.yourorg</groupId>
    <artifactId>your-package</artifactId>
    <version>1.2.3</version>
</dependency>
```

Gradle:

```groovy
implementation 'com.yourorg:your-package:1.2.3'
```

{{%/* /choosable */%}}
{{%/* choosable language yaml */%}}

```bash
pulumi package add your-package
```

{{%/* /choosable */%}}
{{%/* choosable language hcl */%}}

```hcl
terraform {
  required_providers {
    your-package = {
      source  = "pulumi/your-package"
      version = "1.2.3"
    }
  }
}
```

Then run `pulumi install`.

{{%/* /choosable */%}}
{{</* /chooser */>}}
````

A few things to watch:

- The two shortcodes take different delimiters, and the difference is deliberate. `{{%/* choosable */%}}` renders the content it wraps as Markdown, which the code fences inside each block need. `{{</* chooser */>}}` passes its content through unrendered, which is right because that content is the already-rendered `choosable` blocks. Mixing them up silently breaks the page.
- YAML consumes the package directly through its schema, so its installation command is `pulumi package add`.
- [Pulumi HCL](/docs/iac/languages-sdks/hcl/) resolves packages from a `required_providers` block rather than a command. Give the block, and note that `pulumi install` applies it. A `pulumi/`-prefixed source names a Pulumi Registry package, and it takes an exact version rather than a constraint.
- Java has no one-line install command, so give the Maven and Gradle dependency coordinates, as above.
- If you publish no SDKs, `pulumi package add` is your whole installation section: one command, and no chooser needed. Many bridged providers title this section "Generate Provider", but `## Installation` is the preferred heading.
- Links to package feeds (npm, PyPI, NuGet, pkg.go.dev, Maven Central) are accepted, and many existing packages use them instead. Prefer commands, and add links alongside them if you like.

You don't need to tell readers to install the plugin binary. Both a published SDK and one generated by `pulumi package add` carry your package's `pluginDownloadURL`, and `pulumi install` fetches the binary from it.

### Example usage

Your page's `## Example Usage` section provides a complete, minimal Pulumi program that declares a single resource from your package, in every language you support. It needs the imports and enough surrounding code to actually run: a bare resource declaration on its own isn't enough.

Alongside the program, give the full configuration needed to run it, as `pulumi config set` commands:

```bash
pulumi config set --secret your-package:apiToken <your-token>
pulumi config set your-package:region us-east-1
```

Optionally, show the same configuration as a [Pulumi ESC](/docs/esc/) environment. If you do, link to the ESC documentation so a reader unfamiliar with it can follow along.

### Configuration

Your page's `## Configuration` section has one required part and one optional part.

Document every configuration parameter your package accepts. For each one, give:

- Name: the bare option name, such as `apiToken`. Don't prefix it with the package name. The whole table is about your package, so repeating `your-package:` on every row is noise; the prefix belongs only in `pulumi config set` commands, where it's needed to disambiguate.
- Required?: whether the package works without it.
- Secret?: whether it should be set with `pulumi config set --secret`.
- Description: what it does and what a valid value looks like.

Two things routinely get missed here, because they aren't derivable from your schema. Put them in the parameter descriptions:

- Environment variables. A parameter's environment-variable fallback often isn't in the Pulumi schema at all (or, for a bridged provider, the Terraform schema): it's read by the vendor SDK at a layer beneath it. If a parameter can be supplied by an environment variable, say so and name the variable.
- Mutually exclusive options. If setting one parameter forbids or overrides another, or if a group of parameters must be supplied together, say so in the descriptions of every parameter involved. Nothing else in the documentation surfaces that constraint.

Optionally, follow the reference with worked examples as `pulumi config set` commands, with explanatory text and links where a reader needs background. Add these if there's more than one way to authenticate, such as CLI login, a service principal, or OIDC. Show each one as its own example instead of describing them in prose.

### Optional sections

Anything else useful goes after the sections above. What existing packages add, most common first: `## Authentication` (when there's enough of it to want its own section instead of living under Configuration), `## Environment Variables`, `## Resources`, `## Requirements` or `## Prerequisites`, `## Troubleshooting`, `## Migration` notes for a major version bump, and links to further reading.

### When the page gets long

If the installation and configuration material outgrows the overview page, with several authentication methods or a long configuration table, you can move it into a second file, `docs/installation-configuration.md`, which renders as a separate Installation & Configuration page. The large cloud providers do this: the [AWS installation page](/registry/packages/aws/installation-configuration/) runs to several thousand words covering shared credentials files, EC2 instance metadata, OIDC, and ESC.

This is about volume, not an extra requirement. Most packages don't need it, and a single overview page is a complete submission.

## Package metadata

Metadata for your package is generated from the [`schema.json`](/docs/iac/guides/building-extending/packages/schema/) in your repository. To make sure your package looks great in the Registry, don't forget to add metadata like:

- `displayName`: the friendly name for your package displayed on the Registry's browse page; this name should match the `title` in your overview page's front matter
- `description`: a short description of your package; it should include the package name
- `logoUrl`: a web-accessible URL to a logo for your package (ideally an SVG); we recommend using the githubusercontent.com raw URL for a logo stored in your package's repository; all surrounding whitespace should be removed from the logo, and wordmarks are preferred
- `publisher`: your personal or company name, as you'd like it to be shown on the Registry
- `keywords`:
  - `category/CATEGORY`: replace `CATEGORY` with one of `cloud`, `database`, `infrastructure`, `monitoring`, `network`, `utility`, `versioncontrol`
  - `kind/KIND`: replace `KIND` with one of `native`, `component`
    - Note: don't set a kind if you're bridging a Terraform provider
- `pluginDownloadURL`: a web-accessible URL that contains the compiled plugin binary associated with your package. See [Authoring an Executable Plugin Package](/docs/iac/guides/building-extending/packages/executable-plugin/#plugindownloadurl) for the URL format, hosting options (GitHub Releases, GitLab Releases, custom HTTP), and interpolation variables.

## API docs

API docs for your package are automatically generated from the `schema.json` in your repository. Many Pulumi users learn to use a Pulumi package via the API docs, since they appear automatically in many IDEs' auto-complete and inline documentation features, like Visual Studio Code's IntelliSense feature. Investing in API docs for your package is one of the best ways to improve its usability. Check out the [`pulumi-eks` schema](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) to see how it translates to the [Pulumi Registry](/registry/packages/eks/api-docs/) for an example of great API docs.

## Examples

Runnable examples are one of the most effective ways to help people adopt your package. Contribute them to the [`pulumi/examples`](https://github.com/pulumi/examples) repository on GitHub, where Pulumi users already look for working programs.

## Publish your package

Once you've authored and tested your package locally, you can publish it to make it available to the Pulumi community. You must publish:

- A GitHub release, tagged with a `v`-prefixed [Semver 2.0](https://semver.org/) version (`vX.Y.Z`). The Registry reads your schema and documentation straight from the release tag.

  If your `schema.json` declares a `version`, it has to match the release tag. Either omit the `version` key entirely, which is what bridged providers do so the Registry takes the version from the publish request, or stamp the real version at release time. A mismatch is rejected.
- The plugin binary, to a host of your choice: GitHub Releases, GitLab Releases, or a custom HTTP endpoint. Point `pluginDownloadURL` at it.

For how to cross-compile the plugin binary, the archive naming convention the CLI expects, and the supported `pluginDownloadURL` forms, see [Authoring an Executable Plugin Package](/docs/iac/guides/building-extending/packages/executable-plugin/). That guide also covers the canonical release pipeline used by Pulumi's own providers.

### Publishing SDKs

Per-language SDKs are recommended, not required. A consumer who runs [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) against your package generates a typed SDK locally from your schema, so your package is usable in every Pulumi language whether you publish anything to npm or PyPI.

Publishing SDKs is still worth doing. It lets consumers install your package the way they install everything else in their language, it makes your package discoverable in the language's own package search, and it means no SDK generation step on a first build or in CI.

Pulumi generates SDKs from your `schema.json` with [`pulumi package gen-sdk`](/docs/iac/cli/commands/pulumi_package_gen-sdk/), and you publish each one to its language's package registry:

| Language | Published to |
|----------|--------------|
| TypeScript/JavaScript | [npm Registry](https://npmjs.com) |
| Python | [Python Package Index (PyPI)](https://pypi.org) |
| .NET (C#/F#/VB) | [NuGet Gallery](https://nuget.org) |
| Java | [Maven Central](https://central.sonatype.com) |
| Go | your Git repository, by pushing a module tag (no external registry) |

We recommend publishing an SDK for every one of these languages, so consumers in any language get the same experience. Pulumi YAML and Pulumi HCL need no per-language SDK: they reference the package directly through its schema.

If your package is hosted on GitHub, the [`pulumi/pulumi-package-publisher`](https://github.com/pulumi/pulumi-package-publisher) GitHub Action publishes the npm, PyPI, NuGet, and Maven Central SDKs in a single step (select languages with its `sdk:` input); you push the Go module tag separately. See the [Publishing SDKs](/docs/iac/guides/building-extending/packages/executable-plugin/#publishing-sdks) section of the executable-plugin guide for the full workflow.

## Submit your package to the Registry

Listing your package on the Registry is one pull request against [`pulumi/registry`](https://github.com/pulumi/registry) that adds exactly one entry to [`community-packages/package-list.json`](https://github.com/pulumi/registry/blob/master/community-packages/package-list.json) and changes nothing else:

```json
{
  "repoSlug": "<owner>/<repo>",
  "schemaFile": "provider/cmd/pulumi-resource-<name>/schema.json"
}
```

| Field | Description |
|---|---|
| `repoSlug` | Your package's GitHub repository in `owner/repo` form, for example `checkly/pulumi-checkly` |
| `schemaFile` | The path to your `schema.json` from the root of your repository, for example `provider/cmd/pulumi-resource-checkly/schema.json` |

That single entry is the whole registration. Your documentation, metadata, and API docs are generated from your repository and published for you after merge, so don't commit any generated files, documentation, or package YAML. A pull request that touches anything outside the package list (and the publisher list described below) is rejected automatically.

For a complete example, see [pulumi/registry#12279](https://github.com/pulumi/registry/pull/12279).

For an individually maintained package, your GitHub handle is enough. If a company maintains it, Pulumi needs a contact person at that company before a maintainer merges.

### What happens next

Automated checks run on your pull request and post a fact sheet as a comment. They pin your package's latest release, generate its documentation, install the plugin, resolve any SDKs you advertise, and lint your overview page. Documentation generation and the plugin install are blocking; SDK resolution and the documentation lint are advisory.

If something is flagged, fix it in your package's repository: cut a release, publish an SDK, correct the schema path. Then comment `/check` on the pull request to re-run. The checks read your live repository rather than the pull request's diff, so you don't push a new commit to `pulumi/registry` to re-validate.

A Pulumi maintainer reviews the fact sheet and approves. Maintainers can also comment `/preview` to build a live preview of your package's Registry pages. Nothing merges automatically. After merge, your package listing and API docs are generated and published to the Registry.

### Register a new publisher

If you're publishing under a name that isn't already in the Registry, add it to [`publisher-names.json`](https://github.com/pulumi/registry/blob/master/tools/resourcedocsgen/pkg/publishers/publisher-names.json) in the same pull request. This is the one exception to the one-entry rule, and publishing fails without it.

The file maps the `publisher` string in your schema (the key) to that publisher's slug in the Registry backend (the value, which goes into an API path). The key and the value are usually the same. If you already ship packages under an existing slug, use that one so the two don't split.

## Keep your listing current

To ship a new version, cut a new GitHub release. You don't open another pull request. A scheduled job in `pulumi/registry` runs twice a day, at 05:30 and 17:30 UTC, and checks every listed package for a release newer than the one the Registry has. When it finds one it regenerates that package's metadata and documentation from the new release and opens a pull request, which a Pulumi maintainer merges. Your updated listing, documentation, and API docs go live from there.

Search works the same way. The filter box on the Registry index page matches a package by its title, its name, and its keywords, and those keywords come from the `keywords` field of your `schema.json`. To make your package findable by a new term, add the term to `keywords` and cut a release. Don't edit the generated package YAML in `pulumi/registry` by hand; the next metadata publish overwrites it.
