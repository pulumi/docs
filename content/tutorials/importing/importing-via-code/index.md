---
title_tag: Importing Resources with Code | Pulumi
title: "Importing via code"
layout: topic
date: 2022-06-03T11:33:05-05:00
draft: false
description: Try importing resources with code via Pulumi's ResourceOptions.
meta_desc: Learn how to import resources as part of migrating to Pulumi using code via Pulumi's ResourceOptions in this tutorial.
index: 3
estimated_time: 10
meta_image: meta.png
aliases:
    - /learn/importing/importing-via-code/
---

So, importing via the CLI is pretty nice. However, what if you want to import resource state in your code directly? Run the code once, then you're set to go? Well, we can do that with an import call in the code itself. This call is part of the `ResourceOptions` in every SDK that Pulumi provides.

## Finding identifiers

As before, we have to get `id`s from our providers to import resources. We've done this a couple times now, so you should have it handy!

## Coding up the import

We use the `ResourceOptions` `import` key to define a key-value pair that contains the ID. Let's try importing the frontend container into a new project.

Make a new directory and initialize a new Pulumi project in your language of choice, making sure to install the Pulumi Docker provider as before. Then, referring back to the `learn-pulumi-import` project from the previous step, copy the code that was generated for the `frontend-container` resource into the new project's {{< langfile >}}. That code should look something like this:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
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

```python
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

Remove the `protect` resource option and replace it with the `import` resource option, along with the ID of your front-end container:

{{% choosable language typescript %}}

```typescript {hl_lines=[24]}
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
    import: "0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python {hl_lines=[23]}
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
    opts = pulumi.ResourceOptions(import_="0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba"))
```

Note that in the Python SDK, the `import` option is named `import_` to avoid conflicting with the reserved `import` keyword.

{{% /choosable %}}

## Running the import

Now that you have the code, actually importing the resource is one command away:

```bash
$ pulumi up

Previewing (dev)

     Type                       Name                          Plan
 +   pulumi:pulumi:Stack        learn-pulumi-import-code-dev  create
 =   └─ docker:index:Container  frontend-container            import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this update? yes
Updating (dev)

     Type                       Name                          Status
 +   pulumi:pulumi:Stack        learn-pulumi-import-code-dev  created (2s)
 =   └─ docker:index:Container  frontend-container            imported (0.53s)

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 3s
```

As before, you'll get an equals sign instead of a plus sign indicating the resource was imported without modification.

One big difference to note for this method compared to the others is that this method **does not** protect the resource automatically. From here, any subsequent action by Pulumi as a result of modification of your code will apply to the resource, including destruction if you were to remove the resource from your code.

## Moving forward

You may now remove the `import` option from the imported resource definition, as Pulumi only recognizes that option once. And you can modify the resources as you see fit in the code with every `pulumi up` or `pulumi destroy` applying to the resource as with every other one you have in your code.

{{% notes type=warning %}}

If you were following along, don't forget to tear down your stack and tear down the Terraform resources you stood up! `pulumi destroy` and `terraform destroy`

{{% /notes %}}

---

Congratulations! You've now finished this tutorial on importing resources and migrating to Pulumi! In this tutorial, you learned about importing resources via a CLI command, importing resources in bulk, and importing resources in code.

Go build new things, and watch this space for more learning experiences with Pulumi!

{{< tutorials/stepper >}}
