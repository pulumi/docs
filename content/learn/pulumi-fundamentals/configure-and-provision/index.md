---
title_tag: Configuring & Provisioning Containers | Learn Pulumi
title: "Configuring and Provisioning Containers"
layout: topic
date: 2021-09-07T14:12:59-05:00
draft: false
description: Configure and provision your first containers locally with Pulumi.
meta_desc: Learn how to configure and provision your first containers locally with Pulumi in this tutorial.
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
[configure](/docs/concepts/config/) your infrastructure,
and that includes being able to configure the different stacks with different
values. As a result, it makes sense to include the basic configurations as
variables at the top of your program.

## Configure the application

Add the following configuration variables to your Pulumi program:

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

These configuration declarations go below your imports.

```typescript
// Get configuration values
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");
```

{{% /choosable %}}

{{% choosable language python %}}

These configuration declarations go below your imports.

```python
# Get configuration values
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
```

{{% /choosable %}}

{{% choosable language go %}}

First, add this to the end of your `import` section:

```go
"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
```

Run `go mod tidy` to update the `go.mod` and `go.sum` files as necessary.

Next, add these configuration declarations near the top of the `main()` function, just after the `pulumi.Run` line.

```go
// Get configuration values
cfg := config.New(ctx, "")
frontendPort := cfg.RequireFloat64("frontendPort")
backendPort := cfg.RequireFloat64("backendPort")
mongoPort := cfg.RequireFloat64("mongoPort")
_ = frontendPort + backendPort + mongoPort
```

That last line is, again, just to satisfy Go's requirement that no variables can be declared that aren't used later. We'll remove this as we proceed.

{{% /choosable %}}

{{% choosable language java %}}

These configuration declarations go in the static `stack()` method:

```java
// Get configuration values
final var config = ctx.config();
final var frontendPort = config.requireInteger("frontendPort");
final var backendPort = config.requireInteger("backendPort");
final var mongoPort = config.requireInteger("mongoPort");
```

{{% /choosable %}}

{{% choosable language yaml %}}

These statements go between the `description` and the `resources` where `configuration` and `variables` have been:

```yaml
# Get configuration values
configuration:
  frontendPort:
    type: Number
  backendPort:
    type: Number
  mongoPort:
    type: Number

# Define variables
variables:
  backendImageName: backend
  frontendImageName: frontend
```

{{% /choosable %}}

You'll end up using these configuration values later, passing them as environment variables to the containers.

Your Pulumi program should now match this code:

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

// Get configuration values
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");

const stack = pulumi.getStack();

