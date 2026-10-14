---
title: Connect AWS
title_tag: Connect AWS | Pulumi Agents
h1: Connect AWS
meta_desc: Connect an AWS account to Pulumi Agents using temporary credentials from Pulumi ESC.
menu:
    ai:
        name: AWS
        parent: ai-integrations-cli
        weight: 10
---

Connect an AWS account so an agent can inspect resources through the AWS CLI. Pulumi ESC supplies credentials when the task runs. The setup is the same for Neo and agents you configure.

## Choose the AWS role

Choose an IAM role with permissions for the agent's work. For example, checking versioning on a known S3 bucket in your account requires [`s3:GetBucketVersioning`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) on that bucket. It doesn't require access to its objects or permission to change versioning.

If you reuse a deployment role, check for permissions the investigation doesn't need. See [Design access around the job](/docs/ai/agents/permissions/#design-access-around-the-job) for guidance on identities and credential scope.

## Prepare an ESC environment

Use an ESC environment that supplies credentials for the role, or [configure OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/) to create one.

Use the [AWS login provider's OIDC configuration](/docs/esc/providers/login/aws-login/#oidc) to expose temporary credentials as `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. Set `AWS_REGION` to the region you want the agent to use.

The agent also needs [permission to open the environment](/docs/ai/agents/permissions/#scope-pulumi-cloud-access).

## Connect the environment

As an organization administrator:

{{% agent-cli-connection tool="AWS" %}}

For example, name the connection `production-aws-investigation` and include the AWS account ID in its notes.
