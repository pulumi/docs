---
title: Rotators
title_tag: Rotators
h1: Provider
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-rotators
    weight: 6
---

ESC rotators allow users to rotate credentials and secrets using ESC. These providers are accessed via the `fn::rotate` built-in function.

| Rotator                                                                        | Description                                                                                                                     |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [aws-iam](/docs/esc/integrations/rotated-secrets/aws-iam/)                     | The `aws-iam` rotator enables you rotate access credentials for an AWS IAM User.                                                |
