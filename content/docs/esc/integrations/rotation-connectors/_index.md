---
title: Rotation Connectors
title_tag: Rotate credentials in private networks with Rotation Connectors | Pulumi ESC
h1: Rotation Connectors
meta_desc: Pulumi ESC enables credential rotation in private networks using Rotation Connectors.
menu:
  esc:
    name: Rotation Connectors
    identifier: esc-rotation-connectors
    parent: esc-integrations
    weight: 2
---

Many organizations keep their databases in private networks, making it impossible for external credential managers (like ESC!) to rotate the credentials.

Pulumi ESC's solution to that problem are Rotation Connectors - open-source, easy-to-deploy pieces of insfrastructure that will securely rotate your credentials and store them in your ESC Environment for easy use.

See [Rotated Secrets](/docs/esc/integrations/rotated-secrets) page for details on which rotators require you to deploy a rotation connector.

Once you determined that you need one, follow the links below to learn how to set up and use each Rotation Connector.

| Rotation Connector                                                             | Description                                                                                                                     |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [AWS Lambda](/docs/esc/integrations/rotation-connectors/aws-lambda/)             | The `AWS Lambda` rotation connector enables you rotate credentials inside private AWS VPCs.                                     |
