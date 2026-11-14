# Self-hosted feature parity

This directory configures the generator for the self-hosted feature parity page, `content/docs/administration/self-hosting/feature-parity.md`, and its internal companion table. Both are built from the feature definitions in the private `pulumi-service` repository, so only people with access to it can regenerate them. The feature metadata that maps flags to rows lives there too, in `cmd/service/api/features/self-hosted-parity.json`, because it names internal flags and unreleased features. This repo only keeps the configuration for the public rows. Without a clone, `make generate-feature-parity` skips generation and leaves the existing page alone.

## Generating

Like the SDK and CLI doc generators, this reads a sibling clone of its source repo. Unlike them, `pulumi-service` isn't part of `make update-repos`, because it's private and is often a clone you work in. Locally it stays on its default branch, so the table tracks what's merged; the nightly workflow reads `production` instead (see [In CI](#in-ci)), so to match the published page, check out `production` in your clone. To clone it, or to update a clean clone that's on its default branch (anything else is left alone):

```bash
./scripts/update_repos.sh pulumi-service
```

Then regenerate everything:

```bash
make generate-feature-parity
```

To use a clone somewhere else, set `PULUMI_SERVICE_REPO`, the same way `JAVA_REPO` points `gen_javadoc.sh` at a `pulumi-java` checkout:

```bash
PULUMI_SERVICE_REPO=/path/to/pulumi-service make generate-feature-parity
```

`make generate-feature-parity` runs `go run scripts/update-feature-parity.go --all`, which runs each step below in order. If there's no `pulumi-service` clone, `--all` skips generation and leaves the existing page alone. To run a single step, pass its flag instead of `--all`, from the repo root:

| Step | Flag | Output |
| :---- | :---- | :---- |
| Raw data | `--generate-raw` | `generated/feature-detection-raw.md`: every feature in `features.go` with its license settings, preconditions, dependencies, and LaunchDarkly flag, plus every direct LaunchDarkly check |
| Internal summary | `--update-summary` | `generated/feature-parity-internal.md`: one row per feature with status, ETA, and summary |
| History | `--enrich` | Adds a History column to the internal summary with the PR that introduced each feature. Needs the `gh` CLI, and is skipped if `gh` isn't installed |
| Public page | `--publish` | `content/docs/administration/self-hosting/feature-parity.md` |

The generator fails rather than write a partial page: when the metadata or a LaunchDarkly source file is missing, when it finds no features or no flag helpers, when any Go file in `pulumi-service` fails to parse, or when a published row no longer comes out of the metadata. Parsing needs the Go toolchain `pulumi-service` uses, so `make generate-feature-parity` sets `GOTOOLCHAIN` from its `go.mod`.

`--full-report` prints a quick availability comparison to stdout for debugging. It skips the dependency and metadata logic, so use the internal summary for actual status.

Everything in `generated/` is gitignored because it contains internal information. Copy the internal summary to the internal Notion page by hand after regenerating.

### In CI

