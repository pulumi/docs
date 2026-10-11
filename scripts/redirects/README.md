# Custom redirects

This directory holds the hand-maintained 301 redirect rules for pulumi.com. Every `.txt`
file here is applied on every production deploy.

## File format

Each non-blank, non-comment line is:

```
<source-key>|<destination>
```

- `<source-key>` is the S3 object key relative to the site root, with no leading slash
  (e.g. `registry/packages/aws/how-to-guides/example/index.html`).
- `<destination>` is either an absolute URL (`https://www.pulumi.com/...`) or a
  path relative to the current bucket (`/dev/tutorials/example/`).
- In this repo, lines starting with `#`, and blank lines, are skipped — see the filter
  in `scripts/make-s3-redirects.js` (`.filter(line => line && !line.startsWith("#"))`).
  Use `#` comments freely here to explain a rule's history or why it can't simply be
  deleted. **This is not universal** — pulumi/registry's applier has no such filter (see
  below), so don't copy a `#`-commented file there expecting the same behavior.

## How these rules are applied

`scripts/make-s3-redirects.sh` globs every `*.txt` file in this directory and feeds each
one to `scripts/make-s3-redirects.js`, which sets each key's S3 object as a
website-redirect (`WebsiteRedirectLocation`), producing a real HTTP 301 rather than a
client-side meta-refresh. This runs as part of every production push
(`scripts/ci-push.sh`), after `scripts/sync-and-test-bucket.sh` has already synced the
built site to the bucket with `s5cmd sync --delete`. The `--delete` matters here: it means
nothing survives a deploy by accident. If a redirect is live on pulumi.com today, some
`.txt` file in this directory (or the equivalent directory in another repo — see below)
put it there on the most recent deploy. There is no such thing as an orphaned rule that
"just happens to still work" from a prior deploy.

## The other redirect source: Hugo aliases

Not all redirects are hand-written here. A page can declare Hugo `aliases` in its front
matter, and `scripts/translate-redirects.js` scans the built site for the resulting
client-side meta-refresh stubs and folds them into the same redirect pipeline. Use a
Hugo `alias` for a redirect that lives alongside the page it points from (e.g. a renamed
or moved doc); use a hand-written rule in this directory for anything else, including
cross-domain redirects (`/dev/...`) and redirects for pages that no longer exist in this
repo at all.

## Cross-repo ownership: this directory does not own everything under `registry/**`

**pulumi/registry has its own, independently-deployed `scripts/redirects/` directory**,
applied by that repo's own `scripts/ci/make-s3-redirects.sh` as part of its own push
pipeline. Redirect keys under `registry/**` — most notably the large family of
`registry/packages/*/how-to-guides/*` how-to guides that redirect to `/dev/tutorials/...`
or `/dev/examples/...` — are documented and owned there, not here. See
`pulumi/registry :: scripts/redirects/how-to-guides-to-dev-redirects.txt`.

Both repos share the same `<source-key>|<destination>` line format and directory name, so
a search for a `registry/**` key in this repo alone will report a false "orphan": the rule
exists, just in the other repo. The two appliers are *not* otherwise identical, though —
pulumi/registry's `scripts/ci/make-s3-redirects.sh` reads every line as `key|location`
with no `#`-comment filter, so a `#` comment in one of its redirect files gets uploaded as
a real (broken) S3 redirect keyed by the comment text. Don't assume a convention that's
safe in this repo's files is safe in pulumi/registry's. Before concluding a live redirect
is undocumented, check both directories for the key itself:

- `pulumi/docs :: scripts/redirects/*.txt` (this directory)
- `pulumi/registry :: scripts/redirects/*.txt`

If you're adding a rule for a `registry/**` key, it belongs in pulumi/registry, not here.
