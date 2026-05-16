<p align="center">
  <a href="https://www.pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=top-logo" title="Pulumi Documentation - Build and Deploy Infrastructure as Code Solutions on Any Cloud">
    <img src="https://www.pulumi.com/images/logo/logo-on-white-box.svg?" width="350">
   </a>

  [![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=slack-badge)
  [![GitHub Discussions](https://img.shields.io/github/discussions/pulumi/pulumi)](https://github.com/pulumi/pulumi/discussions)
  [![License](https://img.shields.io/github/license/pulumi/pulumi)](LICENSE)
  ![Deployment Status](https://github.com/pulumi/docs/actions/workflows/build-and-deploy.yml/badge.svg?branch=master&event=push)
  ![Examples Tests](https://github.com/pulumi/docs/actions/workflows/scheduled-test.yml/badge.svg?branch=master)

# Pulumi Documentation Site

## Table of contents

* :blue_book: [View Pulumi Docs](https://pulumi.com/docs/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-toc)
* :clap: [Contributing](#Contributing)
* :toolbox:	[Setup and Development](#setup-and-development)
  * [Generating SDK and CLI documentation](#generating-sdk-and-cli-documentation)
* :busts_in_silhouette: [Pulumi Community](#community)
* :blue_book: [Pulumi Developer Resources](#pulumi-resources)
* :compass:	[Pulumi Roadmap](#pulumi-roadmap)

## About this repository

This repository hosts all of the hand-crafted documentation, guides, tutorials, blogs, and landing pages that you see on [https://pulumi.com](https://pulumi.com?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=about-docs), as well as all of the assets and templates we use to render the Pulumi website. It also houses the documentation that we generate for the Pulumi CLI and language SDKs, and it's responsible for building and deploying the website (with Pulumi, of course!).

### What's not in this repository

* Pulumi AI: You'll find the open-source components of the Pulumi AI project at https://github.com/pulumi/pulumi-ai.
* Pulumi Registry: You'll find everything related to the Registry at https://github.com/pulumi/registry.

## Contributing

We welcome all contributions to this repository. Be sure to read our [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE-OF-CONDUCT.md) first, then [submit a pull request](https://github.com/pulumi/docs/pulls) here on GitHub. If you see something that needs fixing but don't have time to contribute, you can also [file an issue](https://github.com/pulumi/docs/issues).

> Tip: open your PR as a **draft** while you iterate. Automated review fires when you mark it ready for review, so a draft-first flow keeps the CI noise down and the review fresh. See [CONTRIBUTING.md](CONTRIBUTING.md#draft-first-pull-requests) for the full lifecycle.

See also:

* [Build and deployment guide](./BUILD-AND-DEPLOY.md)
* [Publishing a Pulumi blog post](./BLOGGING.md)
* [Documentation and coding style guide](./STYLE-GUIDE.md)
* [AI agent instructions](./AGENTS.md)

# Setup and Development

### Toolchain

The website is built with Hugo, with supporting tooling in Node.js, Yarn, Go, and Vale. There are two ways to install these locally.

#### Recommended: install Hugo, then use mise for everything else

[mise](https://mise.jdx.dev/) is a version manager that reads [`mise.toml`](./mise.toml) and installs the exact versions of Node, Yarn, Go, and Vale that CI uses. The build scripts route tool invocations through `mise exec` automatically, so you don't need to `mise activate` in your shell.

Hugo isn't managed by mise because Hugo's macOS distribution is a signed `.pkg` installer (no tarball), which mise's standard backend can't unpack. Install Hugo from your system package manager.

```bash
# 1. Install mise (one time).
brew install mise              # macOS
# or: curl https://mise.run | sh   # Linux / other

# 2. Install Hugo (one time).
brew install hugo              # macOS
# or download from https://github.com/gohugoio/hugo/releases

# 3. Install all pinned tools + project dependencies.
make ensure

# 4. Run the site locally on http://localhost:1313.
make serve
```

`make ensure` warns if your local Hugo version doesn't match the version we deploy with (0.157.0 extended), but doesn't enforce it — Hugo is generally backwards-compatible across minor releases, and the production artifact is built with the pinned version in CI.

#### Without mise

You can also install everything by hand:

* [Hugo](https://gohugo.io/installation/) 0.157.0 (extended)
* [Node.js](https://nodejs.org/en/download/package-manager) 24
* [Yarn](https://classic.yarnpkg.com/lang/en/docs/install) 1.x
* [Go](https://golang.org/) 1.26 (only needed for SDK doc builds and example-program tests)
* [Vale](https://vale.sh/docs/install) 3.14.1 (only needed for `make lint-prose`)

`make ensure` and `make serve` work the same way — version mismatches warn rather than fail.

#### SDK and CLI documentation

To also build the SDK and CLI documentation, you'll need a few more tools:

* [Python](https://www.python.org) (>= 3.7)
* [.NET](https://dotnet.microsoft.com/download) (>= 6)
* [Pulumi](https://www.pulumi.com/docs/install)
* [Pulumi ESC](https://www.pulumi.com/docs/install/esc)

#### Dev Container

This repository includes a dev container configuration that provides a fully pre-configured environment with all the tools you need for developing and contributing to the Pulumi documentation. Using the dev container eliminates the need to install dependencies manually, as it comes with:

* Hugo, Node.js, Yarn, and Markdown tooling.
* Vale for prose linting.
* Go, Python, .NET, and the Pulumi CLI.
* VS Code extensions for Markdown linting, link checking, and Pulumi support.
* Google Cloud CLI and GitHub CLI.

To use the dev container:

1. Install [Docker](https://www.docker.com) (or another compatible container engine), [VS Code](https://code.visualstudio.com/), and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
1. Clone this repository
1. Open the repository in VS Code
1. When prompted, click "Reopen in Container" or run the "Dev Containers: Reopen in Container" command from the Command Palette

The `.vscode` directory is preconfigured with launch and build tasks. When using default keybindings, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> to build the site, and <kbd>F5</kbd> to launch the server locally. All of the `make` commands can be listed in the UI pressing <kbd>F1</kbd> and selecting **Tasks: Run Task**.

For more information on dev containers, see the [VS Code Dev Containers documentation](https://code.visualstudio.com/docs/devcontainers/containers).

### Repository layout

* **Documentation and page content**: We generally follow Hugo's [directory-structure conventions](https://gohugo.io/getting-started/directory-structure/), with Markdown files in `./content`, layout files (including partials and shortcodes) in `./layout`, and data files in `./data`. There are also several [Hugo templates](https://gohugo.io/content-management/archetypes/) available in `./archetypes` for bootstrapping common content types like blog posts and Learn modules.

* **CSS and JavaScript**: We build our CSS and JavaScript bundles separately from Hugo and check in the built artifacts at `./assets`. We use [Tailwind](https://tailwindcss.com/) for CSS, [Stencil](https://stenciljs.com/) for web components, and [jQuery](https://jquery.com/) for wiring things together in general. Source files for these are in `./theme`.

* **Examples**: Many of the examples we include in our documentation are maintained as full Pulumi programs and tested daily. You'll find them all at `./static/programs`.

* **Infrastructure**: We deploy the website as a statically built artifact to a unique Amazon S3 bucket on every commit to the base branch of this repo. The Pulumi program that handles this is located in `./infrastructure`. This is also where you'll find the CloudFront configuration that handles proxying [Pulumi Neo](https://pulumi.com/product/neo/) and the [Pulumi Registry](https://pulumi.com/registry).

### Using the Makefile

The `Makefile` exposes a number of useful helpers for authoring:

* `make ensure` resolves and installs all dependencies
* `make lint` checks all Markdown files for correctness
* `make format` formats all applicable files to ensure they conform to style guidelines
* `make serve` runs the Hugo server locally at <http://localhost:1313> and watches for changes. You can set `BUILD_FUTURE=false` to simulate production behavior by excluding future-dated content (e.g., `BUILD_FUTURE=false make serve`). Note: Hugo's dev server does not serve content from `static-prebuilt/`, so generated SDK reference pages under `/docs/reference/pkg/{nodejs,python,dotnet,java}/...` will 404 in dev mode — use `make build && make serve-static` to preview those.
* `make serve-all` does the same as `make serve`, but also watches for changes to CSS and JS source files
* `make build` generates the website and writes it to `./public`. This includes copying `static-prebuilt/` (where the auto-generated SDK reference docs live) into the output, which is why this combined with `make serve-static` is the way to preview SDK pages locally.
* `make build-assets` builds only the CSS and JavaScript asset bundles
* `make serve-static` runs a local HTTP server that serves the contents of `./public` — use this after `make build` when you need to verify SDK reference pages or anything else served out of `static-prebuilt/`
* `make test` tests all of the programs in `./static/programs` (see `./scripts/programs/test.sh` for options)
* `make new-tutorial` scaffolds a new single-page tutorial
* `make new-tutorial-module` scaffolds a new multi-page tutorial
* `make new-tutorial-topic` scaffolds a new tutorial topic and adds it to an existing multi-page tutorial
* `make new-example-program` generates a new multi-language set of examples at `./static/programs`
* `make new-dev-stack` creates a new dev stack (in the `pulumi` organization, which you must belong to)
* `make deploy-dev-stack` runs a build, deploys to S3, runs the tests, and deploys to the selected dev stack

As a content contributor, the commands you'll use most often are these:

```bash
make ensure    # Install or update dependencies.
make serve     # Run the development server locally on http://localhost:1313.
make lint      # Identify any Markdown or code-formatting issues so you can fix them.
```

### Claude Commands

If you have [Claude Code](https://claude.com/claude-code) installed, you can use specialized slash commands to streamline your documentation workflow. These commands provide intelligent assistance with context awareness, interactive prompts, and automatic configuration.

To see all available commands, run:

```
/docs-tools
```

This will display the complete list of documentation tools and commands with descriptions, including commands for content creation, review and approval, content improvement, and issue resolution.

> Note: While these skills are built for Claude Code, they also work with other AI agents! GitHub Copilot can execute them with the slash prefix (e.g., `/docs-tools`), while Codex works without the slash (e.g., `docs-tools`).

## Generating SDK and CLI documentation

We generate reference documentation in two surfaces — language-specific SDK docs and command-line tool docs — and check the output into this repository. In normal operation each one is regenerated automatically by a dedicated GitHub Actions workflow whenever its upstream source repo cuts a release; you only need to regenerate manually when you're modifying a generator script or investigating a regression.

### What gets generated and by which workflow

| Surface | Source repo | Workflow file | Output |
|---|---|---|---|
| Pulumi CLI commands | `pulumi/pulumi` | [`pulumi-cli-docs.yml`](.github/workflows/pulumi-cli-docs.yml) | `content/docs/iac/cli/commands/` |
| Pulumi ESC CLI commands | `pulumi/esc` | [`esc-cli.yml`](.github/workflows/esc-cli.yml) | `content/docs/esc/cli/commands/` |
| Pulumi SDK — TypeScript | `pulumi/pulumi` | [`pulumi-sdk-typescript-docs.yml`](.github/workflows/pulumi-sdk-typescript-docs.yml) | `static-prebuilt/docs/reference/pkg/nodejs/pulumi/` |
| Pulumi SDK — Python | `pulumi/pulumi` | [`pulumi-sdk-python-docs.yml`](.github/workflows/pulumi-sdk-python-docs.yml) | `static-prebuilt/docs/reference/pkg/python/pulumi/` |
| Pulumi SDK — .NET | `pulumi/pulumi-dotnet` | [`pulumi-sdk-dotnet-docs.yml`](.github/workflows/pulumi-sdk-dotnet-docs.yml) | `static-prebuilt/docs/reference/pkg/dotnet/` |
| Pulumi SDK — Java | `pulumi/pulumi-java` | [`pulumi-sdk-java-docs.yml`](.github/workflows/pulumi-sdk-java-docs.yml) | `static-prebuilt/docs/reference/pkg/jvm/` |
| Pulumi Policy SDK — Python | `pulumi/pulumi-policy`* | [`pulumi-policy-sdk-python-docs.yml`](.github/workflows/pulumi-policy-sdk-python-docs.yml) | `static-prebuilt/docs/reference/pkg/python/pulumi_policy/` |
| Pulumi ESC SDK — Python | `pulumi/esc-sdk`* | [`pulumi-esc-sdk-python-docs.yml`](.github/workflows/pulumi-esc-sdk-python-docs.yml) | `static-prebuilt/docs/reference/pkg/python/pulumi_esc_sdk/` |

(\*) These two workflows are `workflow_dispatch`-only today; an upstream `repository_dispatch` from the source repo is a planned follow-up.

(Go SDK docs aren't generated here — they're hosted at [pkg.go.dev](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi) directly from `pulumi/pulumi`.)

### Two ways to regenerate

#### Option A — Trigger the GitHub Actions workflow (recommended)

For the CLI and the Pulumi-SDK workflows (TypeScript, Python, .NET, Java), the canonical way to regenerate is to fire the workflow from your terminal. The workflow installs the right toolchains, runs the generator, opens a PR, and (because of the `automation/merge` label) auto-merges it once CI passes.

```bash
# Pulumi SDK - Python at the currently-released CLI version
gh workflow run pulumi-sdk-python-docs.yml --repo pulumi/docs --ref master -f version=3.238.0

# Pulumi SDK - TypeScript
gh workflow run pulumi-sdk-typescript-docs.yml --repo pulumi/docs --ref master -f version=3.238.0

# Pulumi SDK - .NET
gh workflow run pulumi-sdk-dotnet-docs.yml --repo pulumi/docs --ref master -f version=<dotnet-version>

# Pulumi SDK - Java
gh workflow run pulumi-sdk-java-docs.yml --repo pulumi/docs --ref master -f version=<java-version>

# Pulumi Policy SDK / Pulumi ESC SDK - Python
gh workflow run pulumi-policy-sdk-python-docs.yml --repo pulumi/docs --ref master -f version=<policy-version>
gh workflow run pulumi-esc-sdk-python-docs.yml   --repo pulumi/docs --ref master -f version=<esc-sdk-version>

# Pulumi CLI markdown
gh workflow run pulumi-cli-docs.yml --repo pulumi/docs --ref master -f version=3.238.0
```

> ⚠️ **Don't run these against non-current versions under normal circumstances.** The generated PR carries `automation/merge` and auto-merges as soon as CI passes, which means firing a workflow against an older version will roll back the docs on master. For an exploratory regen against a non-current version, immediately strip `automation/merge` from the generated PR and disable auto-merge (`gh pr merge <N> --disable-auto`) before CI completes, or close the PR.

#### Option B — Run the generator locally

Useful when you're modifying a generator script (e.g. `scripts/run_typedoc.sh`, `scripts/generate_python_docs.sh`) and want to inspect the output without round-tripping through CI.

```bash
make ensure         # Install dependencies (one-time).
make update-repos   # Clone sibling pulumi/pulumi (etc.) repos — needed for the TypeScript build.

# TypeScript: pulumi package only
NOBUILD=true PKGS=pulumi ./scripts/run_typedoc.sh

# Python: pick one package per invocation. Valid PACKAGE values: pulumi, pulumi_policy, pulumi_esc_sdk.
PACKAGE=pulumi          ./scripts/generate_python_docs.sh
PACKAGE=pulumi_policy   ./scripts/generate_python_docs.sh
PACKAGE=pulumi_esc_sdk  ./scripts/generate_python_docs.sh

# .NET (requires `dotnet` and the `docfx` global tool on PATH)
dotnet tool install -g docfx    # one-time
./scripts/run_docfx.sh

# Java (requires Java 17 + Gradle; see pulumi-sdk-java-docs.yml for details)
JAVA_REPO=../pulumi-java ./scripts/gen_javadoc.sh

# Pulumi CLI markdown — uses the currently-installed `pulumi` binary, so install
# the version you're documenting before running.
PULUMI_EXPERIMENTAL=true pulumi gen-markdown ./content/docs/iac/cli/commands

# Pulumi ESC CLI markdown
esc gen-docs ./content/docs/esc/cli/commands
```

The generated content lands in the output paths from the table above. Preview locally with:

```bash
make build           # Build the website, copying all generated docs into place.
make serve-static    # Serve the built site on http://localhost:8080.
```

With `make serve-static` running, browse to <http://localhost:8080/docs>:

* Choose **Languages & SDKs** → your language → scroll to the package you're interested in.
* Choose **Pulumi CLI** or **Pulumi ESC CLI** → **Commands**.

### Checking in generated docs

All generated docs (CLI markdown + Node.js, Python, .NET, Java SDK reference) are checked into this repository. In normal operation the workflows above create the commits and PRs automatically; you don't need to commit generated output yourself.

## Search

We use [Algolia](https://www.algolia.com/) for search, and we update the Algolia search index [on every deployment](https://github.com/pulumi/docs/blob/master/scripts/ci-push.sh#L13) of the website. Whether you're adding a new page or updating an existing one, your changes will be reflected in search results within a few seconds of release.

### Creating findable content

We currently index every page of the website, including the blog and the Registry. However, we do not index all of the content of every page &mdash; we only index certain properties of the page. These include:

* Page titles (specifically the `title` and `h1` frontmatter params)
* Page descriptions (specifically the `meta_desc` param)
* Second-level headings (e.g., those prefixed with `##` in Markdown files)
* Keywords, if any (via the `search.keywords` param)
* Authors, if any (via the `authors` param)
* Tags, if any (via the `tags` param)

Because of this, it's important to be thoughtful about the terms you use for these fields, especially titles, keywords, descriptions, and H2 headings. If you want your content to be findable by specific terms, you must make sure those terms exist in one or more of the fields listed above.

For example, if you were writing a guide to building an ETL pipeline with Redshift, and you wanted to make sure the page would be surfaced for queries like `redshift data warehouse etl`, you might construct the page's frontmatter in the following way:

```yaml
title: Build an ETL pipeline with Redshift and AWS Glue
meta_desc: Learn how to combine AWS Glue and Amazon Redshift to build a fully-automated ETL pipeline with Pulumi.
search:
    keywords:
        - data warehouse
```

In this case, the optional `search.keywords` field is included to cover the terms `data warehouse`, as those terms don't exist in the page's title or description. If it weren't, queries for `data warehouse` would fail to match this particular page.

Certain fields also rank higher than others in terms of their overall relevance. (Titles and keywords, for example, are considered more relevant than descriptions.) For a full list of these rankings, along with all of the rules we apply to the search index, see the [search app in pulumi/docs](https://github.com/pulumi/docs/blob/master/scripts/search/settings.js).

### Keeping pages out of search results

To keep a page from showing up in search results (including on Google, etc.), use the `block_external_search_index` frontmatter parameter:

```yaml
title: My page
...
block_external_search_index: true
```

## Community

Engage with our community to elevate your developer experience:

* **Join our online [Pulumi Community on Slack](https://slack.pulumi.com/?utm_campaign=pulumi-docs-repo&utm_source=github.com&utm_medium=welcome-slack)** - Interact with thousands of Pulumi developers for collaborative problem-solving and knowledge-sharing!
* **Join a [Local Pulumi User Groups (PUGs)](https://www.meetup.com/pro/pugs/)** - Attend tech-packed meetups and hands-on virtual or in-person workshops.
* **Follow [@PulumiCorp](https://twitter.com/PulumiCorp) on X (Twitter)** - Get real-time updates, technical insights, and sneak peeks into the latest features.
* **Subscribe to our YouTube Channel, [PulumiTV](https://www.youtube.com/@PulumiTV)** - Learn about AI / ML essentials, launches, workshops, demos and more.
* **Follow our [LinkedIn](https://www.linkedin.com/company/pulumi/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-community)** - Uncover company news, achievements, and behind-the-scenes glimpses.

## Pulumi developer resources

Delve deeper into Pulumi with additional resources:

* [Get Started with Pulumi](https://www.pulumi.com/docs/get-started/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources): Deploy a simple application in AWS, Azure, Google Cloud, or Kubernetes using Pulumi.
* [Registry](https://www.pulumi.com/registry/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources): Search for packages and learn about the supported resources you need. Install the package directly into your project, browse the API documentation, and start building.
* [Pulumi Blog](https://www.pulumi.com/blog/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources) - Stay in the loop with our latest tech announcements, insightful articles, and updates.
* [Try Pulumi Neo](https://www.pulumi.com/product/neo/?utm_campaign=pulumi-docs-github-repo&utm_source=github.com&utm_medium=docs-resources) - Use natural-language prompts to generate Pulumi infrastructure-as-code programs in any language.

## Pulumi roadmap

Review the planned work for the upcoming quarter and a selected backlog of issues that are on our mind but not yet scheduled on the [Pulumi Roadmap.](https://github.com/orgs/pulumi/projects/44)
