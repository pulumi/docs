---
title: Calling the Cloud API
title_tag: "Pulumi CLI: Calling the Pulumi Cloud REST API"
meta_desc: Use pulumi api to call any Pulumi Cloud REST API endpoint from the CLI, with stable exit codes and a JSON error envelope for scripts and agents.
h1: Calling the Pulumi Cloud REST API from the CLI
menu:
  iac:
    parent: iac-cli
    identifier: iac-cli-api
    weight: 60
aliases:
- /docs/iac/cli/cloud-api/
---

The [`pulumi api`](/docs/iac/cli/commands/pulumi_api/) command lets you call any [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/) endpoint directly from the CLI. It runs non-interactively, is safe to script, and reuses the credentials you already use with `pulumi login`, so you don't need to manage a separate token to call the API.

The command is modeled after [`gh api`](https://cli.github.com/manual/gh_api): you pass a path, an operation ID, or a `METHOD path` row and the CLI handles authentication, headers, path-template substitution, and content negotiation for you.

## Subcommands

`pulumi api` ships in three forms:

* [`pulumi api <path-or-operation-id>`](/docs/iac/cli/commands/pulumi_api/) issues a single HTTP request against the named endpoint.
* [`pulumi api list`](/docs/iac/cli/commands/pulumi_api_list/) (alias: `ls`) lists every endpoint exposed by the [Pulumi Cloud OpenAPI spec](/docs/reference/cloud-rest-api/). Output is a TTY-friendly table by default; pass `--output=json` to get a stable, scriptable envelope.
* [`pulumi api describe <path-or-operation-id>`](/docs/iac/cli/commands/pulumi_api_describe/) prints the parameters, request body, and response schemas for a single operation. Default output is a human-readable text render; pass `--output=markdown` for a piping-friendly markdown document or `--output=json` for the stable JSON envelope.

## Authentication

`pulumi api` uses the same access token as the rest of the Pulumi CLI. Anything that authorizes `pulumi login` — a personal, organization, or team [access token](/docs/administration/access-identity/access-tokens/), `PULUMI_ACCESS_TOKEN`, or an OIDC-issued token — also authorizes API calls.

If a request requires authentication and the CLI is not authenticated, `pulumi api` exits with code `3` and an error envelope identifying the auth failure. A `401` or `403` response from the API maps to the same exit code.

## Path-template substitution

Most Pulumi Cloud endpoints take an organization, project, or stack as part of the URL — for example, `/api/orgs/{orgName}/members`. `pulumi api` resolves each template variable in the following order:

1. A literal value typed directly into the URL (no template variable to fill).
1. A matching `-F` or `-f` field (consumed for the path and not forwarded as a query or body parameter).
1. The current Pulumi project context: the selected stack's organization, the project name from `Pulumi.yaml`, and the selected stack name.

When a stack is selected, you can usually call:

```bash
pulumi api ListOrganizationMembers
```

and the CLI fills `{orgName}` from the selected stack automatically. When no project context is available, supply the values with `-F`:

```bash
pulumi api GetStack -F orgName=acme -F projectName=web -F stackName=prod
```

If a path template and a request body field share a parameter name, the first matching `-F` is consumed for the path. Any subsequent `-F` with the same key is sent in the body, so you can pass `-F` twice to fill both. To keep the body fully separate, use `--body` or `--input` instead.

## Request flags

`pulumi api` accepts a `gh api`-style flag set for shaping the request:

| Flag | Purpose |
|---|---|
| `-X` / `--method` | HTTP method. Defaults to `GET`, or `POST` when body fields, `--body`, or `--input` are present. |
| `-F` / `--field` | Typed `key=value`. Numbers, booleans, and `null` are auto-detected; JSON object/array literals are parsed; `@file` reads from a file and `@-` reads from stdin. Routed as query parameters on `GET`/`HEAD` and as JSON body fields otherwise. |
| `-f` / `--raw-field` | String `key=value` with no type coercion. Sent verbatim. |
| `-H` / `--header` | Custom HTTP header `Key: Value` (repeatable). User headers win over the encoder's defaults (`Accept`, `Content-Type`); a user-supplied `Authorization` is dropped to keep the resolved CLI token in place. |
| `--body` | Inline request body sent verbatim. Mutually exclusive with `--input`. |
| `--input` | Read the request body from a file; `-` reads from stdin. |
| `--paginate` | Follow continuation cursors and emit a single combined JSON envelope. Capped at 1000 pages; on truncation, network failure, or cancellation, the partial result is flushed so callers always have something to act on. |
| `-i` / `--include` | Include the HTTP status line and response headers in the output. |
| `--silent` | Suppress the response body on success. Errors are still printed. |
| `--verbose` | Dump the resolved request and the full response to stderr. |
| `--dry-run` | Print the resolved request without sending it. |
| `--output` | Drive content negotiation. Default uses the operation's primary response content type (usually JSON). `json` or `markdown` request that format via the `Accept` header — rejected if the operation's spec doesn't declare it. `raw` keeps the operation's default `Accept` and passes the response body through unchanged. |

Both requests and responses use gzip compression in transit. The CLI routes responses by content type: it pretty-prints JSON, passes text and markdown through as-is, and streams binary responses unchanged.

## OpenAPI spec caching

The CLI fetches the OpenAPI spec once from `/api/openapi/pulumi-spec.json` and caches it under `$PULUMI_HOME/cloud-api-cache/<host>/spec.json` for 24 hours. When the cached copy is older than the TTL and a refresh fails (network error, 5xx response), the CLI returns the stale cache along with a stderr warning so transient outages don't break `list` and `describe`.

Pass `--refresh-spec` to any subcommand to force a re-fetch.

## Exit codes and error envelope

`pulumi api` uses the standard [Pulumi CLI exit-code mapping](/docs/iac/cli/exit-codes/). The values it can emit are:

| Exit code | Meaning |
|----------:|---------|
| `0` | Success. |
| `1` | Caller error: bad arguments, no matching operation, missing template variable, or partial pagination. |
| `2` | Invalid flag combination (for example, `--body` and `--input` together). |
| `3` | Authentication or authorization failure (missing credentials, `401`, or `403`). |
| `8` | Operation canceled (`SIGINT` or `SIGTERM`). |
| `255` | Internal CLI error. |

On failure, the CLI writes errors to stderr as a single-line JSON envelope with a stable `code` field. Agents and scripts can parse the envelope to react to specific failure modes; tests pin the schema so it does not drift between releases.

## Examples

### Basic requests

Inspect the currently authenticated user:

```bash
pulumi api /api/user
```

Call by URL path with template variables filled from `-F`:

```bash
pulumi api /api/orgs/{orgName}/members -F orgName=acme
```

Call by operation ID — `orgName` is taken from the current Pulumi project:

```bash
pulumi api ListOrganizationMembers
```

Pass path variables explicitly when no project context is available:

```bash
pulumi api GetStack -F orgName=acme -F projectName=web -F stackName=prod
```

### Bodies and fields

Create a resource via `POST`; body fields are auto-detected from the operation:

```bash
pulumi api CreateOrgToken -F orgName=acme \
  -F name=ci-bot -F description="CI deploy token" \
  -F admin=false -F expires=0
```

Send a nested JSON body by mixing scalar fields with an inline JSON literal:

```bash
pulumi api CreateStack -F orgName=acme -F projectName=web \
  -F stackName=prod -F 'tags={"env":"prod","team":"platform"}'
```

Pass an entire request body inline, or read it from a file or stdin:

```bash
pulumi api UpdateStackTags -F orgName=acme -F projectName=web -F stackName=prod \
  --body '{"env":"prod","team":"platform"}'

pulumi api UpdateStackTags --input ./tags.json

cat tags.json | pulumi api UpdateStackTags --input -
```

### Filtering and pagination

Filter the JSON response with `jq`:

```bash
pulumi api /api/user --output=json | jq '.githubLogin'
```

Walk every page of a paginated endpoint:

```bash
pulumi api ListUserStacks --paginate | jq -r '.stacks[].stackName'
```

### Discovery and dry-run

Browse the API surface and inspect a specific operation:

```bash
pulumi api list --output=json | jq '.operations[] | select(.tag == "Stacks")'

pulumi api describe CreateOrgToken --output=markdown
```

Preview the resolved request without sending it:

```bash
pulumi api CreateOrgToken -F orgName=acme \
  -F name=ci-bot -F description="CI" -F admin=false -F expires=0 --dry-run
```

## See also

* [`pulumi api` command reference](/docs/iac/cli/commands/pulumi_api/)
* [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/)
* [Pulumi Cloud access tokens](/docs/administration/access-identity/access-tokens/)
* [Pulumi CLI exit codes](/docs/iac/cli/exit-codes/)
