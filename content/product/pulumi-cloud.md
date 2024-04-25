---
title: Pulumi Cloud
layout: pulumi-cloud

meta_desc: Pulumi Cloud is the easiest way to use Pulumi open source at scale.
aliases:
    - /product/pulumi-service/

overview:
    titleTop: Fully-managed
    titleBottom: Infrastructure as Code platform
    description: |
        Pulumi Cloud is the easiest way to use Pulumi open source at scale. It stores infrastructure state and secrets, provides search and clear visibility into all your clouds, runs remote deployments, integrates with CI/CD pipelines, and enforces policies.

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

        - name: Panther Labs
          link: /case-studies/panther-labs/
          logo: panther-labs
          description: |
            Increased velocity and speed, with deployments that are up to 10x faster.

        - name: Mercedes-Benz
          link: /case-studies/mercedes-benz/
          logo: mercedes-benz
          description: |
            Enabled developers to deploy Kubernetes clusters quickly and easily.

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

capabilities:
    title: Key capabilities
    items:
        - title: Manage infrastructure state, secrets, and configuration
          image: /images/product/console-resource-graph.svg
          details:
            - title: Fully-managed, single source of truth
              description: |
                Store your infrastructure’s state for any cloud in Pulumi's secure backend, which has built-in scaling, availability, and fault tolerance.

              more_info: |
                Allow developers to safely deploy in parallel with concurrent state-locking.

                Audit changes or rollback to previous versions with a [complete history](/docs/concepts/state/#checkpoints) of your state.

            - title: Manage infrastructure secrets and configuration
              description: |
                Use built-in secrets management for encrypted data such as credentials or tokens. Store and manage collections of config in [Pulumi ESC](/product/esc) into environment groupings.

              more_info: |
                Your infrastructure [state is encrypted](/docs/concepts/state/#state-encryption) in transit and at rest.

                Sensitive configurations (e.g. database passwords, cloud tokens) are [stored as secrets](/docs/concepts/secrets/).

                Use Pulumi's secrets manager or integrate with AWS KMS, Azure Key Vault, Google KMS, and HashiCorp Vault.

        - title: Increase productivity and collaboration
          image: /images/product/console-stack-timeline.svg
          details:
            - title: Collaborate better within teams
              description: |
                Add teammates to Pulumi so you can work on projects together, ship code collaboratively, and coordinate changes to infrastructure.

              more_info: |
                Invite new team members and share projects to collaborate on infrastructure.

                View [timelines](/docs/pulumi-cloud/projects-and-stacks/#stack-activity) that show diffs of changed resources and who made the changes.

                [Tag stacks](/docs/concepts/stack/#stack-tags) for easier filtering and searching.

            - title: Software delivery integrations
              description: |
                Integrate Pulumi with your software delivery pipeline so that you can version, build, test, and deploy infrastructure code like software.

              more_info: |
                Work with existing tools like IDEs, test frameworks, and package managers.

                Integrate your [source control system](/docs/pulumi-cloud/deployments/ci-cd-integration-assistant/) so teams can trace changes back to commits and pull requests.

                Continuously deliver infrastructure through existing pipelines with [CI/CD integrations](/docs/using-pulumi/continuous-delivery/).

                Use event-based [webhooks](/docs/pulumi-cloud/webhooks/) to notify external services like Slack or continuous integration tools.

                Use [the Service API](/blog/pulumi-rest-api/) to manage stacks, updates, teams, and more.

        - title: Build infrastructure automation that scales
          image: /images/product/pulumi-deployments.png
          details:
            - title: Run cloud infrastructure operations remotely
              description: |
                [Run remote infrastructure commands](/docs/pulumi-cloud/deployments/) to provision, configure, and destroy cloud resources, all executed in a secure cloud environment.

              more_info: |
                Trigger deployments via REST API, click to deploy from Pulumi Cloud's console, Git Push to Deploy, Remote Automation API, and other programmatic building blocks.

                Use a simple, centralized format for specifying everything needed to deploy your infrastructure stacks.

            - title: Manage infrastructure operations at high scale with Deployments-as-a-Service
              description: |
                Use the [Pulumi Deployments REST API](/docs/pulumi-cloud/deployments/api/) to programmatically trigger deployments for high volume infrastructure automation use cases.

              more_info: |
                Call Pulumi's [REST API endpoint](/docs/pulumi-cloud/deployments/api/) to trigger Pulumi commands that run in Pulumi Cloud (e.g., update, destroy, refresh, preview).

                Offload your local Automation API deployment workloads to Pulumi Cloud via the [Remote Automation API feature](/docs/pulumi-cloud/deployments/#deployment-triggers).

        - title: View and search all infrastructure from one place
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

        - title: Set guardrails and access controls
          image: /images/product/console-policy-group.svg
          details:
            - title: Set up identity and access controls
              description: |
                Integrate SSO and your [identity provider](/docs/pulumi-cloud/access-management/scim/) with Pulumi, set [user permissions](/docs/pulumi-cloud/access-management/teams/) for each stack, and track user activity with [audit logs](/docs/pulumi-cloud/audit-logs/).

              more_info: |
                Single sign-on with any [SAML 2.0](/docs/pulumi-cloud/access-management/saml/) identity provider like Azure Active Directory, Google Workspace , Okta, and OneLogin.

                Manage Pulumi access from your central identity provider via [SCIM 2.0 integration](/docs/pulumi-cloud/access-management/scim/).

                Set [role-based access controls](/docs/pulumi-cloud/access-management/teams/) that limit who can access infrastructure.

                Track the activity of users within your organization with [audit logs](/docs/pulumi-cloud/audit-logs/).


            - title: Proactive compliance enforcement
              description: |
                Set guardrails for developers deploying with Pulumi by creating [policy packs](/docs/using-pulumi/crossguard/configuration/) that enforce your [deployment rules](/docs/using-pulumi/crossguard/).

              more_info: |
                Define [Policy as Code](/docs/using-pulumi/crossguard/) rules for security, best practices, and more.

                Assign [policy packs](/docs/using-pulumi/crossguard/configuration/) that run on specific stacks (e.g., dev/test/staging rules).

                Automatically block deployments that violate your organization's policies.

open_source:
    title: The easiest way to use Pulumi open source
    image: /images/product/service-open-source-diagram.svg
    description: |
        Pulumi Cloud is a managed service for Pulumi's open source CLI and SDK. It tracks your [infrastructure’s state](/docs/concepts/state/) and coordinates updates with the CLI, which creates or updates resources to reach your infrastructure’s [desired state](/docs/concepts/how-pulumi-works/).

        You can also use any cloud or on-premises storage to build and [run your own backend](/docs/concepts/state/#logging-into-a-self-managed-backend).

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
