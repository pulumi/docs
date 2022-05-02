---
title: Pulumi Service
layout: pulumi-service

meta_desc: The Pulumi Service enables infrastructure and development teams to focus on building, deploying, and managing modern cloud applications faster and reliably.

overview:
    titleTop: Fully-managed
    titleBottom: cloud engineering platform
    description: |
        The Pulumi Service is the easiest way to use Pulumi open source at scale, enabling infrastructure and development teams to focus on building, deploying, and managing modern cloud applications faster and reliably. It is a managed service that handles infrastructure state and secrets, sets up SAML SSO, integrates with CI/CD pipelines, and enforces compliance rules.

case_studies:
    title: Customers innovating with Pulumi Service
    items:
        - name: Atlassian
          link: /case-studies/atlassian
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: GreenPark Sports
          link: /case-studies/greenpark-sports
          logo: greenpark-sports
          description: |
            All developers contribute infrastructure code and deploy 70% more changes.

        - name: Panther Labs
          link: /case-studies/panther-labs
          logo: panther-labs
          description: |
            Increased velocity and speed, with deployments that are up to 10x faster.

        - name: Mercedes-Benz
          link: /case-studies/mercedes-benz
          logo: mercedes-benz
          description: |
            Enabled developers to deploy Kubernetes clusters quickly and easily.

        - name: Lemonade
          link: /case-studies/lemonade
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.

        - name: Snowflake
          link: /case-studies/snowflake
          logo: snowflake
          description: |
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments

capabilities:
    title: Key capabilities
    items:
        - title: Manage infrastructure state and secrets
          image: /images/product/console-resource-graph.svg
          details:
            - title: Fully-managed, single source of truth
              description: |
                Store your infrastructure’s state for any cloud in Pulumi's secure backend, which has built-in scaling, availability, and fault tolerance.

              more_info: |
                Allow developers to safely deploy in parallel with concurrent state-locking.

                Audit changes or rollback to previous versions with a [complete history](/docs/intro/concepts/state/#checkpoints) of your state.

            - title: Automatic secrets management
              description: |
                Use built-in secrets management for encrypted data such as credentials or tokens. You can also bring your own secrets manager.

              more_info: |
                Your infrastructure [state is encrypted](/docs/intro/concepts/state/#state-encryption) in transit and at rest.

                Sensitive configurations (e.g. database passwords, cloud tokens) are [stored as secrets](/docs/intro/concepts/secrets/).

                Use Pulumi's secrets manager or integrate with AWS KMS, Azure Key Vault, Google KMS, and HashiCorp Vault.

        - title: Increase developer productivity and collaboration
          image: /images/product/console-stack-timeline.svg
          details:
            - title: Team-wide visibility and collaboration
              description: |
                Visualize projects, stacks, and cloud resources so you and developers in your organization know what’s running and where.

              more_info: |
                View [timelines](/docs/intro/pulumi-service/projects-and-stacks/#stack-activity) that show diffs of changed resources and who made the changes.

                [Tag stacks](/docs/intro/concepts/stack/#stack-tags) for easier filtering and searching.

                Track the activity of users within your organization with [audit logs](/docs/intro/pulumi-service/audit-logs/).

            - title: Software delivery integrations
              description: |
                Integrate Pulumi with your software delivery pipeline so that you can version, build, test, and deploy infrastructure code like software.

              more_info: |
                Work with existing tools like IDEs, test frameworks, and package managers.

                Integrate your [source control system](/docs/intro/pulumi-service/ci-cd-integration-assistant/) so teams can trace changes back to commits and pull requests.

                Continuously deliver infrastructure through existing pipelines with [CI/CD integrations](/docs/guides/continuous-delivery/).

                Use event-based [webhooks](/docs/intro/pulumi-service/webhooks/) to notify external services like Slack or continuous integration tools.

                Use [the Service API](/blog/pulumi-rest-api/) to manage stacks, updates, teams, and more.

        - title: Set guardrails and access controls
          image: /images/product/console-policy-group.svg
          details:
            - title: Collaboration with secure access controls
              description: |
                Use identity and access controls to manage who can make changes to your infrastructure.

              more_info: |
                Invite new team members and share projects to collaborate on infrastructure.

                Single sign-on with any [SAML 2.0](/docs/guides/saml/) identity provider like Azure Active Directory, Google Workspace , Okta, and OneLogin.

                Manage Pulumi access from your central identity provider via [SCIM 2.0 integration](/docs/guides/scim/).

                Set [role-based access controls](/docs/intro/pulumi-service/teams/) that limit who can access infrastructure.

            - title: Proactive compliance enforcement
              description: |
                Set guardrails for developers in your organization and enforce configuration and deployment rules.

              more_info: |
                Define [Policy as Code](/docs/guides/crossguard/) rules for security, best practices, and more.

                Assign [policy packs](/docs/guides/crossguard/configuration/) that run on specific stacks (e.g., dev/test/staging rules).

                Automatically block deployments that violate your organization's policies.

open_source:
    title: The easiest way to use Pulumi open source
    image: /images/product/service-open-source-diagram.svg
    description: |
        Pulumi Service is a managed service for the open source CLI and SDK. It tracks your [infrastructure’s state](/docs/intro/concepts/state/) and coordinates updates with the CLI, which creates or updates resources to reach your infrastructure’s [desired state](/docs/intro/concepts/how-pulumi-works/).

        You can also use any cloud or on-premises storage to build and [run your own backend](/docs/intro/concepts/state/#logging-into-a-self-managed-backend).

security:
    title: Pulumi takes security seriously
    image: /images/product/soc-aicpa.svg
    description: |
        Pulumi Service runs in an AWS VPC and our architecture follows industry best practices. All network communication is encrypted using TLS and Pulumi’s endpoints are only accessible via HTTPS. Your data is also encrypted at-rest and Pulumi is compliant with SOC 2 Type II.

deployment:
    title: Deployment options
    items:
        - title: Managed
          icon: rocketship
          icon_color: purple
          description: |
            Use the Pulumi Service without worrying about scaling, availability, fault tolerance, and concurrency.

        - title: Self-hosted
          icon: program
          icon_color: yellow
          description: |
            [Run the Pulumi Service](/product/self-hosted) in your on-premises or cloud environment and manage it yourself.

pricing:
    title: Pricing
    description: |
        The Pulumi Service offers Editions for Individual, Team, Enterprise, and Business Critical. Support is available on Enterprise and Business Critical. You only pay for what you use, and there are free tiers available.

get_started:
    title: Get started today
    description: |
        Pulumi is open source and free to get started. Deploy your first stack today.
---