// Pull the backend image
const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}Image`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});

// Pull the frontend image
const frontendImageName = "frontend";
const frontend = new docker.RemoteImage(`${frontendImageName}Image`, {
    name: "pulumi/tutorial-pulumi-fundamentals-frontend:latest",
});

// Pull the MongoDB image
const mongoImage = new docker.RemoteImage("mongoImage", {
    name: "pulumi/tutorial-pulumi-fundamentals-database-local:latest",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_docker as docker

# Get configuration values
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(f"{backend_image_name}_image",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                            )

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(f"{frontend_image_name}_image",
                              name="pulumi/tutorial-pulumi-fundamentals-frontend:latest"
                             )

# Pull the MongoDB image
mongo_image = docker.RemoteImage("mongo_image",
                                 name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
                                )
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Get configuration values
		cfg := config.New(ctx, "")
		frontendPort := cfg.RequireFloat64("frontendPort")
		backendPort := cfg.RequireFloat64("backendPort")
		mongoPort := cfg.RequireFloat64("mongoPort")
		_ = frontendPort + backendPort + mongoPort

		// Pull the backend image
		backendImageName := "backend"
		backendImage, err := docker.NewRemoteImage(ctx, fmt.Sprintf("%v-image", backendImageName), &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-backend:latest"),
		})
		if err != nil {
			return err
		}
		ctx.Export("backendDockerImage", backendImage.Name)

		// Pull the frontend image
		frontendImageName := "frontend"
		frontendImage, err := docker.NewRemoteImage(ctx, fmt.Sprintf("%v-image", frontendImageName), &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-frontend:latest"),
		})
		if err != nil {
			return err
		}
		ctx.Export("frontendDockerImage", frontendImage.Name)

		// Pull the MongoDB image
		mongoImage, err := docker.NewRemoteImage(ctx, "mongo-image", &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-database-local:latest"),
		})
		if err != nil {
			return err
		}
		ctx.Export("mongoDockerImage", mongoImage.Name)

		return nil
	})
}
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
        // Get configuration values
        final var config = ctx.config();
        final var frontendPort = config.requireInteger("frontendPort");
        final var backendPort = config.requireInteger("backendPort");
        final var mongoPort = config.requireInteger("mongoPort");

        final var stackName = ctx.stackName();

        // Pull the backend image
        final String backendImageName = "backend";
        final var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );

        // Pull the frontend image
        final String frontendImageName = "frontend";
        final var frontendImage = new RemoteImage(
                frontendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",frontendImageName))
                        .build()
        );

        // Pull the MongoDB image
        final var mongoImage = new RemoteImage(
                "mongoImage",
                RemoteImageArgs.builder()
                        .name("pulumi/tutorial-pulumi-fundamentals-database-local:latest")
                        .build()
        );
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my_first_app
runtime: yaml
description: A minimal Pulumi YAML program

# Get configuration values
configuration:
  frontendPort:
    type: Number
  backendPort:
    type: Number
  mongoPort:
    type: Number

# Define variables
variables:
  backendImageName: backend
  frontendImageName: frontend
resources:
  # Pull the backend image
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest

  # Pull the frontend image
  frontend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-frontend:latest

  # Pull the MongoDB image
  mongo-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-database-local:latest
outputs:       {}
```

{{% /choosable %}}

Try and run your `pulumi up` again at this point. You should get an error that looks something like this:

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

The content of the file should be like this:

```yaml
config:
  my_first_app:backendPort: "3000"
  my_first_app:frontendPort: "3001"
  my_first_app:mongoPort: "27017"
```

Now, try and rerun your Pulumi program with `pulumi up` command.

Your Pulumi program should now run, but you're not actually using these newly
configured ports just yet! That's because we don't have any container resources
that use the ports; we only have image resources.

## Create a Container resource

In the last topic, we retrieved Docker images from a remote registry. Now we want to create Docker containers and pass these containers the configuration values we just defined. Our containers will need to connect to each other, so we will need to create a [`Network`](/registry/packages/docker/api-docs/network), which is another resource.

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

Add the following code at the bottom of your program:

```typescript
// Create a Docker network
const network = new docker.Network("network", {
    name: `services-${stack}`,
});
```

{{% /choosable %}}

{{% choosable language python %}}

Add the following code at the bottom of your program:

```python
# Create a Docker network
network = docker.Network("network", name=f"services_{stack}")
```

{{% /choosable %}}

{{% choosable language go %}}

Add this code at the bottom of your program, just before the last `return nil` statement:

```go
// Create a Docker network
network, err := docker.NewNetwork(ctx, "network", &docker.NetworkArgs{
	Name: pulumi.String(fmt.Sprintf("services-%v", ctx.Stack())),
})
if err != nil {
	return err
}
ctx.Export("containerNetwork", network.Name)
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
// Create a Docker Network
final var network = new Network(
        "network",
        NetworkArgs.builder()
                .name(String.format("services-%s",stackName))
                .build()
);
```

{{% /choosable %}}

{{% choosable language yaml %}}

 Add the following code at the bottom of your `resources` section:

```yaml
# Create a Docker network
network:
  type: docker:index:Network
  properties:
    name: services-${pulumi.stack}
```

{{% /choosable %}}

