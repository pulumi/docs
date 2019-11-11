---
title: Deploy Apps
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-apps
    weight: 8
---

The following are examples of how to create and use various types of Kubernetes
resources, and typical apps and workloads.

{{< cloudchoose >}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for the AWS apps stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/06-apps

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for the Azure apps stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/06-apps

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for the GCP apps stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/06-apps

{{% /md %}}
</div>

The full code for the apps is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps

## Overview

Check out how to:

  * [Build and Deploy a Container](#build-and-deploy-a-container)
  * [Deploy Wordpress](#deploy-wordpress)
  * [Create a Deployment with a Secret](#create-a-deployment-with-a-secret)
  * [Perform a ConfigMap Rollout on a Deployment](#perform-a-configmap-rollout-on-a-deployment)
  * [Deploy a DaemonSet](#deploy-a-daemonset)
  * [Deploy a Job](#deploy-a-job)
  * [Deploy a CronJob](#deploy-a-cronjob)
  * [Deploy a StatefulSet](#deploy-a-statefulset)
  * [Learn More](#learn-more)

## Build and Deploy a Container

Build a Docker container image, push it to the registry, and deploy it to
Kubernetes.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this app stack is on [GitHub][gh-aws-deploy-stack].
[gh-aws-deploy-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/06-apps/deploy-container

```ts
import * as awsx from "@pulumi/awsx";
import * as k8s from "@pulumi/kubernetes";

// Create a repository.
const repo = new awsx.ecr.Repository("my-repo");

// Build a Docker image from a local Dockerfile context in the
// './node-app' directory, and push it to the registry.
const customImage = "node-app";
const appImage = repo.buildAndPushImage(`./${customImage}`);

// Create a k8s provider.
const provider = new k8s.Provider("provider", {
    kubeconfig: config.kubeconfig,
    namespace: config.appsNamespaceName,
});

// Create a Deployment of the built container.
const appLabels = { app: customImage };
const appDeployment = new k8s.apps.v1.Deployment("app", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: customImage,
                    image: appImage,
                    ports: [{name: "http", containerPort: 80}],
                }],
            }
        },
    }
}, { provider: provider });
```
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for this app stack is on [GitHub][gh-azure-deploy-stack].
[gh-azure-deploy-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/06-apps/deploy-container

```ts
import * as azure from "@pulumi/azure";
import * as docker from "@pulumi/docker";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("samples");

// Create a registry in ACR.
const registry = new azure.containerservice.Registry("myregistry", {
    resourceGroupName: resourceGroup.name,
    sku: "Basic",
    adminEnabled: true,
});

// Build a Docker image from a local Dockerfile context in the
// './node-app' directory, and push it to the registry.
const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${registry.loginServer}/${customImage}:v1.0.0`,
    build: {
        context: `./${customImage}`,
    },
    registry: {
        server: registry.loginServer,
        username: registry.adminUsername,
        password: registry.adminPassword,
    },
});

// Create a k8s provider.
const provider = new k8s.Provider("provider", {
    kubeconfig: config.kubeconfig,
    namespace: config.appsNamespaceName,
});

// Create a Deployment of the built container.
const appLabels = { app: customImage };
const appDeployment = new k8s.apps.v1.Deployment("app", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: customImage,
                    image: appImage.imageName,
                    ports: [{name: "http", containerPort: 80}],
                }],
            }
        },
    }
}, { provider: provider });
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this app stack is on [GitHub][gh-gcp-deploy-stack].
[gh-gcp-deploy-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/06-apps/deploy-container

```ts
import * as docker from "@pulumi/docker";
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

// Get the GCP project registry repository.
const registry = gcp.container.getRegistryRepository();

// Build a Docker image from a local Dockerfile context in the
// './node-app' directory, and push it to the registry.
const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${registry.repositoryUrl}/${customImage}:v1.0.0`,
    build: {
        context: `./${customImage}`,
    },
});

// Create a k8s provider.
const provider = new k8s.Provider("provider", {
    kubeconfig: config.kubeconfig,
    namespace: config.appsNamespaceName,
});

// Create a Deployment of the built container.
const appLabels = { app: customImage };
const appDeployment = new k8s.apps.v1.Deployment("app", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: customImage,
                    image: appImage.imageName,
                    ports: [{name: "http", containerPort: 80}],
                }],
            }
        },
    }
}, { provider: provider });
```

{{% /md %}}
</div>

## Deploy Wordpress

The full code for this app stack is on [GitHub][gh-wp-stack].
[gh-wp-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/wordpress

```ts
import * as k8s from "@pulumi/kubernetes";

