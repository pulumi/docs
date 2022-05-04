---
title: "Creating Docker Images"
layout: topic
date: 2021-09-07T14:06:50-05:00
draft: false
description: Use Pulumi and the Docker provider to build Docker images locally.
meta_desc: Use Pulumi and the Docker provider to build Docker images locally.
index: 1
estimated_time: 10
meta_image: meta.png
authors:
    - sophia-parafina
    - laura-santamaria
tags:
    - fundamentals
    - docker
links:
    - text: Code Repo
      url: https://github.com/pulumi/tutorial-pulumi-fundamentals
---

In this part, we'll create our first Pulumi _resource_. Resources in Pulumi are
the basic building blocks of your infrastructure, whether that's a database
instance or a compute instance or a specific storage bucket. In Pulumi,
_resource providers_ manage your resources. You can group those resources to
abstract them (such as a group of compute instances that all have the same
configuration and implementation) via component resources.

In this case, our resources are going to be Docker containers and images that we
build locally using infrastructure as code. Our resource provider is Docker, and
we're using {{< langhost >}} as our _language host_, or the executor that compiles the
code we write and interprets it for Pulumi.

{{% notes type="info" %}}
Note that we're only using Docker here to make it easier to learn about Pulumi
(mainly because setting up a new account on any of the cloud providers can take
some time and can introduce a lot of complexity). Most users are using one of
the major cloud providers to build with Pulumi.
{{% /notes %}}

## Verify your application

Let's explore what app we're deploying on the infrastructure we're creating. Open up the [pulumi/tutorial-pulumi-fundamentals repo](https://github.com/pulumi/tutorial-pulumi-fundamentals). Let's explore the contents of the `app/` directory. There is a backend, a frontend, and a data directory. All three directories contain a `Dockerfile` that builds the application images.

Let's examine the backend `Dockerfile` in `app/backend/Dockerfile`:

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

This `Dockerfile` copies the REST backend into the Docker filesystem, installs
the dependencies, and builds the image. Note that port 3000 must be open on your
host machine.

## Build your Docker Image with Pulumi

{{% choosable language typescript %}}

Before we start writing our Pulumi program, we need to install the right
provider. In this case, we want to use the `@pulumi/docker` provider for Node.js,
our language host. Let's to install the provider now:

```bash
cd ../
npm install @pulumi/docker
```

{{% /choosable %}}

{{% choosable language python %}}

Before we start writing our Pulumi program, we need to install the right
provider. In this case, we want to use the `pulumi_docker` provider for Python,
our language host. It's always good practice for Python to work inside a virtual
environment, or venv, so let's activate our venv and use `pip` to install the
provider along with the main Pulumi package:

```bash
cd ../
source venv/bin/activate
pip3 install pulumi_docker
```

You should see output showing the provider package being installed, just like
for any Python package install. Add the package to the `requirements.txt` file
by adding `pulumi_docker` on a new line at the end of the file.

{{% /choosable %}}

{{% choosable language java %}}

Before we start writing our Pulumi program, we need to install the right providers. In this case, we want to use the `com.pulumi:docker` provider for Java, our language host. Since we're using Gradle, we'll add it to our build file, and it will get added at build time. Let's modify our `build.gradle` file in the `app/` directory:

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

var pulumiJavaSdkVersion = System.getenv("PULUMI_JAVA_SDK_VERSION") ?: "0.0.1"
var pulumiDockerSdkVersion = System.getenv("PULUMI_DOCKER_PROVIDER_SDK_VERSION") ?: "3.1.0"

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

{{% choosable language yaml %}}
{{% /choosable %}}

Back inside your Pulumi program, let's build your first Docker image. Remember
that a Pulumi program is the code that defines the desired state of your
infrastructure using a general-purpose programming language. In this case, we're
using {{< langhost >}}, so our main file is {{< langfile >}}. Inside your program's
{{< langfile >}} file, use any editor to add the following code:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

const stack = pulumi.getStack();

