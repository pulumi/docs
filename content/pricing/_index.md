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
        secrets_price: $0
        secrets_unit:
        secrets_note:
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
              secrets_price: $0.5
              secrets_unit: per secret/month
              secrets_note:
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
              secrets_price: $0.75
              secrets_unit: per secret/month
              secrets_note: (Volume discounts available)
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
              secrets_price: Custom
              secrets_unit:
              secrets_note:
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
                      

---
