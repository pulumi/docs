---
title_tag: "Security Hardening | Self-Hosting Pulumi"
meta_desc: Security hardening best practices for self-hosted Pulumi Cloud including network security, encryption, SMTP, and bot protection.
title: Security hardening
h1: Security hardening
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Security Hardening
    parent: administration-security-compliance-self-hosted-operations
    weight: 9
    identifier: administration-security-compliance-self-hosted-operations-security-hardening
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

This page covers security hardening recommendations for production self-hosted Pulumi Cloud deployments. For authentication configuration, see [SAML SSO](/docs/administration/self-hosting/saml-sso/).

## Network security

- Place the database and application containers in private subnets with no direct internet access.
- Use security groups or network policies to restrict traffic between tiers.
- Consider using an ingress allowlist (`ingressAllowList` config) to restrict access by IP range.
- All self-hosted installers support configuring CIDR-based allowlists on the ingress controller.

## Encryption

- **At rest**: Enable storage encryption on database clusters and object storage buckets.
- **In transit**: Enforce TLS on all connections (load balancer, database, object storage).
- **Secrets**: Store sensitive configuration (license keys, TLS certificates, SMTP credentials, database passwords) using `pulumi config set --secret`.

## SMTP and email

For production deployments, configure SMTP to enable:

- User invitation workflows
- Password reset emails
- Organization notifications

SMTP is optional for initial testing but required for production use. See the [API component reference](/docs/administration/self-hosting/components/api/) for SMTP environment variables.

## CAPTCHA and bot protection

Configure Cloudflare Turnstile for signup protection:

- Set `recaptchaSiteKey` (Turnstile widget site key)
- Set `recaptchaSecretKey` (Turnstile widget secret key)
