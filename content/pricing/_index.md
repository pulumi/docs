---
title: Pricing
meta_desc: Pulumi's open source infrastructure as code SDK and enterprise SaaS is available in various editions with a starting cost of free.
type: page
layout: pricing
menu:
    header:
        weight: 2
aliases:
    - /blog/tf-migration-offer

tiers:
    free:
        title: Free
        subtitle: The basics for individuals and organizations with cloud projects.
        iac_price: $0
        iac_unit:
        iac_note:
        esc_price: $0
        esc_unit:
        esc_note:
        primary_cta: Create a free organization
        primary_cta_link: /docs/quickstart
        items: |
            - 200 free IaC resources
            - Unlimited projects/stacks
            - 25 free secrets
            - 3,000 free deployments minutes
            - Community support
    trialed:
        items:
            - title: Team
              subtitle: Collaboration for growing teams and cloud projects.
              iac_price: $0.36
              iac_unit: per resource/month
              iac_note:
              esc_price: $0.5
              esc_unit: per secret/month
              esc_note:
              primary_cta: Start free trial
              primary_cta_link: https://app.pulumi.com/signup
              items: |
                Everything in **Individual**, plus:
                - Secure team collaboration
                - Up to 10 team members
                - Automatic CI/CD
                - Unlimited ESC configuration
                - Full deployment history
                - Basic support
            - title: Enterprise
              subtitle: Advanced cloud engineering capabilities for large teams in production.
              iac_price: $1.08
              iac_unit: per resource/month
              iac_note: (Volume discounts available)
              esc_price: $0.75
              esc_unit: per secret/month
              esc_note: (Volume discounts available)
              primary_cta: Start free trial
              primary_cta_link: https://app.pulumi.com/signup
              secondary_cta: Contact Sales
              secondary_cta_link: /contact/?form=sales
              items: |
                  Everything in **Team**, plus:
                  - Unlimited members & teams
                  - Role-based access control (RBAC)
                  - SAML/SSO
                  - Secrets versioning
                  - Audit logs
                  - Enterprise support available
            - title: Business Critical
              subtitle: Advanced security, compliance, and hosting for mission-critical needs.
              iac_price: Custom
              iac_unit:
              iac_note:
              esc_price: Custom
              esc_unit:
              esc_note:
              primary_cta: Contact Sales
              primary_cta_link: /contact/?form=sales
              items: |
                  Everything in **Enterprise**, plus:
                  - Volume discounts and invoicing
                  - Policies and compliance
                  - Automatic group & user sync (SCIM)
                  - Audit logs export
                  - 24/7 support included
                  - Private Slack channel
                  - Professional services and training

customers:
    - stat: "**10x** increase in development velocity"
      logo: nvidia
    - stat: "**50%** faster customer onboarding"
      logo: snowflake
    - stat: "**75%** reduction in hard-coded credentials"
      logo: nubank
    - stat: "**100%** increase in developer satisfaction"
      logo: crunchyroll
    - stat: "**80%** reduction in deployment times"
      logo: unity