const wordpressSvc = new k8s.core.v1.Service("wordpress", {
    spec: {
        type: "LoadBalancer",
        externalTrafficPolicy: "Cluster",
        ports: [
            {
                name: "http",
                port: 80,
                targetPort: "http"
            },
            {
                name: "https",
                port: 443,
                targetPort: "https"
            }
        ],
        selector: {
            app: "wordpress"
        }
    }
}, { provider: provider });

const wordpress = new k8s.apps.v1.Deployment("wordpress", {
    spec: {
        selector: {
            matchLabels: {
                app: "wordpress",
                release: "example"
            }
        },
        strategy: {
            type: "RollingUpdate"
        },
        replicas: 1,
        template: {
            metadata: {
                labels: {
                    app: "wordpress",
                    release: "example"
                }
            },
            spec: {
                hostAliases: [
                    {
                        ip: "127.0.0.1",
                        hostnames: [
                            "status.localhost"
                        ]
                    }
                ],
                containers: [
                    {
                        name: "wordpress",
                        image: "docker.io/bitnami/wordpress:5.2.4-debian-9-r0",
                        imagePullPolicy: "IfNotPresent",
                        env: [
                            { name: "ALLOW_EMPTY_PASSWORD", value: "yes" },
                            { name: "MARIADB_HOST", value: "mariadb" },
                            { name: "MARIADB_PORT_NUMBER", value: "3306" },
                            { name: "WORDPRESS_DATABASE_NAME", value: "bitnami_wordpress" },
                            { name: "WORDPRESS_DATABASE_USER", value: "bn_wordpress" },
                            {
                                name: "WORDPRESS_DATABASE_PASSWORD",
                                valueFrom: {
                                    secretKeyRef: {
                                        name: mariadbSecret.metadata.name,
                                        key: "mariadb-password"
                                    }
                                }
                            },
                            ...
                        ],
                        ports: [
                            { name: "http", containerPort: 80 },
                            { name: "https", containerPort: 443 }
                        ],
                        volumeMounts: [
                            {
                                mountPath: "/bitnami/wordpress",
                                name: "wordpress-data",
                                subPath: "wordpress"
                            }
                        ],
                        resources: {
                            requests: {
                                cpu: "300m",
                                memory: "512Mi"
                            }
                        }
                    }
                ],
                volumes: [
                    {
                        name: "wordpress-data",
                        persistentVolumeClaim: {
                            claimName: wordpressPVC.metadata.name
                        }
                    }
                ]
            }
        }
    }
}, { provider: provider });
...
```

## Create a Deployment with a Secret

Create a [Deployment][k8s-deploy] NGINX that uses a [Secret][k8s-secret]. 

The full code for this app stack is on [GitHub][gh-deploy-secret-stack].
[gh-deploy-secret-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/deployment-secret
[k8s-deploy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
[k8s-secret]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment://kubernetes.io/docs/concepts/configuration/secret/ 

{{< k8s-language noyaml >}}

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
```ts
import * as k8s from "@pulumi/kubernetes";

// Create a Secret with the database credentials.
const databaseSecret = new k8s.core.v1.Secret("db-secret", {
    stringData: {
        "database-username": config.databaseUsername,
        "database-password": config.databasePassword,
    }
}, { provider: provider });

