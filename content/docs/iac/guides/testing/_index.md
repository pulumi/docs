---
title_tag: "Testing Pulumi programs"
meta_desc: "Guide to automated testing of Pulumi programs: unit testing, property testing, integration testing."
title: Testing
h1: Testing Pulumi programs
menu:
    iac:
        name: Testing
        parent: iac-using-pulumi
        weight: 50
        identifier: iac-guides-testing
aliases:
- /docs/iac/guides/testing/
- /docs/guides/testing/
- /docs/using-pulumi/testing/
- /docs/iac/concepts/testing/
---

Because Pulumi uses general purpose programming languages to provision cloud resources, you can take advantage of native testing frameworks and perform **automated tests** of your infrastructure.

Automated testing comes in multiple styles: unit testing of individual pieces, integration testing of system components, and end-to-end testing of the complete application. Each has its own advantages and appropriate uses.

Similarly, Pulumi provides multiple testing styles for cloud programs:

- **Unit tests** are fast in-memory tests that mock all external calls.
- **Property tests** run resource-level assertions *while* infrastructure is being deployed.
- **Integration tests** deploy ephemeral infrastructure and run external tests against it.

The following table summarizes the differences between the three approaches:

|                                | [**Unit tests**](/docs/iac/guides/testing/unit/)    | [**Property tests**](/docs/discovery-governance/guides/write-a-policy-pack/)  | [**Integration tests**](/docs/iac/guides/testing/integration/)  |
|--------------------------------|---------------|---------|----------|
| Provision real infrastructure  | No            | Yes     | Yes      |
| Require the Pulumi CLI         | No            | Yes     | Yes      |
| Time to execute                | Milliseconds  | Seconds | Minutes  |
| Language                       | Same as Pulumi program  | Node.js or Python  | Any language  |
| Validation target              | Resource inputs  | Resource inputs and outputs | External endpoints |

Try all three styles of testing and use the ones that suit your quality targets, development practices, and application style. For many teams, a combination of these approaches makes sense: unit tests that run quickly and validate program logic, property tests that validate key correctness invariants, and integration tests that test end-to-end interaction of infrastructure components.

## Unit testing

Unit tests evaluate the behavior of your code in isolation, while all external dependencies are replaced by **mocks**. Unit tests run in memory without any out-of-process calls, which makes them fast. Therefore, unit tests are suitable for fast feedback loops during development, including **Test-Driven Development** (TDD).

Unit tests are authored in the same language as the Pulumi program under test. You can use your favorite test and mock frameworks, such as Mocha for Node.js or NUnit for .NET.

Because cloud resources aren't created, you can't write a test that evaluates the behavior of infrastructure. For example, you can't make HTTP requests to endpoints, because there's no web server to serve them.

[**Learn more and get started with unit testing**](/docs/iac/guides/testing/unit/).

## Property testing

Property tests are based on [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/), Pulumi's offering to set guardrails and enforce compliance for cloud resources. Beyond authoring company-wide policies, you can use Pulumi Policies for infrastructure testing: each policy becomes a property, an invariant, that a test evaluates and asserts.

Property tests run inside the Pulumi CLI before and after infrastructure provisioning. In contrast to "black-box" integration testing, policy rules have access to all input and output values of all cloud resources in the stack. As opposed to unit testing, property tests can evaluate real values returned from the cloud provider instead of mocked ones.

Property tests can run against any cloud environment: a persistent "acceptance" stack, an ephemeral cloud environment created for each pull request, or a combination of those.

[**Learn more and get started with property testing**](/docs/discovery-governance/guides/write-a-policy-pack/).

## Integration testing

Integration testing takes a different approach from unit tests: the tests deploy cloud resources and validate their actual **behavior**.

An integration test invokes the Pulumi command-line interface (CLI) to deploy infrastructure to an [ephemeral environment](https://about.gitlab.com/blog/kubecon-na-2019-are-you-about-to-break-prod/). When the resources are deployed, the test retrieves endpoints of the infrastructure from the stack outputs: usually, a URL or a public IP address. The test verifies that the infrastructure behaves as expected; for example, it expects a valid HTML document from a health-check endpoint or runs a suite of application-level tests against the public API. When the tests finish, the infrastructure is destroyed.

Integration tests let you test the actual cloud infrastructure and its real properties. However, compared to unit tests, integration tests take more time to execute.

Depending on the resources involved and how often you run tests, even short-lived ephemeral environments may incur notable charges from the cloud provider. Be sure to plan accordingly and measure frequently.

[**Learn more and get started with integration testing**](/docs/iac/guides/testing/integration/).

## Examples

The [examples repository](https://github.com/pulumi/examples#testing) includes these complete, runnable tests:

| Example | Description |
| ------- | ----------- |
| [Unit tests in TypeScript](https://github.com/pulumi/examples/tree/74db62a03d013c2854d2cf933c074ea0a3bbf69d/testing-unit-ts) | Mock-based unit tests in TypeScript. |
| [Unit tests in Python](https://github.com/pulumi/examples/tree/74db62a03d013c2854d2cf933c074ea0a3bbf69d/testing-unit-py) | Mock-based unit tests in Python. |
| [Unit tests in Go](https://github.com/pulumi/examples/tree/74db62a03d013c2854d2cf933c074ea0a3bbf69d/testing-unit-go) | Mock-based unit tests in Go. |
| [Unit tests in C#](https://github.com/pulumi/examples/tree/74db62a03d013c2854d2cf933c074ea0a3bbf69d/testing-unit-cs) | Mock-based unit tests in C#. |
| [Property tests in TypeScript](https://github.com/pulumi/examples/tree/74db62a03d013c2854d2cf933c074ea0a3bbf69d/testing-pac-ts) | Tests based on policy as code in TypeScript. |
| [Integration tests in Go](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-integration) | Deploy-check-destroy tests in Go. |
