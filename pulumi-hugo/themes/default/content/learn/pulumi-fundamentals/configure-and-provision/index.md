---
title: "Configuring and Provisioning Containers"
layout: topic
date: 2021-09-07T14:12:59-05:00
draft: false
description: Configure and provision your first containers locally with Pulumi.
meta_desc: Configure and provision your first containers locally with Pulumi.
index: 2
estimated_time: 10
meta_image: meta.png
authors:
    - sophia-parafina
    - laura-santamaria
tags:
    - fundamentals
    - configuration
    - provisioning
    - containers
    - docker
links:
    - text: Code Repo
      url: https://github.com/pulumi/tutorial-pulumi-fundamentals
---

Now that we've created our images, we can provision our application with a
network and containers. First, we're going to add configuration to our Pulumi
program. Pulumi is a tool to
[configure]({{< relref "docs/intro/concepts/config" >}}) your infrastructure,
and that includes being able to configure the different stacks with different
values. As a result, it makes sense to include the basic configurations as
variables at the top of your program.

## Configure the application

Add the following configuration variables to your Pulumi program:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

These configuration declarations go below your imports.

```typescript
// get configuration
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");
```

{{% /choosable %}}

{{% choosable language python %}}

These configuration declarations go below your imports.

```python
# get configuration
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
```

{{% /choosable %}}

{{% choosable language java %}}

These configuration declarations go in the static `stack()` method:

```java
var config = ctx.config();
var frontendPort = config.requireInteger("frontendPort");
var backendPort = config.requireInteger("backendPort");
var mongoPort = config.requireInteger("mongoPort");
```

{{% /choosable %}}

{{% choosable language yaml %}}

These statements go between the `description` and the `resources`.

```yaml
configuration:
  frontendPort:
    type: Integer
  backendPort:
    type: Integer
  mongoPort:
    type: Integer
variables:
  backendImageName: backend
  frontendImageName: frontend
```

{{% /choosable %}}

Your Pulumi program should now match this code:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

// get configuration
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");

const stack = pulumi.getStack();

const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});

// build our frontend image!
const frontendImageName = "frontend";
const frontend = new docker.RemoteImage(`${frontendImageName}`, {
    name: "pulumi/tutorial-pulumi-fundamentals-frontend:latest",
});

