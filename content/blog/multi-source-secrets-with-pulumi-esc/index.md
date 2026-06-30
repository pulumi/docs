---
title: "One ESC Environment, Many Secret Stores"
date: 2026-07-02
meta_desc: "Compose Pulumi ESC environments from AWS Secrets Manager, HashiCorp Vault, and 1Password so apps consume one resolved configuration view."
meta_image: meta.png
feature_image: feature.png
authors:
  - pablo-seibelt
tags:
  - esc
  - secrets
  - 1password
social:
    twitter: |
        Secrets rarely live in one place.

        Use Pulumi ESC to compose AWS Secrets Manager, HashiCorp Vault, and 1Password into one resolved environment.
    linkedin: |
        Most teams inherit multiple secret stores.

        This guide shows how Pulumi ESC can compose AWS Secrets Manager, HashiCorp Vault, and 1Password into one environment that applications and stacks can consume consistently.
    bluesky: |
        Secrets live everywhere.

        ESC can compose AWS Secrets Manager, Vault, and 1Password into one resolved config view.
---

Modern infrastructure often relies on multiple secret stores. You might use [AWS Secrets Manager](/docs/esc/integrations/dynamic-secrets/aws-secrets/) for cloud-native services, [HashiCorp Vault](/docs/esc/integrations/dynamic-secrets/vault-secrets/) for enterprise-wide secrets, and [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/) for team-shared credentials. Pulumi ESC gives teams one resolved view without forcing a migration away from the systems they already trust.

This post focuses on composing and orchestrating secrets across heterogeneous providers, including how to connect to Vault, handle naming conflicts, and define clear consumer interfaces.

By the end of this post, you will compose a single [Pulumi ESC](/docs/esc/) environment that aggregates secrets from AWS Secrets Manager, HashiCorp Vault, and 1Password. You will learn how to define provider boundaries, handle naming conflicts through namespacing, and provide a clean, resolved view of all secrets for your applications and CI/CD pipelines.

<!--more-->

## Why it matters now

Operational complexity and the risk of fragmented security policies increase as organizations adopt specialized secret stores. Without a central orchestration layer, it is impossible to get a unified view of who has access to what across the entire platform. Platform teams need a way to provide a consistent interface for developers while maintaining the security controls of each underlying provider.

## The challenge of secret sprawl

As organizations grow, secrets spread across different platforms. This sprawl leads to several issues:

1. Developers must learn multiple APIs and CLI tools.
2. Auditing access becomes difficult across fragmented systems.
3. Rotating secrets requires updates in multiple locations.
4. Applications need complex logic to fetch secrets from different providers.

Pulumi ESC addresses these challenges by acting as an orchestration layer. It doesn't replace your existing secret stores; it integrates with them to provide a consistent interface.

## Composing a multi-source environment

In Pulumi ESC, you define environments using YAML. You can pull secrets from various providers and map them into a single configuration tree.

Here is an example of an ESC environment that pulls secrets from AWS Secrets Manager, HashiCorp Vault, and 1Password:

```yaml
values:
  # AWS Secrets Manager for database credentials
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/esc-oidc
          sessionName: esc-multi-source-env
    secrets:
      fn::open::aws-secrets:
        region: us-west-2
        login: ${aws.login}
        get:
          db-password:
            secretId: prod/db/password

  # HashiCorp Vault for API keys
  vault:
    login:
      fn::open::vault-login:
        address: https://vault.example.com
        jwt:
          role: esc-reader
    secrets:
      fn::open::vault-secrets:
        login: ${vault.login}
        read:
          stripe-key:
            path: secret/stripe
            field: api_key

  # 1Password for shared team credentials
  onepassword:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken:
            fn::secret: "ops_123ABC"
        get:
          github-token:
            ref: "op://Engineering/GitHub/token"

  # Unified view for the application
  app-secrets:
    DB_PASSWORD: ${aws.secrets.db-password}
    STRIPE_API_KEY: ${vault.secrets.stripe-key}
    GITHUB_TOKEN: ${onepassword.secrets.github-token}
  environmentVariables:
    DB_PASSWORD: ${app-secrets.DB_PASSWORD}
    STRIPE_API_KEY: ${app-secrets.STRIPE_API_KEY}
    GITHUB_TOKEN: ${app-secrets.GITHUB_TOKEN}
```

The Vault connection happens in two steps. `fn::open::vault-login` authenticates ESC to Vault using the JWT/OIDC role configured in Vault, and `fn::open::vault-secrets` uses that login session to read a specific secret path. The `field: api_key` setting selects the literal `api_key` field stored at `secret/stripe`, so the unified view can reference `${vault.secrets.stripe-key}` without exposing the Vault response wrapper to consumers.

## Namespacing and precedence

By mapping secrets into specific keys like `app-secrets`, you create a clean interface for your applications. This namespacing prevents collisions between different sources.

If you need to override a secret for a specific environment, use `imports:` to compose a base environment and then override specific values in the child environment:

```yaml
imports:
  - acme/platform/base-secrets
values:
  app-secrets:
    DB_PASSWORD: ${aws.secrets.db-password}
```

Values defined in the child environment take precedence over imported values with the same path, which lets you keep common provider configuration in one place while overriding environment-specific secrets.

## Consuming the resolved view

Once your environment is defined, consumers don't need to know where the secrets originated. They only need to interact with the Pulumi ESC environment.

You can view the resolved secrets using the [Pulumi CLI](/docs/install/):

```bash
pulumi env open <org>/<project>/multi-source-env
```

This command returns a single JSON object containing all the resolved values. The `environmentVariables` block exposes selected values to `pulumi env run` and shell-based tools. Applications can also consume the resolved values through the Pulumi SDKs, ensuring a secure and consistent workflow.

By centralizing your secrets management with Pulumi ESC, you reduce complexity and strengthen your secrets management model without having to migrate your existing secret stores.

{{< blog/cta-button "Explore ESC dynamic secrets" "/docs/esc/integrations/dynamic-secrets/" >}}
