---
title_tag: "Registry API for agents"
meta_desc: "Query every published Pulumi package, version by version, through the cloud registry API: endpoints, parameters, schemas, and markdown access for agents."
title: Registry API for agents
h1: Registry API for agents
menu:
    reference:
        name: Registry API for agents
        parent: reference-home
        weight: 6
---

The cloud registry API serves every published Pulumi package, version by version: READMEs, installation instructions, API docs navigation, per-type docs, examples, and the package schema. It's the programmatic counterpart of the [Pulumi Registry](/registry/), and it's built for AI agents and scripts.

Public packages need no authentication. For private packages, send `Authorization: token $PULUMI_ACCESS_TOKEN`. The API works without the Pulumi CLI, and the CLI can call it through [`pulumi api`](/docs/iac/cli/api/).

## Quick start

With the CLI, `pulumi api` fills in `lang` and `os` from the project runtime and the host OS:

```bash
pulumi api list --filter registry
pulumi api describe GetPackageVersion
pulumi api /api/registry/packages/pulumi/pulumi/aws/versions/latest/readme
```

Over HTTP, request the markdown variant with an `Accept` header:

```bash
curl -H "Accept: text/markdown" \
  https://api.pulumi.com/api/registry/packages/pulumi/pulumi/aws/versions/latest/readme

curl -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/registry/packages/<source>/<publisher>/<private-pkg>/versions/latest/installation
```

## Endpoints

All paths are relative to `https://api.pulumi.com`. Replace `{version}` with a pinned semver where possible, or `latest` for the most recent published version.

```text
/api/registry/packages?search={query}
/api/registry/packages/{source}/{publisher}/{name}/versions
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}/readme
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}/installation
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}/nav
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}/docs/{typeToken}
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}/examples
```

- The `versions` list is paginated with a `continuationToken`. It's reachable over HTTP only, because it isn't in the OpenAPI spec that `pulumi api` reads.
- `installation` returns `404` for packages that publish no installation configuration.
- Type tokens in `docs/{typeToken}` are URL-encoded with `encodeURIComponent` or an equivalent. For example, `random:index/randomPassword:RandomPassword` becomes `random%3Aindex%2FrandomPassword%3ARandomPassword`. Discover type tokens with `nav?depth=full`.

## Parameters

| Parameter | Applies to | Values |
|-----------|------------|--------|
| `lang` | Common | `typescript`, `python`, `go`, `csharp`, `java`, `yaml`, `hcl`, or `all`. HTTP calls default to `go`; the CLI fills it from the project runtime. |
| `os` | Common | `linux`, `macos`, or `windows`. |
| `depth` | `nav` | `summary` or `full`. |
| `q` | `nav`, `examples` | A search term. |
| `limit` | `examples` | Defaults to 20. Values above 100 are clamped to 100. |

For prose responses, pass `--output=markdown` to `pulumi api`, or send `Accept: text/markdown` over HTTP.

## Provider schemas

The full Pulumi schema for a provider includes resource types, input and output shapes, function signatures, and language-specific type mappings. The response from `versions/{version}` includes a `schemaURL` field; follow it for the version-pinned schema:

```bash
pulumi api /api/registry/packages/pulumi/pulumi/aws/versions/7.0.0 \
  | jq -r .schemaURL | xargs curl
```

[`pulumi package get-schema`](/docs/iac/cli/commands/pulumi_package_get-schema/) accepts `<name>[@version]`, a plugin binary or folder path, or a local `.json` or `.yaml` schema file:

```bash
pulumi package get-schema aws
pulumi package get-schema aws@7.0.0
```

The static schema URL on the Pulumi Registry serves the latest version only:

```bash
curl https://www.pulumi.com/registry/packages/aws/schema.json
```

## Markdown access to docs pages

Every `/docs/` URL on www.pulumi.com is also available as markdown, through either of two equivalent mechanisms:

- **`Accept` header**: send `Accept: text/markdown` to the normal URL.
- **`.md` suffix**: drop the trailing slash and append `.md`. For example, `/docs/iac/concepts/resources/` becomes `/docs/iac/concepts/resources.md`. The docs root is the exception: use `/docs/index.md`.

Both forms return the same content from the same cache entry:

```bash
curl -H "Accept: text/markdown" https://www.pulumi.com/docs/iac/concepts/resources/
curl https://www.pulumi.com/docs/iac/concepts/resources.md
```

`/registry/` URLs support the same mechanisms, such as `/registry/packages/<name>.md` and `/registry.md`, but only for the latest version of a package:

```bash
curl -H "Accept: text/markdown" https://www.pulumi.com/registry/packages/aws/
curl https://www.pulumi.com/registry/packages/aws.md
curl https://www.pulumi.com/registry.md
```

`/registry/packages/<name>/api-docs/*` pages aren't served as markdown. Use the `nav` and `docs/{typeToken}` endpoints of the cloud registry API instead.

## Next steps

- [Registry URL reference](/docs/reference/registry-urls/)
- [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/)
- [`pulumi api`](/docs/iac/cli/api/)
