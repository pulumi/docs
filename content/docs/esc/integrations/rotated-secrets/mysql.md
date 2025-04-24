---
title: mysql
title_tag: mysql Pulumi ESC Rotator
meta_desc: The `mysql` rotator enables you to rotate credentials for MySQL database.
h1: mysql
menu:
  esc:
    identifier: mysql-rotator
    parent: esc-rotated-secrets
    weight: 2
---

The `mysql` rotator enables you to rotate user credentials for a MySQL database in your Environment. This rotator requires that you setup an [`aws-lambda` rotation connector](/docs/esc/integrations/rotation-connectors/aws-lambda) first. Setting up the connector will also provide you with a ready-to-go rotation environment, making this page easier to understand.

## Example

Best practice is to have 2 separate environments, one with managing credentials that is restricted to admins only, and one with the rotator itself.

### Credentials Environment

```yaml
values:
  managingUser:
    username: managing_user # Replace with your user value
    password: manager_password # Replace with your user value behind fn::secret
  awsLogin:
    fn::open::aws-login:
      oidc:
        duration: 1h
        roleArn: arn:aws:iam::1234567890:role/... # Role that has permissions to rotate your credentials, setup as part of the aws-lambda rotation connector
        sessionName: pulumi-esc-secret-rotator
```

### Rotator Environment

```yaml
values:
  dbRotator:
    fn::rotate::mysql:
      inputs:
        database:
          connector:
            awsLambda:
              login: ${environments.rotatorExample.managingCredentials.awsLogin} # An implicit import from the above environment (assuming it's called rotatorExample/managingCredentials)
              lambdaArn: arn:aws:lambda:us-west-2:616138583583:function:PulumiEscSecretRotatorLambda-Function-e1c630a
          database: rotator_db
          host: iaro-rotator-mysql.cluster-chuqccm8uxqx.us-west-2.rds.amazonaws.com
          port: 3306
          managingUser: ${environments.rotatorTest.iaroManagingCreds.managingUser} # An implicit import from the above environment (assuming it's called rotatorExample/managingCredentials)
        rotateUsers:
          username1: user1
          username2: user2
```

### State

If you have existing users that you want to use right away, you can provide `state` object directly under the `fn::rotate::mysql` rotator.

```yaml
state:
  current:
    password:
      fn::secret: <password>
    username: user1
  previous:
    password:
      fn::secret: <password>
    username: user2
```

## Setup

## Inputs

| Property      | Type                              | Description            |
|---------------|-----------------------------------|------------------------|
| `database`    | [DatabaseConfig](#databaseconfig) | Database configuration |
| `rotateUsers` | [RotateUsers](#rotateusers)       | Users to rotate        |

## State (Optional)

| Property | Type                              | Description                                                                                               |
|----------|-----------------------------------|-----------------------------------------------------------------------------------------------------------|
| current  | [UserCredential](#usercredential) | Current credential information. These are the newest and recommended credentials.                         |
| previous | [UserCredential](#usercredential) | Previous credential information. These credentials are still valid, but will be phased out next rotation. |

## Outputs

| Property | Type                              | Description                                                                                               |
|----------|-----------------------------------|-----------------------------------------------------------------------------------------------------------|
| current  | [UserCredential](#usercredential) | Current credential information. These are the newest and recommended credentials.                         |
| previous | [UserCredential](#usercredential) | Previous credential information. These credentials are still valid, but will be phased out next rotation. |

### DatabaseConfig

| Property       | Type                                                | Description                                                     |
|----------------|-----------------------------------------------------|-----------------------------------------------------------------|
| `connector`    | [Connector](#connector)                             | Database connector configuration                                |
| `database`     | string                                              | Name of the database to use                                     |
| `host`         | string                                              | Endpoint of the database                                        |
| `port`         | int                                                 | Port of the database server                                     |
| `managingUser` | [UserCredential](#usercredential)                   | Credentials for a user that has priviledges to change passwords |

### Connector

| Property    | Type                                                | Description                      |
|-------------|-----------------------------------------------------|----------------------------------|
| `awsLambda` | [AWSLambdaConfig](#awslambdaconfig)                 | AWS Lambda configuration         |

### AWSLambdaConfig

| Property    | Type                                                                  | Description                                                     |
|-------------|-----------------------------------------------------------------------|-----------------------------------------------------------------|
| `login`     | [AWSLogin](/docs/esc/integrations/dynamic-login-credentials/aws-login) | AWS login that has access to assume `aws-lambda` connector role |
| `lambdaArn` | string                                                                | The ARN of the `aws-lambda` connector                           |

### RotateUsers

| Property    | Type   | Description                                                                                                   |
|-------------|--------|---------------------------------------------------------------------------------------------------------------|
| `username1` | string | Username of user in the database to rotate. If no state is provided, this user will be the one to be rotated. |
| `username2` | string | Username of user in the database to rotate.                                                                   |

### UserCredential

| Property   | Type   | Description                       |
|------------|--------|-----------------------------------|
| `username` | string | Username of user in the database. |
| `password` | string | Password of user in the database. |
