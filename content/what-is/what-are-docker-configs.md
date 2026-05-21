---
title: What are Docker Configs?
meta_desc: "Docker Configs are Swarm-only objects for storing non-sensitive config files and mounting them into services without rebuilding the image. Learn limits, use cases, and Secrets vs. Configs."
meta_image: /images/what-is/what-are-docker-configs-meta.png
type: what-is
page_title: "What are Docker Configs?"
authors: ["torian-crane"]
---

**Docker Configs are Swarm-only objects for storing non-sensitive configuration files (nginx configs, application properties, JSON/YAML settings, certificate bundles) and mounting them into service containers at a path you choose, without rebuilding the image.** Configs let you keep one generic container image and project environment-specific configuration in at deploy time.

The single most important rule: **Docker Configs are not encrypted at rest.** They're encrypted in transit between Swarm nodes (over mutual TLS) and only delivered to nodes running services that reference them, but the stored value sits in the Raft log in plaintext. For credentials, tokens, TLS keys, and anything else genuinely sensitive, use [Docker Secrets](/what-is/what-are-docker-secrets/) instead. Configs are for the config file next to the credential, not the credential itself.

In this article, we'll cover the key questions about Docker Configs:

* What is a Docker Config used for?
* How do Docker Configs and Docker Secrets compare?
* How do containers consume Docker Configs?
* What are the limits of Docker Configs?
* How do you create and use a Docker Config?
* What are Docker Configs best practices?
* How does Pulumi manage Docker Configs?
* Frequently asked questions about Docker Configs

## What is a Docker Config used for?

A Docker Config is the right place for any file an application or sidecar needs at startup that isn't sensitive but still varies by environment. Typical contents:

* `nginx.conf`, `haproxy.cfg`, and other reverse-proxy configurations.
* Application settings files (`application.properties`, `appsettings.json`, `config.yaml`).
* Public certificate bundles (CA certs, public keys).
* Feature-flag manifests and routing rules.
* Logging or telemetry configuration files.

Configs let you build a single, generic image (`myorg/api:1.2.3`) and project the per-environment configuration in at deploy time. You don't rebuild the image to change the log level; you publish a new Config and update the service.

## How do Docker Configs and Docker Secrets compare?

Configs and [Secrets](/what-is/what-are-docker-secrets/) are sibling features with the same Swarm plumbing but different security guarantees.

| Aspect | Docker Configs | Docker Secrets |
|---|---|---|
| Intended for | Non-sensitive config files | Sensitive credentials and keys |
| Encrypted at rest | **No** (plaintext in Raft log) | Yes (encrypted in Raft log) |
| Encrypted in transit | Yes (mTLS between nodes) | Yes (mTLS between nodes) |
| Default mount path | `/<config-name>` at filesystem root | `/run/secrets/<secret-name>` |
| Storage in container | Regular filesystem mount | `tmpfs` (in-memory only) |
| Maximum size | 500 KB | 500 KB |
| Immutable once attached | Yes | Yes |
| Swarm-only | Yes | Yes |

The "Encrypted at rest" row is the decision driver. Anything sensitive belongs in a Secret. Everything else (config files, public certs, routing rules) belongs in a Config and benefits from being mounted as a real on-disk file rather than tucked into the more restricted `tmpfs` mount Secrets use.

## How do containers consume Docker Configs?

Configs are mounted into a service's containers as files. By default, a Config named `nginx-config` lands at `/nginx-config` inside the container; you can choose a different path with the `target` option:

```bash
docker service create --name web \
  --config source=nginx-config,target=/etc/nginx/nginx.conf,mode=0444 \
  nginx:alpine
```

Inside the container, applications read the Config like any other file:

```bash
$ cat /etc/nginx/nginx.conf
# ... nginx configuration ...
```

Unlike Secrets (which always live in `tmpfs`), Configs are mounted onto the regular container filesystem, which is fine because their contents aren't sensitive.

## What are the limits of Docker Configs?

Docker Configs share most of the Swarm-feature boundaries that Secrets have, plus a couple specific to non-sensitive data.

* **Swarm-only.** No support outside of Swarm services. Standalone `docker run` and non-Swarm Compose can't consume them.
* **500 KB maximum size.** Large configuration bundles (multi-megabyte ML model configs, full nginx site directories) don't fit and should be packaged differently.
* **Not encrypted at rest.** Don't smuggle credentials into a Config to avoid the Secret workflow. Anything genuinely sensitive belongs in a [Docker Secret](/what-is/what-are-docker-secrets/) even if it's mixed in with a larger config file.
* **Immutable once attached.** A Config attached to a running service can't be edited in place; rotating means create-new-name + service-update + delete-old.
* **No native versioning.** Docker doesn't track config history. If you need rollback, keep the canonical version in Git and let your IaC pipeline reconcile.
* **Service-scoped delivery.** A Config is delivered only to nodes running services that reference it. Nodes without a referencing service never receive the value.

## How do you create and use a Docker Config?

Once you've initialized a Swarm (`docker swarm init`), creating and attaching a Config is short:

```bash
$ echo "This is my config data" | docker config create my-config -
j41rg08gmnx1t91l0zjnefosz

$ docker config ls
ID                          NAME        CREATED          UPDATED
j41rg08gmnx1t91l0zjnefosz   my-config   33 seconds ago   33 seconds ago

$ docker service create --name web \
    --config source=my-config,target=/etc/my-app/config.conf \
    nginx:alpine

$ docker exec -it $(docker ps -qf name=web) cat /etc/my-app/config.conf
This is my config data
```

