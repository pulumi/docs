---
title: postgres
title_tag: postgres Pulumi ESC Rotator
meta_desc: The `postgres` rotator enables you to rotate credentials for Postgres.
h1: postgres
menu:
  esc:
    identifier: postgres-rotator
    parent: esc-rotated-secrets
    weight: 4
---

The `postgres` rotator enables you to rotate user credentials for a PostgreSQL database in your Environment.

## Prerequisites

- A running database instance in AWS
- [Database users setup for rotation](/docs/esc/environments/rotation/db-user-setup)
- [AWS Lambda Rotation Connector setup](/docs/esc/environments/rotation/aws-lambda)

## Example

Best practice is to have 2 separate environments, one with managing credentials that is restricted to admins only, and one with the rotator itself.

### Credentials Environment

```yaml
values:
  managingUser:
    username: managing_user # Replace with your username value
    password:
      # Replace ciphertext below with your password, keeping fn::secret to encrypt it, like so "fn::secret: <password>"
      fn::secret:
        ciphertext: ZXNjeAAAAAEAAAEAFatkojHgMRjHuWIwKbPqplpSUoKCrtLUCwtU0rhJuhtOa6eUBM/kxRgB/rp9
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
    fn::rotate::postgres:
      inputs:
        database:
          connector:
            awsLambda:
              login: ${environments.rotatorExample.managingCredentials.awsLogin} # An implicit import from the above environment (assuming it's called rotatorExample/managingCredentials)
              lambdaArn: arn:aws:lambda:aws-region:111111111111:function:PulumiEscSecretRotatorLambda-Function-xxxxxxx
          database: rotator_example_db
          host: rotator-example-mysql.cluster-xxxxxxxxxxxx.aws-region.rds.amazonaws.com
          port: 5432
          managingUser: ${environments.rotatorExample.managingCredentials.managingUser} # An implicit import from the above environment (assuming it's called rotatorExample/managingCredentials)
        rotateUsers:
          username1: user1
          username2: user2
```

Note the 2 usernames inside the `rotateUsers` field - these are the users whose passwords will be rotated by the managing user. Once rotated, the usernames and their corresponding password will be stored in the `state` object. We need 2 users to ensure no apps using these credentials ever go down - while one of the users is being rotated, the other will be used and vice versa.

### State

If you have existing users that you want to use right away, you can provide the `state` object directly under the `fn::rotate::postgres` rotator.

The users are cycled in the following manner: when `username1` is the `current` user, `username2` is `previous` and vice versa. During a rotation, `previous` user's password is changed and its credentials are put into `current` user, with the other user moved to `previous`. Your apps should always use the `current` credentials, this way after a rotation, these credentials are still valid, just stored in the `previous` user, and your app can switch on the next configuration retrieval. One thing you have to be mindful of is to not rotate your secrets more frequently than your apps update their configuration - this will lead to them attempting to use credentials that are already rotated out.

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
| `managingUser` | [UserCredential](#usercredential)                   | Credentials for a user that has privileges to change passwords  |

### Connector

| Property    | Type                                | Description                      |
|-------------|-------------------------------------|----------------------------------|
| `awsLambda` | [AWSLambdaConfig](#awslambdaconfig) | An [AWS Lambda connector](/docs/esc/environment/rotation/aws-lambda) needs to be setup |

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
