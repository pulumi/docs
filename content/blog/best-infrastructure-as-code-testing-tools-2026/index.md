---
title: "Best Tools for Testing Infrastructure as Code in 2026"
date: 2026-11-24
draft: false
meta_desc: "The best tools for testing infrastructure as code in 2026: static analysis, policy checks, unit tests, and integration tests, compared by layer and fit."
authors:
    - pulumi-content-team
tags:
    - infrastructure-as-code
    - testing
    - policy-as-code
    - devops
category: general
faq_schema: true
itemlist_name: "Infrastructure as Code Testing Tools"
itemlist:
    - name: "Checkov"
    - name: "Trivy"
    - name: "TFLint"
    - name: "Open Policy Agent and Conftest"
    - name: "HashiCorp Sentinel"
    - name: "Pulumi Policies"
    - name: "Pulumi unit tests"
    - name: "terraform test and tofu test"
    - name: "AWS CDK assertions"
    - name: "Terratest"
    - name: "Pulumi integration tests and the Automation API"
    - name: "pulumi preview and review stacks"
    - name: "LocalStack"

related_posts:
    - how-to-test-infrastructure-as-code
    - best-policy-as-code-tools

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Infrastructure testing has layers: static analysis, policy checks, unit tests, and integration tests against short-lived environments.

        We compared the tools for each layer: Checkov, Trivy, OPA, Terratest, terraform test, Pulumi, and more.
    linkedin: |
        Most infrastructure as code testing advice lists tools in one flat pile. A linter, a policy engine, a unit test framework, and an integration harness answer different questions, and a healthy pipeline usually needs one of each.

        We organized the 2026 tool landscape as a testing pyramid: static analysis (Checkov, Trivy, TFLint), policy as code (OPA and Conftest, Sentinel, Pulumi Policies), unit tests (Pulumi mocks, terraform test, CDK assertions), and integration tests against short-lived environments (Terratest, the Pulumi integration framework, LocalStack).

        The post also answers the question we hear most: can you unit test Terraform? Yes, within limits, and it spells out what those limits are.
    bluesky: |
        A linter, a policy engine, a unit test framework, and an integration harness answer different questions about your infrastructure.

        We compared the infrastructure as code testing tools for each layer in 2026, and answered "can you unit test Terraform?" directly.
---

Testing infrastructure as code means validating infrastructure definitions before they change real cloud resources, using static analysis, policy checks, unit tests, and integration tests against short-lived environments. It matters because infrastructure mistakes carry a large blast radius and slow feedback. A public bucket caught in a pull request is a one-line fix.

<!--more-->

This post comes from Pulumi's blog, so Pulumi appears in several entries, and we have tried to state its limits as plainly as the others. No single tool covers every layer. A linter answers "is this configuration well formed and safe?", a policy engine answers "is this change allowed?", a unit test answers "does my logic do what I intended?", and an integration test answers "does the deployed system work?" This guide compares widely used tools for each layer in 2026 and says where each one fits.

For a hands-on walkthrough, see [how to test infrastructure as code](/blog/how-to-test-infrastructure-as-code/). This post focuses on choosing tools.

## What does the infrastructure testing pyramid look like?

The classic test pyramid applies to infrastructure, with one adjustment: the top layer creates real cloud resources, so it costs money and minutes.

1. **Static analysis and policy checks** read code, plans, or resource properties without deploying anything. They run in seconds and catch misconfigurations and rule violations.
2. **Unit tests** run your logic with cloud calls mocked. They run in milliseconds to seconds and catch bugs in the code that generates resources, such as conditionals, loops, and naming.
3. **Integration tests** deploy to a short-lived environment, assert against real resources, and tear everything down. They take minutes and catch problems that only real cloud APIs reveal, such as IAM propagation, quota limits, and networking.

Aim for many fast checks at the bottom and a few high-value integration tests at the top.

## Which infrastructure as code testing tools should you compare?