In Docker Compose (v3.3+, Swarm mode):

```yaml
services:
  web:
    image: nginx:alpine
    configs:
      - source: nginx-config
        target: /etc/nginx/nginx.conf
        mode: 0444

configs:
  nginx-config:
    file: ./nginx.conf
```

For production deployments, prefer `external: true` and create the Config out of band so the value isn't committed alongside the Compose file (the same pattern that's recommended for Secrets).

## What are Docker Configs best practices?

* **Use Configs for non-sensitive data only.** The lack of at-rest encryption is the defining limitation. Anything genuinely sensitive belongs in a [Docker Secret](/what-is/what-are-docker-secrets/).
* **Choose explicit target paths.** Default mounts at `/<config-name>` are fine for demos but rarely match where applications actually look for configuration. Always set `target` to the canonical path your app expects.
* **Keep the source of truth in Git.** Configs are deploy artifacts; the canonical version of the file should live in your IaC repo and be checked in.
* **Treat Configs as immutable.** Roll forward with a new Config name (`nginx-config-v2`) rather than mutating values. Update the service to reference the new Config, then remove the old one once nothing depends on it.
* **Split large files.** Configs cap at 500 KB. Big bundles (full nginx site directories, large rule sets) should be broken into multiple Configs or shipped as a separate volume.
* **Watch the diff in PR review.** Because Configs are projected into services exactly as written, the Pulumi/Compose diff is also the production diff. Code review catches misconfigurations before deploy.

## How does Pulumi manage Docker Configs?

The [Pulumi Docker provider](/registry/packages/docker/) treats Configs as first-class resources, so the same program that provisions a Swarm stack can declare its Configs and the services that reference them.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";
import * as fs from "fs";

const nginxConfig = new docker.Config("nginx-config", {
    name: "nginx-config",
    data: Buffer.from(fs.readFileSync("./nginx.conf", "utf8")).toString("base64"),
});
```

A few benefits of managing Configs this way:

* The Config and the service that consumes it live in the same Pulumi program; refactoring is straightforward.
* Rotations are reviewable PRs. Renaming a Config triggers a service update with full preview output.
* For per-environment values that aren't sensitive but still vary (log levels, region settings, public endpoints), keep them in [Pulumi config](/docs/iac/concepts/config/) and template them into the Config at deploy time. Anything actually sensitive comes from [Pulumi ESC](/product/esc/) and lands in a Docker Secret instead.

[Get started with Pulumi](/docs/get-started/) to manage Swarm Configs, Secrets, and services as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Docker Configs

### Are Docker Configs encrypted?

In transit, yes — Configs travel between Swarm nodes over mutual TLS. At rest, no — they're stored in the Raft log on manager nodes without encryption. That's why Configs are explicitly for non-sensitive data; encrypted-at-rest storage is what [Docker Secrets](/what-is/what-are-docker-secrets/) provide.

### What's the difference between a Docker Config and a Docker Secret?

Same Swarm plumbing, different security guarantees. Both are mounted into containers as files, both are immutable once created, both cap at 500 KB. The differences: Secrets are encrypted at rest and mounted as `tmpfs` (in-memory); Configs are stored plaintext and mounted onto the regular filesystem. Use Configs for config files; use Secrets for credentials.

### Can I use Docker Configs without Docker Swarm?

No. Configs are a Swarm-mode feature. Standalone `docker run` and non-Swarm `docker-compose` can't consume them. For non-Swarm environments, bind-mount the file, bake it into the image, or use the orchestrator's native mechanism (`ConfigMap` in Kubernetes, for example).

### What is the maximum size of a Docker Config?

500 KB. For larger configuration bundles, either split them into multiple Configs (one per logical section) or use a shared volume to hand the data to the container.

### Where is a Docker Config mounted by default?

At the root of the container filesystem, with the Config's name as the filename — for example, a Config named `nginx-config` mounts at `/nginx-config`. Most teams override this with the `target` option to match where the application actually reads its config from (e.g., `/etc/nginx/nginx.conf`).

### How do I update a Docker Config?

You don't, in place. Create a new Config (often suffixed with a version), update the referencing service(s) to use the new Config, then remove the old one once nothing references it. The update is a service redeploy.

### Can I store TLS certificates in a Docker Config?

Public certificates yes; private keys no. The certificate itself isn't sensitive once issued. The private key is, and it belongs in a Docker Secret. A common pattern is to put the cert in a Config and the key in a Secret, then reference both from the same service.

### Should I check Docker Config contents into Git?

Yes — the source file behind a Config is just a config file. Keep the canonical version in your IaC repo and let your deployment pipeline create the Config from it. That gives you version history, code review, and rollback for free, and matches how the rest of your infrastructure is managed.

## Learn more

Pulumi manages Docker Configs and Secrets in the same program as the services that consume them. Configurable content stays in Git; sensitive content stays in [Pulumi ESC](/product/esc/); every change is a reviewable pull request. [Get started today](/docs/get-started/).

Related reading:

* [What are Docker Secrets?](/what-is/what-are-docker-secrets/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [What are Kubernetes Secrets?](/what-is/what-are-kubernetes-secrets/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
