---
title: Imports
title_tag: Importing other environments | Pulumi ESC
h1: Importing other environments
meta_desc: Pulumi ESC allows you to import and compose configurations from multiple environments, reducing duplication and ensuring consistency.
menu:
  esc:
    identifier: esc-importing-environments
    parent: esc-concepts
    weight: 5
aliases:
  - /docs/esc/environments/imports/
  - /docs/esc/environments/importing-environments/
  - /docs/esc/get-started/import-environments/
  - /docs/pulumi-cloud/esc/get-started/import-environments/
  - /docs/esc/guides/importing-environments/
  - /docs/esc/environments/syntax/top-level-keys/imports/
  - /docs/reference/esc-syntax/top-level-keys/imports/
  - /docs/esc/reference/top-level-keys/imports/
---

Pulumi ESC allows you to compose environments by importing configuration and secrets from other environments. This reduces duplication, ensures consistency, and enables you to organize configuration hierarchically. You can import both static and dynamic values, including secrets, from any number of other environments.

Imports support two modes: **explicit imports** that merge entire environments, and **implicit imports** that reference specific values without exposing the full environment structure.

| Feature | Explicit imports | Implicit imports |
|---------|-----------------|------------------|
| **Syntax** | `imports: [project/env]` | `${environments.project.env.path}` |
| **Scope** | Imports entire environment | Imports specific value only |
| **Merge behavior** | Full JSON Merge Patch | No merging |
| **Resolved output** | All imported values visible | Only referenced values visible |
| **Use case** | Share common configuration across environments | Selectively reference values without exposing full structure |

## Explicit imports

Explicit imports are defined in the `imports` top-level key of an environment. The `imports` key is a list of environments that are resolved at runtime. The values from the imported environments are merged into the current environment using a [JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396), with the current values overwriting the imported environment's values where keys are redefined.

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
Hello from the myapp/dev environment!

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

### Environment names

Each entry in the `imports` list names an environment to import. Environment names should be qualified with a project (e.g. `my-project/dev`). If no project name is given, the default project is assumed (e.g. the unqualified name `foo` refers to `default/foo`):

```yaml
imports:
  - auth-core          # Imports the "auth-core" environment in the "default" project
  - network-infra/dev  # Imports the "dev" environment in the "network-infra" project
```

### Import options

To control the behavior of an import, specify an object with options instead of a plain string:

```yaml
imports:
  - auth-core: { merge: false } # Import "default/auth-core", but don't add it to the merge stack
```

#### Available options

| Option  | Type    | Default | Description |
|---------|---------|---------|-------------|
| `merge` | boolean | `true`  | Whether to add the imported environment to the merge stack. When `false`, the environment is evaluated but its values are not automatically merged into the current environment. Unmerged imports are still accessible via the [`imports` built-in property](/docs/esc/concepts/interpolations-and-references/#imports). |

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

## Precedence rules

When multiple environment sources are combined and settings overlap, values are applied successively in the order in which they're imported and defined.

For example, in the following scenario, three environments define a key `foo`, each with a different value. The third environment, `project/environment-c`, imports `project/environment-a` and `project/environment-b` (importantly, in that order):

```yaml
# project/environment-a
values:
  foo: bar
```

```yaml
# project/environment-b
imports:
  - project/environment-a
values:
  foo: baz
  pulumiConfig:
    foo: ${foo}
```

```yaml
# project/environment-c
imports:
  - project/environment-a
  - project/environment-b
values:
  foo: qux
  pulumiConfig:
    foo: ${foo}
```

Notice how the value of `foo` is overwritten with each successive environment:

```bash
$ esc env open project/environment-a foo
"bar"

$ esc env open project/environment-b foo
"baz"

$ esc env open project/environment-c foo
"qux"
```

Also notice that when the local definition of `foo` is removed from `project/environment-c` and its imports are reordered, the value of `foo` changes to reflect the value inherited from `project/environment-a` --- i.e., the last-imported one:

```yaml
# project/environment-c
imports:
  - project/environment-b
  - project/environment-a
values:
  pulumiConfig:
    foo: ${foo}
```

```bash
$ esc env open project/environment-c foo
"bar"
```

To unset a value inherited from another environment, overwrite it with `null`.
