---
title: Rotating secrets
title_tag: Pulumi ESC rotating secrets
h1: Rotating secrets
meta_desc: Operational guidance for rotating secrets with Pulumi ESC — best practices and deploying rotation connectors for private networks.
menu:
  esc:
    identifier: esc-operations-rotation
    parent: esc-operations
    weight: 1
---

Operational guidance for rotating secrets with Pulumi ESC. For background on what rotation is and how the `fn::rotate::*` syntax works, see [Rotators](/docs/esc/concepts/rotators/).

## Best practices

See [Best practices](/docs/esc/operations/rotation/best-practices/) for guidance on least privilege, separation of concerns, composing rotated environments, and handling partial failures.

## Rotation connectors

Some [rotators](/docs/esc/providers/rotators/) need to reach the credential they're rotating — for example, the `mysql` and `postgres` rotators must connect to the database to change a user's password. When the target lives in a private network that Pulumi Cloud can't reach directly, a **rotation connector** runs the rotation inside that network on Pulumi Cloud's behalf.

### Available connectors

| Connector | Runtime | Used by |
|---|---|---|
| [AWS Lambda](/docs/esc/operations/rotation/aws-lambda/) | AWS Lambda inside a VPC | `mysql`, `postgres` |

### Setup checklists

- [Database user setup](/docs/esc/operations/rotation/db-user-setup/) — pre-create the database user (and grant the right permissions) that a rotator will manage.