const backendImageName = "backend";
const backend = new docker.RemoteImage(`${backendImageName}`, {
    name: "pulumi/tutorial-pulumi-fundamentals-backend:latest",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import os
import pulumi
import pulumi_docker as docker

stack = pulumi.get_stack()

# build our backend image!
backend_image_name = "backend"
backend = docker.RemoteImage("backend",
                             name="pulumi/tutorial-pulumi-fundamentals-backend:latest"
                            )
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package my_first_app;

import com.pulumi.Context;
import com.pulumi.Exports;
import com.pulumi.Pulumi;
import com.pulumi.docker.RemoteImage;
import com.pulumi.docker.RemoteImageArgs;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static Exports stack(Context ctx) {

        final var stackName = ctx.stackName();

        final String backendImageName = "backend";
        var backendImage = new RemoteImage(
                backendImageName,
                RemoteImageArgs.builder()
                        .name(String.format("pulumi/tutorial-pulumi-fundamentals-%s:latest",backendImageName))
                        .build()
        );
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: fundamentals
runtime: yaml
description: A minimal Pulumi YAML program
resources:
  backend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-backend:latest
```

{{% /choosable %}}

{{% choosable language typescript %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stack` variable for later use. When we build our backend image, we give it a name in our stack as "backend" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some language constructs in here like `process.cwd()`.
With Pulumi, we have access to the full language ecosystem, including built-ins and
third-party libraries. Pulumi also has typing support, so you can use the tools
in your favorite IDE, like completion, to verify that you're using the correct
types for any inputs you're using. Pretty cool!

{{% /choosable %}}

{{% choosable language python %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stack` variable for later use. When we build our backend image, we give it a name in our stack as "backend" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some language constructs in here like `os.getcwd()`.
With Pulumi, we have access to the full language ecosystem, including
third-party libraries. Pulumi also has typing support, so you can use the tools
in your favorite IDE, like completion, to verify that you're using the correct
types for any inputs you're using. Pretty cool!

{{% /choosable %}}

{{% choosable language java %}}

In this file, we import the main Pulumi package and the Docker provider. Then, we figure out which stack we're operating against, and populate the `stackName` variable for later use. When we build our backend image, we give it a name in our stack as "backend" before passing some arguments to the Docker provider. The Docker provider uses the `name` argument to pull a remote image for us to use.

Notice that we're mixing in some language constructs in here like `String.format`. With Pulumi, we have access to the full language ecosystem, including third-party libraries. Pulumi also has typing support, so you can use the tools in your favorite IDE, like completion, to verify that you're using the correct types for any inputs you're using. Pretty cool!

{{% /choosable %}}

{{% choosable language yaml %}}

In this file, we're defining a `RemoteImage` resource using the Docker provider. The `properties` are the arguments (or _inputs_ in Pulumi terms) that the resource takes. The Docker provider uses the `name` input to pull a remote image for us to use.

{{% /choosable %}}

Run `pulumi up`.

{{% notes type="info" %}}
Note that it make take a bit before you get any output because Docker is doing a
lot of work in the background before it connects to Pulumi. Be patient!
{{% /notes %}}

Pulumi should build your Docker image. First, though, it
gives you a preview of the changes you'll be making to the stack and asks if the
changes appear okay to you. You'll need to reply "yes" to the prompt to actually
build the image. After the command finishes, you will see your image if you run
the command `docker images` or `docker image ls` (depending on your preference).

Let's dig a bit deeper into the code and explore the various Pulumi concepts.
Every resource has _inputs_ and _outputs_. Inputs are values that are
provided to the resource. Outputs are the resource's properties. Note that
Pulumi can't know the output until the resource has completed provisioning as
some of those outputs are provided by the provider after everything has loaded,
booted, or otherwise has come online. More on outputs later.

In our case here, the Docker
[`RemoteImage`]({{< relref "/registry/packages/docker/api-docs/remoteimage" >}}) resource
takes the following inputs:

{{% choosable language python %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language typescript %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language java %}}

- an unnamed string: a name for the resource we are creating
- `name`: the name of the remote image to pull down

{{% /choosable %}}

{{% choosable language yaml %}}

- `name`: the name of the remote image to pull down

{{% /choosable %}}

Now that we've provisioned our first piece of infrastructure, let's add the
other pieces of our application.

## Add the frontend client and MongoDB

Our application includes a frontend client and MongoDB. We'll add them to the
program, so add this code after the previous fragment.

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
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
  frontend-image:
    type: docker:index:RemoteImage
    properties:
      name: pulumi/tutorial-pulumi-fundamentals-frontend:latest
```

{{% /choosable %}}

We build the frontend client and the populated MongoDB database image the same way we built the backend.

Compare your program now to this complete program before we move forward:

{{< chooser language "typescript,python,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

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
import com.pulumi.Exports;
import com.pulumi.Pulumi;
import com.pulumi.docker.RemoteImage;
import com.pulumi.docker.RemoteImageArgs;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static Exports stack(Context ctx) {

        final var stackName = ctx.stackName();

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

If your code looks the same, great! Otherwise, update yours to match this code.

Now, run `pulumi up` to build all of the images that we'll need.

{{% notes type="info" %}}
Note that, in the future, you don't need to run `pulumi up` in stages like this
to create your infrastructure. You can write the entire program and then run it.
We're only doing a step-by-step process here to make learning easier.
{{% /notes %}}

From here, we can move on to configuring and provisioning our containers.

Onward!
