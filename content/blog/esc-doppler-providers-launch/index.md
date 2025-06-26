---
title: "Announcing Doppler Providers for Pulumi ESC: Dynamic Login and Dynamic Secrets" 
date: 2025-06-26
allow_long_title: true
meta_desc: "Pulumi ESC adds Doppler providers for dynamic OIDC login and centralized secret fetching, enhancing security and simplifying management."
meta_image: meta.png 
authors:
  - robert-harris
tags:
  - esc
  - secrets
  - doppler 
  - features
  - configuration-management
  - dynamic-secrets
  - oidc
---

We are excited to announce support for [Doppler](https://doppler.com/) within [Pulumi ESC](/product/esc)! Pulumi ESC centralizes secrets and configuration management, providing a unified source of truth across your environments. With the addition of Doppler, a popular secrets management platform, ESC further extends its ecosystem, enabling seamless and secure access to secrets stored across diverse systems.

<!--more-->

This release introduces two distinct dynamic providers for Doppler, each designed to improve security and streamline your workflows: 

*   **[`doppler-login`](/docs/esc/integrations/dynamic-login-credentials/doppler-login/) (Dynamic Login):** This provider securely generates short-lived OIDC access tokens for authenticating *to* Doppler. Static, long-lived credentials are a significant security risk. The `doppler-login` provider directly addresses this by generating temporary, just-in-time credentials using OIDC. **Use this provider when you need temporary credentials to interact directly with Doppler**, for instance, using the Doppler CLI or SDKs in local development or CI/CD pipelines, without storing long-lived static tokens. ESC manages the OIDC flow, providing a fresh token when needed.

*   **[`doppler-secrets`](/docs/esc/integrations/dynamic-secrets/doppler-secrets/) (Dynamic Secrets):** This provider dynamically fetches secrets stored *within* your Doppler configs and makes them available within the Pulumi ESC environment. **Use this provider when you need specific secrets *from* Doppler to configure your applications or infrastructure managed via ESC.** This centralizes secret consumption, allowing you to access Doppler secrets using the same consistent ESC patterns used for AWS, Azure, GCP, Infisical, Vault, 1Password, and more.

Pulumi ESC acts as a robust **secrets broker** provider consistent API interface for all your tools, applications and workflows. It securely handles *both* the generation of temporary authentication credentials (like with `doppler-login`) and the fetching of application secrets (like with `doppler-secrets`) from various providers such as Doppler, cloud platforms ([AWS](/docs/esc/integrations/dynamic-secrets/aws-secrets/), [Azure](/docs/esc/integrations/dynamic-secrets/azure-secrets/), [GCP](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)), and other secret managers ([Infisical](/docs/esc/integrations/dynamic-secrets/infisical-secrets/), [Vault](/docs/esc/integrations/dynamic-secrets/vault-secrets/), [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/)). Once centralized in ESC, these secrets and configurations are consistently available for you to consume via ESC's many developer friendly methods including the [ESC SDK](/docs/esc/development/languages-sdks/), [ESC CLI](/docs/esc/cli/), [Kubernetes External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/), [CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/), or sync them to various platforms where they are needed such as [GitHub Secrets](https://github.com/pulumi/esc-examples/tree/main/sync/github-secrets), [AWS Secrets Manager](https://github.com/pulumi/esc-examples/tree/main/sync/aws-secrets-manager), and more!

## Getting Started: Using the Doppler Providers

Let's walk through how to configure and use each provider.

### Prerequisites

Your Doppler workplace must be on the Team or Enterprise plan in order to use OIDC (via service account identities).

Configure Doppler for OpenID Connect(OIDC) before you try out the providers. Follow the steps in [Doppler OIDC documentation](/docs/esc/environments/configuring-oidc/doppler/). This involves creating a Service Account Identity in Doppler, with OIDC authentication pointing to `https://api.pulumi.com/oidc`, and configuring the audience and subject claims. Note down the **Identity ID**.

### How to Use the doppler-login Provider (Dynamic Authentication)

1. Create a Pulumi ESC environment (e.g., `pulumi-org/doppler-auth/oidc-login`) with the following environment definition and update the `identityId`.

```yaml
# Environment: pulumi-org/doppler-auth/oidc-login
values:
  doppler:
    # Configure the Dynamic Login provider using OIDC
    login:
      fn::open::doppler-login:
        oidc:
          identityId: <your-identity-id> # Replace with your Doppler Identity ID
  
  # Expose the token as an environment variable for easy consumption
  environmentVariables:
    DOPPLER_TOKEN: ${doppler.login.accessToken}
```

2. Save the environment.
3. Validate the environment by clicking on Open in the Pulumi Cloud console, or running `esc open pulumi-org/doppler-auth/oidc-login` in your CLI. The output will include the `doppler.login.accessToken`.
4. Usage Example: Run Doppler CLI commands dynamically:
```bash
esc run pulumi-org/doppler-auth/oidc-login -- doppler secrets download --no-file --format=json --project=<your-project-id> --config=<your-config-id> 
# The DOPPLER_TOKEN env var is automatically injected
```

### How to Use the doppler-secrets Provider (Dynamically Fetching Secrets)

Use this provider to pull secrets *from* Doppler *into* your ESC environment for consumption by your applications, CI/CD systems, Pulumi IaC, Terraform and more!

1.  Create an ESC environment where you need the secrets (e.g., `pulumi-org/my-app/dev`).
2.  **Import** the dynamic login environment (if using OIDC for authentication, which is recommended). This makes the temporary Doppler token available.
3.  Configure the `doppler-secrets` provider, referencing the imported login details. See example below. 
4.  Specify the secrets to fetch using the `get` block. Replace placeholders.

```yaml
# Environment: pulumi-org/my-app/dev
imports:
  # Import the environment performing Dynamic Login (recommended)
  - pulumi-org/doppler-auth/oidc-login # Use the path to your login environment

values:
  # Define a structure to hold secrets fetched from Doppler
  dopplerSecrets: 
    fn::open::doppler-secrets:
      # Authenticate using the token from the imported Dynamic Login environment
      login: ${doppler.login} # Pass the login object from the import
      # Specify the Doppler project and config to retrieve secrets from
      project: example-project
      config: dev
      # Specify secrets to retrieve from Doppler
      get:
        # Define names for the secrets as they will appear in ESC's output under 'dopplerSecrets'
        apiKey: # This is the name within ESC
          name: API_KEY # The name of the secret in Doppler
        appSecret: # Pull another secret into ESC
          name: APP_SECRET
  
  # Optionally, map fetched secrets to environment variables for application consumption
  environmentVariables:
    API_KEY: ${dopplerSecrets.apiKey}
    APP_SECRET: ${dopplerSecrets.appSecret}
```
5.  Save the environment.
6.  Validate the environment by clicking on Open in the Pulumi Cloud console, or running `esc open pulumi-org/my-app/dev` in your CLI. The output will show the imported `doppler.login`, the fetched secrets under `dopplerSecrets`, and the mapped `environmentVariables`.
7.  **Usage Example:** Run an application that needs these secrets:
    ```bash
    esc run pulumi-org/my-app/dev -- node app.js 
    # The API_KEY and APP_SECRET env vars are automatically injected
    ```

## Conclusion

The new `doppler-login` and `doppler-secrets` providers for Pulumi ESC offer powerful and secure ways to interact with Doppler. Use `doppler-login` for dynamic, short-lived OIDC authentication when interacting directly with Doppler APIs or CLIs. Use `doppler-secrets` to securely fetch secrets *from* Doppler *into* your centralized ESC environment. Together, they enhance your security posture and simplify configuration management.

We encourage you to explore these new capabilities. Dive into the [doppler-login](/docs/esc/integrations/dynamic-login-credentials/doppler-login/), [doppler-secrets](/docs/esc/integrations/dynamic-secrets/doppler-secrets/) for detailed configuration options, check out the broader [Pulumi ESC Documentation](/docs/esc/), and share your feedback or ask questions in the [Pulumi Community Slack](https://slack.pulumi.com/).
