---
title_tag: Creating Docker Images | Pulumi Tutorials
title: Creating Docker Images
layout: topic
description: Use Pulumi and the Docker provider to build Docker images locally.
meta_desc: Learn how to use Pulumi and the Docker provider to create Docker images locally in this tutorial.
meta_image: meta.png
weight: 2
estimated_time: 10
aliases:
    - /learn/create-docker-images/
---

In this part, you'll create your first Pulumi _resource_. Resources in Pulumi are the basic building blocks of your infrastructure, whether that's a database
instance or a compute instance or a specific storage bucket. In Pulumi, _resource providers_ manage your resources. You can group those resources to
abstract them (such as a group of compute instances that all have the same configuration and implementation) via component resources.

In this case, the resources you're provisioning will be Docker containers and images that you build locally with Pulumi infrastructure as code. The resource provider is Docker, and you'll be using {{< langhost >}} as your _language host_, or the executor that compiles the code that you write and interprets it for Pulumi.

{{% notes type="info" %}}
Note that we're only using Docker here to make it easier to learn about Pulumi (mainly because setting up a new account on any of the cloud providers can take
some time and can introduce a lot of complexity). Most users are using one of the major cloud providers to build with Pulumi.
{{% /notes %}}

## Verify your application

Let's explore the app you'll be creating. In a browser, open the [pulumi/tutorial-pulumi-fundamentals repository](https://github.com/pulumi/tutorial-pulumi-fundamentals) on GitHub. In this repository, you'll find a `frontend`, `backend`, and `data` directory. Each directory contains a `Dockerfile` that builds the image for that portion of the application.

Let's examine the backend `Dockerfile` in `backend/Dockerfile`:

```docker
FROM node:14

# Create app directory
WORKDIR /usr/src/app

COPY ./src/package*.json ./

RUN npm install
COPY ./src .
RUN npm build
EXPOSE 3000

CMD [ "npm", "start" ]
```

This `Dockerfile` copies the REST backend into the Docker filesystem, installs the dependencies, and builds the image. Note that port 3000 must be open on your
host machine.

{{% notes type="info" %}}
For the purposes of this topic, we've already built the images. We are showing the code for the application here just for completeness; you won't actually need to do anything with this code.
{{% /notes %}}

## Pull a Docker Image with Pulumi

{{% choosable language typescript %}}

Before you start writing a Pulumi program, you need to install a resource provider. In this case, you'll need the `@pulumi/docker` provider for Node.js. Let's install the provider now:

```bash
npm install @pulumi/docker
```

{{% /choosable %}}

{{% choosable language python %}}

Before you start writing a Pulumi program, you need to install a resource provider. In this case, you'll need the `pulumi_docker` provider for Python. It's always good practice for Python to work inside a virtual environment, or venv, so let's activate our venv and use `pip` to install the
provider along with the main Pulumi package:

```bash
cd ../
source venv/bin/activate
pip3 install pulumi_docker
```

You should see output showing the provider package being installed, just like for any Python package install. Add the package to the `requirements.txt` file
by adding `pulumi_docker` on a new line at the end of the file.

{{% /choosable %}}

{{% choosable language go %}}

Before you start writing a Pulumi program, you need to install a resource provider. In this case, you'll need the `pulumi-docker` provider for Go. Add a reference to `pulumi-docker` to your `go.mod` and `main.go` files. Change the `go.mod` file so that the `require` section looks like this:

```go
require (
    github.com/pulumi/pulumi-docker/sdk/v3 v3.6.1
    github.com/pulumi/pulumi/sdk/v3 v3.44.2
)
```

Next, add it to the `import` line in `main.go`:

```go
import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
)
```

After making these changes, run `go mod tidy` in your terminal. From here, Pulumi will automatically download and install the necessary Go providers the first time we execute the Pulumi program with `pulumi preview` or `pulumi up`.

{{% /choosable %}}

{{% choosable language java %}}

Before you start writing a Pulumi program, you need to install a resource provider. In this case, you'll need the `com.pulumi:docker` provider for Java. Since we're using Gradle, you can add a reference to the provider in your build file to install it at build time. Modify `build.gradle` in the `app/` directory:

```java
plugins {
    id 'application'
}

repositories {
    maven { // The google mirror is less flaky than mavenCentral()
        url("https://maven-central.storage-download.googleapis.com/maven2/")
    }
    mavenCentral()
    mavenLocal()
}

var pulumiJavaSdkVersion = System.getenv("PULUMI_JAVA_SDK_VERSION") ?: "0.1.0"
var pulumiDockerSdkVersion = System.getenv("PULUMI_DOCKER_PROVIDER_SDK_VERSION") ?: "3.2.0"

dependencies {
    implementation "com.pulumi:pulumi:$pulumiJavaSdkVersion"
    implementation "com.pulumi:docker:$pulumiDockerSdkVersion"
}

application {
    mainClass = project.hasProperty("mainClass")
            ? project.getProperty("mainClass")
            : 'my_first_app.App'
}

```

{{% /choosable %}}

Back inside your Pulumi program, you're ready to pull your first Docker image. Remember that a Pulumi program is the code that defines the desired state of your
infrastructure using a general-purpose programming language. In this case, you're using {{< langname >}}, so the program file is {{< langfile >}}. In {{< langfile >}}, use any editor to add the following code:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

const stack = pulumi.getStack();

// Pull the backend image
const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}Image`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_docker as docker

stack = pulumi.get_stack()

# Pull the backend image
backend_image_name = "backend"
backend = docker.RemoteImage(
    f"{backend_image_name}_image",
    name="pulumi/tutorial-pulumi-fundamentals-backend:latest",
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
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Pull the backend image
        backendImageName := "backend"
        backendImage, err := docker.NewRemoteImage(ctx, fmt.Sprintf("%v-image", backendImageName), &docker.RemoteImageArgs{
			Name: pulumi.String("pulumi/tutorial-pulumi-fundamentals-backend:latest"),
		})
		if err != nil {
			return err
		}
        ctx.Export("backendDockerImage", backendImage.Name)

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

        final var stackName = ctx.stackName();

        // Pull the backend image
        final String backendImageName = "backend";
        final var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-first-app
runtime: yaml
description: A minimal Pulumi YAML program

configuration: {}
variables:     {}
resources:
  # Pull the backend image
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest
outputs:       {}
```

