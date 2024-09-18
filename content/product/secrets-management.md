---
title: "Pulumi ESC: Centralized Secrets Management & Orchestration"
layout: secrets-management

meta_title: "Pulumi ESC: Centralized Secrets Management & Orchestration"
meta_desc: Centralized secrets management & orchestration. Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
meta_image: "/images/product/esc-how-it-works-diagram.png"
aliases:
    - /esc
    - /product/esc

subtitle: Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.

overview:
    header: A central hub to securely manage all of your environments, secrets, and configurations
    body: |
      - **Stop secret sprawl.** Pull and sync secrets and configuration with any secrets store – HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.  
      - **Trust (and prove) your secrets are secure.** Adopt dynamic, short-lived secrets on demand as a best practice. Lock down every environment with RBAC, versioning, and a full audit log of all changes.  
      - **Ditch `.env` files.** No more copying-and-pasting secrets or storing them in plaintext on dev computers. Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and SDKs.
      - **Use with or without Pulumi IaC.** Use Pulumi ESC independently, or use with Pulumi IaC to support storing secrets in config in a more secure way than using plaintext.

screenshot:
    items:
        - title: Composable
          description: Secrets and configurations are organized into logical groupings called environments. Environments support importing one into another, allowing for easy composability and inheritance of shared secrets and configuration.
        - title: Traceable
          description: Never lose track of where configurations are being used. Trace the downstream impact of any secrets or configuration changes to see if they match expectations. 
        - title: Versionable
          description: Create different versions of environments, so you can gracefully migrate between breaking configuration changes.

integrate:
    header: Natively integrated with your tools
    cards:
        - title: Use any secrets store
          body: Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more. 
          icon: lock
          color: salmon
        - title: Access from anywhere
          body: Consume configuration and secrets in any environment from any application, tool, or CI/CD platform via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.
          icon: security
          color: purple

security:
    header: Security you can trust (and prove)
    items:
        - icon: lock
          icon_color: purple
          title: Robust Access Controls
          description: Pulumi ESC leverages the same Pulumi Cloud identity, RBAC, Teams, SAML/SCIM, OIDC, and scoped access tokens used for Pulumi IaC to ensure secrets management complies with enterprise security policies.
        - icon: clipboard
          icon_color: yellow
          title: Fully Auditable
          description: Every time secrets or configuration values are accessed or changed with Pulumi ESC, the action is fully logged for auditing. Logs include who accessed what, the action they took, and even a full record of showing which originating environments accessed values are inherited from.
        - icon: clock
          icon_color: salmon
          title: Dynamic Secrets
          description: Pulumi ESC connects to cloud providers and supporting secrets stores via OpenId Connect (OIDC), allowing it to generate dynamic, short-lived secrets on demand. This ensures secure, just-in-time access and reduces the risk of long-lived credentials being compromised.

features:
  - header: Centralized secrets management
    body: Access, share, and manage confidential information such as secrets, passwords, and API keys as well as configuration information such as network settings and deployment options.
  - header: Secrets orchestration
    body: Pull and sync configuration and secrets from any secrets store and consume in any application, tool, or CI/CD platform.
  - header: Composable environments
    body: Environments support importing one into another, allowing for easy composability and inheritance of shared secrets and configuration.
  - header: Versionable
    body: Every change to an environment as well as any of its secrets and configuration is versioned, so rolling back or accessing an old version is easy.
  - header: RBAC
    body: Role-based access controls (RBAC) makes it easy to secure your secrets and configurations by assigning permissions to users based on their role within your organization.
  - header: Dynamic secrets
    body: Connects to cloud providers and supporting secrets stores via OIDC to support generating just-in-time, short-lived credentials that revoke access when the lease expires.
  - header: Audit logging
    body: All actions taken on environments, secrets, or configuration values are fully logged for auditing.
  - header: Developer-friendly
    body: Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.

diagram:
    items:
        - number: 1
          description: Pulumi ESC organizes secrets and configurations into logical groupings called environments. Each environment can be composed of multiple environments allowing easy inheritance of shared secrets and configuration.
        - number: 2
          description: Pulumi ESC supports a variety of secrets stores as sources – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and it has an extensible plugin model that allows third-party secret stores.
        - number: 3
          description: Pulumi ESC makes it easy to integrate shared secrets and configurations into any application, tool, or CI/CD platform with a CLI, API, Kubernetes operator, and Typescript/Javascript, Python, and Go SDKs. Every value in an environment can be accessed from any execution environment.
        - number: 4
          description: Pulumi ESC leverages the same Pulumi Cloud identity, RBAC, Teams, SAML/SCIM, and scoped access tokens used for Pulumi IaC. Every environment is versioned with all changes fully logged for auditing.

customer_quotes:
  tetrate:
    text: |
      “With Pulumi ESC, our developers get dynamic AWS and Azure credentials on-demand. Onboarding new developers is quick and secure, with no more manually filling in .env templates.”
    author: Liam White, Platform Lead
    logo: tetrate
  mysten:
    text: |
      “Pulumi ESC has been a lifesaver for us. It’s nice to throw everything behind an ESC environment and eliminate one-off granting IAM permissions and other issues related to static credentials.”
    author: JK Jensen, Software Engineering Team Lead
    logo: mysten-labs

learn:
    title: Get Started
    items:
        - title: Try Pulumi ESC today
          description: Centralize and manage secrets securely on any cloud by creating a free Pulumi account.
          buttons:
            - link: https://app.pulumi.com/
              type: primary
              action: Try Pulumi ESC
        - title: Documentation
          description: Review our documentation to learn more about Pulumi ESC.
          buttons:
            - link: /docs/esc/
              type: secondary
              action: Pulumi ESC Docs
            - link: /docs/pulumi-cloud/esc/get-started/
              type: secondary
              action: Get Started with Pulumi ESC

---
