---
title_tag: "Running your program on refresh and destroy | Pulumi Operations"
meta_desc: Use --run-program to execute your Pulumi program before refresh or destroy. Required for dynamic credentials and useful for diff-clean provider upgrades.
title: Running your program on refresh and destroy
h1: Running your program on refresh and destroy
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Running your program on refresh and destroy
        parent: iac-operations-stack-management
        weight: 15
---

By default, `pulumi refresh` and `pulumi destroy` do not execute your program. They operate on stack configuration and the resources already recorded in state. The `--run-program` flag opts in to running your program first, so the operation sees whatever your program computes at runtime — provider credentials, dynamic resources, or updated provider inputs.

Reach for `--run-program` whenever the values that `refresh` or `destroy` depend on are produced by code rather than persisted in state. The two most common situations are dynamic credentials and provider upgrades.

## Refreshing or destroying with expired credentials

Most cloud credentials are short-lived: OIDC-issued tokens and STS session credentials expire on the order of minutes to hours, and credentials brokered through a secrets manager are often similarly time-bound. When `pulumi up` runs, the program fetches a fresh credential and Pulumi records the resulting provider configuration in state. The credential is not re-fetched on later operations.

A few hours or days later, running `pulumi refresh` or `pulumi destroy` reuses that recorded provider configuration. The token has expired, the operation fails, and the failure looks like an auth error from the cloud rather than a stale-credential problem.

Add `--run-program` to re-run your program so the provider gets a fresh credential:

```bash
pulumi refresh --run-program
pulumi destroy --run-program
```

## Removing spurious diffs after a provider upgrade

Major-version provider releases typically change resource schemas: property names and types shift, deprecated fields disappear, and the inputs the provider expects look different from what is currently in state. Running `pulumi refresh` after a major provider update without running the program can surface spurious diffs that reflect schema differences rather than real drift in the cloud.

Running the program gives the new provider the inputs it needs to compute a clean diff between your program's intent and the cloud state. After upgrading a provider's major version, run:

```bash
pulumi up --refresh --run-program
```

The [AWS provider 6.x → 7.x migration guide](https://www.pulumi.com/registry/packages/aws/how-to-guides/7-0-migration/) prescribes exactly this command for that reason. The same pattern applies to any provider upgrade where the schema changes — Azure, GCP, Kubernetes, or any other.

## Using the flag

`--run-program` is accepted by `pulumi refresh`, `pulumi destroy`, and by `pulumi up` and `pulumi preview` when they perform a refresh step (`--refresh`):

```bash
pulumi refresh --run-program
pulumi destroy --run-program
pulumi up --refresh --run-program
pulumi preview --refresh --run-program
```

To set it once per shell or in CI, use the equivalent environment variable:

```bash
export PULUMI_RUN_PROGRAM=true
```

See [Pulumi CLI environment variables](/docs/iac/cli/environment-variables/) for the full list.

## Related uses

- **Resource hooks.** Delete hooks require `--run-program` on `pulumi destroy` — without it, Pulumi cannot register the hooks before deletion and the operation fails. See [Deletions and delete hooks](/docs/iac/concepts/resources/options/hooks/#deletions-and-delete-hooks).
- **Dynamic providers.** Programs that use [dynamic providers](/docs/iac/concepts/providers/dynamic-providers/) need the program to run so Pulumi can load the provider's implementation from your code.

## See also

- [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) — CLI reference.
- [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy/) — CLI reference.
- [Improved refresh and destroy experience for Pulumi IaC](/blog/improved-refresh-destroy-experience/) — original announcement, with extended examples.
- [Resource hooks](/docs/iac/concepts/resources/options/hooks/) — when delete hooks force the use of `--run-program`.
