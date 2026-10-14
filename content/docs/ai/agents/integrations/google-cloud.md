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

The Google Cloud CLI integration expects an ESC environment that supplies a service account key file through `GOOGLE_APPLICATION_CREDENTIALS`. Use ESC's [files output](/docs/esc/concepts/outputs/#files) to write the stored key to a temporary file when the task runs. Set `CLOUDSDK_CORE_PROJECT` under [environmentVariables](/docs/esc/concepts/outputs/#environmentvariables) to the project ID the agent should use.

The agent also needs [permission to open the environment](/docs/ai/agents/permissions/#scope-pulumi-cloud-access).

## Connect the environment

As an organization administrator:

{{% agent-cli-connection tool="Google Cloud" %}}

Give the connection a name that identifies its purpose, such as `staging-google-cloud`. Include the project ID and any region or zone restrictions in its notes.

## Use the connection

Select the connection in the task composer's **CLI integrations** menu. In the task, identify the project and resources the agent should work with. See [Tasks and collaboration](/docs/ai/agents/tasks/) to assign work and review the results.
