---
title: What are Kubernetes Secrets?
meta_desc: "Kubernetes Secrets are objects for storing sensitive data like passwords, tokens, and keys. Learn types, base64 vs encryption, and integration patterns."
meta_image: /images/what-is/what-are-kubernetes-secrets-meta.png
type: what-is
page_title: "What are Kubernetes Secrets?"
authors: ["diana-esteves"]
---

**Kubernetes Secrets are built-in API objects that store small amounts of sensitive data (passwords, API tokens, TLS keys, container registry credentials) and inject them into pods as environment variables, mounted files, or `imagePullSecrets` references.** A Secret is a namespaced resource stored in the cluster's `etcd` datastore and consumed by workloads through the Kubernetes API.

The most common point of confusion: by default, Secret values in `etcd` are **base64-encoded, not encrypted**. Base64 is reversible by anyone who can read the data, so a Secret is only as protected as the cluster's `etcd` access controls and any [encryption-at-rest configuration](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) you enable. Production clusters layer additional protection on top: an external KMS provider for encryption at rest, RBAC to limit which workloads can read which Secrets, and often an external store (HashiCorp Vault, AWS Secrets Manager, [Pulumi ESC](/product/esc/)) brokered into the cluster through the [External Secrets Operator](https://external-secrets.io/) or the [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/).

In this article, we'll cover the key questions about Kubernetes Secrets:

* What is a Kubernetes Secret used for?
* How are Kubernetes Secrets stored?
* What types of Kubernetes Secrets are there?
* How do pods consume Secrets?
* What are the limitations of Kubernetes Secrets?
* How do Secrets compare to ConfigMaps?
* How do external secret stores integrate with Kubernetes?
* How does Pulumi manage Kubernetes Secrets?
* Frequently asked questions about Kubernetes Secrets

## What is a Kubernetes Secret used for?

A Secret holds the credentials and keys a workload needs at runtime without baking them into a container image, a Git repository, or a pod spec in plain text. Typical uses:

* Database connection strings and passwords.
* API tokens for third-party services.
* TLS certificates and private keys for ingress controllers.
* Docker registry credentials so a pod can pull a private image.
* Service account tokens that pods present to the Kubernetes API.

Anything more sensitive than a feature flag or a log level belongs in a Secret rather than a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/).

## How are Kubernetes Secrets stored?

A Secret lives in `etcd`, the cluster's distributed key-value store. The path from a `kubectl create secret` command to the application that reads the value runs through several layers, each of which can be hardened separately.

| Layer | Default behavior | Production hardening |
|---|---|---|
| API submission | TLS to the API server | Same; ensure API server cert is rotated |
| Storage in etcd | **Base64-encoded only** | Enable [encryption at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) with an external KMS (AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault) |
| Access from the API | RBAC on the `secrets` resource | Default-deny RBAC; grant `get` on specific Secret names; audit-log all `secrets` reads |
| Delivery to pods | Mounted from `tmpfs` (in-memory), not written to disk | Same; avoid passing Secrets as command-line args |
| In the pod | Readable by any process in the container | Use distroless images; drop unnecessary capabilities |

The single most important hardening step is enabling encryption at rest with a KMS provider. Without it, anyone who can read `etcd` (an admin, a backup, a compromised control-plane node) can read every Secret in the cluster.

## What types of Kubernetes Secrets are there?

Secrets carry a `type` field that signals to the API server and to controllers how the data should be interpreted. The built-in types:

| Type | Purpose |
|---|---|
| `Opaque` | Arbitrary user-defined key/value data. The default and most common type. |
| `kubernetes.io/service-account-token` | Token issued for a ServiceAccount; created automatically (or via TokenRequest) and mounted into pods. |
| `kubernetes.io/dockercfg` | Legacy `~/.dockercfg` registry credentials. |
| `kubernetes.io/dockerconfigjson` | Modern `~/.docker/config.json` registry credentials. Referenced by `imagePullSecrets`. |
| `kubernetes.io/basic-auth` | Username and password for basic auth. |
| `kubernetes.io/ssh-auth` | SSH private key. |
| `kubernetes.io/tls` | TLS certificate and key. Consumed by ingress controllers and webhook configurations. |
| `bootstrap.kubernetes.io/token` | Bootstrap tokens used to join new nodes to the cluster. |

Custom types are allowed (any string with a domain prefix), but the built-ins cover almost every real use case.

## How do pods consume Secrets?

A workload reads a Secret in one of three ways:

1. **Environment variables.** Inject specific keys with `env.valueFrom.secretKeyRef`, or load all keys at once with `envFrom.secretRef`. Simple, but the values appear in process environment listings and may leak into logs.
1. **Mounted files.** Project the Secret into a volume; each key becomes a file under the mount path (for example, `/etc/secrets/db-password`). Preferred for TLS certs and anything an application reads from disk. The mount is backed by `tmpfs`, so the data never hits the node's disk.
1. **`imagePullSecrets`.** A pod-level reference that tells the kubelet which registry credentials to use when pulling images. Only used for `dockerconfigjson` Secrets.

File mounts are generally safer than env vars: less likely to be logged, easier to rotate without a restart (the kubelet updates the mounted files on a sync interval), and easier to scope through file permissions.

## What are the limitations of Kubernetes Secrets?

Secrets cover the common case but have well-known gaps that drive teams to external solutions.

* **Base64 is not encryption.** Without encryption at rest configured, anyone with `etcd` access reads every Secret.
* **No built-in versioning.** A Secret has one current value. Rolling back means re-creating it from a backup or external source.
* **No native rotation.** Kubernetes won't rotate a database password or expire an API token. Rotation has to come from an operator, an external store, or a manual process.
* **Namespace-scoped only.** No first-class way to share a Secret across namespaces without copying it (or using a third-party operator).
* **Limited audit detail.** Audit logs show that a Secret was read, but most clusters don't enable that audit level by default.
* **1 MiB size limit per Secret.** Fine for credentials, too small for large keys or files.
* **Cluster-bound.** Multi-cluster fleets need an external source of truth and a sync mechanism.

These gaps don't make Secrets unusable; they explain why most teams pair them with an external store.

## How do Secrets compare to ConfigMaps?

Both objects look similar (key/value data, namespaced, mounted as files or env vars), but they're not interchangeable.

| Aspect | Secret | ConfigMap |
|---|---|---|
| Intended for | Sensitive data | Non-sensitive configuration |
| Default storage | Base64-encoded in etcd | Plain text in etcd |
| Encryption at rest | Supported via KMS provider | Supported via KMS provider |
| Size limit | 1 MiB | 1 MiB |
| Mounted via | `tmpfs` (in-memory) | Regular file (in-memory in practice via the kubelet) |
| Visibility | Hidden from `kubectl describe` by default | Shown in `kubectl describe` |

Use Secrets for credentials, tokens, and keys. Use ConfigMaps for log levels, feature flags, application URLs, and other non-sensitive settings. Mixing the two (putting secrets in ConfigMaps to "make them easier to read") defeats the small but real protections Secrets provide.

## How do external secret stores integrate with Kubernetes?

For anything beyond a small cluster, the operating pattern is to keep the source of truth outside the cluster and project values in as native Kubernetes Secrets. Two patterns dominate.

### External Secrets Operator (ESO)