comparison_table:
    sections:
        #### 
        # Products
        ####
        - header: Products
          tables:

            # Pulumi IaC table
            - header: Pulumi IaC
              subheader: Fully-managed IaC Platform
              rows:
                - title: Price per resource/month
                  items:
                    - content: Free
                    - content: $0.36
                    - content: $1.08  Custom
                    - content: $1.08  Custom
                - title: Included resource/month
                  items:
                    - content: Free
                    - content: 200
                    - content: _blank
                    - content: _blank
                - title: Commitment discounts
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
                - title: Concurrent updates
                  items:
                    - content: 1
                    - content: 5
                    - content: Unlimited
                    - content: Unlimited
                - title: Developer portal
                  items:
                    - content: Host public templates
                    - content: Host public templates
                    - content: Host private templates
                    - content: Host private templates
                - title: Resource Search
                  link: /docs/pulumi-cloud/insights/search/
                  items:
                    - content: |
                        2K results/query  
                        No property search
                    - content: |
                        2K results/query  
                        No property search
                    - content: |
                        10K results in UI,  
                        unlimited in API,  
                        Property search included
                    - content: |
                        10K results in UI,  
                        unlimited in API,  
                        Property search included
                - title: Data Export
                  link: /docs/pulumi-cloud/insights/export/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
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
                  link: /docs/using-pulumi/continuous-delivery/
                  items:
                    - content: Many
                      tooltip: AWS Code Services, Azure DevOps, Codeship, CircleCI, GitHub, GitLab, Google Cloud Build, Jenkins, Travis, and more
                    - content: Many
                      tooltip: AWS Code Services, Azure DevOps, Codeship, CircleCI, GitHub, GitLab, Google Cloud Build, Jenkins, Travis, and more
                    - content: Customized for you
                    - content: Customized for you
                - title: CI/CD Assistant
                  link: /docs/pulumi-cloud/deployments/ci-cd-integration-assistant/
                  items:
                    - content: _blank
                    - content: _check
                    - content: _check
                    - content: _check
                - title: GitHub Enterprise Server support
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check
            
            ## Pulumi ESC table
            - header: Pulumi ESC
              rows:
                - title: Pricer per secret/month
                  items:
                    - content: Free
                    - content: $0.50
                    - content: $0.75/Custom
                    - content: Custom
                - title: Price per config
                  items:
                    - content: Free
                    - content: Free
                    - content: Free
                    - content: Free
                - title: Price per 10k API calls
                  items:
                    - content: Free
                    - content: $0.10
                    - content: $0.10
                    - content: $0.10
                - title: Included secrets/month
                  items:
                    - content: 25
                    - content: 25
                    - content: 25
                    - content: 25
                - title: Included API calls/month
                  items:
                    - content: 10
                    - content: 10
                    - content: 10
                    - content: 10
                - title: Commitment discounts
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
                - title: "# of secrets"
                  items:
                    - content: 25
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                - title: "# of projects"
                  items:
                    - content: 10
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                - title: "# of environments"
                  items:
                    - content: 10
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                - title: API call limits
                  items:
                    - content: 10k / month
                    - content: Unlimited
                    - content: Unlimited
                    - content: Unlimited
                - title: Version history
                  items:
                    - content: _blank
                    - content: Up to 5
                    - content: _check
                    - content: _check
                - title: Version tags and import by tags
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Integrations - Dynamic credentials
                  items:
                    - content: _blank
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Integrations - Dynamic secrets
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Integrations - Sync
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Multi-language SDKs
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check

        #### 
        # Key Capabilities
        ####
        - header: Key Capabilities
          tables:
            ## Pulumi Deployments table
            - header: Pulumi Deployments
              rows:
                - title: Minutes included
                  items:
                    - content: 500/month
                    - content: 3,000/month
                    - content: 3,000/month
                    - content: 3,000/month
                - title: Cost per minute
                  items:
                    - content: _blank
                    - content: $0.01
                    - content: Starts at $0.01
                    - content: Starts at $0.01
                - title: Drift detection
                  link: /docs/pulumi-cloud/deployments/drift/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Time-to-live stacks
                  link: /docs/pulumi-cloud/deployments/ttl/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Scheduled deployments
                  link: /docs/pulumi-cloud/deployments/schedules/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Concurrency limit
                  items:
                    - content: 1
                    - content: 5
                    - content: 25
                    - content: 150
                - title: Self-hosted deployment runners
                  items:
                    - content: Available
                    - content: Available
                    - content: Available
                    - content: Available

            ## CrossGuard table
            - header: Pulumi CrossGuard
              rows:
                - title: Gated deployments
                  items:
                    - content: Local enforcement
                    - content: Local enforcement
                    - content: Local enforcement
                    - content: Server-side enforcement
                - title: Organization policies
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: _check
                - title: Compliance-ready policies
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: _check
                - title: Remediation policies
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: _check
                - title: Dashboard for policy violations
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: _check


        #### 
        # Pulumi Cloud Fundamentals
        ####
        - header: Pulumi Cloud Fundamentals
          tables:
            ## Core table
            - header: Core
              subheader: Fully-managed IaC Platform
              rows:
                - title: Pulumi Co-pilot
                  items:
                    - content: _blank
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Webhooks
                  link:
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
                  link: /docs/pulumi-cloud/organizations
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Multiple supported
                    - content: Multiple supported

            ## Security table
            - header: Security
              subheader: Fully-managed IaC Platform
              rows:
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
                      tooltip: Azure Active Directory, Google Workspace, Okta, OneLogin, and more
                    - content: Many
                      tooltip: Azure Active Directory, Google Workspace, Okta, OneLogin, and more
                - title: SCIM integration
                  link: /docs/pulumi-cloud/access-management/scim/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _blank
                    - content: _check
                - title: Create and manage teams
                  link: /docs/pulumi-cloud/access-management/teams/
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check
                - title: Role-based access control (RBAC)
                  link: /docs/pulumi-cloud/organizations#organization-roles
                  items:
                    - content: _blank
                    - content: _blank
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
                - title: Organization and Team Access Tokens
                  link: /docs/pulumi-cloud/access-management/organization-access-tokens/
                  tooltip: These are machine access tokens that are scoped to the organization or team level
                  items:
                    - content: _blank
                    - content: _blank
                    - content: _check
                    - content: _check

            ## Support table
            - header: Support
              subheader: Secrets management
              rows:
                - title: Community Slack
                  link: https://slack.pulumi.com/
                  items:
                    - content: _check
                    - content: _check
                    - content: _check
                    - content: _check
                - title: Support
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: Available
                - title: Ticketing & email support
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: Available
                - title: Private Slack channel
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Available
                    - content: Available
                - title: Normal ticket service level objective
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Variable
                    - content: Variable
                - title: Urgent ticket service level objective
                  items:
                    - content: _blank
                    - content: _blank
                    - content: Variable
                    - content: Variable
                - title: Advisor access
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
                - title: Professional services
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
    pricing:
        - question: How are resources billed?
          answer: |
            Resources are billed hourly as Pulumi Credits. 1 Pulumi Credit is the price for managing one resource for one hour. The Price per credit for Team and Enterprise is $0.0005 and $0.0015 respectively,

            For billing purposes, partial resource hour used is billed as a full hour and we count any resource that's declared in a Pulumi program. This includes provider resources (e.g., an Amazon S3 bucket), component resources which are groupings of resources (e.g., an Amazon EKS cluster), and stacks which contain resources (e.g., dev, test, prod stacks).

            You consume one Pulumi Credit to manage each resource for an hour. For example, one stack containing one S3 bucket and one EC2 instance is three resources that are counted in your bill.
        - question: How are secrets billed?
          answer: |
            Secrets are billed hourly. The price per secret of $0.5 and $0.75 for Team and Enterprise is for 730 hours (~ 1 month). If you have your secrets stored for 4 days on Pulumi Cloud Team Edition, the price you pay would be 4 x 24 x 0.5 / 730 = $.0657

            Secrets include both static secrets and dynamic secrets/credentials. When using the Pulumi ESC Document Editor, each definition of fn::secret:* and fn::open::* (except Pulumi-stacks provider) is counted as a secret. The number of secrets only from the latest environment revision is counted towards your billing.
        - question: How are secrets API call metered?
          answer: |
            You pay $0 for the first free 10K API calls / month to the [ReadOpen API](/docs/pulumi-cloud/cloud-rest-api/#read-open-environment) endpoint. Once you hit 10,000 API calls, you are metered at $0.1 for 10K API calls. If you use 5K API calls you will billed $0.05. 

            Usage of API usage include any calls from the [CLI](/docs/esc-cli/), [SDK](/docs/esc/sdk/), [Pulumi-service provider](/registry/packages/pulumiservice/api-docs/environment/), direct [REST API](/docs/pulumi-cloud/cloud-rest-api/) call that hits the ReadOpen API endpoint
        - question: What can I do with 200 free resources per month? 
          answer: |
            You could manage 200 S3 buckets or 200 EC2 instances for a month using this amount. Note that free resources translate to 150K monthly Pulumi credits. 

            As another example, you could manage something more complex like a production Amazon EKS cluster with associated IAM roles, VPC, subnets, gateway route tables, and a small microservice deployed into the cluster.
        - question: How do I find out how many resources I have?
          answer: |
            There are several ways you can estimate the number of resources you have managed with Pulumi.

            - If using Pulumi Cloud: Navigate to the dashboard and review the resource graph titled “Resource Count over Time.”

            - If using Pulumi with a self-managed backend: Export your stack state and count the number of lines with a universal resource name (URN). You can pipe the state through a grep command for "urn" to estimate the number of resources.

            If you haven't deployed anything with Pulumi: See the previous FAQ for a few examples of applications and their number of resources.
        - queston: What are some examples of how many resources are needed for my use case?
          answer: |
            Serverless API with Amazon API Gateway and AWS Lambda
            Estimated resources: 9
            This scenario is a stack with an Amazon API Gateway, an AWS Lambda event handler, and associated IAM roles. 

            Amazon EKS running in a VPC
            Estimated resources: 20
            This scenario is a stack with an Amazon VPC (including subnets, internet gateway, security groups, and route table), Amazon EKS cluster and node group, and associated IAM roles. 

            Amazon ECS cluster and RDS backend running in a VPC
            Estimated resources: 24
            This scenario is a stack with an Amazon VPC (including subnets, security groups, and route table associations), Amazon ECS (including cluster and service, load balancer resources, and IAM resources), and Amazon RDS (including RDS instance and subnet group). Each group of resources (VPC, ECS, RDS) is represented by a component resource.
        - question: Can I prepay for resources, secrets, and secrets API calls?
          answer: Yes, you can! Please contact us to discuss the Enterprise and Business Critical Editions, which include bulk discounts for buying in advance.
    
    product:
---