| Tool | Test type | Language/DSL | CI integration |
| --- | --- | --- | --- |
| Checkov | Static analysis, policy | Python-based scanner; custom checks in Python or YAML | CLI, pre-commit, GitHub Actions and other CI systems |
| Trivy | Static analysis (misconfiguration scanning) | Go CLI; custom checks in Rego | CLI, official GitHub Action, container image |
| TFLint | Linting | Go CLI, HCL config, plugin rulesets | CLI, pre-commit, GitHub Action |
| Open Policy Agent and Conftest | Policy as code | Rego | Conftest CLI against plans and config files in any CI |
| HashiCorp Sentinel | Policy as code | Sentinel language | HCP Terraform and Terraform Enterprise policy checks |
| Pulumi Policies | Policy as code (pre-deployment and on existing resources) | TypeScript, Python, or Rego policy packs | Runs on `pulumi preview` and `pulumi up`, so any CI that runs the Pulumi CLI |
| Pulumi unit tests | Unit (mocked) | Same language as the program: TypeScript, Python, Go, C#, Java | Any test runner CI already uses, no cloud credentials needed |
| terraform test and tofu test | Unit (plan mode, mocks) and integration (apply mode) | HCL (`.tftest.hcl`) | CLI command, so any CI that runs Terraform or OpenTofu |
| AWS CDK assertions | Unit (synthesized template) | TypeScript, Python, Java, C#, Go | Standard test runner in CI |
| Terratest | Integration | Go | `go test` in any CI, needs cloud credentials |
| Pulumi integration tests and the Automation API | Integration | Any language (Automation API); Go framework | Any CI, needs cloud credentials |
| pulumi preview and review stacks | Plan diff, ephemeral per-PR environments | Pulumi CLI; any Pulumi language | Pull request comments through CI or Pulumi Deployments |
| LocalStack | Integration against an emulator | Language-agnostic; works with any tool that can set a custom endpoint | Docker container in CI |

## Which tools handle static analysis?

Static analysis is the cheapest layer and the one to adopt first. It needs no cloud credentials and runs on every commit.

### Checkov

Checkov is an open-source scanner maintained by Prisma Cloud (Palo Alto Networks). It ships with a large library of built-in checks across Terraform, CloudFormation, Kubernetes manifests, Helm charts, Dockerfiles, and more, and it can scan Terraform plan output as well as source files. Custom checks are written in Python or YAML.

**Best for:** teams that want broad security coverage with minimal setup and a mix of formats in one repository.

**Limits:** it evaluates configuration, not behavior, so it cannot tell you whether your module logic produces the right number of subnets. Built-in checks reflect common benchmarks, so expect to suppress or tune some for your environment.

### Trivy

Trivy, from Aqua Security, scans container images, filesystems, and infrastructure configuration. Its misconfiguration scanning absorbed the earlier tfsec project, which Aqua now points users away from in favor of Trivy. It covers Terraform, CloudFormation, Kubernetes, Dockerfiles, and Helm, and custom checks are written in Rego.

**Best for:** teams that already scan images with Trivy and want one scanner for images and IaC configuration.

**Limits:** it checks static properties, so coverage depends on rules for the resource types you use.

### TFLint

TFLint is a Terraform linter with provider-aware rulesets for AWS, Azure, and Google Cloud. It catches issues such as invalid instance types, deprecated syntax, and unused declarations, beyond what `terraform validate` reports.

**Best for:** Terraform and OpenTofu repositories that want fast feedback on correctness and style.

**Limits:** it targets HCL, so it does not apply to programs in other languages, and it focuses on correctness more than security policy.

## Which tools enforce policy as code?

Policy engines decide whether a change is allowed. They are the layer where platform and security teams encode rules once and apply them to every team. For a deeper comparison, see [best policy as code tools](/blog/best-policy-as-code-tools/).

### Open Policy Agent and Conftest

