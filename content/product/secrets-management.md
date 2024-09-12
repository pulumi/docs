---
title: "Pulumi ESC: Environments, Secrets, and Configuration"
layout: secrets-management

meta_title: "Pulumi ESC: Environments, Secrets, and Configuration"
meta_desc: Centralized environments, secrets, and configuration management for cloud applications and infrastructure
meta_image: "/images/product/esc-how-it-works-diagram.png"
aliases:
    - /esc
    - /product/esc

subtitle: Centralized secrets management & orchestration. Easily access, share, and manage secrets securely on any cloud, using your favorite programming languages.

overview:
    header: Centralized environments, secrets, and configuration management and orchestration that helps streamline operations, improve traceability, and ensure consistent security practices
    body: |
      - **Stop secret sprawl.** Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.  
      - **Trust (and prove) your secrets are secure.** Every environment can be locked down with role-based access controls (RBAC) and versioned with all changes fully logged for auditing.  
      - **Ditch `.env` files.** No more storing secrets in plaintext on dev computers. Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.
      - **Use with or without Pulumi IaC.** Use Pulumi ESC to centrally manage your configuration and secrets independently of Pulumi IaC, or use ESC and IaC together for the convenience of storing secrets in config with a higher degree of security than using plaintext.

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
          description: Pulumi ESC provides just-in-time, short-lived credentials, making them easy to adopt as a security best practice. 

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
    body: Generate just-in-time, short-lived credentials that revoke access when the lease expires.
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
