---
title: Rotated secrets
title_tag: Rotate credentials in Pulumi ESC with Rotators | Pulumi ESC
h1: Rotate credentials for external services
meta_desc: Pulumi ESC enables credential rotation for various external services.
menu:
  esc:
    name: Rotated secrets
    identifier: esc-rotated-secrets
    parent: esc-integrations
    weight: 2
---

Pulumi ESC Rotators enable you to rotate credentials both automatically and manually for a number of supported services.

To learn how to set up and use each rotator, follow the links below. To learn how to configure OpenID Connect (OIDC) for the rotators that support it, see [OpenID Connect integration](/docs/pulumi-cloud/oidc/) in the Pulumi Cloud documentation.

| Rotator                                                      | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [aws-iam](/docs/esc/integrations/rotated-secrets/aws-iam/)   | The `aws-iam` rotator enables you rotate access credentials for an AWS IAM User.                             |
| [mysql](/docs/esc/integrations/rotated-secrets/mysql/)       | The `mysql` rotator enables you to rotate user credentials for a MySQL database in your Environment.         |
| [postgres](/docs/esc/integrations/rotated-secrets/postgres/) | The `postgres` rotator enables you to rotate user credentials for a PostgreSQL database in your Environment. |