Open Policy Agent (OPA) is a general-purpose policy engine with a declarative language called Rego. Conftest is a CLI that runs Rego policies against structured files, which makes it a common way to check `terraform show -json` plan output, Kubernetes manifests, or any JSON and YAML configuration.

**Best for:** organizations that want one policy language across Terraform plans, Kubernetes, and other systems.

**Limits:** Rego has a learning curve for engineers used to imperative languages, and policies against plan JSON depend on the plan's structure, so they need maintenance as providers change.

### HashiCorp Sentinel

Sentinel is HashiCorp's policy framework, integrated into HCP Terraform and Terraform Enterprise. Policies run between plan and apply and can be advisory, soft-mandatory, or hard-mandatory.

**Best for:** teams standardized on HCP Terraform or Terraform Enterprise that want policy enforcement built into the run workflow.

**Limits:** it uses its own language and is tied to the Terraform workflow. HCP Terraform also supports OPA policies, which is the route for teams that prefer Rego.

### Pulumi Policies

Pulumi Policies lets you write policy packs in TypeScript, Python, or Rego and enforce them during `pulumi preview` and `pulumi up`, so a violating change can be blocked before any resource is created. Policies receive resource inputs, and after deployment they can also inspect outputs, which allows rules about values only the cloud provider knows. Packs can also scan resources that already exist in connected cloud accounts.

**Best for:** teams that want policy written in a general-purpose language they already know, with enforcement tied to the deployment engine.

**Limits:** enforcement lives in the Pulumi workflow, so it is the natural choice for Pulumi stacks and a poor fit for other tools. Centrally managed policy groups and scanning of existing resources are Pulumi Cloud features, so check which editions include what you need. Its ecosystem of ready-made rules is smaller than Checkov's.

## Which tools support unit testing?

Unit tests validate the logic that generates your infrastructure. The key question for each tool is how much of the surrounding software testing ecosystem you can reuse.

### Pulumi unit tests

Pulumi programs are ordinary programs in TypeScript, Python, Go, C#, or Java, so unit tests use the frameworks those ecosystems already have: Mocha or Jest for TypeScript, pytest for Python, `go test` for Go, NUnit or xUnit for C#, and JUnit for Java. The Pulumi SDK provides a mocking hook that replaces cloud provider calls with fakes. Tests run in memory, in milliseconds, with no cloud credentials and no Pulumi CLI, and the same CI job that runs application tests can run them.

Here is a minimal TypeScript example. It assumes `index.ts` exports `bucket`, an `aws.s3.BucketV2` created with an `owner` tag:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as assert from "assert";

pulumi.runtime.setMocks({
    newResource: (args) => ({ id: `${args.name}-id`, state: args.inputs }),
    call: (args) => args.inputs,
}, "demo", "test", false);

