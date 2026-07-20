---
title_tag: "Dependency Caching | Pulumi Deployments"
meta_desc: Speed up Pulumi Deployments by caching downloaded dependencies between runs on Pulumi-managed workflow runners
title: "Dependency Caching"
h1: "Dependency Caching"
menu:
  deployments:
    name: Dependency Caching
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-dependency-caching
    weight: 90
---

When using Pulumi-managed workflow runners, you can speed up deployments with dependency caching.

Dependency caching covers more than your language packages. A cache entry bundles three things a deployment would otherwise download every run: your language dependencies (including the Pulumi SDKs, which are cached as ordinary package-manager packages), the Pulumi [resource plugins](/docs/iac/concepts/plugins/) your program uses, and any [policy packs](/docs/insights/policy/policy-packs/). In practice the plugins are usually the largest and slowest to fetch, so caching them is where most of the time savings come from.

The mechanism is straightforward. On the first deployment, the runner detects these items — using your lock files for the language dependencies — archives them, and stores the archive in blob storage. On later deployments, the runner pulls that archive down and unpacks it, saving the time it would otherwise spend downloading everything again. When your dependencies change, the runner invalidates the old cache and creates a new one.

{{% notes type="info" %}}
Dependency caching is unavailable on stacks that use a [customer-managed runner pool](/docs/deployments/concepts/customer-managed-runners/#dependency-caching), because you already control the lifetime and contents of those runners.
{{% /notes %}}

## Enabling dependency caching

Dependency caching is off by default. You can enable it per stack:

- **Pulumi Cloud**: on the stack's **Settings** → **Deploy** page, turn on **Enable dependency caching**.
- **Deployment settings**: set `cacheOptions.enable` to `true`.
- **REST API**: set the same `cacheOptions.enable` field on the stack's [deployment settings](/docs/reference/cloud-rest-api/deployments/).

Dependency caching is not available on stacks backed by Terraform state.

Because caching is a per-stack setting but the cache itself is shared across the project, stacks in the same project can have it enabled and disabled independently:

- A stack with caching **disabled** runs no cache steps at all. It neither reads from nor writes to the project's cache, so it can't benefit from it and can't disturb it.
- A stack with caching **enabled** reads and writes the shared project cache, keyed by the contents of its lock files.
- Two caching-enabled stacks with identical lock files share the same cache entries and warm the cache for each other.
- Disabling caching on a stack does not delete anything. [Clearing the cache](#clearing-the-cache) is a separate, project-wide action.

## What gets cached

In addition to the dependencies below, every cache entry includes the downloaded Pulumi plugins (`~/.pulumi/plugins`) and policy packs (`~/.pulumi/policies`). Language SDKs are not handled specially — they are cached as part of your normal package manager dependencies.

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
- **Overriding `PULUMI_HOME` disables plugin caching.** The plugin and policy paths are fixed at `~/.pulumi`, so if you point `PULUMI_HOME` elsewhere with a custom environment variable, those directories are not cached. Your language dependencies are still cached.

## Verifying and troubleshooting

To confirm caching is working, open a deployment's logs and read the **Restore cache** and **Save cache** steps. Neither step prints the words "hit" or "miss," so look for these lines instead.

In the **Restore cache** step:

| Log line | What it means |
|----------|---------------|
| `Detected project runtime: python` | Pulumi identified the runtime. |
| `Calculated cache entry with key pip-<hash>...` | Pulumi computed the cache key from your lock file. |
| `Decompressing and extracting cache...` followed by `Cache restored successfully` | **Cache hit.** Dependencies were restored. |
| `No cache to restore, skipping...` | **Cache miss.** Either this is the first deployment, or your lock file changed. |
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

Pulumi invalidates the cache automatically whenever your lock files change, so clearing it by hand is rarely necessary. If you need to force a cold rebuild, you can:

- **Pulumi Cloud**: use the **Clear cache** action on the stack's **Deployments** page.
- **REST API**: send `DELETE /api/stacks/{organization}/{project}/{stack}/deployments/cache`.

Both clear the cache for the **entire project**, not just the selected stack. Every stack in the project will rebuild its cache on its next deployment.

## Limits and constraints

- Caches are shared at the project level, so all stacks within a project can share the same cache. Caches are fully isolated and never shared between organizations.
- Cache archives are limited to 5 GB compressed. A larger archive is skipped with a warning rather than failing the deployment.
- **A cache failure never fails a deployment.** Every problem with caching is a warning and a skip, which is why an unexpectedly slow deployment is worth checking against the log lines above.
- Cache keys are matched exactly. Unlike some CI systems, there is no partial or fallback key match, so any change to a lock file produces a completely cold cache.
- Caches that go unread for roughly a month are evicted. A cache in regular use stays warm.
- The **Save cache** step does not run when a `destroy` operation is configured to delete the stack afterward.
