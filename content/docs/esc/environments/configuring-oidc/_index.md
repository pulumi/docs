---
title_tag: Configure OpenID Connect | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange with Pulumi ESC
title: Configure OpenID Connect
h1: Configuring OpenID Connect for Pulumi ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: Configuring OIDC
    identifier: esc-configuring-oidc
    parent: esc-environments
    weight: 6
---

Pulumi ESC can be configured to act as an OpenID Connect (OIDC) provider, issuing signed, short-lived tokens. These tokens can then be exchanged by external systems for temporary cloud provider credentials, eliminating the need for hard-coded credentials.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789123:role/aws-role
          sessionName: esc-${context.pulumi.user.login}
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

In this example we have an environment definition and ARN that identifies us to AWS. We're requesting a short term token that will live for 1 hour for the session `sessionName: esc-${context.pulumi.user.login}`. This token will be used to provide access to the AWS services defined in the permissions policies set for the role.

## Configuring OpenID with your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

* [Configuring OIDC for AWS](/docs/esc/environments/configuring-oidc/aws/)
* [Configuring OIDC for Azure](/docs/esc/environments/configuring-oidc/azure/)
* [Configuring OIDC for Google Cloud](/docs/esc/environments/configuring-oidc/gcp/)
* [Configuring OIDC for Vault](/docs/esc/environments/configuring-oidc/vault/)
