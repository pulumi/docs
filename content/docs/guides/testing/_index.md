---
title: Testing
meta_desc: "Guide to automated testing of Pulumi programs: unit testing, property testing, integration testing."
menu:
    userguides:
        identifier: testing
        weight: 7
---

Pulumi uses general-purpose programming languages to define cloud infrastructure. This capability opens up all the doors to **automated testing** of the infrastructure resources.

The software industry has come up with multiple styles of automated testing. Unit testing of individual pieces, integration testing of system components, end-to-end testing of the complete application&mdash;each style has its advantages and challenges.

Pulumi provides a similar choice of testing options for cloud programs. Currently, we identify three types of tests:

- **Unit Tests** are fast in-memory tests that mock all external calls.
- **Property Tests** run resource-level assertions *while* infrastructure is being deployed.
- **Integration Tests** deploy ephemeral infrastructure and run external tests against it.

The following table summarizes the differences between the three approaches:

|                                | Unit Tests    | Property Tests  | Integration Tests  |
|--------------------------------|---------------|---------|----------|
| Provision real infrastructure  | No            | Yes     | Yes      |
| Require the Pulumi CLI         | No            | Yes     | Yes      |
| Time to execute                | Milliseconds  | Seconds | Minutes  |
| Language                       | Same as Pulumi program  | Node.js or Python  | Any language  |
| Validation target              | Resource inputs  | Resource inputs and outputs | External endpoints |

We encourage you to try all three styles of testing and use the ones that are most suitable for your quality targets, development practices, and application style. For many teams, a combination of these approaches may make sense: unit tests that can run quickly and validate program logic, property tests to validate key correctness invariants, and integration tests to test end-to-end interaction of infrastructure components.

## Unit Testing

If you ever created unit tests for your application code, you can directly transfer your skills to testing Pulumi programs. Unit tests evaluate the behavior of your code in isolation, while all external dependencies are replaced by **mocks**.

Unit tests run in memory without any out-of-process calls, which makes them blazingly fast. Therefore, unit tests are suitable for fast feedback loops during development, including **Test-Driven Development** (TDD).

You author the unit tests in the same language as the Pulumi program under test. You are free to use your favorite test and mock frameworks like Mocha for Node.js or NUnit for .NET.

Because there are no real cloud resources created, you can't write a test that would evaluate the behavior of infrastructure. For example, you can't make HTTP requests to endpoints: there's no webserver to serve them.

[Learn more and get started with Unit Testing]({{< relref "./unit" >}}).

## Property Testing

Property tests are based on [Policy as Code]({{< relref "../crossguard" >}}) (also known as "CrossGuard"), Pulumi's offering to set guardrails and enforce compliance for cloud resources. In addition to authoring company-wide policies, CrossGuard enables another type of infrastructure testing. Each policy becomes a property, an invariant, that a test evaluates and asserts.

Property tests run inside the Pulumi CLI before and after infrastructure provisioning. In contrast to "black-box" integration testing, policy rules have access to all input and output values of all cloud resources in the stack. As opposed to unit testing, property tests can evaluate real values returned from the cloud provider instead of the mocked ones.

Property tests can run against any cloud environment: it can be a persistent "acceptance" stack, an ephemeral cloud environment created for each pull request, or a combination of those.

[Learn more and get started with Property Testing]({{< relref "./property-testing" >}}).

## Integration Testing

Integration testing takes the opposite approach: the tests deploy real cloud resources and validate their actual **behavior**.

The flow goes like this:

1. A test invokes the Pulumi command-line interface (CLI) to deploy infrastructure to an ephemeral environment.
2. When deployment succeeds, the test queries stack outputs to retrieve endpoints of the infrastructure: usually, a URL or a public IP address.
3. The test verifies that the infrastructure behaves as expected: for example, it expects a valid HTML document from a health-check endpoint, or runs a suite of application-level tests against the public API.
4. Upon completion, the infrastructure is destroyed.

The great advantage of integration tests is the ability to test the actual cloud infrastructure and its real properties. However, compared to unit tests, integrations tests take a long time to execute.

Depending on the type of resources and frequency of testing, even short-lived ephemeral environments may incur notable charges from the cloud provider. Be sure to plan accordingly and measure frequently.

[Learn more and get started with Integration Testing]({{< relref "./integration" >}}).

## Examples

Several complete and runnable tests are available in the [examples repository](https://github.com/pulumi/examples#testing):

Example		| Description |
----- 		| --------- |
[Unit Tests in TypeScript](https://github.com/pulumi/examples/tree/master/testing-unit-ts)      | Mock-based unit tests in TypeScript.
[Unit Tests in Python](https://github.com/pulumi/examples/tree/master/testing-unit-py)  | Mock-based unit tests in Python.
[Unit Tests in Go](https://github.com/pulumi/examples/tree/master/testing-unit-go)      | Mock-based unit tests in Go.
[Unit Tests in C#](https://github.com/pulumi/examples/tree/master/testing-unit-cs)      | Mock-based unit tests in C#.
[Property Testing in TypeScript](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-pac-ts)       | Tests based on Policy-as-Code in TypeScript.
[Integration Testing in Go](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-integration)  | Deploy-check-destroy tests in Go.
