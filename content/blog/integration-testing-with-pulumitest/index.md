---
title: "Best Practices for Integration Testing with PulumiTest"
date: 2025-10-23
draft: false
meta_desc: Learn how to write robust integration tests for your infrastructure code using PulumiTest, with practical examples and best practices from real-world scenarios.
meta_image: meta.png
authors:
    - rshade
tags:
    - testing
    - go
    - features
---

Writing infrastructure code is one thing. Being confident that it actually works in production is another. PulumiTest brings integration testing directly into your development workflow, letting you validate that your infrastructure behaves correctly before it ever reaches production. Whether you're building a new cloud service, migrating existing infrastructure, or maintaining critical production systems, PulumiTest gives you the confidence to ship faster without sacrificing reliability.

<!--more-->

## What is PulumiTest?

PulumiTest is a streamlined wrapper around Pulumi's Automation API, purpose-built for testing scenarios. It abstracts away the complexity of direct CLI interactions while maintaining the flexibility you need for sophisticated test cases. Think of it as your infrastructure testing framework—handling the boilerplate so you can focus on validating what matters.

At its core, PulumiTest provides:

- **Test isolation** - Programs are automatically copied to temporary directories, preserving your source code integrity
- **Smart defaults** - Automatic dependency installation, stack creation, and cleanup
- **Flexibility** - Full control over backends, providers, and test configurations
- **Multi-step testing** - Validate infrastructure updates, replacements, and migrations
- **SDK integration** - First-class support for testing local SDK changes across all languages

## Why integration testing matters for infrastructure

Unit tests validate that your infrastructure code compiles and produces the expected resource definitions. But they don't tell you whether those resources actually work when deployed to your cloud provider. Integration tests fill this critical gap.

Consider these real-world scenarios where integration testing saves the day:

**Security group misconfiguration:** Your code defines a security group that should allow traffic from your application tier to your database tier. Unit tests verify the rules exist, but only an integration test can confirm the network connectivity actually works.

**Multi-resource dependencies:** You're deploying a Kubernetes cluster with a load balancer, application pods, and a certificate manager. Integration tests validate that certificates are properly generated, pods are running, and the load balancer is routing traffic correctly.

**Update behavior:** You're migrating Lambda functions from Python 3.8 to Python 3.12. Integration tests can deploy both versions, validate functionality, and ensure a smooth update path without replacements.

**Provider-specific quirks:** Cloud providers have subtle differences in how they handle resource updates. Integration tests catch these provider-specific behaviors before they cause production incidents.

## Getting started with PulumiTest

Here's a minimal example testing an AWS S3 bucket deployment:

```go
package main

import (
    "testing"
    "path/filepath"

    "github.com/pulumi/providertest/pulumitest"
    "github.com/pulumi/providertest/pulumitest/opttest"
)

func TestS3Bucket(t *testing.T) {
    test := pulumitest.NewPulumiTest(t,
        filepath.Join("test-programs", "s3-bucket"),
    )

    // Deploy the infrastructure
    test.Up(t)
}
```

That's it. PulumiTest handles:

1. Copying your program to a temporary directory
1. Installing dependencies
1. Creating a test stack
1. Running `pulumi up`
1. Cleaning up when the test completes

By default, PulumiTest uses a local backend in a temporary directory, ensuring complete test isolation without affecting your production stacks.

## Best practice: Organize test programs strategically

Structure your test programs to mirror real-world deployment patterns. Rather than testing individual resources in isolation, test meaningful configurations that represent actual use cases.

```
test-programs/
├── basic-vpc/          # Simple VPC configuration
├── app-with-database/  # Application tier + RDS
├── kubernetes-cluster/ # Complete EKS setup
└── multi-region/       # Cross-region replication
```

Each test program should represent a coherent infrastructure pattern that you'd actually deploy. This approach catches integration issues that only manifest when resources interact.

## Best practice: Leverage test isolation features

PulumiTest's isolation features are your first line of defense against flaky tests. Here's how to use them effectively:

### Temporary directories

By default, programs are copied to OS-specific temporary directories. For debugging, you can control this behavior:

```go
// Keep temporary files after test completion
os.Setenv("PULUMITEST_RETAIN_FILES", "true")

// Use a specific temporary directory
test := pulumitest.NewPulumiTest(t,
    "test-programs/vpc",
    opttest.TempDir("/tmp/my-test"),
)

// Or test in place without copying (useful for debugging)
test := pulumitest.NewPulumiTest(t,
    "test-programs/vpc",
    opttest.TestInPlace(),
)
```

### Stack isolation

Failed stacks are automatically destroyed, but you can preserve them for debugging:

```go
// Preserve failed stacks for inspection
os.Setenv("PULUMITEST_SKIP_DESTROY_ON_FAILURE", "true")
```

This is invaluable when debugging complex failures—you can inspect the actual cloud resources after the test fails.

## Best practice: Test provider integrations properly

Testing against real cloud providers requires careful credential management. PulumiTest supports multiple approaches:

