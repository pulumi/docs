---
title: "Importing via the CLI"
layout: topic
date: 2022-06-03T11:33:44-05:00
draft: false
description: Explore how to import resources as part of a migration with the Pulumi CLI
meta_desc: Explore how to import resources as part of a migration with the Pulumi CLI
index: 1
estimated_time: 10
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - terraform
---

In your quest to convert all of the older infrastructure for the Pulumipus Boba Tea Shop to Pulumi, you realized that you have some resources that are deployed using the old system. Rather than spinning those resources back up when you deploy your Pulumi program, you just want to import the state of those resources into Pulumi. While it may seem like a contrived example, it's actually a very common situation. Other teams or prior work used tools like Ansible, a CDK, or Terraform or chose to build and manage infrastructure by hand through CLIs from the cloud providers or through the web portals and UIs from various providers. Migrating to a platform like Pulumi that manages state requires either (1) replacing those resources or (2) finding a way to tell the platform about the resource's current state and tying that resource to code udpates in the future. Generally, unless a platform replaces resources regularly, it's less disruptive and more useful to leave those resources standing when moving to Pulumi.

For Pulumi, there are three paths to take when importing resources. Pulumi allows you to import resources from any currently existing system with either (1) the `import` CLI command or (2) an `import` option in the code. Alternately, we can bulk import resources from anywhere with a special JSON file and the `import` CLI command. The CLI command also offers a resource definition (code snippet) that we can add to our Pulumi program to manage the resource moving forward. Because of this bonus information, we'll explore the CLI command first.

## Setting up

The `pulumi import` command is built into the CLI, so there's nothing new to install there. However, there *are* some setup steps we need to do. First, we need to create a Pulumi project and stack for the resource to live in.

```bash
$ mkdir learn-pulumi-import
$ cd learn-pulumi-import
$ pulumi new <language> -y
```

For the provider that currently hosts that resource, we need to follow the installation and configuration information for the provider. So, for Docker, we're following [these directions].

{{< chooser language "csharp,go,java,python,typescript,yaml" >}}

{{% choosable language python %}}

If you're using the standard tooling:

```bash
$ echo "pulumi-docker" >> requirements.txt
$ source venv/bin/activate
$ pip install -r requirements.txt
```

If you're using Poetry, Pipenv, or another third-party tool, you need the `pulumi-docker` package.

{{% /choosable %}}

{{% choosable language typescript %}}

If you're using `npm`:

```bash
$ npm install @pulumi/docker
```

If you're using `yarn`:

```bash
$ yarn add @pulumi/docker
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ go get github.com/pulumi/pulumi-docker/sdk/v3
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ dotnet add package Pulumi.Docker
```

{{% /choosable %}}

{{% choosable language java %}}

If you're using Maven as your build system, update the `pom.xml` file to include the dependency:

```xml
<dependency>
    <groupId>com.pulumi</groupId>
    <artifactId>docker</artifactId>
    <version>3.2.0</version>
</dependency>
```

Then run the following command:

```bash
$ mvn validate
$ mvn clean install
```

If you're using Gradle, update the `build.gradle` file to include the depenedency:

```gradle
// ...
var pulumiDockerSdkVersion = System.getenv("PULUMI_DOCKER_PROVIDER_SDK_VERSION") ?: "3.2.0"

dependencies {
// ...
    implementation "com.pulumi:docker:$pulumiDockerSdkVersion"
}
```

Then run the following command:

```bash
$ gradle build --refresh-dependencies
```

{{% /choosable %}}

{{% choosable language yaml %}}

Since you're using YAML, there's no specific setup. We'll add the provider as part of our updates to the `Pulumi.yaml` file.

{{% /choosable %}}

{{< /chooser >}}

## Using the `import` command

