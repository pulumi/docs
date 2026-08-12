---
title_tag: "System Requirements | Self-Hosting Pulumi"
meta_desc: Everything a self-hosted Pulumi Cloud installation needs — compute, MySQL, object storage, OpenSearch, DNS, TLS, and license keys.
title: System requirements
h1: Self-Hosted Pulumi Cloud System Requirements
menu:
  administration:
    name: System requirements
    parent: administration-self-hosting
    weight: 2
    identifier: administration-self-hosting-system-requirements
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

Every deployment option needs the same set of things: somewhere to run three containers, a MySQL database, an object store, and DNS and TLS for two endpoints. The managed-platform installers provision most of this for you. The [bring-your-own-infrastructure](/docs/administration/self-hosting/deployment-options/byo-infra-hosted/) and [Docker Engine](/docs/administration/self-hosting/deployment-options/local-docker/) options expect you to supply it.

## Licenses

| Key | Required | Notes |
| :-- | :-- | :-- |
| `PULUMI_LICENSE_KEY` | Yes | A JWT issued by Pulumi. The service will not start without it. |
| `AG_GRID_LICENSE_KEY` | Yes | Set on the console container. |

You receive both as part of a [proof of concept](/product/self-hosted/#self-hosted-trial).

## Compute

Three containers make up an installation: the [API](/docs/administration/self-hosting/components/api/), the [console](/docs/administration/self-hosting/components/console/), and a migrations job that runs once per upgrade.

| Service | CPU | Memory |
| :-- | :-- | :-- |
| API | 2 vCPU | 4 GB |
| Console | 0.5 vCPU | 512 MB |
| Migrations | 128m | 128 MB |

The API and console are stateless, so scale the API horizontally rather than vertically. A single-host evaluation needs at least **2 CPU cores and 8 GB of memory**.

For production sizing, high availability, and per-installer configuration, see [Compute sizing](/docs/administration/self-hosting/operations/compute-sizing/).

## Database

| Requirement | Value |
| :-- | :-- |
| Engine | MySQL 8.0.x |
| Storage | 20 GB SSD minimum |
| `sql_mode` | Must include `STRICT_TRANS_TABLES` |

If you are supplying your own server rather than letting an installer provision one:

- Create a database named `pulumi` before installing. The installers do not create it.
- Grant the application user the privileges it needs:

    ```sql
    GRANT ALL PRIVILEGES ON `pulumi`.* TO 'pulumi'@'%';
    GRANT CREATE USER ON *.* TO 'pulumi'@'%' WITH GRANT OPTION;
    ```

- Enable inbound ICMP (ping) on the MySQL server. The installer's connectivity check depends on it.

{{% notes type="warning" %}}
`STRICT_TRANS_TABLES` is not a suggestion. Without it, schema migrations fail with `ALGORITHM=INPLACE is not supported. Try ALGORITHM=COPY`. Aurora MySQL 8.0 does not set it by default — see [Required sql_mode settings](/docs/administration/self-hosting/operations/database/#required-sql_mode-settings) for how to set it per engine.
{{% /notes %}}

## Object storage

| Requirement | Value |
| :-- | :-- |
| Type | S3-compatible, Azure Blob Storage, or Google Cloud Storage |
| Storage | 200 GB SSD minimum |

An installation uses separate buckets for checkpoints, policy packs, engine events, and service metadata. See [Object storage](/docs/administration/self-hosting/operations/object-storage/) for the full inventory and replication guidance.

Two requirements catch people out with non-AWS S3-compatible stores:

- Pass `endpoint=IP:PORT` and `s3ForcePathStyle=true` as query parameters on the storage endpoint.
- The store, and any proxy or ingress in front of it, must preserve the `Content-Encoding: gzip` header on responses. Stripping it returns garbled state to clients.

## Search

| Requirement | Value |
| :-- | :-- |
| Engine | OpenSearch 2.x |
| Tested versions | 2.9 and 2.11 |

Resource search needs an OpenSearch cluster, but it is not in the critical path — if the cluster is unreachable, stack updates still work and the console reports search as unavailable. See [Search](/docs/administration/self-hosting/components/search/).

## Kubernetes

The EKS, AKS, GKE, and bring-your-own-infrastructure options need a conformant Kubernetes cluster. Each installer pins the version it was validated against; see the deployment guide for the option you are using. The ECS, Docker Compose, and Docker Engine options need no Kubernetes.

## DNS and TLS

Every installation serves two endpoints from a domain you control:

- `api.<your-domain>` — the API, which the CLI and console call.
- `app.<your-domain>` — the console.

Each needs a TLS certificate. The managed-platform installers can request these for you; the others expect you to supply them.

## Network access

Ingress on 443 (and 80 redirecting to it) from CLI users and browsers, plus 8080 from the console to the API. Egress to your database on 3306, your object store, and — unless you are running [air-gapped](/docs/administration/self-hosting/airgapped/) — Docker Hub to pull images. SMTP on 25, 465, or 587 is optional and only needed for invitations and password resets.

See [Network requirements](/docs/administration/self-hosting/network/) for the full list.
