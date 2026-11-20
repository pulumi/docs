---
title_tag: "Dependency caching | Pulumi Deployments"
meta_desc: Speed up Pulumi Deployments by caching downloaded dependencies between runs on Pulumi-managed workflow runners
title: "Dependency caching"
h1: "Dependency caching"
menu:
  deployments:
    name: Dependency caching
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-dependency-caching
    weight: 90
---

When using Pulumi-managed workflow runners, you can speed up deployments with dependency caching. Cache entries belong to individual stacks.

Dependency caching covers more than your language packages. A cache entry bundles three things a deployment would otherwise download every run: your language dependencies (including the Pulumi SDKs, which are cached as ordinary package-manager packages), the Pulumi [resource plugins](/docs/iac/concepts/plugins/) your program uses, and any [policy packs](/docs/discovery-governance/concepts/policy-as-code/policy-packs/). In practice the plugins are usually the largest and slowest to fetch, so caching them is where most of the time savings come from.

When caching is enabled, the runner uses lock files and package-manager cache paths to calculate a cache key. Updates, refreshes, destroys (unless the stack is deleted afterward), and drift remediation can save new entries in blob storage. Later deployments of the same stack can restore those entries instead of downloading the dependencies again. Changed lock files or package-manager cache paths select a different key, which needs its own entry.

