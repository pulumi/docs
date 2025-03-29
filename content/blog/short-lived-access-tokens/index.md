---
title: "Announcing Short Lived Access Tokens in Pulumi Cloud"

date: 2024-06-25T09:08:31-07:00

draft: false

meta_desc: Introducing short-lived access tokens in Pulumi Cloud for enhanced security
  and flexibility, now available in the console and REST API.

meta_image: meta.png

authors:
  - meagan-cojocar

tags:
  - releases

search:
  keywords:
    - Tokens
    - Security
    - Access Tokens
    - Short-Lived
---

We are excited to introduce a new feature that our users have been eagerly awaiting: Short-Lived Access Tokens! This enhancement allows you to set an optional expiry date on [Personal Access Token](/docs/pulumi-cloud/access-management/access-tokens/#personal-access-tokens), [Team Access Token](/docs/pulumi-cloud/access-management/access-tokens/#team-access-tokens), and [Organization Access Token](/docs/pulumi-cloud/access-management/access-tokens/#organization-access-tokens), making them automatically invalid after a specified date. This feature is now available in the [Pulumi Cloud console](https://app.pulumi.com) and the [Pulumi Cloud REST API](/blog/short-lived-access-tokens/create-token.mp4), providing enhanced security and control over your access tokens.

<!--more-->

## Why Short-Lived Access Tokens?

Security and flexibility are paramount in managing infrastructure as code (IaC) and [Environments, Secrets and Config (ESC)](/docs/esc), and our users have consistently requested the ability to create access tokens with a limited lifespan. With short-lived access tokens, you can:

1. **Enhance Security**: By limiting the lifespan of your access tokens, you reduce the risk of tokens being misused if they are inadvertently exposed.
2. **Improve Automation**: Automate token management in your CI/CD pipelines, ensuring that tokens expire as needed and can then be rotated.
3. **Simplify Audits**: Easily track and manage token expirations, ensuring compliance with your organization’s security policies.

## How It Works

### Creating Short-Lived Tokens in the console

When creating a [new access token in the Pulumi Console](/docs/pulumi-cloud/access-management/access-tokens), you will now see an optional expiry date field. Simply set the date when you want the token to expire, and it will automatically become invalid on that date. This feature is available for Personal Access Tokens, Team Access Tokens, and Organization Access Tokens (note: Team Access Tokens and Organization Access Tokens are only available in the Enterprise and Business Critical editions of Pulumi Cloud).

{{< video title="Short Lived Access Token in Pulumi Cloud" src="create-token.mp4" controls="false" autoplay="true" loop="true" >}}

Learn more by reviewing [our access token documentation](/docs/pulumi-cloud/access-management/access-tokens).

### OIDC Trust Relationships

A few months ago [we released OpenID Connect (OIDC) Trust Relationships for Pulumi Cloud](/blog/oidc-trust-relationships), allowing you to generate short-lived Pulumi Cloud tokens using OIDC from within your CI/CD pipelines, such as GitHub Actions. Now we are exposing the optional expiration field in the console and in the REST API. Your OIDC generated tokens will also show in the UI alongside those created with other methods.

### REST API Support

We have also exposed this functionality in the Pulumi REST API, allowing you to programmatically create and manage short-lived tokens. This makes it easier to integrate token management into your automation scripts and tools.

```bash
# Example API request to create a short-lived token
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{"description": "{description}", "name": "{unique_name}", "expires": 0}' \
  https://api.pulumi.com/api/orgs/{org}/teams/{team}/tokens
```

## Try It Today

We invite you to try out the new short lived access tokens in Pulumi Cloud. As always, we value your feedback and look forward to hearing how this feature helps streamline your workflows and enhances security.

For more details, check out [our documentation](/docs/pulumi-cloud/access-management/access-tokens) and [API reference docs](/docs/pulumi-cloud/cloud-rest-api). If you have any questions or need assistance, [our support team](https://support.pulumi.com/hc/en-us) is here to help.
