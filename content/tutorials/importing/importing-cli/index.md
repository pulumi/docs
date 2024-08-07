---
title_tag: Importing Resources with CLI | Pulumi Tutorials
title: Importing with the CLI
layout: topic
description: Explore how to import resources as part of a migration with the Pulumi CLI
meta_desc: Learn how to import resources as part of migrating to Pulumi using the Pulumi CLI approach in this tutorial.
weight: 2
estimated_time: 10
meta_image: meta.png
aliases:
    - /learn/importing/importing-cli/
---

In your quest to convert all of the older infrastructure for the Pulumipus Boba Tea Shop to Pulumi, you realized that you have some resources that are deployed using the old system. Rather than spinning those resources back up when you deploy your Pulumi program, you just want to import the state of those resources into Pulumi. While it may seem like a contrived example, it's actually a very common situation. Other teams or prior work used tools like Ansible, a CDK, or Terraform or chose to build and manage infrastructure by hand through CLIs from the cloud providers or through the web portals and UIs from various providers. Migrating to a platform like Pulumi that manages state requires either (1) replacing those resources or (2) finding a way to tell the platform about the resource's current state and tying that resource to code updates in the future. Generally, unless a platform replaces resources regularly, it's less disruptive and more useful to leave those resources standing when moving to Pulumi.

For Pulumi, there are three paths to take when importing resources. Pulumi allows you to import resources from any currently existing system with either (1) the `import` CLI command or (2) an `import` option in the code. Alternately, we can bulk import resources from anywhere with a special JSON file and the `import` CLI command. The CLI command also offers a resource definition (code snippet) that we can add to our Pulumi program to manage the resource moving forward. Because of this bonus information, we'll explore the CLI command first.

## Setting up

The `pulumi import` command is built into the CLI, so there's nothing new to install there. However, there *are* some setup steps we need to do. First, we need to create a Pulumi project and stack for the resource to live in.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```bash
$ mkdir learn-pulumi-import
$ cd learn-pulumi-import
$ pulumi new typescript --yes
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir learn-pulumi-import
$ cd learn-pulumi-import
$ pulumi new python --yes
```

{{% /choosable %}}

For the provider that currently hosts that resource, we need to follow the installation and configuration information for the provider. So, for Docker, we're following [these directions].

{{% choosable language python %}}

```bash
$ echo "pulumi-docker" >> requirements.txt
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ npm install @pulumi/docker
```

{{% /choosable %}}

## Using the `import` command

Now that we have our provider set up, we can import some resources! We're going to import a `Container` resource.

The first thing we have to do is figure out the _type_ and _id_ of the resource to import. Resources that are importable all have [a section in the API docs] that details these values. Note that, in general, the resources in a generally available provider can be imported.

In the case of the Docker provider's `Container` resource, here's the sample:

```bash
$ pulumi import docker:index/container:Container foo 9a550c0f0163d39d77222d3efd58701b625d47676c25c686c95b5b92d1cba6fd
```

Here's how that example maps to what we need:

* **type**: docker:index/container:Container
* **name**: foo
* **id**: 9a550c0f0163d39d77222d3efd58701b625d47676c25c686c95b5b92d1cba6fd

The _type_ will be the same regardless of which container we import as that type defines the resource type that Pulumi searches for. To break it down, it's of a form of `<provider>:<namespace>:<resource>`, so we're using the `docker` provider, searching in the `index/container` namespace, and wanting the `Container` resource.

To get the _id_ of the container, we'll need to query the Docker daemon:

```bash
$ docker ps -a --no-trunc
CONTAINER ID                                                       IMAGE                                                                     COMMAND                            CREATED          STATUS                    PORTS                      NAMES
0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba   sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23   "docker-entrypoint.sh npm start"   10 minutes ago   Up 10 minutes             0.0.0.0:3001->3001/tcp     frontend-dev
a4087dbaaaa3ef75ca69fa0b871f3c9a94e5fc963ff13f62246b97bc75e20fc0   sha256:bbf5d2ba61771bdbb5208366d85e7fec004082826069f26376ebd1f8b850d2a2   "docker-entrypoint.sh npm start"   10 minutes ago   Up 10 minutes             0.0.0.0:3000->3000/tcp     backend-dev
d9c6afa03e5b0862c2368e3578cfb820df4caf8f9e4341df789fdd2c0e53081a   sha256:8c7e1d287856ec812667ffb046d78b2250b35c1c2119e9e3fddb09633bcd4982   "docker-entrypoint.sh mongod"      11 minutes ago   Up 11 minutes (healthy)   0.0.0.0:27017->27017/tcp   mongo-dev
```

We'll import the first container in the list, whose _id_ starts with `0dcb711`. The _name_ argument (second one, `foo` above) is the logical name to assign to the resource once it's imported. We'll use `frontend-container` for this.

Let's try importing that resource! Run the following command:

```bash
$ pulumi import docker:index/container:Container frontend-container 0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba
```

{{% notes %}}

Resource types (e.g., `docker:index/container:Container`) are case-sensitive.

{{% /notes %}}

The output should look something like this:

```bash
$ pulumi import docker:index/container:Container frontend-container 0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba

