---
title: How to Step Up Cloud Infrastructure Testing
meta_desc: "Learn how to test cloud infrastructure as code: unit, property, integration, and security tests, where each fits in CI/CD, and the tools to use."

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
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
authors: ["cam-soper"]
---

**Cloud infrastructure testing is the practice of validating the code that defines your cloud resources the same way you'd validate application code: with unit tests, property tests, integration tests, and security tests running in CI before changes reach production.** When infrastructure lives in source control as [infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/), the same engineering disciplines that catch bugs in applications can catch bugs in VPCs, IAM policies, Kubernetes clusters, and DNS records before they cause an outage or a compliance finding.

Most teams that adopt IaC stop at deploy-and-verify: spin up the resources, click around, hope for the best. That's the infrastructure equivalent of "no automated tests, just QA." It works for small estates and breaks badly at scale. A real testing program for infrastructure mirrors the testing pyramid software teams already use: fast tests run on every commit, slower tests run on PRs, the slowest run pre-deploy. This article walks through the layers, what each one catches, and how to wire them into a CI/CD pipeline.

In this article, we'll cover the key questions about cloud infrastructure testing:

* Why test infrastructure as code?
* What are the layers of infrastructure testing?
* What is IaC unit testing?
* What is property testing for infrastructure?
* What is integration testing for infrastructure?
* What is security and policy testing for infrastructure?
* Where do these tests fit in a CI/CD pipeline?
* What tools are used for infrastructure testing?
* How does Pulumi support infrastructure testing?
* Frequently asked questions about infrastructure testing

## Why test infrastructure as code?

Three reasons make automated infrastructure tests worth the investment:

* **Misconfigurations are the dominant source of cloud incidents.** Public buckets, overly broad IAM, open security groups, and missing encryption account for the majority of reported cloud breaches. The cheapest moment to catch any of those is a test that fails before the merge.
* **Manual review doesn't scale.** A typical cloud-native app spans hundreds of resources changing daily. No human reviewer reliably catches a regression like "the new module just opened SSH to the internet" by reading a diff. A test does.
* **Rollback is expensive.** Reverting an infrastructure change can cascade: dropped database, deleted secrets, broken DNS. Catching the issue in CI is dramatically cheaper than rolling forward through an incident.

## What are the layers of infrastructure testing?

Like application testing, infrastructure testing has layers that trade speed for fidelity.

| Layer | What it catches | Provisions real resources? | Typical runtime |
|---|---|---|---|
| **Static analysis / linting** | Syntax errors, obvious misconfigs, drift from project standards | No | Seconds |
| **Unit tests** | Logic in your IaC code (loops, conditionals, components) | No (mocked) | Seconds |
| **Property tests** | Constraints on the planned/deployed resource shape | No (or transient) | Seconds to minutes |
| **Integration / end-to-end tests** | Whether the resulting infrastructure actually works | Yes, ephemeral | Minutes to tens of minutes |
| **Security / policy tests** | Compliance, security posture, organizational rules | No or partial | Seconds |

A healthy program runs every layer; the cheap ones run on every commit, the expensive ones run on PRs or pre-deploy.

## What is IaC unit testing?

