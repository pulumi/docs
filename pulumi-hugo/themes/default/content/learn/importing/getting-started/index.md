---
title: "Getting Started"
layout: topic
date: 2022-06-03T11:31:57-05:00
draft: false
description: Get set up to import resources and migrate to Pulumi in this pathway.
meta_desc: Get set up to import resources and migrate to Pulumi in this pathway.
index: 0
estimated_time: 2
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - terraform
---

Infrastructure as code, as a concept, has been around for a while. We as a community have created many tools and ecosystems to build infrastructure in a reusable, repeatable, and reliable manner. For one reason or another, you've decided to bring resources created by another tool or by hand to Pulumi. This pathway is a practical walkthrough of what you need to know to bring Pulumi into your existing ecosystem.

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
    "DATABASE_NAME=cart",
    "NODE_ENV=development"
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

Initializing the backend...

Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 2.13.0"...
- Installing kreuzwerker/docker v2.13.0...
- Installed kreuzwerker/docker v2.13.0 (self-signed, key ID 24E54F214569A8A5)

Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

$ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.backend-container will be created
  + resource "docker_container" "backend-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = [
          + "DATABASE_HOST=mongodb://mongo:27017",
          + "DATABASE_NAME=cart",
          + "NODE_ENV=development",
        ]
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "backend-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "backend-dev",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 3000
          + internal = 3000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.frontend-container will be created
  + resource "docker_container" "frontend-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = [
          + "HTTP_PROXY=backend-dev:3000",
          + "LISTEN_PORT=3001",
          + "PROXY_PROTOCOL=http://",
        ]
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "frontend-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "frontend-dev",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 3001
          + internal = 3001
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.mongo-container will be created
  + resource "docker_container" "mongo-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = (known after apply)
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "mongo-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "mongo",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 27017
          + internal = 27017
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.backend will be created
  + resource "docker_image" "backend" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-backend:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_image.frontend will be created
  + resource "docker_image" "frontend" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-frontend:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_image.mongo will be created
  + resource "docker_image" "mongo" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-database-local:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_network.network will be created
  + resource "docker_network" "network" {
      + driver      = (known after apply)
      + id          = (known after apply)
      + internal    = (known after apply)
      + ipam_driver = "default"
      + name        = "services-dev"
      + options     = (known after apply)
      + scope       = (known after apply)

      + ipam_config {
          + aux_address = (known after apply)
          + gateway     = (known after apply)
          + ip_range    = (known after apply)
          + subnet      = (known after apply)
        }
    }

Plan: 7 to add, 0 to change, 0 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.

$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.backend-container will be created
  + resource "docker_container" "backend-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = [
          + "DATABASE_HOST=mongodb://mongo:27017",
          + "DATABASE_NAME=cart",
          + "NODE_ENV=development",
        ]
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "backend-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "backend-dev",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 3000
          + internal = 3000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.frontend-container will be created
  + resource "docker_container" "frontend-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = [
          + "HTTP_PROXY=backend-dev:3000",
          + "LISTEN_PORT=3001",
          + "PROXY_PROTOCOL=http://",
        ]
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "frontend-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "frontend-dev",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 3001
          + internal = 3001
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.mongo-container will be created
  + resource "docker_container" "mongo-container" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = (known after apply)
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "mongo-dev"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

      + networks_advanced {
          + aliases = [
              + "mongo",
            ]
          + name    = "services-dev"
        }

      + ports {
          + external = 27017
          + internal = 27017
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.backend will be created
  + resource "docker_image" "backend" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-backend:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_image.frontend will be created
  + resource "docker_image" "frontend" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-frontend:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_image.mongo will be created
  + resource "docker_image" "mongo" {
      + id           = (known after apply)
      + keep_locally = false
      + latest       = (known after apply)
      + name         = "pulumi/tutorial-pulumi-fundamentals-database-local:latest"
      + output       = (known after apply)
      + repo_digest  = (known after apply)
    }

  # docker_network.network will be created
  + resource "docker_network" "network" {
      + driver      = (known after apply)
      + id          = (known after apply)
      + internal    = (known after apply)
      + ipam_driver = "default"
      + name        = "services-dev"
      + options     = (known after apply)
      + scope       = (known after apply)

      + ipam_config {
          + aux_address = (known after apply)
          + gateway     = (known after apply)
          + ip_range    = (known after apply)
          + subnet      = (known after apply)
        }
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.backend: Creating...
docker_image.mongo: Creating...
docker_network.network: Creating...
docker_image.frontend: Creating...
docker_image.mongo: Creation complete after 2s [id=sha256:8c7e1d287856ec812667ffb046d78b2250b35c1c2119e9e3fddb09633bcd4982pulumi/tutorial-pulumi-fundamentals-database-local:latest]
docker_container.mongo-container: Creating...
docker_network.network: Creation complete after 2s [id=46cebea2e4b0a63bc4e8a502b8c38dc2a0009729090c0b5d798544695b6c21d4]
docker_container.mongo-container: Creation complete after 1s [id=d9c6afa03e5b0862c2368e3578cfb820df4caf8f9e4341df789fdd2c0e53081a]
docker_image.backend: Still creating... [10s elapsed]
docker_image.frontend: Still creating... [10s elapsed]
docker_image.frontend: Still creating... [20s elapsed]
docker_image.backend: Still creating... [20s elapsed]
docker_image.frontend: Still creating... [30s elapsed]
docker_image.backend: Still creating... [30s elapsed]
docker_image.backend: Creation complete after 33s [id=sha256:bbf5d2ba61771bdbb5208366d85e7fec004082826069f26376ebd1f8b850d2a2pulumi/tutorial-pulumi-fundamentals-backend:latest]
docker_container.backend-container: Creating...
docker_container.backend-container: Creation complete after 3s [id=a4087dbaaaa3ef75ca69fa0b871f3c9a94e5fc963ff13f62246b97bc75e20fc0]
docker_image.frontend: Creation complete after 38s [id=sha256:f62880b6243361e97fc9dd5ee4def8a1bc4fd0e44b1b93660157b24b628dbe23pulumi/tutorial-pulumi-fundamentals-frontend:latest]
docker_container.frontend-container: Creating...
docker_container.frontend-container: Creation complete after 1s [id=0dcb71164c20edb491477f16028f34546bc7852351c442bab4998a015b41cfba]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```

Now that we have some resources to import, let's go explore what we can do.