Define a new
[`Container`](/registry/packages/docker/api-docs/container)
resource in your Pulumi program below the `Network` resource, like this:

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// Create the backend container
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
# Create the backend container
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

{{% choosable language go %}}

```go
// Create the backend container
// Use _ instead of a variable name since this container isn't referenced
_, err = docker.NewContainer(ctx, "backend-container", &docker.ContainerArgs{
	Name:  pulumi.String(fmt.Sprintf("backend-%v", ctx.Stack())),
	Image: backendImage.RepoDigest,
	Ports: &docker.ContainerPortArray{
		&docker.ContainerPortArgs{
			Internal: pulumi.Int(backendPort),
			External: pulumi.Int(backendPort),
		},
	},
	Envs: pulumi.StringArray{
		pulumi.String(fmt.Sprintf("DATABASE_HOST=%v", mongoHost)),
		pulumi.String(fmt.Sprintf("DATABASE_NAME=%v", database)),
		pulumi.String(fmt.Sprintf("NODE_ENV=%v", nodeEnvironment)),
	},
	NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
		&docker.ContainerNetworksAdvancedArgs{
			Name: network.Name,
			Aliases: pulumi.StringArray{
				pulumi.String(fmt.Sprintf("backend-%v", ctx.Stack())),
			},
		},
	},
}, pulumi.DependsOn([]pulumi.Resource{
	mongoContainer,
}))
if err != nil {
	return err
}
```

Because we now have something that is referencing the `backendImage` and `network` resources we defined earlier, we can now remove the `ctx.Export` statements for those resources from our code.

{{% /choosable %}}

{{% choosable language java %}}

```java
// Create the backend container
final var backendContainer = new Container(
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
                                String.format("NODE_ENV=%s",nodeEnvironment)
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
# Create the backend container
backend-container:
  type: docker:index:Container
  properties:
    name: ${backendImageName}-${pulumi.stack}
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
        aliases: ["${backendImageName}-${pulumi.stack}"]
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

{{% choosable language go %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backendContainer` depends on the `mongoContainer`. If we tried to run `pulumi up` without the `mongoContainer` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