[ESO](https://external-secrets.io/) is a controller that watches `ExternalSecret` resources and synchronizes values from an external store (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager, Azure Key Vault, [Pulumi ESC](/product/esc/), and many others) into native Kubernetes Secrets. Applications keep reading regular Secrets; ESO handles fetching, rotation, and reconciliation.

### Secrets Store CSI Driver

The [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/) mounts secrets directly from an external store as files in a pod, without creating a Kubernetes Secret object at all (or, optionally, by syncing one for env-var consumption). Useful when you want secrets to live exclusively in the external store and never touch `etcd`.

| Pattern | What lands in etcd | Best for |
|---|---|---|
| **External Secrets Operator** | A normal Kubernetes Secret, materialized from the external source | Existing apps that read native Secrets; broad provider support |
| **Secrets Store CSI Driver** | Nothing (or an optionally-synced Secret) | Pods that read secrets from disk; minimizing data in etcd |
| **Vault Agent sidecar** | Nothing | Workloads with dynamic short-lived credentials |

Either approach lets teams centralize rotation, audit, and access control in one place and treat Kubernetes Secrets as a delivery mechanism rather than the system of record.

## How does Pulumi manage Kubernetes Secrets?

[Pulumi's Kubernetes provider](/registry/packages/kubernetes/) exposes `Secret` as a first-class resource. The same Pulumi program that provisions a cluster can declare its Secrets, populate them from [Pulumi ESC](/product/esc/), and roll them forward through the same review and CI pipeline as the rest of your infrastructure.

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const dbPassword = config.requireSecret("dbPassword");

const dbCreds = new k8s.core.v1.Secret("db-creds", {
    metadata: { name: "db-creds", namespace: "app" },
    type: "Opaque",
    stringData: {
        username: "app",
        password: dbPassword,
    },
});
```

A few things happen for free here:

* `config.requireSecret` pulls the value from [Pulumi ESC](/product/esc/) or a stack-level encrypted config. No plaintext credentials in the program, the state file, or Git.
* The Secret resource is reconciled like any other Kubernetes object: drift is detected, deletes are tracked, and rollouts can be coordinated with the deployments that consume the Secret.
* For external stores, Pulumi's [External Secrets](/registry/packages/kubernetes/) and provider packages let you create `ExternalSecret`, `SecretStore`, and `ClusterSecretStore` resources in code alongside the apps that depend on them.

[Get started with Pulumi for Kubernetes](/docs/iac/clouds/kubernetes/) to manage clusters, Secrets, and external-secret integrations in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Kubernetes Secrets

### Are Kubernetes Secrets encrypted?

By default, no. Secret values are base64-encoded in `etcd` (reversible, not encrypted). Encryption at rest requires explicitly configuring an `EncryptionConfiguration` on the API server, typically backed by a KMS provider (AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault). Most managed Kubernetes services (EKS, GKE, AKS) make this a one-flag setting.

### Is base64 the same as encryption?

No. Base64 is an encoding that converts binary data to a printable ASCII string. It is fully reversible without a key (`echo "cm9vdA==" | base64 -d` returns `root`). Anyone with read access to `etcd` or the API can decode any Secret.

### Who can read Kubernetes Secrets?

Any identity with `get` or `list` permission on the `secrets` resource in the relevant namespace. By default that includes cluster admins, the workloads that mount the Secret via a ServiceAccount, and any RBAC binding that grants those verbs. Audit logging and least-privilege RBAC are the standard controls.

### How do I rotate a Kubernetes Secret?

Kubernetes itself won't rotate values for you. Options: rotate the upstream credential (database password, API key) and update the Secret manually; let an operator like the External Secrets Operator pull the new value from an external store on a schedule; or use short-lived dynamic credentials (Vault, IRSA, Workload Identity) that the workload requests on demand.

### What is the size limit for a Kubernetes Secret?

1 MiB per Secret. The total etcd object size cap (~1.5 MiB) and the way Secrets are streamed to nodes make larger payloads impractical. Store large blobs (full certificate bundles, large keyfiles) in object storage and put only the reference in a Secret.

### Can I share a Secret across namespaces?

Not natively. A Secret is scoped to one namespace. Common workarounds: copy the Secret into each namespace with a controller (Reflector, Kubed); use an `ExternalSecret` per namespace pointing at the same external source; or run the consuming workload in the namespace where the Secret lives.

### How are Secrets exposed to pods at runtime?

As environment variables, as files in a `tmpfs` volume, or as `imagePullSecrets` references on the pod spec. File mounts are usually preferred: they're easier to rotate without a pod restart (the kubelet refreshes the mount on a sync interval, default 60 seconds) and harder to leak into logs.

### What is the difference between a Secret and an ExternalSecret?

A `Secret` is a native Kubernetes object that holds data in `etcd`. An `ExternalSecret` is a custom resource defined by the [External Secrets Operator](https://external-secrets.io/) that declares "fetch this value from an external store and project it as a Secret." Pods still consume a regular `Secret`; ESO is the controller that keeps it in sync.

### Should I commit Kubernetes Secret manifests to Git?

Not in plaintext. Either reference an external store ([Pulumi ESC](/product/esc/), AWS Secrets Manager, Vault) at apply time, encrypt the manifest with a tool like SOPS or sealed-secrets, or pull the values from a CI-time secret store. Committing base64 to Git is committing plaintext.

### Does Pulumi store Kubernetes Secrets in state?

Values pulled through `config.requireSecret` or [Pulumi ESC](/product/esc/) are encrypted in the Pulumi state file using your stack's encryption key (Pulumi-managed, KMS, or a passphrase). `kubectl`-style plaintext does not appear in state. See [secrets in Pulumi](/docs/iac/concepts/secrets/) for the full model.

## Learn more

Pulumi puts Kubernetes Secrets into the same review-and-CI workflow as the rest of your cluster: values come from [Pulumi ESC](/product/esc/), manifests are declared in TypeScript, Python, Go, C#, Java, or YAML, and every change is a reviewable pull request. [Get started today](/docs/get-started/).

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
* [What is Google Cloud Secret Manager?](/what-is/what-is-google-cloud-secret-manager/)
* [What are Docker Secrets?](/what-is/what-are-docker-secrets/)
