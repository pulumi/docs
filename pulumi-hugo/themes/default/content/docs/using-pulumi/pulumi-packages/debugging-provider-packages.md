---
title_tag: "How to Debug Pulumi Provider Packages"
meta_desc: "Learn the process for debugging Pulumi providers locally."
title: Debug provider packages
h1: Debug Pulumi provider packages
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    usingpulumi:
        parent: pulumi-packages
        identifier: how-to-debug-providers
        weight: 2
---

When developing or troubleshooting Pulumi providers, you may need to debug the provider code locally. This guide walks you through starting your provider in debug mode, setting breakpoints, and running tests.

## Starting the provider in debug mode

To setup a process to debug, you will need to start the provider in debug mode through your local IDE. Upon startup, the provider should output a port number to the console (e.g., `12345`), indicating it is ready for a debugger to attach. Here are two examples for GoLand and VS Code.

### Example for GoLand

For GoLand you can follow these steps.

1. Configure the working directory to the program you are going to run to mirror how Pulumi would start the provider

![Screenshot of GoLand configuration for debugging providers](/docs/using-pulumi/pulumi-packages/img/goland-debug-config.png)

### Example for VS Code

For VS Code you can follow these steps.

1. Navigate to **Run -> Add Configuration** and add the **Go: launch package** configuration
2. Edit `"program": "${fileDirname}"` to point to `cmd/pulumi-resource-<PROVIDER>` , e.g., `cmd/pulumi-resource-azure-native` for the Azure Native provider
![Screenshot of VS Code configuration for debugging providers](/docs/using-pulumi/pulumi-packages/img/vscode-launch-config.png)
3. Edit "name": `"Launch Package"` to give it a descriptive name
4. Launch package

![Screenshot of VS Code configuration for debugging providers](/docs/using-pulumi/pulumi-packages/img/vscode-debug-config.png)

## Setting breakpoints

With your IDE configured, set breakpoints within the provider code where you wish to pause execution during debugging.

## Running Pulumi with debug providers

To attach the Pulumi CLI to your provider running in debug mode, use the `PULUMI_DEBUG_PROVIDERS` environment variable. Specify the provider and port number the debugger is listening on.

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

Once Pulumi runs or tests are initiated with the `PULUMI_DEBUG_PROVIDERS` environment variable set, your IDE should automatically attach to the specified port and pause execution at your set breakpoints.

{{< notes type="warning" >}}
**Terminating the Provider Process**: Be cautious when terminating the provider process as the Pulumi state can get out of sync with the actual cloud resources. When in doubt, `pulumi refresh` will address this.
{{< /notes >}}

## Debugging Bridged Providers

### Debugging tfgen

If you need to debug tfgen in one of the providers, you first have to start
tfgen using [dlv](https://github.com/go-delve/delve) exec.

#### Install dlv

```shell
go install github.com/go-delve/delve/cmd/dlv@latest
```

#### Run tfgen with dlv exec

```shell
make debug_tfgen
```

#### Using local pulumi-terraform-bridge

If you want to use a local `pulumi-terraform-bridge` you can use [go
workspaces](https://go.dev/doc/tutorial/workspaces) to build the local provider
along with the local `pulumi-terraform-bridge`.

For example, if you had the following directory structure:

```shell
$ ls
pulumi-my-provider        # YOUR provider
pulumi-terraform-bridge   # github.com/pulumi/pulumi-terraform-bridge

$ cd pulumi-my-provider
```

Then you can run the following commands:

```shell
$ go work init
$ go work use -r ./provider
$ go work use -r ../pulumi-terraform-bridge
```

Then you can re-build tfgen to use the local bridge.

```shell
make tfgen_build_only
```

#### Attaching to the debugger in VS Code

For VS Code you can follow these steps to connect to the debugger.

1. Navigate to **Run -> Add Configuration** and add the **Go: Connect to server** configuration
![Screenshot of VS Code configuration for debugging providers](/docs/using-pulumi/pulumi-packages/img/vscode-launch-config-connect-to-server.png)

2. Edit "name": `"Connect to server"` to give it a descriptive name
3. Connect to server

![Screenshot of VS Code configuration for debugging tfgen](/docs/using-pulumi/pulumi-packages/img/vscode-debug-config-connect-to-server.png)
