---
title_tag: Deploying Kubernetes Apps | Crosswalk
title: Deploying Kubernetes Apps
meta_desc: This page gives you an overview on how to deploy Kubernetes applications to different cloud providers.
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-apps
    weight: 9
---

The following are examples of how to create and use various types of Kubernetes
resources, and typical apps and workloads.

{{< chooser cloud "aws,azure,gcp" / >}}

{{% choosable cloud aws %}}

The full code for the AWS apps stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/06-apps
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

The full code for the Azure apps stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/06-apps
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud gcp %}}

The full code for the GCP apps stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/06-apps
<!-- markdownlint-enable url -->

{{% /choosable %}}

The full code for the apps is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps
<!-- markdownlint-enable url -->

## Overview

Check out how to:

- [Overview](#overview)
- [Build and Deploy a Container](#build-and-deploy-a-container)
- [Deploy a Pod with a Sidecar](#deploy-a-pod-with-a-sidecar)
- [Deploy a Helm Chart](#deploy-a-helm-chart)
- [Deploy Wordpress](#deploy-wordpress)
- [Create a Deployment with a Secret](#create-a-deployment-with-a-secret)
- [Perform a ConfigMap Rollout on a Deployment](#perform-a-configmap-rollout-on-a-deployment)
- [Deploy a Job](#deploy-a-job)
- [Deploy a DaemonSet](#deploy-a-daemonset)
- [Deploy a CronJob](#deploy-a-cronjob)
- [Deploy a StatefulSet](#deploy-a-statefulset)
- [Learn More](#learn-more)

## Build and Deploy a Container

Build a Docker container image, push it to the registry, and deploy it to
Kubernetes.

{{% choosable cloud aws %}}

The full code for this app stack is on [GitHub][gh-aws-deploy-stack].

<!-- markdownlint-disable url -->
[gh-aws-deploy-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/06-apps/build-deploy-container
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{< choosable k8s-language typescript >}}

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

{{< /choosable >}}

{{< choosable k8s-language typescript-kx >}}

```ts
import * as awsx from "@pulumi/awsx";
import * as k8s from "@pulumi/kubernetes";
import * as kx from "@pulumi/kubernetesx";

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

// Define the Pod for the Deployment.
const pb = new kx.PodBuilder({
    containers: [{
        image: appImage,
        ports: { "http": 80 },
    }],
});

// Create a Deployment of the Pod defined by the PodBuilder.
const appDeploymentKx = new kx.Deployment("app-kx", {
    spec: pb.asDeploymentSpec(),
}, { provider: provider });
```

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

{{% choosable cloud azure %}}

The full code for this app stack is on [GitHub][gh-azure-deploy-stack].

<!-- markdownlint-disable url -->
[gh-azure-deploy-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/06-apps/build-deploy-container
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{< choosable k8s-language typescript >}}

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

{{< /choosable >}}

{{< choosable k8s-language typescript-kx >}}

```ts
import * as azure from "@pulumi/azure";
import * as k8s from "@pulumi/kubernetes";
import * as kx from "@pulumi/kubernetesx";
import * as docker from "@pulumi/docker";
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

// Define the Pod for the Deployment.
const pb = new kx.PodBuilder({
    containers: [{
        image: appImage.imageName,
        ports: { "http": 80 },
    }],
});

// Create a Deployment of the Pod defined by the PodBuilder.
const appDeploymentKx = new kx.Deployment("app-kx", {
    spec: pb.asDeploymentSpec(),
}, { provider: provider });
```

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

{{% choosable cloud gcp %}}

The full code for this app stack is on [GitHub][gh-gcp-deploy-stack].

<!-- markdownlint-disable url -->
[gh-gcp-deploy-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/06-apps/build-deploy-container
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{< choosable k8s-language typescript >}}

```ts
import * as docker from "@pulumi/docker";
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

// Get the GCP project registry repository.
const registry = gcp.container.getRegistryRepositoryOutput();

// Get the repository URL
const repositoryUrl = registry.repositoryUrl;

// Build a Docker image from a local Dockerfile context in the
// './node-app' directory, and push it to the registry.
const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${repositoryUrl}/${customImage}:v1.0.0`,
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

{{< /choosable >}}

{{< choosable k8s-language typescript-kx >}}

```ts
import * as docker from "@pulumi/docker";
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";
import * as kx from "@pulumi/kubernetesx";
import * as pulumi from "@pulumi/pulumi";

// Get the GCP project registry repository.
const registry = gcp.container.getRegistryRepositoryOutput();

// Get the repository URL
const repositoryUrl = registry.repositoryUrl;

// Build a Docker image from a local Dockerfile context in the
// './node-app' directory, and push it to the registry.
const customImage = "node-app";
const appImage = new docker.Image(customImage, {
    imageName: pulumi.interpolate`${repositoryUrl}/${customImage}:v1.0.0`,
    build: {
        context: `./${customImage}`,
    },
});

// Create a k8s provider.
const provider = new k8s.Provider("provider", {
    kubeconfig: config.kubeconfig,
    namespace: config.appsNamespaceName,
});

// Define the Pod for the Deployment.
const pb = new kx.PodBuilder({
    containers: [{
        image: appImage.imageName,
        ports: { "http": 80 },
    }],
});

// Create a Deployment of the Pod defined by the PodBuilder.
const appDeploymentKx = new kx.Deployment("app-kx", {
    spec: pb.asDeploymentSpec(),
}, { provider: provider });
```

{{< /choosable >}}

{{< /chooser >}}

{{% /choosable %}}

## Deploy a Pod with a Sidecar

The full code for this app stack is on [GitHub][gh-wp-stack].

<!-- markdownlint-disable url -->
[gh-wp-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/pod-sidecar
<!-- markdownlint-enable url -->

Create a NGINX Pod with a Debian sidecar that prints to a file in a shared
volume of the Pod.

```ts
import * as k8s from "@pulumi/kubernetes";

// Create an example Pod with a Sidecar.
const pod = new k8s.core.v1.Pod("example", {
    spec: {
        restartPolicy: "Never",
        volumes: [
            {name: "shared-data", emptyDir: {}},
        ],
        containers: [
            {
                name: "nginx",
                image: "nginx",
                resources: {requests: {cpu: "50m", memory: "50Mi"}},
                volumeMounts: [
                    { name: "shared-data", mountPath: "/usr/share/nginx/html"},
                ],
            },
            {
                name: "debian-container",
                image: "debian",
                resources: {requests: {cpu: "50m", memory: "50Mi"}},
                volumeMounts: [
                    { name: "shared-data", mountPath: "/pod-data"},
                ],
                command: [ "/bin/bash"],
                args: ["-c", "echo Hello from the Debian container > /pod-data/index.html ; sleep infinity"],
            }
        ],
    }
}, { provider: provider });
```

Print out the contents of the shared file from the `nginx` container in the Pod.

```bash
$ kubectl exec -it example-<SUFFIX> -n `pulumi output stack appsNamespaceName` -c nginx -- cat /usr/share/nginx/html/index.html
```

## Deploy a Helm Chart

Deploy the [Helm chart][nginx-helm] into the `app-svcs` namespace created in [Configure
Cluster Defaults][crosswalk-k8s-defaults], and publicly expose it to the
Internet using a [load balanced Service][k8s-lb-svc].

> Note: NGINX requires a privileged PSP given its [use][nginx-priv-use] of `allowPrivilegeEscalation: true`.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Deploy the NGINX ingress controller using the Helm chart.
const nginx = new k8s.helm.v3.Chart("nginx",
    {
        namespace: config.appSvcsNamespaceName,
        chart: "nginx-ingress",
        version: "1.24.4",
        fetchOpts: {repo: "https://charts.helm.sh/stable/"},
        values: {controller: {publishService: {enabled: true}}},
        transformations: [
            (obj: any) => {
                // Do transformations on the YAML to set the namespace
                if (obj.metadata) {
                    obj.metadata.namespace = config.appSvcsNamespaceName;
                }
            },
        ],
    },
    {providers: {kubernetes: provider}},
);
```

<!-- markdownlint-disable url -->
[nginx-priv-use]: https://github.com/helm/charts/blob/master/stable/nginx-ingress/values.yaml#L12
[k8s-lb-svc]: https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer
[nginx-helm]: https://github.com/helm/charts/tree/master/stable/nginx-ingress
[crosswalk-k8s-defaults]: /docs/guides/crosswalk/kubernetes/configure-defaults/#namespaces
<!-- markdownlint-enable url -->

## Deploy Wordpress

Create a Deployment of Wordpress.

The full code for this app stack is on [GitHub][gh-deploy-wp-stack].

<!-- markdownlint-disable url -->
[gh-deploy-wp-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/wordpress
<!-- markdownlint-enable url -->

```ts
import * as k8s from "@pulumi/kubernetes";

const wordpress = new k8s.apps.v1.Deployment("wordpress", {
    spec: {
        selector: { matchLabels: { app: "wordpress", release: "example" } },
        strategy: { type: "RollingUpdate" },
        replicas: 1,
        template: {
            metadata: { labels: { app: "wordpress", release: "example" } },
            spec: {
                hostAliases: [ { ip: "127.0.0.1", hostnames: [ "status.localhost"] } ],
                containers: [
                    {
                        name: "wordpress",
                        image: "docker.io/bitnami/wordpress:5.2.4-debian-9-r0",
                        imagePullPolicy: "IfNotPresent",
                        env: [
                            { name: "MARIADB_HOST", value: "mariadb" },
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
                        resources: { requests: { cpu: "300m", memory: "512Mi" } }
                        ...
                    }
                ],
                ...
            }
        }
    }
}, { provider: provider });
```

## Create a Deployment with a Secret

Create a [Deployment][k8s-deploy] NGINX that uses a [Secret][k8s-secret].

The full code for this app stack is on [GitHub][gh-deploy-secret-stack].

<!-- markdownlint-disable url -->
[gh-deploy-secret-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/deployment-secret
[k8s-deploy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
[k8s-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{% choosable k8s-language typescript %}}

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

{{% /choosable %}}

{{% choosable k8s-language typescript-kx %}}

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
const nginxPB = new kx.PodBuilder({
    containers: [{
        image: "nginx",
        env: {
            "DATABASE_USERNAME": databaseSecretKx.asEnvValue("database-username"),
            "DATABASE_PASSWORD": databaseSecretKx.asEnvValue("database-password"),
        }
    }]
});

// Create a KX Deployment from the KX PodBuilder by transforming it into a DeploymentSpec.
// The deployment use database credentials as environment variables.
const nginxDeployment = new kx.Deployment(appName, {
    spec: nginxPB.asDeploymentSpec({replicas: 1})
}, { provider: provider });
```

{{% /choosable %}}

{{< /chooser >}}

## Perform a ConfigMap Rollout on a Deployment

For a complete example, check out our Kubernetes [Graceful App Rollout][tutorial-app-rollout]
tutorial for more details on how to update a Deployment automatically
when it's ConfigMap changes.

[tutorial-app-rollout]: /registry/packages/kubernetes/how-to-guides/configmap-rollout/

## Deploy a Job

Deploy a [Job][k8s-job] of a Perl program.

The full code for this app stack is on [GitHub][gh-job-stack].

<!-- markdownlint-disable url -->
[gh-job-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/job
[k8s-job]: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{% choosable k8s-language typescript %}}

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

{{% /choosable %}}

{{% choosable k8s-language typescript-kx %}}

```ts
import * as kx from "@pulumi/kubernetesx";

// Create the PodBuilder for the Job.
const pb = new kx.PodBuilder({
    containers: [{
        name: "pi",
        image: "perl",
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"],
    }],
    restartPolicy: "Never",
});

// Create a Job using the Pod defined by the PodBuilder.
const exampleJobKx = new kx.Job("example-job-kx", {
    spec: pb.asJobSpec(),
}, { provider: provider });
```

{{% /choosable %}}

{{< /chooser >}}

## Deploy a DaemonSet

Deploy a [DaemonSet][k8s-ds] of NGINX across all nodes in the cluster.

The full code for this app stack is on [GitHub][gh-ds-stack].

<!-- markdownlint-disable url -->
[gh-ds-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/daemonset
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{% choosable k8s-language typescript %}}

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

{{% /choosable %}}

{{% choosable k8s-language typescript-kx %}}

Coming Soon.

{{% /choosable %}}

{{< /chooser >}}

## Deploy a CronJob

Deploy a [CronJob][k8s-cj] of a command that runs every minute.

The full code for this app stack is on [GitHub][gh-cronjob-stack].

<!-- markdownlint-disable url -->
[gh-cronjob-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/cronjob
[k8s-cj]: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{% choosable k8s-language typescript %}}

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

{{% /choosable %}}

{{% choosable k8s-language typescript-kx %}}

Coming soon.

{{% /choosable %}}

{{< /chooser >}}

## Deploy a StatefulSet

Deploy a [StatefulSet][k8s-ss] of [MariaDB][mariadb].

The full code for this app stack is on [GitHub][gh-ss-stack].

<!-- markdownlint-disable url -->
[gh-ss-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/apps/statefulset
[k8s-ss]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[mariadb]: https://mariadb.org/
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,typescript-kx" >}}

{{% choosable k8s-language typescript %}}

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

{{% /choosable %}}

{{% choosable k8s-language typescript-kx %}}

Coming soon.

{{% /choosable %}}

{{< /chooser >}}

## Learn More

To learn more about how to work with Kubernetes and Pulumi, check out the
[Kubernetes Tutorials][k8s-tutorials] for details.

[k8s-tutorials]: /registry/packages/kubernetes/how-to-guides/
