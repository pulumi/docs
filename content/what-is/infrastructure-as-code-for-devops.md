---
title: Infrastructure as Code for DevOps
meta_desc: "How infrastructure as code enables a modern DevOps program: CI/CD for the platform, shift-left testing, policy as code, and platform engineering."

type: what-is
page_title: "Infrastructure as Code for DevOps"

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

**Infrastructure as code (IaC) is the substrate that makes DevOps work at cloud scale: every cloud resource is defined in version-controlled code, every change ships through CI/CD, and every policy and test that applies to application code now applies to the platform underneath it.** Without IaC, the rest of a DevOps program (CI/CD, automated testing, policy as code, blameless postmortems, platform engineering) doesn't have anything to act on past the application boundary.

[DevOps](/what-is/what-is-devops/) is a culture and a set of practices for shipping software faster and more reliably. [Infrastructure as code](/what-is/what-is-infrastructure-as-code/) is the technical practice that turns the cloud platform itself into something teams can ship through the same pipeline as the app. Together they replace ticket-driven, console-clicking operations with a workflow where infrastructure is reviewed in pull requests, gated by automated tests and policies, and deployed by the same CI/CD systems that ship the application.

In this article, we'll cover the key questions about infrastructure as code for DevOps:

* Why does DevOps need infrastructure as code?
* How does IaC map onto the DevOps lifecycle?
* How does IaC support each CALMS pillar?
* How does IaC enable CI/CD for infrastructure?
* How does IaC enable shift-left testing and policy as code?
* How does IaC enable platform engineering and self-service?
* What is the maturity progression from manual ops to IaC-enabled DevOps?
* What tools support IaC for DevOps?
* How does Pulumi fit into a DevOps program?
* Frequently asked questions about IaC for DevOps

## Why does DevOps need infrastructure as code?

DevOps grew up in the era when servers were long-lived and small in number. The cloud changed both: a modern stack has hundreds or thousands of resources, changing daily, across many accounts and providers. Three forces make IaC mandatory rather than optional for any serious DevOps program:

* **Scale.** No team can manage thousands of cloud resources by hand. The only way to keep environments consistent, auditable, and reproducible past a small footprint is to define them as code.
* **Speed.** DevOps measures itself on deployment frequency and lead time. Manual infrastructure provisioning adds days; codified infrastructure adds minutes. The performance gap between elite and low-performing teams in DORA's State of DevOps reports tracks closely with how automated the infrastructure pipeline is.
* **Risk.** Most cloud incidents are misconfigurations: open security groups, public buckets, wildcard IAM. Catching those in a code review and a CI policy check is much cheaper than catching them in production.

## How does IaC map onto the DevOps lifecycle?

The DevOps lifecycle (plan → code → build → test → release → deploy → operate → monitor) was originally drawn around application code. IaC extends each stage to cover the platform as well.

| Lifecycle stage | What IaC contributes |
|---|---|
| **Plan** | Infrastructure changes are scoped, designed, and threat-modeled alongside the application features that depend on them. |
| **Code** | Resources are defined in real programming languages, in the same repos and the same review process as the application code. |
| **Build** | The IaC program is the build artifact. Every commit produces a reproducible plan that can be replayed against any environment. |
| **Test** | Unit, property, integration, and security tests run against IaC programs in CI, the same way they run against applications. |
| **Release** | A reviewed, tested IaC plan is promoted toward production through gated environments (dev → staging → prod). |
| **Deploy** | The IaC engine applies the plan, with rollback as a first-class operation rather than a runbook. |
| **Operate** | Drift detection surfaces console-edits that diverge from the declared state, so the system stays in a known shape. |
| **Monitor** | Logs, metrics, and traces flow back into the next planning cycle. Findings from incidents become new IaC components, new tests, and new policies. |

## How does IaC support each CALMS pillar?

CALMS (Culture, Automation, Lean, Measurement, Sharing) is one of the most widely cited frameworks for what a DevOps culture looks like. IaC contributes directly to each pillar.

| Pillar | What IaC contributes |
|---|---|
| **Culture** | Application and platform changes flow through the same review process. Operations stops being an out-of-band ticket queue and becomes a peer to development. |
| **Automation** | Every cloud resource is provisioned by code. Manual console clicks are exceptions that get noticed by drift detection. |
| **Lean** | Smaller, more frequent infrastructure changes replace big-bang quarterly migrations. Failed changes are reverted in minutes. |
| **Measurement** | Deployment frequency, lead time, change-failure rate, and MTTR can be measured for the platform the same way they're measured for the product. |
| **Sharing** | Reusable infrastructure components and policy packs ship between teams. Platform teams package vetted patterns; product teams consume them. |

## How does IaC enable CI/CD for infrastructure?

The same CI/CD machinery that ships application code can ship infrastructure once it's in code. A typical flow:

1. An engineer opens a pull request that changes IaC.
1. CI runs static analysis, security scanners (Checkov, tfsec, Trivy), and unit tests against the IaC program.
1. CI runs `pulumi preview` (or equivalent) against the target environment and posts the diff to the PR.
1. [Policy as code](/docs/insights/policy/) checks the planned changes against organizational rules.
1. A human reviewer approves the diff. The PR merges.
1. CI runs `pulumi up` to apply the change to staging, then to production after smoke tests pass.
1. Drift detection runs on a schedule against the deployed state.

