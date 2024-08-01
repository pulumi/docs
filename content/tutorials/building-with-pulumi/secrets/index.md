---
title_tag: Working with Secrets | Learn Pulumi
title: "Working with Secrets"
layout: topic
date: 2021-09-20T08:33:36-05:00
draft: false
description: Explore how Pulumi handles secrets across all environments.
meta_desc: Learn how secrets work within Pulumi and how to access secrets with this tutorial.
index: 4
estimated_time: 10
meta_image: meta.png
aliases:
    - /learn/building-with-pulumi/secrets/
---

All resource input and output values are recorded as _state_ and are stored in Pulumi Cloud, a file, or a pluggable provider that you choose. These raw values are usually just server names, configuration settings, and so on. In some cases, however, these values contain sensitive data, such as database passwords or service tokens.

Pulumi Cloud always transmits and stores entire state files securely; however, Pulumi also supports encrypting specific values as "secrets" for extra protection. Encryption ensures that these values never appear as plain-text in your state file. By default, the encryption method uses automatic, per-stack encryption keys provided by Pulumi Cloud or you can use a [provider of your own choosing](/docs/concepts/secrets#configuring-secrets-encryption)
instead.

To encrypt a configuration setting before runtime, use the CLI command `pulumi config set` with the `--secret` option. All encrypted values are stored as ciphertext in configuration and state files.

Back inside the `my-first-app` project, make sure the `staging` is selected and set a username and password for MongoDB:

```bash
$ pulumi stack select staging

$ pulumi config set mongoUsername admin
$ pulumi config set --secret mongoPassword S3cr37
```

Now try listing the configuration for the stack as before, and notice, the value for `mongoPassword` is hidden:

```bash
$ pulumi config

KEY               VALUE
backendPort      3000
database         cart
frontendPort     3002
mongoHost        mongodb://mongo:27017
mongoPassword    [secret]
mongoPort        27017
mongoUsername    admin
nodeEnvironment  development
protocol         http://
```

Notice the password value is also encrypted in the stack configuration file:

```bash
$ cat Pulumi.staging.yaml

config:
  my-first-app:backendPort: "3000"
  my-first-app:database: cart
  my-first-app:frontendPort: "3002"
  my-first-app:mongoHost: mongodb://mongo:27017
  my-first-app:mongoPassword:
    secure: AAABANASX3meu/8efB9H4oSyXrr/4GPYxfxsomW1NQbIoKU+xSY=
  my-first-app:mongoPort: "27017"
  my-first-app:mongoUsername: admin
  my-first-app:nodeEnvironment: development
  my-first-app:protocol: http://
```

Secrets can be accessed in code using secret-specific helper functions. Modify the code in {{< langfile >}} in `my-first-app` to add the following lines:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
const config = new pulumi.Config();
// ...

const mongoUsername = config.require("mongoUsername");
const mongoPassword = config.requireSecret("mongoPassword");
```

{{% /choosable %}}

{{% choosable language python %}}

```python

config = pulumi.Config()
#...

mongo_username = config.require("mongoUsername")
mongo_password = config.require_secret("mongoPassword")
```

{{% /choosable %}}

We need to make a few changes to use this new username and password. First,
let's go ahead and make sure when our `mongo` container is created, it has the
correct username and password. Update the container definition to use the `envs`
input property to set environment variables for the database username and password:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
const mongoContainer = new docker.Container("mongoContainer", {
    image: mongoImage.repoDigest,
    name: `mongo-${stack}`,
    ports: [
        {
            internal: mongoPort,
            external: mongoPort,
        },
    ],
    networksAdvanced: [
        {
            name: network.name,
            aliases: ["mongo"],
        },
    ],
    envs: [
        `MONGO_INITDB_ROOT_USERNAME=${mongoUsername}`,
        pulumi.interpolate`MONGO_INITDB_ROOT_PASSWORD=${mongoPassword}`,
    ],
});
```

Then, we need to update the backend container to use the new authentication. We need to slightly change the value of `mongoHost` first:

```bash
$ pulumi config set mongoHost mongo
```

{{% /choosable %}}

{{% choosable language python %}}

```python
mongo_container = docker.Container(
    "mongo_container",
    image=mongo_image.repo_digest,
    name=f"mongo-{stack}",
    ports=[docker.ContainerPortArgs(internal=mongo_port, external=mongo_port)],
    networks_advanced=[
        docker.ContainerNetworksAdvancedArgs(name=network.name, aliases=["mongo"])
    ],
    envs=[
        f"MONGO_INITDB_ROOT_USERNAME={mongo_username}",
        mongo_password.apply(lambda password: f"MONGO_INITDB_ROOT_PASSWORD={password}"),
    ],
)
```

Then, we need to update the backend container to use the new authentication. We need to slightly change the value of `mongo_host` first:

```bash
$ pulumi config set mongoHost mongo
```

{{% /choosable %}}

Then, update the backend container resource as follows:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
const backendContainer = new docker.Container("backendContainer", {
    name: `backend-${stack}`,
    image: backend.repoDigest,
    ports: [
        {
            internal: backendPort,
            external: backendPort,
        },
    ],
    envs: [
        pulumi.interpolate`DATABASE_HOST=mongodb://${mongoUsername}:${mongoPassword}@${mongoHost}:${mongoPort}`,
        `DATABASE_NAME=${database}?authSource=admin`,
        `NODE_ENV=${nodeEnvironment}`,
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
}, { dependsOn: [ mongoContainer ]});
```

And finally, add a line at the end of the program to export password as a stack output:

```typescript
// ...
export { mongoPassword };
```

{{% /choosable %}}

{{% choosable language python %}}

```python
backend_container = docker.Container(
    "backend_container",
    image=backend.repo_digest,
    name=f"backend-{stack}",
    ports=[docker.ContainerPortArgs(internal=backend_port, external=backend_port)],
    envs=[
        pulumi.Output.concat(
            "DATABASE_HOST=mongodb://",
            mongo_username,
            ":",
            mongo_password,
            "@",
            mongo_host,
            ":",
            f"{mongo_port}",
        ),  # Changed!
        f"DATABASE_NAME={database}?authSource=admin",  # Also changed!
        f"NODE_ENV={node_environment}",
    ],
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
    opts=pulumi.ResourceOptions(depends_on=[mongo_container]),
)
```

And finally, add a line at the end of the program to export password as a stack output:

```python
#...
pulumi.export("mongoPassword", mongo_password)
```

{{% /choosable %}}

Run `pulumi up` again and notice that while the `mongoPassword` output has been registered, it's hidden from view because Pulumi is now tracking it as an encrypted secret:

```
Outputs:
  + mongoPassword: [secret]
    url          : "http://localhost:3002"
```

To get at the underlying plain-text value, you'll need to pass the `--show-secrets` option:

{{% choosable language typescript %}}

```bash
$ pulumi stack output mongoPassword --show-secrets
S3cr37
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi stack output mongoPassword --show-secrets
S3cr37
```

{{% /choosable %}}

To learn more about Pulumi secrets, see the [secrets documentation](/docs/concepts/secrets/).

---

Congratulations! You’ve finished the Building with Pulumi tutorial. In this tutorial, you learned all about stacks, outputs, and stack references so you can work in multiple environments. You also learned about encrypted secrets and how to use them in your programs.

Go build new things, and watch this space for more learning experiences on Pulumi!

{{< tutorials/stepper >}}
