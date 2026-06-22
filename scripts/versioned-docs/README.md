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

## Scripts

| script | purpose |
|---|---|
| `inject-version-switcher.sh` | Insert loader + (archive mode) noindex/canonical into generated HTML; strips any pre-existing canonical/robots. |
| `publish-version.sh` | Refuse-overwrite, inject, sync immutable, manifest read-modify-write, invalidate. |
| `snapshot-cli-docs.sh` | Turn a built `public/docs/iac/cli/commands/` into a self-contained snapshot (vendor fingerprinted css/js, rewrite intra-links) and publish. |
| `redact-version.sh` | Delete a version's objects (all S3 versions) + drop it from the manifest + invalidate. |
| `assert-head-tag.sh` | CI guard: every generated page has a `</head>`/`</body>` injection point. |

## Runbooks

### Enable auto-publish on releases
Auto-publish is **off by default** — real release workflows are unaffected until you opt in.
To turn it on (after the `production` stack is deployed):
1. Set repo **variable** `VERSIONED_DOCS_ENABLED=true`.
2. Set repo **variable** `VERSIONED_DOCS_PROD_DISTRIBUTION_ID` to the production CloudFront id.
Every SDK/CLI release workflow then archives its version to production automatically.

### Manually publish / test a single version
Dispatch the relevant workflow with `publish_versioned=true` and `target_env=testing`
(or `production`). The CLI workflow runs a full `make build` first; SDK workflows publish
their already-generated `static-prebuilt/...` output.

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
1. `pulumi up` `infrastructure/versioned-docs/production` (creates the prod bucket + role).
2. Set `www.pulumi.com:versionedDocsStack: "pulumi/pulumi-docs-versioned/production"` in
   `infrastructure/Pulumi.www-production.yaml`, then `pulumi up` the `www-production` stack
   (adds the origin + behavior).
3. Deploy the site so `/js/versioned-docs.js` is served in production.
4. Set the `VERSIONED_DOCS_ENABLED` + `VERSIONED_DOCS_PROD_DISTRIBUTION_ID` repo variables.

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