The principle is the same as application CI: fast feedback for in-progress changes, slower and broader checks closer to production. Pulumi integrates with all major CI/CD systems via [the Pulumi CI/CD integration guide](/docs/iac/guides/continuous-delivery/) and [GitHub Actions](/docs/iac/guides/continuous-delivery/github-actions/).

## How does IaC enable shift-left testing and policy as code?

"Shift left" means moving tests and policy checks as early in the pipeline as possible, ideally before merge. IaC makes both possible for the platform.

* **Unit tests** verify the logic of IaC programs in memory, with mocked cloud responses. Examples: every resource is tagged, no security group opens SSH to the internet, encryption is enabled on every bucket.
* **Property tests** assert specific properties on the planned resource graph (every database has backups enabled with a 7-day retention; every Kubernetes cluster uses the LTS provider version).
* **Integration tests** spin up ephemeral stacks in a sandbox account, run end-to-end assertions, and tear down.
* **Policy as code** enforces organizational rules across every change. [Pulumi CrossGuard](/docs/insights/policy/) lets you write policies in TypeScript, Python, or OPA's Rego and run them against `pulumi preview` so non-compliant changes never merge. Those policies apply to Pulumi stacks written in any supported language.
* **Security scans** (Checkov, tfsec, Snyk IaC) run on every commit and surface known-bad configurations.

For deeper coverage of each layer, see [how to step up cloud infrastructure testing](/what-is/how-to-step-up-cloud-infrastructure-testing/).

## How does IaC enable platform engineering and self-service?

[Platform engineering](/what-is/what-is-platform-engineering/) is the organizational pattern most teams reach for once their DevOps program grows past a handful of services. A platform team builds an internal developer platform (IDP) that paves the road for product teams: standard CI/CD, standard infrastructure templates, standard policy and observability.

IaC is the substrate for that platform:

* **Reusable components.** Platform teams ship [Pulumi components](/docs/iac/concepts/components/) that bundle the right defaults: encryption, logging, IAM, network placement, autoscaling. Product teams consume secure infrastructure without re-deriving every choice.
* **Policy as code.** Organization-wide rules (no public buckets, no wildcard IAM, mandatory tags) are enforced uniformly across every team's stack.
* **Self-service interfaces.** The platform team's components and policies define what product teams can self-serve. Pulumi's automation API turns those components into APIs, web forms, or chatbot commands, so non-platform engineers can provision compliant infrastructure on demand.
* **Golden paths.** Pre-built stacks for the most common patterns (a stateless service, a queue-driven worker, a customer-facing API) become one-command operations.

Without IaC, every team reinvents the same VPC, the same IAM, the same logging setup, and the platform team is reduced to writing wiki pages. With IaC, the same patterns become version-controlled, testable, reusable software.

## What is the maturity progression from manual ops to IaC-enabled DevOps?

Most organizations move through some version of this progression as their DevOps program matures:

1. **Console clicks.** Engineers create resources by hand in the cloud console. Reproducibility is whatever a runbook says.
1. **Shell scripts.** Console steps get translated to CLI calls and checked into a repo. Faster, but every partial failure leaves the system in an unknown state.
1. **Imperative SDK code.** Cloud provider SDKs in a real programming language. Cleaner error handling, still procedural.
1. **Declarative IaC.** A program describes the desired state of the system; an engine reconciles real infrastructure to match. Drift is detectable; rollback is a first-class operation.
1. **IaC + CI/CD + policy as code.** Every change is a pull request gated by automated tests and policies. Infrastructure ships at the same cadence as application code.
1. **Platform-engineered IaC.** The platform team ships reusable components, golden paths, and policy packs. Product teams self-serve compliant infrastructure through curated interfaces.

The DORA performance brackets (low, medium, high, elite) roughly track this progression. Teams stuck on steps 1–2 deploy infrequently and recover slowly; teams operating at steps 5–6 deploy on demand with low change-failure rates.

## What tools support IaC for DevOps?

A DevOps toolchain built around IaC typically combines tools from several categories:

| Category | Representative tools |
|---|---|
| Source control | GitHub, GitLab, Bitbucket |
| CI/CD | GitHub Actions, GitLab CI, CircleCI, Jenkins, Buildkite, Argo CD |
| Infrastructure as code | [Pulumi](/), Terraform, OpenTofu, AWS CloudFormation, Bicep |
| Policy as code | [Pulumi CrossGuard](/docs/insights/policy/), Open Policy Agent (OPA), HashiCorp Sentinel |
| Static IaC scanning | Checkov, tfsec, Terrascan, Snyk IaC |
| Containers and orchestration | Docker, Podman, Kubernetes, ECS |
| Secrets and config | [Pulumi ESC](/product/esc/), HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| Observability | Prometheus, Grafana, Datadog, New Relic, OpenTelemetry |
| Incident management | PagerDuty, Opsgenie, FireHydrant, Rootly |

