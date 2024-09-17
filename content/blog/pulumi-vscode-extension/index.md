---
title: "Announcing the Pulumi Visual Studio Code Extension"
date: 2024-09-18
meta_desc: "Enhance your Pulumi development experience with the new VS Code extension. Manage Pulumi IaC and Pulumi ESC directly in your editor."
tags:
    - releases
    - features
---

The Pulumi team is thrilled to bring you the Pulumi Visual Studio (VS) Code Extension, designed to enhance your Pulumi development experience by integrating directly into the tool you already know and love. We understand that working efficiently is key, and this extension helps you do just that by reducing context switching and window juggling, making it easier to build, deploy, and manage your Pulumi applications.

We're focused on developing tools that empower developers to work more seamlessly and efficiently with Pulumi. With this new VS Code extension, we've taken a major step towards this goal. It provides a unified environment where you can debug Infrastructure as Code (IaC) projects, create and handle Environments, Secrets, and Configuration (ESC), and leverage enhanced Pulumi YAML linting and error checking—all without leaving your IDE. Let's dive into the details for each of these.

The following are a few examples of new capabilities you can do within VS Code today:

1. Launch your Pulumi program under a debugger
2. Automatically generate a launch configuration for a Pulumi project
3. Create and explore Pulumi ESC (Environments, Secrets, and Configuration)
4. Get contextual warnings and errors directly within the editor for Pulumi YAML

## Getting Started

### Install the Software

1. Install Pulumi 3.132.0 (or greater) using [these instructions](https://www.pulumi.com/docs/install/).
2. Install the [Pulumi VS Code extension](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-tools) from the Visual Studio Marketplace.

## Debugging Pulumi Programs

### Start Debugging

The Pulumi VS Code Extension allows you to run and debug Pulumi programs with ease. Open a new or existing Pulumi project in VS Code and use an automatic or customized launch configuration.

1. Select the __Run and Debug__ icon.
2. Choose __Show all automatic debug configurations__.
3. Select "Pulumi..." then "pulumi preview" or "pulumi up".

![Automatic Debug Configuration](/iac-automatic-1.png)

Pulumi automatically generates a debug configuration for the current stack, making it simple to get started. You can also set breakpoints in your program and use the full functionality of the VS Code debugger.

### Create a Launch Configuration

For more control, you can create a customized launch configuration:

1. Click the gear icon when selecting an automatic debug configuration to customize it.
2. Alternatively, create a `launch.json` file and use a configuration template.

![Launch Configuration](/iac-launch-configuration.png)

You can run without debugging by selecting "Run Without Debugging" from the Run menu or by adding `"noDebug": "true"` to your configuration.

![Debugging](/iac-debugging.png)

## Using Pulumi ESC

Manage your Pulumi ESC environments directly within VS Code using the ESC Explorer.

### Open the ESC Explorer

From the primary sidebar, open the "Pulumi ESC Explorer" view and click "Login" to authenticate to Pulumi Cloud. Once logged in, you'll see a tree of your organizations and environments.

![Pulumi ESC Explorer](/explorer.png)

### Create, Edit, and Manage Environments

Easily create or edit environments by clicking the plus sign on an organization or project node. The extension opens an editor where you can define and save new environment revisions. The IntelliSense functionality will guide you on various values, such as completion for setting up provider configuration.

![Add ESC Environment](/add-env.png)

You can also:

- Run your application in the context of your environment by hovering over it and selecting the terminal icon
- Delete environments by hovering over them and selecting the delete icon
- Decrypt environments for cloning or moving
- View environment versions over time
- Compare different environments or environment versions
- Use the search icon to quickly find environments
- Tag specific environment revisions for easy reference.

![Delete ESC Environment](/delete-env.png)

## Pulumi YAML Support

The Pulumi VS Code Extension enhances YAML development for Pulumi, providing features that streamline the editing and validation process.

### Existing Capabilities

#### Warnings and Errors

The Pulumi Language Server Protocol (LSP) provides contextual warnings and errors directly within the editor:

- Warnings: Alerts when a variable is defined but never referenced.
- Errors:
  - Invalid YAML document detection.
  - Reference errors for non-existent variables.
  - Duplicate names for variables/resources.

#### On Hover

Hover over a resource type token or function type token to see a popup with descriptions, helping you understand your resources and functions better.

#### Completion

Experience semantic completion for:

- Predefined Pulumi YAML keys such as "resources" or "properties".
- Resource properties or function arguments.
- Type tokens for resources or functions.
- Structured variables (e.g., referencing properties within complex objects).

## Wrapping up

This extension is currently in public beta, and we're eager to hear from the Pulumi community. Your feedback is crucial in helping us shape the future of the extension. If you have suggestions for new features or encounter any bugs, please [open an issue](https://github.com/pulumi/pulumi-vscode-tools/issues).

### What's Next

We're committed to making Pulumi development as efficient and enjoyable as possible. In the coming months, expect even more features and improvements, all aimed at helping you work smarter and faster. Stay tuned for updates as we continue to build out this powerful extension and bring new capabilities to the Pulumi platform.