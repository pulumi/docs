---
title: Publishing Components from GitHub Actions
title_tag: Publishing Pulumi Components from GitHub Actions to Private Registry
h1: Publishing Components from GitHub Actions
meta_desc: Learn how to set up automated publishing of Pulumi components from GitHub Actions to your Pulumi Cloud private registry.
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
  - /docs/idp/concepts/publishing-from-github-actions/
  - /docs/idp/get-started/publishing-from-github-actions/
menu:
  idp:
    parent: idp-guides
    identifier: idp-guides-publishing-github-actions
    weight: 20
---

Automating the publication of Pulumi components from GitHub Actions to your Pulumi Cloud private registry enables robust CI/CD workflows for infrastructure building blocks.
This guide walks through setting up automated testing and publishing workflows that ensure quality while maintaining fast iteration cycles.

## Prerequisites

- A Pulumi component authored and working locally (see [Build a Component](/docs/iac/using-pulumi/build-a-component))
- A [GitHub repository](https://github.com/pulumi-labs/pulumi-component-lifecycle-example) containing your component code
- Access to a [Pulumi Cloud private registry](/docs/idp/concepts/private-registry)
- Configure Pulumi and GitHub integrations: [OIDC](/docs/administration/access-identity/oidc-client/github/), [GitHub App](/docs/iac/using-pulumi/continuous-delivery/github-app/), etc.
- Component [documentation](https://github.com/pulumi-labs/pulumi-component-lifecycle-example#static-page-component) written and committed to your repository

## Development Workflow Overview

The recommended workflow for developing and publishing components follows these stages:

1. **Local Development**: Author your component using a [local development workflow](/docs/iac/using-pulumi/build-a-component)
2. **Repository Setup**: Create a [GitHub repository](https://github.com/pulumi-labs/pulumi-component-lifecycle-example) with proper documentation
3. **Testing Infrastructure**: Write [comprehensive unit and integration tests](/docs/iac/concepts/components/testing-components)
4. **Automated Testing**: Set up [GitHub Actions](https://github.com/pulumi-labs/pulumi-component-lifecycle-example/tree/main/.github/workflows/test.yml) for continuous testing
5. **Versioned Releases**: Create semantic [versioned releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) on GitHub
6. **Automated Publishing**: Automate the [release and publishing](https://github.com/pulumi-labs/pulumi-component-lifecycle-example/tree/main/.github/workflows/release.yml) process

## Repository Structure

Organize your component repository with the following structure:

```
my-component/
├── README.md                   # Component documentation
├── PulumiPlugin.yaml           # Runtime specification
├── Makefile                    # Build and test commands
├── tests/                      # Test directory
│   ├── unit/                   # Unit tests (language-specific)
│   └── integration/            # Integration tests
├── examples/                   # Usage examples
└── .github/
    └── workflows/
        ├── test.yml            # Test workflow
        └── release.yml         # Release workflow
```

We recommend *one component per repository*, rather than a single repository for all your components. That allows you to version and release each component separately. In some cases, it may make sense to package a few highly correlated components together in the same repository, but this should be done with caution using integration tests between the components.

## Example Component Repository

For the purposes of this documentation, please refer to the [example component repository](https://github.com/pulumi-labs/pulumi-component-lifecycle-example). This GitHub repo contains the component code, tests, and GitHub Actions described here. If you'd like to follow along, pull this repo locally as a reference.

### Create a Makefile

We recommend that you create a `Makefile` to standardize your build and test commands. This example `Makefile` shows how to set up some basic commands like `make build` and `make test`, which can run the various tasks for you. Since the component in our example is written using Go, we use `go build` and `go test` to build and run unit tests. For integration tests, we use a local workbench that runs `pulumi preview` to validate the component end-to-end.

```makefile
# ./Makefile
.PHONY: test unit-test integration-test build clean

# Run all tests
test: unit-test integration-test

# Run unit tests
unit-test:
	@echo "Running unit tests..."
	go test

# Run integration tests with pulumi preview
integration-test:
	@echo "Running integration tests..."

	PULUMI_CONFIG_PASSPHRASE="foo" pulumi login --local;
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi install;
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi cancel --stack organization/static-page-integration-test/dev --yes;
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi destroy --stack organization/static-page-integration-test/dev --yes --refresh --remove;
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi -C tests/integration stack init organization/static-page-integration-test/dev --non-interactive;
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi -C tests/integration stack select organization/static-page-integration-test/dev;
	-PULUMI_CONFIG_PASSPHRASE="foo" pulumi -C tests/integration config set aws:region us-west-2;
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi -C tests/integration package add ../..;
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi -C tests/integration preview;
	PULUMI_CONFIG_PASSPHRASE="foo" pulumi logout --local;
	rm tests/integration/Pulumi.dev.yaml

# Build the component
build:
	@echo "Building component..."
	go build

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm static-page-component
```

## Testing Your Component

### Unit Tests

Write unit tests that validate your component's logic without creating cloud resources by using the `integration` library from the [Pulumi Provider SDK](/docs/iac/guides/building-extending/providers/pulumi-provider-sdk/). Here we can set up a mock provider server to catch calls for resource creation and return mock resources back.

```go
// ./main_test.go
package main

import (
    "testing"

    "github.com/blang/semver"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/require"

    p "github.com/pulumi/pulumi-go-provider"
    "github.com/pulumi/pulumi-go-provider/infer"
    "github.com/pulumi/pulumi-go-provider/integration"
    "github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
    "github.com/pulumi/pulumi/sdk/v3/go/property"
)

func TestConstruct(t * testing.T) {

    // Configure Mocks: The provider is roughly the same as in our main.go
    myProvider, err: = infer.NewProviderBuilder().
    WithNamespace("example").
    WithComponents(
        infer.ComponentF(NewStaticPage),
    ).
    WithModuleMap(map[tokens.ModuleName] tokens.ModuleName {
        "static-page-component": "index",
    }).
    Build()
    require.NoError(t, err)

    // Configure Mocks: The Server catches calls to create resources, and returns mock resources instead.
    server, err: = integration.NewServer(
        t.Context(),
        "example",
        semver.MustParse("0.1.0"),
        integration.WithProvider(myProvider),
        integration.WithMocks( & integration.MockResourceMonitor {
            NewResourceF: func(args integration.MockResourceArgs)(string, property.Map, error) {
                // NewResourceF is called as the each resource is registered
                switch {
                    case args.TypeToken == "aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2":
                        assert.Equal(t, args.Name, "test-static-page-website")
                        return args.Name, property.NewMap(map[string] property.Value {
                            "websiteEndpoint": property.New("http://pulumi.com"),
                        }), nil
                }
                return "", property.Map {}, nil
            },
        }),
    )
    require.NoError(t, err)

    // test the "static-page-component:index:StaticPage" component
    // We try to construct a StaticPage component named "test-static-page"
    // The mock will set the endpoint value
    resp, err: = server.Construct(p.ConstructRequest {
        Urn: "urn:pulumi:stack::project::static-page-component:index:StaticPage::test-static-page",
        Inputs: property.NewMap(map[string] property.Value {
            "indexContent": property.New("test content"),
        }),
    })
    require.NoError(t, err)
        // check that we got the correct output. If something was broken then we'd never get the call
        // to create the BucketWebsiteConfigurationV2 object, and thus, never get this mock value back
    require.Equal(t, property.NewMap(map[string] property.Value {
        "endpoint": property.New("http://pulumi.com"),
    }), resp.State)
}
```

Run the unit tests using `go test`:

```bash
$ go test
```

or if you have the `Makefile` set up already:

```bash
$ make unit-test
```

### Integration Tests

For integration tests, set up a small local test workbench using a YAML Pulumi program. Then you can use `pulumi preview` to validate resource creation:

```yaml
# ./tests/integration/Pulumi.yaml
name: static-page-integration-test
description: A minimal Pulumi YAML program
runtime: yaml
packages:
  static-page-component: ../..
resources:
  my-static-page:
    type: static-page-component:StaticPage
    properties:
      indexContent: "test content"
outputs:
  endpoint: ${my-static-page.endpoint}
```

Run integration tests with:

```bash
$ cd tests/integration
$ pulumi preview
```

or if you have the `Makefile` set up already:

```bash
$ make integration-test
```

## GitHub Actions Setup

### Test Workflow

Before we publish, we need to be able to validate our code in an automated fashion. For that, we will set up a test workflow in GitHub Actions.

Create `.github/workflows/test.yml` for continuous testing:

```yaml
# ./.github/workflows/test.yml
name: Test Workflow

on:
  pull_request: # Trigger on a PR
  workflow_dispatch: # Allows manual triggering of the workflow

jobs:
  integration-test:
    permissions:
      id-token: write
      contents: read

    runs-on: ubuntu-latest

    ### Set variables for the action.
    env:
      PULUMI_ORG: 'pulumi' # Your Pulumi organization

    steps:
      - uses: actions/checkout@v4
      - name: Authenticate to Pulumi
        uses: pulumi/auth-actions@v1
        with:
          organization: ${{ env.PULUMI_ORG }}
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-region: us-west-2
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      - name: Run Preview
        uses: pulumi/actions@v6
        with:
          command: preview
          work-dir: tests/integration
          stack-name: ${{ env.PULUMI_ORG }}/static-page-integration-test/dev
          upsert: true

  unit-test:
    permissions:
      id-token: write
      contents: read

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Setup Go ✨
        uses: actions/setup-go@v3
        with:
          go-version: '1.24'
      - name: Downloading dependencies 📦
        run: go mod download
      - name: Run Tests
        run: go test
```

In this workflow, we use some [Pulumi-specific GitHub Actions](/docs/iac/using-pulumi/continuous-delivery/github-actions/), as well as some off-the-shelf standard actions.

For the integration tests:

- [`actions/checkout`](https://github.com/actions/checkout) - check out the code into the Github runner
- [`pulumi/auth-actions`](https://github.com/pulumi/auth-actions) - authenticate with Pulumi Cloud (make sure to [setup GitHub OIDC](/docs/administration/access-identity/oidc-client/github/))
- [`aws-actions/configure-aws-credentials`](https://github.com/aws-actions/configure-aws-credentials) - set up AWS credentials
- [`pulumi/actions`](https://github.com/pulumi/actions) - Run a Pulumi command, in this case, `pulumi preview`

In the `pulumi/actions` step, we use one of [Pulumi's GitHub Actions](/docs/iac/using-pulumi/continuous-delivery/github-actions/) and configure it to run the `preview` command, change the root directory with `work-dir`, set the correct stack name by passing in the Pulumi organization name via the `env.PULUMI_ORG` variable we set earlier in the file, and configure `upsert` to make sure that the stack gets created if it doesn't exist yet, or updated if it does.

For the unit tests we also use [`actions/setup-go`](https://github.com/actions/setup-go) to install the Golang tooling. That sets us up to run `go mod download` to install our dependencies and `go test` to run the unit tests.

### Release and Publishing Workflow

Finally, we need some automation to cut a release and have it publish directly to your Pulumi private repository. Create `.github/workflows/release.yml` for automated publishing:

```yaml
# ./.github/workflows/release.yml
name: Release Workflow

on:
  push:
    tags:
      - '*' # Trigger on any tag push.
  workflow_dispatch: # Allows manual triggering of the workflow

jobs:
  distribute-release:
    permissions:
      id-token: write
      contents: read

    runs-on: ubuntu-latest

    ### Set variables for the action.
    env:
      PULUMI_ORG: 'pulumi' # The Pulumi organization to publish the component to.

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          ref: ${{ github.ref }} # Checkout the specific tag that triggered the workflow
          fetch-depth: 0 # Ensures the build matches the git tag.

      - name: Authenticate to Pulumi
        uses: pulumi/auth-actions@v1
        with:
          organization: ${{ env.PULUMI_ORG }}
          requested-token-type: urn:pulumi:token-type:access_token:organization
          scope: admin

      # Determine the version to use - either the triggered tag or latest tag for manual runs
      - name: Determine Component Version
        id: version
        run: |
          if [[ "${{ github.event_name }}" == "push" ]]; then
            # For tag pushes, use the tag that triggered the workflow
            VERSION="${{ github.ref_name }}"
            echo "Using triggered tag: $VERSION"
          else
            # For manual runs, get the latest tag
            VERSION=$(git tag --sort=-version:refname | head -1)
            echo "Manual run: Using latest tag: $VERSION"
          fi
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      # Publish if this is a tag push.
      - name: Publish Component to Private Registry
        if: github.event_name == 'push'
        run: |
          echo "Publishing latest component version to the ${{ env.PULUMI_ORG }} Pulumi org."
          pulumi package publish https://github.com/${{ github.repository }} --publisher ${{ env.PULUMI_ORG }}
```

This workflow will be automatically triggered any time a tag is pushed. The easiest way to do that is via the GitHub web-ui, by clicking on "Releases" then "Draft a new Release", which will give a form that includes a new semver tag, name of the release, and release notes. When the release is made it will push a tag to the repo, which will then trigger this workflow. It can also be run manually.

Similarly to the testing workflow, we use a mix of Pulumi-specific GitHub Actions, as well as some off-the-shelf standard actions:

- `actions/checkout@v4` - check out the code into the Github runner
- `pulumi/auth-actions@v1` - authenticate with Pulumi Cloud

However, `pulumi/actions` doesn't support the `publish` subcommand, so we set that step up manually via a `run` step. Use the `PULUMI_ORG` variable to set the `--publisher` and the GitHub Actions-internal `github.repository` variable to get the name of the repository.

## GitHub Actions Triggers

Now that we have these workflows in place, you could set up your automation in a variety of ways. Consider configuring your workflows with different triggers based on your team's needs:

### Test Workflow Triggers

- **On Push**: Test every commit to main branches
- **On Pull Request**: Test all proposed changes
- **Manual Dispatch**: Allow on-demand testing
- **Scheduled**: Daily tests to catch environmental issues
- **On Release**: Final validation before publishing

### Release Workflow Triggers

- **On Release Published**: Automatically publish when GitHub releases are created
- **Manual Dispatch**: Allow manual publishing with version specification
- **Multi-repo automation**: Coordinate releases by triggering the release workflow from another repo's action

For more details on GitHub Actions triggers, see the [GitHub Actions documentation](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).

## Workflow Status Notifications

Consider configuring notifications for workflow failures, like this YAML stanza that [notifies via Slack](https://github.com/marketplace/actions/slack-notify):

```yaml
jobs:
  slackNotification:
    name: Slack Notification
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Slack Notification
      uses: rtCamp/action-slack-notify@v2
      env:
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
```

## Next Steps

Once your automated publishing workflow is established, consider these enhancements:

- **Deployment Hooks**: Set up Pulumi Cloud [webhooks](/docs/deployments/deployments/using/triggers/#deployment-webhooks) to trigger deployments when new component versions are published
- **Version Compatibility Testing**: Test new versions against existing consumer programs
- **Progressive Rollouts**: Implement canary releases and blue/green deployments for high-impact components
- **Integration with Policies**: Create [Pulumi Policies](/docs/insights/policy/) policies that ensure only *approved* component versions are deployed

## Learn More

- [Build a Component](/docs/iac/using-pulumi/build-a-component)
- [Testing Components](/docs/iac/concepts/components/testing-components)
- [Private Registry](/docs/idp/concepts/private-registry)
- [GitHub Actions for Pulumi](/docs/iac/using-pulumi/continuous-delivery/github-actions)
- [Pulumi Deployments](/docs/pulumi-cloud/deployments)