// build our mongodb image!
const mongoImage = new docker.RemoteImage("mongo", {
    name: "pulumi/tutorial-pulumi-fundamentals-database-local:latest",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import os
import pulumi
import pulumi_docker as docker

# get configuration
config = pulumi.Config()
frontend_port = config.require_int("frontend_port")
backend_port = config.require_int("backend_port")
mongo_port = config.require_int("mongo_port")

stack = pulumi.get_stack()

# build our backend image!
backend_image_name = "backend"
backend = docker.RemoteImage("backend",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                            )

# build our frontend image!
frontend_image_name = "frontend"
frontend = docker.RemoteImage("frontend",
                              name="pulumi/tutorial-pulumi-fundamentals-frontend:latest"
                             )

# build our mongodb image!
mongo_image = docker.RemoteImage("mongo",
                                 name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
                                )
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package my_first_app;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.docker.RemoteImage;
import com.pulumi.docker.RemoteImageArgs;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var config = ctx.config();
        var frontendPort = config.requireInteger("frontendPort");
        var backendPort = config.requireInteger("backendPort");
        var mongoPort = config.requireInteger("mongoPort");

        final var stackName = ctx.stackName();

        // Create our images
        final String backendImageName = "backend";
        var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );

        final String frontendImageName = "frontend";
        var frontendImage = new RemoteImage(
                frontendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",frontendImageName))
                        .build()
        );

        var mongoImage = new RemoteImage(
                "mongoImage",
                RemoteImageArgs.builder()
                        .name("pulumi/tutorial-pulumi-fundamentals-database-local:latest")
                        .build()
        );
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: fundamentals
runtime: yaml
description: a yaml test
configuration:
  frontendPort:
    type: Integer
  backendPort:
    type: Integer
  mongoPort:
    type: Integer
variables:
  backendImageName: backend
  frontendImageName: frontend
resources:
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest
  frontend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-frontend:latest
  mongo-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-database-local:latest
```

{{% /choosable %}}

Try and run your `pulumi up` again at this point. You should get an error like
this:

```bash
Diagnostics:
  pulumi:pulumi:Stack (my_first_app-dev):
    error: Missing required configuration variable 'my_first_app:frontendPort'
        please set a value using the command `pulumi config set my_first_app:frontendPort <value>`
    error: an unhandled error occurred: <...> exited with non-zero exit code: 1
```

This is because we have specified that this config option is _required_.
Remember how we can use the same program to define multiple stacks? Let's set
the ports for this stack, which the Pulumi command line knows already from when
you first initialized the project (it's the `dev` stack by default):

```bash
pulumi config set frontendPort 3001
pulumi config set backendPort 3000
pulumi config set mongoPort 27017
```

This set of commands creates a file in your directory called `Pulumi.dev.yaml`
to store the configuration for this stack.

Now, try and rerun your Pulumi program.

Your Pulumi program should now run, but you're not actually using these newly
configured ports just yet! That's because we don't have any container resources
that use the ports; we only have image resources.

## Create a Container resource

In the last topic, we built Docker images. Now we want to create Docker
containers and pass our configuration to them. Our containers will need to
connect to each other, so we will need to create a
[`Network`]({{< relref "registry/packages/docker/api-docs/network" >}}), which
is another resource. Add the following code at the bottom of your program:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// create a network!
const network = new docker.Network("network", {
    name: `services-${stack}`,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# create a network!
network = docker.Network("network", name=f"services-{stack}")
```

{{% /choosable %}}

{{% choosable language java %}}

Add these imports to the top:

```java
import com.pulumi.docker.Network;
import com.pulumi.docker.NetworkArgs;
import com.pulumi.docker.Container;
import com.pulumi.docker.ContainerArgs;
import com.pulumi.docker.inputs.ContainerNetworksAdvancedArgs;
import com.pulumi.docker.inputs.ContainerPortArgs;
import com.pulumi.resources.CustomResourceOptions;
```

Add this code at the bottom:

```java
// Set up a Docker Network
var network = new Network(
        "network",
        NetworkArgs.builder()
                .name(String.format("services-%s",stackName))
                .build()
);
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  network:
    type: docker:index:Network
    properties:
      name: services-${pulumi.stack}
```

{{% /choosable %}}

Define a new
[`Container`]({{< relref "registry/packages/docker/api-docs/container" >}})
resource in your Pulumi program below the `Network` resource, like this:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// create the backend container!
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
        `DATABASE_HOST=${mongoHost}`,
        `DATABASE_NAME=${database}`,
        `NODE_ENV=${nodeEnvironment}`,
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
}, { dependsOn: [ mongoContainer ]});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# create the backend container!
backend_container = docker.Container("backend_container",
                        name=f"backend-{stack}",
                        image=backend.repo_digest,
                        ports=[docker.ContainerPortArgs(
                            internal=backend_port,
                            external=backend_port)],
                        envs=[
                            f"DATABASE_HOST={mongo_host}",
                            f"DATABASE_NAME={database}",
                            f"NODE_ENV={node_environment}"
                        ],
                        networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                            name=network.name
                        )],
                        opts=pulumi.ResourceOptions(depends_on=[mongo_container])
                        )
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var backendContainer = new Container(
                "backendContainer",
                ContainerArgs.builder()
                        .name(String.format("backend-%s",stackName))
                        .image(backendImage.repoDigest())
                        .ports(ContainerPortArgs.builder()
                                .internal(backendPort)
                                .external(backendPort)
                                .build())
                        .envs(List.of(
                                String.format("DATABASE_HOST=%s",mongoHost),
                                String.format("DATABASE_NAME=%s",database),
                                String.format("NODE_ENV%s",nodeEnvironment)
                        ))
                        .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                                .name(network.name())
                                .build()
                        )
                        .build(),
                CustomResourceOptions.builder()
                        .dependsOn(mongoContainer)
                        .build()
        );
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  backend-container:
    type: docker:index:Container
    properties:
      name: backend-${pulumi.stack}
      image: ${backend-image.repoDigest}
      ports:
        - internal: ${backendPort}
          external: ${backendPort}
      envs:
        [
          "DATABASE_HOST=${mongoHost}",
          "DATABASE_NAME=${database}",
          "NODE_ENV=${nodeEnvironment}"
        ]
      networksAdvanced:
        - name: ${network.name}
          aliases: ["backend-${pulumi.stack}"]
    options:
      dependsOn:
        - ${mongo-container}