// Create a Deployment that uses the database credentials as environment variables.
const appName = "nginx";
const appLabels = { app: appName };
const nginx = new k8s.apps.v1.Deployment(appName, {
    metadata: { labels: appLabels },
    spec: {
        selector: {
            matchLabels: appLabels,
        },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [
                    {
                        image: "nginx",
                        name: "nginx",
                        env: [
                            {
                                name: "DATABASE_USERNAME",
                                valueFrom: {
                                    secretKeyRef: {
                                        name: databaseSecret.metadata.name,
                                        key: "database-username"
                                    }
                                }
                            },
                            {
                                name: "DATABASE_PASSWORD",
                                valueFrom: {
                                    secretKeyRef: {
                                        name: databaseSecret.metadata.name,
                                        key: "database-password"
                                    }
                                }
                            }
                        ]
                    },
                ],
            },
        },
    },
}, { provider: provider });
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript-kx"></div>
<div class="mt">
{{% md %}}
```ts
import * as kx from "@pulumi/kubernetesx";

// Create a KX Secret with the database credentials.
const databaseSecretKx = new kx.Secret("db-secret", {
    stringData: {
        "database-username": config.databaseUsername,
        "database-password": config.databasePassword,
    }
}, { provider: provider });

// Create a KX PodBuilder for the demo app.
const nginxPB = new kx.PodBuilder(appName, {
    spec: {
        containers: [{
            image: "nginx",
            env: {
                "DATABASE_USERNAME": databaseSecretKx.asEnvValue("database-username"),
                "DATABASE_PASSWORD": databaseSecretKx.asEnvValue("database-password"),
            }
        }]
    }
});

// Create a KX Deployment from the KX PodBuilder by transforming it into a DeploymentSpec.
// The deployment use database credentials as environment variables.
const nginxDeployment = new kx.Deployment(appName, {
    spec: nginxPB.asDeploymentSpec({replicas: 1})
}, { provider: provider });
```
{{% /md %}}
</div>

## Perform a ConfigMap Rollout on a Deployment

For a complete example, check out the [Graceful App Rollout][tutorial-app-rollout] tutorial for more details
on how to update a Deployment automatically when it's ConfigMap changes.

[tutorial-app-rollout]: {{< relref "/docs/tutorials/kubernetes/configmap-rollout" >}}

## Deploy a DaemonSet

Deploy a [DaemonSet][k8s-ss] of NGINX across all nodes in the cluster.

