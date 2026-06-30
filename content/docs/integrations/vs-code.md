---
title: Pulumi VS Code Extension
title_tag: Pulumi VS Code Extension | Pulumi Integrations
h1: Pulumi VS Code Extension
meta_desc: Use the Pulumi VS Code extension to debug programs, get Pulumi YAML language support, and manage ESC environments without leaving your editor.
menu:
  integrations:
    name: VS Code
    identifier: integrations-vs-code
    parent: integrations-home
    weight: 3
aliases:
  - /docs/esc/integrations/vs-code/
  - /docs/esc/development/vs-code-extension/
---

The [Pulumi Tools extension for VS Code](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-tools) brings Pulumi's core capabilities directly into your editor. With it, you can:

- Run and debug Pulumi programs with the full VS Code debugger.
- Get Pulumi YAML language support, including type checking, hover tooltips, and completion.
- Create and manage Pulumi ESC environments, secrets, and configuration without leaving the IDE.

## Prerequisites

Before you begin, ensure you have the following:

- [Visual Studio Code](https://code.visualstudio.com/)
- The [Pulumi Tools extension for VS Code](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-tools)
- The [Pulumi CLI](/docs/install/) (version 3.132.0 or later) for debugging Pulumi programs
- A [Pulumi Cloud account](https://app.pulumi.com/signup) for managing ESC environments

## Installation

Install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-tools), or search for "Pulumi" in the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`) within VS Code. The extension supports both [single-folder workspaces](https://code.visualstudio.com/docs/editor/workspaces#_singlefolder-workspaces) and [multi-root workspaces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces).

## Debugging Pulumi programs

The extension lets you launch and debug Pulumi programs with breakpoints and the full functionality of the VS Code debugger. It automatically generates debug configurations to run `pulumi up` or `pulumi preview` for the current stack, and you can also create a custom `launch.json` configuration.

For step-by-step instructions, see [Attaching a debugger to a Pulumi program](/docs/iac/operations/debugging/debugger-attachment/).

## Pulumi YAML language support

Along with the many programming languages Pulumi supports, you can also define infrastructure using [Pulumi YAML](/docs/iac/languages-sdks/yaml/). The extension provides rich editing support for this YAML dialect, built on the [Pulumi YAML Language Server Protocol (LSP)](https://github.com/pulumi/pulumi-lsp), which is available for use in any IDE.

### Type checking

The Pulumi YAML LSP provides contextual warnings and errors directly within the editor:

- Warnings when a variable is defined but never referenced.
- Errors for invalid YAML documents.
- Reference errors for non-existent variables.

### Hover tooltips

Hover over a resource type token or function type token to see a popup with its description, helping you understand your resources and functions.

### Completion lists

The extension offers semantic completion for:

- Predefined Pulumi YAML keys, such as `resources` or `properties`.
- Resource properties and function arguments.
- Type tokens for resources and functions.
- Structured variables, such as references to properties within complex objects.

## Managing ESC environments

The extension lets you manage your [Pulumi ESC](/docs/esc/) environments without leaving VS Code. From the primary sidebar, open the **Pulumi ESC Explorer** view and select **login** to authenticate to Pulumi Cloud. Once logged in, you will see a tree of your organizations and their environments.

### Create and edit environments

Select the **plus (+) icon** next to an organization to create a new project and environment, or next to a project to add an environment to it. Select an existing environment in the tree to open it in the editor, where you get completion, error checking, and other IDE features. Each time you save, the extension creates a new environment revision, giving you version control over your changes. Expand an environment node to browse its revisions, and use the **tag** icon on a revision to label it.

You can also hover over an environment in the Explorer to delete it, generate a `pulumi env run` command in the terminal, or search and refresh the tree from the icons at the top of the view.

### Open vs. decrypt an environment

These are two distinct operations:

- **Open** (the **Preview** button, top-right of the editor) fully resolves the environment: it decrypts secrets, invokes dynamic providers, and expands all configuration values into your chosen output format.
- **Decrypt** (the **decrypt** icon shown on hover) only unlocks the stored secrets without resolving providers or interpolations, which is useful when moving or cloning environments with their secrets intact.

### Code navigation and comparison

The editor supports **Go to Definition** and **Find all References** across symbols, interpolations, and values. To diff two environments or revisions, right-click (or control-click) the first node and choose **Select for compare**, then right-click another node and choose **Compare with selected**.