### Using ambient credentials

The simplest approach uses your existing cloud credentials:

```go
test := pulumitest.NewPulumiTest(t,
    "test-programs/aws-vpc",
    opttest.UseAmbientBackend(),
)
```

Your AWS credentials from `~/.aws/credentials` or environment variables are automatically available to the test.

### Attaching local providers

When developing custom providers, you can attach a locally-built provider binary:

```go
test := pulumitest.NewPulumiTest(t,
    "test-programs/custom-provider",
    opttest.AttachProviderBinary(
        "myprovider",
        "/path/to/pulumi-resource-myprovider",
    ),
)
```

This is essential for testing provider changes before publishing.

### Provider debugging

For deep debugging, attach to a running provider process:

```go
// Start your provider with debugging enabled on port 12345
// Then in your test:
test := pulumitest.NewPulumiTest(t,
    "test-programs/debug",
    opttest.AttachProvider("myprovider", "12345"),
)
```

This enables full debugger integration, breakpoints, and step-through debugging of your provider code.

## Best practice: Validate multi-step updates

Infrastructure isn't static. You need to test updates, not just initial deployments. PulumiTest's `UpdateSource` method makes this straightforward:

```go
func TestLambdaRuntimeMigration(t *testing.T) {
    test := pulumitest.NewPulumiTest(t,
        filepath.Join("test-programs", "lambda-python38"),
    )

    // Deploy with Python 3.8
    upResult := test.Up(t)

    // Verify Python 3.8 runtime
    require.Contains(t, upResult.Outputs, "functionArn")

    // Update to Python 3.12
    test.UpdateSource(t, filepath.Join("test-programs", "lambda-python312"))

    // Deploy the update
    updateResult := test.Up(t)

    // Verify no replacements occurred (important for zero-downtime)
    assertup.HasNoReplacements(t, updateResult)

    // Verify Python 3.12 is running
    // ... additional validation ...
}
```

This pattern is crucial for:

- **Runtime migrations** - Validate smooth upgrades without resource replacements
- **Configuration changes** - Ensure updates don't cause unexpected replacements
- **Schema migrations** - Test database migrations alongside infrastructure changes
- **Blue-green deployments** - Validate cutover mechanisms work correctly

## Best practice: Use assertions effectively

PulumiTest includes `assertup` and `assertpreview` packages for common validation patterns:

```go
import (
    "github.com/pulumi/providertest/pulumitest/assertup"
    "github.com/pulumi/providertest/pulumitest/assertpreview"
)

func TestNoChangesAfterRefresh(t *testing.T) {
    test := pulumitest.NewPulumiTest(t, "test-programs/stable-vpc")

    // Initial deployment
    test.Up(t)

    // Refresh should show no drift
    refreshResult := test.Refresh(t)
    assertup.HasNoChanges(t, refreshResult)

    // Preview should show no pending changes
    previewResult := test.Preview(t)
    assertpreview.HasNoChanges(t, previewResult)
}
```

Common assertions include:

- `HasNoChanges()` - Verify no drift or pending updates
- `HasNoReplacements()` - Ensure updates don't force replacements
- `HasNoDeletes()` - Validate no resources are being deleted

## Best practice: Test local SDK changes

When developing or debugging Pulumi SDKs, you need to test against your local changes. PulumiTest integrates seamlessly with each language's package management:

### Node.js with yarn link

```go
test := pulumitest.NewPulumiTest(t,
    "test-programs/typescript-app",
    opttest.YarnLink("@pulumi/aws"),
    opttest.YarnLink("@pulumi/awsx"),
)
```

First run `yarn link` in your locally-built SDK directory, then reference it in your test.

### Go with module replacements

```go
test := pulumitest.NewPulumiTest(t,
    "test-programs/go-app",
    opttest.GoModReplacement(
        "github.com/pulumi/pulumi-aws/sdk/v6",
        "/path/to/local/sdk",
    ),
)
```

### .NET with project references

```go
test := pulumitest.NewPulumiTest(t,
    "test-programs/csharp-app",
    opttest.DotNetReference(
        "Pulumi.Aws",
        "/path/to/pulumi-aws/sdk/dotnet",
    ),
)
```

This workflow is essential for provider development—you can validate SDK changes before publishing them.

## Best practice: Configure stack settings appropriately

Stack configuration often varies between test and production environments. PulumiTest makes it easy to set test-specific configuration:

```go
func TestWithConfiguration(t *testing.T) {
    test := pulumitest.NewPulumiTest(t, "test-programs/configurable-app")

    // Set test-specific configuration
    test.SetConfig(t, "app:environment", "test")
    test.SetConfig(t, "app:debugMode", "true")
    test.SetConfig(t, "aws:region", "us-west-2")

    // Deploy with test configuration
    result := test.Up(t)

    // Validate test-specific behavior
    // ...
}
```

This is particularly useful for:

