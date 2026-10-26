# Self-hosted feature parity

This directory configures the generator for the self-hosted feature parity page, `content/docs/administration/self-hosting/feature-parity.md`, and its internal companion table. Both are built from the feature definitions in the private `pulumi-service` repository, so only people with access to it can regenerate them. Without a clone, `make generate-feature-parity` skips generation and leaves the existing page alone.

## Generating

Like the SDK and CLI doc generators, this reads a sibling clone of its source repo. `make update-repos` clones or updates `pulumi-service` next to this repo along with the others. Unlike them, `pulumi-service` stays on its default branch rather than a release tag, so the table tracks what's merged. To update only that clone:

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

`--full-report` prints a quick availability comparison to stdout for debugging. It skips the dependency and metadata logic, so use the internal summary for actual status.

Everything in `generated/` is gitignored because it contains internal information. Copy the internal summary to the internal Notion page by hand after regenerating.

## How status is decided

Status follows how the service evaluates a feature on self-hosted:

1. `SelfHosted.Available` in `features.go`. If it's `false`, the feature is `N`.
1. The license toggle, falling back to `SelfHosted.Default`. Available but off by default is `Y (has toggle)`; on by default is `Y`.
1. Dependencies, from `featureDependencies` in `features.go` plus `depends_on` in `feature-metadata.json`. A feature whose dependency is unavailable is left out, because the dependency's own row covers it. A dependency that needs a license toggle makes the feature `Y (has toggle)`.
1. Direct LaunchDarkly checks. LaunchDarkly flags attached to `features.go` entries only matter on Pulumi Cloud, but code can also check a flag directly. Self-hosted can't reach LaunchDarkly, so those checks return the default written at the call site. A `false` default turns the behavior off whatever the license says, so the feature is `N`.

Anything no flag controls runs the same code on self-hosted as on Pulumi Cloud, so it isn't listed. The public page says so. Some of those features still need installation configuration; list them as hand-maintained rows (see below) when that's worth calling out.

### Direct LaunchDarkly checks

The generator parses `pulumi-service` for calls that read a LaunchDarkly flag, including the service-wide helpers in `featureflag/flags.go`, `featureflags.Enabled` and its variants from `pkg/featureflags`, and flags passed as plain strings, and records each default. A default of `IsSelfHostedEnterprise()` counts as `true`, because that's what it returns on self-hosted. The raw report lists every check with its default, whether it's on or off on self-hosted, the row it affects, and where it's called.

- A flag already attached to a `features.go` entry marks that entry `N` when a check defaults to `false`.
- Any other flag needs an entry in `feature-metadata.json`, keyed by its `LDKey...` constant (or the flag string if there's no constant). Give it a `marketing_name` to show it as its own row, add it to another entry's `feature_keys` to make that row `N` (as Dependency Caching and Terraform Module Registry do), or set `include_in_table: false` for operational and rollout flags.
- New flags show as **Not mapped** in the raw report until someone classifies them.

## Configuration

### `feature-metadata.json`

Controls the internal summary. Entries are keyed by feature key (`PulumiFeature...`), LaunchDarkly key (`LDKey...`), or any name for grouped and hand-maintained entries. A feature with no entry appears under its `FriendlyName` from `features.go`.

| Field | Description |
| :---- | :---- |
| `marketing_name` | Row name. Entries with the same name are combined into one row. |
| `feature_keys` | Combines several flags into one row. The first key is used to find the row's history. The row is `N` only if all are unavailable, or if any is turned off by a direct LaunchDarkly check. |
| `include_in_table` | `false` hides the row. Defaults to `true`. |
| `depends_on` | Dependencies that `features.go` doesn't declare, such as Neo sub-features on `PulumiFeatureAIAgents`. |
| `status` | Overrides the computed status, such as `Y (needs config)` for features that work once the installation is configured. |
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

Controls the public page. Entries are keyed by `marketing_name`. A row with no entry is published, so add `"publish": false` for every internal-only row.

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
