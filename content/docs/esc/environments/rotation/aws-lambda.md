---
title: AWS Lambda Rotation Connector
title_tag: AWS Lambda Rotation Connector
meta_desc: The `aws-lambda` connector enables you to rotate credentials inside of a private AWS VPC.
h1: AWS Lambda Rotation Connector
menu:
  esc:
    identifier: aws-lambda
    parent: esc-rotating-secrets
    weight: 1
---

The `aws-lambda` rotation connector enables you to rotate credentials inside of a private AWS VPC. Check out the [Rotated Secrets page](/docs/esc/integrations/rotated-secrets/) to learn which kinds of credentials can be rotated using Pulumi ESC. See [rotation connectors](/docs/esc/environments/rotation#rotation-connectors) section for more info on why rotation connectors are needed in the first place.

## Prerequisites

- A running database instance in AWS
- [Database users setup for rotation](/docs/esc/environments/rotation/db-user-setup)

## Setup Lambda Infrastructure

First, we need to setup infrastructure that will actually call your database and rotate the user credentials.

If you are using AWS RDS, we recommend using a template called `esc-connector-lambda-typescript`. You can instantiate a new project from it using either [New Project Wizard](https://www.pulumi.com/docs/idp/concepts/new-project-wizard/) or using [Pulumi CLI](https://www.pulumi.com/docs/iac/cli/) by running `pulumi new esc-connector-lambda-typescript`. Fill out the template configuration and run `pulumi up` to deploy the infrastructure.

If you are not using AWS RDS, or if you want to deploy connector infrastructure manually, take a look at the [template readme](https://github.com/pulumi/templates/blob/master/esc-connector-lambda-typescript/README.md).

The code that runs inside the lambda is open-source for full transparency, feel free to take a look [here](https://github.com/pulumi/esc-rotator-lambdas/tree/main/rotators/aws-lambda).

## Explanation of created environments

If you used the template above, it has already created 2 environments for you to hit the ground running with database credential rotations. Navigate to your Environments page in Pulumi Console and locate the 2 new environments.

The first one is the managing credentials environment, containing managing user credentials for your database and the [OIDC AWS login](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/aws-login/). Make sure to fill in your managing user credentials, using `fn::secret` for the password. Make sure to [restrict access](https://www.pulumi.com/docs/administration/organizations-teams/teams/) to this environment to only admin-level users, to ensure managing user credentials are safe.

The second new environment contains the rotator itself, referencing the first environment for the sensitive values. Adjust the `rotateUsers` and `database` fields to your values. If you're using a non-default port, you might need to change the actual rotator name after `fn::rotate::` - `mysql` or `postgres`, as the template guesses the database type by its default port.

That's all there is to it! You can now [import your rotator environment](https://www.pulumi.com/docs/esc/environments/imports/) into any other environment that needs database credentials to use right away.

## Rotate the environment

Now that you have a rotator environment setup, you can start rotating the actual secrets. To test it, you can manually rotate the environment by clicking on the `Rotate secrets` button inside the three-dot menu in your rotator environment or by running `pulumi env rotate org/project/environment` with your rotator environment name. Assuming rotation is successful, you will see a new `current` set of credentials in the `state` object of the rotator that you can use. If the rotation is not successful, you can find out what the issue was by navigating to the `Secret Rotation` tab and checking the `Last secret rotations` section.

On the same tab, you can also create [rotation schedules](https://www.pulumi.com/docs/esc/environments/rotation/#schedule) to automatically rotate the credentials after a period of time.