The [Self-hosted feature parity](../../.github/workflows/self-hosted-feature-parity.yml) workflow regenerates the page nightly and on demand, the same way the CLI and SDK docs workflows do: it checks out `pulumi-service` with pulumi-bot's token, runs the raw, internal summary, and public page steps, and opens a PR when the page changes, listing each status change. Like those workflows, the PR auto-merges, with one exception: the page's statuses are computed but its Details are hand-written, so when a row with Details changes status, `status-changes.py` flags it and the PR waits for someone to check the Details still match (and fix `public_notes` if they don't). A manual run against another branch never auto-merges either. Because this repo's workflow logs are public, it doesn't run `--enrich` or `--full-report`, and it never uploads `generated/`. It reads `pulumi-service`'s `production` branch, which is what `pulumi/service:latest` and the dated Docker Hub tags are built from, so the page matches what customers can install; `master` only becomes the `edge` images. To regenerate from another branch, run it by hand with the `pulumi_service_branch` input; it takes branch names only.

## How status is decided

Status follows how the service evaluates a feature on self-hosted:

1. `SelfHosted.Available` in `features.go`. If it's `false`, the feature is `N`.
1. The license toggle, falling back to `SelfHosted.Default`. Available but off by default is `Y (has toggle)`; on by default is `Y`.
1. Dependencies, from `featureDependencies` in `features.go` plus `depends_on` in `self-hosted-parity.json`. A feature whose dependency is unavailable is left out, because the dependency's own row covers it. A dependency that needs a license toggle makes the feature `Y (has toggle)`.
1. Direct LaunchDarkly checks. LaunchDarkly flags attached to `features.go` entries only matter on Pulumi Cloud, but code can also check a flag directly. Self-hosted can't reach LaunchDarkly, so those checks return the default written at the call site. A `false` default turns the behavior off whatever the license says, so the feature is `N`.

Anything no flag controls runs the same code on self-hosted as on Pulumi Cloud, so it isn't listed. The public page shows only the rows chosen in `feature-publish-config.json` and says it isn't a complete list. Some of those features still need installation configuration; list them as hand-maintained rows (see below) when that's worth calling out.

### Direct LaunchDarkly checks

The generator parses `pulumi-service` for calls that read a LaunchDarkly flag, including the service-wide helpers in `featureflag/flags.go`, `featureflags.Enabled` and its variants from `pkg/featureflags`, and flags passed as plain strings, and records each default. A default of `IsSelfHostedEnterprise()` counts as `true`, because that's what it returns on self-hosted. The raw report lists every check with its default, whether it's on or off on self-hosted, the row it affects, and where it's called.

- A flag already attached to a `features.go` entry marks that entry `N` when a check defaults to `false`.
- Any other flag needs an entry in `self-hosted-parity.json`, keyed by its `LDKey...` constant (or the flag string if there's no constant). Give it a `marketing_name` to show it as its own row, add it to another entry's `feature_keys` to make that row `N` (as Dependency Caching and Terraform Module Registry do), or set `include_in_table: false` for operational and rollout flags.
- New flags show as **Not mapped** in the raw report until someone classifies them.

## Configuration

### `self-hosted-parity.json` (in pulumi-service)

Controls the internal summary. Entries are keyed by feature key (`PulumiFeature...`), LaunchDarkly key (`LDKey...`), or any name for grouped and hand-maintained entries. A feature with no entry appears under its `FriendlyName` from `features.go`.

| Field | Description |
| :---- | :---- |
| `marketing_name` | Row name. Entries with the same name are combined into one row. |
| `feature_keys` | Combines several flags into one row. The first key is used to find the row's history. The row is `N` only if all are unavailable, or if any is turned off by a direct LaunchDarkly check. |
| `include_in_table` | `false` hides the row. Defaults to `true`. |
| `depends_on` | Dependencies that `features.go` doesn't declare, such as Neo sub-features on `PulumiFeatureAIAgents`. |
| `status` | Overrides the computed status, such as `Y (needs config)` for features that work once the installation is configured. A computed `N` always wins, so an override can't hide a feature the code turns off. |
| `summary` | Internal description for the Summary column. |
| `default_eta` | ETA for a new row. ETAs already in the generated internal summary are kept on regeneration. |
| `notes` | Internal notes. Used as the ETA for rows that aren't `Y` and have no ETA. |
| `gate` | Makes a hand-maintained row for a capability no flag controls. Describes what controls it, such as `none (configuration only)`. Set `status` and `summary` alongside it. |

Example of a combined row:

```json
"Deployments": {
  "marketing_name": "Deployments",
  "feature_keys": ["PulumiFeatureDeployments", "PulumiFeatureSelfHostedDeployments"],
  "status": "Y (needs config)",
  "summary": "Runs on customer-managed workflow agents registered to an agent pool."
}
```

### `feature-publish-config.json`

Controls the public page. Entries are keyed by `marketing_name`. Only rows listed here with `"publish": true` appear on the public page, so a new feature stays off it until someone adds it. List only public rows: this file is in a public repo, so leave internal and unreleased features out entirely rather than listing them as hidden.

| Field | Description |
| :---- | :---- |
| `publish` | Whether the row appears on the public page. |
| `public_name` | Name shown on the public page, if different from `marketing_name`. Use current product names from the brand guide. |
| `docs_url` | Docs page that explains the feature. The name links to it. |
| `public_notes` | Short explanation for the Details column, such as setup the feature needs. |

The public page shows these statuses:

| Internal status | Public status |
| :---- | :---- |
| `Y` | Available |
| `Y (has toggle)` | Requires enablement |
| `Y (needs config)` | Requires configuration |
| `N` | Not available |

The page's front matter, intro, and status key are written by `generatePublicContent` in `scripts/update-feature-parity.go`. Edit them there, not in the generated page.