The point isn't the longest stack; it's a connected one where IaC sits at the center and every other tool reads from or writes to the same source of truth.

## How does Pulumi fit into a DevOps program?

Pulumi is IaC built for engineering teams that already use DevOps practices. Concrete patterns:

* **Real languages.** Write IaC in TypeScript, Python, Go, C#, Java, or YAML. The same languages, test runners, and IDE tooling that work for application code work for the platform.
* **Same review process.** Pulumi programs live in the same repos as application code (or in their own platform repos). Every change is a pull request with a diff that reviewers can read.
* **CI/CD-native.** Pulumi runs in every major CI/CD platform. The [Pulumi GitHub Actions integration](/docs/iac/guides/continuous-delivery/github-actions/) and [CI/CD guide](/docs/iac/guides/continuous-delivery/) document common patterns.
* **Policy as code through CrossGuard.** Write policies in the same language as the IaC. Run them on every preview and update.
* **Secrets through Pulumi ESC.** Centralized, encrypted, audited. [Pulumi ESC](/product/esc/) pulls secrets at runtime into Pulumi programs, CI jobs, and applications without leaving plaintext copies in code or state.
* **Self-service through automation API.** The [automation API](/docs/iac/packages-and-automation/automation-api/) turns Pulumi programs into libraries that other software can call, which is how platform teams expose self-service over their components.

[Get started with Pulumi](/docs/get-started/) to put your cloud infrastructure on the same engineering footing as your application code.

## Frequently asked questions about IaC for DevOps

### Is IaC the same thing as DevOps?

No. DevOps is the broader culture and set of practices for delivering software. IaC is one specific technical practice within DevOps that extends the same engineering disciplines to cloud infrastructure. You can have DevOps without IaC (poorly) and IaC without DevOps (rare), but together they reinforce each other.

### Can I do DevOps without infrastructure as code?

Past a small footprint, not really. Manual provisioning makes the DORA metrics (deployment frequency, lead time, change-failure rate, MTTR) harder to move in the right direction, and it makes shift-left testing of the platform layer impractical. Most serious DevOps programs end up at IaC even if they didn't plan to.

### What's the difference between declarative and imperative IaC?

Declarative IaC describes the desired state; an engine reconciles real infrastructure against it. Imperative IaC describes the steps; the tool runs them in order. Declarative is more common for cloud infrastructure because it handles partial failure, drift, and rollback. See [What is Infrastructure as Code?](/what-is/what-is-infrastructure-as-code/) for the deeper comparison.

### How does IaC affect deployment frequency?

It dramatically increases it. Manual environment setup measured in days becomes a `pulumi up` measured in minutes. Once application and infrastructure changes flow through the same CI/CD pipeline, deploying becomes a routine event rather than a project.

### Where does policy as code fit in?

Policy as code is the enforcement layer for organizational rules: no public buckets, no wildcard IAM, every resource must have an owner tag, every database must have backups. Policies run on every IaC change in CI, so non-compliant changes never reach production. In Pulumi, [CrossGuard](/docs/insights/policy/) is the policy-as-code engine.

### How does IaC support compliance frameworks like SOC 2 or HIPAA?

By producing audit-grade evidence as a byproduct of normal work. Every change is a reviewed pull request with author, approver, and timestamp; every policy violation is logged; every deploy is recorded. Auditors get a concrete artifact that proves a control was enforced on a specific change at a specific time, which is much stronger than "we have a policy that says..."

### Does IaC replace configuration management tools like Ansible or Chef?

Mostly yes for cloud-native workloads. Chef, Puppet, and Ansible were built for the era of long-lived servers that needed in-place configuration. With immutable infrastructure and containers, most of that configuration moves into the image build, leaving IaC as the primary discipline for provisioning. Configuration management still has a role for VM fleets and legacy systems.

### How does IaC fit with Kubernetes?

Kubernetes manifests are themselves a form of declarative infrastructure code; tools like Helm and Kustomize layer on top. Pulumi can also manage Kubernetes alongside the rest of the cloud platform, which keeps the cluster and the workloads in one program. See [infrastructure as code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/) for the Kubernetes-specific patterns.

### How do you measure the impact of adopting IaC for DevOps?

DORA's four key metrics: deployment frequency, lead time for changes, change-failure rate, and mean time to recover. Track a single value stream for at least a quarter before and after the IaC adoption to see the trend. Most teams see lead time drop first, then deployment frequency, then change-failure rate.

### How do I introduce IaC to a team that's been running manual ops?

Start with one new service or one well-defined existing piece of infrastructure. Get it into Pulumi, set up CI/CD around it, write a few unit tests and a policy. Use that as the template for the next service. Avoid the "big-bang migration of everything" approach: it usually stalls, and the team learns more from shipping one thing well.

## Learn more

Pulumi puts cloud infrastructure on the same engineering footing as application code: real programming languages, real testing tools, real CI/CD, real policy as code. That's what makes the DevOps lifecycle work end to end for the cloud, not just for the app on top. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
* [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
* [How to Step Up Cloud Infrastructure Testing](/what-is/how-to-step-up-cloud-infrastructure-testing/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
