---
title: "Announcing Infisical Support for Pulumi ESC: Dynamic Login and Secrets"
date: 2025-04-15T10:00:00-07:00
allow_long_title: true
meta_desc: "Pulumi ESC adds integration support for Infisical, enabling teams to generate dynamic Infisical login credentials and centralize secrets management by fetching values from Infisical."
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
---

We are excited to announce integration support for [Infisical](https://infisical.com/) within [Pulumi ESC](/product/esc)! Pulumi ESC is a powerful tool designed to **centralize your secrets and configuration management**, providing a single source of truth across your environments and applications. Infisical, a rapidly growing open-source secrets management platform, is the latest addition to ESC's expanding ecosystem of integrations, making it even easier to manage all your sensitive data in one place.

<!--more-->

This release introduces two key dynamic providers for Infisical:

*   **Dynamic Login (`infisical-login`):** Securely generates short-lived OIDC access tokens for authenticating *to* Infisical, eliminating the need for static service account tokens. 
*   **Dynamic Secrets (`infisical-secrets`):** Dynamically fetches secrets stored within your Infisical projects, centralizing their access alongside secrets from other sources managed by ESC.

## Enhanced Security with Dynamic Credentials & Centralized Access

Static, long-lived credentials pose a significant security risk as they can be inadvertently exposed over time. Pulumi ESC addresses this through dynamic capabilities. The **Dynamic Login** provider for Infisical enhances security by generating temporary, just-in-time OIDC tokens for authentication. This drastically reduces the exposure window compared to static tokens. The **Dynamic Secrets** provider allows ESC to fetch secrets stored in Infisical when needed, centralizing access control and consumption patterns.

Pulumi ESC acts as a powerful **secrets broker**, securely handling both the generation of temporary credentials (Dynamic Login) and the fetching of application secrets (Dynamic Secrets) from various providers like Infisical, cloud platforms ([AWS](/docs/esc/integrations/dynamic-secrets/aws-secrets/), [Azure](/docs/esc/integrations/dynamic-secrets/azure-secrets/), [GCP](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)), and other managers ([Vault](/docs/esc/integrations/dynamic-secrets/vault-secrets/), [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/)). Once centralized in ESC, secrets are consistently available via environment variables, Pulumi configuration, SDKs, CLI, Kubernetes integrations ([Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/), [CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/)), or sync workflows ([GitHub Secrets](https://github.com/pulumi/esc-examples/tree/main/sync/github-secrets), [AWS Secrets Manager](https://github.com/pulumi/esc-examples/tree/main/sync/aws-secrets-manager)).


## Getting Started

### Step 1: Configure Dynamic Login (`infisical-login`)

1. In your Infisical project, follow these steps to setup OIDC and note your Identity ID.
2. Create a Pulumi ESC Environment (e.g., `infisical/oidc-login`). Replace `<your-identity-id>`.
3. Click Open on the Console to ensure your ESC environment is configured correctly. 

```yaml
# Environment: infisical/oidc-login
values:
  infisical:
    # Configure the Dynamic Login provider
    login:
      fn::open::infisical-login:
        oidc:
          identityId: <your-identity-id>
  environmentVariables:
    ARM_ACCESS_TOKEN: ${infisical.login.accessToken}
```

This environment now provides ${infisical.login.accessToken}. You can use the ESC CLI to run Infisical CLI commands dynamically. 


### Step 2: Fetch Stored Secrets via Dynamic Secrets (infisical-secrets)

Use the temporary token from Step 1 to fetch secrets stored within Infisical.

1.  Create or modify the target ESC Environment (e.g., my-app/dev-config).
2. import the Dynamic Login environment (infisical/oidc-login).
3. Configure the Dynamic Secrets provider (infisical-secrets), authenticating with ${infisical.login.accessToken}.
5. Specify secrets to fetch. Replace placeholders.
5. Click Open environment to retrive the secrets from Infisical 

**Infisical provider syntax:**

```yaml
# Environment: my-app/dev-config
imports:
  # Import the environment performing Dynamic Login
  - infisical/oidc-login

values:
  # Define where fetched secrets will be stored
  secrets:
    # Use the Dynamic Secrets provider for Infisical
    fn::open::infisical-secrets:
      # Authenticate using the token from Dynamic Login
      login:
        accessToken: ${infisical.login.accessToken}
      # Specify secrets to retrieve
      retrieve: 
        apiKey:
          projectId: <replace-with-your-projectID>
          environment: <replace-with-your-environment-slug>
          secretKey: /api/service/key
```

Now, esc run my-app/dev-config -- your-command securely provides the necessary secrets to your-command.

You can use this for PUlumi IaC

{{< video title="Pulumi ESC Infisical Dynamic Login & Secrets Demo" src="placeholder-video.mp4" >}}

## Conclusion

The new Infisical integration enhances Pulumi ESC, offering improved security through Dynamic Login for temporary credentials and centralized management via Dynamic Secrets fetching. This combination allows ESC to act as a secure broker for your Infisical secrets, simplifying access and bolstering your security posture.

We encourage you to explore these new capabilities. Visit the Pulumi ESC Infisical Providers Documentation to get started, check out the broader Pulumi ESC Documentation, and share your feedback or connect with us on the Pulumi Community Slack.