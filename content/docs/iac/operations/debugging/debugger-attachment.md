---
title_tag: "Debugging Pulumi programs"
meta_desc: "Guide to attaching a debugger to Pulumi programs and stepping through the code."
title: Attaching a debugger
h1: Attaching a debugger to a Pulumi program
menu:
    iac:
        name: Attaching a debugger
        parent: iac-operations-debugging
        weight: 20
        identifier: iac-operations-debugging-debugger-attachment
aliases:
    - /docs/support/debugging/debugger-attachment/
    - /docs/using-pulumi/debugging/
    - /docs/concepts/debugging/
    - /docs/iac/concepts/debugging/
    - /docs/iac/troubleshooting/debugging/debugger-attachment/
---

Because Pulumi uses general-purpose programming languages to provision cloud resources, you can take advantage of native debugging tools to troubleshoot your infrastructure definitions.

You can't directly F5-launch your Pulumi program from your IDE. Instead, you run the Pulumi CLI, which launches your program through its language runtime in a separate process, and then you attach to that process from your IDE. See [How Pulumi works](/docs/iac/guides/basics/how-pulumi-works/) to learn more about the Pulumi execution model.

## Debugging with Visual Studio Code and the Pulumi extension

Pulumi provides a VS Code extension that you can use to launch and debug Pulumi programs.

### Install the extension

Install the [Pulumi extension](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-tools) using Visual Studio Marketplace.

### Open a project

Open a new or existing Pulumi project as a VS Code workspace. The extension supports both [single-folder workspaces](https://code.visualstudio.com/docs/editor/workspaces#_singlefolder-workspaces)
and [multi-root workspaces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces).

### Start debugging

Pulumi programs are run (with or without debugging) using a [launch configuration](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations). Select the Run and Debug icon in the Activity Bar on the side of VS Code, then use an automatic debug configuration or create a launch configuration file for your project.

The extension automatically generates a debug configuration to run `pulumi up` or `pulumi preview` for the current Pulumi stack. To use an automatic debug configuration, do the following:

1. Open your program file in VS Code and set a breakpoint.
1. Select the __Run and Debug__ icon.
1. Choose __Show all automatic debug configurations__.
1. Select __Pulumi...__, then `pulumi preview` or `pulumi up`. Debugging starts automatically.

    ![VS Code list of automatic debug configurations with Pulumi selected](/docs/iac/operations/debugging/images/automatic-1.png)

    ![Pulumi launch configurations for pulumi preview and pulumi up](/docs/iac/operations/debugging/images/automatic-2.png)

1. Select or create a stack if prompted to do so.

    ![Stack selection prompt listing existing stacks and a create option](/docs/iac/operations/debugging/images/stack-selection-1.png)

### Debug your program

Set breakpoints in your program code and use the full functionality of the VS Code debugger.
See [VS Code Debugging](https://code.visualstudio.com/docs/editor/debugging) for more information.

![VS Code editor paused at a breakpoint in a Pulumi TypeScript program](/docs/iac/operations/debugging/images/debugging.png)

### Pulumi CLI output

Access the CLI output via the Debug Console view.

![Pulumi CLI output in the VS Code Debug Console](/docs/iac/operations/debugging/images/debug-console.png)

## Debugging with other IDEs

You can use any other IDE or editor that supports attaching to running programs using the [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/). The tools differ depending on your preference and the language you are using, but the process is similar:

1. Start with an existing Pulumi project that contains `Pulumi.yaml` and your program.
2. Open your IDE and set a breakpoint in your program.
3. Run `pulumi up --attach-debugger` from a command line.
4. Wait until `pulumi` is paused waiting for a debugger to attach.
5. Attach the debugger to a running process of your language runtime.
6. Step through the program to find the problem.
7. Run the program to completion and let `pulumi` shut down all the processes.
8. Change your program and repeat the process if needed.

`pulumi up` runs your program twice, once for the preview and once for the update, and both runs trigger the debugger. Use `pulumi preview --attach-debugger` or `pulumi up --skip-preview --attach-debugger` to pick one of the two modes.

## Manual debugger setup

To set up debugging manually for a Node.js program, create or update `.vscode/launch.json` with the following configuration to enable debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Pulumi Program (debug)",
            "type": "node",
            "request": "attach",
            "continueOnAttach": true,
            "skipFiles": [
                "${workspaceFolder}/node_modules/**/*.js",
                "${workspaceFolder}/lib/**/*.js",
                "<node_internals>/**/*.js"
            ]
        }
    ]
}
```

Open your program and set breakpoints by clicking to the left of the line numbers.

In a terminal, run `NODE_OPTIONS="--inspect-brk" pulumi up` to start the deployment process in debug mode. This causes Pulumi to pause execution and wait for a debugger to attach.

Press `F5` in VS Code to start debugging. VS Code will attach to the waiting Node.js process, and execution will continue until reaching the first breakpoint you have set.

For a step-by-step guide to attaching a debugger to a Pulumi TypeScript program, see the [breakpoint debugging blog post](/blog/next-level-iac-breakpoint-debugging/).