The full code for this app stack is on [GitHub][gh-ds-stack].
[gh-ds-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/daemonset
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

```ts
import * as k8s from "@pulumi/kubernetes";

// Create a DaemonSet that deploys nginx to each worker node.
const appName = "nginx";
const appLabels = { app: appName };
const nginx = new k8s.apps.v1.DaemonSet(appName, {
    metadata: { labels: appLabels },
    spec: {
        selector: {
            matchLabels: appLabels,
        },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [
                    {
                        image: "nginx",
                        name: "nginx",
                    },
                ],
            },
        },
    },
}, { provider: provider });
```

## Deploy a Job

Deploy a [Job][k8s-job] of a Perl program.

The full code for this app stack is on [GitHub][gh-job-stack].
[gh-job-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/job
[k8s-job]: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/

```ts
import * as k8s from "@pulumi/kubernetes";

// Create an example Job.
const exampleJob = new k8s.batch.v1.Job("example-job", {
    spec: {
        template: {
            spec: {
                containers: [
                    {
                        name: "pi",
                        image: "perl",
                        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"],
                    }
                ],
                restartPolicy: "Never"
            }
        },
    }
}, { provider: provider });
```

## Deploy a CronJob

Deploy a [CronJob][k8s-cj] of a command that runs every minute.

The full code for this app stack is on [GitHub][gh-cronjob-stack].
[gh-cronjob-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/cronjob
[k8s-cj]: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/

```ts
import * as k8s from "@pulumi/kubernetes";

// Create an example CronJob.
const exampleCronJob = new k8s.batch.v1beta1.CronJob("example-cronjob", {
    spec: {
        schedule: "*/1 * * * *",
        jobTemplate: {
            spec: {
                template: {
                    spec: {
                        containers: [
                            {
                                name: "hello",
                                image: "busybox",
                                args: ["/bin/sh",  "-c", "date; echo Hello from the Kubernetes cluster"],
                            }
                        ],
                        restartPolicy: "OnFailure"
                    }
                }
            }
        },
    }
}, { provider: provider });
```

## Deploy a StatefulSet

Deploy a [StatefulSet][k8s-ss] of [MariaDB][mariadb].

The full code for this app stack is on [GitHub][gh-ss-stack].
[gh-ss-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/apps/statefulset
[k8s-ss]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[mariadb]: https://mariadb.org/

```ts
import * as k8s from "@pulumi/kubernetes";

// Deploy MariaDB as a StatefulSet.
const mariadb = new k8s.apps.v1.StatefulSet("mariadb", {
    spec: {
        selector: {
            matchLabels: {
                app: "mariadb",
                release: "example",
                component: "master"
            }
        },
        serviceName: "mariadb",
        replicas: 1,
        updateStrategy: {
            type: "RollingUpdate"
        },
        template: {
            metadata: {
                labels: {
                    app: "mariadb",
                    release: "example",
                    component: "master"
                }
            },
            spec: {
                serviceAccountName: "default",
                securityContext: {
                    fsGroup: 1001,
                    runAsUser: 1001
                },
                affinity: {
                    podAntiAffinity: {
                        preferredDuringSchedulingIgnoredDuringExecution: [
                            {
                                weight: 1,
                                podAffinityTerm: {
                                    topologyKey: "kubernetes.io/hostname",
                                    labelSelector: {
                                        matchLabels: {
                                            app: "mariadb",
                                            release: "example"
                                        }
                                    }
                                }
                            }
                        ]
                    }
                },
                containers: [
                    {
                        name: "mariadb",
                        image: "docker.io/bitnami/mariadb:10.3.18-debian-9-r36",
                        imagePullPolicy: "IfNotPresent",
                        env: [
                            {
                                name: "MARIADB_ROOT_PASSWORD",
                                valueFrom: {
                                    secretKeyRef: {
                                        name: mariadbSecret.metadata.name,
                                        key: "mariadb-root-password"
                                    }
                                }
                            },
                            { name: "MARIADB_USER", value: "bn_wordpress" },
                            {
                                name: "MARIADB_PASSWORD",
                                valueFrom: {
                                    secretKeyRef: {
                                        name: mariadbSecret.metadata.name,
                                        key: "mariadb-password"
                                    }
                                }
                            },
                            { name: "MARIADB_DATABASE", value: "bitnami_wordpress" }
                        ],
                        ports: [
                            { name: "mysql", containerPort: 3306 }
                        ],
                        livenessProbe: {
                            exec: {
                                command: ["sh", "-c", "exec mysqladmin status -uroot -p$MARIADB_ROOT_PASSWORD"],
                            },
                            initialDelaySeconds: 120,
                            periodSeconds: 10,
                            timeoutSeconds: 1,
                            successThreshold: 1,
                            failureThreshold: 3
                        },
                        readinessProbe: {
                            exec: {
                                command: ["sh", "-c", "exec mysqladmin status -uroot -p$MARIADB_ROOT_PASSWORD"]
                            },
                            initialDelaySeconds: 30,
                            periodSeconds: 10,
                            timeoutSeconds: 1,
                            successThreshold: 1,
                            failureThreshold: 3
                        },
                        volumeMounts: [
                            {
                                name: "data",
                                mountPath: "/bitnami/mariadb"
                            },
                            {
                                name: "config",
                                mountPath: "/opt/bitnami/mariadb/conf/my.cnf",
                                subPath: "my.cnf"
                            }
                        ]
                    }
                ],
                volumes: [
                    {
                        name: "config",
                        configMap: {
                            name: mariadbCM.metadata.name
                        }
                    }
                ]
            },
        },
        volumeClaimTemplates: [
            {
                metadata: {
                    name: "data",
                    labels: {
                        app: "mariadb",
                        component: "master",
                        release: "example",
                    }
                },
                spec: {
                    accessModes: [
                        "ReadWriteOnce"
                    ],
                    resources: {
                        requests: {
                            storage: "8Gi"
                        }
                    }
                }
            }
        ]
    }
}, { provider: provider });
```

## Learn More


To learn more about how to work with Kubernetes and Pulumi, check out the
[Kubernetes Tutorials][k8s-tutorials] for details.

[k8s-tutorials]: {{< relref "/docs/tutorials/kubernetes" >}}
