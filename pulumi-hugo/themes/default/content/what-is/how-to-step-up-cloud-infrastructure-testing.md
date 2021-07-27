---
title: How to Step Up Cloud Infrastructure Testing
meta_desc: |
    Learn more about modeling infrastructure testing on standard software practices by including other tests, such as unit, integration, policy and security tests.

type: what-is
page_title: "Stepping Up Your Infrastructure Testing: A Quick Introduction"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - kenshoo
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

Infrastructure testing isn’t new and, over the years, there have been various tools that people have used to perform it. However, what tends to happen is that standard ops testing focuses on acceptance tests. That means the ops team spins up some infrastructure in the cloud and they then test that infrastructure to see if it’s correct. Of course, if it wasn’t spun up correctly, the team needs to destroy and recreate it. That’s not a great approach because, potentially, something that shouldn’t have happened already has, depending on how quickly the team took a look.

A better approach is to model infrastructure testing on standard software practices for applications. That means including other tests, such as unit, integration, policy and security tests. All these tests can be part of a test-driven development (TDD) strategy. With TDD, you first write the test cases that specify and validate what the code will do. The test cases are created and tested first. The initial run will fail, of course, because the code isn’t written. Then, you write the new code, which should pass the tests. If it doesn’t, you know early on that you’ve got some bugs that need to be fixed.

TDD is one way to shift risk to the left. That means you move testing to as early in the development cycle as possible, instead of testing at the end of the cycle. Fixing problems early, before there’s a lot of code with all its complexities and interdependencies in place, will make your debugging sessions simpler. The end result is you’ll deliver faster.

## Unit Tests

Unit tests evaluate the behavior of your infrastructure in isolation. External dependencies, such as databases, are replaced by mocks to check your resource configuration and responses. It’s possible to use mocks because responses from cloud providers are well known and tested. You already know how, given some parameters, the provider will respond.

Unit tests run in memory without any out-of-process calls, which makes them very fast. Use them for fast feedback loops during development. Unit tests really help you solve problems early in the life cycle of your infrastructure.

A few examples of what you can verify are:

- Resources are correctly tagged.
- Instances don’t have an SSH connection open to the Internet.
- Web site URLs are valid.

When you’re planning your tests, think about using a tool that lets you write your tests in a general purpose language such as Python, Go, TypeScript or C#, rather than in a special-purpose DSL. Standard languages all have well-understood tools and frameworks that make it much easier to test your code.

## Integration Tests

Integration testing (also known as black-box testing) comes after unit testing and it takes a different approach. Integration tests deploy cloud resources and validate their actual behavior but in an ephemeral environment. An ephemeral environment is a short-lived environment that mimics a production environment. It’s often simpler and only includes the first-level dependencies of the code you’re testing.

Some of the behaviors you can verify are:

- Your project’s code is syntactically well-formed and runs without errors.
- Your stack’s configuration and secrets work and are interpreted correctly.
- Your project can be successfully deployed to your cloud provider.
- The infrastructure behaves as expected: for example, a health-check endpoint returns a valid HTML document, or a suite of application-level tests succeeds against the public API.

Once the integration tests are finished, you can destroy the ephemeral infrastructure.

## Property Tests

A type of test you may not be familiar with is a property test. Property tests run resource-level assertions while the infrastructure is being deployed. They are there to test your policies and they rely on you having written your policies as code.

In contrast to “black-box” integration testing, policies have access to all input and output values of all cloud resources in the stack. As opposed to unit testing, property tests can evaluate real values returned from the cloud provider instead of the mocked ones.

Use property tests to ensure that your infrastructure complies with your company’s standards. A couple examples are:

- Checking that you’re using the correct version of the provider's managed Kubernetes service.
- Ensuring a service can make an API call to a policy engine to determine whether a request is authorized or not.
- Ensuring that a resource is provisioned inside a private VPC, rather than the default one.

## Security Tests

Too often, security tests are left until the last minute, or code that’s considered “finished” gets thrown over the wall to a security team, who’ve been left out of the entire development process. The phrase “courting disaster” comes to mind when considering this approach. Large companies and governments have all suffered well-publicized data breaches that exposed millions of confidential records.

Security tests should be as much a part of your workflow as any other type of testing. Just as you start testing your code early with unit tests, so should you start testing early to find security problems. If you have a dedicated security team, involve them right away, so they can help you design effective tests. Make sure those tests are included in your CI/CD pipeline.

Just a few of the things you should do are:

- Strip out all plaintext secrets.
- Make sure all secrets are encrypted.
- Think about adopting services offered by your cloud provider to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

As with all the other tests we’ve mentioned, security testing should be done as early in the process as possible. If you have a dedicated security team, make sure to involve them immediately. Don’t write your code and then hand off what you consider to be a production-ready code to them. There are a variety of security tests you can incorporate into your development process. Here are a few:

- Vulnerability Scanning: This kind of testing uses automated software to scan a system against known vulnerability signatures. There are vulnerability scanners on the market that you can use.
- Penetration testing or pen tests: This kind of testing simulates an attack from a malicious hacker. This testing involves analysis of a particular system to check for potential vulnerabilities to an external hacking attempt. You might want to check out the The Open Web Application Security Project ([OWASP](https://owasp.org/www-project-web-testing-environment/)), which is a worldwide non-profit organization focused on improving the security of software. The project has multiple tools to pen-test various software environments and protocols.
- Ethical hacking: Try scheduling “game days,” where people in your company deliberately try to hack its systems.

## Learn More

Pulumi lets you take advantage of the well-developed testing frameworks that support your favorite programming language. It also includes many features for helping you ensure that your infrastructure works the way it should, is reliable and is secure. Visit us at pulumi.com or [get started]({{< relref "/docs/get-started" >}}) for free today.
