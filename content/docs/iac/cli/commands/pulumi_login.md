---
title: "pulumi login | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_login/
meta_desc: "Authenticate with the Pulumi Cloud or self-hosted backend. Manage your login credentials."
---



Log in to the Pulumi Cloud

## Synopsis

Log in to the Pulumi Cloud.

The Pulumi Cloud manages your stack's state reliably. Simply run

    $ pulumi login

and this command will prompt you for an access token, including a way to launch your web browser to
easily obtain one. You can script by using `PULUMI_ACCESS_TOKEN` environment variable.

By default, this will log in to the managed Pulumi Cloud backend.
If you prefer to log in to a self-hosted Pulumi Cloud backend, specify a URL. For example, run

    $ pulumi login https://api.pulumi.acmecorp.com

to log in to a self-hosted Pulumi Cloud running at the api.pulumi.acmecorp.com domain.

For `https://` URLs, the CLI will speak REST to a Pulumi Cloud that manages state and concurrency control.
You can specify a default org to use when logging into the Pulumi Cloud backend or a self-hosted Pulumi Cloud.

If you prefer to operate Pulumi independently of a Pulumi Cloud, and entirely local to your computer,
pass `file://<path>`, where `<path>` will be where state checkpoints will be stored. For instance,

    $ pulumi login file://~

will store your state information on your computer underneath `~/.pulumi`. It is then up to you to
manage this state, including backing it up, using it in a team environment, and so on.

As a shortcut, you may pass --local to use your home directory (this is an alias for `file://~`):

    $ pulumi login --local

Additionally, you may leverage supported object storage backends from one of the cloud providers to manage the state independent of the Pulumi Cloud. For instance,

AWS S3:

    $ pulumi login s3://my-pulumi-state-bucket

GCP GCS:

    $ pulumi login gs://my-pulumi-state-bucket

Azure Blob:

    $ pulumi login azblob://my-pulumi-state-bucket

PostgreSQL:

    $ pulumi login postgres://username:password@hostname:5432/database

### OIDC token exchange

For secure authentication in CI/CD pipelines and automated workflows, you can use OIDC token exchange to log in without managing long-lived credentials. This feature exchanges a short-lived OIDC token from your identity provider for a Pulumi Cloud access token.

To log in using OIDC token exchange, provide an OIDC token and your organization name:

    $ pulumi login --oidc-token <token> --oidc-org <org-name>

The `--oidc-token` flag accepts either a raw token string or a file path prefixed with `file://`:

    $ pulumi login --oidc-token file:///path/to/token.txt --oidc-org my-org

By default, the exchanged token is scoped to your organization. You can optionally scope it to a specific team or user:

    $ pulumi login --oidc-token <token> --oidc-org my-org --oidc-team my-team

The exchanged access token expires after 2 hours by default. You can customize the expiration using the `--oidc-expiration` flag:

    $ pulumi login --oidc-token <token> --oidc-org my-org --oidc-expiration 4h

This approach is particularly useful in environments like GitHub Actions, GitLab CI, or any CI/CD system that provides OIDC tokens, as it eliminates the need to store long-lived Pulumi access tokens as secrets.

## Command

```
pulumi login [<url>] [flags]
```

## Options

```
  -c, --cloud-url string         A cloud URL to log in to
      --default-org string       A default org to associate with the login. Please note, currently, only the managed and self-hosted backends support organizations
  -h, --help                     help for login
      --insecure                 Allow insecure server connections when using SSL
      --interactive              Show interactive login options based on known accounts
  -l, --local                    Use Pulumi in local-only mode
      --oidc-expiration string   The expiration for the cloud backend access token in duration format (e.g. '15m', '24h')
      --oidc-org string          The organization to use for OIDC token exchange audience
      --oidc-team string         The team when exchanging for a team token
      --oidc-token string        An OIDC token to exchange for a cloud backend access token. Can be either a raw token or a file path prefixed with 'file://'.
      --oidc-user string         The user when exchanging for a personal token
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
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi](/docs/iac/cli/commands/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 12-Dec-2025
