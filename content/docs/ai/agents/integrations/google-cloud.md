---
title: Connect Google Cloud
title_tag: Connect Google Cloud | Pulumi Agents
h1: Connect Google Cloud
meta_desc: Connect Google Cloud to Pulumi Agents using credentials managed by Pulumi ESC.
menu:
    ai:
        name: Google Cloud
        parent: ai-integrations-cli
        weight: 11
---

Connect Google Cloud so an agent can use the `gcloud` CLI with credentials from Pulumi ESC.

## Choose the service account

Use a service account with access to the projects and resources the agent needs. Grant only the actions required for its work. See [Design access around the job](/docs/ai/agents/permissions/#design-access-around-the-job) for guidance on credential scope and lifecycle.

## Prepare an ESC environment

Use the [Google Cloud login provider](/docs/esc/providers/login/gcp-login/) to obtain a temporary access token. Under [environmentVariables](/docs/esc/concepts/outputs/#environmentvariables), export its `accessToken` output as `CLOUDSDK_AUTH_ACCESS_TOKEN`. Set `CLOUDSDK_CORE_PROJECT` to the project ID the agent should use. The login provider's example shows the complete `gcloud` configuration.

The agent also needs [permission to open the environment](/docs/ai/agents/permissions/#scope-pulumi-cloud-access).

## Connect the environment

As an organization administrator:

{{% agent-cli-connection tool="Google Cloud" %}}

Give the connection a name that identifies its purpose, such as `staging-google-cloud`. Include the project ID and any region or zone restrictions in its notes.

## Use the connection

In the task, name the connection and identify the project and resources the agent should work with. See [Tasks and collaboration](/docs/ai/agents/tasks/) to assign work and review the results.