```

{{% /choosable %}}

{{% choosable language typescript %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backendContainer` depends on the `mongoContainer`. If we tried to run `pulumi up` without the `mongoContainer` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

{{% choosable language python %}}

It is important to note something here. In the `Container` resource, we are referencing `repo_digest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `Image` resource. Another dependency to note is that the `backend_container` depends on the `mongo_container`. If we tried to run `pulumi up` without the `mongo_container` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

{{% choosable language java %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backendContainer` depends on the `mongoContainer`. If we tried to run `pulumi up` without the `mongoContainer` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

{{% choosable language yaml %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backend-container` depends on the `mongo-container`. If we tried to run `pulumi up` without the `mongo-container` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

The backend container also requires environment variables to connect to the
mongo container and set the node environment for Express.js. These are set in
`./app/backend/src/.env`. Like before we can set them using `pulumi config` on
the command line:

```bash
pulumi config set mongoHost mongodb://mongo:27017
pulumi config set database cart
pulumi config set nodeEnvironment development
pulumi config set protocol http://
```

Then, we need to add them to the top of our program with the rest of the
configuration variables.

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
const mongoHost = config.require("mongoHost"); // Note that strings are the default, so it's not `config.requireString`, just `config.require`.
const database = config.require("database");
const nodeEnvironment = config.require("nodeEnvironment");
const protocol = config.require("protocol")
```

{{% /choosable %}}

{{% choosable language python %}}

```python
mongo_host = config.require("mongoHost") # Note that strings are the default, so it's not `config.require_str`, just `config.require`.
database = config.require("database")
node_environment = config.require("nodeEnvironment")
protocol = config.require("protocol")
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var mongoHost = config.require("mongoHost");
var database = config.require("database");
var nodeEnvironment = config.require("nodeEnvironment");
var protocol = config.require("protocol");
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  mongoHost:
    type: String
  database:
    type: String
  nodeEnvironment:
    type: String
  protocol:
    type: String
```

{{% /choosable %}}

{{% choosable language typescript %}}

We also need to create `Container` resources for the frontend and mongo
containers. Put the `mongoContainer` declaration just above the `backendContainer` one, and the
`frontendContainer` declaration at the end of the file. Here's the code for the mongo container:

{{% /choosable %}}

{{% choosable language python %}}

We also need to create `Container` resources for the frontend and mongo
containers. Put the `mongo_container` declaration just above the `backend_container` one, and the
`frontend_container` declaration at the end of the file. Here's the code for the mongo container:

{{% /choosable %}}

{{% choosable language java %}}

We also need to create `Container` resources for the frontend and mongo containers. Put the `mongoContainer` declaration just above the `backendContainer` one, and the `frontendContainer` declaration at the end of the file. Here's the code for the mongo container:

{{% /choosable %}}

{{% choosable language yaml %}}

We also need to create `Container` resources for the frontend and mongo containers. Put the `mongo-container` declaration just above the `backend-container` one, and the `frontend-container` declaration at the end of the file. Here's the code for the mongo container:

{{% /choosable %}}

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// create the mongo container!
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
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# create the mongo container!
mongo_container = docker.Container("mongo_container",
                        image=mongo_image.repo_digest,
                        name=f"mongo-{stack}",
                        ports=[docker.ContainerPortArgs(
                          internal=mongo_port,
                          external=mongo_port
                        )],
                        networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                            name=network.name,
                            aliases=["mongo"]
                        )]
                        )
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var mongoContainer = new Container(
        "mongoContainer",
        ContainerArgs.builder()
                .name(String.format("mongo-%s",stackName))
                .image(mongoImage.repoDigest())
                .ports(ContainerPortArgs.builder()
                        .internal(mongoPort)
                        .external(mongoPort)
                        .build())
                .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                        .name(network.name())
                        .aliases("mongo")
                        .build()
                )
                .build()
);
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  mongo-container:
    type: docker:index:Container
    properties:
      name: mongo-${pulumi.stack}
      image: ${mongo-image.repoDigest}
      ports:
        - internal: ${mongoPort}
          external: ${mongoPort}
      networksAdvanced:
        - name: ${network.name}
          aliases: ["mongo"]