Now that we have our provider set up, we can import some resources! We're going to import a `Container` resource. The first thing we have to do is figure out the **type**, **name**, and **ID** of the resource we want to import. Resources that are importable all have [a section in the API docs] that demonstrates these values. Note that, in general, the resources in a generally available provider can be imported. If it's a provider in public preview (as noted in the API docs), those resources cannot be imported yet as the maintainers are focusing on general features before moving to imports.

In the case of the Docker provider's `Container` resource, here's the sample:

```bash
$ pulumi import docker:index/container:Container foo 9a550c0f0163d39d77222d3efd58701b625d47676c25c686c95b5b92d1cba6fd
```

Here's how that example maps to what we need:

* **type**: docker:index/container:Container
* **name**: foo
* **id**: 9a550c0f0163d39d77222d3efd58701b625d47676c25c686c95b5b92d1cba6fd

We can work with this! The _type_ will be the same regardless of which container we import as that type defines the resource type that Pulumi searches for. To break it down, it's of a form of `<provider>:<namespace>:<resource>`, so we're using the `docker` provider, searching in the `index/container` namespace, and wanting the `Container` resource.

To get the _name_ and _id_, we're going to ask Docker for that information:

```bash
$ docker ps -a --no-trunc
CONTAINER ID                                                       IMAGE                                                                     COMMAND                            CREATED          STATUS                    PORTS                      NAMES
0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba   sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23   "docker-entrypoint.sh npm start"   10 minutes ago   Up 10 minutes             0.0.0.0:3001->3001/tcp     frontend-dev
a4087dbaaaa3ef75ca69fa0b871f3c9a94e5fc963ff13f62246b97bc75e20fc0   sha256:bbf5d2ba61771bdbb5208366d85e7fec004082826069f26376ebd1f8b850d2a2   "docker-entrypoint.sh npm start"   10 minutes ago   Up 10 minutes             0.0.0.0:3000->3000/tcp     backend-dev
d9c6afa03e5b0862c2368e3578cfb820df4caf8f9e4341df789fdd2c0e53081a   sha256:8c7e1d287856ec812667ffb046d78b2250b35c1c2119e9e3fddb09633bcd4982   "docker-entrypoint.sh mongod"      11 minutes ago   Up 11 minutes (healthy)   0.0.0.0:27017->27017/tcp   mongo-dev
```

So, for the first container in the list, _name_ is `frontend-dev` and _id_ is `0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba`. Let's try importing that resource! Run the following command:

```bash
$ pulumi import docker:index/container:Container frontend-dev 0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba
```

{{% notes type="warning" %}}

Remember to capitalize the resource type! If you don't, you'll get an error similar to the following one:

```bash
$ pulumi import docker:index/container:container frontend-dev 0dcb71164c20
Previewing import (dev)

View Live: https://app.pulumi.com/<org>/learn-pulumi-import/dev/previews/a4839f10-f1b3-44f3-b8dd-1c2a0c38e8d2

     Type                       Name                     Plan       Info
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  create     1 error
 =   └─ docker:index:container  frontend-dev             import     1 error

Diagnostics:
  docker:index:container (frontend-dev):
    error: Preview failed: unrecognized resource type (Read): docker:index/container:container

  pulumi:pulumi:Stack (learn-pulumi-import-dev):
    error: preview failed
```

Also, for Docker, the ID is the full ID, not the shortened one, hence the `--no-trunc` flag.

{{% /notes %}}

The output should appear something like this:

```bash
pulumi import docker:index/container:Container frontend-dev 0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba
Previewing import (dev)

View Live: https://app.pulumi.com/<org>/learn-pulumi-import/dev/previews/2ebd05d0-b37c-4e24-baa8-cf1e2f45bf3a

     Type                       Name                     Plan
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  create
 =   └─ docker:index:Container  frontend-dev             import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this import?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details
```

Let's check the details:

