---
title: Rotation connectors
title_tag: Pulumi ESC rotation connectors
h1: Rotation connectors
meta_desc: Deploy Pulumi ESC rotation connectors so rotators can reach databases and services that live in private networks.
menu:
  esc:
    identifier: esc-operations-rotation
    parent: esc-operations
    weight: 1
---

Some [rotators](/docs/esc/providers/rotators/) need to reach the credential they're rotating — for example, the `mysql` and `postgres` rotators must connect to the database to change a user's password. When the target lives in a private network that Pulumi Cloud can't reach directly, a **rotation connector** runs the rotation inside that network on Pulumi Cloud's behalf.

For background on what rotation is and how the `fn::rotate::*` syntax works, see [Rotation](/docs/esc/concepts/rotators/).

## Available connectors

| Connector | Runtime | Used by |
|---|---|---|
| [AWS Lambda](/docs/esc/operations/rotation/aws-lambda/) | AWS Lambda inside a VPC | `mysql`, `postgres` |

## Setup checklists

- [Database user setup](/docs/esc/operations/rotation/db-user-setup/) — pre-create the database user (and grant the right permissions) that a rotator will manage.