```

{{% /choosable %}}

And the code for the frontend container:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// create the frontend container!
const frontendContainer = new docker.Container("frontendContainer", {
    image: frontend.repoDigest,
    name: `frontend-${stack}`,
    ports: [
        {
            internal: frontendPort,
            external: frontendPort,
        },
    ],
    envs: [
        `LISTEN_PORT=${frontendPort}`,
        `HTTP_PROXY=backend-${stack}:${backendPort}`,
        `PROXY_PROTOCOL=${protocol}`
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# create the frontend container!
frontend_container = docker.Container("frontend_container",
                                      image=frontend.repo_digest,
                                      name=f"frontend-{stack}",
                                      ports=[docker.ContainerPortArgs(
                                          internal=frontend_port,
                                          external=frontend_port
                                      )],
                                      envs=[
                                          f"LISTEN_PORT={frontend_port}",
                                          f"HTTP_PROXY=backend-{stack}:{backend_port}",
                                          f"PROXY_PROTOCOL={protocol}"
                                      ],
                                      networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                          name=network.name
                                      )]
                                      )
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var frontendContainer = new Container(
        "frontendContainer",
        ContainerArgs.builder()
                .name(String.format("frontend-%s",stackName))
                .image(frontendImage.repoDigest())
                .ports(ContainerPortArgs.builder()
                        .internal(frontendPort)
                        .external(frontendPort)
                        .build())
                .envs(List.of(
                        String.format("LISTEN_PORT=%d",frontendPort),
                        String.format("HTTP_PROXY=backend-%s:%d",stackName,backendPort),
                        String.format("PROXY_PROTOCOL=%s",protocol)
                ))
                .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                        .name(network.name())
                        .build())
                .build()
);
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  frontend-container:
    type: docker:index:Container
    properties:
      name: frontend-${pulumi.stack}
      image: ${frontend-image.repoDigest}
      ports:
        - internal: ${frontendPort}
          external: ${frontendPort}
      envs:
        [
          "LISTEN_PORT=${frontendPort}",
          "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
          "PROXY_PROTOCOL=http://"
        ]
      networksAdvanced:
        - name: ${network.name}
          aliases: ["frontend-${pulumi.stack}"]
```

{{% /choosable %}}

Let's see what the whole program looks like next.

## Put it all together

Now that we know how to create a container we can complete our program.

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

// get configuration
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");
const mongoHost = config.require("mongoHost"); // Note that strings are the default, so it's not `config.requireString`, just `config.require`.
const database = config.require("database");
const nodeEnvironment = config.require("nodeEnvironment");
const protocol = config.require("protocol")

const stack = pulumi.getStack();

const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});

// build our frontend image!
const frontendImageName = "frontend";
const frontend = new docker.RemoteImage(`${frontendImageName}`, {
    name: "pulumi/tutorial-pulumi-fundamentals-frontend:latest",
});

