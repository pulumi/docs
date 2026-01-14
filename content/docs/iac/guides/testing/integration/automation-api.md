---
title_tag: "Integration Testing with Automation API"
meta_desc: "Learn how to use Pulumi's Automation API to write integration tests in your preferred programming language."
title: Automation API testing
h1: Integration Testing with Automation API
meta_image: /images/docs/meta-images/docs-meta.png
weight: 2
menu:
    iac:
        name: Automation API testing
        parent: iac-guides-testing-integration
        weight: 2
---

Pulumi's [Automation API](/docs/iac/automation-api/) provides a programmatic interface for integration testing. While not a purpose-built integration testing framework, you can use Automation API in your integration tests to accomplish the same objectives of basic correctness testing, resource validation, and runtime testing. Automation API is available in all Pulumi languages except YAML and is a part of the Pulumi SDK.

## Testing workflow

To write integration tests with Automation API, follow these steps:

1. Create a stack using Automation API.
1. Set up stack configuration and secrets.
1. Deploy the stack using `up()`.
1. Perform resource validation by examining the deployment state.
1. Perform runtime checks by interacting with deployed infrastructure.
1. Tear down the stack using `destroy()` and clean up resources.

## Validating resource and stack properties

To validate that the correct resources were created with the expected properties, you can export the stack and examine the resulting resources.

For example, in TypeScript:

```typescript
export async function getDeployment(): Promise<Deployment> {
  const stack = await LocalWorkspace.createOrSelectStack(args);

  return stack.exportStack();
}
```

You can then iterate through the `Deployment` object to check that the expected resources and property values are present.

## Validating infrastructure correctness

Runtime validation involves interacting with your deployed infrastructure to verify it works correctly. For example, you might:

- Make HTTP requests to validate an API endpoint
- Query a database to verify data was created correctly
- Check that files exist in object storage
- Verify that VMs are responding to network requests

The Automation API gives you full access to stack outputs, which typically include endpoints, URLs, and other information needed to interact with your infrastructure.

## Example

The [`localProgram-tsnode-mochatests` example](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/localProgram-tsnode-mochatests) demonstrates how to:

- Set up a stack using Automation API
- Perform runtime validation checks
- Tear down the stack as part of a test

## Additional resources

Integration tests written with Automation API in the Pulumi SDK repositories:

- [Node.js tests](https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/tests/automation/localWorkspace.spec.ts)
- [Go tests](https://github.com/pulumi/pulumi/blob/master/sdk/go/auto/local_workspace_test.go)
- [Python tests](https://github.com/pulumi/pulumi/blob/master/sdk/python/lib/test/automation/test_local_workspace.py)
- [C# tests](https://github.com/pulumi/pulumi-dotnet/blob/main/sdk/Pulumi.Automation.Tests/LocalWorkspaceTests.cs)
- [Java example](https://github.com/pulumi/automation-api-examples/blob/main/java/localProgram/)
