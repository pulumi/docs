---
title_tag: "Environment Variables | Pulumi Deployments"
meta_desc: The environment variables Pulumi Deployments sets automatically, and how to define and persist your own
title: "Environment Variables"
h1: "Environment Variables"
menu:
  deployments:
    name: Environment Variables
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-environment-variables
    weight: 100
---

By default, there are a set of environment variables set by the process automatically:

- `GITHUB_TOKEN`: A GitHub access token, set automatically when the deployment's source is a GitHub repository. When the source is connected through the [Pulumi GitHub App](/docs/integrations/version-control/github-app/#github-token-in-deployments), this is a short-lived app installation token scoped to your whole GitHub App installation, not just the source repository; when you configure the source with your own personal access token, that token is used instead. Not set if you provide your own `GITHUB_TOKEN` through custom environment variables. See [GitHub token in deployments](/docs/integrations/version-control/github-app/#github-token-in-deployments) for scope and security details.
- `PULUMI_ACCESS_TOKEN`: A temporary token with read-write access only to the stack being deployed.
- `PULUMI_DEPLOY_OIDC_CONFIG`: OIDC configuration provided for the cloud integrations
- `PULUMI_CI_SYSTEM`: "Pulumi Deployments"
- `PULUMI_CI_BUILD_ID`: Current deployment ID
- `PULUMI_CI_BUILD_NUMBER`: Current deployment version
- `PULUMI_CI_BUILD_URL`: Current deployment URL
- `PULUMI_CI_ORGANIZATION`: Current account organization
- `PULUMI_CI_PROJECT`: Current project name
- `PULUMI_CI_STACK`: Current stack name
- `PULUMI_CI_OPERATION`: Current Pulumi operation (`update`, `preview`, `destroy`, `refresh`, `detect-drift`, or `remediate-drift`)

These can be overridden or extended by configuring custom environment variables.

## PULUMI_ENV

Environment variables can be persisted between pre-run commands and the final pulumi deployment by appending them to the file on the file system named `PULUMI_ENV`.

Example Usage:

```bash
export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
echo GOOGLE_OAUTH_ACCESS_TOKEN=$GOOGLE_OAUTH_ACCESS_TOKEN >> /PULUMI_ENV
```

Running `env` in a subsequent pre-run command will show the environment variable and it should be usable by scripts or your pulumi program.
{{% notes type="info" %}}
If `/PULUMI_ENV` does not work, and you are on self hosted, you can look for the following message in the logs to get the location: `Loading PULUMI_ENV from`.
{{% /notes %}}
