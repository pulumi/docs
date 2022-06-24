---
title: "Importing in Bulk"
layout: topic
date: 2022-06-15T16:19:41-05:00
draft: false
description: Explore how to import multiple resources into Pulumi with a JSON file.
meta_desc: Explore how to import multiple resources into Pulumi with a JSON file.
index: 2
estimated_time: 5
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - import
    - terraform
---

It's very unlikely that you only need to import a single resource. In real life, you generally have a handful or more resources to import. It's a lot nicer to import all of the resources at once instead of manually importing them one by one. Or, if you're importing them through a pipeline of some sort, you want a programmatic way of importing the resources. That's all where the bulk import command comes in.

## Importing resources in bulk

To import resources in bulk, we need to build up a JSON file that has all of the information for each resource: a `type`, a `name`, and an `id`. As we mentioned in the last page, the `name` and `id` are values to get from your provider, either through a console or a CLI. While there is type information in the Import section of the API docs for that resource, there's another way to get the type. Pulumi's YAML provider uses that information to provision resources, so you can flip to YAML in the docs to get the resource's type.

While there are hacky ways to get the needed information, like taking a `.tfstate` file and trimming it down as a starting point, this file is created manually most of the time.

For our example, here's our final JSON file for importing, trimmed from the `.tfstate` file and modified to add the proper types in. Note that you will have different `id` values. Copy this code (with new `id` values) to a file called `resources.json` in your project directory:

<!-- ERROR: We can't import RemoteImages apparently; the IDs aren't accepted. Original JSON for that, if it works, follows.

        {
            "type": "docker:index/remoteImage:RemoteImage",
            "name": "backend",
            "id": "sha256:bbf5d2ba61771bdbb5208366d85e7fec004082826069f26376ebd1f8b850d2a2pulumi/tutorial-pulumi-fundamentals-backend:latest"
        },
        {
            "type": "docker:index/remoteImage:RemoteImage",
            "name": "frontend",
            "id": "sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23pulumi/tutorial-pulumi-fundamentals-frontend:latest"
        },
        {
            "type": "docker:index/remoteImage:RemoteImage",
            "name": "mongo",
            "id": "sha256:8c7e1d287856ec812667ffb046d78b2250b35c1c2119e9e3fddb09633bcd4982pulumi/tutorial-pulumi-fundamentals-database-local:latest"
        },
-->

```json
{
    "resources": [
        {
            "type": "docker:index/container:Container",
            "name": "backend-container",
            "id": "1cff08113e52781b1643097c947fa4fe92139a76a020d51c4856bf73207894a2"
        },
        {
            "type": "docker:index/container:Container",
            "name": "frontend-container",
            "id": "08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468"
        },
        {
            "type": "docker:index/container:Container",
            "name": "mongo-container",
            "id": "d29716e07716c9ac8da4d0f1c5dec9baeef68996a594d043bde236d53a3c2aee"
        },
        {
            "type": "docker:index/network:Network",
            "name": "network",
            "id": "46cebea2e4b0a63bc4e8a502b8c38dc2a0009729090c0b5d798544695b6c21d4"
        }
    ]
}
```

To use this file, we run `pulumi import -f <path to json file>`.

