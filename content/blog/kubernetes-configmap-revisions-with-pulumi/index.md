---
title: "Implementing Kubernetes ConfigMap Revisions with Pulumi and Argo Rollouts"
h1: "How we implemented ConfigMap revisions in Kubernetes using Pulumi and Argo Rollouts"
date: "2025-07-03"
meta_desc: "Learn how to implement ConfigMap revisions in Kubernetes using Pulumi's ConfigMapPatch and owner references with ReplicaSets to leverage Kubernetes garbage collection."
meta_image: meta.png
authors: ["matan-baruch"]
tags: ["kubernetes", "pulumi", "configmap", "argo-rollouts", "canary-deployment"]
---

ConfigMaps in Kubernetes don't have built-in revision support,
which can create challenges when deploying applications with canary strategies.
When using Argo Rollouts with AWS Spot instances,
ConfigMap deletions during canary deployments can cause older pods to fail when they try to reload configuration.
We solved this by implementing a custom ConfigMap revision system
using Pulumi's ConfigMapPatch and Kubernetes owner references.

<!--more-->

## The Problem

When deploying applications to Kubernetes using canary strategies with Argo Rollouts,
we encountered a specific challenge:

1. **Pulumi's ConfigMap suffix behavior**: By default,
   Pulumi adds a suffix to ConfigMap names when the content changes
2. **Canary deployment issues**: During canary deployments,
   the old ConfigMap gets deleted,
   but older pods (especially on AWS Spot instances that can be replaced during canary) may fail to reload
3. **No native revision support**: Neither Kubernetes nor Pulumi natively supports ConfigMap revisions like they do for deployments

## The solution: ConfigMap revisions with owner references

Our solution leverages Kubernetes' garbage collection mechanism
by using owner references to tie ConfigMaps to ReplicaSets created during canary deployments.

### Key components

1. **Pulumi's ConfigMapPatch**: Patches existing ConfigMaps with owner references
2. **ReplicaSet Owner References**: Links ConfigMaps to ReplicaSets for automatic cleanup
3. **Kubernetes Garbage Collection**: Automatically cleans up ConfigMaps when ReplicaSets are deleted
4. **Retain on Delete**: Protects ConfigMaps from immediate deletion during Pulumi updates

### Implementation

Here's how we implemented this solution in our rollout component:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as k8sClient from "@kubernetes/client-node";

interface RolloutComponentArgs {
    namespace: string;
    configMapPatch?: boolean;
    kubeconfig: pulumi.Output<any>;
    configMapName: pulumi.Output<string>;
    rolloutSpec: k8s.types.input.apiextensions.CustomResourceArgs["spec"];
}

export class ConfigMapRevisionRollout extends pulumi.ComponentResource {
    public readonly rollout: k8s.apiextensions.CustomResource;
    
    constructor(
        name: string, 
        args: RolloutComponentArgs, 
        opts?: pulumi.ComponentResourceOptions
    ) {
        super("pulumi:component:ConfigMapRevisionRollout", name, {}, opts);

        // Create the Argo Rollout using CustomResource
        this.rollout = new k8s.apiextensions.CustomResource(
            `${name}-rollout`,
            {
                apiVersion: "argoproj.io/v1alpha1",
                kind: "Rollout",
                metadata: {
                    name: name,
                    namespace: args.namespace,
                },
                spec: args.rolloutSpec,
            },
            { parent: this, ...opts }
        );

        // Apply ConfigMap revision patching if enabled
        if (args.configMapPatch) {
            this.setupConfigMapRevisions(name, args);
        }

        this.registerOutputs({
            rollout: this.rollout,
        });
    }

    private setupConfigMapRevisions(name: string, args: RolloutComponentArgs): void {
        pulumi
            .all([args.kubeconfig, args.configMapName])
            .apply(async ([kubeconfig, configMapName]) => {
                try {
                    // Create Server-Side Apply enabled provider
                    const ssaProvider = new k8s.Provider(`${name}-ssa-provider`, {
                        kubeconfig: JSON.stringify(kubeconfig),
                        enableServerSideApply: true,
                    });

                    // Wait for rollout to stabilize and create ReplicaSets
                    await this.waitForRolloutStabilization();

                    // Get ReplicaSets associated with this rollout
                    const replicaSets = await this.getAssociatedReplicaSets(
                        args.namespace,
                        configMapName,
                        kubeconfig
                    );

                    if (replicaSets.length === 0) {
                        pulumi.log.warn("No ReplicaSets found for ConfigMap patching");
                        return;
                    }

                    // Create owner references for the ConfigMap
                    const ownerReferences = replicaSets.map(rs => ({
                        apiVersion: "apps/v1",
                        kind: "ReplicaSet",
                        name: rs.metadata?.name!,
                        uid: rs.metadata?.uid!,
                        controller: false,
                        blockOwnerDeletion: false,
                    }));

                    // Patch the ConfigMap with owner references
                    new k8s.core.v1.ConfigMapPatch(
                        `${configMapName}-revision-patch`,
                        {
                            metadata: {
                                name: configMapName,
                                namespace: args.namespace,
                                ownerReferences: ownerReferences,
                                annotations: {
                                    "pulumi.com/patchForce": "true",
                                    "configmap.kubernetes.io/revision-managed": "true",
                                },
                            },
                        },
                        {
                            provider: ssaProvider,
                            retainOnDelete: true,
                            parent: this,
                        }
                    );

                    pulumi.log.info(
                        `Successfully patched ConfigMap ${configMapName} with ${ownerReferences.length} owner references`
                    );
                } catch (error) {
                    pulumi.log.error(`Failed to setup ConfigMap revisions: ${error}`);
                    throw error;
                }
            });
    }

