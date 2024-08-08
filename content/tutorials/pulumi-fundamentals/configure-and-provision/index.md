---
title_tag: Configuring & Provisioning Containers | Pulumi Tutorials
title: Configuring and Provisioning Containers
layout: topic
description: Configure and provision your first containers locally with Pulumi.
meta_desc: Learn how to configure and provision your first containers locally with Pulumi in this tutorial.
meta_image: meta.png
weight: 3
estimated_time: 10
aliases:
    - /learn/pulumi-fundamentals/configure-and-provision/
---

Now that you've created the application's Docker images, you can provision the application's network and containers. You'll start by adding a few configuration settings to the Pulumi program. Pulumi has first-class support for [configuring](/docs/concepts/config/) infrastructure, and that includes being able to configure multiple stacks within the same project with different values.

## Configure the application

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

Add the following configuration variables to your Pulumi program somewhere near the top, just below your `import` statements:

```typescript
// Get configuration values
const config = new pulumi.Config();
const frontendPort = config.requireNumber("frontendPort");
const backendPort = config.requireNumber("backendPort");
const mongoPort = config.requireNumber("mongoPort");
```

{{% /choosable %}}

{{% choosable language python %}}

Add the following configuration variables to your Pulumi program somewhere near the top, just below your `import` statements:

```python
# Get configuration values
config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
```

{{% /choosable %}}

You'll end up using these configuration values later, passing them as environment variables to the containers.

Your program should now match the following code:

{{< chooser language "typescript,python" />}}

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
backend = docker.RemoteImage(
    f"{backend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-backend:latest",
)

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(
    f"{frontend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-frontend:latest",
)

# Pull the MongoDB image
mongo_image = docker.RemoteImage(
    "mongo_image", name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
)
```

{{% /choosable %}}

Try and run your `pulumi up` again at this point. You should get an error that looks something like this:

```bash
Diagnostics:
  pulumi:pulumi:Stack (my-first-app-dev):
    error: Missing required configuration variable 'my-first-app:frontendPort'
        please set a value using the command `pulumi config set my-first-app:frontendPort <value>`
    error: an unhandled error occurred: <...> exited with non-zero exit code: 1
```

This is because we've specified that this config option is _required_. Recall that with Pulumi, you use a single program to define multiple stacks. Let's set
the ports for the currently selected stack (the `dev` stack), which Pulumi should remember from when you ran `pulumi new` a moment ago:

```bash
pulumi config set frontendPort 3001
pulumi config set backendPort 3000
pulumi config set mongoPort 27017
```

This set of commands creates a file in your directory called `Pulumi.dev.yaml` to store the configuration settings for this stack. The content of the file should look something like this:

```yaml
config:
  my-first-app:backendPort: "3000"
  my-first-app:frontendPort: "3001"
  my-first-app:mongoPort: "27017"
```

Now, try and rerun your Pulumi program with `pulumi up`.

Your Pulumi program should now run, but you're not actually using these newly
configured ports just yet! That's because we don't have any container resources
that use the ports; we only have image resources.

## Create a container resource

In the previous topic, we fetched three Docker images from a remote registry, one for each component of the application we're building. Now we want to create Docker containers with these images and pass the containers the configuration values we just defined. These containers will need to communicate with one another, so you'll need to create a [`Docker network`](/registry/packages/docker/api-docs/network) using a new Pulumi resource.

{{< chooser language "typescript,python" />}}

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

Next, declare a new [`Container`](/registry/packages/docker/api-docs/container) resource just below the `Network` resource, like this:

{{< chooser language "typescript,python" />}}

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
backend_container = docker.Container(
    "backend_container",
    name=f"backend-{stack}",
    image=backend.repo_digest,
    ports=[docker.ContainerPortArgs(internal=backend_port, external=backend_port)],
    envs=[
        f"DATABASE_HOST={mongo_host}",
        f"DATABASE_NAME={database}",
        f"NODE_ENV={node_environment}",
    ],
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
    opts=pulumi.ResourceOptions(depends_on=[mongo_container]),
)
```

{{% /choosable %}}

{{% choosable language typescript %}}

Notice the `Container` definition references the `repoDigest` property of the  `RemoteImage` resource. This tells Pulumi there's a dependency relationship between these two resources, so it'll know to provision the `RemoteImage` first.

Another dependency to note is the `backendContainer`'s reliance on `mongoContainer`. This is an application-level dependency --- the backend service needs to connect to the database on startup --- so we use the `dependsOn` resource option to express the dependency explicitly. If we didn't, Pulumi might attempt to provision the backend service before the database was available, and the deployment would fail.

{{% /choosable %}}

{{% choosable language python %}}

Notice the `Container` definition references the `repo_digest` property of the `RemoteImage` resource. This tells Pulumi there's a dependency relationship between these two resources, so it'll know to provision the `RemoteImage` first.

Another dependency to note is the `backend_container`'s reliance on `mongo_container`. This is an application-level dependency --- the backend service needs to connect to the database on startup --- so we use the `depends_on` resource option to express the dependency explicitly. If we didn't, Pulumi might attempt to provision the backend service before the database was available, and the deployment would fail.

{{% /choosable %}}

It's also important to note the backend container requires a few environment variables to connect to the Mongo container and configure the Node.js web service. These are set in the `backend/src/.env` file in the [tutorial-pulumi-fundamentals](https://github.com/pulumi/tutorial-pulumi-fundamentals/tree/main/backend) repository. We don't want to hardcode these values; we want them to be configurable. Like before, we can do that using `pulumi config set` on the command line:

```bash
pulumi config set mongoHost mongodb://mongo:27017
pulumi config set database cart
pulumi config set nodeEnvironment development
pulumi config set protocol http://
```