// build our mongodb image!
const mongoImage = new docker.RemoteImage("mongo", {
    name: "pulumi/tutorial-pulumi-fundamentals-database-local:latest",
});

// create a network!
const network = new docker.Network("network", {
    name: `services-${stack}`,
});

// create the mongo container!
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
});

// create the backend container!
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
        `DATABASE_HOST=${mongoHost}`,
        `DATABASE_NAME=${database}`,
        `NODE_ENV=${nodeEnvironment}`,
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
}, { dependsOn: [ mongoContainer ]});

// create the frontend container!
const frontendContainer = new docker.Container("frontendContainer", {
    image: frontend.repoDigest,
    name: `frontend-${stack}`,
    ports: [
        {
            internal: frontendPort,
            external: frontendPort,
        },
    ],
    envs: [
        `LISTEN_PORT=${frontendPort}`,
        `HTTP_PROXY=backend-${stack}:${backendPort}`,
        `PROXY_PROTOCOL=${protocol}`
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import os
import pulumi
import pulumi_docker as docker

# get configuration
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
mongo_host = config.require("mongoHost") # Note that strings are the default, so it's not `config.require_str`, just `config.require`.
database = config.require("database")
node_environment = config.require("nodeEnvironment")
protocol = config.require("protocol")

stack = pulumi.get_stack()

# build our backend image!
backend_image_name = "backend"
backend = docker.RemoteImage("backend",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                            )

# build our frontend image!
frontend_image_name = "frontend"
frontend = docker.RemoteImage("frontend",
                              name="pulumi/tutorial-pulumi-fundamentals-frontend:latest"
                             )

# build our mongodb image!
mongo_image = docker.RemoteImage("mongo",
                                 name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
                                )

# create a network!
network = docker.Network("network", name=f"services-{stack}")

# create the mongo container!
mongo_container = docker.Container("mongo_container",
                        image=mongo_image.repo_digest,
                        name=f"mongo-{stack}",
                        ports=[docker.ContainerPortArgs(
                          internal=mongo_port,
                          external=mongo_port
                        )],
                        networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                            name=network.name,
                            aliases=["mongo"]
                        )]
                        )

# create the backend container!
backend_container = docker.Container("backend_container",
                        name=f"backend-{stack}",
                        image=backend.repo_digest,
                        ports=[docker.ContainerPortArgs(
                            internal=backend_port,
                            external=backend_port)],
                        envs=[
                            f"DATABASE_HOST={mongo_host}",
                            f"DATABASE_NAME={database}",
                            f"NODE_ENV={node_environment}"
                        ],
                        networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                            name=network.name
                        )],
                        opts=pulumi.ResourceOptions(depends_on=[mongo_container])
                        )

# create the frontend container!
frontend_container = docker.Container("frontend_container",
                                      image=frontend.repo_digest,
                                      name=f"frontend-{stack}",
                                      ports=[docker.ContainerPortArgs(
                                          internal=frontend_port,
                                          external=frontend_port
                                      )],
                                      envs=[
                                          f"LISTEN_PORT={frontend_port}",
                                          f"HTTP_PROXY=backend-{stack}:{backend_port}",
                                          f"PROXY_PROTOCOL={protocol}"
                                      ],
                                      networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                          name=network.name
                                      )]
                                      )