```bash
Do you want to perform this import? details
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:dev::learn-pulumi-import::pulumi:pulumi:Stack::learn-pulumi-import-dev]
    = docker:index/container:Container: (import) 🔒
        [id=0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba]
        [urn=urn:pulumi:dev::learn-pulumi-import::docker:index/container:Container::frontend-dev]
        [provider=urn:pulumi:dev::learn-pulumi-import::pulumi:providers:docker::default_3_2_0::04da6b54-80e4-46f7-96ec-b56ff0331ba9]
        command    : [
            [0]: "npm"
            [1]: "start"
        ]
        entrypoints: [
            [0]: "docker-entrypoint.sh"
        ]
        hostname   : "0dcb71164c20"
        image      : "sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23"
        ipcMode    : "private"
        logDriver  : "json-file"
        name       : "frontend-dev"
        networkMode: "default"
        ports      : [
            [0]: {
                external  : 3001
                internal  : 3001
            }
        ]
        shmSize    : 64
        workingDir : "/usr/src/app"
```

Notice the equal sign (=) instead of our usual plus sign (+) in the resource table and in the details? That's Pulumi's way of telling us that it's adding something to the state without modifying it. In short, it's the import sign.

And when we actually say yes to the import, here's the output:

{{% choosable language csharp %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import-csharp/dev/updates/1

     Type                       Name                            Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-csharp-dev  created
 =   └─ docker:index:Container  frontend-dev                    imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

using Pulumi;
using Docker = Pulumi.Docker;

class MyStack : Stack
{
    public MyStack()
    {
        var frontend_dev = new Docker.Container("frontend-dev", new Docker.ContainerArgs
        {
            Command =
            {
                "npm",
                "start",
            },
            Entrypoints =
            {
                "docker-entrypoint.sh",
            },
            Hostname = "0dcb71164c20",
            Image = "sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23",
            IpcMode = "private",
            LogDriver = "json-file",
            Name = "frontend-dev",
            NetworkMode = "default",
            Ports =
            {
                new Docker.Inputs.ContainerPortArgs
                {
                    External = 3001,
                    Internal = 3001,
                },
            },
            ShmSize = 64,
            WorkingDir = "/usr/src/app",
        }, new CustomResourceOptions
        {
            Protect = true,
        });
    }

}
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import-go/dev/updates/1

     Type                       Name                        Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-go-dev  created
 =   └─ docker:index:Container  frontend-dev                imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

package main

import (
	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := docker.NewContainer(ctx, "frontend-dev", &docker.ContainerArgs{
			Command: pulumi.StringArray{
				pulumi.String("npm"),
				pulumi.String("start"),
			},
			Entrypoints: pulumi.StringArray{
				pulumi.String("docker-entrypoint.sh"),
			},
			Hostname:    pulumi.String("0dcb71164c20"),
			Image:       pulumi.String("sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23"),
			IpcMode:     pulumi.String("private"),
			LogDriver:   pulumi.String("json-file"),
			Name:        pulumi.String("frontend-dev"),
			NetworkMode: pulumi.String("default"),
			Ports: ContainerPortArray{
				&ContainerPortArgs{
					External: pulumi.Int(3001),
					Internal: pulumi.Int(3001),
				},
			},
			ShmSize:    pulumi.Int(64),
			WorkingDir: pulumi.String("/usr/src/app"),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import-java/dev/updates/1

     Type                       Name                          Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-java-dev  created
 =   └─ docker:index:Container  frontend-dev                  imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

package generated_program;

import java.util.*;
import java.io.*;
import java.nio.*;
import com.pulumi.*;
import com.pulumi.resources.CustomResourceOptions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var frontend_dev = new Container("frontend-dev", ContainerArgs.builder()
            .command(
                "npm",
                "start")
            .entrypoints("docker-entrypoint.sh")
            .hostname("0dcb71164c20")
            .image("sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23")
            .ipcMode("private")
            .logDriver("json-file")
            .name("frontend-dev")
            .networkMode("default")
            .ports(ContainerPortArgs.builder()
                .external(3001)
                .internal(3001)
                .build())
            .shmSize(64)
            .workingDir("/usr/src/app")
            .build(), CustomResourceOptions.builder()
                .protect(true)
                .build());

    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import-python/dev/updates/1

     Type                       Name                            Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-python-dev  created
 =   └─ docker:index:Container  frontend-dev                    imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

import pulumi
import pulumi_docker as docker

frontend_dev = docker.Container("frontend-dev",
    command=[
        "npm",
        "start",
    ],
    entrypoints=["docker-entrypoint.sh"],
    hostname="0dcb71164c20",
    image="sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23",
    ipc_mode="private",
    log_driver="json-file",
    name="frontend-dev",
    network_mode="default",
    ports=[docker.ContainerPortArgs(
        external=3001,
        internal=3001,
    )],
    shm_size=64,
    working_dir="/usr/src/app",
    opts=pulumi.ResourceOptions(protect=True))
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/<org>/learn-pulumi-import/dev/updates/1

     Type                       Name                     Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  created
 =   └─ docker:index:Container  frontend-dev             imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

const frontend_dev = new docker.Container("frontend-dev", {
    command: [
        "npm",
        "start",
    ],
    entrypoints: ["docker-entrypoint.sh"],
    hostname: "0dcb71164c20",
    image: "sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23",
    ipcMode: "private",
    logDriver: "json-file",
    name: "frontend-dev",
    networkMode: "default",
    ports: [{
        external: 3001,
        internal: 3001,
    }],
    shmSize: 64,
    workingDir: "/usr/src/app",
}, {
    protect: true,
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import-yaml/dev/updates/1

     Type                       Name                          Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-yaml-dev  created
 =   └─ docker:index:Container  frontend-dev                  imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 2s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

resources:
  frontend-dev:
    type: docker:Container
    properties:
      command:
        - npm
        - start
      entrypoints:
        - docker-entrypoint.sh
      hostname: 0dcb71164c20
      image: sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23
      ipcMode: private
      logDriver: json-file
      name: frontend-dev
      networkMode: default
      ports:
        - external: 3001
          internal: 3001
      shmSize: 64
      workingDir: /usr/src/app
    options:
      protect: true
```

{{% /choosable %}}

Notice you'll get a code snippet (or resource definition) to add to your {{< langfile >}}.

{{% notes type="info" %}}

One thing to note here is the `protect` option (documented [in the TypeScript SDK] and [in the Python SDK]). Because we're importing this resource into state without it being in the code, the resource is protected from accidental deletion on a `pulumi destroy` to avoid tearing down a resource before the code for it has been completed. To delete the resource, you have to set that flag to `false` through the code.

[in the TypeScript SDK]: https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/#ResourceOptions-protect
[in the Python SDK]: https://www.pulumi.com/docs/reference/pkg/python/pulumi/#pulumi.ResourceOptions

{{% /notes %}}

Generally, the code snippets are reasonably helpful. In this case, however, the code snippet provided will need to be modified as the container information is all stored in the image rather than the container. Usually, the main changes to these code snippets are to use resource references and update any variables we plan to provide, along with merging it into existing Pulumi programs.

{{< chooser language "csharp,go,java,python,typescript,yaml" >}}

{{% choosable language csharp %}}

```csharp
// ...
using Docker = Pulumi.Docker;

class MyStack : Stack
{
    public MyStack()
    {
        // ...
        var frontend_dev = new Docker.Container("frontend-dev", new Docker.ContainerArgs
        {
            Envs =
            {
                $"LISTEN_PORT={FrontendPort}",
                $"HTTP_PROXY=backend-dev:{BackendPort}",
                $"PROXY_PROTOCOL={Protocol}"
            }
            Image = frontendImage.Latest,
            Name = "frontend-dev",
            NetworksAdvanced =
            {
                new Docker.Inputs.ContainerNetworksAdvancedArgs
                {
                    Name = networkName
                }
            }
            Ports =
            {
                new Docker.Inputs.ContainerPortArgs
                {
                    External = FrontendPort,
                    Internal = FrontendPort,
                },
            },
        }, new CustomResourceOptions
        {
            Protect = true,
        });
    }

}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// ...

import (
	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
// ...
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        // ...
		_, err := docker.NewContainer(ctx, "frontend-dev", &docker.ContainerArgs{
			Envs: [
                pulumi.String(fmt.Sprintf("LISTEN_PORT=%d",frontendPort)),
                pulumi.String(fmt.Sprintf("HTTP_PROXY=backend-%s:%d",stackName,backendPort)),
                pulumi.String(fmt.Sprintf("PROXY_PROTOCOL=%s",protocol))
            ]
            Image:       frontendImage.Latest,
			Name:        pulumi.String("frontend-dev"),
            NetworksAdvanced:  &ContainerNetworksAdvancedArgs{
                Name: Network.name
            },
			Ports: ContainerPortArray{
				&ContainerPortArgs{
					External: frontendPort,
					Internal: frontendPort,
				},
			},
		}, pulumi.Protect(true))
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
// ...

import java.util.*;
import java.io.*;
import java.nio.*;
// ...
import com.pulumi.resources.CustomResourceOptions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var frontend_dev = new Container("frontend-dev",
        ContainerArgs.builder()
            .envs(List.of(
                    String.format("LISTEN_PORT=%d",frontendPort),
                    String.format("HTTP_PROXY=backend-%s:%d",stackName,backendPort),
                    String.format("PROXY_PROTOCOL=%s",protocol)
            ))
            .image(frontendImage.repoDigest())
            .name("frontend-dev")
            .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                    .name(network.name())
                    .build())
            .ports(ContainerPortArgs.builder()
                    .internal(frontendPort)
                    .external(frontendPort)
                    .build())
            .build(), CustomResourceOptions.builder()
                .protect(true)
                .build());
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# ...
import pulumi_docker as docker

frontend_dev = docker.Container(
    "frontend-dev",
    envs=[
        f"LISTEN_PORT={frontend_port}",
        f"HTTP_PROXY=backend-dev:{backend_port}",
        f"PROXY_PROTOCOL={protocol}"
    ],
    image=frontend.repo_digest,
    name="frontend-dev",
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(
        name=network.name
    )]
    ports=[docker.ContainerPortArgs(
        internal=frontend_port,
        external=frontend_port
    )],
    opts=pulumi.ResourceOptions(protect=True))
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
//...
import * as docker from "@pulumi/docker";

//...

const frontend_dev = new docker.Container("frontend-dev", {
    image: frontend.repoDigest,
    name: `frontend-dev`,
    ports: [
        {
            internal: frontendPort,
            external: frontendPort,
        },
    ],
    envs: [
        `LISTEN_PORT=${frontendPort}`,
        `HTTP_PROXY=backend-dev:${backendPort}`,
        `PROXY_PROTOCOL=${protocol}`
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
}, {
    protect: true,
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
# ...
  frontend-dev:
    type: docker:index:Container
    properties:
      envs:
        [
          "LISTEN_PORT=${frontendPort}",
          "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
          "PROXY_PROTOCOL=http://"
        ]
      image: ${frontend-image.repoDigest}
      name: frontend-dev
      networksAdvanced:
        - name: ${network.name}
          aliases: ["frontend-dev"]
      ports:
        - external: ${frontendPort}
          internal: ${frontendPort}
    options:
      protect: true
```

{{% /choosable %}}

{{< /chooser >}}

<br/>
<br/>

Now, that's just adding one resource at a time. What's it like to add resources all at once in a bulk import? Onward!

[these directions]: https://www.pulumi.com/registry/packages/docker/installation-configuration/
[a section in the API docs]: https://www.pulumi.com/registry/packages/docker/api-docs/container/#import