{{% choosable language java %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backendContainer` depends on the `mongoContainer`. If we tried to run `pulumi up` without the `mongoContainer` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

{{% choosable language yaml %}}

It is important to note something here. In the `Container` resource, we are referencing `repoDigest` from the `RemoteImage` resource. Pulumi now knows there is a dependency between these two resources and will know to create the `Container` resource _after_ the `RemoteImage` resource. Another dependency to note is that the `backend-container` depends on the `mongo-container`. If we tried to run `pulumi up` without the `mongo-container` running or present somewhere in state, Pulumi would let us know that the resource didn't exist and would stop.

{{% /choosable %}}

It's also important to note the backend container requires some environment variables to connect to the Mongo container and to set the Node environment for Express.js. These are set in the `backend/src/.env` file in the [tutorial-pulumi-fundamentals](https://github.com/pulumi/tutorial-pulumi-fundamentals/tree/main/backend) repository. We don't want to hardcode these values; we want them to be configurable. To do that, we'll need to define some additional configuration values. Like before, we can set them using `pulumi config` on the command line:

```bash
pulumi config set mongoHost mongodb://mongo:27017
pulumi config set database cart
pulumi config set nodeEnvironment development
pulumi config set protocol http://
```

Then, we need to add them to the top of our program with the rest of the
configuration values.

{{< chooser language "typescript,python,go,java,yaml" / >}}

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

{{% choosable language go %}}

```go
mongoHost := cfg.Require("mongoHost") // Note that strings are the default, so it's not `cfg.RequireStr`, just `cfg.Require`
database := cfg.Require("database")
nodeEnvironment := cfg.Require("nodeEnvironment")
protocol := cfg.Require("protocol")
```

{{% /choosable %}}

{{% choosable language java %}}

```java
final var mongoHost = config.require("mongoHost"); // Note that strings are the default, so it's not `config.requireString`, just `config.require`
final var database = config.require("database");
final var nodeEnvironment = config.require("nodeEnvironment");
final var protocol = config.require("protocol");
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
mongoHost:
  type: string
database:
  type: string
nodeEnvironment:
  type: string
protocol:
  type: string
```

{{% /choosable %}}

All these configuration values are set as required, meaning if you forget to set them with `pulumi config set`, then `pulumi up` will report an error.

{{% choosable language typescript %}}

We also need to create `Container` resources for the frontend and Mongo
containers. Put the `mongoContainer` declaration just before the `backendContainer` one, and the
`frontendContainer` declaration after the `backendContainer` declaration. Here's the code for the Mongo container:

{{% /choosable %}}

{{% choosable language python %}}

We also need to create `Container` resources for the frontend and Mongo
containers. Put the `mongo_container` declaration just before the `backend_container` one, and the
`frontend_container` declaration after `backend_container`. Here's the code for the Mongo container:

{{% /choosable %}}

{{% choosable language go %}}

We also need to create `Container` resources for the frontend and Mongo
containers. Put the `mongoContainer` declaration just before the declaration for the backend container and declaration for the frontend container just after the declaration for the backend container. Here's the code for the Mongo container:

{{% /choosable %}}

{{% choosable language java %}}

We also need to create `Container` resources for the frontend and Mongo containers. Put the `mongoContainer` declaration just before the `backendContainer` one, and the `frontendContainer` declaration after the declaration for `backendContainer`. Here's the code for the Mongo container:

{{% /choosable %}}

{{% choosable language yaml %}}

We also need to create `Container` resources for the frontend and Mongo containers. Put the `mongo-container` declaration just before the `backend-container` one, and the `frontend-container` declaration after the `backend-container` declaration. Here's the code for the Mongo container:

{{% /choosable %}}

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// Create the MongoDB container
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
# Create the MongoDB container
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

{{% choosable language go %}}

```go
// Create the MongoDB container
mongoContainer, err := docker.NewContainer(ctx, "mongo-container", &docker.ContainerArgs{
	Name:  pulumi.String(fmt.Sprintf("mongo-%v", ctx.Stack())),
	Image: mongoImage.RepoDigest,
	Ports: &docker.ContainerPortArray{
		&docker.ContainerPortArgs{
			Internal: pulumi.Int(mongoPort),
			External: pulumi.Int(mongoPort),
		},
	},
	NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
		&docker.ContainerNetworksAdvancedArgs{
			Name: network.Name,
			Aliases: pulumi.StringArray{
				pulumi.String("mongo"),
			},
		},
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Create the MongoDB container
final var mongoContainer = new Container(
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
# Create the MongoDB container
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

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
// Create the frontend container
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
        `PORT=${frontendPort}`,
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
# Create the frontend container
frontend_container = docker.Container("frontend_container",
                                      image=frontend.repo_digest,
                                      name=f"frontend-{stack}",
                                      ports=[docker.ContainerPortArgs(
                                          internal=frontend_port,
                                          external=frontend_port
                                      )],
                                      envs=[
                                          f"PORT={frontend_port}",
                                          f"HTTP_PROXY=backend-{stack}:{backend_port}",
                                          f"PROXY_PROTOCOL={protocol}"
                                      ],
                                      networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                          name=network.name
                                      )]
                                      )
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create the frontend container
_, err = docker.NewContainer(ctx, "frontend-container", &docker.ContainerArgs{
	Name:  pulumi.String(fmt.Sprintf("frontend-%v", ctx.Stack())),
	Image: frontendImage.RepoDigest,
	Ports: &docker.ContainerPortArray{
		&docker.ContainerPortArgs{
			Internal: pulumi.Int(frontendPort),
			External: pulumi.Int(frontendPort),
		},
	},
	Envs: pulumi.StringArray{
		pulumi.String(fmt.Sprintf("PORT=%v", frontendPort)),
		pulumi.String(fmt.Sprintf("HTTP_PROXY=backend-%v:%v", ctx.Stack(), backendPort)),
		pulumi.String(fmt.Sprintf("PROXY_PROTOCOL=%v", protocol)),
	},
	NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
		&docker.ContainerNetworksAdvancedArgs{
			Name: network.Name,
			Aliases: pulumi.StringArray{
				pulumi.String(fmt.Sprintf("frontend-%v", ctx.Stack())),
			},
		},
	},
})
if err != nil {
	return err
}
```

At this point, all the variables we've declared have been used, so you can remove all the `ctx.Export` statements, and remove this line from the configuration declarations near the top of your program:

```go
_ = frontendPort + backendPort + mongoPort
```

We used these lines to temporarily satisfy Go's requirements as we were building out the program; now that our program is complete, they are no longer needed.

{{% /choosable %}}

{{% choosable language java %}}

```java
// Create the frontend container
final var frontendContainer = new Container(
        "frontendContainer",
        ContainerArgs.builder()
                .name(String.format("frontend-%s",stackName))
                .image(frontendImage.repoDigest())
                .ports(ContainerPortArgs.builder()
                        .internal(frontendPort)
                        .external(frontendPort)
                        .build())
                .envs(List.of(
                        String.format("PORT=%d",frontendPort),
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
# Create the frontend container
frontend-container:
  type: docker:index:Container
  properties:
    name: ${frontendImageName}-${pulumi.stack}
    image: ${frontend-image.repoDigest}
    ports:
      - internal: ${frontendPort}
        external: ${frontendPort}
    envs:
      [
        "PORT=${frontendPort}",
        "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
        "PROXY_PROTOCOL=${protocol}"
      ]
    networksAdvanced:
      - name: ${network.name}
        aliases: ["${frontendImageName}-${pulumi.stack}"]
```

{{% /choosable %}}

Let's see what the whole program looks like next.

## Put it all together

Now that we know how to create a container we can complete our program.

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

// Get configuration values
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");
const mongoHost = config.require("mongoHost"); // Note that strings are the default, so it's not `config.requireString`, just `config.require`.
const database = config.require("database");
const nodeEnvironment = config.require("nodeEnvironment");
const protocol = config.require("protocol")

const stack = pulumi.getStack();

// Pull the backend image
const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}Image`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});

// Pull the frontend image
const frontendImageName = "frontend";
const frontend = new docker.RemoteImage(`${frontendImageName}Image`, {
    name: "pulumi/tutorial-pulumi-fundamentals-frontend:latest",
});

// Pull the MongoDB image
const mongoImage = new docker.RemoteImage("mongoImage", {
    name: "pulumi/tutorial-pulumi-fundamentals-database-local:latest",
});

// Create a Docker network
const network = new docker.Network("network", {
    name: `services-${stack}`,
});

// Create the MongoDB container
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

// Create the backend container
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

// Create the frontend container
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
        `PORT=${frontendPort}`,
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
import pulumi
import pulumi_docker as docker

# Get configuration values
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
mongo_host = config.require("mongoHost") # Note that strings are the default, so it's not `config.require_str`, just `config.require`.
database = config.require("database")
node_environment = config.require("nodeEnvironment")
protocol = config.require("protocol")

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(f"{backend_image_name}_image",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                            )

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(f"{frontend_image_name}_image",
                              name="pulumi/tutorial-pulumi-fundamentals-frontend:latest"
                             )

# Pull the MongoDB image
mongo_image = docker.RemoteImage("mongo_image",
                                 name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
                                )

# Create a Docker network
network = docker.Network("network", name=f"services_{stack}")

# Create the MongoDB container
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

# Create the backend container
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

# Create the frontend container
frontend_container = docker.Container("frontend_container",
                                      image=frontend.repo_digest,
                                      name=f"frontend-{stack}",
                                      ports=[docker.ContainerPortArgs(
                                          internal=frontend_port,
                                          external=frontend_port
                                      )],
                                      envs=[
                                          f"PORT={frontend_port}",
                                          f"HTTP_PROXY=backend-{stack}:{backend_port}",
                                          f"PROXY_PROTOCOL={protocol}"
                                      ],
                                      networks_advanced=[docker.ContainerNetworksAdvancedArgs(
                                          name=network.name
                                      )]
                                      )

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Get configuration values
		cfg := config.New(ctx, "")
		frontendPort := cfg.RequireFloat64("frontendPort")
		backendPort := cfg.RequireFloat64("backendPort")
		mongoPort := cfg.RequireFloat64("mongoPort")
		mongoHost := cfg.Require("mongoHost") // Note that strings are the default, so it's not `cfg.RequireStr`, just `cfg.Require`
		database := cfg.Require("database")
		nodeEnvironment := cfg.Require("nodeEnvironment")
		protocol := cfg.Require("protocol")

		// Pull the backend image
		backendImageName := "backend"
		backendImage, err := docker.NewRemoteImage(ctx, fmt.Sprintf("%v-image", backendImageName), &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-backend:latest"),
		})
		if err != nil {
			return err
		}

		// Pull the frontend image
		frontendImageName := "frontend"
		frontendImage, err := docker.NewRemoteImage(ctx, fmt.Sprintf("%v-image", frontendImageName), &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-frontend:latest"),
		})
		if err != nil {
			return err
		}

		// Pull the MongoDB image
		mongoImage, err := docker.NewRemoteImage(ctx, "mongo-image", &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-database-local:latest"),
		})
		if err != nil {
			return err
		}

		// Create a Docker network
		network, err := docker.NewNetwork(ctx, "network", &docker.NetworkArgs{
			Name: pulumi.String(fmt.Sprintf("services-%v", ctx.Stack())),
		})
		if err != nil {
			return err
		}

		// Create the MongoDB container
		mongoContainer, err := docker.NewContainer(ctx, "mongo-container", &docker.ContainerArgs{
			Name:  pulumi.String(fmt.Sprintf("mongo-%v", ctx.Stack())),
			Image: mongoImage.RepoDigest,
			Ports: &docker.ContainerPortArray{
				&docker.ContainerPortArgs{
					Internal: pulumi.Int(mongoPort),
					External: pulumi.Int(mongoPort),
				},
			},
			NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
				&docker.ContainerNetworksAdvancedArgs{
					Name: network.Name,
					Aliases: pulumi.StringArray{
						pulumi.String("mongo"),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create the backend container
		// Use _ instead of a variable name since this container isn't referenced
		_, err = docker.NewContainer(ctx, "backend-container", &docker.ContainerArgs{
			Name:  pulumi.String(fmt.Sprintf("backend-%v", ctx.Stack())),
			Image: backendImage.RepoDigest,
			Ports: &docker.ContainerPortArray{
				&docker.ContainerPortArgs{
					Internal: pulumi.Int(backendPort),
					External: pulumi.Int(backendPort),
				},
			},
			Envs: pulumi.StringArray{
				pulumi.String(fmt.Sprintf("DATABASE_HOST=%v", mongoHost)),
				pulumi.String(fmt.Sprintf("DATABASE_NAME=%v", database)),
				pulumi.String(fmt.Sprintf("NODE_ENV=%v", nodeEnvironment)),
			},
			NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
				&docker.ContainerNetworksAdvancedArgs{
					Name: network.Name,
					Aliases: pulumi.StringArray{
						pulumi.String(fmt.Sprintf("backend-%v", ctx.Stack())),
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{
			mongoContainer,
		}))
		if err != nil {
			return err
		}

		// Create a frontend container
		_, err = docker.NewContainer(ctx, "frontend-container", &docker.ContainerArgs{
			Name:  pulumi.String(fmt.Sprintf("frontend-%v", ctx.Stack())),
			Image: frontendImage.RepoDigest,
			Ports: &docker.ContainerPortArray{
				&docker.ContainerPortArgs{
					Internal: pulumi.Int(frontendPort),
					External: pulumi.Int(frontendPort),
				},
			},
			Envs: pulumi.StringArray{
				pulumi.String(fmt.Sprintf("PORT=%v", frontendPort)),
				pulumi.String(fmt.Sprintf("HTTP_PROXY=backend-%v:%v", ctx.Stack(), backendPort)),
				pulumi.String(fmt.Sprintf("PROXY_PROTOCOL=%v", protocol)),
			},
			NetworksAdvanced: &docker.ContainerNetworksAdvancedArray{
				&docker.ContainerNetworksAdvancedArgs{
					Name: network.Name,
					Aliases: pulumi.StringArray{
						pulumi.String(fmt.Sprintf("frontend-%v", ctx.Stack())),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
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
        // Get configuration values
        final var config = ctx.config();
        final var frontendPort = config.requireInteger("frontendPort");
        final var backendPort = config.requireInteger("backendPort");
        final var mongoPort = config.requireInteger("mongoPort");
        final var mongoHost = config.require("mongoHost");
        final var database = config.require("database");
        final var nodeEnvironment = config.require("nodeEnvironment");
        final var protocol = config.require("protocol");

        final var stackName = ctx.stackName();

        // Create the backend image
        final String backendImageName = "backend";
        final var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );

        // Create the frontend image
        final String frontendImageName = "frontend";
        final var frontendImage = new RemoteImage(
                frontendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",frontendImageName))
                        .build()
        );

        // Create the MongoDB image
        final var mongoImage = new RemoteImage(
                "mongoImage",
                RemoteImageArgs.builder()
                        .name("pulumi/tutorial-pulumi-fundamentals-database-local:latest")
                        .build()
        );

        // Create a Docker network
        final var network = new Network(
                "network",
                NetworkArgs.builder()
                        .name(String.format("services-%s",stackName))
                        .build()
        );

        // Create the MongoDB container
        final var mongoContainer = new Container(
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

        // Create the backend container
        final var backendContainer = new Container(
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
                                String.format("NODE_ENV=%s",nodeEnvironment)
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

        // Create the frontend container
        final var frontendContainer = new Container(
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
                                String.format("PORT=%d",frontendPort),
                                String.format("HTTP_PROXY=backend-%s:%d",stackName,backendPort),
                                String.format("PROXY_PROTOCOL=%s",protocol)
                        ))
                        .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                                .name(network.name())
                                .build())
                        .build()
        );

        ctx.export("link", Output.of("http://localhost:3001"));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my_first_app
runtime: yaml
description: A minimal Pulumi YAML program

# Get configuration values
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

# Define variables
variables:
  backendImageName: backend
  frontendImageName: frontend

resources:
  # Pull the backend image
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest

  # Pull the frontend image
  frontend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-frontend:latest

  # Pull the MongoDB image
  mongo-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-database-local:latest

  # Create a Docker network
  network:
    type: docker:index:Network
    properties:
      name: services-${pulumi.stack}

  # Create the MongoDB container
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

  # Create the backend container
  backend-container:
    type: docker:index:Container
    properties:
      name: ${backendImageName}-${pulumi.stack}
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
          aliases: ["${backendImageName}-${pulumi.stack}"]
    options:
      dependsOn:
        - ${mongo-container}

  # Create the frontend container
  frontend-container:
    type: docker:index:Container
    properties:
      name: ${frontendImageName}-${pulumi.stack}
      image: ${frontend-image.repoDigest}
      ports:
        - internal: ${frontendPort}
          external: ${frontendPort}
      envs:
        [
          "PORT=${frontendPort}",
          "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
          "PROXY_PROTOCOL=${protocol}"
        ]
      networksAdvanced:
        - name: ${network.name}
          aliases: ["${frontendImageName}-${pulumi.stack}"]
outputs:       {}

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
explore the [Building with Pulumi](/learn/building-with-pulumi/) pathway.
