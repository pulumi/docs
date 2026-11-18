---
title: Prepare pull requests
title_tag: Prepare pull requests | Pulumi Agents
h1: Prepare pull requests
meta_desc: Have an agent open a pull request in your connected repository and push revisions from the same task.
aliases:
- /docs/ai/concepts/neo/pull-requests/
- /docs/pulumi-cloud/neo/pull-requests/
- /docs/iac/neo/pull-requests/
- /docs/ai/pull-requests/
- /docs/ai/neo/pull-requests/
menu:
    ai:
        name: Prepare pull requests
        parent: ai-agents-review
        weight: 20
        identifier: ai-pull-requests
---

An agent can open a pull request in a connected repository and push revisions to it from the same task.

## Before you begin {#prerequisites}

### Connect version control {#vcs-integration}

Connect the repository through a [version control integration](/docs/ai/agents/integrations/#repositories). Pulumi supports pull requests through [GitHub](/docs/integrations/version-control/github-app/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), [GitLab](/docs/integrations/version-control/gitlab/), and [Bitbucket](/docs/integrations/version-control/bitbucket/).

[Custom VCS](/docs/integrations/version-control/custom-vcs/) connections support cloning and pushing code, but do not support opening pull requests.

### Identify the repository {#code-access}

Include the repository URL in your request. For a task attached to a stack, the agent can also use the stack's Git metadata tags to locate its source repository. The version control integration must have access to that repository.

<span id="cicd-integration"></span>

## Open a pull request {#pull-requests}

1. In the task where the agent prepared the change, ask it to open a pull request.
1. If the task's [approval mode](/docs/ai/agents/permissions/#separate-approvals-from-access) requires confirmation, approve the request.
1. Follow the pull-request link in the task to review the diff and your repository's checks.

The pull request describes the change and links back to the task. Reviewers need [access to the task](/docs/ai/agents/permissions/#give-teammates-access) to read that conversation. For a Neo task, [enable link sharing](/docs/ai/agents/tasks/#ownership-and-sharing) if reviewers in your organization need access.

## Request revisions {#requesting-changes}

Reply in the same task with the changes you want. The agent can push revisions to the existing pull request. Follow [Review proposed changes](/docs/ai/agents/review-changes/) for reviewing and merging the change.
