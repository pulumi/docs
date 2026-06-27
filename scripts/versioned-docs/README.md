# Versioned SDK & CLI docs

Immutable, write-once snapshots of each SDK and CLI docset, published to a permanent S3
bucket on every release and served through the existing CloudFront distribution under
`/docs/versioned/{tool}/{version}/`. Historical versions never enter git, Hugo, or the
per-deploy origin sync, so there is **no impact on site build/deploy time**.

## How it fits together

- **Storage** — `infrastructure/versioned-docs/` (stacks `testing`, `production`) owns the
  permanent bucket `pulumi-docs-versioned-{env}` (S3 website hosting, versioning, public-read
  GetObject only, `protect`) and the GitHub-OIDC role `versioned-docs-publisher-{env}`
  (trust scoped to `repo:pulumi/docs:*`). Exports: `bucketName`, `bucketArn`,
  `bucketWebsiteEndpoint`, `publisherRoleArn`.
- **Serving** — the main stack (`infrastructure/index.ts`) adds, behind the optional
  `versionedDocsStack` config, one origin + one `/docs/versioned/*` behavior (ordered ahead
  of the dotnet and `/docs/*` behaviors) + a cache policy that honors each object's origin
  `Cache-Control` + a pass-through response-headers policy (so the global `max-age=60`
  override does **not** clobber immutable archives).
- **Per-tool manifest** — `docs/versioned/{tool}/versions.json` (`Cache-Control: max-age=300`)
  lists versions; archive content is `max-age=31536000, immutable`.
- **Selector UI** — the evergreen loader `/js/versioned-docs.js` (+ `.css`) renders the
  banner/dropdown on archived pages and (via `layouts/partials/docs/cli-command-banner.html`)
  on live CLI pages. All styling lives in those two files, so the chrome can be restyled
  **without republishing archives**. The loader fails silent when no manifest exists.
- **CLI archive theme** — CLI snapshots are Hugo-rendered site pages, so they need the site
  CSS. Rather than vendoring a frozen per-version copy, every CLI archive references one
  shared, permanent contract URL `/css/versioned-docs-archive.css`, re-derived from the docs
  CSS bundle on every site build (`scripts/build-site.sh`). Updating that one file re-themes
  the **entire** CLI back-catalog at once. The heavy site JS is dropped from snapshots (the
  nav is trimmed to a static list), so archives carry no fingerprinted `/js/` that would rot.

## Scripts

| script | purpose |
|---|---|
| `inject-version-switcher.sh` | Insert loader + (archive mode) noindex/canonical into generated HTML; strips any pre-existing canonical/robots. |
| `publish-version.sh` | Refuse-overwrite, inject, sync immutable, manifest read-modify-write, invalidate. |
| `snapshot-cli-docs.sh` | Turn a built `public/docs/iac/cli/commands/` into a snapshot (point css at the shared `/css/versioned-docs-archive.css` theme bundle, drop the site js, trim the nav, rewrite intra-links) and publish. `--out-dir DIR` writes the finished snapshot locally instead of publishing (dry run). |
| `redact-version.sh` | Delete a version's objects (all S3 versions) + drop it from the manifest + invalidate. |
| `assert-head-tag.sh` | CI guard: every generated page has a `</head>`/`</body>` injection point. |

## Runbooks

### Enable auto-publish on releases
There is **no enable flag** — auto-publish turns itself on when the env's versioned-docs
**storage stack exists**. Each release workflow's "Resolve publish target" step reads the
bucket + publisher role from `pulumi/pulumi-docs-versioned/<env>` and the CloudFront
distribution id from `pulumi/www.pulumi.com/www-<env>`, all via `pulumi stack output` (no
hardcoded ids, nothing to set by hand). If the storage stack isn't stood up the bucket output
is empty and every publish step no-ops; the moment you `pulumi up` the storage stack, releases
start archiving. If the distribution id can't be read the publish still succeeds and just skips
the invalidation (staleness bounded by the manifest's 300s TTL). `target_env` defaults to
`production`.

### Manually publish / test a single version
Dispatch the relevant workflow with the `version` and `target_env` (`testing` or `production`);
add `publish_only=true` to skip the latest-docs PR (backfill style). Publishing is automatic
when that env's storage stack exists — there is no `publish_versioned` toggle. The CLI workflow
runs a full `make build` first; SDK workflows publish their already-generated
`static-prebuilt/...` output.

### Redact a version
```
AWS_PROFILE=<env> scripts/versioned-docs/redact-version.sh \
  --tool <tool> --version vX.Y.Z --bucket pulumi-docs-versioned-<env> \
  --distribution-id <dist-id> --yes
```

### Backfill historical major/minor versions
Prereqs already in place: `update_repos.sh <repo> <tag>` honors a requested tag, and
`generate_python_docs.sh` pins the primary package when `VERSION` is set. Loop the relevant
workflow's `workflow_dispatch` over each qualifying tag (skip patches). Old toolchains that
fail to build are skipped, not fixed.

### Restyle the selector / banner
Edit `static/js/versioned-docs.js` / `.css` and redeploy the site. **Never move** the
`/js/versioned-docs.js` URL — archived pages reference it forever.

## Production setup checklist (not yet done)
1. `pulumi up` `infrastructure/versioned-docs/production` (creates the prod bucket + role). This
   is the switch: once its outputs exist, release workflows resolve them and start archiving —
   there is no separate enable flag.
2. Set `www.pulumi.com:versionedDocsStack: "pulumi/pulumi-docs-versioned/production"` in
   `infrastructure/Pulumi.www-production.yaml` (a StackReference to the stack from step 1, so it
   must come second), then let a normal site deploy's `pulumi up www-production` add the origin +
   `/docs/versioned/*` behavior and serve `/js/versioned-docs.js` + `/css/versioned-docs-archive.css`.
3. Backfill the historical catalog (dispatch the workflows with `target_env=production`,
   `publish_only=true`, staggered, then `rebuild-manifest.sh`).
4. Verify: archives serve `max-age=31536000, immutable`, the manifest `max-age=300`, and the
   existing `/docs/*` + dotnet routes still resolve.

## Tool ids
`pulumi-cli`, `nodejs`, `nodejs-policy`, `nodejs-esc-sdk`, `python`, `python-policy`,
`python-esc-sdk`, `dotnet`, `dotnet-esc-sdk`, `java`. (ESC CLI is not included — those docs
are no longer part of the site.)

## Known follow-ups
- `dotnet` snapshots currently include the `esc-sdk/` subtree (also archived separately as
  `dotnet-esc-sdk`); add an exclude if the duplication matters.
- Live **SDK** pages don't show the selector (only archives + live CLI pages do); injecting
  it would add a `<script>` to every generated SDK file, which we skipped to avoid commit
  churn. Revisit if wanted.
