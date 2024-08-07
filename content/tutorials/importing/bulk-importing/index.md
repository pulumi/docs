---
title_tag: Importing Resources in Bulk | Pulumi Tutorials
title: Importing in bulk
layout: topic
description: Explore how to import multiple resources into Pulumi with a JSON file.
meta_desc: Learn how to bulk import multiple resources into Pulumi with a JSON file in this tutorial.
weight: 3
estimated_time: 5
meta_image: meta.png
aliases:
    - /learn/importing/bulk-importing/
---

It's very unlikely that you only need to import a single resource. In real life, you generally have a handful or more resources to import. It's a lot nicer to import all of the resources at once instead of manually importing them one by one. Or, if you're importing them through a pipeline of some sort, you want a programmatic way of importing the resources. That's all where the bulk import command comes in.

## Importing resources in bulk

To import resources in bulk, we need to build up a JSON file that has all of the information for each resource: a `type`, a desired `name`, and an `id`. As we mentioned in the last page, the `id` is obtained from the associated service provider (Docker in our case), either through a console or a CLI. The type information is contained in the Import section of the API docs for the target resource.

For our example, here's our final JSON file for importing; it contains the IDs of the two other containers we provisioned earlier with Terraform, `backend-dev` and `mongo-dev`. Copy this code, replacing the container IDs with your own, into a new file called `resources.json` in the root of the Pulumi project containing the `frontend-container` we just imported:

```json
{
    "resources": [
        {
            "type": "docker:index/container:Container",
            "name": "backend-container",
            "id": "a4087dbaaaa3ef75ca69fa0b871f3c9a94e5fc963ff13f62246b97bc75e20fc0"
        },
        {
            "type": "docker:index/container:Container",
            "name": "mongo-container",
            "id": "d9c6afa03e5b0862c2368e3578cfb820df4caf8f9e4341df789fdd2c0e53081a"
        }
    ]
}
```

To import these resources, run `pulumi import -f <path-to-file>`:

```bash
$ pulumi import -f ./resources.json

Previewing import (dev)

     Type                       Name                     Plan
     pulumi:pulumi:Stack        learn-pulumi-import-dev
 =   ├─ docker:index:Container  backend-container        import
 =   └─ docker:index:Container  mongo-container          import

Resources:
    = 2 to import
    2 unchanged

Do you want to perform this import? yes
Importing (dev)

     Type                       Name                     Status
     pulumi:pulumi:Stack        learn-pulumi-import-dev
 =   ├─ docker:index:Container  backend-container        imported (0.33s)
 =   └─ docker:index:Container  mongo-container          imported (0.52s)

Resources:
    = 2 imported
    2 unchanged

Duration: 1s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

# Code begins here...
```

It imports the resources into your stack and offers code snippets again for all of the resources in the JSON file.

Once again, copy the generated code for the two new resources into {{< langfile >}} (adding it to what's there now), then run `pulumi up`, and see that the update produces no changes:

```bash
$ pulumi up --skip-preview

Updating (dev)

     Type                 Name                     Status
     pulumi:pulumi:Stack  learn-pulumi-import-dev

Resources:
    4 unchanged

Duration: 1s
```

What if you wanted to specify the import behavior inside of your code, maintaining control as part of your code instead of via manual commands? Let's explore! Onward!

{{< tutorials/stepper >}}
