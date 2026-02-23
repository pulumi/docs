---
title: Pulumi Cloud
layout: pulumi-cloud

meta_desc: Pulumi Cloud is the smartest and easiest way to automate, secure, and manage your cloud.
aliases:
    - /product/pulumi-service/
    - /product/cloud/
    - /cloud/

overview:
    title: Intelligent Infrastructure Management
    description: |
        Pulumi Cloud is the smartest and easiest way to automate, secure, and manage everything you run in the cloud. It stores infrastructure state, centralizes secrets management, provides search and clear visibility into all your clouds, runs remote deployments, integrates with CI/CD pipelines, and enforces security and compliance policies.

case_studies:
    title: Customers innovating with Pulumi Cloud
    items:
        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: Starburst
          link: /blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/
          logo: starburst
          description: |
            Increased velocity and speed, with deployments that are up to 3x faster.

        - name: BMW
          link: /case-studies/bmw/
          logo: bmw
          description: |
            Enabled developers to deploy across hybrid cloud environments.

        - name: Lemonade
          link: /case-studies/lemonade/
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments

products:
    - header: Products
      content:
        - header: Pulumi IaC
          tabid: iac-select
          subheader: Productive cloud automation
          link: /product/infrastructure-as-code/
          image: /images/product/console-resource-graph.svg
          details:
            - title: Fully-managed, single source of truth
              description: |
                Pulumi Cloud is a fully managed service for [infrastructure as code](/what-is/what-is-infrastructure-as-code/). Store your infrastructure’s state for any cloud in Pulumi's secure backend, which has built-in scaling, availability, and fault tolerance. You also get access to granular access controls, CICD integrations, SAML/SCIM, audit logging, and more.

              more_info: |
                Allow developers to safely deploy in parallel with concurrent state-locking.

                Audit changes or rollback to previous versions with a [complete history](/docs/iac/concepts/state-and-backends/#checkpoints) of your state.

            - title: Manage infrastructure secrets and configuration
              description: |
                Use built-in [secrets management](/what-is/what-is-secrets-management/) for encrypted data such as credentials or tokens. Store and manage collections of config in [Pulumi ESC](/product/esc) into environment groupings.

              more_info: |
                Your infrastructure [state is encrypted](/docs/iac/concepts/state-and-backends/#state-encryption) in transit and at rest.

                Sensitive configurations (e.g. database passwords, cloud tokens) are [stored as secrets](/docs/concepts/secrets/).

                Use Pulumi's secrets manager or integrate with AWS KMS, Azure Key Vault, Google KMS, and HashiCorp Vault.
            - title: IaC as a programmatic interface
              description: |
                With [Automation API](/automation),  you can use the Pulumi engine as a strongly typed SDK in your application code, enabling it to call functions that can provision and configure infrastructure on any cloud.

              more_info: |
                Automation API enables you to build custom cloud interfaces for your technical end users. For example, build self-service developer portals, CLIs, frameworks, and CI/CD workflows.

                Easily build high-scale, SaaS applications that serve customers with single-tenant instances. Automate creating and managing infrastructure for thousands of unique customers.
            - title: Software delivery integrations
              description: |
                Integrate Pulumi with your software delivery pipeline so that you can version, build, test, and deploy infrastructure code like software.

              more_info: |
                Work with existing tools like IDEs, test frameworks, and package managers.

                Integrate your [source control system](/docs/platform/deployments/ci-cd-integration-assistant/) so teams can trace changes back to commits and pull requests.

                Continuously deliver infrastructure through existing pipelines with [CI/CD integrations](/docs/iac/packages-and-automation/continuous-delivery/).

                Use event-based [webhooks](/docs/platform/webhooks/) to notify external services like Slack or continuous integration tools.

                Use [the Service API](/blog/pulumi-rest-api/) to manage stacks, updates, teams, and more.
        - header: Pulumi ESC
          tabid: esc-select
          subheader: Automatic cloud security
          link: /product/esc/
          image: /images/product/esc-screenshot-2.png
          details:
            - title: Stop secrets sprawl
              description: |
                Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.

              more_info: |
                Access, share, and manage confidential information such as secrets, passwords, and API keys as well as configuration information such as network settings and deployment options.

                Environments support importing one into another, allowing for easy composability and inheritance of shared secrets and configuration.

                Every change to an environment as well as any of its secrets and configuration is versioned, so rolling back or accessing an old version is easy.

            - title: Trust (and prove) your secrets are secure
              description: |
                 Every environment can be locked down with role-based access controls (RBAC) and versioned with all changes fully logged for auditing.

              more_info: |
                Pulumi ESC leverages the same Pulumi Cloud identity, RBAC, Teams, SAML/SCIM, OIDC, and scoped access tokens used for Pulumi IaC to ensure secrets management complies with enterprise security policies.

                Every time secrets or configuration values are accessed or changed with Pulumi ESC, the action is fully logged for auditing. Logs include who accessed what, the action they took, and even a full record of showing which originating environments accessed values are inherited from.

            - title: Ditch .env files
              description: |
                No more storing secrets in plaintext on dev computers. Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.

              more_info: |
                Pulumi ESC also provides just-in-time, short-lived credentials, making them easy to adopt as a security best practice.

            - title: Use with or without Pulumi IaC
              description: |
                Use Pulumi ESC to centrally manage your configuration and secrets independently of Pulumi IaC, or use ESC and IaC together for the convenience of storing secrets in config with a higher degree of security than using plaintext.

              more_info: |
                Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.
        - header: Pulumi Insights
          tabid: insights-select
          subheader: Intelligent cloud management
          link: /product/pulumi-insights/
          image: /images/product/resource-search-diagram.svg
          details:
            - title: Clear visibility across all infrastructure
              description: |
                View resources deployed in all your clouds, organized in projects and stacks, so that you know what's running and where.

              more_info: |
                View dashboards for quick insights into your infrastructure, such as how many resources are running and who has made changes.

                [Tag stacks](/docs/concepts/stack/#stack-tags) for easier filtering and searching.

                Jump directly to the cloud console for each resource you've deployed with Pulumi.

            - title: Search for resources across all clouds
              description: |
                Easily look for resources in a single cloud or across all your clouds with structured queries or natural language search.

              more_info: |
                Search for resources by filtering with facets like type, provider, project, and stack.

                Use a structured query syntax or natural language search (coming soon).

                Share queries with your teammates.
    - header: Cross-Product Capabilities
      content:
        - header: Pulumi Policies
          tabid: policies-select
          subheader: Policy as code
          link: /docs/insights/policy/
          image: /images/product/console-policy-group.svg
          details:
            - title: Proactive compliance enforcement
              description: |
                Set guardrails for developers deploying with Pulumi by creating [policy packs](/docs/insights/policy/policy-packs/) that enforce your [deployment rules](/docs/insights/policy/).

              more_info: |
                Define [Policy as Code](/docs/insights/policy/) rules for security, best practices, and more.

                Assign [policy packs](/docs/insights/policy/policy-packs/) that run on specific stacks (e.g., dev/test/staging rules).

                Automatically block deployments that violate your organization's policies.
            - title:  Enterprise compliance enforcement
              description: |
                Business Critical customers can enforce [compliance](/docs/insights/policy/policy-packs/) and remediate non-compliance using Pulumi provided policies across your organization.

              more_info: |
                Choose from hundreds of policies for AWS, Azure, Google Cloud, and Kubernetes. Support for PCI DSS, ISO 27001, SOC 2, and CIS Benchmarks.

                Set policy packs that block prohibited deployments across your entire organization, preventing issues.

            - title:  Continuous and automatic compliance
              description: |
                Policies can remediate violations to fix the problems found in addition to reporting them as violations.

              more_info: |
                Here are a few examples of the remediation policy use cases:

                - Tagging resources with standard, organization-wide tags.
                - Disabling Internet access for gateways and firewall rules.
                - Enabling encryption on storage or buckets.
                - Down-sizing virtual machine configuration to use less expensive machine types.
        - header: Pulumi Deployments
          tabid: deployments-select
          subheader: Infrastructure lifecycle management
          link: /product/pulumi-deployments/
          image: /images/product/pulumi-deployments.png
          details:
            - title: Run cloud infrastructure operations remotely
              description: |
                [Run remote infrastructure commands](/docs/platform/deployments/) to provision, configure, and destroy cloud resources, all executed in a secure cloud environment.

              more_info: |
                Trigger deployments via REST API, click to deploy from Pulumi Cloud's console, Git Push to Deploy, Remote Automation API, and other programmatic building blocks.

                Use a simple, centralized format for specifying everything needed to deploy your infrastructure stacks.

            - title: Manage infrastructure operations at high scale with Deployments-as-a-Service
              description: |
                Use the [Pulumi Deployments REST API](/docs/platform/deployments/api/) to programmatically trigger deployments for high volume infrastructure automation use cases.

              more_info: |
                Call Pulumi's [REST API endpoint](/docs/platform/deployments/api/) to trigger Pulumi commands that run in Pulumi Cloud (e.g., update, destroy, refresh, preview).

                Offload your local Automation API deployment workloads to Pulumi Cloud via the [Remote Automation API feature](/docs/platform/deployments/#deployment-triggers).
        - header: Pulumi Neo
          tabid: copilot-select
          subheader: AI-powered infrastructure management
          link: /product/neo/
          image: /images/product/neo-prompt.png
          details:
            - title: Generate infrastructure as code
              description: |
                Generate a Pulumi program and deploy cloud infrastructure in seconds with a few simple text prompts.

              more_info: |
                **Example Pulumi Neo prompts:**

                *“Create a new serverless application on AWS”*

                *“Configure a Kubernetes cluster with best practices on Azure”*

                *“Deploy a Cloudflare worker that uses sticky load balancing to distribute traffic to my Google Cloud backend”*

            - title: Understand your team's cloud usage
              description: |
                Pulumi Neo has access to all of your Pulumi projects and stacks, and can relate those to your live cloud environments.

              more_info: |
                **Example Pulumi Neo prompts:**

                *“What versions of Kubernetes do I currently have deployed?”*

                *“What AWS account does VPC vpc-04a11 live within?”*

                *“What environments do we have related to Azure?”*

                *“Describe the architecture of my www-frontend project.”*

            - title: Discover cost savings opportunities
              description: |
                Pulumi Neo uses a combination of Pulumi and cloud understanding to discover and reclaim cloud waste.

              more_info: |
                **Example Pulumi Neo prompts:**

                *“What are my least used, most expensive resources?”*

                *“What are my top 10 most expensive cloud resources?”*

                *“How much did my cloud costs increase month over month – and what team was responsible for driving them upwards?”*

            - title: Stay secure
              description: |
                Pulumi Neo leverages knowledge about security best practices by combining Pulumi’s supergraph and cloud skills.

              more_info: |
                **Example Pulumi Neo prompts:**

                *“Do I have any insecure endpoints open to the Internet?”*

                *“Do any of my S3 buckets have public-read access? If yes, help me make them private.”*

                *“Do you see any anomalous activity within the past 48 hours?”*

            - title: Debug cloud failures
              description: |
                Pulumi Neo can access history, logs, and runtime metrics so you can easily get answers about what is failing and why.

              more_info: |
                **Example Pulumi Neo prompts:**

                *“Why did my deployment yesterday fail?”*

                *“We had an outage Thursday evening around 11pm. Do you understand why?”*

                *“I can’t access my EC2 instance i-3f8e over the Internet, why?”*
        - header: Team Management
          tabid: management-select
          image: /images/product/pulumi-cloud-access.png
          details:
            - title: Set up identity and access controls
              description: |
                Integrate SSO and your [identity provider](/docs/administration/access-identity/scim/) with Pulumi, set [user permissions](/docs/administration/organizations-teams/teams/) for each stack, and track user activity with [audit logs](/docs/pulumi-cloud/audit-logs/).

              more_info: |
                Single sign-on with any [SAML 2.0](/docs/administration/access-identity/saml/) identity provider like Azure Active Directory, Google Workspace , Okta, and OneLogin.

                Manage Pulumi access from your central identity provider via [SCIM 2.0 integration](/docs/administration/access-identity/scim/).

                Set [role-based access controls](/docs/administration/organizations-teams/teams/) that limit who can access infrastructure.

                Track the activity of users within your organization with [audit logs](/docs/pulumi-cloud/audit-logs/).
            - title: Collaborate better within teams
              description: |
                Add teammates to Pulumi so you can work on projects together, ship code collaboratively, and coordinate changes to infrastructure.

              more_info: |
                Invite new team members and share projects to collaborate on infrastructure.

                View [timelines](/docs/platform/projects-and-stacks/#stack-activity) that show diffs of changed resources and who made the changes.

                [Tag stacks](/docs/concepts/stack/#stack-tags) for easier filtering and searching.

open_source:
    title: The easiest way to use Pulumi open source
    image: /images/product/service-open-source-diagram.svg
    description: |
        Pulumi Cloud is a managed service for Pulumi IaC's open source CLI and SDK. It tracks your [infrastructure’s state](/docs/iac/concepts/state-and-backends/) and coordinates updates with the CLI, which creates or updates resources to reach your infrastructure’s [desired state](/docs/concepts/how-pulumi-works/).

        You can also use any cloud or on-premises storage to build and [run your own backend](/docs/iac/concepts/state-and-backends/#using-a-diy-backend).

security:
    title: Pulumi takes security seriously
    image: /images/product/soc-aicpa.svg
    description: |
        Pulumi Cloud runs in an AWS VPC and our architecture follows industry best practices. All network communication is encrypted using TLS and Pulumi’s endpoints are only accessible via HTTPS. Your data is also encrypted at-rest and Pulumi is compliant with SOC 2 Type II.

deployment:
    title: Deployment options
    items:
        - title: SaaS
          icon: rocketship
          icon_color: purple
          description: |
            Use Pulumi Cloud without worrying about scaling, availability, fault tolerance, and concurrency.

        - title: Self-hosted
          icon: program
          icon_color: yellow
          description: |
            [Run Pulumi Cloud](/product/self-hosted/) in your on-premises or cloud environment and manage it yourself.

pricing:
    title: Pricing
    description: |
        Pulumi Cloud offers Editions for Individual, Team, Enterprise, and Business Critical. Support is available on Enterprise and Business Critical. You only pay for what you use, and there are free tiers available.

get_started:
    title: Get started today
    description: |
        Pulumi is open source and free to get started. Deploy your first stack today.
---
