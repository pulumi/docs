---
title: Publishing Components from GitHub Actions
title_tag: Publishing Pulumi Components from GitHub Actions to Private Registry
h1: Publishing Components from GitHub Actions
meta_desc: Learn how to set up automated publishing of Pulumi components from GitHub Actions to your Pulumi Cloud private registry.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  idp:
    parent: idp-get-started
    identifier: idp-publishing-github-actions
    weight: 6
---

Automating the publication of Pulumi components from GitHub Actions to your Pulumi Cloud private registry enables robust CI/CD workflows for infrastructure building blocks.
This guide walks through setting up automated testing and publishing workflows that ensure quality while maintaining fast iteration cycles.

## Prerequisites

Before setting up automated publishing, ensure you have:

- A Pulumi component authored and working locally (see [Build a Component]({{< relref "/docs/iac/using-pulumi/build-a-component" >}}))
- A GitHub repository containing your component code
- Access to a [Pulumi Cloud private registry]({{< relref "/docs/idp/get-started/private-registry" >}})
- Component documentation written and committed to your repository

## Development Workflow Overview

The recommended workflow for publishing components follows these stages:

1. **Local Development**: Author your component using a local development workflow
2. **Repository Setup**: Create a GitHub repository with proper documentation
3. **Testing Infrastructure**: Write comprehensive unit and integration tests
4. **Versioned Releases**: Create semantic versioned releases on GitHub
5. **Manual Validation**: Publish initial releases manually to validate the process
6. **Automated Testing**: Set up GitHub Actions for continuous testing
7. **Automated Publishing**: Automate the release and publishing process

## Setting Up Your Repository

### Repository Structure

Organize your component repository with the following structure:

```
my-component/
├── README.md                    # Component documentation
├── Pulumi.yaml                  # Component metadata
├── PulumiPlugin.yaml           # Runtime specification
├── Makefile                    # Build and test commands
├── tests/                      # Test directory
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
├── examples/                   # Usage examples
└── .github/
    └── workflows/
        ├── test.yml            # Test workflow
        └── release.yml         # Release workflow
```

### Create a Makefile

Create a `Makefile` that standardizes your build and test commands:

```makefile
.PHONY: test unit-test integration-test build clean

# Run all tests
test: unit-test integration-test

# Run unit tests
unit-test:
	@echo "Running unit tests..."
	# Add your unit test commands here
	# Example: pytest tests/unit/
	
# Run integration tests with pulumi preview
integration-test:
	@echo "Running integration tests..."
	cd tests/integration && pulumi preview --expect-no-changes
	
# Build the component
build:
	@echo "Building component..."
	pulumi package build

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf dist/
```

## Testing Your Component

### Unit Tests

Write unit tests that validate your component's logic without creating cloud resources:

```python
# tests/unit/test_component.py
import pytest
from my_component import MyComponent

def test_component_creation():
    # Test component instantiation
    component = MyComponent("test", {
        "param1": "value1",
        "param2": "value2"
    })
    assert component is not None
```

### Integration Tests

Create integration tests that use `pulumi preview` to validate resource creation:

```yaml
# tests/integration/Pulumi.yaml
name: integration-test
runtime: yaml
resources:
  testComponent:
    type: myorg:components:MyComponent
    properties:
      name: integration-test
      configuration:
        environment: test
```

Run integration tests with:

```bash
cd tests/integration
pulumi preview --expect-no-changes
```

### Policy Validation

Include policy pack validation in your tests to ensure compliance:

```bash
# In your Makefile or test script
pulumi preview --policy-pack ./policies
```

## GitHub Actions Setup

### Test Workflow

Create `.github/workflows/test.yml` for continuous testing:

```yaml
name: Test Component

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:  # Manual trigger
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Pulumi
      uses: pulumi/actions@v5
      with:
        pulumi-version: latest
        
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
        
    - name: Run Tests
      env:
        PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
      run: make test
      
    - name: Upload Test Results
      uses: actions/upload-artifact@v4
      if: always()
      with:
        name: test-results
        path: test-results/
```

### Release and Publishing Workflow

Create `.github/workflows/release.yml` for automated publishing:

