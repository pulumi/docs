---
title: "Keep your secrets secure, by default"
date: 2021-02-19
draft: false
meta_desc: Pulumi keeps your infrastructure passwords, tokens, keys, and more secure, by default.
meta_image: secure_by_default.png
authors:
    - alex-mullans
tags:
    - security
    - secrets
---

An unauthorized user gaining access to your infrastructure can be catastrophic: data can be stolen or leaked, security holes can be exploited, and more. That risk makes it critical to keep the infrastructure secrets—the passwords, access tokens, keys, and so on—well-protected. This is particularly true in automated systems, like continuous integration and delivery and infrastructure-as-code systems.

<!--more-->

## Pulumi’s built-in secret storage

Pulumi takes these risks seriously. That’s why we built the Pulumi platform to be secure by default. It protects all secret data using Pulumi’s built-in [secret storage](https://www.pulumi.com/docs/concepts/secrets/). This secret store “just works”, regardless of whether you use our hosted [Pulumi Service](https://www.pulumi.com/product/#teams), the [Self-Hosted Pulumi Service](https://www.pulumi.com/docs/pulumi-cloud/self-hosted/), or the [self-managed backend](https://www.pulumi.com/docs/concepts/state/#backends). The Pulumi Service protects secrets automatically when you create a stack with `pulumi new` or `pulumi stack init`. If you use a self-managed backend like AWS S3 or Google Cloud Storage, secrets are protected by a passphrase that you choose when you start a new stack with `pulumi new`. In all cases, every Pulumi [stack](https://www.pulumi.com/docs/concepts/stack/) gets a unique encryption key.

## What secrets are protected

Pulumi protects all of the [`state`](https://www.pulumi.com/docs/concepts/state/) metadata that it knows about your infrastructure with encryption: encryption in transit when it’s sent to your backend and encryption at rest (if you’re using the hosted or self-hosted Pulumi Service). This base layer of protection applies to all state, including both non-secret and secret metadata. Secret storage is the next level of protection. It ensures that secret values are never exposed in plaintext in any file that Pulumi writes to your disk. Secrets are identified in a few ways:

- All Pulumi providers—both native providers like [`azure-native`](https://github.com/pulumi/pulumi-azure-native/) and Terraform-based providers like [Datadog](https://github.com/pulumi/terraform-provider-datadog)—know which of their outputs should be secret and mark them as such. This ensures that you're secure by default  when you start using a new provider. There's no need to pick which outputs are secret or worry that you’ve missed one.
- You can mark other Pulumi outputs [as secret](https://www.pulumi.com/docs/concepts/secrets/#explicitly-marking-resource-outputs-as-secrets).
- In addition to Pulumi inputs and outputs, you can also mark Pulumi configuration values [as secret](https://www.pulumi.com/docs/concepts/secrets/#secrets).

Any secret identified by you or by Pulumi is fully protected in the secret storage and not stored in plaintext on disk. This prevents leaks of secrets when files are committed to a source code repository or uploaded to a continuous integration and delivery system.

## Integration with other secret stores

For smaller organizations, the secret storage built into Pulumi is usually sufficient. In larger organizations however, it’s likely that a centralized secret management system is already in use, like [AWS Key Management System](https://aws.amazon.com/kms/), [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/), [Google Cloud Key Management](https://cloud.google.com/security-key-management), or [Hashicorp Vault](https://www.vaultproject.io/). Pulumi integrates with each of these systems to make it easy to [protect secrets](https://www.pulumi.com/docs/concepts/secrets/#initializing-a-stack-with-alternative-encryption) in the way required by the organization.

## Next steps

It’s easy to get started with secrets management in Pulumi, because there’s nothing extra you need to do. Begin with any one of our [get started tutorials](https://www.pulumi.com/docs/quickstart/) and Pulumi will automatically protect your secrets along the way.

[Learn more about Pulumi’s secret storage in our docs](https://www.pulumi.com/docs/concepts/secrets/)
