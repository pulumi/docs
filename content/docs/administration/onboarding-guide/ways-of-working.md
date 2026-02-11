---
title: Ways of working
meta_desc: Key decisions around team structure, project organization, and collaboration workflows.
aliases:
  - /docs/pulumi-cloud/get-started/onboarding-guide/ways-of-working/
  - /docs/deployments/get-started/onboarding-guide/ways-of-working/
weight: 2
menu:
    administration:
        name: Ways of working
        parent: pulumi-onboarding-guide
        identifier: ways-of-working
---
Your approach to organizing teams and projects will shape how your organization collaborates on cloud infrastructure. This section covers the key decisions around team structure, project organization, and collaboration workflows that will set your teams up for success.

## Structuring your projects

Pulumi's project model is intentionally flexible to support many different architectures and working styles. However, you'll need to make some decisions up front about how to structure your projects.

### Understanding projects and stacks

Both Pulumi IaC and Pulumi ESC have a notion of **project**—an abstract concept defining a collection of related configurations. Pulumi IaC projects have any number of **stacks** (instances of that project), while Pulumi ESC projects have **environments** (groups of related secrets and configuration).

Think of an IaC project like a Git repository and a stack like a Git branch. Just as teams structure Git repos differently—some prefer monolithic repos while others prefer smaller, single-purpose repos—you can structure Pulumi projects in various ways.

### Choosing your project architecture

Most teams prefer smaller, purpose-built projects. This makes securing and deploying them independently easier, though it does add complexity as your architecture becomes made up of many interdependent stacks.

A typical team might have these IaC projects:

- **Security layer**: IAM roles, KMS keys, etc.
- **Networking base layer**: VPCs, subnets, etc.
- **Multiple Kubernetes clusters**: Defined and configured differently
- **Multiple database projects**: Data lakes, MySQL infrastructures, etc.
- **Application projects**: Containerized, VM-based, or serverless applications

These projects can depend on one another—for instance, the Kubernetes project likely needs VPC and subnet IDs exported from the networking base layer.

For stacks, you might have:

- **Production**: us-west, us-east, and Europe
- **Staging**: In fewer regions
- **Development**: Many stacks, perhaps one per developer

Each IaC project has its own set of stacks, so you may want ESC environments representing each logical grouping.

{{% notes type="info" %}}

