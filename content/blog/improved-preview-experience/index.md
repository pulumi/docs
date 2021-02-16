---
title: "Improved Pulumi Previews"
date: 2020-10-29
draft: false
meta_desc: "Announcing a significant improvement to the pulumi preview experience."
meta_image: preview_update.png 
authors:
    - paul-stack
tags:
    - enhancement
    - pulumi
---

Today we are announcing a minor but significant improvement to the Pulumi [preview]({{< relref "/docs/reference/cli/pulumi_preview" >}})
experience.

<!--more-->

## Change in Behaviour

We can look at a sample Pulumi application that creates a Google GKE cluster. Pulumi then deploys an application into the
Kubernetes cluster.

```typescript
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const name = "helloworld";

const config = new pulumi.Config();
export const masterVersion = config.get("masterVersion") ||
    gcp.container.getEngineVersions().then(it => it.latestMasterVersion);

// Create a GKE cluster
const cluster = new gcp.container.Cluster(name, {
    // We can't create a cluster with no node pool defined, but we want to only use
    // separately managed node pools. So we create the smallest possible default
    // node pool and immediately delete it.
    initialNodeCount: 1,
    removeDefaultNodePool: true,

    minMasterVersion: masterVersion,
    resourceLabels: {
        "stack": pulumi.getStack()
    },
});

const nodePool = new gcp.container.NodePool(`primary-node-pool`, {
    cluster: cluster.name,
    initialNodeCount: 2,
    location: cluster.location,
    nodeConfig: {
        preemptible: true,
        machineType: "n1-standard-1",
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ],
    },
    version: masterVersion,
    management: {
        autoRepair: true,
    },
}, {
    dependsOn: [cluster],
});

const clusterName = cluster.name;

// Manufacture a GKE-style kubeconfig. Note that this is slightly "different"
// because of the way GKE requires gcloud to be in the picture for cluster
// authentication (rather than using the client cert/key directly).
export const kubeconfig = pulumi.
    all([ cluster.name, cluster.endpoint, cluster.masterAuth ]).
    apply(([ name, endpoint, masterAuth ]) => {
        const context = `${gcp.config.project}_${gcp.config.zone}_${name}`;
        return `apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: ${masterAuth.clusterCaCertificate}
    server: https://${endpoint}
  name: ${context}
contexts:
- context:
    cluster: ${context}
    user: ${context}
  name: ${context}
current-context: ${context}
kind: Config
preferences: {}
users:
- name: ${context}
  user:
    auth-provider:
      config:
        cmd-args: config config-helper --format=json
        cmd-path: gcloud
        expiry-key: '{.credential.token_expiry}'
        token-key: '{.credential.access_token}'
      name: gcp
`;
    });

// Create a Kubernetes provider instance that uses our cluster from above.
const clusterProvider = new k8s.Provider(name, {
    kubeconfig: kubeconfig,
}, {
  dependsOn: [nodePool],
});

// Create a Kubernetes Namespace
const ns = new k8s.core.v1.Namespace(name, {}, { provider: clusterProvider });
const namespaceName = ns.metadata.name;

// Create a NGINX Deployment
const appLabels = { appClass: name };
const deployment = new k8s.apps.v1.Deployment(name,
    {
        metadata: {
            namespace: namespaceName,
            labels: appLabels,
        },
        spec: {
            replicas: 1,
            selector: { matchLabels: appLabels },
            template: {
                metadata: {
                    labels: appLabels,
                },
                spec: {
                    containers: [
                        {
                            name: name,
                            image: "nginx:latest",
                            ports: [{ name: "http", containerPort: 80 }],
                        },
                    ],
                },
            },
        },
    },
    {
        provider: clusterProvider,
    },
);

// Create a LoadBalancer Service for the NGINX Deployment
const service = new k8s.core.v1.Service(name,
    {
        metadata: {
            labels: appLabels,
            namespace: namespaceName,
        },
        spec: {
            type: "LoadBalancer",
            ports: [{ port: 80, targetPort: "http" }],
            selector: appLabels,
        },
    },
    {
        provider: clusterProvider,
    },
);
```

A simple change to the labels for the GKE cluster led to a preview that suggested that the dependent resources would need to be replaced.

```
     Type                              Name                         Plan        Info
     pulumi:pulumi:Stack               gcp-ts-gke-hello-world-dev2
 ~   ├─ gcp:container:Cluster          helloworld                   update      [diff: ~resourceLabels]
 +-  ├─ gcp:container:NodePool         primary-node-pool            replace     [diff: ~location]
 +-  ├─ pulumi:providers:kubernetes    helloworld                   replace     [diff: ~kubeconfig]
 +-  ├─ kubernetes:core/v1:Namespace   helloworld                   replace     [diff: -metadata~provider]
 +-  ├─ kubernetes:core/v1:Service     helloworld                   replace     [diff: ~metadata,provider]
 +-  └─ kubernetes:apps/v1:Deployment  helloworld                   replace     [diff: ~metadata,provider]

Resources:
    ~ 1 to update
    +-5 to replace
    6 changes. 1 unchanged
```

The result of the Pulumi apply showed that only the `gcp:container:Cluster` changed, and no other Kubernetes resources were replaced. This is because Pulumi
was trying to be conservative and let you know what "could" happen. It was calculating that changes to the cluster could potentially lead to the outputs changing
which other resource rely on. In practice, that wasn't going to happen. Pulumi previously had to be conservative for correctness because it didn't have a way to check.

```
     Type                      Name                         Status      Info
     pulumi:pulumi:Stack       gcp-ts-gke-hello-world-dev2
 ~   └─ gcp:container:Cluster  helloworld                   updated     [diff: ~resourceLabels]

Resources:
    ~ 1 updated
    6 unchanged
```

Pulumi now supports asking the individual resource providers about what outputs will change as part of an update to a resource.
This allows the providers (like the GCP provider in this case) to give more specific information, which allows Pulumi to provide more accurate previews:

```
     Type                      Name                         Plan       Info
     pulumi:pulumi:Stack       gcp-ts-gke-hello-world-dev2
 ~   └─ gcp:container:Cluster  helloworld                   update     [diff: ~resourceLabels]

Resources:
    ~ 1 to update
    6 unchanged
```

## Conclusion

The improved preview is available in Pulumi v2.12.0 and is supported in all new provider releases.
If you would like to disable this new behaviour and preserve the previous, more conservative behaviour, you can set an
environment variable `PULUMI_DISABLE_PROVIDER_PREVIEW` to a truthy value (`1` or `true`).
