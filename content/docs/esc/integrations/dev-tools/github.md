---
title_tag: GitHub Integration | Pulumi ESC
title: GitHub
h1: "Pulumi ESC GitHub Action"
meta_desc: This page provides an overview of how to use Pulumi ESC with GitHub.
weight: 3
menu:
  esc:
    identifier: esc-dev-tools-integrations-github
    parent: esc-dev-tools-integrations
---

## Pulumi ESC GitHub Action

The [Pulumi ESC GitHub Action](https://github.com/marketplace/actions/esc-action) allows you to run ESC commands in your GitHub Actions workflows or inject secrets and configuration into your GitHub Actions workflows.

- Minimally, the GitHub action will download the Pulumi ESC CLI. If a `version` is specified, that version will be downloaded.
- Optionally, if an `environment` is passed in as an input, the action will inject all environment variables (specifically the keys under `values.environmentVariables` and projected files under `values.files`) from the environment into the current action/workflow environment.
- If specific keys are passed in using the `keys` input - only those keys will be injected into the GitHub Workflow.

### Example

This example shows how to inject all environment variables from the `tinyco/someProject/myEnv` environment into the GitHub Workflow from where it is called.

It is recommended to use the [pulumi/auth-actions](https://github.com/marketplace/actions/pulumi-auth-action) GitHub Action to authenticate with Pulumi Cloud to avoid having to use a long-lived access token in your workflow. The `pulumi/auth-actions` action will authenticate with Pulumi Cloud and generate a short-lived token and set it as the `PULUMI_ACCESS_TOKEN` environment variable.

```yaml
on:
  - pull_request

permissions:
  id-token: write
  contents: read

jobs:
  test-all-key-injection:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: pulumi
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Install and inject ESC environment variables
        uses: pulumi/esc-action@v1
        with:
          environment: 'tinyco/someProject/myEnv'
      - name: Verify environment variables were injected
        run: |
          echo "Testing env injection..."
          echo "FOO=$FOO"
          echo "SOME_IMPORTANT_KEY=$SOME_IMPORTANT_KEY"
          echo "TEST_ENV=$TEST_ENV"
```

### Use Cases

- **Injecting secrets into GitHub Actions**: The GitHub Action can be used to inject secrets into GitHub Actions workflows, allowing you to dynamically access your secrets from ESC as they are needed, rather than storing them in GitHub Secrets as long-lived static secrets. This allows you to leverage many of ESC's key features, such as automatic secret rotation and short-lived dynamic credentials and secrets and prevents secret sprawl.
- **Running ESC commands in GitHub Actions**: The GitHub Action can be used to run any arbitrary ESC commands in GitHub Actions workflows, beyond just injecting secrets. This allows you to use ESC as part of your CI/CD pipeline and create, update, or open environments automatically as part of your workflow.

## Importing secrets from GitHub Actions

If you have existing secrets in GitHub that you would like to import into ESC, you can run a one-time GitHub Action workflow like the following:

```yaml
name: Export secrets to ESC

on:
  - workflow_dispatch

permissions:
  id-token: write
  contents: read

jobs:
  export-to-esc:
    runs-on: ubuntu-latest
    name: Export GitHub secrets to ESC
    steps:
      - name: Install ESC CLI
        uses: pulumi/esc-action@v1
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: pulumi
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Export secrets to ESC
        run: |
          esc env get $ESC_ENVIRONMENT || esc env init $ESC_ENVIRONMENT
          echo "$GITHUB_SECRETS" | python3 -c 'import sys, yaml, json; j=json.loads(sys.stdin.read()); print(yaml.safe_dump({"values": {"environmentVariables": {name: {"fn::secret": value} for (name, value) in j.items() if name != "github_token"}}}))' | esc env edit $ESC_ENVIRONMENT -f -
        shell: bash
        env:
          ESC_ENVIRONMENT: myorg/myproject/myenvironment
          GITHUB_SECRETS: ${{ toJSON(secrets) }}
```

This workflow will export all GitHub secrets available to that repository into the specified ESC environment. You can run this workflow manually from the GitHub Actions UI.
