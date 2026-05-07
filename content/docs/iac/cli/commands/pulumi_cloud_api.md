---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi cloud api | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_cloud_api/
meta_desc: "Learn about the pulumi cloud api command."
---



Call any Pulumi Cloud API endpoint

## Synopsis

Call any Pulumi Cloud API endpoint.

The positional argument may be: a path (with optional {template} variables, e.g.
`/api/orgs/{orgName}/members`), an operation ID as shown in `list` (e.g.
`ListOrgMembers`), or a paste-friendly row (`GET /api/...`). Template variables
are resolved from the current Pulumi project / selected stack, or supplied
with -F (e.g. `-F orgName=acme`).

Fields provided via -F/--field and -f/--raw-field are sent as query parameters
on GET/HEAD requests and as a JSON request body on POST/PUT/PATCH/DELETE. Method
defaults to GET, or POST when body fields, --body, or --input are present.

Value forms accepted by -F:
  - scalars: `-F name=acme`, `-F count=3`, `-F enabled=true`, `-F note=null`
  - nested JSON: `-F 'labels={"env":"prod"}'`, `-F 'tags=["a","b"]'`
  - file / stdin: `-F body=@./payload.json`, `-F note=@-`
Use -f/--raw-field to suppress coercion and send the value verbatim as a string.

For an entire request body, pass --body '<json>' inline, or --input <file> (use
`-` for stdin) to stream from a file.

A field whose key matches a path template variable (e.g. `-F poolId=123` against
`{poolId}`) fills that variable and is not forwarded as a query or body parameter.
This is the way to supply non-context path parameters when calling by operation
ID.

When a path template and the request body share a parameter name, the first
matching -F is consumed for the path and any subsequent -F with the same key is
sent in the body. Pass -F twice to fill both, or use --body / --input to supply
the body separately.

The OpenAPI spec is cached locally for 24 hours; pass --refresh-spec on any
subcommand to force a re-fetch.

Exit codes: 0 success; 1 caller error; 2 invalid flags; 3 auth; 8 cancelled;
255 internal.

```
pulumi cloud api [path-or-operation-id] [flags]
```

## Examples

```
  # Inspect the currently authenticated user.
  pulumi cloud api /api/user

  # Call by raw path with template variables filled from -F.
  pulumi cloud api /api/orgs/{orgName}/members -F orgName=acme

  # Multiple template variables in the path are filled the same way.
  pulumi cloud api /api/stacks/{orgName}/{projectName}/{stackName} \
    -F orgName=acme -F projectName=web -F stackName=prod

  # Call by operation ID — orgName is taken from the current Pulumi project.
  pulumi cloud api ListOrgMembers

  # Pass path variables explicitly when no project context is available.
  pulumi cloud api GetStack -F orgName=acme -F projectName=web -F stackName=prod

  # Create a resource via POST; body fields go into a JSON body automatically.
  pulumi cloud api CreateStackTag -F orgName=acme -F projectName=web \
    -F stackName=prod -F name=env -F value=prod

  # Build a nested body by mixing scalar fields with an inline JSON object.
  pulumi cloud api CreateStack -F orgName=acme -F projectName=web \
    -F stackName=prod -F 'tags={"env":"prod","team":"platform"}'

  # Send an array of items using a JSON literal.
  pulumi cloud api AddTeamMembers -F orgName=acme -F teamName=eng \
    -F 'members=["alice","bob","carol"]'

  # Pass the entire request body inline with --body.
  pulumi cloud api UpdateStack -F orgName=acme -F projectName=web -F stackName=prod \
    --body '{"description":"managed by agent"}'

  # Read a JSON body from a file, or from stdin with `-`.
  pulumi cloud api UpdateStackTag --input ./tag.json
  cat tag.json | pulumi cloud api UpdateStackTag --input -

  # Filter the JSON response with jq.
  pulumi cloud api /api/user --format=json | jq '.githubLogin'

  # Follow pagination cursors and stream the combined result to jq.
  pulumi cloud api ListStacks --paginate | jq '.stacks[].name'

  # Extract just the status line + headers without the body.
  pulumi cloud api /api/user --include --silent

  # Preview the resolved request without sending it.
  pulumi cloud api CreateStackTag -F orgName=acme --dry-run
```

## Options

```
      --body string             Inline request body sent verbatim (default Content-Type: application/json). Mutually exclusive with --input
      --dry-run                 Print the resolved request without sending it
      --envelope-version int    Pin the JSON envelope version the caller expects (default 1)
  -F, --field stringArray       Typed key=value; numbers/bools/null auto-detected; JSON object/array literals parsed; @file reads file; @- reads stdin. Sent as query params on GET/HEAD, JSON body fields otherwise
      --format json             Drive content negotiation and rendering. Default uses the op's primary response content type (usually JSON). json or `markdown` request that format via the Accept header — rejected if the op's spec doesn't declare it. `raw` keeps the op's default Accept and writes the body through unchanged.
  -H, --header Key: Value       Custom HTTP header Key: Value (repeatable)
  -h, --help                    help for api
  -i, --include                 Include HTTP status line and response headers in output
      --input -                 Read request body from file; - reads stdin
  -X, --method string           HTTP method (default GET, POST when body fields are present)
      --paginate                Follow pagination cursors and emit the combined result
  -f, --raw-field stringArray   String key=value with no type coercion. Sent as query params on GET/HEAD, JSON body fields otherwise
      --refresh-spec            Re-fetch the OpenAPI spec from Pulumi Cloud and overwrite the local cache
      --silent                  Do not print the response body on success; errors are still printed and exit non-zero
      --verbose                 Dump full request and response to stderr
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --otel-traces string           Export OpenTelemetry traces to the specified endpoint. Use file:// for local JSON files, grpc:// for remote collectors
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
```

## SEE ALSO

* [pulumi cloud](/docs/iac/cli/commands/pulumi_cloud/)	 - Interact with Pulumi Cloud
* [pulumi cloud api describe](/docs/iac/cli/commands/pulumi_cloud_api_describe/)	 - Show the parameters and schemas for a Pulumi Cloud API operation
* [pulumi cloud api list](/docs/iac/cli/commands/pulumi_cloud_api_list/)	 - List every Pulumi Cloud API endpoint

###### Auto generated by spf13/cobra on 7-May-2026
