---
title: Rotators
title_tag: Pulumi ESC rotators
h1: Rotators
meta_desc: Pulumi ESC rotators replace credentials for AWS IAM, Azure apps, MySQL, PostgreSQL, Snowflake, and custom services on a schedule or on demand.
menu:
  esc:
    name: Rotators
    identifier: esc-providers-rotators
    parent: esc-home
    weight: 4
aliases:
  - /docs/esc/integrations/rotated-secrets/
  - /docs/esc/concepts/providers/rotators/
---

Reference catalog of the credential rotators shipped with Pulumi ESC. For an introduction to how rotators work — the rotation lifecycle, scheduling, permissions, and best practices — see [Rotators](/docs/esc/concepts/rotators/). For deploying rotation connectors so a rotator can reach a target inside a private network, see [Rotation connectors](/docs/esc/operations/rotation/).

| Rotator | Required connector | Description |
|---|---|---|
| [aws-iam](/docs/esc/providers/rotators/aws-iam/) | None | Rotate access credentials for an AWS IAM user. |
| [azure-app-secret](/docs/esc/providers/rotators/azure-app-secret/) | None | Rotate client secrets for an Azure app registration. |
| [mysql](/docs/esc/providers/rotators/mysql/) | `aws-lambda` (private networks only) | Rotate user credentials for a MySQL database. |
| [password](/docs/esc/providers/rotators/password/) | None | Rotate any user-defined key using password generation rules. |
| [passphrase](/docs/esc/providers/rotators/passphrase/) | None | Rotate any user-defined key using memorable passphrase generation rules. |
| [postgres](/docs/esc/providers/rotators/postgres/) | `aws-lambda` (private networks only) | Rotate user credentials for a PostgreSQL database. |
| [snowflake-user](/docs/esc/providers/rotators/snowflake-user/) | None | Rotate RSA keypairs for a Snowflake user. |
| [external](/docs/esc/providers/rotators/external/) | None | Rotate credentials using a custom service adapter. |
