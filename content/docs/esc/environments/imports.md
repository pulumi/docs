---
title: Importing other environments
title_tag: Importing other environments | Pulumi ESC
h1: Importing other environments
meta_desc: Pulumi ESC allows you to import and compose configurations from multiple environments, reducing duplication and ensuring consistency.
menu:
  esc:
    name: Importing environments
    identifier: esc-importing-environments
    parent: esc-environments
    weight: 2
---

Environments can be composed from other environments.

Different applications are often configured in similar ways and with common values --- for example, an e-commerce site and order-management system both configured to use the same cloud account, database-connection string, and third-party API key. Managing the duplication of these values across multiple configuration files, however, can be difficult, especially when one of those values changes --- e.g., when an API key is regenerated.

To address these challenges, Pulumi ESC allows you to identify common or closely related configuration settings and define them only once, as individual environments, and then _import_ those environments into other, more specialized environments as needed. Imports also allow you to expose certain environments without having to distribute any concrete values and to delegate responsibility for particular environments to other teams in your organization. Environments can import both static and dynamic values, including secrets, from any number of other environments.

## Explicit imports

Explicit imports are defined in the `imports` section of an environment. The `imports` section is a list of environments that are resolved at runtime. The values from the imported environments are merged into the current environment using a [JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396), with the current values overwriting the imported environment's values where keys are redefined.

In the following example, two environments, `aws/dev` and `stripe/dev`, are used to compose a third environment, `myapp/dev`:

```yaml
# myorg/aws/dev
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
# myorg/stripe/dev
values:
  stripe:
    apiURL: https://api.stripe.com
    apiKey:
      fn::secret: sk_XemWAl12i4x3hZhp4vBKDEXAMPLE
```

The application-specific `myapp/dev` environment then `imports` these two environments and use their settings to compose new values:

```yaml
# myorg/myapp/dev
imports:
  - aws/dev
  - stripe/dev

values:
  greeting: Hello from the myapp/dev environment!

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    STRIPE_API_KEY: ${stripe.apiKey}
    STRIPE_API_URL: ${stripe.apiURL}
    GREETING: ${greeting}
```

Finally, `esc run` renders `myapp/dev`'s environment variables for use on the command line:

```bash
$ esc run myorg/myapp/dev -- bash -c 'echo $GREETING'
Hello from the dev environment!

$ esc run myorg/myapp/dev -- bash -c 'echo $STRIPE_API_URL'
https://api.stripe.com

$ esc run myorg/myapp/dev -- bash -c 'echo $STRIPE_API_KEY'
[secret]

$ esc run myorg/myapp/dev -- bash -c 'echo $AWS_SECRET_ACCESS_KEY'
[secret]

$ echo "'$GREETING'"
''
```

Notice in the example that the `environmentVariables` were exposed to the `bash` command, but not to the surrounding shell, and that the values marked as secrets with `fn::secret` were protected from exposure.

## Implicit imports

Implicit imports are used to reference values from other environments without having to explicitly import them. This is useful when you want to reference a value from another environment without needing to expose the entire environment.

Implicit imports take the form of a reference to the special `environments` key like `${environments.PROJECT.ENV.VALUEPATH}`.

In the following example, the `aws/dev` environment is implicitly imported into the `myapp/dev` environment:

```yaml
# myorg/aws/dev
values:
  aws:
    region: us-west-2
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789012:role/MyRole
          sessionName: pulumi-environments-session
```

```yaml
# myorg/myapp/dev
values:
  greeting: Hello from the myapp/dev environment!

  environmentVariables:
    AWS_REGION: ${environments.aws.dev.aws.region}
    GREETING: ${greeting}
```

In this example, the `AWS_REGION` value is implicitly imported from the `aws/dev` environment, but only the `region` value is imported, rather than the entire `aws/dev` environment.

The resolved value of the above environment at `open` time would be:

```json
{
  "greeting": "Hello from the myapp/dev environment!",
  "environmentVariables": {
    "AWS_REGION": "us-west-2",
    "GREETING": "Hello from the myapp/dev environment!"
  }
}
```

Compare this to the resolved value of the `myapp/dev` environment example from the explicit imports section, where each imported environment is merged into the current environment:

```json
{  
  "stripe": {
    "apiURL": "https://api.stripe.com",
    "apiKey": "sk_XemWAl12i4x3hZhp4vBKDEXAMPLE"
  },
  "aws": {
    "region": "us-west-2",
    "login": {
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
    }
  },
  "greeting": "Hello from the myapp/dev environment!",
  "environmentVariables": {
    "AWS_ACCESS_KEY_ID": "AKIAIOSFODNN7EXAMPLE",
    "AWS_SECRET_ACCESS_KEY": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE",
    "STRIPE_API_KEY": "sk_XemWAl12i4x3hZhp4vBKDEXAMPLE",
    "STRIPE_API_URL": "https://api.stripe.com",
    "GREETING": "Hello from the myapp/dev environment!"
  }
}
```

## Evaluation

Note that each distinct reference is evaluated exactly once. Consider the following case:

```yaml
imports:
  - default/foo
values:
  a: ${environments.default.foo.bar}
```

In the environment definition above, `default/foo` is evaluated only once.
