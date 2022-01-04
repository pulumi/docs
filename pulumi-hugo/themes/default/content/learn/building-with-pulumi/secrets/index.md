---
title: "Working with Secrets"
layout: topic
date: 2021-09-20T08:33:36-05:00
draft: false
description: Explore how Pulumi handles secrets across all environments.
meta_desc: Explore how Pulumi handles secrets across all environments.
index: 4
estimated_time: 10
meta_image: meta.png
authors:
    - matt-stratton
tags:
    - secrets
block_external_search_index: false
---

All resource input and output values are recorded as _state_ and are stored
in the Pulumi Service, a file, or a pluggable provider that you choose. These
raw values are usually just server names, configuration settings, and so on. In
some cases, however, these values contain sensitive data, such as database
passwords or service tokens.

The Pulumi Service always transmits and stores entire state files securely;
however, Pulumi also supports encrypting specific values as "secrets" for extra
protection. Encryption ensures that these values never appear as plain-text in
your state file. By default, the encryption method uses automatic, per-stack
encryption keys provided by the Pulumi Service or you can use a
[provider of your own
choosing]({{< relref "/docs/intro/concepts/secrets#configuring-secrets-encryption" >}})
instead.

To encrypt a configuration setting before runtime, you can use the CLI command
`pulumi config set` command with a `--secret` flag. All these encrypted values
are stored in your state file.

Inside our `my-first-app` program that we have been working with, let's set a
username and password for mongoDB:

```bash
$ pulumi config set mongo_username admin
$ pulumi config set --secret mongo_password S3cr37
```

If we list the configuration for our stack, the plain-text value for
`mongo-password` will not be printed:

```bash
$ pulumi config

KEY               VALUE
backend_port      3000
database          cart
frontend_port     3001
mongo_password    [secret]
mongo_username    admin
mongo_host        mongodb://mongo:27017
mongo_port        27017
node_environment  development
```

This is also encrypted in the associated configuration file:

```bash
$ cat Pulumi.dev.yaml

config:
  my-first-app:backend_port: "3000"
  my-first-app:database: cart
  my-first-app:frontend_port: "3001"
  my-first-app:mongo_password:
    secure: AAABADQXFlU0mxbTmNyl39UfVg4DdFoL94SCNMX3MkvZhBZjeAM=
  my-first-app:mongo_username: admin
  my-first-app:mongo_host: mongodb://mongo:27017
  my-first-app:mongo_port: "27017"
  my-first-app:node_environment: development


```

We can access the secrets similarly to other configuration data, however we must
specify that it is a secret:

Add this code to the {{% langfile %}} inside of `my-first-app`:

{{< chooser language "python" / >}}

{{% choosable language typescript %}}

```typescript
const config = new pulumi.Config();

const dbPassword = config.requireSecret("dbPassword");

export let password = dbPassword

```

{{% /choosable %}}

{{% choosable language python %}}

```python

config = pulumi.Config()

#...

mongo_username = config.require("mongo_username")
mongo_password = config.require_secret("mongo_password")

```

{{% /choosable %}}

We need to make a few changes to use this new username and password. First,
let's go ahead and make sure when our `mongo` container is created, it has the
correct username and password. Add the following environment variables to the
`mongo` container:

```python
                                   envs=[
                                         f"MONGO_INITDB_ROOT_USERNAME={mongo_username}",
                                        pulumi.Output.concat(
                                             "MONGO_INITDB_ROOT_PASSWORD=",
                                             config.require_secret("mongo_password")
                                         )
                                     ],
```

So the entire `docker.Container` resource will look like this:

```python

mongo_container = docker.Container("mongo_container",
                                   image=mongo_image.latest,
                                   name=f"mongo-{stack}",
                                   ports=[docker.ContainerPortArgs(
                                       internal=mongo_port,
                                       external=mongo_port
                                   )],
                                   envs=[
                                         f"MONGO_INITDB_ROOT_USERNAME={mongo_username}",
                                         pulumi.Output.concat(
                                             "MONGO_INITDB_ROOT_PASSWORD=",
                                             config.require_secret("mongo_password")
                                         )
                                     ],
                                   networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                       name=network.name,
                                       aliases=["mongo"]
                                   )]
                                   )


```

We need to have our seed container use the new password to connect. Change the
`command` in the `data_seed_container` resource to look like this:

```python
data_seed_container = docker.Container("data_seed_container",
                                       image=mongo_image.latest,
                                       name="data_seed",
                                       must_run=False,
                                       rm=True,
                                       opts=pulumi.ResourceOptions(depends_on=[backend_container]),
                                       mounts=[docker.ContainerMountArgs(
                                           target="/home/products.json",
                                           type="bind",
                                           source=f"{os.getcwd()}/products.json"
                                       )],
                                       command=[ # This is the changed part!
                                           "sh", "-c",
                                           pulumi.Output.concat(
                                               "mongoimport --host ",
                                               mongo_host,
                                               " -u ",
                                               mongo_username,
                                               " -p ",
                                               config.require_secret("mongo_password"),
                                               " --authenticationDatabase admin --db cart --collection products --type json --file /home/products.json --jsonArray"
                                           )
                                       ],
                                       networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                           name=network.name
                                       )]
                                       )
```

Finally, we need to update the backend container to use the new authentication.
We need to slightly change the value of `mongo_host` first:

```bash
pulumi config set mongo_host mongo
```

Then, update the `backend_container` resource as follows:

```python
backend_container = docker.Container("backend_container",
                                     image=backend.base_image_name,
                                     name=f"backend-{stack}",
                                     ports=[docker.ContainerPortArgs(
                                         internal=backend_port,
                                         external=backend_port
                                     )],
                                     envs=[
                                         Output.concat(
                                             "DATABASE_HOST=mongodb://",
                                             mongo_username,
                                             ":",
                                             config.require_secret("mongo_password"),
                                             "@",
                                             mongo_host,
                                             ":",
                                             f"{mongo_port}",
                                         ), #Changed!
                                         f"DATABASE_NAME={database}?authSource=admin", # Also changed!
                                         f"NODE_ENV={node_environment}"
                                     ],
                                     networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                         name=network.name
                                     )],
                                     opts=pulumi.ResourceOptions(depends_on=[mongo_container])
                                     )


```

<!-- {{% choosable language go %}}

```go

import (
  "fmt"

  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    dbPassword := c.RequireSecret("dbPassword")
    ctx.Export("x", pulumi.String(dbPassword))

    return nil
  }
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp

class AppStack : Stack
{
    public AppStack()
    {
        var config = new Config();

        var dbPassword = config.RequireSecret("dbPassword");
        this.dbPassword = Output.Create(dbPassword);
    }
}

```

{{% /choosable %}} -->

When we run `pulumi up`, we see that the output is set (so our use of the secret
worked!), but Pulumi knows that value was a secret, so when we try to set it as
an output, it will not display.

If we would like to see the plain-text value, we can do it with this command:

```bash
$ pulumi stack output mongo_password --show-secrets
S3cr37
```

For more information on how Pulumi uses secrets, including how to set them
programmatically, review the
[corresponding docs]({{< relref "/docs/intro/concepts/secrets" >}}).

From here, we're moving on to the last part of the Pulumi in Practice pathway:
testing. Onward!

<!-- [^1]: [state]({{< relref "/docs/intro/concepts/state" >}}) -->