    private async waitForRolloutStabilization(): Promise<void> {
        // Wait for rollout to create and stabilize ReplicaSets
        // In production, consider using a more sophisticated polling mechanism
        await new Promise(resolve => setTimeout(resolve, 10000));
    }

    private async getAssociatedReplicaSets(
        namespace: string,
        configMapName: string,
        kubeconfig: any
    ): Promise<k8sClient.V1ReplicaSet[]> {
        const kc = new k8sClient.KubeConfig();
        kc.loadFromString(JSON.stringify(kubeconfig));
        
        const appsV1Api = kc.makeApiClient(k8sClient.AppsV1Api);
        
        try {
            const response = await appsV1Api.listNamespacedReplicaSet(
                namespace,
                undefined, // pretty
                false, // allowWatchBookmarks
                undefined, // continue
                undefined, // fieldSelector
                `configMap=${configMapName}` // labelSelector
            );
            
            return response.body.items;
        } catch (error) {
            pulumi.log.error(`Failed to list ReplicaSets: ${error}`);
            return [];
        }
    }
}
```

## How it works

1. **Rollout Creation**: When a new rollout is created, Argo Rollouts generates new ReplicaSets for the canary deployment
2. **ConfigMap Patching**: Our code waits for the ReplicaSet creation, then patches the ConfigMap with owner references pointing to these ReplicaSets
3. **Garbage Collection**: Kubernetes automatically tracks the relationship between ConfigMaps and ReplicaSets
4. **Automatic Cleanup**: When ReplicaSets are cleaned up (based on the default 10 revision history), their associated ConfigMaps are also garbage collected

## Benefits

- **Revision Control**: ConfigMaps now have revision-like behavior tied to ReplicaSet history
- **Automatic Cleanup**: No manual intervention needed for ConfigMap cleanup
- **Canary Safety**: Old ConfigMaps remain available during canary deployments until ReplicaSets are cleaned up
- **Spot Instance Resilience**: Pods that get replaced during canary deployments can still access their original ConfigMaps

## Configuration options

```typescript
interface RolloutComponentArgs {
    namespace: string;
    configMapPatch?: boolean;
    kubeconfig: pulumi.Output<any>;
    configMapName: pulumi.Output<string>;
    rolloutSpec: k8s.types.input.apiextensions.CustomResourceArgs["spec"];
}
```

To enable this feature in your rollout:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Create your EKS cluster
const cluster = new k8s.Provider("k8s-provider", {
    kubeconfig: clusterKubeconfig,
});

// Create ConfigMap
const appConfig = new k8s.core.v1.ConfigMap("app-config", {
    metadata: {
        name: "my-app-config",
        namespace: "default",
        labels: {
            app: "my-app",
            configMap: "my-app-config", // Important for ReplicaSet selection
        },
    },
    data: {
        "app.properties": "key=value\nother=setting",
    },
}, { provider: cluster });

// Create rollout with ConfigMap revision management
const rollout = new ConfigMapRevisionRollout("my-app", {
    namespace: "default",
    configMapPatch: true,
    kubeconfig: clusterKubeconfig,
    configMapName: appConfig.metadata.name,
    rolloutSpec: {
        replicas: 3,
        selector: {
            matchLabels: { app: "my-app" },
        },
        template: {
            metadata: {
                labels: { app: "my-app" },
            },
            spec: {
                containers: [{
                    name: "app",
                    image: "nginx:latest",
                    volumeMounts: [{
                        name: "config",
                        mountPath: "/etc/config",
                    }],
                }],
                volumes: [{
                    name: "config",
                    configMap: {
                        name: appConfig.metadata.name,
                    },
                }],
            },
        },
        strategy: {
            canary: {
                maxSurge: 1,
                maxUnavailable: 0,
                steps: [
                    { setWeight: 20 },
                    { pause: { duration: "1m" } },
                    { setWeight: 50 },
                    { pause: { duration: "2m" } },
                ],
            },
        },
    },
});
```

## Key dependencies

The solution uses several key packages:

- `@pulumi/kubernetes`: For Kubernetes resources and ConfigMapPatch
- `@kubernetes/client-node`: For direct Kubernetes API access  
- Argo Rollouts CRDs installed in your cluster

## Conclusion

This approach gives us ConfigMap revision functionality that doesn't exist natively in Kubernetes or Pulumi.
By leveraging Kubernetes' garbage collection mechanism and Pulumi's patching capabilities,
we created a robust solution for managing ConfigMap lifecycles during canary deployments.

The solution is particularly valuable when:

- Running canary deployments with Argo Rollouts
- Using AWS Spot instances that can be replaced during deployments
- Needing automatic cleanup of old ConfigMaps without manual intervention
- Wanting to maintain configuration availability for older pods during deployment transitions

This pattern can be extended to other scenarios
where you need revision control for Kubernetes resources that don't natively support it.
