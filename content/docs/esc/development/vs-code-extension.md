---
title: ESC VS Code Extension
title_tag: Using Pulumi ESC with VS Code | Pulumi ESC
h1: Using Pulumi ESC with VS Code
meta_desc: Pulumi This page provides an overview on how to use the Pulumi VS Code extension to manage your Pulumi Environments, Secrets, and Configuration
menu:
  esc:
    parent: esc-development
    weight: 2
---

The [Pulumi Tools extension for VS Code](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode) allows you to manage your Pulumi ESC environments directly from your editor. This enables you to create and manage environments, secrets and configuration directly within the IDE with rich IDE features.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Pulumi Tools extension for VS Code](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode)
- A [Pulumi Cloud account](https://app.pulumi.com)

## Getting Started with Pulumi ESC in VS Code

The Visual Studio Code Pulumi Tools extension lets you manage your ESC without having to leave VS Code.

## Open the ESC Explorer

From the primary sidebar, open the **Pulumi ESC Explorer** view, and click **login** to authenticate to Pulumi Cloud.

![Pulumi ESC Explorer](/docs/esc/assets/esc-explorer.png)

Once logged in, you will see a tree of your organizations and, within each organization, your ESC environments.

## Create a project and environment

To create a new ESC project and environment:

1. In the ESC Explorer, locate your **organization**
2. Click the **plus (+) icon** next to your org
3. Enter a name for your project and environment

The extension will open up an editor with an example environment definition you can then edit.

## Create an environment in an existing project

To create a new ESC within an existing project:

1. In the ESC Explorer, locate your **organization** and **project**
2. Click the **plus (+) icon** next to your project
3. Enter a name for environment

## Edit an existing environment

To edit an existing environment:

1. Click on an **environment** in the ESC Explorer tree
2. Make your changes in the editor
3. Save the file to create a new revision of the environment

Each time you save changes to an environment, a new revision is created. Revisions provide version control for your environments, allowing you to track changes over time and revert to previous versions if needed. You can view all revisions of an environment by expanding the environment node in the ESC Explorer.

## Opening an environment

When you `open` an environment in Pulumi ESC, we will decrypt any secrets, invoke any dynamic providers, and resolve all configuration values. This lets you view the fully resolved environment with all variables expanded and secrets decrypted in your chosen output format.

To open and preview an environment:

1. Select an environment in the editor
2. Click the **Preview** button in the editor's top-right corner
3. Select your desired output format when prompted

![Pulumi ESC Explorer - open an environment](/docs/esc/assets/esc-vscode-add-env.png)

## Decrypting an environment

Decryption is the process of unlocking the encrypted secrets within an environment without performing a full environment opening operation. This is particularly useful when you need to:

- Move environment data between projects or organizations
- Clone environments with their secrets intact

To decrypt an environment:

1. Hover over the environment in the ESC Explorer
2. Click the **decrypt** icon that appears to the right

![Pulumi ESC Explorer - decrypt an environment](/docs/esc/assets/esc-vscode-decrypt-env.png)

## Deleting an environment

To delete an environment:

1. Hover over the environment in the ESC Explorer
2. Click the **delete** (trash) icon that appears
3. Confirm the deletion by entering the environment name when prompted

![Pulumi ESC Explorer - deleting an environment](/docs/esc/assets/esc-vscode-delete-env.png)

## Refreshing environments

The extension automatically refreshes after changes, but you can manually refresh by:

1. Clicking the refresh icon at the top right of the ESC Explorer tree view

![Pulumi ESC Explorer - refresh an environment](/docs/esc/assets/esc-vscode-refresh.png)

## Searching environments

To search for specific environments:

1. Click the search icon in the top right of the ESC Explorer
2. Type your search term
3. View results in the panel that appears

![Pulumi ESC Explorer - search an environment](/docs/esc/assets/esc-vscode-search.png)

## Tagging revisions

To tag a specific revision:

1. Locate the revision in the ESC Explorer, by clicking on the expand icon of your environment
2. Choose your revision and click the **tag** icon
3. Enter a name for the tag

![Pulumi ESC Explorer - tag revisions](/docs/esc/assets/esc-vscode-tag-revision.png)

## Running ESC commands in the terminal

You can quickly generate ESC Run commands for execution in the terminal:

1. Hover over the environment in the ESC Explorer
2. Click the **Add to terminal** icon that appears
3. The appropriate command will be populated in your terminal

![Pulumi ESC Explorer - run commands](/docs/esc/assets/esc-vscode-run.png)

## Go to definition/find all references

The extension supports standard code navigation features:

- **Go to Definition**: Quickly navigate to symbol definitions
- **Find all References**: Locate all references to symbols, interpolations, and values

## Comparing Environments and Revisions

To compare two environments or revisions:

1. Right-click (or control-click) the first node to compare
2. Choose **Select for compare**
3. Right-click (or control-click) on another node
4. Select **Compare with selected**