Now, add these settings to the top of your program file, just below the others:

{{< chooser language "typescript,python" />}}

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

Note that all of these settings are marked _required_. If you attempted to run `pulumi up` before setting them with `pulumi config set`, Pulumi would detect the missing values and the deployment would fail.

{{% choosable language typescript %}}

Now you'll create `Container` resources for the frontend and Mongo containers. Put the `mongoContainer` declaration just before `backendContainer`, and the `frontendContainer` declaration after `backendContainer`. Here's the code for the Mongo container:

{{% /choosable %}}

{{% choosable language python %}}

Now you'll create `Container` resources for the frontend and Mongo containers. Put the `mongo_container` declaration just before `backend_container`, and the
`frontend_container` declaration after `backend_container`. Here's the code for the Mongo container:

{{% /choosable %}}

{{< chooser language "typescript,python" />}}

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
mongo_container = docker.Container(
    "mongo_container",
    image=mongo_image.repo_digest,
    name=f"mongo-{stack}",
    ports=[docker.ContainerPortArgs(internal=mongo_port, external=mongo_port)],
    networks_advanced=[
        docker.ContainerNetworksAdvancedArgs(name=network.name, aliases=["mongo"])
    ],
)
```

{{% /choosable %}}

And the code for the frontend container:

{{< chooser language "typescript,python" />}}

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
frontend_container = docker.Container(
    "frontend_container",
    image=frontend.repo_digest,
    name=f"frontend-{stack}",
    ports=[docker.ContainerPortArgs(internal=frontend_port, external=frontend_port)],
    envs=[
        f"PORT={frontend_port}",
        f"HTTP_PROXY=backend-{stack}:{backend_port}",
        f"PROXY_PROTOCOL={protocol}",
    ],
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
)
```

{{% /choosable %}}

Let's see what the whole program looks like next.

## Put it all together

Now that we know how to create a container we can complete our program.

{{< chooser language "typescript,python" />}}

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
mongo_host = config.require("mongoHost")  # Note that strings are the default, so it's not `config.require_str`, just `config.require`.
database = config.require("database")
node_environment = config.require("nodeEnvironment")
protocol = config.require("protocol")

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(
    f"{backend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-backend:latest",
)

# Pull the frontend image
frontend_image_name = "frontend"
frontend = docker.RemoteImage(
    f"{frontend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-frontend:latest",
)

# Pull the MongoDB image
mongo_image = docker.RemoteImage(
    "mongo_image", name="pulumi/tutorial-pulumi-fundamentals-database-local:latest"
)

# Create a Docker network
network = docker.Network("network", name=f"services_{stack}")

# Create the MongoDB container
mongo_container = docker.Container(
    "mongo_container",
    image=mongo_image.repo_digest,
    name=f"mongo-{stack}",
    ports=[docker.ContainerPortArgs(internal=mongo_port, external=mongo_port)],
    networks_advanced=[
        docker.ContainerNetworksAdvancedArgs(name=network.name, aliases=["mongo"])
    ],
)

# Create the backend container
backend_container = docker.Container(
    "backend_container",
    name=f"backend-{stack}",
    image=backend.repo_digest,
    ports=[docker.ContainerPortArgs(internal=backend_port, external=backend_port)],
    envs=[
        f"DATABASE_HOST={mongo_host}",
        f"DATABASE_NAME={database}",
        f"NODE_ENV={node_environment}",
    ],
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
    opts=pulumi.ResourceOptions(depends_on=[mongo_container]),
)

# Create the frontend container
frontend_container = docker.Container(
    "frontend_container",
    image=frontend.repo_digest,
    name=f"frontend-{stack}",
    ports=[docker.ContainerPortArgs(internal=frontend_port, external=frontend_port)],
    envs=[
        f"PORT={frontend_port}",
        f"HTTP_PROXY=backend-{stack}:{backend_port}",
        f"PROXY_PROTOCOL={protocol}",
    ],
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
)
```

{{% /choosable %}}

With Docker networking, you can use image names to refer to a container by name. In this application, the React frontend sends requests to the Express backend service. The URL for the backend service is configured via the `setupProxy.js` file in `app/frontend/src` via the `HTTP_PROXY` environment variable.

Run `pulumi up` to get the application running. Open a browser to `http://localhost:3001` and you should see that the Boba Tea shop is now deployed. Well done!

## Clean up

Whenever you're working on learning something new with Pulumi, it's always a good idea to clean up any resources you've created so you don't get charged for cloud resources you no longer need. Let's do that now.

Run `pulumi destroy` to remove everything in the stack:

```bash
$ pulumi destroy
Previewing destroy (dev)

View in Browser: https://app.pulumi.com/<org>/<project>/<stack>/previews/<build-id>

...
Do you want to perform this destroy? yes
Destroying (dev)

View in Browser: https://app.pulumi.com/<org>/<project>/<stack>/updates/<update-id>

...

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run 'pulumi stack rm dev'.
```

That's it! That last comment you see in the output notes that the stack and all of the configuration and history will stay
in your dashboard in Pulumi Cloud ([app.pulumi.com](https://app.pulumi.com/)). For now, that's okay. We'll talk
more about removing the project from your history in another tutorial.

---

Congratulations! You've completed the Pulumi Fundamentals tutorial. You learned how to create a Pulumi project; work on your Pulumi program to build Docker images, containers, and networks; and deploy the infrastructure locally with your first resource provider. Now, [head back to the main page](/tutorials/) and explore a few other tutorials to understand more about Pulumi. The best next step to take is to dive into the [Building with Pulumi](/tutorials/building-with-pulumi/) tutorial.

{{< tutorials/stepper >}}
