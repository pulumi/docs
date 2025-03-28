---
title: mysql
title_tag: mysql Pulumi ESC Rotator
meta_desc: The `mysql` rotator enables you to rotate credentials for MySQL.
h1: mysql
menu:
  esc:
    identifier: mysql-rotator
    parent: esc-rotated-secrets
    weight: 2
---

The `mysql` rotator enables you to rotate user credentials for a MySQL database in your Environment.

## Example

```yaml
values:
  mysql:
    fn::rotate::mysql:
      inputs:
        database:
          connector:
            awsLambda:
              roleArn: arn:aws:iam::1234567890:role/your-role
              lambdaArn: arn:aws:lambda...
          database: dbname
          host: <database host>
          port: 3306
          managingUser:
            username: managinguser
            password:
              fn::secret: mypassword
        rotateUsers:
          username1: user1
          username2: user2
```

If you have existing usernames/passwords for the users to rotate that you want ESC to keep track of, you can optionally provide an initial `state`.

```yaml
values:
  mysql:
    fn::rotate::mysql:
      inputs:
        database:
          connector:
            awsLambda:
              roleArn: arn:aws:iam::1234567890:role/your-role
              lambdaArn: arn:aws:lambda...
          database: dbname
          host: <database host>
          port: 3306
          managingUser:
            username: managinguser
            password:
              fn::secret: <password>
        rotateUsers:
          username1: user1
          username2: user2
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

In order for ESC to connect to your database, you will need to use one of our connectors. Currently, only the AWS Lambda connector is supported.

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

| Property    | Type                                                | Description                      |
|-------------|-----------------------------------------------------|----------------------------------|
| `connector` | [DatabaseConnectorConfig](#databaseconnectorconfig) | Database connector configuration |

### DatabaseConnectorConfig

| Property    | Type                                                | Description                      |
|-------------|-----------------------------------------------------|----------------------------------|
| `awsLambda` | [AWSLambdaConfig](#awslambdaconfig)                 | AWS Lambda configuration         |

### AWSLambdaConfig

| Property    | Type   | Description                               |
|-------------|--------|-------------------------------------------|
| `roleArn`   | string | The ARN of the role to assume.            |
| `lambdaArn` | string | The ARN of the ESC Secret Rotation Lambda |

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