Learn more about [organizing projects and stacks](https://www.pulumi.com/docs/using-pulumi/organizing-projects-stacks/) here.

{{%/notes%}}

### Deciding on a language strategy

Pulumi's polyglot nature supports the top programming languages: Python, Go, Node.js languages (JavaScript, TypeScript), .NET languages (C#, F#), JVM languages (Java, Groovy, Scala, Clojure), and YAML for simple use cases. [Learn more about language support](https://www.pulumi.com/docs/languages-sdks/).

You have two main options:

**Single-language (recommended for most teams)**
This approach makes it easier to standardize on tools, patterns, and practices, and to train your team. Choose the language your team already uses to leverage existing standards.

**Multi-language (common in large organizations)**
While offering flexibility, this approach risks fragmentation between teams using different languages. Pulumi addresses this through consistent experiences across languages in Pulumi Cloud and Pulumi Policies, plus [Pulumi Packages](https://www.pulumi.com/docs/iac/guides/packages/) that let you author packages in one language and consume them in another.

## Organizing people for collaboration

Your Pulumi Cloud hierarchy consists of **users**, **organizations**, and **teams**. Each plays a critical role in how your team collaborates and enforces security and best practices.

### Setting up your organization

Start by creating an organization—a container for your IaC projects and stacks, ESC projects and environments, and Insights accounts and discovered resources. Most companies need only a single organization, though you can create multiple if you require extra separation or multiple identity providers. The infrastructure platform group typically owns this configuration and handles onboarding developers and security experts.

Organizations and their capabilities are a paid feature of Pulumi Cloud. Creating an organization starts a free trial. [Create your organization here](https://app.pulumi.com/site/organizations/add).

### Creating teams

Teams are groups of individual users that typically reflect your company's structure or working groups. By organizing members into teams, you can control which projects, stacks, and environments they can access, and with what permissions, through role-based access control (RBAC). Teams and roles change frequently, so Pulumi Cloud makes it easy to reconfigure teams or automatically sync with your identity provider. [Learn more about teams](https://www.pulumi.com/docs/administration/organizations-teams/teams/).

### Configuring Single Sign-On (SSO)

Many organizations prefer to use Single Sign-On (SSO) with identity providers like Microsoft Entra ID, Google Workspace, Okta, or any SAML 2.0 compliant provider. If you have SSO with System for Cross-domain Identity Management (SCIM) enabled, onboarding and offboarding happen automatically. Otherwise, you can continue using email, GitHub, GitLab, or Atlassian identity. [Learn about configuring SSO](https://www.pulumi.com/docs/administration/access-identity/saml/).

Once you've completed the setup steps, you're ready to invite your team. Refer to [Inviting members to an organization](https://www.pulumi.com/docs/administration/organizations-teams/organizations/#inviting-members-to-an-organization) for detailed instructions.

### Creating productive developer experiences

It's common to give developers their own stacks for development and testing. Pulumi's projects and stacks model makes this easy and leads to fast, productive experiences.

**Developer stack patterns:**

- **Individual developer stacks**: Each developer gets their own complete environment
- **Shared infrastructure**: Developers share costly resources like databases while having their own application instances
- **[Review stacks](https://www.pulumi.com/docs/deployments/deployments/review-stacks/)**: Short-lived stacks for each pull request that are automatically torn down
- **[TTL stacks](https://www.pulumi.com/docs/deployments/deployments/ttl/)**: Automatically destroyed after a specified timeframe to prevent cloud waste

Use [stack references](https://www.pulumi.com/blog/iac-recommended-practices-using-stack-references/) to factor out shared infrastructure and create flexible project architectures.

### Enabling developer self-service

Platform engineering teams often want to enable application and backend developers to self-serve their infrastructure needs while maintaining security, compliance, and cost controls. Pulumi enables self-service with guardrails through three main models:

**1. Direct Pulumi IaC access**
Developers interface with Pulumi directly, typically using separate teams with different RBAC settings. Use components, templates, and policies to enforce guardrails while providing simpler starting points.

**2. YAML interface**
Developers check in YAML files to a Git repository and let CI/CD handle the rest. Write components, templates, and policies with simple interfaces conducive to YAML usage. [Learn more about Pulumi YAML](https://www.pulumi.com/docs/languages-sdks/yaml/).

**3. UI-based experience**
Developers log into a portal and click buttons to provision infrastructure. Options include:

- [Pulumi IDP](https://www.pulumi.com/docs/idp/)
- [Pulumi's Backstage plugin](https://www.pulumi.com/blog/pulumi-backstage-plugin/)
- Custom portals powered by [Pulumi's Automation API](https://www.pulumi.com/docs/using-pulumi/automation-api/)

[Learn more about building developer portals](https://www.pulumi.com/docs/idp/concepts/).

## Working together on deployments

With Pulumi, your entire team can collaborate and ship cloud applications and infrastructure faster with guardrails that ensure security, compliance, and best practices.

### Deploying continuously

While most teams start by running the Pulumi CLI manually, you'll eventually want to automate workflows, especially for production environments. The most common workflow is deploying IaC configuration changes through Git-based CI/CD.

**CI/CD platform options:**

- **[Pulumi Deployments](https://www.pulumi.com/docs/deployments/deployments/)** (recommended): Purpose-built for IaC deployments and integrated into Pulumi Cloud
- **[Pulumi Kubernetes Operator](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/)**: Trigger deployments from within Kubernetes clusters
- **Existing CI/CD solutions**: GitHub Actions, GitLab CI, Octopus Deploy, and [many others](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/)

**GitHub users**: Install the [Pulumi GitHub App](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/github-app/) for instant GitOps workflow support, including deployment previews in pull requests.

**GitLab users**: Use the [Pulumi GitLab Integration](https://www.pulumi.com/docs/iac/using-pulumi/continuous-delivery/gitlab-app/) to set up Pipelines and Webhooks for GitLab CI/CD.

**Setting up CI/CD:**

1. Choose your platform
2. Define your branching strategy (e.g., does main map to production?)
3. Configure your pipelines and testing strategies
4. Set up [Pulumi Cloud access tokens](https://www.pulumi.com/docs/administration/access-identity/access-tokens/) for automation

### Guarding against drift

Drift occurs when changes happen outside your IaC pipeline, causing conflicts between your last known deployment and your cloud resources' current state. This can cause security issues or outages during your next deployment. Pulumi supports [detecting and remediating drift](https://www.pulumi.com/docs/deployments/deployments/drift).

## Integrating with and extending Pulumi

Pulumi was built with extensibility in mind, following a "building blocks" philosophy where every service is powered by APIs you can access for custom workflows and system requirements.

### Extending Pulumi with custom workflows

**[Pulumi Cloud REST API](https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/)**
The well-documented, powerful API that powers the CLI and cloud console experiences.

**[Pulumi Automation API](https://www.pulumi.com/docs/using-pulumi/automation-api/)**
Embed IaC capabilities into any software, enabling custom tools, self-serve portals, complex deployment orchestrations, and even SaaS products that provision cloud resources.

**[Pulumi Cloud Webhooks](https://www.pulumi.com/docs/deployments/webhooks/)**
React to lifecycle events in Pulumi Cloud by invoking custom REST API endpoints. Use these for posting to Slack channels, triggering test runs after deployments, and more.

### Writing your own IaC providers

Pulumi supports hundreds of providers out of the box, but you can extend it further:

**[Custom providers](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/authoring/)**
Create providers for new or internal systems where neither Terraform nor Pulumi providers exist. This involves creating resource schemas and CRUD operations.

**[Terraform provider bridging](https://www.pulumi.com/blog/any-terraform-provider/)**
Bridge any Terraform provider at development time to use it from Pulumi IaC programs.

**[Dynamic providers](https://www.pulumi.com/docs/iac/concepts/providers/dynamic-providers/)**
Write CRUD logic inline in your Pulumi IaC program without building a separate provider.

### Contributing to open source

Pulumi's entire SDK is open source under the Apache 2.0 license, available in the [Pulumi GitHub organization](https://github.com/pulumi). With over 500 repositories, the Pulumi team is responsive and loves to collaborate in the open. [Read the Contributing to Pulumi guide](https://github.com/pulumi/pulumi/blob/master/CONTRIBUTING.md) to get started—pull requests are always welcome!

{{< get-started-stepper >}}
