---
title: Instructions and context
title_tag: Instructions and context | Pulumi Agents
h1: Instructions and context
meta_desc: Set saved agent instructions, organization preferences, repository conventions, and the context for individual tasks.
aliases:
- /docs/ai/concepts/neo/instructions/
menu:
    ai:
        name: Instructions and context
        parent: ai-agents
        identifier: ai-instructions
        weight: 40
---

Use an agent's system prompt to set requirements for its work, such as which checks to run before opening a pull request. Put details that change between assignments, such as an incident's time window, in the task message. Keep repository build and test commands in the repository's `AGENTS.md` file.

Instructions guide the agent's work. They do not restrict the permissions of connected credentials or enforce a policy. Use [roles and credentials](/docs/ai/agents/permissions/) to control access.

## Instructions for an agent your team creates

Tasks assigned to an agent your team creates use its **System prompt**, including tasks started by a schedule or event. Include any team conventions it should follow in that field. See [Customize the instructions](/docs/ai/agents/configure/#customize-the-instructions) for an example system prompt.

## Organization instructions {#custom-instructions}

<span id="what-to-include"></span>
<span id="custom-instructions-best-practices"></span>

**Organization instructions** apply only to Neo. Agents your team creates do not inherit them, even if their **System prompt** is empty. Use this setting for conventions that Neo should follow across tasks, such as required resource tags.

### Example {#example}

```text
When proposing AWS infrastructure changes:
- Use {service}-{environment}-{region} for resource names.
- Include environment and owner tags.
- Check storage resources for encryption at rest.
- Include preview results in the pull request. If a preview cannot run,
  explain what prevented it and which changes remain unverified.
```

### Set organization instructions {#configuring-custom-instructions}

1. Open **Agent Settings** in Pulumi Cloud.
1. Select **Organization instructions**.
1. Enter the requirements for Neo tasks.
1. Save your changes.

### How instructions apply {#configuration-precedence}

Repository instructions add conventions for the codebase. Task messages provide details for the current assignment, but do not change the agent's saved configuration or grant additional access.

## Repository instructions {#repository-instructions}

<span id="how-it-works"></span>
<span id="example-1"></span>
<span id="repository-instructions-best-practices"></span>

Both Neo and agents your team creates are instructed to read applicable `AGENTS.md` files when they first inspect a repository and when working in a subdirectory. Keep project-specific setup, build, and test instructions in these files. Include the commands an agent needs to validate a change. For example:

```markdown
# Project instructions

## Setup
Run `npm ci` to install the dependencies in the lockfile.

## Validation
Run `npm test` and `npm run lint` before opening a pull request.
Include the results and explain any checks that could not run.

## Changes
Use TypeScript for new code. Keep changes limited to the assignment.
```

Adapt these commands to the repository. Instructions that name unavailable tools or obsolete commands can prevent the agent from validating its work.

### Instructions for subdirectories {#subdirectory-support}

An `AGENTS.md` file applies to its directory and all subdirectories. Add a nested file when part of the repository needs different commands or conventions. For files in that subtree, the nested instructions take precedence where they conflict with a parent file.

### Load repository context {#bootstrapping-repository-instructions}

[Connect the repository or tool](/docs/ai/agents/integrations/) that contains the instructions. Include the repository URL in the task and the path to any document the agent should read before starting.

## Context for an individual task

Identify the stack or repository, the result you want, and any constraints for this assignment. Put these details in the [task message](/docs/ai/agents/configure/#save-and-assign-a-task).
