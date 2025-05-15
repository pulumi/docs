---
title: snowflake-login
title_tag: snowflake-login Pulumi ESC Provider
meta_desc: The `snowflake-login` provider enables OIDC authentication to Snowflake for use with Pulumi ESC.
h1: snowflake-login
menu:
  esc:
    identifier: snowflake-login
    parent: esc-dynamic-login-credentials
---

The `snowflake-login` provider enables authentication to Snowflake using OpenID Connect (OIDC) for Pulumi ESC. This allows you to securely access Snowflake without storing long-lived credentials in your environment configurations.

## Configuring OIDC for Snowflake

To use OIDC authentication with Snowflake, you need to set up a security integration in Snowflake that trusts the Pulumi OIDC provider.

### Step 1: Create a Security Integration in Snowflake

Execute the following SQL in your Snowflake account to create a security integration:
Refer to the Snowflake's [Configure custom authorization servers for External OAuth](https://docs.snowflake.com/en/user-guide/oauth-ext-custom) documentation for more information.

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
  -- Optionally, restrict to specific roles:
  -- EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ('<snowflake roles that can be assumed>')
  -- EXTERNAL_OAUTH_ANY_ROLE_MODE = 'ENABLE'
;
```

Replace `<pulumi-org>` with your Pulumi organization name.

### Step 2: Create a User in Snowflake for ESC Login

Create a Snowflake user that will be used by ESC:

```sql
CREATE USER ESC_LOGIN_USER
  DEFAULT_ROLE = '<role>'
  TYPE = SERVICE;

-- Grant necessary permissions to the user
GRANT ROLE <role> TO USER ESC_LOGIN_USER;
```

Replace `<role>` with the role that has the necessary permissions for your use case.

## Using with Pulumi ESC

Once you've configured OIDC in Snowflake, you can use the `snowflake-login` provider in your Pulumi ESC environment:

```yaml
values:
  snowflake:
    login:
      fn::open::snowflake-login:
        oidc:
          account: myorganization-account
          user: ESC_LOGIN_USER
          role: ESC_ROLE  # Optional
```

### Validation

When opening the environment, you should see output similar to the following:

```json
{
  "snowflake": {
    "login": {
      "account": "myorganization-account",
      "user": "ESC_LOGIN_USER",
      "token": "[secret]"
    }
  }
}
```

You can validate your configuration is working by connecting to snowflake with using the minted oidc token:

```shell
> snowsql \
  --accountname <snowflake.login.account> \
  --username <snowflake.login.user> \
  --authenticator=oauth \
  --token=<snowflake.login.token>
```

## Inputs

| Property            | Type   | Description                                                                             |
|---------------------|--------|-----------------------------------------------------------------------------------------|
| `oidc.account`      | string | Required. Snowflake account identifier.                                                 |
| `oidc.user`         | string | Required. User login name.                                                              |
| `oidc.role`         | string | Optional. Role to assume. See [Snowflake OAuth Scopes](https://docs.snowflake.com/en/user-guide/oauth-ext-overview#scopes) for more information. |

## Outputs

| Property   | Type   | Description                              |
|------------|--------|------------------------------------------|
| `account`  | string | Snowflake account identifier.            |
| `user`     | string | User login name.                         |
| `token`    | string | OAuth token (stored as a secret).        |
