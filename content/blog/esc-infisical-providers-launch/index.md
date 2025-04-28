---
title: "Announcing Infisical Providers for Pulumi ESC: Dynamic Login and Dynamic Secrets" 
date: 2025-04-28
allow_long_title: true
meta_desc: "Pulumi ESC adds Infisical providers for dynamic OIDC login and centralized secret fetching, enhancing security and simplifying management."
meta_image: meta.png 
authors:
  - boris-schlosser
  - arun-loganathan
tags:
  - esc
  - secrets
  - infisical
  - features
  - configuration-management
  - dynamic-secrets
  - oidc
---

We are thrilled to announce enhanced integration support for [Infisical](https://infisical.com/) within [Pulumi ESC](/product/esc)! Pulumi ESC centralizes secrets and configuration management, providing a unified source of truth across your environments. With the addition of Infisical, a popular open-source secrets management platform, ESC further extends its ecosystem, enabling seamless and secure access to secrets stored across diverse systems.

<!--more-->

This release introduces two distinct dynamic providers for Infisical, each designed to improve security and streamline your workflows: 

*   **[`infisical-login`](/docs/esc/integrations/dynamic-login-credentials/infisical-login/) (Dynamic Login):** This provider securely generates short-lived OIDC access tokens for authenticating *to* Infisical. Static, long-lived credentials are a significant security risk. The `infisical-login` provider directly addresses this by generating temporary, just-in-time credentials using OIDC. **Use this provider when you need temporary credentials to interact directly with Infisical**, for instance, using the Infisical CLI or SDKs in local development or CI/CD pipelines, without storing long-lived static tokens. ESC manages the OIDC flow, providing a fresh token when needed.

*   **[`infisical-secrets`](/docs/esc/integrations/dynamic-secrets/infisical-secrets/) (Dynamic Secrets):** This provider dynamically fetches secrets stored *within* your Infisical projects and makes them available within the Pulumi ESC environment. **Use this provider when you need specific secrets *from* Infisical to configure your applications or infrastructure managed via ESC.** This centralizes secret consumption, allowing you to access Infisical secrets using the same consistent ESC patterns used for AWS, Azure, GCP, Vault, 1Password, and more.

Pulumi ESC acts as a robust **secrets broker** provider consistent API interface for all your tools, applications and workflows. It securely handles *both* the generation of temporary authentication credentials (like with `infisical-login`) and the fetching of application secrets (like with `infisical-secrets`) from various providers such as Infisical, cloud platforms ([AWS](/docs/esc/integrations/dynamic-secrets/aws-secrets/), [Azure](/docs/esc/integrations/dynamic-secrets/azure-secrets/), [GCP](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)), and other secret managers ([Vault](/docs/esc/integrations/dynamic-secrets/vault-secrets/), [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/)). Once centralized in ESC, these secrets and configurations are consistently available for you to consume via ESC's many developer friendly methods including the [ESC SDK](/docs/esc/development/languages-sdks/), [ESC CLI](/docs/esc/cli/), [Kubernetes External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/), [CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/), or sync them to various platforms where they are needed such as [GitHub Secrets](https://github.com/pulumi/esc-examples/tree/main/sync/github-secrets), [AWS Secrets Manager](https://github.com/pulumi/esc-examples/tree/main/sync/aws-secrets-manager), and more!

## Getting Started: Using the Infisical Providers

Let's walk through how to configure and use each provider.

### Prerequisites

Configure Infisical for OpenID Connect(OIDC) before you try out the providers. Follow the steps in [Infisical OIDC documentation](/docs/esc/environments/configuring-oidc/infisical/). This involves creating an Identity in Infisical, adding OIDC authentication pointing to `https://api.pulumi.com/oidc`, and configuring the audience and subject claims. Note down the **Identity ID**.

### How to Use the infisical-login Provider (Dynamic Authentication)

1. Create a Pulumi ESC environment (e.g., `pulumi-org/infisical-auth/oidc-login`) with the following environment definition and update the `identityId`.

```yaml
# Environment: pulumi-org/infisical-auth/oidc-login
values:
  infisical:
    # Configure the Dynamic Login provider using OIDC
    login:
      fn::open::infisical-login:
        oidc:
          identityId: <your-identity-id> # Replace with your Infisical Identity ID
  
  # Expose the token as an environment variable for easy consumption
  environmentVariables:
    INFISICAL_TOKEN: ${infisical.login.accessToken}
```

2. Save the environment.
3. Validate the environment by clicking on Open in the Pulumi Cloud console, or running `esc open pulumi-org/infisical-auth/oidc-login` in your CLI. The output will include the infisical.login.accessToken.
4. Usage Example: Run Infisical CLI commands dynamically:
```bash
esc run pulumi-org/infisical-auth/oidc-login -- infisical secrets get API_KEY --projectId=<your-project-id>
# The INFISICAL_TOKEN env var is automatically injected
```

### How to Use the infisical-secrets Provider (Dynamically Fetching Secrets)

Use this provider to pull secrets *from* Infisical *into* your ESC environment for consumption by your applications, CI/CD systems, Pulumi IaC, Terraform and more!

1.  Create an ESC environment where you need the secrets (e.g., `pulumi-org/my-app/dev`).
2.  **Import** the dynamic login environment (if using OIDC for authentication, which is recommended). This makes the temporary Infisical token available.
3.  Configure the `infisical-secrets` provider, referencing the imported login details. See example below. 
4.  Specify the secrets to fetch using the `get` block. Replace placeholders.

```yaml
# Environment: pulumi-org/my-app/dev
imports:
  # Import the environment performing Dynamic Login (recommended)
  - pulumi-org/infisical-auth/oidc-login # Use the path to your login environment

values:
  # Define a structure to hold secrets fetched from Infisical
  infisicalSecrets: 
    fn::open::infisical-secrets:
      # Authenticate using the token from the imported Dynamic Login environment
      login: ${infisical.login} # Pass the login object from the import
      # Specify secrets to retrieve from Infisical
      get:
        # Define names for the secrets as they will appear in ESC's output under 'infisicalSecrets'
        apiKey: # This is the name within ESC
          projectId: <your-infisical-project-id> 
          environment: prod # The Infisical environment slug (e.g., 'prod', 'dev')
          secretKey: api-key # The key of the secret in Infisical
        appSecret: # Pull another secret `app-secret` into ESC
          projectId: <your-infisical-project-id>
          environment: dev
          secretKey: app-secret 
  
  # Optionally, map fetched secrets to environment variables for application consumption
  environmentVariables:
    API_KEY: ${infisicalSecrets.apiKey}
    APP_SECRET: ${infisicalSecrets.appSecret}
```
5.  Save the environment.
6.  Validate the environment by clicking on Open in the Pulumi Cloud console, or running `esc open pulumi-org/my-app/dev` in your CLI. The output will show the imported `infisical.login`, the fetched secrets under `infisicalSecrets`, and the mapped `environmentVariables`.
7.  **Usage Example:** Run an application that needs these secrets:
    ```bash
    esc run pulumi-org/my-app/dev -- node app.js 
    # The API_KEY and APP_SECRET env vars are automatically injected
    ```

## Conclusion

The new `infisical-login` and `infisical-secrets` providers for Pulumi ESC offer powerful and secure ways to interact with Infisical. Use `infisical-login` for dynamic, short-lived OIDC authentication when interacting directly with Infisical APIs or CLIs. Use `infisical-secrets` to securely fetch secrets *from* Infisical *into* your centralized ESC environment. Together, they enhance your security posture and simplify configuration management.

We encourage you to explore these new capabilities. Dive into the [infisical-login](/docs/esc/integrations/dynamic-login-credentials/infisical-login/), [infisical-secrets](/docs/esc/integrations/dynamic-secrets/infisical-secrets/) for detailed configuration options, check out the broader [Pulumi ESC Documentation](/docs/esc/), and share your feedback or ask questions in the [Pulumi Community Slack](https://slack.pulumi.com/).
