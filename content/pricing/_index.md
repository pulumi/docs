---
title: Pricing
meta_desc: Pulumi IaC and Pulumi ESC is available in various editions and is free to individuals
type: page
layout: pricing
menu:
    header:
        weight: 2
aliases:
    - /blog/tf-migration-offer

tiers:
    trialed:
        items:
            - title: Individual
              subtitle: Free forever for individuals.
              price: Free
              price_label:
              unit:
              note: No credit card required
              items: |
                You get:
                - IaC state management
                - Unlimited projects, stacks, and environments
                - Unlimited updates and history
                - 500 free deployments minutes
            - title: Team
              subtitle: Everything you need to get started.
              price: $40
              price_label: /mo
              unit: "**500** resources included"
              note: Additional resources **$0.1825**/mo
              items: |
                Everything in **Individual**, plus:
                - Up to 10 users
                - Secure collaboration and CI/CD
                - AI assistance with Pulumi Neo
                - Resource search
                - OIDC and Org Access Tokens
                - Webhooks
                - Automatic secrets rotation
                - Community support
            - title: Enterprise
              subtitle: Security and collaboration for large teams.
              price: $400
              price_label: /mo
              unit: "**2,000** resources included"
              note: Additional resources start at **$0.365**/mo
              items: |
                  Everything in **Team**, plus:
                  - Unlimited users
                  - SAML/SSO and RBAC
                  - Internal developer platform (IDP)
                  - Audit logs
                  - Drift detection and remediation
                  - Time-to-live stacks
                  - Priority feature requests
                  - 12x5 Enterprise Support available
            - title: Business Critical
              subtitle: Advanced governance, policies, and controls.
              price: Custom
              price_label:
              unit:
              note: Volume discounts and invoicing
              items: |
                  Everything in **Enterprise**, plus:
                  - [Self-hosting available](/product/self-hosted)
                  - Compliance policies
                  - Org-wide policy enforcement
                  - Automatic group & user sync (SCIM)
                  - Audit logs export
                  - Volume pricing and invoicing
                  - Private Slack and Professional Services
                  - 24x7 Enterprise Support available

customers:
    - stat: "**5x faster** time to market"
      logo: unity
      link: /case-studies/unity
    - stat: "**100 days saved** each year with Pulumi Cloud instead of DIY state management"
      logo: starburst
      link: /case-studies/starburst
    - stat: "**10x faster deployments**, from weeks to hours"
      logo: snowflake
      link: /case-studies/snowflake