```

{{% /choosable %}}

{{% choosable language java %}}

```java
package my_first_app;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.docker.RemoteImage;
import com.pulumi.docker.RemoteImageArgs;
import com.pulumi.docker.Network;
import com.pulumi.docker.NetworkArgs;
import com.pulumi.docker.Container;
import com.pulumi.docker.ContainerArgs;
import com.pulumi.docker.inputs.ContainerNetworksAdvancedArgs;
import com.pulumi.docker.inputs.ContainerPortArgs;
import com.pulumi.resources.CustomResourceOptions;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var config = ctx.config();
        var frontendPort = config.requireInteger("frontendPort");
        var backendPort = config.requireInteger("backendPort");
        var mongoPort = config.requireInteger("mongoPort");
        var mongoHost = config.require("mongoHost");
        var database = config.require("database");
        var nodeEnvironment = config.require("nodeEnvironment");
        var protocol = config.require("protocol");

        final var stackName = ctx.stackName();

        // Create our images
        final String backendImageName = "backend";
        var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );

        final String frontendImageName = "frontend";
        var frontendImage = new RemoteImage(
                frontendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",frontendImageName))
                        .build()
        );

        var mongoImage = new RemoteImage(
                "mongoImage",
                RemoteImageArgs.builder()
                        .name("pulumi/tutorial-pulumi-fundamentals-database-local:latest")
                        .build()
        );

        // Set up a Docker Network
        var network = new Network(
                "network",
                NetworkArgs.builder()
                        .name(String.format("services-%s",stackName))
                        .build()
        );

        // Container time!
        var mongoContainer = new Container(
                "mongoContainer",
                ContainerArgs.builder()
                        .name(String.format("mongo-%s",stackName))
                        .image(mongoImage.repoDigest())
                        .ports(ContainerPortArgs.builder()
                                .internal(mongoPort)
                                .external(mongoPort)
                                .build())
                        .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                                .name(network.name())
                                .aliases("mongo")
                                .build()
                        )
                        .build()
        );

        var backendContainer = new Container(
                "backendContainer",
                ContainerArgs.builder()
                        .name(String.format("backend-%s",stackName))
                        .image(backendImage.repoDigest())
                        .ports(ContainerPortArgs.builder()
                                .internal(backendPort)
                                .external(backendPort)
                                .build())
                        .envs(List.of(
                                String.format("DATABASE_HOST=%s",mongoHost),
                                String.format("DATABASE_NAME=%s",database),
                                String.format("NODE_ENV%s",nodeEnvironment)
                        ))
                        .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                                .name(network.name())
                                .build()
                        )
                        .build(),
                CustomResourceOptions.builder()
                        .dependsOn(mongoContainer)
                        .build()
        );

        var frontendContainer = new Container(
                "frontendContainer",
                ContainerArgs.builder()
                        .name(String.format("frontend-%s",stackName))
                        .image(frontendImage.repoDigest())
                        .ports(ContainerPortArgs.builder()
                                .internal(frontendPort)
                                .external(frontendPort)
                                .build()
                        )
                        .envs(List.of(
                                String.format("LISTEN_PORT=%d",frontendPort),
                                String.format("HTTP_PROXY=backend-%s:%d",stackName,backendPort),
                                String.format("PROXY_PROTOCOL=%s",protocol)
                        ))
                        .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                                .name(network.name())
                                .build())
                        .build()
        );

        ctx.export("link", Output.of("http://localhost:3001"));
        return ctx.exports();
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: fundamentals
runtime: yaml
description: a yaml test
configuration:
  frontendPort:
    type: Number
  backendPort:
    type: Number
  mongoPort:
    type: Number
  mongoHost:
    type: String
  database:
    type: String
  nodeEnvironment:
    type: String
  protocol:
    type: String
variables:
  backendImageName: backend
  frontendImageName: frontend
resources:
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest
  frontend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-frontend:latest
  mongo-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-database-local:latest
  network:
    type: docker:index:Network
    properties:
      name: services-${pulumi.stack}
  mongo-container:
    type: docker:index:Container
    properties:
      name: mongo-${pulumi.stack}
      image: ${mongo-image.repoDigest}
      ports:
        - internal: ${mongoPort}
          external: ${mongoPort}
      networksAdvanced:
        - name: ${network.name}
          aliases: ["mongo"]
  backend-container:
    type: docker:index:Container
    properties:
      name: backend-${pulumi.stack}
      image: ${backend-image.repoDigest}
      ports:
        - internal: ${backendPort}
          external: ${backendPort}
      envs:
        [
          "DATABASE_HOST=${mongoHost}",
          "DATABASE_NAME=${database}",
          "NODE_ENV=${nodeEnvironment}"
        ]
      networksAdvanced:
        - name: ${network.name}
          aliases: ["backend-${pulumi.stack}"]
    options:
      dependsOn:
        - ${mongo-container}
  frontend-container:
    type: docker:index:Container
    properties:
      name: frontend-${pulumi.stack}
      image: ${frontend-image.repoDigest}
      ports:
        - internal: ${frontendPort}
          external: ${frontendPort}
      envs:
        [
          "LISTEN_PORT=${frontendPort}",
          "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
          "PROXY_PROTOCOL=http://"
        ]
      networksAdvanced:
        - name: ${network.name}
          aliases: ["frontend-${pulumi.stack}"]