describe("storage", () => {
    let infra: typeof import("./index");

    before(async () => {
        infra = await import("./index");
    });

    it("tags the bucket with an owner", async () => {
        const tags = await new Promise<Record<string, string> | undefined>(
            (resolve) => infra.bucket.tags.apply(resolve),
        );
        assert.ok(tags && tags["owner"], "bucket must have an owner tag");
    });
});
```

Because the test is code, you can generate cases in a loop, share fixtures across stacks, mock a dependency with your usual mocking library, and fail a build on coverage. These are the same techniques you use for application code, with no extra framework to learn.

**Best for:** teams that want fast feedback on conditionals, loops, component logic, and naming without deploying.

**Limits:** mocks return what you tell them to, so these tests exercise your logic and the inputs you pass, and say nothing about how the real cloud responds. The mocks and the dynamic import in the example add setup you write yourself. Mock-based unit tests need a general-purpose language runtime, so programs written in YAML are covered by integration tests instead.

### terraform test and tofu test

Terraform 1.6 introduced a native test framework: test files with a `.tftest.hcl` extension containing `run` blocks and `assert` conditions. By default each run applies real infrastructure, which is integration testing. Setting `command = plan` validates logic without creating resources, and Terraform 1.7 added the ability to mock provider data, which enables faster unit-style tests. OpenTofu provides the same workflow through `tofu test`, with mock providers arriving in OpenTofu 1.8.

**Best for:** validating Terraform and OpenTofu modules with tooling that ships in the CLI and needs no extra dependencies.

**Limits:** tests and assertions are written in HCL, so you work within HCL expressions rather than a general-purpose language. Mocked tests are most natural for module inputs and plan-time logic. See the FAQ below for more.

### AWS CDK assertions

The AWS CDK includes an assertions library. A test synthesizes a stack to a CloudFormation template, then checks it with helpers such as `Template.fromStack` and `hasResourceProperties`. Tests are written in the same language as the CDK app and run with that language's test runner.

**Best for:** AWS-only teams already using the CDK.

**Limits:** assertions cover the synthesized template, not live behavior.

## Which tools handle integration testing?

Integration tests deploy to a real, short-lived environment and verify behavior from the outside. They are the slowest and most expensive layer, so use them for the paths that matter most.

### Terratest

Terratest, from Gruntwork, is a Go library for writing automated infrastructure tests. A typical test applies a Terraform module with `terraform.InitAndApply`, runs assertions such as an HTTP request against the output URL, and destroys everything in a deferred cleanup.

**Best for:** end-to-end tests of Terraform, OpenTofu, Packer, or Kubernetes setups by teams comfortable writing Go.

**Limits:** tests need cloud credentials, take minutes, and cost real money. Teams that do not use Go take on a second language for tests.

### Pulumi integration tests and the Automation API

Pulumi offers two routes to integration testing. The Go integration test framework deploys a program, runs validation callbacks, and tears the stack down, though it requires Go. The Automation API drives Pulumi from code, so you can create a stack, deploy it, read its outputs, assert against them, and destroy the stack from a test in TypeScript, Python, Go, C#, or Java. Unlike unit tests, integration tests also work for programs written in YAML.

**Best for:** end-to-end validation of Pulumi stacks in the language your tests already use.

**Limits:** like all real-deployment tests, they require credentials, run for minutes, and incur cloud costs. The Automation API removes the Go requirement but needs the Pulumi CLI installed.

### pulumi preview and review stacks

`pulumi preview` shows the diff a change would produce without applying it. The `--expect-no-changes` flag fails the command when any change is proposed, which makes it useful for drift checks and refactoring PRs that should change nothing. Pulumi Deployments review stacks go a step further: they create an ephemeral stack for each pull request so reviewers can see the real deployed result. Time-to-live (TTL) stacks are destroyed automatically after a set period, which keeps test environments from piling up.

**Best for:** catching unintended changes at review time and giving every PR an isolated environment.

**Limits:** a preview reports what the engine plans to do and cannot confirm that the deployed system behaves correctly. Review stacks create real resources and need the same budget attention as any ephemeral environment.

### LocalStack

LocalStack emulates many AWS services locally in a Docker container. Terraform, OpenTofu, Pulumi, and the CDK can all point at it by overriding endpoints, which gives you integration-style tests with no cloud account and fast startup.

**Limits:** an emulator approximates AWS and does not replicate every service or behavior, and check current LocalStack docs for which services each edition includes. Treat it as a fast pre-check and keep some tests against the real cloud.

## How does Pulumi approach infrastructure testing?

Pulumi's approach starts from one fact: a Pulumi program is real code in a general-purpose language. That means the testing pyramid maps directly onto tools your team already runs. Unit tests use pytest, Jest, `go test`, xUnit, or JUnit. Integration tests drive stacks through the Automation API from the same test framework. Policy checks run inside `pulumi preview`. Pipelines run all of it in the CI system you already have, next to your application tests, with the same coverage reports and the same review habits. The [Pulumi testing guide](/docs/iac/guides/testing/) covers unit, property, and integration testing in detail.

Pulumi has costs too. There is no built-in `pulumi test` command, so you bring and wire up your own test runner. Mocks must be registered before the program loads and you write the fake provider responses yourself. A polyglot organization maintains test patterns in several languages. Review stacks, TTL stacks, and centrally managed policy are Pulumi Cloud features. Teams that prefer a single declarative syntax with testing built into the CLI may find HCL-native tools a simpler fit.

## How do you assemble a testing pipeline?

A pipeline that works for most teams runs the layers in order of cost, and stops at the first failure:

1. **Format and lint** on every commit: TFLint for Terraform, or your language's linter and type checker for Pulumi and CDK programs.
2. **Static scan** on every pull request: Checkov or Trivy against source or plan output.
3. **Unit tests** on every pull request: Pulumi mocks, `terraform test` in plan mode, or CDK assertions.
4. **Policy check** against the plan or preview: Conftest with Rego, Sentinel, or Pulumi Policies.
5. **Integration tests** against an ephemeral environment on pull requests that touch critical modules, or nightly: Terratest, the Pulumi integration tools, or review stacks.
6. **Preview or plan review** before merging, then deploy from CI with a manual approval for production.

Start with steps 1 and 2. They take an afternoon and catch many common mistakes.

## Can you unit test Terraform?

Yes, with limits. Terraform 1.6 added `terraform test` with `.tftest.hcl` files. Running a test with `command = plan` validates logic without creating resources, and Terraform 1.7 added mock providers and overrides so tests can run without cloud credentials. OpenTofu supports the same model through `tofu test`, with mock providers added in 1.8.

The main constraint is the language. Assertions are HCL expressions, so tests use HCL's own constructs (variables, multiple `run` blocks, `expect_failures`) in place of a general-purpose language's frameworks, libraries, and mocking tools. Plan-mode tests can only assert on values known at plan time, and values computed by the cloud at apply time need an apply-mode run against real resources. For deeper scenarios, such as making HTTP requests to a deployed endpoint, teams typically add Terratest, written in Go. A common combination is `terraform test` for module logic, Checkov for security, and Terratest for a few end-to-end checks.

## What should you use to test infrastructure code with mocked cloud resources and your normal test framework?

If your infrastructure is written in a general-purpose language, use the test framework you already have: pytest, Jest, Mocha, `go test`, xUnit, NUnit, or JUnit, plus the SDK's mocking hook. Pulumi's SDK mocks provider calls in TypeScript, Python, Go, C#, and Java. Terraform 1.7 and OpenTofu 1.8 support mock providers in `.tftest.hcl` files. The AWS CDK synthesizes templates locally, so assertions need no mocking at all. Mocked tests verify your logic and inputs, so pair them with a smaller set of tests against real resources.

## How do you spin up real cloud resources for integration tests and tear them down afterward?

Three common patterns work. Terratest wraps apply and destroy inside a Go test. The Pulumi Automation API creates a stack, deploys it, runs assertions, and destroys it from a test in your language of choice. Pulumi Deployments review stacks create an environment per pull request, and TTL stacks clean up automatically. Whichever you pick, give each run a unique name and destroy resources in a cleanup step that runs on failure.

## Checkov vs OPA: which should you use?

They solve adjacent problems. Checkov ships ready-made checks, so you get coverage on day one. OPA with Conftest gives you a general policy language for your organization's own rules across Terraform plans, Kubernetes, and other systems. Many teams run both: Checkov as a baseline and OPA for custom rules.

## How do you test Kubernetes infrastructure changes before deploying to a shared cluster?

Scan manifests and Helm charts with Checkov or Trivy, enforce cluster rules with OPA or Pulumi Policies, and apply the change to a short-lived cluster such as kind in CI. Use a preview or plan diff as the final gate.

## Where should you start?

Pick the cheapest layer you have not adopted yet. With no checks today, add a static scanner this week. With scanners but no unit tests, write three for the modules that change most. With both, add one nightly integration test for your most critical path.
