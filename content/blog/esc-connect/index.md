---
title: "Introducing ESC Connect: Integrate Any Secret Source with Pulumi ESC"
date: 2025-12-01
allow_long_title: true
meta_desc: "ESC Connect enables you to integrate any custom or proprietary secret source with Pulumi ESC through simple HTTPS adapters, without waiting for native support."
meta_image: meta.png
authors:
- claire-gaestel
tags:
- esc
- secrets
- features
---

We're excited to announce ESC Connect — a new capability that lets you integrate any secret source with [Pulumi ESC](/product/esc/) by building simple HTTPS adapter services. If you've ever needed to pull secrets from a proprietary system, a legacy tool, or a third-party service that doesn't have native ESC support, you no longer have to wait for us to build a provider. You can build your own adapter in an afternoon and start using it immediately.

<!--more-->

Pulumi ESC has [native integrations](/docs/esc/integrations/) with popular secret management systems like [AWS Secrets Manager](/docs/esc/integrations/dynamic-secrets/aws-secrets/), [Azure KeyVault](/docs/esc/integrations/dynamic-secrets/azure-secrets/), [HashiCorp Vault](/docs/esc/integrations/dynamic-secrets/vault-secrets/), [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/), and others. But in real-world infrastructure, you often need to work with systems that fall outside this list. Maybe you built a custom secret management system years ago and it's still running in production. Maybe you're using a niche third-party service. Maybe your secrets are locked behind a firewall in a legacy system that predates modern APIs.

ESC Connect changes this by letting you build simple HTTPS adapter services using the [`external` provider](/docs/esc/integrations/dynamic-secrets/external/). Your adapter handles requests from ESC, fetches secrets from your custom source, and returns them. ESC handles authentication with signed JWT tokens, so you get fine-grained control over access without building a complete security infrastructure.

## Building an adapter

Here's an [ESC environment](/docs/esc/environments/) configuration that uses ESC Connect:

```yaml
values:
  customSecrets:
    fn::open::external:
      url: https://my-adapter.example.com/fetch-secrets
      request:
        secretName: DATABASE_PASSWORD
```

When you open this environment, ESC makes an authenticated POST request to your adapter. 
Your adapter validates the JWT token, fetches the secret from your source, and returns it:

```typescript
const handler = async (event) => {
    // 1. Validate JWT from Authorization header
    const claims = await validateJWT(event.headers.Authorization);

    // 2. Verify audience and body hash for security
    verifyAudience(claims.aud, event.url);
    verifyBodyHash(event.body, claims.body_hash);

    // 3. Fetch secret from your source
    const request = JSON.parse(event.body);
    const secret = await fetchFromYourSource(request.secretName);

    // 4. Return the secret
    return { statusCode: 200, body: JSON.stringify(secret) };
};
```

The [example reference implementation](#try-it-out) includes an `ESCRequestValidator` class that handles JWT verification and request integrity checking for you. See the [documentation](/docs/esc/integrations/dynamic-secrets/external/) for detailed security requirements and examples in other languages.

## Automated rotation

ESC Connect also supports automated secret rotation through [`fn::rotate::external`](/docs/esc/integrations/rotated-secrets/external/). Your rotation adapter receives the current credential state, generates new credentials, updates your target system, and returns the new state. ESC handles scheduling and maintains both current and previous credentials during transitions for zero-downtime rotation.

```yaml
values:
  rotatedCredentials:
    fn::rotate::external:
      inputs:
        url: https://my-adapter.example.com/rotate
        request:
          service: database
          environment: production
```

Learn more about [secret rotation in Pulumi ESC](/docs/esc/environments/rotation/) and the [external rotator implementation patterns](/docs/esc/integrations/rotated-secrets/external/).

## Try it out

ESC Connect is available now in Pulumi ESC. We've created a [deployable reference adapter implementation](https://github.com/pulumi/examples/tree/master/aws-ts-esc-external-adapter-lambda) on AWS Lambda that demonstrates secure request validation:

[![Deploy this example with Pulumi](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/examples/blob/master/aws-ts-esc-external-adapter-lambda/README.md)

Check out the documentation for the [external provider](/docs/esc/integrations/dynamic-secrets/external/) and [external rotator](/docs/esc/integrations/rotated-secrets/external/) to learn more about building production adapters.

To learn more about Pulumi ESC, explore the [ESC documentation](/docs/esc/) or [get started for free](/docs/esc/get-started/). If you build an adapter for a system that others might find useful, share it in the [Pulumi Community Slack](https://slack.pulumi.com) — we'd love to see what you build.
