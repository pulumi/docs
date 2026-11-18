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

Connect an AWS account so an agent can use the AWS CLI for the work you delegate. [Pulumi ESC](/docs/esc/) supplies temporary credentials for the IAM role you choose when the task runs.

## Choose the AWS role

Choose an IAM role with permissions for the agent's work. For example, checking versioning on a known S3 bucket in your account requires [`s3:GetBucketVersioning`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) on that bucket. It doesn't require access to its objects or permission to change versioning.

If you reuse a deployment role, check for permissions the agent's assignment does not require. See [Choose integration permissions](/docs/ai/agents/permissions/#design-access-around-the-job) to choose which permissions to grant.

## Prepare an ESC environment

Use an ESC environment that supplies credentials for the role, or [configure OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/) to create one.

Use the [AWS login provider's OIDC configuration](/docs/esc/providers/login/aws-login/#oidc) to expose temporary credentials as `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. Set `AWS_REGION` to the region you want the agent to use.

Grant the agent's Pulumi Cloud role [permission to open the environment](/docs/ai/agents/permissions/#scope-pulumi-cloud-access), so ESC can supply credentials to the AWS CLI.

## Connect the environment

With permission to manage organization integrations (`org_integrations:update`):

{{% agent-cli-connection tool="AWS" %}}

For example, name the connection `production-aws-investigation` and include the AWS account ID in its notes.

## Use the connection

Include the connection name, AWS account, region, and target resources in the [assignment](/docs/ai/agents/configure/#save-and-assign-a-task).
