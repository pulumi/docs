---
title: What are Docker Secrets?
meta_desc: "Docker Secrets are encrypted, Swarm-only objects for delivering sensitive data to services as in-memory files under /run/secrets/. Learn limits and best practices."
meta_image: /images/what-is/what-are-docker-secrets-meta.png
type: what-is
page_title: "What are Docker Secrets?"
authors: ["torian-crane"]
---

**Docker Secrets are an encrypted, Swarm-only mechanism for delivering sensitive data (passwords, API tokens, TLS keys, SSH keys) to services, mounted into containers as in-memory files under `/run/secrets/`.** Secrets are stored encrypted in the Raft log on the Swarm manager nodes, encrypted in transit between nodes, and never written to a container's writable filesystem.

The biggest constraint to understand up front: Docker Secrets only work with [Docker Swarm](https://docs.docker.com/engine/swarm/) services. Standalone `docker run` containers cannot consume them. Most teams not running Swarm reach for a different solution — application-level reads from a secrets manager, Kubernetes Secrets with [External Secrets Operator](https://external-secrets.io/), or runtime injection via [Pulumi ESC](/product/esc/) — for the same problem.

In this article, we'll cover the key questions about Docker Secrets:

* What is a Docker Secret used for?
* How does Docker Secret encryption work?
* How do containers access secrets at runtime?
* What are the limits of Docker Secrets?
* How do Docker Secrets compare to other options?
* How do you create and use a Docker Secret?
* What are Docker Secrets best practices?
* How does Pulumi handle Docker Secrets?
* Frequently asked questions about Docker Secrets

## What is a Docker Secret used for?

A Docker Secret is the right place for any sensitive value a Swarm service needs at runtime that you don't want baked into the image or visible in `docker inspect`. Typical uses:

* Database passwords and connection strings.
* API tokens and OAuth client secrets.
* TLS certificates and private keys.
* SSH private keys for pulling Git repositories or reaching managed instances.
* External secret-manager bootstrap credentials.

For non-sensitive configuration (nginx config files, application settings, feature flags), use [Docker Configs](/what-is/what-are-docker-configs/) instead. Docker Configs are stored unencrypted at rest and aren't intended for sensitive data.

## How does Docker Secret encryption work?

Docker Secrets are protected at every stage of their lifecycle inside a Swarm cluster.

| Layer | Protection |
|---|---|
| At rest on managers | Encrypted in the Raft log on Swarm manager nodes |
| In transit between nodes | Encrypted via mutual TLS over the Swarm overlay |
| Delivery to workers | Sent only to nodes running a task that needs the secret |
| In the container | Mounted as an in-memory `tmpfs` file; never written to disk |
| After container stop | The `tmpfs` mount is destroyed with the container |

A secret value is delivered to a worker only when a task that needs it is scheduled there. Nodes that don't run any task referencing the secret never receive the value.

## How do containers access secrets at runtime?

Inside a container, a Docker Secret named `db_password` appears as a regular file at `/run/secrets/db_password`. The application reads it the same way it would read any file:

```bash
$ cat /run/secrets/db_password
my_secret_data
```

The mount is backed by `tmpfs`, so the value lives only in memory and disappears with the container. Applications generally read the file at startup (and re-read it on a SIGHUP if they support hot reloads) rather than caching the value.

You can choose a different mount path, ownership, or file mode at service-create time:

```bash
docker service create \
  --name api \
  --secret source=db_password,target=/secrets/db,uid=1000,gid=1000,mode=0400 \
  myorg/api:1.2.3
```

## What are the limits of Docker Secrets?

Docker Secrets have well-defined boundaries that drive most of the friction teams hit.

* **Swarm-only.** Not available to `docker run`, `docker-compose up` outside of Swarm mode, Kubernetes, ECS, or any other orchestrator.
* **500 KB maximum size** per secret. Sufficient for credentials and most TLS material; too small for large key bundles or full configuration files.
* **Immutable once created.** A secret's value can't be edited in place. Rotation means creating a new secret with a different name and updating the service to reference it.
* **No built-in rotation.** Docker doesn't expire or refresh secrets on a schedule. Rotation is your responsibility (or an integration with an external secrets manager).
* **No native versioning or audit history.** Once a secret is removed, its previous value is gone. Track secret names and update events in your IaC repo if you need a paper trail.
* **Service-scoped delivery.** A secret is only readable inside containers of services that explicitly reference it; there's no way to grant ad-hoc access to a running container.

## How do Docker Secrets compare to other options?

The right tool depends on the orchestrator and the level of integration you need.

| Mechanism | Encrypted at rest | Encrypted in transit | Rotation | Works outside Swarm |
|---|---|---|---|---|
| **Docker Secrets** | Yes | Yes | Manual (rename + redeploy) | No |
| **Docker Configs** | No | Yes | Manual | No |
| **Environment variables** | No | No | Manual | Yes |
| **[Kubernetes Secrets](/what-is/what-are-kubernetes-secrets/)** | Off by default (base64); optional KMS | Yes (TLS to API) | Via external operator | Yes |
| **External vault** ([Vault](/what-is/what-is-hashicorp-vault/), [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/)) | Yes | Yes | Built-in | Yes |
| **[Pulumi ESC](/product/esc/)** | Yes | Yes | Dynamic credentials, lease-based | Yes |

For new projects past Swarm, the typical pattern is to keep the source of truth in an external store and inject values at deploy or runtime; Docker Secrets remain the simplest option for teams already running Swarm.

## How do you create and use a Docker Secret?

The full lifecycle is short. From an initialized Swarm:

```bash
$ echo "my_secret_data" | docker secret create db_password -
ix4v0pm352e7a4idpshbrbrt4

$ docker secret ls
ID                          NAME           DRIVER    CREATED          UPDATED
ix4v0pm352e7a4idpshbrbrt4   db_password              14 seconds ago   14 seconds ago

$ docker service create --name api --secret db_password nginx:alpine

$ docker exec -it $(docker ps -qf name=api) cat /run/secrets/db_password
my_secret_data
```

With Docker Compose (v3.1+) running in Swarm mode:

```yaml
services:
  api:
    image: myorg/api:1.2.3
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

Setting `external: true` tells Compose the secret was created out of band (with `docker secret create`); otherwise Compose creates it from a file at deploy time. External-source secrets are the safer default: the secret value never lives next to your `docker-compose.yml`.

## What are Docker Secrets best practices?

* **Use Docker Secrets only for sensitive data.** Move non-sensitive configuration to [Docker Configs](/what-is/what-are-docker-configs/) so a secret's blast radius stays small.
* **Rotate by replacement.** Create a new secret (`db_password_v2`), update the service to reference it, remove the old secret once no service uses it. Don't try to mutate values in place.
* **Mount as files, not env vars.** Docker Secrets are always file-mounted; resist any temptation to copy them into environment variables, which leak into `docker inspect`, child processes, and crash logs.
* **Scope secrets to specific services.** Each service should declare only the secrets it actually needs. Don't grant a service every secret in the swarm.
* **Pull from an external store when possible.** Even with Docker Secrets, prefer pulling the source of truth from a centralized store (HashiCorp Vault, AWS Secrets Manager, [Pulumi ESC](/product/esc/)) so rotation and audit live in one place.
* **Keep an audit trail in code.** Manage `docker service create`/`docker secret create` commands through IaC, not console history. The Git log becomes the audit log.

## How does Pulumi handle Docker Secrets?

For Swarm clusters managed through Pulumi, the [Docker provider](/registry/packages/docker/) treats secrets and services as first-class resources, and [Pulumi ESC](/product/esc/) is the natural source of truth for the underlying values.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

const config = new pulumi.Config();
const dbPassword = config.requireSecret("dbPassword");

const dbSecret = new docker.Secret("db-password", {
    name: "db_password",
    data: dbPassword.apply(v => Buffer.from(v).toString("base64")),
});
```

What you get from this pattern:

* The plaintext value lives in [Pulumi ESC](/product/esc/) (or a stack-level encrypted config), never in Git or the Pulumi state file in plaintext.
* Every secret-create or service-update flows through a pull request and Pulumi's preview/apply cycle, so rotations are reviewable changes.
* For teams not on Swarm, the same Pulumi program can broker secrets directly from ESC into Kubernetes, ECS, or application runtimes.

[Get started with Pulumi](/docs/get-started/) to manage container infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Docker Secrets

### Are Docker Secrets encrypted at rest?

Yes. Secrets are encrypted in the Raft log on Swarm manager nodes. The encryption key is held by the cluster; Docker can be configured to use an external key with `docker swarm unlock`. Worker nodes only ever hold a secret in memory while a task that needs it is running.

### Can I use Docker Secrets without Docker Swarm?

No. Docker Secrets are a Swarm-only feature. Standalone `docker run` or non-Swarm `docker-compose` deployments can't use them. Common alternatives for non-Swarm environments: read from a secrets manager at startup, mount secrets via a sidecar, or use orchestrator-native primitives like [Kubernetes Secrets](/what-is/what-are-kubernetes-secrets/).

### What is the maximum size of a Docker Secret?

500 KB. Enough for nearly all credentials, API tokens, and individual TLS certs and keys. For larger payloads (full certificate bundles, signed key sets), store the payload in object storage and put only the reference and signing key in a Docker Secret.

### Where is a Docker Secret mounted inside a container?

By default, at `/run/secrets/<secret_name>`. You can override the path, file mode, and ownership at service-create time with the `target`, `mode`, `uid`, and `gid` options on `--secret`.

### How do I rotate a Docker Secret?

Create a new secret with a different name, update the referencing service(s) to use the new secret, then remove the old one once nothing references it. Docker Secrets are immutable in place, so rotation is always create-new + redeploy + delete-old.

### Are Docker Secrets visible in `docker inspect`?

No. Secret values are excluded from `docker inspect` output. References to the secret (name, ID, target path) are shown, but the value itself is only readable from inside a container that mounts it.

### Can multiple services share a single Docker Secret?

Yes. Any number of services in the same Swarm can reference the same secret. Each service declares the secret on its own `docker service create` (or its Compose definition), and Swarm delivers the value to each container that needs it.

### Should I integrate Docker Secrets with an external vault?

Often, yes. Even with Docker Secrets in Swarm, teams typically keep the source of truth in [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/), or [Pulumi ESC](/product/esc/) and project values into Swarm at deploy time. That keeps rotation, audit, and access control consistent across Swarm, Kubernetes, and standalone services.

### Are Docker Secrets a good fit for compliance?

For teams already running Swarm, yes — encryption at rest, encrypted transit, scoped delivery, and in-memory mounts cover the main control objectives auditors care about. Most compliance friction comes from the rotation and audit gaps; pairing Docker Secrets with an external vault or [Pulumi ESC](/product/esc/) closes those.

## Learn more

Pulumi treats Docker Secrets like any other resource: declared in code, reviewed in pull requests, populated from [Pulumi ESC](/product/esc/), and rolled forward through CI. [Get started today](/docs/get-started/).

Related reading:

* [What are Docker Configs?](/what-is/what-are-docker-configs/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What are Kubernetes Secrets?](/what-is/what-are-kubernetes-secrets/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