```bash
$pulumi import -f ../resources.json
Previewing import (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import/dev/previews/e1a3e822-2d51-442f-b8e1-f2974616ede1

     Type                       Name                     Plan
     pulumi:pulumi:Stack        learn-pulumi-import-dev
 =   ├─ docker:index:Container  frontend-container       import
 =   ├─ docker:index:Container  backend-container        import
 =   ├─ docker:index:Network    network                  import
 =   └─ docker:index:Container  mongo-container          import

Resources:
    = 4 to import
    2 unchanged

Do you want to perform this import? details
  pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:dev::learn-pulumi-import::pulumi:pulumi:Stack::learn-pulumi-import-dev]
    = docker:index/container:Container: (import) 🔒
        [id=08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468]
        [urn=urn:pulumi:dev::learn-pulumi-import::docker:index/container:Container::frontend-container]
        [provider=urn:pulumi:dev::learn-pulumi-import::pulumi:providers:docker::default_3_2_0::294e4dcb-6e69-4b56-84dc-16306ee5228f]
        command    : [
            [0]: "npm"
            [1]: "start"
        ]
        entrypoints: [
            [0]: "docker-entrypoint.sh"
        ]
        hostname   : "08a181ba69e4"
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
    = docker:index/container:Container: (import) 🔒
        [id=1cff08113e52781b1643097c947fa4fe92139a76a020d51c4856bf73207894a2]
        [urn=urn:pulumi:dev::learn-pulumi-import::docker:index/container:Container::backend-container]
        [provider=urn:pulumi:dev::learn-pulumi-import::pulumi:providers:docker::default_3_2_0::294e4dcb-6e69-4b56-84dc-16306ee5228f]
        command    : [
            [0]: "npm"
            [1]: "start"
        ]
        entrypoints: [
            [0]: "docker-entrypoint.sh"
        ]
        hostname   : "1cff08113e52"
        image      : "sha256:bbf5d2ba61771bdbb5208366d85e7fec004082826069f26376ebd1f8b850d2a2"
        ipcMode    : "private"
        logDriver  : "json-file"
        name       : "backend-dev"
        networkMode: "default"
        ports      : [
            [0]: {
                external  : 3000
                internal  : 3000
            }
        ]
        shmSize    : 64
        workingDir : "/usr/src/app"
    = docker:index/container:Container: (import) 🔒
        [id=d29716e07716c9ac8da4d0f1c5dec9baeef68996a594d043bde236d53a3c2aee]
        [urn=urn:pulumi:dev::learn-pulumi-import::docker:index/container:Container::mongo-container]
        [provider=urn:pulumi:dev::learn-pulumi-import::pulumi:providers:docker::default_3_2_0::294e4dcb-6e69-4b56-84dc-16306ee5228f]
        command    : [
            [0]: "mongod"
        ]
        entrypoints: [
            [0]: "docker-entrypoint.sh"
        ]
        healthcheck: {
            tests     : [
                [0]: "CMD"
                [1]: "/usr/local/bin/docker-healthcheck.sh"
            ]
        }
        hostname   : "d29716e07716"
        image      : "sha256:8c7e1d287856ec812667ffb046d78b2250b35c1c2119e9e3fddb09633bcd4982"
        ipcMode    : "private"
        logDriver  : "json-file"
        name       : "mongo-dev"
        networkMode: "default"
        ports      : [
            [0]: {
                external  : 27017
                internal  : 27017
            }
        ]
        shmSize    : 64
    = docker:index/network:Network: (import) 🔒
        [id=46cebea2e4b0a63bc4e8a502b8c38dc2a0009729090c0b5d798544695b6c21d4]
        [urn=urn:pulumi:dev::learn-pulumi-import::docker:index/network:Network::network]
        [provider=urn:pulumi:dev::learn-pulumi-import::pulumi:providers:docker::default_3_2_0::294e4dcb-6e69-4b56-84dc-16306ee5228f]
        driver     : "bridge"
        ipamConfigs: [
            [0]: {
                gateway   : "172.18.0.1"
                subnet    : "172.18.0.0/16"
            }
        ]
        name       : "services-dev"

Do you want to perform this import? yes
Importing (dev)

View Live: https://app.pulumi.com/nimbinatus/learn-pulumi-import/dev/updates/2

     Type                       Name                     Status
     pulumi:pulumi:Stack        learn-pulumi-import-dev
 =   ├─ docker:index:Container  frontend-container       imported
 =   ├─ docker:index:Container  backend-container        imported
 =   ├─ docker:index:Network    network                  imported
 =   └─ docker:index:Container  mongo-container          imported

Resources:
    = 4 imported
    2 unchanged

Duration: 3s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

# ...
```

It imports the resources into your stack and offers code snippets again for all of the resources in the JSON file. Pretty cool!

<br/>
<br/>

What if you want to specify the import behavior inside of your code, maintaining control as part of your code instead of via manual commands? Let's explore! Onward!