{{% notes type="info" %}}
Dependency caching is unavailable on stacks that use a [customer-managed runner pool](/docs/administration/concepts/customer-managed-runners/#not-supported-on-customer-managed-runners), because you already control the lifetime and contents of those runners.
{{% /notes %}}

## Enabling dependency caching

Dependency caching is off by default. You can enable it per stack:

- **Pulumi Cloud**: on the stack's **Settings** → **Deploy** page, turn on **Cache dependencies to speed up deployments**.
- **Deployment settings**: set `cacheOptions.enable` to `true`.
- **REST API**: set the same `cacheOptions.enable` field on the stack's [deployment settings](/docs/reference/cloud-rest-api/deployments/).

Dependency caching is not available on stacks backed by Terraform state.

Both the setting and the cache entries are scoped to a single stack, so stacks in the same project can have caching enabled and disabled independently:

- A stack with caching **disabled** runs no cache steps at all. It neither reads nor writes any cache entries.
- A stack with caching **enabled** restores its own cache entries, keyed by its lock file contents and package-manager cache paths. Operations that can save entries populate the cache.
- Identical lock files do not make one stack reuse another stack's cache. A new stack always starts cold, even when another stack in the same project deploys the same program with the same lock file.
- Disabling caching on a stack does not delete anything. [Clearing the cache](#clearing-the-cache) is a separate action that works at the project level.

Previews and drift-detection runs can restore existing entries, but they do not save new ones. To populate an entry, run an update, refresh, destroy that retains the stack, or drift remediation.

## What gets cached

For supported runtimes, the cache collects the language dependency paths below, plus the Pulumi plugin and policy directories when present. Those directories default to `~/.pulumi/plugins` and `~/.pulumi/policies`. If `PULUMI_HOME` is set, the cache uses its `plugins` and `policies` subdirectories instead. Missing directories are skipped. Language SDKs use the normal package manager cache paths rather than a separate SDK cache.

| Runtime | Detected using | Cached directories |
|---------|----------------|--------------------|
| Python (pip) | `requirements.txt` | The `venv` directory beside it, and `~/.cache/pip` |
| Python (uv) | `uv.lock` | The uv cache directory |
| Python (Poetry) | `poetry.lock` | The in-project `.venv` directory, and Poetry's cache directory |
| Node.js (npm) | `package-lock.json` | `node_modules` and the npm cache |
| Node.js (Yarn) | `yarn.lock` | `node_modules` and the Yarn cache |
| Node.js (pnpm) | `pnpm-lock.yaml` | The pnpm store (not `node_modules`) |
| .NET | `packages.lock.json`, or `.csproj`, `.fsproj`, and `.vbproj` files | `~/.nuget/packages` |
| Go | `go.sum`, falling back to `go.mod` | The module cache and the build cache |

Lock files are located by searching the deployment's working directory and then each of its parent directories, so a lock file at the root of a monorepo works even when `Pulumi.yaml` lives in a subdirectory. The .NET runtime is the exception: it searches only the working directory and below.

A few constraints are worth knowing before you turn caching on:

- **Java and YAML are not supported.** Only Python, Node.js, .NET, and Go have caching support. Enabling the setting on a Java or YAML stack is harmless but has no effect — the cache steps run, log `Skipping caching step: unsupported runtime`, and nothing is cached, including plugins.
- **Python projects must have exactly one lock file.** If more than one of `requirements.txt`, `uv.lock`, and `poetry.lock` is present, Pulumi can't tell which package manager you intend to use and skips caching entirely — including plugins. Poetry is supported natively, so do not export a `requirements.txt` alongside your `poetry.lock`.
- **For pip, the virtual environment must be named `venv`.** A virtual environment named `.venv` or `env` is not cached.
- **For Node.js**, a `packageManager` field in `package.json` determines the package manager. Without that field, Pulumi infers it from the lock file, and multiple lock files cause caching to be skipped.
- **Custom executor images must include your package manager.** Pulumi asks the package manager (`npm`, `yarn`, `pnpm`, `uv`, or `poetry`) where its cache lives, so the binary has to be on the `PATH`. If it isn't, caching is skipped. See [Deployment execution environment](/docs/deployments/guides/custom-images/).
- **Plugin and policy paths follow `PULUMI_HOME`.** If you override it, the cache captures its `plugins` and `policies` subdirectories when present. Without an override, the cache uses `~/.pulumi`. `PULUMI_HOME` is not part of the cache key, so if you change it after entries have been saved, [clear the cache](#clearing-the-cache) to capture plugins and policies at the new paths.

## Verifying and troubleshooting

To confirm caching is working, open a deployment's logs and read the **Restore cache** and **Save cache** steps. Neither step prints the words "hit" or "miss," so look for these lines instead.

In the **Restore cache** step:

| Log line | What it means |
|----------|---------------|
| `Detected project runtime: python` | Pulumi identified the runtime. |
| `Calculated cache entry with key pip-<hash>...` | Pulumi computed the cache key from your lock file and package-manager cache paths. |
| `Decompressing and extracting cache...` followed by `Cache restored successfully` | **Cache hit.** Dependencies were restored. |
| `No cache to restore, skipping...` | **Cache miss.** No entry exists for this key. This can happen on the first deployment, after only previews or drift-detection runs, when lock files or package-manager cache paths change, or after entries are cleared or evicted. |
| `Skipping caching step: <reason>` | **Nothing was cached.** The reason explains why — usually an unsupported runtime or a missing or ambiguous lock file. |

In the **Save cache** step:

| Log line | What it means |
|----------|---------------|
| `Got cache entry key <key>..., capturing paths: [...]` | The directories about to be archived. |
| `Compressed file "<key>.tar.zst", size: ...` followed by `Uploaded ... successfully` | A new cache entry was written. |
| `Key "<key>" already cached, skipping...` | Your dependencies were unchanged, so nothing was re-uploaded. This is the normal steady state. |
| `Warning: cache entry ... exceeded size limit ..., skipping...` | The archive was larger than the size limit and was not saved. |
| `Directory "<path>" not found, skipping...` | An expected directory didn't exist and was left out of the archive. |

If a deployment isn't getting faster, the most common cause is a `Skipping caching step` line in the **Restore cache** step. Read the reason it gives.

## Clearing the cache

Changed lock files or package-manager cache paths select a different cache key, so clearing the cache by hand is rarely necessary. If you need to force a cold rebuild, you can:

- **Pulumi Cloud**: use the **Clear cache** action on the stack's **Deployments** page.
- **REST API**: send `DELETE /api/stacks/{organization}/{project}/{stack}/deployments/cache`.

Both actions clear cache entries for **all stacks in the project**. Each stack must populate its own entries again.

## Limits and constraints

- Cache entries are scoped per stack. Stacks do not share entries with each other, even within the same project and with identical lock files, and caches are never shared between organizations.
- Cache archives are limited to 5 GB compressed. A larger archive is skipped with a warning rather than failing the deployment.
- **A cache failure never fails a deployment.** Every problem with caching is a warning and a skip, which is why an unexpectedly slow deployment is worth checking against the log lines above.
- Cache keys are matched exactly, with no partial or fallback key match. Changed lock files or package-manager cache paths select another key. That key produces a miss unless an entry already exists for it.
- Caches that go unread for roughly a month are evicted. A cache in regular use stays warm.
- The **Save cache** step does not run for previews or drift detection, or when a `destroy` operation deletes the stack afterward.
