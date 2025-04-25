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

Pulumi ESC Rotators are ESC functions that enable you to rotate various credentials both automatically and manually for a number of supported services. Rotated credentials are stored in your ESC Environments, allowing you to easily and securely use them from anywhere. Some of the rotators require you to deploy [Rotation Connectors](/docs/esc/environments/rotation/#rotation-connectors) in order to rotate credentials inside private networks.

To learn how to set up and use each rotator, follow the links below. All rotators use [login providers](/docs/esc/integrations/dynamic-login-credentials/) for authorization, with the most secure way being OpenID Connect (OIDC) login providers. Learn more about how to configure them in [OpenID Connect](/docs/pulumi-cloud/oidc/) Pulumi Cloud documentation.

| Rotator                                                      |Required connector | Description                                                                                                                     |
|--------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [aws-iam](/docs/esc/integrations/rotated-secrets/aws-iam/)   |None               | The `aws-iam` rotator enables you to rotate access credentials for an AWS IAM User.                                                |
| [mysql](/docs/esc/integrations/rotated-secrets/mysql/)       |`aws-lambda`       | The `mysql` rotator enables you to rotate user credentials for a MySQL database in your Environment.                            |
| [postgres](/docs/esc/integrations/rotated-secrets/postgres/) |`aws-lambda`       | The `postgres` rotator enables you to rotate user credentials for a PostgreSQL database in your Environment.                    |
