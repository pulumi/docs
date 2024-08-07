---
title_tag: Getting Started with Migration & Imports | Pulumi Tutorials
title: Getting started
layout: topic
description: Get set up to import resources and migrate to Pulumi in this tutorial.
meta_desc: Learn how to set up your local system to get started with bringing Pulumi into your existing ecosystem in this tutorial.
weight: 1
estimated_time: 2
meta_image: meta.png
aliases:
    - /learn/importing/getting-started/
---

Infrastructure as code, as a concept, has been around for a while. We as a community have created many tools and ecosystems to build infrastructure in a reusable, repeatable, and reliable manner. For one reason or another, you've decided to bring resources created by another tool or by hand to Pulumi. This tutorial is a practical walkthrough of what you need to know to bring Pulumi into your existing ecosystem.

## Starting with some resources

Let's pretend that, in our fictional Pulumipus Boba Tea Shop company, we have some infrastructure that started out as a Terraform build. In fact, here's a small snippet of that code:

```hcl {.line-numbers}
terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "backend" {
  name         = "pulumi/tutorial-pulumi-fundamentals-backend:latest"
  keep_locally = false
}

resource "docker_image" "frontend" {
  name         = "pulumi/tutorial-pulumi-fundamentals-frontend:latest"
  keep_locally = false
}

resource "docker_image" "mongo" {
  name         = "pulumi/tutorial-pulumi-fundamentals-database-local:latest"
  keep_locally = false
}

resource "docker_network" "network" {
  name = "services-dev"
}

resource "docker_container" "mongo-container" {
  image = docker_image.mongo.latest
  name  = "mongo-dev"
  ports {
    internal = 27017
    external = 27017
  }
  networks_advanced {
    name = "services-dev"
    aliases = ["mongo"]
  }
}

resource "docker_container" "backend-container" {
  image = docker_image.backend.latest
  name  = "backend-dev"
  env   = [
    "DATABASE_HOST=mongodb://mongo:27017",
    "DATABASE_NAME=cart"
  ]
  ports {
    internal = 3000
    external = 3000
  }
  networks_advanced {
    name = "services-dev"
    aliases = ["backend-dev"]
  }
}

resource "docker_container" "frontend-container" {
  image = docker_image.frontend.latest
  name  = "frontend-dev"
  env   = [
    "LISTEN_PORT=3001",
    "HTTP_PROXY=backend-dev:3000",
    "PROXY_PROTOCOL=http://"
  ]
  ports {
    internal = 3001
    external = 3001
  }
  networks_advanced {
    name = "services-dev"
    aliases = ["frontend-dev"]
  }
}
```

We need some deployed resources to import in. To that end, if you don't have some example resources you'd rather use, get Docker up and running on your machine. To check that it's installed, run:

```bash
$ docker --version
```

To ensure Docker is running, run

```bash
$ docker ps -a
```

If you get the following error, you need to start Docker:

```bash
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

Once you've got Docker up and running, copy this example to a `main.tf` file in a new directory. Then run the following commands in that directory to stand up the resources for later:

```bash
$ terraform init
$ terraform apply

...
Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
...

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```

Now that we have some resources to import, let's go explore what we can do.

{{< tutorials/stepper >}}
