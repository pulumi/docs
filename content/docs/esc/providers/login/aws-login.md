---
title_tag: aws-login Pulumi ESC Provider
meta_desc: The aws-login Pulumi ESC Provider enables you to log in to AWS using OIDC or static credentials.
title: aws-login
h1: aws-login
menu:
  esc:
    identifier: aws-login
    parent: esc-providers-login
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/aws-login/
    - /docs/esc/providers/aws-login/
    - /docs/esc/integrations/dynamic-login-credentials/aws-login/
    - /docs/esc/concepts/providers/login/aws-login/
---

The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access AWS resources or fetch secrets using the `aws-secrets` provider.

## Examples

### OIDC

OIDC is the recommended way to log in to AWS. Pulumi Cloud exchanges a short-lived OIDC token for temporary AWS credentials by assuming an IAM role, so there are no long-lived keys to store or rotate.

The `aws-login` provider's outputs can be consumed by the [Pulumi AWS provider](https://www.pulumi.com/registry/packages/aws/), the `aws` CLI, and the AWS SDKs. Because all three read the same standard AWS environment variables, a single `environmentVariables` block covers all three:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::012345678912:role/role-abcd123
          sessionName: pulumi-esc
  environmentVariables:
    # Credentials consumed by the aws CLI, the AWS SDKs, and the Pulumi AWS provider
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    # Sets the region for the aws CLI, the AWS SDKs, and the Pulumi AWS provider
    AWS_REGION: us-west-2
```

### Static credentials

The `static` input lets you supply existing AWS credentials — an IAM user's access key, or temporary credentials from another source — instead of having ESC generate them through OIDC. Whichever method you use, `aws-login` normalizes the result into one uniform set of outputs (`accessKeyId`, `secretAccessKey`, `sessionToken`). Everything downstream — `environmentVariables`, the `aws-secrets` provider, and the `aws-parameter-store` provider — consumes those outputs the same way regardless of how you logged in. That means you can use static credentials for local development and OIDC for production, or migrate from one to the other, without changing a single consumer.

Store the credentials as encrypted ESC secrets rather than committing them in plaintext. You can encrypt a value in place with `pulumi env set --secret <org>/<project>/<environment> aws.creds.secretAccessKey <value>`, or wrap a literal with the `fn::secret` function as shown below:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        static:
          accessKeyId: AKIAIOSFODNN7EXAMPLE
          secretAccessKey:
            fn::secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_REGION: us-west-2
```

{{< notes type="warning" >}}
Prefer OIDC wherever it is available. Static credentials are long-lived secrets that must be rotated manually and increase the blast radius if leaked; OIDC issues short-lived credentials on demand and requires no stored keys.
{{< /notes >}}

### Scoping down a session

You can narrow what an assumed session is allowed to do with two optional `oidc` inputs:

