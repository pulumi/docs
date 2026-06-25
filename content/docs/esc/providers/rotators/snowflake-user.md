---
title: snowflake-user
title_tag: snowflake-user Pulumi ESC Rotator
meta_desc: The `snowflake-user` rotator enables you to rotate RSA keypairs for a Snowflake database user.
h1: snowflake-user
menu:
  esc:
    identifier: snowflake-user
    parent: esc-providers-rotators
    weight: 1
aliases:
  - /docs/esc/integrations/rotated-secrets/snowflake-user/
  - /docs/esc/concepts/providers/rotators/snowflake-user/
---

The `snowflake-user` rotator enables you to rotate RSA keypairs for a Snowflake database user in your Environment. It automatically manages the key rotation process, ensuring that two keys remain valid at any point in time, which allows for seamless credential rotation without disrupting service availability. (See [rotation concepts](/docs/esc/concepts/rotators/)).

## How Key Rotation Works

When the `snowflake-user` rotator is executed:

1. It connects to Snowflake using the provided login credentials.
2. It generates a new 2048-bit RSA keypair.
3. If a previous keypair exists in the state, it sets the user's `RSA_PUBLIC_KEY_2` to the previous public key.
4. It sets the user's `RSA_PUBLIC_KEY` to the new public key.
5. The new private key is stored securely in the environment state.

This two-key approach ensures that applications have time to update to the new key before the old one is completely removed, providing a smooth transition during rotation.

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

Follow the OIDC setup steps in the [snowflake-login documentation](/docs/esc/providers/login/snowflake-login/) to allow Pulumi ESC to authenticate as the rotation service user.

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

### Step 5: Managing credentials

Set up an environment with [Snowflake login credentials](/docs/esc/providers/login/snowflake-login/) for the rotation service user:

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

### Step 6: Rotated environment

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

### Alternative: authenticating with a private key

Instead of an OIDC `token` from the [snowflake-login](/docs/esc/providers/login/snowflake-login/) provider, the `login` can authenticate directly with a key-pair by supplying a `privateKey`. Provide `account`, `user`, and exactly one of `privateKey` or `token`:

```yaml
# my-org/rotators/snowflake-keyrotator
values:
  user:
    fn::rotate::snowflake-user:
      inputs:
        login:
          account: myorganization-account
          user: ESC_ROTATION_SERVICE_USER
          privateKey:
            fn::secret: |
              -----BEGIN PRIVATE KEY-----
              MIIEvQIBADANBgkqhkiG9w0BAQE...
              -----END PRIVATE KEY-----
        targetUser: ESC_ROTATION_DEMO_USER
```

## Validation

Perform a manual rotation on the environment to provision a new private key. If successful, should see output similar to the following when opening the environment:

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
| `token`      | string | OAuth token (output of [snowflake-login](/docs/esc/providers/login/snowflake-login/) provider).  |

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

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Rotation fails to authenticate to Snowflake | The OIDC security integration may be misconfigured, or the rotation service user may lack access. | Verify the `EXTERNAL_OAUTH` security integration values (issuer, JWKS URL, audience, allowed roles) and confirm the service user maps to the expected `login_name`. See [snowflake-login](/docs/esc/providers/login/snowflake-login/). |
| Rotation fails with a permissions error | The rotator role may not be able to alter the target user. | Confirm the rotator role can alter the target user, following the grants in [Configuring Snowflake for Key Rotation](#configuring-snowflake-for-key-rotation). |
| Applications fail to authenticate after a rotation | Applications may still be using the rotated-out public key (`RSA_PUBLIC_KEY_2`). | Update applications to the `current` private key; the previous key remains valid as `RSA_PUBLIC_KEY_2` until the next rotation. |

## Related

- [Rotators](/docs/esc/concepts/rotators/) - How credential rotation works in Pulumi ESC
- [snowflake-login](/docs/esc/providers/login/snowflake-login/) - Authenticate with Snowflake via OIDC
- [Rotators reference](/docs/esc/providers/rotators/) - Catalog of all ESC rotators
