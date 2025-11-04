---
title_tag: "Integration Testing for Pulumi Programs"
meta_desc: "Guide to integration testing of Pulumi programs with various testing frameworks and approaches."
title: Integration testing
h1: Integration Testing for Pulumi Programs
meta_image: /images/docs/meta-images/docs-meta.png
weight: 3
menu:
    iac:
        name: Integration testing
        parent: iac-guides-testing
        weight: 3
        identifier: iac-guides-testing-integration
    usingpulumi:
        parent: testing
        identifier: testing-integration
aliases:
    - /docs/guides/testing/integration/
    - /docs/using-pulumi/testing/integration/
    - /docs/iac/concepts/testing/integration/
---

Integration testing validates your Pulumi programs by running your program and testing the results without examining internal implementation details. For example, you might test that an HTTP endpoint is available and gives the expected response to an incoming request. An integration test runs the program in combination with the Pulumi CLI or Automation API to deploy infrastructure to an ephemeral environment. Once your tests are run and the correctness of your infrastructure is verified (or refuted), you will typically destroy the infrastructure you created for the test. This approach is known as "black-box testing" because it tests the program from the outside.

## Why integration testing?

Integration testing allows you to validate that your infrastructure code works correctly in a real cloud environment. Unlike unit tests that mock cloud resources, or Policy as Code that verifies expectations for specific resources in your stack, integration tests deploy actual infrastructure to verify your code's behavior end-to-end.

By running a program through integration tests, you can ensure:

- Your project's code is syntactically well-formed and runs without errors.
- Your stack's configuration and secrets work and are interpreted correctly.
- Your project can be successfully deployed to your cloud provider of choice.
- Resources of the desired shape are successfully created.
- The infrastructure behaves as expected: for example, a health-check endpoint returns a valid HTML document, or a suite of application-level tests succeeds against the public API.
- Your project can be successfully updated from its starting state to other states.
- Your project can be successfully destroyed and removed from your cloud provider.

## Integration testing options

Pulumi supports several approaches to integration testing, each with different trade-offs:

### Integration testing framework

Pulumi provides a [dedicated integration testing framework](/docs/iac/guides/testing/integration/framework/) written in Go. This framework is designed to drive lifecycle operations against a Pulumi program: deploying a new stack from scratch, optionally updating it with variations, and tearing it down afterwards.

Benefits:

- Purpose-built for testing Pulumi programs
- Comprehensive lifecycle testing capabilities, including the ability to test update/upgrade paths
- Robust validation options for resources and runtime behavior
- Can test Pulumi programs written in any supported language

Constraints:

- Tests must be written in Go

### Automation API

You can use [Automation API for integration testing](/docs/iac/guides/testing/integration/automation-api/) to programmatically run CLI actions and write tests using your preferred testing framework. This approach gives you full control over the testing process using the programming language of your choice.

Benefits:

- Write tests in your preferred language and testing framework
- Full programmatic control over stack lifecycle
- Easy integration with existing language-specific tooling for testing
- Available in Node.js, Python, .NET, Go, and Java

Constraints:

- Not available in YAML

### DIY Options

You can also write integration tests by executing Pulumi CLI commands via shell (either by executing a shell script or by executing shell commands in your preferred language) and making assertions in any language. While Automation API makes this easier by providing language-native APIs, you can accomplish similar results with shell scripts if needed.

Benefits:

- Works with any programming language
- Simple to understand and implement
- No additional dependencies beyond the Pulumi CLI

Trade-offs:

- More manual error handling
- Less type-safe than Automation API
- More difficult to extract and validate resource properties
