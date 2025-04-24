---
title: aws-lambda
title_tag: aws-lambda Pulumi ESC Rotation Connectors
meta_desc: The `aws-lambda` connector enables you to rotate credentials inside of a private AWS VPC.
h1: aws-lambda
menu:
  esc:
    identifier: aws-lambda
    parent: esc-rotation-connectors
    weight: 1
---

The `aws-lambda` rotation connector enables you to rotate credentials inside of a private AWS VPC. Check out the [Rotated Secrets page](/docs/esc/integrations/rotated-secrets/) to learn which kinds of credentials can be rotated using Pulumi ESC. See [rotation connectors](/docs/esc/integrations/rotation-connectors/) page for more info on why rotation connectors are needed in the first place.

AWS Lambda Connector supports rotation of database credentials MySQL and PostgreSQL databases. Before you start, connect to your existing database or provision a new one.

## User setup

First, you need to provision users that will be rotated. If you already have 2 existing users you can use those, otherwise run commands below to setup simple users. Make sure to replace `yourDatabase` with your database name and adjust priviledges as needed! You can also adjust the initial password to anything you'd like.

### MySQL

```
CREATE USER IF NOT EXISTS 'user1'@'%' IDENTIFIED BY 'initial_password';
GRANT SELECT, INSERT, UPDATE
    ON yourDatabase.*
    TO 'user1'@'%';
CREATE USER IF NOT EXISTS 'user2'@'%' IDENTIFIED BY 'initial_password';
GRANT SELECT, INSERT, UPDATE
    ON yourDatabase.*
    TO 'user2'@'%';
```

### PostgreSQL

```
CREATE USER user1 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user1;
CREATE USER user2 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user2;
```

## Managing user

Next, you need to setup a managing user, who will be in charge of actually rotating passwords for the 2 users we created above. Pulumi ESC will have access to this user, so we will scope down this user's priviledges to a minimum. Same as above, replace `yourDatabase` with your database name and `manager_password` with anything you'd like, just make sure to memorize or note it down somewhere.

### MySQL

```
CREATE USER IF NOT EXISTS 'managing_user'@'%' IDENTIFIED BY 'manager_password';
GRANT ALTER ON yourDatabase.* TO 'managing_user'@'%';
GRANT CREATE USER ON *.* TO 'managing_user'@'%';
```

### PostgreSQL

```
CREATE USER managing_user WITH PASSWORD 'manager_password';
ALTER USER managing_user WITH CREATEROLE;
GRANT user1 TO managing_user WITH ADMIN OPTION;
GRANT user2 TO managing_user WITH ADMIN OPTION;
```

## Setup Lambda Infrastructure

Now, we need to setup infrastructure that will actually call your database and rotate the user credentials.

The easiest way to do this is to use a template called `esc-connector-lambda-typescript`. You can instantiate a new project from it using either [New Project Wizard](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/new-project-wizard/) or using [Pulumi CLI](https://www.pulumi.com/docs/iac/cli/) by running `pulumi new esc-connector-lambda-typescript`.

Fill out the template configuration and run `pulumi up` to deploy the infrastructure. For more detailed information on how to deploy this template and on how to deploy connector infrastructure manually, take a look at the [template readme](https://github.com/pulumi/templates/blob/master/esc-connector-lambda-typescript/README.md).

The code that runs inside the lambda is open-source for full transparency, feel free to take a look [here](https://github.com/pulumi/esc-rotator-lambdas/tree/main/rotators/aws-lambda).

## Explanation of created environments

If you used the template above, it has already created 2 environments for you to hit the ground running with database credential rotations. Navigate to your Environments page in Pulumi Console and locate the 2 new environments.

The first one is the managing credentials environment, containing managing user credentials for your database and the [OIDC AWS login](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/aws-login/). Make sure to fill in your manager user credentials, using `fn::secret` for the password. Make sure to [restrict access](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/) to this environment to only admin-level users, to ensure managing user credentials are safe.

The second new environment contains the rotator itself, referencing the first environment for the senstitive values. Adjust the `rotateUsers` and `database` fields to your values. If you're using a non-default port, you might need to change the actual rotator name after `fn::rotate::` - `mysql` or `postgres`.

That's all there is to it! You can now [import your rotator environment](https://www.pulumi.com/docs/esc/environments/imports/) into any other environment that needs database credentials to use right away.

## Rotate the environment

Now that you have a rotator environment setup, you can start rotating the actual secrets. To test, you can manually rotate the environment by clicking on the `Rotate secrets` button inside the three-dot menu in your rotator environment or by running `pulumi env rotate org/project/environment` with your rotator environment name. Assuming rotation is successful, you will see a new `current` set of credentials in the `state` object of the rotator that you can use. If the rotation is not successful, you can find out what the issue was by navigating to the `Secret Rotation` tab and checking the `Last secret rotations` section.

On the same tab, you can also create [rotation schedules](https://www.pulumi.com/docs/esc/environments/rotation/#schedule) to automatically rotate the credentials after a period of time.