{{% /choosable %}}

{{% choosable language typescript %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stack` variable for later use. When we pull our backend image, we give it a name in our stack as "backendImage" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some language constructs in here like string interpolation. With Pulumi, we have access to the full language ecosystem, including built-ins and third-party libraries. Pulumi also has typing support, so you can use the tools in your favorite IDE, like auto-completion, to verify that you're using the correct types for any inputs you're using.

{{% /choosable %}}

{{% choosable language python %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stack` variable for later use. When we pull our backend image, we give it a name in our stack as "backend_image" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some Python constructs in here like f-strings (string interpolation). With Pulumi, we have access to the full language ecosystem, including third-party libraries. Pulumi also has typing support, so you can use the tools in your favorite IDE, like auto-completion, to verify that you're using the correct types for any inputs you're using.

{{% /choosable %}}

{{% choosable language go %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we pull the backend image, using the `backendImageName` variable and supplying the name of the remote image to pull. The Docker provider uses the `Name` argument to supply the name of the remote image for us to use. The `ctx.Export` statement is only there to satisfy Go's requirement that every variable defined must be referenced elsewhere; we'll end up removing it later.

Notice that we're mixing in some language constructs here like `fmt.Sprintf()`. With Pulumi, we have access to the full language ecosystem, including all the functionality found in Go's standard library. Pulumi also has typing support, so you can use the tools in your favorite IDE, like completion, to verify you're using the correct types for any inputs you're using.

{{% /choosable %}}

{{% choosable language java %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stackName` variable for later use. When we pull our backend image, we give it a name in our stack as "backend" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some language constructs in here like `String.format`. With Pulumi, we have access to the full language ecosystem, including third-party libraries. Pulumi also has typing support, so you can use the tools in your favorite IDE, like completion, to verify that you're using the correct types for any inputs you're using.

{{% /choosable %}}

{{% choosable language yaml %}}

In this file, we're defining a `RemoteImage` resource using the Docker provider. The `properties` are the arguments (or _inputs_ in Pulumi terms) that the resource takes. The Docker provider uses the `name` input to pull a remote image for us to use.

{{% /choosable %}}

Run `pulumi up`.

{{% notes type="info" %}}
Note that it make take a bit before you get any output because Docker is doing a
lot of work in the background before it connects to Pulumi. Be patient!
{{% /notes %}}

Pulumi should pull your Docker image. First, though, it
gives you a preview of the changes you'll be making to the stack and asks if the
changes appear okay to you. You'll need to reply "yes" to the prompt to actually
pull the image. After the command finishes, you will see your image if you run
the command `docker images` or `docker image ls` (depending on your preference).

Let's dig a bit deeper into the code and explore the various Pulumi concepts.
Every resource has _inputs_ and _outputs_. Inputs are values that are
provided to the resource. Outputs are the resource's properties. Note that
Pulumi can't know the output until the resource has completed provisioning as
some of those outputs are provided by the provider after everything has loaded,
booted, or otherwise has come online. More on outputs later.

In our case here, the Docker
[`RemoteImage`](/registry/packages/docker/api-docs/remoteimage) resource
takes the following inputs:

{{% choosable language python %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language typescript %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language go %}}

- a Pulumi context: typically represented by the variable `ctx`
- an unnamed string: a name for the resource we are creating
- `Name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language java %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language yaml %}}

- `name`: the name of the remote image to pull down

{{% /choosable %}}

Now that you've provisioned the first piece of infrastructure, you can continue adding the other components of the application.

## Add the frontend client and MongoDB

The application we're building includes a frontend client and a MongoDB database. You'll add them both to the program next. Add the following code after the previous fragment:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
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

{{% choosable language go %}}

Add this code at the bottom of your program, just before the last `return nil` statement:

```go
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
```

{{% /choosable %}}

{{% choosable language java %}}

```java
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
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
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
```

{{% /choosable %}}

This pulls the frontend client and the populated database images in the same way you pulled the backend image earlier.

Compare your program now to the completed program below before moving forward:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

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

If your code looks the same, great! Otherwise, update yours to match this code.

Now, run `pulumi up` to pull all of the images that we'll need.

{{% notes type="info" %}}
Note that, in the future, you don't need to run `pulumi up` in stages like this
to create your infrastructure. You can write the entire program and then run it.
We're only doing a step-by-step process here to make learning easier.
{{% /notes %}}

From here, we can move on to configuring and provisioning our containers.

{{< tutorials/stepper >}}
