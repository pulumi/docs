---
title: aws-secrets
title_tag: aws-secrets Pulumi ESC Provider
meta_desc: The aws-secrets Pulumi ESC Provider enables you to dynamically import Secrets from AWS Secrets Manager.
h1: aws-secrets
menu:
  esc:
    identifier: aws-secrets
    parent: esc-providers-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/aws-secrets/
    - /docs/esc/providers/aws-secrets/
    - /docs/esc/integrations/dynamic-secrets/aws-secrets/
    - /docs/esc/concepts/providers/secrets/aws-secrets/
---

The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment. The provider will return a map of names to Secrets.

The `login` input is an inline [`aws-login`](/docs/esc/providers/login/aws-login/) provider block. The examples below use OIDC, the recommended login method, but `aws-login` also accepts static credentials. See the [`aws-login`](/docs/esc/providers/login/aws-login/) documentation for the full set of login options and for the best practice of defining the login once in a base environment and [importing](/docs/esc/concepts/imports/) it wherever credentials are needed.

## Examples

### Plain-text secrets

The following example demonstrates how to retrieve plain-text (i.e., scalar value) secrets from AWS Secrets Manager:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            # Secret name as shown in the AWS Console, or secret ARN:
            secretId: api-key
          app-secret:
            secretId: app-secret
  pulumiConfig:
    apiKey: ${aws.secrets.api-key}
    appSecret: ${aws.secrets.app-secret}
```

### Key/value pair secrets

The following example demonstrates how to retrieve key/value pair (i.e. JSON) secrets from AWS Secrets Manager and map them to Pulumi IaC configuration values:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          db-creds:
            secretId: prod-db
    secrets-unpacked:
      db-creds:
        fn::fromJSON: ${aws.secrets.db-creds}
  pulumiConfig:
    dbUserName: ${aws.secrets-unpacked.db-creds.userName}
    dbPassword: ${aws.secrets-unpacked.db-creds.password}
```

### Pinning a secret version

By default `aws-secrets` returns the current version of each secret (the `AWSCURRENT` staging label). Use `versionId` to pin to a specific immutable version, or `versionStage` to select by staging label — for example, `AWSPREVIOUS` to read the value from before the most recent rotation:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          # Pin to a specific immutable version by ID:
          api-key-pinned:
            secretId: api-key
            versionId: 01234567-89ab-cdef-0123-456789abcdef
          # Select by staging label (AWSCURRENT is the default):
          api-key-previous:
            secretId: api-key
            versionStage: AWSPREVIOUS
  pulumiConfig:
    apiKey: ${aws.secrets.api-key-pinned}
```

### Using static credentials

When OIDC isn't available, supply existing AWS credentials through the login block's `static` input instead. Store them as encrypted ESC secrets rather than committing them in plaintext, and prefer OIDC wherever possible — see the [`aws-login`](/docs/esc/providers/login/aws-login/#static-credentials) documentation for the full guidance:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        static:
          accessKeyId: AKIAIOSFODNN7EXAMPLE
          secretAccessKey:
            fn::secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            secretId: api-key
  pulumiConfig:
    apiKey: ${aws.secrets.api-key}
```

## Required IAM permissions

The identity that `aws-secrets` logs in as — the assumed OIDC role or the static credentials — must be allowed to read each secret referenced in `get`:

- `secretsmanager:GetSecretValue` on the secret's ARN.
- `kms:Decrypt` on the encryption key, if the secret is encrypted with a customer managed KMS key (CMK). Secrets encrypted with the default AWS managed key (`aws/secretsmanager`) don't require an explicit `kms:Decrypt` grant.

A minimal policy looks like this. Secrets Manager appends a random six-character suffix to each secret's ARN, so the wildcard on the resource matches the secret regardless of that suffix:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-west-1:123456789012:secret:api-key-*"
    },
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-west-1:123456789012:key/<key-id>"
    }
  ]
}
```

{{< notes type="info" >}}
For better security, log in with a dedicated role whose only job is retrieving secrets, rather than reusing a broad role that also has permissions to manage your AWS resources. Scope the role's trust policy to the specific environment that reads the secrets, and attach only the `secretsmanager:GetSecretValue` (and any `kms:Decrypt`) permissions shown above. A separate, narrowly scoped role keeps the blast radius small if the environment is misused, and lets you grant and audit secret access independently of your infrastructure-provisioning roles. You can point `aws-secrets` at this role by giving it its own `aws-login` block with a different `roleArn` than the one your provisioning environments use.
{{< /notes >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, and to validate that your configuration is working, see [Configuring OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/).

{{< notes type="info" >}}
Rather than repeating the `login` block in every environment, define it once in a base environment and [import](/docs/esc/concepts/imports/) it wherever you read secrets. This keeps the OIDC configuration in a single place and means the role and its trust policy only have to grant access to that one base environment.

```yaml
# myorg/aws/login
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
```

```yaml
# myorg/myapp/dev
imports:
  - aws/login

values:
  aws:
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            secretId: api-key
```

{{< /notes >}}

## Troubleshooting

Login failures (assume-role errors, audience or subject mismatches) are covered in the [`aws-login` troubleshooting](/docs/esc/providers/login/aws-login/#troubleshooting) section. The errors below are specific to reading secrets once login succeeds.

### AccessDeniedException on secretsmanager:GetSecretValue

**Symptom:** opening the environment fails with an `AccessDenied` error referencing `secretsmanager:GetSecretValue`.

**Cause:** the logged-in identity isn't allowed to read the secret.

**Fix:** grant `secretsmanager:GetSecretValue` on the secret's ARN to the assumed role or static credentials. See [Required IAM permissions](#required-iam-permissions).

### ResourceNotFoundException / secret not found

**Symptom:** the open fails with `ResourceNotFoundException` or a message that Secrets Manager can't find the specified secret.

**Cause:** the `secretId` doesn't match an existing secret, or the secret lives in a different region than the one set in `region`.

**Fix:** confirm `secretId` matches the secret's name or full ARN exactly, and that `region` is the region the secret is stored in. A pinned `versionId` or `versionStage` that doesn't exist produces the same error — verify the version is still present.

### AccessDeniedException on kms:Decrypt

**Symptom:** an `AccessDenied` error referencing `kms:Decrypt` when reading a secret encrypted with a customer managed key.

**Cause:** the identity can call `GetSecretValue` but isn't allowed to decrypt with the secret's KMS key.

**Fix:** add `kms:Decrypt` for the key to the identity's IAM policy, and make sure the KMS key policy also permits that principal. See [Required IAM permissions](#required-iam-permissions).

## Inputs

| Property | Type                                       | Description                                                                                                                  |
|----------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `region` | string                                     | The AWS region to use.                                                                                                       |
| `login`  | [AWSSecretsLogin](#awssecretslogin)        | Credentials to use to log in to AWS.                                                                                         |
| `get`    | map[string][AWSSecretsGet](#awssecretsget) | A map from names to secrets to read from AWS Secrets Manager. The outputs will map each name to the secret's sensitive data. |

### AWSSecretsLogin

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

### AWSSecretsGet

| Property       | Type   | Description                                             |
|----------------|--------|---------------------------------------------------------|
| `secretId`     | string | The ID of the secret to import.                         |
| `versionId`    | string | [Optional] - The version of the secret to import.       |
| `versionStage` | string | [Optional] - The version stage of the secret to import. |

## Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |
