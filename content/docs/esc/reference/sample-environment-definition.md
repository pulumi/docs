---
title: Sample Environment Definition
title_tag: Sample Environment Definition
h1: Sample Environment Definition
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-sample-environment-definition
    weight: 8
---

```yaml
# ---------------------------------------------------------------------------------------
# Imports section names the environments to import. Environments are merged in order
# per JSON merge patch.
# ---------------------------------------------------------------------------------------

# imports is an optional top-level key
imports:
  - project/environment-a
  - project/environment-b

# ---------------------------------------------------------------------------------------
# Main configuration -- set configuration values either as static values, or interpolated
# from other sources. Values are merged onto imported environments per JSON merge patch.
# ---------------------------------------------------------------------------------------

# values is a required top-level key
values:

  # Values can be objects, arrays, strings, numbers, or booleans
  # References to this value will use the path excluding the
  # top-level "values" key

  # Path is "app"
  app:
    # Path is "app.setting"
    setting: example

    # Path is "app.replicas"
    replicas: 3

    # Path is "app.enabled"
    enabled: true

    # Path is "app.nested"
    nested:
      # Path is "app.nested.setting"
      setting: nested-example

    # Path is "app.items"
    # Array elements are "app.items[0]" and "app.items[1]"
    items: [ "config-a", "config-b" ]

    # Path is "app.multiline"
    # If the value needs to be a multiline value, use YAML pipe.
    multilineValue: |
      The quick brown fox
      jumped over the lazy dog

    # Values within the environment and its imports may be referenced
    # Path is "app.settingCopy"
    settingCopy: ${app.setting}

    # Values can interpolate contextual information
    rootEnvName: ${context.rootEnvironment.name}
    currentEnvName: ${context.currentEnvironment.name}
    currentUser: ${context.pulumi.user.login}
    currentOrg: ${context.pulumi.organization.login}

    # ---------------------------------------------------------------------------------------
    # Functions -- configuration may be transformed with the following functions
    # ---------------------------------------------------------------------------------------

    # Scalar values may be marked secret. The value will be encrypted and
    # stored as ciphertext when the environment is saved.
    # Path is "app.password"
    password:
      fn::secret: YQ!r24kdF7

    # Multiline private key stored as a secret using YAML multiline pipe.
    # The value will be encrypted and
    # stored as ciphertext when the environment is saved.
    # Path is "app.sshKey"
    sshKey:
      fn::secret: |
        -----BEGIN OPENSSH PRIVATE KEY-----
        blahblahblahblahblahblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        dfdsafdsadfsadsfadshblahblabhablhablahkldfldsfjdlsfdlfjdslfjlladsklfll
        -----END OPENSSH PRIVATE KEY-----

    # Join array elements with the given delimiter
    # Path is "app.url"
    url:
      fn::join: [ ", ", "${app.items}" ]

    # Encode the argument as a Base64 string
    # Path is "app.passwordB64"
    passwordB64:
      fn::toBase64: ${app.password}

    # Decodes a base64-encoded string
    # Path is "app.plainString"
    plainString:
      fn::fromBase64: ${app.passwordB64}

    # Encode the argument as a JSON string
    # Path is "app.jsonConfig"
    jsonConfig:
      fn::toJSON: ${app.nested}

    # Decode the JSON string as a JSON Object
    # Path is "app.jsonConfigObject"
    jsonConfigObject:
      fn::fromJSON: ${app.jsonConfig}

    # Encode the argument as a string
    # Path is "app.strConfig"
    strConfig:
      fn::toString: ${app.nested}

  # ---------------------------------------------------------------------------------------
  # Dynamic configuration from providers -- configuration may be loaded from external
  # sources using a variety of providers. This configuration will be loaded when the
  # environment is opened.
  # ---------------------------------------------------------------------------------------

  # 1Password Provider examples
  1password:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken:
            fn::secret: "ops_123ABC"
        get:
          email_section_example:
            ref: "op://Management/PagerDuty/Admin/email"
          anna_sans_section_example:
            ref: "op://dev/Stripe/publishable-key"
          olaf_attr_example:
            ref: "op://development/GitHub/Security/one-time password?attribute=otp"
          sven_ssh_example:
            ref: "op://Private/ssh keys/ssh key/private key?ssh-format=openssh"
          nokk_whitespace_example:
            ref: "op://development/aws/Access Keys/access_key_id"
          gale_unique_id_example:
            ref: "op://prod/yj3jfj2vzsbiwqabprflnl27lm/password"

  # AWS Provider examples
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::086028354146:role/pulumi-deployments-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            secretId: api-key
          app-secret:
            secretId: app-secret

  # Azure Provider examples
  azure:
    login:
      fn::open::azure-login:
        clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
        oidc: true
    secrets:
      fn::open::azure-secrets:
        login: ${azure.login}
        vault: example-vault-name
        get:
          api-key:
            name: api-key
          app-secret:
            name: app-secret

  # GCP Provider examples
  gcp:
    login:
      fn::open::gcp-login:
        project: 123456789
        oidc:
          workloadPoolId: pulumi-esc
          providerId: pulumi-esc
          serviceAccount: pulumi-esc@foo-bar-123456.iam.gserviceaccount.com
    secrets:
      fn::open::gcp-secrets:
        login: ${gcp.login}
        access:
          api-key:
            name: api-key
          app-secret:
            name: app-secret

  # Vault Provider examples
  vault:
    login:
      fn::open::vault-login:
        address: https://127.0.0.1:8200/
        jwt:
          role: example-role
        namespace: example # namespace is only supported for Vault Enterprise
    secrets:
      fn::open::vault-secrets:
        login: ${vault.login}
        read:
          api-key:
            path: api-key
          app-secret:
            path: app-secret
            field: app-field

  # Pulumi Stacks Provider example
  app:
    fn::open::pulumi-stacks:
      stacks:
        k8-cluster:
          stack: k8-cluster-1/dev
  kubeconfig:
    # The referenced stack has a stack output named "kconfig"
    fn::toJSON: ${app.k8-cluster.kconfig}

  # ---------------------------------------------------------------------------------------
  # Exports -- expose configuration values to particular consumers
  # ---------------------------------------------------------------------------------------

  # Configuration nested under the "environmentVariables" key is used to export environment
  # variables when using `esc open --format=shell`, `esc run`, or `pulumi up/preview/refresh/destroy`
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}

  # Configuration nested under the "pulumiConfig" key will be available to Pulumi stacks that
  # reference this environment during `pulumi up/preview/refresh/destroy`
  pulumiConfig:
    aws:region: us-west-2

  # Configuration nested under the 'files' key is used to export as files to the environment
  # when using 'esc open --format=shell', 'esc run', or `pulumi up/preview/refresh/destroy`
  files:
    KUBECONFIG: ${kubeconfig}
```