Previewing import (dev)

     Type                       Name                     Plan
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  create
 =   └─ docker:index:Container  frontend-container       import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this import?  [Use arrows to move, type to filter]
> yes
  no
  details
```

Notice the equals sign (`=`) instead of our usual plus sign (`+`) in the resource table and in the details. That's Pulumi's way of telling us that it's adding something to the state without modifying it.

Go ahead and choose `yes` to complete the import:

{{% choosable language typescript %}}

```bash
Importing (dev)

     Type                       Name                     Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  created
 =   └─ docker:index:Container  frontend-container       imported (0.36s)

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

const frontend_container = new docker.Container("frontend-container", {
    command: [
        "npm",
        "start",
    ],
    entrypoints: ["docker-entrypoint.sh"],
    hostname: "bb9987909e97",
    image: "sha256:314b485ba1247dd1e25d407c5d059a81b27c65c27a4a3b349b03041d556e5e96",
    ipcMode: "private",
    logDriver: "json-file",
    name: "frontend-dev",
    networkMode: "bridge",
    ports: [{
        external: 3001,
        internal: 3001,
    }],
    runtime: "runc",
    shmSize: 64,
    workingDir: "/usr/src/app",
}, {
    protect: true,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
Importing (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/christian-pulumi-corp/learn-pulumi-import/dev/updates/1

     Type                       Name                     Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-dev  created
 =   └─ docker:index:Container  frontend-container       imported (0.41s)

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

frontend_container = docker.Container("frontend-container",
    command=[
        "npm",
        "start",
    ],
    entrypoints=["docker-entrypoint.sh"],
    hostname="bb9987909e97",
    image="sha256:314b485ba1247dd1e25d407c5d059a81b27c65c27a4a3b349b03041d556e5e96",
    ipc_mode="private",
    log_driver="json-file",
    name="frontend-dev",
    network_mode="bridge",
    ports=[docker.ContainerPortArgs(
        external=3001,
        internal=3001,
    )],
    runtime="runc",
    shm_size=64,
    working_dir="/usr/src/app",
    opts = pulumi.ResourceOptions(protect=True))
```

{{% /choosable %}}

Notice the CLI output contains a code snippet for a resource definition.

Copy this code and replace the contents of {{< langfile >}}, then save the file and run `pulumi up`. You should see that the update produces no changes:

```bash
$ pulumi up

Previewing update (dev)

     Type                 Name                     Plan
     pulumi:pulumi:Stack  learn-pulumi-import-dev

Resources:
    2 unchanged

Do you want to perform this update? yes

Updating (dev)

     Type                 Name                     Status
     pulumi:pulumi:Stack  learn-pulumi-import-dev

Resources:
    2 unchanged

Duration: 2s
```

{{% notes type="info" %}}

One thing to note here is the `protect` option (documented [in the TypeScript SDK] and [in the Python SDK]). Because we're importing this resource into state without it being in the code, the resource is protected from accidental deletion on a `pulumi destroy` to avoid tearing down a resource before the code for it has been completed. To delete the resource, you have to set that flag to `false` through the code.

[in the TypeScript SDK]: https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/#ResourceOptions-protect
[in the Python SDK]: https://www.pulumi.com/docs/reference/pkg/python/pulumi/#pulumi.ResourceOptions

{{% /notes %}}

The resource is now under management with Pulumi.

Now, that's just adding one resource at a time. What's it like to add resources all at once in a bulk import? Onward!

[these directions]: https://www.pulumi.com/registry/packages/docker/installation-configuration/
[a section in the API docs]: https://www.pulumi.com/registry/packages/docker/api-docs/container/#import

{{< tutorials/stepper >}}
