---
title: Importing other environments
title_tag: Importing other environments | Pulumi ESC
h1: Importing other environments
meta_desc: Pulumi ESC allows you to import and compose configurations from multiple environments, reducing duplication and ensuring consistency.
menu:
  pulumiesc:
    identifier: esc-importing-environments
    weight: 6
---

Environments can also be composed from other environments.

Different applications are often configured in similar ways and with common values --- for example, an e-commerce site and order-management system both configured to use the same cloud account, database-connection string, and third-party API key. Managing the duplication of these values across multiple configuration files, however, can be difficult, especially when one of those values changes --- e.g., when an API key is regenerated.

To address these challenges, Pulumi ESC allows you to identify common or closely related configuration settings and define them only once, as individual environments, and then _import_ those environments into other, more specialized environments as needed. Imports also allow you to expose certain environments without having to distribute any concrete values and to delegate responsibility for particular environments to other teams in your organization. Environments can import both static and dynamic values, including secrets, from any number of other environments.

In the following example, two environments, `aws-dev` and `stripe-dev`, are used to compose a third environment, `myapp-dev`:

```yaml
# myorg/aws-dev
values:
  aws:
    region: us-west-2
    login:
      fn::open::aws-login:
        static:
          accessKeyId:
            fn::secret: AKIAIOSFODNN7EXAMPLE
          secretAccessKey:
            fn::secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE
```

```yaml
# myorg/stripe-dev
values:
  stripe:
    apiURL: https://api.stripe.com
    apiKey:
      fn::secret: sk_XemWAl12i4x3hZhp4vBKDEXAMPLE
```

The application-specific `myapp-dev` environment then `imports` these two environments and use their settings to compose new values:

```yaml
# myorg/myapp-dev
imports:
  - aws-dev
  - stripe-dev

values:
  greeting: Hello from the dev environment!

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    STRIPE_API_KEY: ${stripe.apiKey}
    STRIPE_API_URL: ${stripe.apiURL}
    GREETING: ${greeting}
```

Finally, `esc run` renders `myapp-dev`'s environment variables for use on the command line:

```bash
$ esc run myorg/myapp-dev -- bash -c 'echo $GREETING'
Hello from the dev environment!

$ esc run myorg/myapp-dev -- bash -c 'echo $STRIPE_API_URL'
https://api.stripe.com

$ esc run myorg/myapp-dev -- bash -c 'echo $STRIPE_API_KEY'
[secret]

$ esc run myorg/myapp-dev -- bash -c 'echo $AWS_SECRET_ACCESS_KEY'
[secret]

$ echo "'$GREETING'"
''
```

Notice in the example that the `environmentVariables` were exposed to the `bash` command, but not to the surrounding shell, and that the values marked as secrets with `fn::secret` were protected from exposure.
