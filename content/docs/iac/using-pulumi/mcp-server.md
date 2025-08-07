---
title_tag: "Pulumi MCP Server | AI-Assisted Infrastructure as Code"
meta_desc: "Learn how to use Pulumi's Model Context Protocol (MCP) server to integrate AI assistants like Cursor, Claude Code, and GitHub Copilot with your Pulumi workflow."
title: MCP server
h1: Pulumi Model Context Protocol server
meta_image: /images/docs/meta-images/docs-meta.png
weight: 6
menu:
    iac:
        name: MCP server
        parent: iac-using-pulumi
        weight: 6
---

The Pulumi Model Context Protocol (MCP) server enables AI-powered coding assistants to help you codify cloud architectures and get diffs for infrastructure changes right in your development environment, much in the same way you already do for code changes thanks to Git. This integration ensures that as you build cloud applications, your infrastructure is repeatable and follows best practices and policies, while dramatically reducing context switching and accelerating Infrastructure as Code (IaC) development workflows.

## What is the Pulumi MCP server?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is a specification that allows language models to interact with external tools and data sources in a structured way. Pulumi's MCP server implementation provides AI assistants with the ability to:

- **Query the Pulumi Registry** for resource information, properties, and documentation
- **Execute Pulumi CLI commands** like `pulumi preview`, `pulumi up`, and `pulumi destroy`
- **Access stack outputs** and configuration values
- **Validate infrastructure code** before deployment
- **Catch and autofix IaC policy violations** using Pulumi's policy-as-code capabilities
- **Debug deployment issues** with real-time feedback

This enables a more intuitive, conversational approach to infrastructure development where you can describe what you want to build in natural language, and the AI assistant can discover resources, generate code, and manage deployments—all without leaving your editor.

## Supported AI assistants

The Pulumi MCP server works with various AI-powered development tools:

- **[Cursor](https://cursor.sh/)** - AI-first code editor
- **[Anthropic's Claude Code](https://claude.ai/code)** - AI assistant for coding
- **[GitHub Copilot](https://github.com/features/copilot)** - AI pair programmer
- **[Windsurf](https://codeium.com/windsurf)** - AI development environment
- Any other AI assistant that supports the Model Context Protocol

## Installation

The Pulumi MCP server is distributed as an npm package. You can install it globally or use it directly with `npx`:

```bash
# Install globally
npm install -g @pulumi/mcp-server

# Or use with npx (recommended)
npx @pulumi/mcp-server
```

## Configuration

### Cursor setup

To configure the Pulumi MCP server with Cursor, create a `mcp.json` file in the `.cursor` directory at your project root:

```json
{
    "mcpServers": {
        "pulumi": {
            "type": "stdio",
            "command": "npx",
            "args": ["@pulumi/mcp-server"]
        }
    }
}
```

After creating the configuration file:

1. Restart Cursor
2. Open the Cursor settings
3. Navigate to the MCP section to verify the connection status
4. The Pulumi MCP server should appear as connected

### Claude Code setup

For Claude Code, add the MCP server configuration to your Claude configuration file:

**On macOS/Linux:**
Add to `~/.config/claude/mcp_servers.json`:

```json
{
  "pulumi": {
    "command": "npx",
    "args": ["@pulumi/mcp-server"],
    "env": {}
  }
}
```

**On Windows:**
Add to `%APPDATA%\Claude\mcp_servers.json`:

```json
{
  "pulumi": {
    "command": "npx",
    "args": ["@pulumi/mcp-server"],
    "env": {}
  }
}
```

After adding the configuration:
1. Restart Claude Code
2. Verify the connection in the MCP section of Claude's settings
3. The Pulumi MCP server should appear as an available tool

### GitHub Copilot setup

GitHub Copilot's MCP support is available through compatible editors. Configure in your editor's MCP settings:

**VS Code with Copilot:**
Add to your VS Code settings.json:

```json
{
  "mcp.servers": {
    "pulumi": {
      "command": "npx",
      "args": ["@pulumi/mcp-server"],
      "type": "stdio"
    }
  }
}
```

**Other editors:**
Refer to your editor's specific MCP integration documentation for configuration details.

### Windsurf setup

In Windsurf, configure the MCP server through the IDE settings:

1. Open Windsurf settings
2. Navigate to MCP Servers section
3. Add a new server with the following configuration:

```json
{
  "name": "pulumi",
  "command": "npx",
  "args": ["@pulumi/mcp-server"],
  "type": "stdio"
}
```

## Available tools

The Pulumi MCP server provides several tools that AI assistants can use to interact with your Pulumi infrastructure:

### Registry tools

- **`pulumi-registry-get-type`** - Get the JSON schema for a specific JSON schema type reference.
- **`pulumi-registry-get-resource`** - Returns information about a Pulumi Registry resource.
- **`pulumi-registry-list-resources`** - List all resource types for a given provider and module.

### CLI tools

- **`pulumi-cli-preview`** - Run `pulumi preview` for a given project and stack.
- **`pulumi-cli-up`** - Run `pulumi up` for a given project and stack.
- **`pulumi-cli-refresh`** - Run `pulumi refresh` for a given project and stack.
- **`pulumi-cli-stack-output`** - Get the output value(s) of a given stack.

### Deployment tools

- **`deploy-to-aws`** - Automatically analyzes your application files and provisions the appropriate AWS resources (S3, Lambda, EC2, etc.) based on what it finds.

## Available prompts

The Pulumi MCP server also provides prompts that AI assistants can use for common workflows:

- **`deploy-to-aws`** - Deploy application code to AWS by generating Pulumi infrastructure
- **`convert-terraform-to-typescript`** - Converts a Terraform file to TypeScript. Takes an optional outputDir parameter for specifying where to output the TypeScript code.

## Getting started

Here's a typical workflow using an AI assistant with the Pulumi MCP server:

### 1. Initialize a new project

Start by asking your AI assistant to help set up a new Pulumi project:

> "Create a new Pulumi project in TypeScript for AWS infrastructure."

The assistant can guide you through project initialization and basic setup.

### 2. Describe your infrastructure needs

Use natural language to describe what you want to build:

> "I need an AWS S3 bucket with public read access for hosting a static website. Please look up the resource properties and create the code."

The AI assistant will:
- Use `pulumi-registry-list-resources` to find available AWS resources
- Use `pulumi-registry-get-resource` to get detailed S3 bucket property information
- Generate the appropriate TypeScript code

### 3. Validate and deploy

Ask the assistant to validate and deploy your infrastructure:

> "Please run a preview to check the changes, then deploy if everything looks good."

The assistant will:
- Use `pulumi-cli-preview` to show planned changes
- Use `pulumi-cli-up` to deploy the infrastructure
- Provide feedback on the deployment status

### 4. Manage and iterate

Continue working conversationally:

> "Add a CloudFront distribution in front of the S3 bucket and export the distribution URL."

The assistant can make incremental changes, validate them, and update your infrastructure.

## Examples

### Provisioning an AKS cluster

Here's an example interaction for creating an Azure Kubernetes Service cluster:

**You:** "I have an empty Pulumi project with TypeScript. Please provision an AKS cluster for a temporary experiment. Export its kubeconfig when done."

**AI Assistant response:**
1. Searches the Pulumi Registry for Azure container service resources
2. Retrieves detailed information about the `ManagedCluster` resource
3. Generates TypeScript code with appropriate configuration
4. Runs `pulumi-cli-preview` to validate the changes
5. Deploys with `pulumi-cli-up`
6. Retrieves the kubeconfig using `pulumi-cli-stack-output`

### Adding monitoring to existing infrastructure

**You:** "Add Application Insights monitoring to my existing Azure web app and configure alerts for high response times."

**AI Assistant response:**
1. Searches for Azure Application Insights resources
2. Generates code to create Application Insights instance
3. Links it to the existing web app
4. Configures alert rules
5. Previews and deploys the changes

## Benefits

Using the Pulumi MCP server with AI assistants provides several key advantages:

### Reduced context switching
- Stay in your editor instead of switching between documentation, CLI, and code
- Get real-time answers about resource properties and configurations
- Instant feedback on infrastructure changes

### Accelerated development
- Faster resource discovery through AI-powered search
- Automated code generation based on best practices
- Real-time validation and error detection

### Enhanced learning
- Learn Pulumi concepts through conversational interaction
- Understand resource relationships and dependencies
- Get explanations of complex infrastructure patterns

### Improved reliability
- Validate changes before deployment with integrated previews
- Catch configuration errors early in the development process
- Access to comprehensive Pulumi Registry information

## Troubleshooting

### MCP server not connecting

If your AI assistant can't connect to the Pulumi MCP server:

1. **Verify installation**: Ensure `@pulumi/mcp-server` is installed and accessible
2. **Check configuration**: Validate your `mcp.json` configuration file syntax
3. **Restart your editor**: Restart your AI assistant or editor application
4. **Check logs**: Look for error messages in your editor's console or logs

### Pulumi CLI commands failing

If CLI commands executed through the MCP server fail:

1. **Verify Pulumi installation**: Ensure Pulumi CLI is installed and in your PATH
2. **Check authentication**: Verify you're logged into Pulumi Cloud or have proper credentials
3. **Validate project**: Ensure you're in a valid Pulumi project directory
4. **Check stack selection**: Verify the correct stack is selected

### Missing registry information

If registry queries return incomplete information:

1. **Check network connectivity**: Ensure you can access the Pulumi Registry
2. **Update MCP server**: Use the latest version of `@pulumi/mcp-server`
3. **Clear cache**: Try clearing any local caches or restarting the MCP server

## Learn more

- [Pulumi MCP Server GitHub repository](https://github.com/pulumi/mcp-server)
- [AI-Assisted Infrastructure as Code blog post](/blog/mcp-server-ai-assistants/)
- [Model Context Protocol specification](https://modelcontextprotocol.io)
- [Pulumi Registry](/registry/)
- [Pulumi CLI reference](/docs/cli/)

## Next steps

Now that you have the Pulumi MCP server set up, explore these related topics:

- [Pulumi concepts](/docs/iac/concepts/) to understand core IaC principles
- [Getting started guides](/docs/iac/get-started/) for your preferred cloud provider
- [Automation API](/docs/iac/automation-api/) for programmatic infrastructure management
- [Continuous delivery](/docs/iac/using-pulumi/continuous-delivery/) for production deployments