Unit tests verify the logic of your IaC programs without calling a cloud provider. External dependencies are replaced with mocks that return canned responses, so the test runs entirely in memory. Pulumi programs can be unit-tested using the standard test runners for the language you wrote them in (Jest/Vitest for TypeScript, pytest for Python, `go test` for Go, xUnit for C#, JUnit for Java).

Examples of what a unit test should assert:

* Every resource carries the required cost-allocation and ownership tags.
* No security group allows `0.0.0.0/0` ingress on port 22.
* A bucket's public-access-block is enabled in every environment.
* The right number of replicas is created when the stack is configured as `production`.

Unit tests run in seconds and produce the tightest feedback loop. The trade-off is that they only test what you wrote; they can't catch a problem in how the cloud provider actually behaves.

For Pulumi-specific patterns, see the [unit testing guide](/docs/iac/guides/testing/unit/).

## What is property testing for infrastructure?

Property tests run after a `pulumi preview` (or equivalent) produces a plan, against the planned resource graph or the freshly-deployed real resources. Unlike unit tests, they see actual cloud-provider outputs; unlike integration tests, they assert on specific resource properties rather than end-to-end behavior.

Property tests are well suited to enforcing organizational rules like:

* "The Kubernetes cluster must use the LTS provider version."
* "Every database must have backups enabled with at least a 7-day retention."
* "All compute lives inside a non-default VPC with private subnets."
* "Every service has logging enabled and shipped to the central log account."

In Pulumi, these checks are usually written as [policy as code](/docs/insights/policy/) using Pulumi Policies. The same policy code runs against `pulumi preview` (blocking the merge) and as a deploy-time gate.

## What is integration testing for infrastructure?

Integration tests deploy real cloud resources into an ephemeral environment, run end-to-end checks, then tear the environment down. They answer the question your unit and property tests can't: "Does the thing I just deployed actually work?"

A typical integration test:

1. Stand up a short-lived stack in a sandbox account using a unique stack name.
1. Wait for resources to converge.
1. Run assertions against the live system: hit a health-check URL, confirm a Lambda returns the expected response, run a SQL query, send a Kafka message and assert it lands.
1. Capture logs and metrics for failure diagnostics.
1. Tear down the stack.

Integration tests are the slowest and most expensive layer (they consume cloud resources), so run them selectively: on PRs that touch production-relevant code paths, on a nightly schedule, or as a deploy-time smoke gate.

See Pulumi's [integration testing guide](/docs/iac/guides/testing/integration/) for end-to-end test patterns.

## What is security and policy testing for infrastructure?

Security testing for IaC has two halves.

**Static scans of the code** catch known bad configurations before deploy: hardcoded secrets, public buckets, missing encryption, dangerous IAM. Tools like Checkov, Terrascan, Trivy, and Snyk IaC scan Terraform, CloudFormation, and Kubernetes manifests against built-in rulesets; Checkov also has a Pulumi-output mode. Run them in CI on every change.

**Policy as code** enforces the rules your security team writes for the organization itself. [Pulumi Policies](/docs/insights/policy/) lets you author policies in TypeScript/JavaScript, Python, or OPA's Rego against the actual Pulumi resource model, with three enforcement levels (`advisory`, `mandatory`, `disabled`). (Pulumi Policies apply to Pulumi stacks written in any supported language, including Go, .NET, and Java.) Policies run during `pulumi preview` and `pulumi up`, so a non-compliant change can't get past CI.

Beyond IaC-specific scans, the wider security testing menu still applies:

* **Vulnerability scanning** of container images and dependencies (Trivy, Snyk, Anchore).
* **Penetration testing** of the deployed system, scheduled or ad hoc.
* **Game days and chaos exercises** that deliberately break parts of the running system to test detection and response.

Whatever the mix, the consistent rule is **shift left**: every security check that can run in CI should, and the deploy gate should fail closed.

## Where do these tests fit in a CI/CD pipeline?

A common shape for an IaC pipeline:

1. **On every commit:** lint, static security scan (Checkov / Trivy), unit tests.
1. **On every pull request:** the above, plus `pulumi preview`, plus Pulumi policies in advisory mode.
1. **On merge to main:** `pulumi preview` against staging, deploy to staging, run integration tests against staging.
1. **On promotion to production:** Pulumi policies in mandatory mode, `pulumi up`, smoke tests against production.

The principle is the same as application CI: fast feedback for changes in progress, slower and broader checks closer to production.

## What tools are used for infrastructure testing?

| Category | Representative tools |
|---|---|
| Unit testing | Jest, Vitest, pytest, `go test`, xUnit, JUnit (standard test runners for the language you write IaC in) |
| Static IaC scanning | Checkov, Terrascan, Trivy, Snyk IaC |
| Policy as code | [Pulumi Policies](/docs/insights/policy/), Open Policy Agent (OPA), HashiCorp Sentinel |
| Property and integration testing | Pulumi automation API, Terratest, Kitchen-Terraform |
| Cloud emulation | LocalStack (AWS), Moto (AWS), Azurite (Azure) |
| Image and dependency scanning | Trivy, Snyk, Anchore, Grype |
| Chaos engineering | Gremlin, AWS Fault Injection Simulator, Chaos Mesh |

The point of a testing toolchain isn't to have the most tools; it's to have one tool covering each layer with a connection into CI, so a regression in any of them fails the build.

## How does Pulumi support infrastructure testing?

Pulumi treats infrastructure as software, which means every testing tool that exists for your application code is available for your IaC:

* **Real programming languages.** Write Pulumi programs in TypeScript, Python, Go, C#, Java, or YAML, and use the same test runners and mocking libraries you already know.
* **Unit testing with mocks.** Pulumi's [test mocks](/docs/iac/guides/testing/unit/) replace cloud provider calls with canned responses, so unit tests run in milliseconds and don't need any cloud credentials.
* **Integration testing through the automation API.** The [automation API](/docs/iac/packages-and-automation/automation-api/) lets you script `pulumi up` and `pulumi destroy` from a test runner, so integration tests can deploy and tear down ephemeral stacks programmatically.
* **Policy as code.** [Pulumi Policies](/docs/insights/policy/) run during preview and update, blocking changes that violate organizational rules. Policy packs are versioned and shipped alongside your code.
* **CI/CD integration.** Pulumi runs in every major CI/CD platform via the [GitHub Actions integration](/docs/iac/guides/continuous-delivery/github-actions/) or any other system that can run a CLI.

[Get started with Pulumi](/docs/get-started/) to provision and test infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about infrastructure testing

### Why test infrastructure at all?

The same reason you test applications: to catch defects when they're cheap to fix. An IAM misconfiguration found in CI costs a few seconds of compute; the same misconfiguration in production can cost a breach.

### What's the difference between IaC unit tests and integration tests?

Unit tests run in memory with mocked cloud responses, so they're fast (seconds) but only test the logic of your IaC code. Integration tests deploy real cloud resources to an ephemeral environment and assert on the running system, so they're slow (minutes) but catch problems that only show up against the real cloud provider.

### Do I need to write tests for every resource?

No. Test the resources and modules that carry real risk: anything with security implications (IAM, networking, secrets), anything that's reused across many stacks (shared components), and anything whose failure would cause an outage. Treat one-off resources the same way you treat one-off scripts.

### What is "property testing" in the IaC sense?

A check that runs against the planned or deployed resource graph and asserts properties on it (for example: every database has backups enabled, every Kubernetes cluster uses the supported version). In Pulumi, property tests are typically written as [Pulumi policies](/docs/insights/policy/).

### How do I test infrastructure without spending a lot on cloud resources?

Run unit tests with mocks for the bulk of your testing. Use cloud emulators (LocalStack, Moto, Azurite) where the provider's behavior is well-modeled. Reserve real-cloud integration tests for the highest-value scenarios, run them in cheap regions, and tear down stacks as soon as the test finishes.

### Should security tests run before or after deploy?

Both. Static scanning and policy as code should run before deploy so non-compliant changes never reach production. Dynamic scanning, penetration testing, and chaos exercises run against the deployed system because they can only see runtime behavior.

### How does test-driven development work for infrastructure?

The same way as for applications: write a test that describes the resource you want (right tag, right encryption, right policy), watch it fail, write the IaC that makes it pass, then refactor. TDD is particularly effective when building reusable infrastructure components, because the tests document the component's contract.

### What's the role of policy as code?

Policy as code is the operating model for organization-wide rules: things like "every database must have backups," "no public S3 buckets," "all compute must be tagged with an owner." Policies live in version control alongside the infrastructure they govern, run automatically on every change, and produce auditable evidence that the rules are enforced.

### Do compliance frameworks (SOC 2, HIPAA, PCI) accept IaC test results as evidence?

Yes — SOC 2, HIPAA, and PCI DSS audits routinely accept IaC test output and policy-as-code run logs as evidence that a control is enforced. A Pulumi Policies run, for example, produces a record of a control being checked against a specific change at a specific time, which is more concrete than a written policy with no enforcement mechanism behind it.

### How do I introduce testing to an existing IaC codebase?

Start with the cheapest layer that produces the most value: static scanning and policy as code in advisory mode. That gives you a baseline of how compliant the current codebase is without blocking anyone. Promote policies to mandatory mode as you remediate findings. Add unit tests to new components as you write them; add integration tests around the highest-risk modules first.

## Learn more

Pulumi lets you take advantage of the testing frameworks, mock libraries, and CI/CD tooling that already work for your application code, and apply them to your infrastructure. Combined with [Pulumi policy as code](/docs/insights/policy/), [the automation API](/docs/iac/packages-and-automation/automation-api/), and a real testing pyramid, that closes the gap between how teams treat application code and how they treat the cloud infrastructure it runs on. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [Infrastructure as Code for DevOps](/what-is/infrastructure-as-code-for-devops/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
