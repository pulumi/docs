---
title: snowflake-user
title_tag: snowflake-user Pulumi ESC Rotator
meta_desc: The `snowflake-user` rotator enables you to rotate RSA keypairs for a Snowflake database user.
h1: snowflake-user
menu:
  esc:
    identifier: snowflake-user
    parent: esc-rotated-secrets
---

The `snowflake-user` rotator enables you to rotate RSA keypairs for a Snowflake database user in your Environment. It automatically manages the key rotation process, ensuring that two keys remain valid at any point in time, which allows for seamless credential rotation without disrupting service availability. (See [rotation concepts](/docs/esc/environments/rotation/)).

## Example

First, set up an environment with Snowflake login credentials:

```yaml
# my-org/logins/snowflake
values:
  snowflake:
    account: myorganization-account
    login:
      fn::open::snowflake-login:
        oidc:
          account: myorganization-account
          user: ESC_ROTATION_SERVICE_USER
          role: ESC_ROTATOR
```

Then, create a separate environment for your rotated credentials:

```yaml
# my-org/rotators/snowflake-keyrotator
values:
  user:
    fn::rotate::snowflake-user:
      inputs:
        login: ${environments.logins.snowflake.snowflake.login}
        targetUser: ESC_ROTATION_DEMO_USER
```

If you have existing keys you want ESC to keep track of, you can optionally provide an initial `state`:

```yaml
# my-org/rotators/snowflake-keyrotator
values:
  user:
    fn::rotate::snowflake-user:
      inputs:
        login: ${environments.logins.snowflake.snowflake.login}
        targetUser: ESC_ROTATION_DEMO_USER
      state:
        account: myorganization-account
        privateKey:
          fn::secret: |
            -----BEGIN PRIVATE KEY-----
            MIIEvQIBADANBgkqhkiG9w0BAQE...
            -----END PRIVATE KEY-----
        createdAt: "2025-01-01T12:00:00Z"
```

## Configuring Snowflake for Key Rotation

### Step 1: Create the Target User

Create the Snowflake user whose keys will be rotated:

```sql
CREATE USER ESC_ROTATION_DEMO_USER
  DEFAULT_ROLE = 'PUBLIC'
  TYPE = SERVICE;
```

### Step 2: Create a Rotator Role

Create a role that has permission to alter the target user:

```sql
CREATE ROLE ESC_ROTATOR;
GRANT OWNERSHIP ON USER ESC_ROTATION_DEMO_USER TO ROLE ESC_ROTATOR;
```

### Step 3: Create a Rotation Service User

Create a service user that will perform the rotation:

```sql
CREATE USER ESC_ROTATION_SERVICE_USER
  DEFAULT_ROLE = 'ESC_ROTATOR'
  TYPE = SERVICE;
GRANT ROLE ESC_ROTATOR TO USER ESC_ROTATION_SERVICE_USER;
```

The rotation service user should have minimal permissions, only enough to alter the target user.

### Step 4: Set Up OIDC for the Rotation Service User

Follow the OIDC setup steps in the [snowflake-login documentation](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/) to allow Pulumi ESC to authenticate as the rotation service user.

```sql
CREATE SECURITY INTEGRATION pulumi_oidc
  TYPE = EXTERNAL_OAUTH
  ENABLED = TRUE
  EXTERNAL_OAUTH_TYPE = CUSTOM
  EXTERNAL_OAUTH_ISSUER = 'https://api.pulumi.com/oidc'
  EXTERNAL_OAUTH_JWS_KEYS_URL = 'https://api.pulumi.com/oidc/.well-known/jwks'
  EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = 'snowflake_user'
  EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'login_name'
  EXTERNAL_OAUTH_AUDIENCE_LIST = ('snowflake:<pulumi-org>')
  EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ('ESC_ROTATOR')
  EXTERNAL_OAUTH_ANY_ROLE_MODE = 'ENABLE';
```

Replace `<pulumi-org>` with your Pulumi organization name.

## Validation

You can validate that your configuration is working by running either of the following:

* `esc open <org>/<project>/<environment>` command of the [ESC CLI](/docs/esc-cli/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

You should see output similar to the following:

```json
{
  "user": {
    "account": "myorganization-account",
    "user": "ESC_ROTATION_DEMO_USER",
    "privateKey": "[secret]",
    "rotatedAt": "2025-04-24T10:00:00Z"
  }
}
```

## Inputs

| Property          | Type                        | Description                                                                                 |
|-------------------|-----------------------------|--------------------------------------------------------------------------------------------|
| `login`           | [SnowflakeLogin](#snowflakelogin) | Required. Credentials used to connect to Snowflake and perform the rotation.              |
| `targetUser`      | string                      | Required. The Snowflake user whose keypair will be rotated.                                 |

### SnowflakeLogin

The `login` object must contain:

| Property   | Type   | Description                                      |
|------------|--------|--------------------------------------------------|
| `account`  | string | Required. Snowflake account identifier.          |
| `user`     | string | Required. Managing user to connect as. This user must have permission to alter the target user. |

And exactly one of:

| Property     | Type   | Description                                                                                                             |
|--------------|--------|-------------------------------------------------------------------------------------------------------------------------|
| `privateKey` | string | Private key in PEM format.                                                                                              |
| `token`      | string | OAuth token (output of [snowflake-login](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/) provider).  |

## State (Optional)

| Property    | Type   | Description                                                            |
|-------------|--------|------------------------------------------------------------------------|
| `account`   | string | Snowflake account identifier.                                          |
| `privateKey`| string | The private key in PEM format.                                         |
| `createdAt` | string | When the keypair was generated, in RFC3339 format.                     |

## Outputs

| Property    | Type   | Description                                                           |
|-------------|--------|-----------------------------------------------------------------------|
| `account`   | string | Snowflake account identifier.                                         |
| `user`      | string | The rotated user.                                                     |
| `privateKey`| string | Private key in PEM format (stored as a secret).                       |
| `rotatedAt` | string | When the keypair was generated, in RFC3339 format.                    |

## How Key Rotation Works

When the `snowflake-user` rotator is executed:

1. It connects to Snowflake using the provided login credentials.
2. It generates a new 2048-bit RSA keypair.
3. If a previous keypair exists in the state, it sets the user's `RSA_PUBLIC_KEY_2` to the previous public key.
4. It sets the user's `RSA_PUBLIC_KEY` to the new public key.
5. The new private key is stored securely in the environment state.

This two-key approach ensures that applications have time to update to the new key before the old one is completely removed, providing a smooth transition during rotation.
