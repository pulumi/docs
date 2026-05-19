---
title: "Five HashiCorp Vault Patterns for Pulumi Teams"
date: 2026-06-23
meta_desc: "Use Pulumi with HashiCorp Vault for production patterns covering secrets engines, namespaces, policies, auth methods, and an ESC migration bridge."
meta_image: meta.png
feature_image: feature.png
authors:
- pablo-seibelt
tags:
- vault
- secrets
- patterns
social:
    twitter: |
        Vault plus Pulumi is more than writing secrets.

        Model engines, namespaces, policies, auth methods, and ESC bridges as repeatable platform patterns.
    linkedin: |
        HashiCorp Vault management becomes safer when the platform patterns are explicit.

        This guide covers five Pulumi patterns for secrets engines, namespaces, policies, auth methods, and an ESC bridge for consumers.
    bluesky: |
        Vault plus Pulumi: secrets engines, namespaces, policies, auth methods, and ESC bridges as repeatable patterns.

        See how the five Vault patterns fit together.
---

[HashiCorp Vault](https://www.vaultproject.io/) is a widely used secrets management platform that provides a centralized way to store, access, and protect sensitive data. Teams managing Vault configuration with Pulumi need repeatable patterns with the same rigor and automation as cloud infrastructure.

This post is not a product comparison between ESC and Vault. Instead, it's a guide for teams already using Vault who want to automate its configuration and bridge it with ESC.

## The pain of manual Vault configuration

When platform teams manage Vault through the CLI or UI, they often create bespoke clusters. These clusters have inconsistent policies, namespaces, and auth methods that are difficult to audit and impossible to replicate for disaster recovery. Manual configuration also slows down application teams who must wait for secrets engines or roles to be provisioned before they can deploy their workloads.

## Why it matters now

Operational risk and audit pressure increase as secrets management becomes a bottleneck for platform velocity. A single misconfigured policy or a missing auth role can block an entire release cycle or create a security gap. Automating Vault configuration ensures that security controls are applied consistently across every environment, from development to production.

## Reader outcome

By the end of this post, you will implement five production-grade patterns for managing HashiCorp Vault with Pulumi. You will learn how to provision secrets engines, isolate environments with namespaces, define granular policies, configure Kubernetes authentication, and build an ESC migration bridge to orchestrate secrets across your entire platform.

<!--more-->

## Pattern 1: Secrets engines

The first step in any Vault deployment is enabling and configuring secrets engines. With Pulumi, you can manage these as resources, ensuring that your storage backends are consistently configured across environments.

```typescript
import * as vault from "@pulumi/vault";

const kvv2 = new vault.Mount("kvv2", {
    path: "secret",
    type: "kv",
    options: {
        version: "2",
    },
    description: "Production KV Version 2 secrets engine",
});
```

Using `vault.Mount` allows you to define the path, type, and version of your secrets engine. This is particularly useful for KV (Key-Value) stores where you might want to enforce [KV version 2](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) for features like secret versioning and soft deletes. If your Vault already has a `secret/` mount, choose a free path or import the existing mount instead of creating a duplicate.

## Pattern 2: Namespace per environment

Vault namespaces, a Vault Enterprise feature, isolate data and configuration. A common pattern is one namespace per environment: development, staging, and production.

```typescript
const environments = ["development", "staging", "production"];
const namespaces = environments.map(env => new vault.Namespace(env, {
    path: env,
}));
```

By managing namespaces with Pulumi, you can ensure that your isolation boundaries are created automatically as part of your infrastructure rollout.

## Pattern 3: Token-bound policies

Vault policies define what actions are allowed on specific paths. Apply least privilege by scoping each policy to the smallest path set its role needs.

```typescript
const appPolicy = new vault.Policy("app-policy", {
    name: "app-policy",
    policy: `
path "secret/data/app/*" {
  capabilities = ["read"]
}
`,
});
```

Template literals let you compose policy bodies from variables or other resource outputs when you need dynamic values.

## Pattern 4: Kubernetes auth method

Vault can authenticate workloads using their native identities. For [Kubernetes](https://kubernetes.io/), this means using ServiceAccounts to authenticate pods.

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const kubernetesCaCert = config.requireSecret("kubernetesCaCert");
const tokenReviewerJwt = config.requireSecret("tokenReviewerJwt");

const k8sAuth = new vault.AuthBackend("kubernetes", {
    type: "kubernetes",
    path: "kubernetes",
});

const k8sAuthConfig = new vault.kubernetes.AuthBackendConfig("k8s-config", {
    backend: k8sAuth.path,
    kubernetesHost: "https://kubernetes.default.svc.cluster.local:443",
    kubernetesCaCert: kubernetesCaCert,
    tokenReviewerJwt: tokenReviewerJwt,
    issuer: "https://kubernetes.default.svc.cluster.local",
});

const appRole = new vault.kubernetes.AuthBackendRole("app-role", {
    backend: k8sAuth.path,
    roleName: "web-app",
    boundServiceAccountNames: ["web-app-sa"],
    boundServiceAccountNamespaces: ["production"],
    tokenPolicies: [appPolicy.name],
    tokenTtl: 3600,
}, { dependsOn: [k8sAuthConfig] });
```

This pattern involves three steps: enabling the Kubernetes auth backend, configuring it with cluster details, and creating roles that map ServiceAccounts to Vault policies. The `production` value in `boundServiceAccountNamespaces` is the Kubernetes namespace, not the Vault Enterprise namespace.

## Pattern 5: ESC migration bridge

As organizations modernize their secrets management, they often look to [Pulumi ESC](/docs/esc/) for environment-wide secrets orchestration. You can use Pulumi to bridge your existing Vault secrets into ESC environments.

This bridge allows you to continue using Vault as your primary secret store while using ESC's version tagging and import-based inheritance features. By referencing Vault paths in your ESC configuration, you can provide a unified interface for your developers. The example assumes the KV v2 mount and database secret exist inside the `production` Vault namespace; provision them with the same patterns above and set the Vault provider namespace when managing namespaced resources.

```yaml
values:
  vault:
    login:
      fn::open::vault-login:
        address: https://vault.example.com
        namespace: production
        jwt:
          role: esc-reader
    secrets:
      fn::open::vault-secrets:
        login: ${vault.login}
        read:
          database:
            path: secret/data/database
            field: password
  app:
    databasePassword: ${vault.secrets.database}
```

## Conclusion

Managing HashiCorp Vault with Pulumi brings the power of IaC to your security infrastructure. Start by codifying one Vault mount, namespace, or auth method, then use Pulumi ESC to expose the secrets your applications already consume.

{{< blog/cta-button "Manage secrets with Pulumi ESC" "/docs/esc/integrations/dynamic-secrets/vault-secrets/" >}}