```

{{% /choosable %}}

With Docker networking, we can use image names to refer to a container. In our
example, the React frontend client sends requests to the Express backend client.
The URL to the backend is set via the `setupProxy.js` file in the
`app/frontend/src` directory with the `HTTP_PROXY` environment variable.

Run `pulumi up` to get the application running. Open a browser to `http://localhost:3001`, and our application is now deployed.

## Update the database

What if we want to add to the products on the page? We can POST to the API just as we would any API. Generally speaking, you would typically wire the database to an API and update it that way with any cloud, so we're going to do exactly that here.

Open a terminal and run the following command.

```bash
curl --location --request POST 'http://localhost:3000/api/products' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ratings": {
        "reviews": [],
        "total": 63,
        "avg": 5
    },
    "created": 1600979464567,
    "currency": {
        "id": "USD",
        "format": "$"
    },
    "sizes": [
        "M",
        "L"
    ],
    "category": "boba",
    "teaType": 2,
    "status": 1,
    "_id": "5f6d025008a1b6f0e5636bc7",
    "images": [
        {
            "src": "classic_boba.png"
        }
    ],
    "name": "My New Milk Tea",
    "price": 5,
    "description": "none",
    "productCode": "852542-107"
}'
```

You should get back the following response:

```bash
{"status":"ok","data":{"product":{"ratings":{"reviews":[],"total":63,"avg":5},"created":1600979464567,"currency":{"id":"USD","format":"$"},"sizes":["M","L"],"category":"boba","teaType":2,"status":1,"_id":"5f6d025008a1b6f0e5636bc7","images":[{"_id":"62608f2a9ad5d90026847b0f","src":"classic_boba.png"}],"name":"My New Milk Tea","price":5,"description":"none","productCode":"852542-107","__v":0}}}
```

Refresh the app on `http://localhost:3001`, and our data is now updated!

## Cleaning up

Whenever you're working on learning something new with Pulumi, it's always a
good idea to clean up any resources you've created so you don't get charged on a
free tier or otherwise leave behind resources you'll never use. Let's clean up.

Run the `pulumi destroy` command to remove all of the resources:

```bash
$ pulumi destroy
Previewing destroy (dev)

View Live: https://app.pulumi.com/<org>/<project>/<stack>/previews/<build-id>

...
Do you want to perform this destroy? yes
Destroying (dev)

View Live: https://app.pulumi.com/<org>/<project>/<stack>/updates/<update-id>

...

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run 'pulumi stack rm dev'.
```

Now your resources should all be cleared! That last comment you see in the
output notes that the stack and all of the configuration and history will stay
in your dashboard on the Pulumi Service ([app.pulumi.com](https://app.pulumi.com/)). For now, that's okay. We'll talk
more about removing the project from your history in another pathway.

---

Congratulations, you've now finished Pulumi Fundamentals! You learned to create
a Pulumi project; work on your Pulumi program to build Docker images,
containers, and networks; and deploy the infrastructure locally with your first
resource provider. Now, head back to the main page and explore some other
tutorials to understand more about Pulumi. The best next step to take is to
explore the [Building with
Pulumi]({{< relref "learn/building-with-pulumi" >}}) pathway.