- **Region selection** - Test in cheaper or faster regions
- **Instance sizing** - Use smaller instances for tests
- **Feature flags** - Enable test-specific features
- **Debug settings** - Increase logging for test environments

## Real-world example: Testing a three-tier application

Here's a comprehensive example testing a realistic three-tier application with VPC, application servers, and RDS database:

```go
func TestThreeTierApp(t *testing.T) {
    test := pulumitest.NewPulumiTest(t,
        filepath.Join("test-programs", "three-tier-app"),
        opttest.StackName("integration-test"),
    )

    // Configure test environment
    test.SetConfig(t, "aws:region", "us-west-2")
    test.SetConfig(t, "dbInstanceClass", "db.t3.micro")
    test.SetConfig(t, "appInstanceType", "t3.small")

    // Deploy the complete stack
    upResult := test.Up(t)

    // Validate VPC resources were created
    require.Contains(t, upResult.Outputs, "vpcId")
    require.Contains(t, upResult.Outputs, "publicSubnetIds")
    require.Contains(t, upResult.Outputs, "privateSubnetIds")

    // Validate application tier
    require.Contains(t, upResult.Outputs, "appLoadBalancerUrl")
    loadBalancerUrl := upResult.Outputs["appLoadBalancerUrl"].Value.(string)

    // Test actual connectivity
    resp, err := http.Get(fmt.Sprintf("http://%s/health", loadBalancerUrl))
    require.NoError(t, err)
    require.Equal(t, http.StatusOK, resp.StatusCode)

    // Validate database tier
    require.Contains(t, upResult.Outputs, "dbEndpoint")

    // Test database connectivity from app tier
    resp, err = http.Get(fmt.Sprintf("http://%s/db-test", loadBalancerUrl))
    require.NoError(t, err)
    require.Equal(t, http.StatusOK, resp.StatusCode)

    // Test update scenario: scale app tier
    test.UpdateSource(t, filepath.Join("test-programs", "three-tier-app-scaled"))
    updateResult := test.Up(t)

    // Verify update succeeded without database replacement
    assertup.HasNoReplacements(t, updateResult)

    // Validate increased capacity
    // ... additional validation ...
}
```

This test validates:

- All infrastructure components deploy successfully
- Network connectivity works between tiers
- The application responds to HTTP requests
- Database connectivity functions correctly
- Updates can be applied without disrupting the database

## Environment variables for debugging

PulumiTest respects several environment variables that control test behavior:

| Variable | Purpose |
|----------|---------|
| `PULUMITEST_RETAIN_FILES` | Keep temporary files after test completion |
| `PULUMITEST_SKIP_DESTROY_ON_FAILURE` | Preserve failed stacks for debugging |
| `PULUMITEST_TEMP_DIR` | Override default temporary directory location |
| `PULUMI_CONFIG_PASSPHRASE` | Set custom encryption passphrase (default: "correct horse battery staple") |

Set these in your CI environment or locally when debugging failing tests.

## Performance considerations

Integration tests are slower than unit tests because they interact with real cloud providers. Here are strategies to keep test suites fast:

**Parallelize tests:** Run independent tests concurrently using Go's built-in test parallelization:

```go
func TestVPC(t *testing.T) {
    t.Parallel()
    // ... test code ...
}

func TestS3Bucket(t *testing.T) {
    t.Parallel()
    // ... test code ...
}
```

**Use regional endpoints wisely:** Some AWS regions are faster than others. Consider using `us-east-1` for faster test execution, or test in regions geographically close to your CI infrastructure.

**Minimize resource counts:** Test with the minimum resources needed to validate behavior. Use `t3.micro` or `t3.small` instances instead of production-sized instances.

**Cache dependencies:** In CI environments, cache `node_modules`, Go module caches, and NuGet packages to speed up dependency installation.

## Getting started checklist

Ready to add integration testing to your infrastructure projects? Follow this checklist:

1. **Install PulumiTest** - Add `github.com/pulumi/providertest` to your Go module
1. **Create test programs** - Set up minimal infrastructure configurations in a `test-programs` directory
1. **Write your first test** - Start simple with a basic deployment test
1. **Add assertions** - Validate outputs and resource properties
1. **Test updates** - Use `UpdateSource` to test infrastructure changes
1. **Integrate with CI** - Run tests automatically on pull requests
1. **Monitor test duration** - Keep tests fast with parallelization and resource optimization

## Learn more

- [PulumiTest documentation](https://github.com/pulumi/providertest/tree/main/pulumitest)
- [Testing infrastructure code](/docs/iac/concepts/testing/)
- [Automation API guide](/docs/iac/packages-and-automation/automation-api/)
- [Provider development guide](/docs/iac/packages-and-automation/pulumi-packages/authoring/)

Integration testing transforms infrastructure development from a leap of faith into a confident, validated process. PulumiTest gives you the tools to catch issues early, validate complex scenarios, and ship infrastructure changes with confidence. Start testing today and experience the peace of mind that comes from knowing your infrastructure actually works—before it reaches production.