```yaml
name: Release and Publish

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to publish'
        required: true
        type: string

jobs:
  publish:
    runs-on: ubuntu-latest
    if: github.event.release.prerelease == false
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Pulumi
      uses: pulumi/actions@v5
      with:
        pulumi-version: latest
        
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
        
    - name: Run Tests Before Publishing
      env:
        PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
      run: make test
      
    - name: Build Package
      run: make build
      
    - name: Publish to Private Registry
      env:
        PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
      run: |
        # Get version from release tag or workflow input
        VERSION=${GITHUB_REF#refs/tags/}
        if [ "${{ github.event_name }}" = "workflow_dispatch" ]; then
          VERSION="${{ github.event.inputs.version }}"
        fi
        
        # Publish to private registry
        pulumi publish \
          --org ${{ secrets.PULUMI_ORG }} \
          --private-registry \
          --version $VERSION
          
    - name: Create Release Notes
      if: github.event_name == 'release'
      run: |
        echo "Component ${{ github.repository }} version ${{ github.event.release.tag_name }} published successfully" >> $GITHUB_STEP_SUMMARY
```

## GitHub Actions Triggers

Configure your workflows with appropriate triggers based on your team's needs:

### Test Workflow Triggers

- **On Push**: Test every commit to main branches
- **On Pull Request**: Test all proposed changes
- **Manual Dispatch**: Allow on-demand testing
- **Scheduled**: Daily tests to catch environmental issues
- **On Release**: Final validation before publishing

For more details on GitHub Actions triggers, see the [GitHub Actions documentation](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).

### Release Workflow Triggers

- **On Release Published**: Automatically publish when GitHub releases are created
- **Manual Dispatch**: Allow manual publishing with version specification

## Demonstrating the System

### Testing Failure Scenarios

1. **Introduce a Breaking Change**:
   ```python
   # Intentionally break the component
   class MyComponent(pulumi.ComponentResource):
       def __init__(self, name, args, opts=None):
           # Remove required parameter to cause failure
           super().__init__('myorg:components:MyComponent', name, None, opts)
           # Missing resource creation will cause tests to fail
   ```

2. **Run the Test Action**:
   - Push the breaking change or trigger manually
   - Observe the test failure in GitHub Actions
   - Review the error logs and fix the issue

3. **Fix the Change**:
   ```python
   # Restore proper component implementation
   class MyComponent(pulumi.ComponentResource):
       def __init__(self, name, args, opts=None):
           super().__init__('myorg:components:MyComponent', name, None, opts)
           
           # Properly create child resources
           self.bucket = aws.s3.BucketV2(f"{name}-bucket",
               opts=pulumi.ResourceOptions(parent=self))
   ```

4. **Verify Test Success**:
   - Push the fix and see tests pass
   - Create a new GitHub release
   - Watch the automated publishing workflow complete

## Advanced Testing Strategies

### Semantic Testing

Beyond basic unit tests, implement tests that validate the semantics of updates:

```python
# Test resource relationships
def test_resource_dependencies():
    # Verify proper parent-child relationships
    # Test resource ordering and dependencies
    pass

# Test state file modifications
def test_state_modifications():
    # Verify updates don't cause unexpected replacements
    # Test that state transitions are safe
    pass
```

### Multi-Environment Testing

Test your component across different environments:

```yaml
strategy:
  matrix:
    environment: [dev, staging, prod]
    pulumi-version: [latest, 3.100.0]
```

## Security Considerations

### Secrets Management

Store sensitive information in GitHub Secrets:

- `PULUMI_ACCESS_TOKEN`: Your Pulumi Cloud access token
- `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`: Cloud provider credentials
- `PULUMI_ORG`: Your Pulumi organization name

### Least Privilege Access

Ensure your GitHub Actions have minimal required permissions:

```yaml
permissions:
  contents: read
  packages: write
  id-token: write  # For OIDC
```

## Monitoring and Observability

### Workflow Status Notifications

Configure notifications for workflow failures:

```yaml
- name: Notify on Failure
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Publishing Metrics

Track publishing success and failures using GitHub's built-in workflow analytics or external monitoring tools.

## Next Steps

Once your automated publishing workflow is established, consider these enhancements:

- **Deployment Hooks**: Set up Pulumi Cloud webhooks to trigger deployments when new component versions are published
- **Automated Documentation**: Generate and publish component documentation automatically
- **Version Compatibility Testing**: Test new versions against existing consumer programs
- **Progressive Rollouts**: Implement canary releases for high-impact components

## Learn More

- [Build a Component]({{< relref "/docs/iac/using-pulumi/build-a-component" >}})
- [Testing Components]({{< relref "/docs/iac/concepts/components/testing-components" >}})
- [Private Registry]({{< relref "/docs/idp/get-started/private-registry" >}})
- [GitHub Actions for Pulumi]({{< relref "/docs/iac/using-pulumi/continuous-delivery/github-actions" >}})
- [Pulumi Deployments]({{< relref "/docs/pulumi-cloud/deployments" >}})