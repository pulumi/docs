---
title: Run previews
title_tag: Run previews | Pulumi Agents
h1: Run previews
meta_desc: Run a Pulumi preview in an agent task and resolve repository, configuration, or credential errors.
aliases:
- /docs/ai/concepts/neo/previews/
- /docs/pulumi-cloud/neo/running-previews/
- /docs/iac/neo/running-previews/
- /docs/ai/running-previews/
- /docs/ai/neo/running-previews/
menu:
    ai:
        name: Run previews
        parent: ai-agents-review
        weight: 10
        identifier: ai-running-previews
---

Ask an agent to run a [Pulumi preview](/docs/iac/cli/commands/pulumi_preview/) to see how its code changes would affect a stack. The preview runs the program and reports planned resource changes without applying them.

## Before you begin {#prerequisites}

<span id="configuration-and-credentials"></span>
<span id="stack-config"></span>
<span id="esc-stack-association"></span>

The agent needs the same program, configuration, and credentials that a preview requires from your terminal or CI workflow:

1. [Connect the repository](/docs/ai/agents/integrations/#repositories) containing the program. For a local CLI or editor session, open the project directory instead.
1. Supply the program's configuration through [stack configuration](/docs/iac/concepts/config/) or an imported [Pulumi ESC environment](/docs/esc/guides/pulumi-iac/).
1. Configure credentials for the program's cloud providers, such as [AWS](/registry/packages/aws/installation-configuration/), [Azure](/registry/packages/azure-native/installation-configuration/), or [Google Cloud](/registry/packages/gcp/installation-configuration/).

If you use ESC, associate the environment with the stack and grant the agent access to open it. An agent your team creates uses its assigned Pulumi Cloud role; Neo uses your permissions by default. See [Permissions and approvals](/docs/ai/agents/permissions/) for access requirements.

## Run a preview {#using-previews}

<span id="preview-workflow"></span>

1. In the task where the agent prepared the code change, ask it to run a preview. Specify the stack if the task involves more than one.
1. If the task's [approval mode](/docs/ai/agents/permissions/#separate-approvals-from-access) requires confirmation, approve the preview request.
1. Open the preview output in the task.

<span id="best-practices"></span>
<span id="always-preview-before-merging"></span>
<span id="preview-output"></span>
<span id="review-preview-output-carefully"></span>
<span id="policy-compliance-checking"></span>

Follow [Review proposed changes](/docs/ai/agents/review-changes/#check-the-code-and-preview) to assess the resource changes, policy results, and failed checks.

## Troubleshooting

### Missing or invalid credentials

Use the preview error to identify the provider or configuration value that failed. If the credentials come from ESC:

1. Check that the environment supplies the credentials the program requires.
1. Open the stack details page and confirm that the environment is associated with the stack.
1. Check that the agent can open the environment and that the credentials allow the required cloud operations.
1. Correct the configuration or access, then ask the agent to run the preview again.

<span id="security-considerations"></span>
