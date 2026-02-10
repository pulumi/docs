---
title_tag: "Testing Pulumi Components"
meta_desc: "Learn strategies and tools for testing Pulumi Components during development and in CI/CD workflows."
title: Testing Pulumi Components
h1: Testing Pulumi Components
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Testing Components
        parent: iac-guides-components
        weight: 20
aliases:
- /docs/iac/concepts/components/testing-components/
- /docs/iac/build-with-pulumi/testing-components/
---

When authoring Pulumi components, it's critical to ensure that changes won't unintentionally break Pulumi programs that consume your components, nor violate organizational policies. This page outlines different testing strategies and tools you can use to confidently update and maintain components.

## Why Testing Matters: Blast Radius and Change Safety

When a component is updated, it's important to understand what other projects or teams might be affected. For example, if a platform engineering team updates a shared component that encapsulates sensitive company security details in response to a security incident or a new regulatory requirement, the platform team will need to verify that the update won’t unintentionally break downstream Pulumi programs.

## Testing Strategies

### Scenario: Security Updates

In this scenario, a platform team owns a reusable IAM component used by many services across the organization. After a security event, they need to update a policy document or rotate a role.

To assess the impact of this change, two primary methods can be used:

### Testing Strategy: Link to a local copy and use `pulumi preview`

[The `pulumi preview` command](/docs/iac/cli/commands/pulumi_preview/) shows what changes will occur if a project consumes the updated version of the component. This helps identify if the changes are additive, destructive, or trigger replacements.

This method works best when:

- You have access to consumer projects
- You can link the component locally

Running `pulumi preview` works great for existing projects to detect any unexpected behavior after an update. The upside of this approach is that it tests your new code in exactly the environments where it will be used, giving real-world feedback that will reveal many unintended consequences of the component update. The downside of this approach is that it may not scale well if your component has many downstream consumers or your team does not have direct access to the Pulumi programs that consume your component.

### Testing Strategy: Integration and Unit Testing Tools

Set up **integration tests** using tools like:

- Language-specific [unit testing](/docs/iac/guides/testing/unit/) tools
- Local test benches ([see below](#yaml-test-benches))
- CI/CD workflows (like [GitHub Actions](/docs/iac/using-pulumi/continuous-delivery/github-actions/)) that validate downstream usage

These tests can assert that the updated component produces expected outputs and maintains compatibility. This approach works well when you don't have access to the end-user programs. However, there are limits to what these types of tests can detect: It's often difficult to write enough tests to have 100% test coverage for all possible inputs. Often there are environment-specific problems related to configuration, secrets, or other factors that are not able to be recreated in the testing environment. So, while these approaches give you *some* security, they are not as comprehensive as simply running `pulumi preview` in a consuming program and seeing what breaks.

#### Integration Testing via the Pulumi Go Provider SDK

If you're working in the Go programming language, components can be tested using the [Pulumi Go Provider SDK](https://github.com/pulumi/pulumi-go-provider), via the built-in `integration` test framework.

Features:

- Can test components and Pulumi programs in any language
- Stand up ephemeral environments
- Assert on created resources and their outputs
- Validate behavior across versions and configs

See ["Integration Testing"](/docs/iac/guides/testing/integration/) and [`pulumi-go-provider/integration`](https://github.com/pulumi/pulumi-go-provider/tree/main/integration) for usage examples.

## Prevention Strategies

While the following methods aren't strictly "testing", they do accomplish similar goals. It helps to limit and reduce the potential range of problems that a breaking change could cause. It's important to remember that the primary purpose of testing is not the testing itself, but the way that tests can reduce the scope of potential problems and prevent production problems.

### Scenario: Cost Control with Abstractions

Platform teams may also want to limit certain choices. For instance, restricting EC2 instance types to specific sizes to manage cost. Changing this inside of a component will help prevent new resources from being made that are too costly.

Instead of relying solely on tests:

### Prevention Strategy: Use Enums to Control Inputs

You can model allowed values directly in your component's implementation using enum types (Python only):

***Example:** A custom enum type in Python that controls the range of inputs to your component*

```python
from enum import Enum

# Custom enum for allowed instance sizes
class InstanceSize(str, Enum):
    T3_MICRO = "t3.micro"
    T3_SMALL = "t3.small"

# In your component args:
class MyComponentArgs(TypedDict):
    instanceSize: pulumi.Input[InstanceSize]
    """The instance size to create, limited to only the options from our custom enum."""

```

This makes invalid configurations impossible to compile or deploy, removing the need for some kinds of tests.

### Prevention Strategy: Use Policies as Guardrails

[Pulumi Policies](/docs/insights/policy/) policies can enforce input constraints dynamically at deployment time. For example:

***Example:** A custom policy in TypeScript that enforces the allowed instance sizes*

```ts
policy.resourceOfType("aws:ec2/instance:Instance", (args, reportViolation) => {
    if (!["t3.micro", "t3.small"].includes(args.props.instanceType)) {
        reportViolation("Only t3.micro and t3.small are allowed.");
    }
});
```

Use policies to enforce security, cost, or compliance constraints that complement component-level modeling. Suppose a component author had changed the input enum accidentally. This policy would catch that at runtime, preventing the costly cloud resources from being created and alerting the end user to the issue. Policies can function as always-on unit tests in that way. Read more about about this in ["Property Testing"](/docs/iac/guides/testing/property-testing/).

## Debugging Strategies

When things go wrong or you need to understand your component more deeply, these approaches can help:

### YAML Test Benches

For quick iteration and fast feedback, you can write minimal YAML programs that consume your component.

Example scaffold:

```yaml
name: test-component
runtime: yaml
resources:
  myResource:
    type: mycompany:platform:MyComponent
    properties:
      name: test
```

Run with:

```bash
pulumi up
```

This is especially useful for catching schema errors, input validation bugs, and unexpected property name casing issues.

We chose YAML for the test bench because it's the simplest language to consume a component in. This approach avoids any confusing issues with multi-language naming, syntax problems within the test bench itself, or issues with SDK generation.

That said, if you're running into problems in one target language but not the other, the same approach can be used with any Pulumi language.

### Inspect the schema directly

Use `pulumi package get-schema` to inspect the component’s generated schema directly, including:

- Inputs and outputs
- Required fields
- Enum types
- Documentation metadata

```bash
pulumi package get-schema ./my-component
```

This provides essential details for debugging interop issues and schema mismatches.

## Learn more

- [Build a Component](/docs/iac/using-pulumi/build-a-component/)
- [Testing Pulumi Programs](/docs/iac/guides/testing/)
- [Pulumi Provider SDK](/docs/iac/build-with-pulumi/pulumi-provider-sdk/)