comparison_table:
    sections:
        ####
        # Products
        ####
        - header: Product
          tables:
            # Pulumi IaC table
            - header: Infrastructure as Code
              subheader: Foundational capability is included in all editions
              rows:
                - title: On-demand resource price
                  items:
                    - content: Free
                    - content: $0.00025/hour<br>($0.185/month)
                    - content: Starting at $0.0005/hour<br>($0.365/month)
                    - content: Custom
                - title: Commitment pricing
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Self-hosting
                  link: /product/self-hosted/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check
                - title: Updates
                  items:
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                - title: Concurrent stack updates
                  items:
                    - content: 1
                    - content: 5
                    - content: Unlimited
                    - content: Unlimited
                - title: Restore Deleted Stacks
                  link: /blog/restore-stacks
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Update history
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: CI/CD integrations
                  link: /docs/iac/packages-and-automation/continuous-delivery/
                  items:
                    - content: Many
                      tooltip: AWS Code Services, Azure DevOps, Codeship, CircleCI, GitHub, GitLab, Google Cloud Build, Jenkins, Travis, and more
                    - content: Many
                      tooltip: AWS Code Services, Azure DevOps, Codeship, CircleCI, GitHub, GitLab, Google Cloud Build, Jenkins, Travis, and more
                    - content: Customized for you
                    - content: Customized for you
                - title: CI/CD Assistant
                  link: /docs/platform/deployments/ci-cd-integration-assistant/
                  items:
                    - content: _blank
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Drift detection
                  link: /docs/platform/deployments/drift/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Time-to-live stacks
                  link: /docs/platform/deployments/ttl/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Scheduled deployments
                  link: /docs/platform/deployments/schedules/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: GitHub Enterprise Server support
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check
                - title: Webhooks
                  link: /docs/platform/webhooks/
                  items:
                    - content: _blank
                    - content: _check
                    - content: _check
                    - content: _check
                - title: REST API
                  link: /docs/pulumi-cloud/cloud-rest-api/
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Automation API
                  link: /automation/
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Pulumi-service provider
                  link: /registry/packages/pulumiservice/
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Members
                  items:
                    - content: 1
                    - content: Up to 10
                    - content: Unlimited
                    - content: Unlimited
                - title: Admins
                  items:
                    - content: _blank
                    - content: 1
                    - content: Unlimited
                    - content: Unlimited
                - title: Organizations
                  link: /docs/pulumi-cloud/admin/organizations/
                  items:
                    - content: _blank
                    - content: 1
                    - content: Multiple supported
                    - content: Multiple supported
                - title: Identity providers
                  link: /docs/pulumi-cloud/accounts
                  items:
                    - content: GitHub, GitLab, Atlassian
                    - content: GitHub, GitLab, Atlassian
                    - content: GitHub, GitLab, Atlassian, SAML/SSO
                    - content: GitHub, GitLab, Atlassian, SAML/SSO
                - title: SAML/SSO
                  link: /docs/pulumi-cloud/access-management/saml/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Many
                      tooltip: Microsoft Entra ID, Google Workspace, Okta, OneLogin, and more
                    - content: Many
                      tooltip: Microsoft Entra ID, Google Workspace, Okta, OneLogin, and more
                - title: SCIM integration
                  link: /docs/pulumi-cloud/access-management/scim/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check
                - title: OIDC Support
                  link: /docs/pulumi-cloud/oidc/
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Create and manage teams
                  link: /docs/pulumi-cloud/access-management/teams/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Role-based access control (RBAC)
                  link: /docs/pulumi-cloud/admin/organizations/#organization-roles
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Organization and Team Access Tokens
                  link: /docs/pulumi-cloud/access-management/organization-access-tokens/
                  tooltip: These are machine access tokens that are scoped to the organization or team level
                  items:
                    - content: _blank
                    - content: _check
                      tooltip: Organization Access Token only
                    - content: _check
                    - content: _check
                - title: Audit Logs
                  link: /docs/pulumi-cloud/audit-logs/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Automated log export to S3
                  link: /docs/pulumi-cloud/audit-logs#automated-export
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check

        ## Key Capabilities section
        - header: Key Capabilities
          tables:
            ## Pulumi ESC table
          - header: Secrets & Configuration
            subheader: Secure configuration management across all environments
            rows:
              - title: On-demand secret price
                items:
                  - content: 25 free
                  - content: $0.000685/hour<br>($0.50/mo)
                  - content: $0.001/hour<br>($0.75/mo)
                  - content: Custom
              - title: Price per plaintext config
                items:
                  - content: Free
                  - content: Free
                  - content: Free
                  - content: Free
              - title: Price per 10K API calls
                items:
                  - content: 10K free
                  - content: $0.10
                  - content: $0.10
                  - content: $0.10
              - title: Commitment pricing
                items:
                  - content: _blank
                  - content: _blank
                  - content: _check
                  - content: _check
              - title: Self-hosting
                link: /product/self-hosted/
                items:
                  - content: _blank
                  - content: _blank
                  - content: _blank
                  - content: Available
              - title: "Max # of secrets"
                items:
                  - content: 25
                  - content: Unlimited
                  - content: Unlimited
                  - content: Unlimited
              - title: "Max # of API calls"
                items:
                  - content: 10K / month
                  - content: Unlimited
                  - content: Unlimited
                  - content: Unlimited
              - title: Version history
                link: /docs/esc/environments/versioning/
                items:
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Version tags and import by tags
                link:  /docs/esc/environments/versioning/#tagging-versions
                items:
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Dynamic credentials
                link: /docs/esc/integrations/dynamic-login-credentials/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Dynamic secrets
                link: /docs/esc/integrations/dynamic-secrets/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Rotated secrets
                link: /docs/esc/integrations/rotated-secrets/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Database Secrets Rotation
                link: /blog/esc-db-secrets-rotation-launch/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Database Secrets Rotation in private networks
                link: /blog/esc-db-secrets-rotation-launch/
                items:
                  - content: _blank
                  - content: _blank
                  - content: _check
                  - content: _check
              - title: Integrations - Sync
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Multi-language SDKs
                link: /docs/esc/sdk/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              
          ## Pulumi Insights Table
          - header: Insights & Governance
            subheader: Visibility and governance across your entire cloud estate
            rows:
              - title: On-demand resource price
                items:
                  - content: Free
                  - content: $0.00025/hour<br>($0.185/month)
                  - content: Starting at $0.0005/hour<br>($0.365/month)
                  - content: Custom
              - title: Workflow cost per minute/ included per month
                link: /pricing#faq
                items:
                  - content: 500 free
                  - content: $0.01<br>3,000 included
                  - content: $0.01 / Custom<br>3,000 included
                  - content: $0.01 / Custom<br>3,000 included                  
              - title: Resource search
                link: /docs/insights/search/
                items:
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Primary Accounts
                items:
                  - content: 1
                  - content: 1
                  - content: 10
                  - content: 20
              - title: Data export
                link: /docs/insights/export/
                items:
                  - content: _blank
                  - content: _blank
                  - content: _check
                  - content: _check
              - title: Property search
                link: /docs/insights/search/#property-queries
                items:
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Policy Enforcement
                link: /docs/insights/policy-as-code
                items: 
                  - content: "Manual"
                  - content: "[Organization-managed](/docs/insights/policy/#pulumi-cloud-integration)"
                  - content: "[Organization-managed](/docs/insights/policy/get-started/#enforcing-a-policy-pack)"
                  - content: "[Organization-managed](/docs/insights/policy/get-started/#enforcing-a-policy-pack)"
              - title: Preventative Policies
                link: /docs/insights/preventative-vs-audit-policies/
                items: 
                  - content: Manual
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Audit Policies
                link: /docs/insights/preventative-vs-audit-policies/
                items: 
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Pre-built Policy Packs
                link: /docs/insights/pre-built-packs
                items: 
                  - content: _blank
                  - content: Pulumi Best Practices
                  - content: Pulumi Best Practices
                  - content: Pulumi Best Practices, CIS, NIST, HITRUST, PCI DSS
              - title: Custom Policy Packs
                link: /docs/insights/policy/policy-as-code/get-started/#creating-a-policy-pack
                items:
                  - content: _blank
                  - content: Up to 25 policies (1 pack limit)
                  - content: Up to 100 policies (3 pack limit)
                  - content: Unlimited
              - title: Enforcement Modes
                link: /docs/insights/policy/#local-policy-execution
                items:
                  - content: _blank
                  - content: Advisory & Mandatory
                  - content: Advisory & Mandatory
                  - content: Advisory, Mandatory & Remediation 
          ## Pulumi Neo Table
          - header: Infrastructure AI
            subheader: Intelligent assistance across all platform capabilities
            rows:
              - title: Pulumi Neo
                link: /docs/ai/neo/
                items:
                  - content: _blank
                  - content: _check
                  - content: _check
                  - content: _check
          ## Pulumi Workflow table
          - header: Internal Developer Platform
            subheader: Self-service capabilities with guardrails
            rows:
              - title: Developer portal
                items:
                  - content: Host public templates
                  - content: Host public templates
                  - content: Host private templates
                  - content: Host private templates
          - header: Support
            subheader: 
            rows:
              - title: Support
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available, 12x5 / 24x7 support
                  - content: Available, 12x5 / 24x7 support
              - title: Normal ticket SLA
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available, 1 or 5 business days
                  - content: Available, 1 or 5 business days
              - title: Urgent ticket SLA
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available, 4 hours to 2 business days
                  - content: Available, 4 hours to 2 business days
              - title: Private Slack channel
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available
                  - content: Available
              - title: Community Slack
                link: https://slack.pulumi.com/
                items:
                  - content: _check
                  - content: _check
                  - content: _check
                  - content: _check
              - title: Professional services
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available
                  - content: Available
              - title: Onboarding and training
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available
                  - content: Available
              - title: Terraform Migration
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available
                  - content: Available
              - title: SLA
                items:
                  - content: _blank
                  - content: _blank
                  - content: Available
                  - content: Available



