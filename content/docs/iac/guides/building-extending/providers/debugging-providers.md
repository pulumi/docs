---
title_tag: "How to debug a Pulumi provider"
meta_desc: "Learn the process for debugging Pulumi providers locally."
title: Debugging Providers
h1: Debugging Pulumi providers
menu:
    iac:
        name: Debugging providers
        parent: iac-guides-providers
        weight: 40
aliases:
    - /docs/iac/operations/debugging/debugging-providers/
    - /docs/support/debugging/debugging-providers/
    - /docs/using-pulumi/pulumi-packages/debugging-provider-packages/
    - /docs/iac/packages-and-automation/pulumi-packages/debugging-provider-packages/
    - /docs/using-pulumi/pulumi-packages/debugging-provider-packages/
    - /docs/iac/using-pulumi/pulumi-packages/debugging-provider-packages/
    - /docs/iac/using-pulumi/extending-pulumi/debugging-providers/
    - /docs/iac/extending-pulumi/debugging-providers/
    - /docs/iac/build-with-pulumi/debugging-providers/
    - /docs/iac/troubleshooting/debugging/debugging-providers/
---

When developing or troubleshooting Pulumi providers, you may need to debug the provider code locally. This guide walks you through starting your provider in debug mode, setting breakpoints, and running tests.

## Starting the provider in debug mode

To set up a process to debug, start the provider in debug mode through your local IDE. On startup, the provider should output a port number to the console (for example, `12345`), indicating that a debugger can attach. Here are two examples for GoLand and VS Code.

### Example for GoLand

Create a **Go Build** run/debug configuration that points at the provider's command directory — `provider/cmd/pulumi-resource-<PROVIDER>` (for example, `provider/cmd/pulumi-resource-azure-native` for the Azure Native provider). Set the configuration's working directory to mirror how Pulumi starts the provider, then run it in debug mode.

### Example for VS Code

In VS Code, configuring a working directory isn't necessary.

1. Navigate to **Run** > **Add Configuration** and add the **Go: Launch Package** configuration.
1. Set `"program"` to the provider's command directory, `provider/cmd/pulumi-resource-<PROVIDER>` (for example, `provider/cmd/pulumi-resource-azure-native` for the Azure Native provider).
1. Set `"name"` to something descriptive, such as `"Debug Provider"`.
1. Run the configuration to launch the provider.

A complete `.vscode/launch.json` looks like this:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Provider",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "${workspaceFolder}/provider/cmd/pulumi-resource-<PROVIDER>",
            "buildFlags": "-ldflags '-X github.com/pulumi/pulumi-<PROVIDER>/provider/pkg/version.Version=1.0.0-alpha.0+dev'",
            "env": {}
        }
    ]
}
```

Hard-coding `"program"` means you don't need to have `main.go` open to start the configuration. Pass the build flags as a single quoted string so that Delve doesn't split the `ldflags` into separate arguments. Use the `"env"` object to set any environment variables your provider needs.

## Setting breakpoints

With your IDE configured, set breakpoints within the provider code where you wish to pause execution during debugging.

## Running Pulumi with debug providers

To attach the Pulumi CLI to your provider running in debug mode, use the `PULUMI_DEBUG_PROVIDERS` environment variable. Specify the provider name and the port number the provider printed on startup.

For example, to debug a deployment with the `azure-native` provider on port `12345`, you would run:

```shell
PULUMI_DEBUG_PROVIDERS="azure-native:12345" pulumi up
```

## Running tests

This approach also works for running tests, such as acceptance tests in a provider's examples folder. For instance:

```shell
cd pulumi-wavefront/examples
PULUMI_DEBUG_PROVIDERS="wavefront:53766" go test -v -tags=python
```

## Debugger attachment

Once you start a Pulumi run or tests with the `PULUMI_DEBUG_PROVIDERS` environment variable set, the Pulumi CLI connects to the provider on the specified port, and your IDE's debugger pauses execution at your breakpoints.

{{< notes type="warning" >}}
**Terminating the provider process**: Be cautious when terminating the provider process as the Pulumi state can get out of sync with the actual cloud resources. When in doubt, `pulumi refresh` will address this.
{{< /notes >}}

## Debugging bridged providers

Many Pulumi providers — including most of the classic cloud providers — are *bridged*: they're built with the [Pulumi Terraform Bridge](https://github.com/pulumi/pulumi-terraform-bridge), which wraps an upstream Terraform provider and re-exposes it as a Pulumi provider. The `PULUMI_DEBUG_PROVIDERS` workflow covered earlier works for any provider; the techniques in this section are specific to bridged providers.

A bridged provider has two parts you might need to debug:

- **The provider runtime** — the `pulumi-resource-<PROVIDER>` binary that runs during `pulumi up`. Debug it with `PULUMI_DEBUG_PROVIDERS`; see [Running Pulumi with debug providers](#running-pulumi-with-debug-providers).
- **tfgen** — the build-time code generator that reads the upstream Terraform provider's schema and produces the Pulumi schema and language SDKs.

### Debugging tfgen

Because tfgen is a build-time tool rather than a running provider process, you debug it by starting it under [dlv](https://github.com/go-delve/delve) `exec` and attaching, rather than with `PULUMI_DEBUG_PROVIDERS`.

#### Install Delve

```shell
go install github.com/go-delve/delve/cmd/dlv@latest
```

#### (Optional) Use a local pulumi-terraform-bridge

If you want to debug against a local `pulumi-terraform-bridge`, use [Go workspaces](https://go.dev/doc/tutorial/workspaces) to build the local provider along with the local `pulumi-terraform-bridge`. Skip this step if you only need to debug the provider's own code.

For example, if you had the following directory structure:

```shell
$ ls
pulumi-my-provider        # YOUR provider
pulumi-terraform-bridge   # github.com/pulumi/pulumi-terraform-bridge

$ cd pulumi-my-provider
```

Then run the following commands:

```shell
go work init
go work use -r ./provider
go work use -r ../pulumi-terraform-bridge
```

If you've already built tfgen, delete the existing binary before you continue. `make tfgen_build_only` only rebuilds when the provider's own sources change, so it won't pick up the workspace otherwise:

```shell
rm bin/pulumi-tfgen-<PROVIDER>
```

#### Run tfgen under Delve

Build the tfgen binary with `make tfgen_build_only`, then start it under Delve with `make debug_tfgen`:

```shell
make tfgen_build_only
make debug_tfgen
```

#### Attaching to the debugger in VS Code

`make debug_tfgen` starts a headless Delve server listening on port `2345`. To connect from VS Code:

1. Navigate to **Run** > **Add Configuration** and add the **Go: Connect to server** configuration.
1. Set `"name"` to something descriptive, such as `"Connect to tfgen"`.
1. Run the configuration to attach to the running tfgen process.

The configuration looks like this:

```json
{
    "name": "Connect to tfgen",
    "type": "go",
    "request": "attach",
    "mode": "remote",
    "port": 2345,
    "host": "127.0.0.1"
}
```
