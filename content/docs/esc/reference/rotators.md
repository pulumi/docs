---
title: Rotators
title_tag: Rotators
h1: Rotators
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-rotators
    weight: 6
---

ESC rotators allow users to rotate credentials and secrets using ESC. These rotators are accessed via the `fn::rotate` built-in function. The credentials provided by a rotator are expected to be statically available, and should only change when the environment is [rotated](/docs/esc/environments/rotation/).

| Rotator                                                                        | Description                                                                                                                     |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [aws-iam](/docs/esc/integrations/rotated-secrets/aws-iam/)                     | The `aws-iam` rotator enables you rotate access credentials for an AWS IAM User.                                                |