faq:
    - category: Pricing
      id: pricing
      items:
        - question: Do I pay as I go, or prepaid up-front?
          answer: |
            Both options are available. If you self-serve by entering a credit card, you will be billed in-arrears every month for your usage. If you prefer to pay up-front, you can [contact sales](/contact?form=sales) and receive a discount for a committed amount of usage paid up-front. If you subsequently consume all up-front purchased usage, you will be billed in-arrears as you go beyond that amount of usage. The details are specified in your contract.
        - question: How are IaC resources billed?
          answer: |
            Should you exceed the 500 and 2,000 included resources in Team and Enterprise, respectively, you will be charged at the end of the month for the number of resource hours consumed in excess of what is included.

            IaC resources are billed hourly at the rate of $0.00025 for Team ($0.1825 per resource per month) and starting at $0.0005 for Enterprise ($0.365 per resource per month). This is the cost of managing an IaC resource for a full hour.

            Enterprise editions receive volume discounts, so that the more resources you consume, the lower the incremental rate. This is true of self-serve pay-as-you-go plans, although prepaid plans offer more considerable discounts.

            For billing purposes, a partial resource hour used is billed as a full hour and we count any resource that's declared in a Pulumi program. This includes [provider resources](/docs/concepts/resources) (e.g., an Amazon S3 bucket), [component resources](/docs/iac/concepts/components) which are groupings of resources (e.g., an Amazon EKS cluster), and [stacks](/docs/iac/concepts/stacks) which contain resources (e.g., dev, test, prod stacks).
        - question: What can I do with 500 IaC resources per month?
          answer: |
            The Team edition includes 500 IaC resources to get started with.

            You could manage 500 EKS clusters or EC2 instances for a month using this amount. As another example, you could manage something more complex like a production Amazon EKS cluster with associated IAM roles, VPC, subnets, gateway route tables, and a small microservice deployed into the cluster.

            This is more than enough to get started with production workloads. The Enterprise edition comes with 2,000 resources.
        - question: How do I find out how many IaC resources I have?
          answer: |
            There are several ways you can estimate the number of resources you have managed with Pulumi.

            - <u>If you are using Pulumi Cloud</u>: Navigate to the dashboard and review the resource graph titled “Resource Count over Time.”

            - <u>If using Pulumi with a DIY backend</u>: Export your stack state and count the number of lines with a universal resource name (URN). You can pipe the state through a grep command for "urn" to estimate the number of resources.

            - <u>If you haven't deployed anything with Pulumi</u>: See the previous FAQ for a few examples of applications and their number of resources.
        - question: What are some examples of how many IaC resources are needed for my use case?
          answer: |
            [**Serverless API with Amazon API Gateway and AWS Lambda**](https://github.com/pulumi/examples/tree/master/aws-ts-apigatewayv2-http-api)
            Estimated resources: <b>9</b><br>
            This scenario is a stack with an Amazon API Gateway, an AWS Lambda event handler, and associated IAM roles.

            [**Amazon EKS running in a VPC**](https://github.com/pulumi/examples/tree/master/aws-py-eks)
            Estimated resources: <b>20</b><br>
            This scenario is a stack with an Amazon VPC (including subnets, internet gateway, security groups, and route table), Amazon EKS cluster and node group, and associated IAM roles.

            [**Amazon ECS cluster and RDS backend running in a VPC**](https://github.com/pulumi/examples/tree/master/aws-py-wordpress-fargate-rds)
            Estimated resources: <b>24</b><br>
            This scenario is a stack with an Amazon VPC (including subnets, security groups, and route table associations), Amazon ECS (including cluster and service, load balancer resources, and IAM resources), and Amazon RDS (including RDS instance and subnet group). Each group of resources (VPC, ECS, RDS) is represented by a component resource.
        - question: How are ESC secrets billed?
          answer: |
            ESC secrets are billed hourly at the rate of $0.000685 for Team ($0.50 per secret per month) and $0.001 for Enterprise ($0.75 per secret per month). This is the cost of managing an ESC secret for a full hour.
            
            For example, if you have your secrets stored for 4 days on Pulumi Cloud Team Edition, the price you pay would be 4 x 24 x 0.5 / 730 = $0.0657

            Secrets include both static secrets and dynamic secrets/credentials. When using the Pulumi ESC Document Editor, each definition of fn::secret:* and fn::open::* (except Pulumi-stacks provider) is counted as a secret. The number of secrets only from the latest environment revision is counted towards your billing.
        - question: How are ESC secrets API calls metered?
          answer: |
            You pay $0 for the first free 10K API calls / month to the [ReadOpen API](/docs/pulumi-cloud/reference/environments/#read-open-environment) endpoint. Once you hit 10,000 API calls, you are metered at $0.1 for 10K API calls. If you use 5K API calls you will billed $0.05.

            API usage include any calls from the [CLI](/docs/esc/cli/), [SDK](/docs/esc/development/languages-sdks/), [Pulumi-service provider](/registry/packages/pulumiservice/api-docs/environment/), direct [REST API](/docs/pulumi-cloud/reference/environments/) call that hits the ReadOpen API endpoint
        - question: What are workflow minutes?
          answer: |
            Workflow Minutes represent the total time used across both Pulumi Insights and Deployments. All usage draws from a single, shared pool of minutes. For Insights, workflow minutes measure the time spent on discovery and policy execution. Deployments also consume workflow minutes by measuring the duration of each deployment process.
        - question: Can I prepay for resources, secrets, and secrets API calls?
          answer: Yes, you can! Please contact us to discuss the Enterprise and Business Critical Editions, which include volume pricing for paying in advance.

    - category: Product
      id: product
      items:
        - question: What are Pulumi open source and Pulumi Cloud?
          answer: |
            Pulumi's Infrastructure as Code CLI and SDK are an open-source project that is supported by an active community. Pulumi Cloud is a managed service for the open source CLI and SDK. It tracks your infrastructure’s state and coordinates updates with the CLI, which creates or updates resources to reach your infrastructure’s desired state. It also manages secrets, supports SAML SSO, integrates with CI/CD pipelines, enforces compliance rules, and much more.

            You're not required to use [Pulumi Cloud](/product/pulumi-service/). You can use any cloud or on-premises storage to build and run your own backend.
        - question: Can I use Pulumi for Free?
          answer: |
            Yes! There are three ways to use Pulumi for free.

            First, Pulumi Cloud is free to use, now and forever, for individuals. You get all of the convenience of automatic state management, unlimited updates, and many other great features without needing to pay anything at all for it.

            Second, Pulumi is an [open-source project](https://github.com/pulumi/pulumi). You can [run Pulumi entirely offline](/docs/iac/concepts/state-and-backends#using-a-diy-backend) without the online service's features, and manage state yourself, instead of using the online service. There are no restrictions — it's all there in the open for you to use freely as you'd like.

            Finally, we offer a 14-day free trial for the Business-critical Edition. Once the trial is over, you can continue to use the Business-critical Edition by chatting with sales or changing to Team or Enterprise Edition. After your trial expires, no data will be lost, and there is a grace period.
        - question: What is an organization? What are projects and stacks?
          answer: |
            The Individual Edition is great for single users with private projects. However, if you are working within a team, you'll typically want to share your projects - for which you need to create an organization. The Team Edition is designed for teams to collaborate on shared infrastructure projects. The Enterprise Edition offers more sophisticated organization management facilities, including RBAC for advanced policy controls.

            Pulumi [projects](/docs/concepts/projects/) and [stacks](/docs/concepts/stack/) are a way to organize Pulumi code. You can consider a Pulumi Project to be analogous to a GitHub repo: a single place for code -- and a Stack to be an instance of that code which has a separate configuration. For instance, Project Foo may have multiple stacks for Dev, Test, Prod, or perhaps for different cloud configurations (e.g. geographic region).
        - question: How do I get started?
          answer: Follow the [Getting Started guide](/docs/quickstart/), which walks you through creating and deploying your first Pulumi project.
        - question: How do I move from Starter or Pro to the new Team Edition?
          answer: We recommend moving from the old SKUs. [Contact us](/contact/?form=sales) to move to the new Team Edition.
        - question: Is Pulumi SOC 2 compliant?
          answer: Yes, Pulumi has completed the SOC 2 Type 2 compliance process. Pulumi is committed to operational excellence for our customers.
        - question: Can I host Pulumi Cloud in my cloud or datacenter?
          answer: Yes, we offer a self-hosted Pulumi Cloud for companies that have specific data control requirements and want to maintain complete control over hosting Pulumi Cloud. This option is available in Business Critical Edition. You can get started with a [30-day free trial here](/product/self-hosted/#self-hosted-trial).
        - question: How do I convince my boss?
          answer: |
            Do you want to use Pulumi in your organization, but aren't sure how to bring it up with your boss? We've created a sample email to help you explain its benefits. Feel free to use the full letter or pieces of it. We are always happy to meet to learn more about your needs and explain these benefits in person — just [contact us](/contact/?form=sales).

            **Sample Email**
            Dear {Name},

            I'd like to propose that we use Pulumi for our cloud infrastructure needs. I've researched the top infrastructure as code platforms, and Pulumi stands out because of its maturity, strong open source community, support for many clouds, and mix of productivity and enterprise controls, meaning it works great for developers and infrastructure teams alike.

            I discovered that Pulumi's community is over 10,000 people and growing, and their customer base includes a diverse array of companies, from startups to some of the largest Fortune 500 and Global 2000 organizations. The top four reasons people are choosing Pulumi are 1) it tames cloud complexity and reduces infrastructure risks, 2) it lets teams use software engineering best practices with infrastructure, 3) it helps teams adopt modern cloud architectures, and 4) it increases collaboration between infrastructure teams, developers, and security engineers.

            Here are some examples of their customers to give you an idea of who is using it and why:

            - Tableau and Fenergo can now release new features faster by empowering their developers to deploy cloud infrastructure easily.
            - [Snowflake migrated to](/case-studies/snowflake/) Kubernetes across multiple clouds in three months.
            - [Mercedes-Benz](/case-studies/mercedes-benz/) Research & Development North America improved collaboration between its infrastructure and application development teams.
            - [Skai](/blog/kenshoo-migrates-to-aws-with-pulumi/) managed a complex public cloud migration project.
            - Cockroach Labs, [Sourcegraph](/case-studies/sourcegraph/), and [Lemonade](/case-studies/lemonade/) created innovative engineering cultures.

            Pulumi is open source and has a SaaS product that helps organizations like ours manage infrastructure with advanced security and policies. Because it's a SaaS, we can start small and grow as our success with the product grows.

            You can learn more on the Pulumi website or view a short introduction video.

            I have many ideas on how Pulumi would deliver immediate value to our team. Should I write a more detailed proposal and share it with you or other members of the team for feedback? The Pulumi team has also offered to have a meeting with us to learn more about our use cases, and discuss potential ways we can work together. Should I set that up?

            Thanks,
            {Your Name}

    - category: Billing and Support
      id: billing
      items:
        - question: How can I keep track of my usage?
          answer: You can keep track of current usage and upcoming charges by navigating to Settings and then Billing & Usage in the Pulumi Cloud.
        - question: When will I be billed for using Team or Enterprise Edition?
          answer: You will be billed for the previous month’s usage on the first day of each month.
        - question: How can groups not seeking a profit use Pulumi for free?
          answer: The [Open-Source Free Edition](/pricing/open-source-free-tier/) allows organizations not seeking a profit with projects under an open-source license to use Pulumi for free.
        - question: What payment options do you accept?
          answer: For the Pulumi Team Edition, you can pay with a credit card (we use Stripe for processing). Pulumi Enterprise Edition offers additional payment options. Please [contact us](/contact/?form=sales) for those options.
        - question: What if I have billing or account issues?
          answer: For any billing or related issues, please [contact us](/contact/).
        - question: What if I am not satisfied with my Pulumi purchase?
          answer: If you're not satisfied with Pulumi, we offer a 14-day money-back guarantee. No questions asked. [Contact us](/contact/).
        - question: How do I get support for Pulumi?
          answer: 12 x 5, 24 x 7 support, professional and advising services, private slack channel are available to purchase in the Enterprise and Business Critical Edition of Pulumi Cloud. [Contact us](/contact/?form=sales) if you need help or have any questions.
        - question: Does Pulumi charge sales tax?
          answer: You may be charged a sales tax in addition to your usage fees in certain jurisdictions. It will be a separate line item on your bill.
---
