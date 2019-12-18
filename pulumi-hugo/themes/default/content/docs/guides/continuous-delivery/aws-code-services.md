---
title: AWS Code Services
meta_desc: This page provides an overview of how to use Pulumi with Amazon Code
           Services CI/CD tools.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-aws-code-services/
- /docs/console/continuous-delivery/aws-code-services/
---

[Amazon Code Services](https://aws.amazon.com/products/developer-tools/) encompases a variety
of specific tools for CI/CD, including [CodePipeline](https://aws.amazon.com/codepipeline/),
[CodeBuild](https://aws.amazon.com/codebuild/), [CodeDeploy](https://aws.amazon.com/codedeploy/),
and others.

To incorporate updating Pulumi stacks into an AWS Code Services-managed CI/CD system, you'll
want to use CodeBuild. Pulumi needs to execute a built program in order to determine the desired
state of cloud resources, and CodeBuild provides a compute environment to do just that.

If you are using CodePipeline, you can then create a new pipeline stage which triggers the
CodeBuild project. Allowing you to update a Pulumi stack wherever it makes sense in your existing
pipeline.

## Configuring CodeBuild

To update a Pulumi stack as part of a CodeBuild project, you'll need to add an environment variable
named `PULUMI_ACCESS_TOKEN`. This is required to authenticate with pulumi.com in order to perform
an update. You can create a new Pulumi access token specifically for your CloudBuild project on
your [Pulumi Account page](https://app.pulumi.com/account/tokens).

Because of the sensitive nature of the access token, it is recommended that the Pulumi access
token be stored in Amazon's Systems Manager (SSM) Parameter Store. This allows you to keep the value secret, while
providing auditable access to CodeBuild.

### Service Role

When Pulumi runs, it needs credentials in order to make any changes to AWS resources. When
`pulumi up` is running on the CloudBuild machine, it will default to using the credentials of
the AWS CodeBuild Service role defined in the CodeBuild project.

In order for Pulumi to successfully update the stack, the running CodeBuild service role needs to
have IAM policies sufficient for updating the resources referenced by the Pulumi program.
This can be done by defining new IAM policies and attaching them to the CloudBuild project's service
role.

For more information on how to manage the IAM policies used in CodeBuild,
see [Amazon's documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up.html#setting-up-service-role).

## Scripts

With the CloudBuild project created, you then just need to add two files to your repository:
`buildspec.yml` and `update_pulumi_stack.sh`.

### buildspec.yml

The following is a minimal `buildspec.yml`, which describes the steps CodeBuild should perform when
building your project. This includes downloading and installing the Pulumi CLI and then running a
script specific to building and updating your stack.

```yaml
version: 0.2

phases:
  install:
    commands:
      # pulumi
      - curl -fsSL https://get.pulumi.com/ | sh
      - export PATH=$PATH:$HOME/.pulumi/bin
  build:
    commands:
      - update_pulumi_stack.sh
```

### update_pulumi_stack.sh

`update_pulumi_stack.sh` is the minimal set of steps for updating a Pulumi stack.

It runs `npm` commands to download the dependencies of the Pulumi program, and then builds it.
And then uses the Pulumi CLI to select the stack and perform the update.

You'll want to modify this script depending on the language used for your program, how it is
built, etc.

```bash
echo "Updating Pulumi Stack"

# Download dependencies and build
npm install
npm run build

# Update the stack
pulumi stack select acme/website-production
pulumi up --yes
```

That's it! With the CloudBuild project configured to update your Pulumi stack on-demand,
you can now incorporate it into other AWS Code Services products.