- `subjectAttributes` customizes the OIDC token's subject (`sub`) claim — for example, to encode the specific environment or user into the claim so your IAM role's trust policy can restrict which environments may assume it. See [OpenID subject customization](/docs/esc/guides/configuring-oidc/#custom-token-claim).
- `policyArns` attaches additional managed policies to the session. The effective permissions are the *intersection* of the role's permissions and these policies, so this is a convenient way to grant a session strictly less than the role allows.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::012345678912:role/role-abcd123
          sessionName: pulumi-esc
          subjectAttributes:
            - currentEnvironment.name
          policyArns:
            - arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

## Consuming the credentials

Because the `aws-secrets` and `aws-parameter-store` providers accept an `aws-login` output as their `login` input, you can log in once and chain the credentials into other providers with `login: ${aws.login}`.

As a best practice, define `aws-login` once in its own environment and [import](/docs/esc/concepts/imports/) it wherever credentials are needed, rather than repeating the login block in every environment. This keeps the OIDC configuration in a single place and means the role and trust policy only have to grant access to the one base environment.

Define the login in a base environment:

```yaml
# myorg/aws/login
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::012345678912:role/role-abcd123
          sessionName: pulumi-esc
```

Then import it into an application environment that consumes the credentials:

```yaml
# myorg/myapp/dev
imports:
  - aws/login

values:
  aws:
    secrets:
      fn::open::aws-secrets:
        region: us-west-2
        login: ${aws.login}
        get:
          api-key:
            secretId: api-key
```

The same `login: ${aws.login}` pattern works for the [`aws-parameter-store`](/docs/esc/providers/aws-parameter-store/) provider. For the full set of options each provider accepts, see the [`aws-secrets`](/docs/esc/providers/aws-secrets/) and [`aws-parameter-store`](/docs/esc/providers/aws-parameter-store/) documentation.

To validate your configuration, open the consuming environment with the `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/iac/cli/commands/pulumi_env_open/):

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
{
  "aws": {
    "login": {
      "accessKeyId": "ASIA....",
      "secretAccessKey": "mWdm....",
      "sessionToken": "Fwo...."
    },
    "secrets": {
      "api-key": "my-api-key"
    }
  }
}
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/aws/) documentation.

## Troubleshooting

Most `aws-login` failures come from the OIDC trust relationship between Pulumi Cloud and AWS. For full setup steps, see [Configuring OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/).

### Not authorized to perform sts:AssumeRoleWithWebIdentity

**Symptom:** opening the environment fails with an `AccessDenied` error referencing `sts:AssumeRoleWithWebIdentity`.

**Cause:** the IAM role's trust policy doesn't allow Pulumi Cloud's OIDC provider to assume it.

**Fix:** confirm the role's trust policy lists the federated principal `arn:aws:iam::<account-id>:oidc-provider/api.pulumi.com/oidc` and the action `sts:AssumeRoleWithWebIdentity`. See [Configuring OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/) for the complete trust policy.

### Audience or subject mismatch

**Symptom:** the assume-role call is rejected even though the role exists and the OIDC provider is configured.

**Cause:** the `aud` or `sub` claim Pulumi sends doesn't satisfy the trust policy's `StringEquals` / `StringLike` conditions — often a wrong organization name, or a `subjectAttributes` change that altered the subject format.

**Fix:** confirm the `aud` condition equals `aws:<your-pulumi-org>` (for the legacy `default` project, just `<your-pulumi-org>`), and that the `sub` condition matches your environment. If you customize the subject with `subjectAttributes`, update the `sub` condition to match — see [OpenID subject customization](/docs/esc/guides/configuring-oidc/#custom-token-claim).

### DurationSeconds exceeds the MaxSessionDuration set for this role

**Symptom:** login fails when `duration` is set above one hour.

**Cause:** an IAM role's maximum session duration defaults to one hour, and the requested session `duration` can't exceed it.

**Fix:** raise the role's **Maximum session duration** in the IAM console (up to 12 hours), or lower the `duration` input to fit within it.

## Inputs

| Property | Type                              | Description                                                       |
|----------|-----------------------------------|-------------------------------------------------------------------|
| `oidc`   | [AWSLoginOIDC](#awsloginoidc)     | [Optional] - OIDC configuration to log in to AWS.                 |
| `static` | [AWSLoginStatic](#awsloginstatic) | [Optional] - A static set of credentials to use to log in to AWS. |

### AWSLoginOIDC

| Property      | Type     | Description                                                                                                                                                                                                  |
|---------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `roleArn`     | string   | The ARN of the role to assume.                                                                                                                                                                              |
| `sessionName` | string   | The name of the role session.                                                                                                                                                                              |
| `duration`    | string   | [Optional] - The duration of the role session. Defaults to 2 hours. Can't exceed the role's maximum session duration (1 hour by default). See [Troubleshooting](#durationseconds-exceeds-the-maxsessionduration-set-for-this-role). |
| `policyArns`  | string[] | [Optional] - ARNs for additional policies to apply to the role session.                                                                                                                                     |
| `subjectAttributes`  | string[] | [Optional] - Subject attributes to be included in the OIDC token. For more information see the [OpenID subject customization](/docs/esc/guides/configuring-oidc/#custom-token-claim) documentation |

### AWSLoginStatic

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

## Outputs

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |
