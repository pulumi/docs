---
title: Google Kubernetes Engine (GKE) - Hello World!
meta_desc: How to launch a new Managed Kubernetes Cluster in Google Kubernetes Engine (GKE) on GCP.
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-gke/"]
---

In this tutorial, we'll launch a new Managed Kubernetes cluster in Google Kubernetes Engine (GKE) on GCP. The [code for this tutorial](https://github.com/pulumi/examples/tree/master/gcp-ts-gke-hello-world) is available on GitHub.

## Prerequisites

1. [Install Pulumi]({{< relref "/docs/get-started/install" >}})
1. [Install Node.js version 8 or later](https://nodejs.org/en/download/)
1. Install a package manager for Node.js, such as [npm](https://www.npmjs.com/get-npm) or [Yarn](https://yarnpkg.com/en/docs/install).
1. [Install Google Cloud SDK (`gcloud`)](https://cloud.google.com/sdk/docs/downloads-interactive)
1. Configure GCP Auth

    * Login using `gcloud`

        ```bash
        $ gcloud auth login
        $ gcloud config set project <YOUR_GCP_PROJECT_HERE>
        $ gcloud auth application-default login
        ```

    > Note: This auth mechanism is meant for inner loop developer
    > workflows. If you want to run this example in an unattended service
    > account setting, such as in CI/CD, please [follow instructions to
    > configure your service account]({{< relref "service-account.md" >}}). The
    > service account must have the role `Kubernetes Engine Admin` / `container.admin`.

## Create a new GKE cluster {#new-gke-cluster}

1. In a new folder `gke-hello-world`, create an empty project with `pulumi new`.

    ```bash
    $ mkdir gke-hello-world && cd gke-hello-world
    $ pulumi new typescript
    ```

    * Enter in a Pulumi project name, and description to detail what this
      Pulumi program does
    * Enter in a name for the [Pulumi stack]({{< relref "/docs/intro/concepts/stack.md" >}}), which is an instance of our Pulumi program, and is used to distinguish amongst different development phases and environments of your work streams.

1. Add the required dependencies:

    This installs the dependent packages [needed]({{< relref "/docs/intro/concepts/how-pulumi-works" >}}) for our Pulumi program.

	```bash
	npm install --save @pulumi/pulumi @pulumi/gcp @pulumi/kubernetes
	```

1. Set the required GCP configuration variables:

    This sets the GCP project and zone for our GKE cluster used in the current
    stack instance of our Pulumi program. This can used as a means to define
    defaults, and differentiate between settings across several Pulumi stacks.

    ```bash
    pulumi config set gcp:project <YOUR_GCP_PROJECT_HERE>
    pulumi config set gcp:zone us-west1-a     // any valid GCP Zone here
    ```

1. Open the existing file `index.ts`, and replace the contents with the following below.

    The `index.ts` occupies the role as the *main* entrypoint in our Pulumi
    program. In it, we are going to declare:

	* The resources we want in GCP to provision the GKE cluster based on our
      cluster configuration settings,
	* The `kubeconfig` file to access the cluster, and
	* The initialization of a Pulumi Kubernetes provider with the
	`kubeconfig`, so that we can deploy Kubernetes resources to the cluster
    once its ready in the next steps.

    ```typescript
    import * as k8s from "@pulumi/kubernetes";
    import * as pulumi from "@pulumi/pulumi";
    import * as gcp from "@pulumi/gcp";

    const name = "helloworld";

    // Create a GKE cluster
    const engineVersion = gcp.container.getEngineVersions().latestMasterVersion;
    const cluster = new gcp.container.Cluster(name, {
        initialNodeCount: 2,
        minMasterVersion: engineVersion,
        nodeVersion: engineVersion,
        nodeConfig: {
            machineType: "n1-standard-1",
            oauthScopes: [
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring"
            ],
        },
    });

    // Export the Cluster name
    export const clusterName = cluster.name;

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
    });
    ```

1. To preview and deploy changes, run `pulumi up` and select "yes."

    The `up` sub-command shows a preview of the resources that will be created
    and prompts on whether to proceed with the deployment. Note that the stack
    itself is counted as a resource, though it does not correspond
    to a physical cloud resource.

    You can also run `pulumi up --diff` to see and inspect the diffs of the
    overall changes expected to take place.

    Running `pulumi up` will deploy the GKE cluster. Note, provisioning a
    new GKE cluster takes between 3-5 minutes.

        $ pulumi up
        Previewing update (gke-demo):

            Type                            Name                 Plan
        +   pulumi:pulumi:Stack             gke-hello-world-dev  create
        +   ├─ gcp:container:Cluster        helloworld           create
        +   └─ pulumi:providers:kubernetes  helloworld           create

        Resources:
            + 3 to create

        Updating (gke-demo):

            Type                            Name                 Status
        +   pulumi:pulumi:Stack             gke-hello-world-dev  created
        +   ├─ gcp:container:Cluster        helloworld           created
        +   └─ pulumi:providers:kubernetes  helloworld           created

        Outputs:
            clusterName: "helloworld-2a6de9a"
            kubeconfig : "<KUBECONFIG_CONTENTS>"

        Resources:
            + 3 created

        Duration: 4m37s

## Access the Kubernetes Cluster using Pulumi Providers

Now that we have an instance of Kubernetes running, we may want to create API resources in Kubernetes to manage our workloads through Pulumi.

We can do this by configuring a Pulumi provider for our newly created cluster, and instantiating a new Kubernetes resource object in our Pulumi program. The concept of a provider allows us to abstract away Kubernetes clusters in Pulumi that are independent of their underlying cloud provider, so that you can operate on and work with your Kubernetes clusters in a standard manner.

1. Create a new Kubernetes Namespace and Deployment:

	This declares a new Kubernetes Namespace, Deployment and Service to be
	created using the Pulumi Kubernetes provider to our cluster.

    Open the existing file `index.ts`, and append the following:

    ```typescript
    // Create a Kubernetes Namespace
    const ns = new k8s.core.v1.Namespace(name, {}, { provider: clusterProvider });

    // Export the Namespace name
    export const namespaceName = ns.metadata.apply(m => m.name);

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
                                ports: [{ name: "http", containerPort: 80 }]
                            }
                        ],
                    }
                }
            },
        },
        {
            provider: clusterProvider,
        }
    );

    // Export the Deployment name
    export const deploymentName = deployment.metadata.apply(m => m.name);

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
        }
    );

    // Export the Service name and public LoadBalancer endpoint
    export const serviceName = service.metadata.apply(m => m.name);
    export const servicePublicIP = service.status.apply(s => s.loadBalancer.ingress[0].ip)
    ```

1. Run `pulumi up`, note the preview diff, and select "yes" to deploy the changes.

    As part of the update, you'll see some new objects in the output: a
    `Namespace` in Kubernetes to deploy into, a `Deployment` resource for
    the NGINX app, and a LoadBalancer `Service` to publicly access NGINX.

    Pulumi understands which changes to a given cloud resource can be made
    in-place, and which require replacement, and computes
    the minimally disruptive change to achieve the desired state. The CLI will
    also output incremental status updates, as the Kubernetes changes progress.

	> **Note:** Pulumi auto-generates a suffix for all objects.
    > See the [Pulumi Programming Model]({{< relref "/docs/intro/concepts/programming-model.md#autonaming" >}}) for more info.
    >
    > ```
    > ...
	> deploymentName : "helloworld-tlsr4sg5"
    > ...
	> namespaceName  : "helloworld-pz4u5kyq"
	> serviceName    : "helloworld-l61b5dby"
	> servicePublicIP: "35.236.26.151"
    > ```

    If you visit the FQDN listed in `servicePublicIP` you should land on the
    NGINX welcome page. Note, that it may take a minute or so for the
    LoadBalancer to become active on GCP.

## Access the Kubernetes Cluster using `kubectl`

You may access your new Kubernetes cluster using `kubectl`. Install `kubectl` as follows:

```bash
export KUBERNETES_VERSION=1.11.6 && sudo curl -s -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl && sudo chmod +x /usr/local/bin/kubectl
```

Next, we need to setup the `kubeconfig` file to configure `kubectl`. We can leverage the Pulumi
stack output in the CLI, as Pulumi facilitates exporting these objects for us.

```bash
pulumi stack output kubeconfig > kubeconfig
export KUBECONFIG=$PWD/kubeconfig

kubectl version
kubectl cluster-info
kubectl get nodes
```

We can also use the stack output to query the cluster for our newly created Deployment:

```bash
kubectl get deployment $(pulumi stack output deploymentName) --namespace=$(pulumi stack output namespaceName)
kubectl get service $(pulumi stack output serviceName) --namespace=$(pulumi stack output namespaceName)
```

We can also create another NGINX Deployment into the `default` namespace using
`kubectl` natively:

```bash
kubectl create deployment my-nginx --image=nginx
kubectl get pods
kubectl delete deployment my-nginx
```

Of course, by doing so, resources are outside of Pulumi's purview, but this simply
demonstrates that all the `kubectl` commands you're used to will work.

## Experimentation

From here on, feel free to experiment. Simply making edits and running `pulumi up` afterwords, will incrementally update your stack.

### Running Off-the-Shelf Guestbook YAML

For example, if you wish to pull existing Kubernetes YAML manifests into
Pulumi to aid in your transition, append the following code block to the existing
`index.ts` file and run `pulumi up`.

This is an example of how to create the standard Kubernetes Guestbook manifests in
Pulumi using the [Guestbook YAML manifests][guestbook]. We take the additional
steps of transforming its properties to use the same Namespace and metadata labels
that the NGINX stack uses, and also make its frontend service use a
LoadBalancer typed Service to expose it publicly.

```typescript
// Create resources for the Kubernetes Guestbook from its YAML manifests
const guestbook = new k8s.yaml.ConfigFile("guestbook",
    {
        file: "https://raw.githubusercontent.com/pulumi/pulumi-kubernetes/master/tests/examples/yaml-guestbook/yaml/guestbook.yaml",
        transformations: [
            (obj: any) => {
                // Do transformations on the YAML to use the same namespace and
                // labels as the NGINX stack above
                if (obj.metadata.labels) {
                    obj.metadata.labels['appClass'] = namespaceName
                } else {
                    obj.metadata.labels = appLabels
                }

                // Make the 'frontend' Service public by setting it to be of type
                // LoadBalancer
                if (obj.kind == "Service" && obj.metadata.name == "frontend") {
                    if (obj.spec) {
                        obj.spec.type = "LoadBalancer"
                    }
                }
            }
        ],
    },
    {
        providers: { "kubernetes": clusterProvider },
    },
);

// Export the Guestbook public LoadBalancer endpoint
export const guestbookPublicIP =
    guestbook.getResourceProperty("v1/Service", "frontend", "status").apply(s => s.loadBalancer.ingress[0].ip);
```

## Clean up

Run the following command to tear down the resources that are part of our stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these
    resources.

1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the
    Pulumi Console and cannot be undone.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and launch a
Managed Kubernetes cluster on GCP GKE.

For a follow-up example on how to use Pulumi programs to create a Kubernetes
apps on your new cluster, see [Kubernetes Tutorial: Getting Started With Pulumi]({{< relref "configmap-rollout" >}}).

We also encourage you to watch Joe Beda, co-founder of Kubernetes and Heptio,
take Pulumi for a spin in an episode of [TGIK8s](https://github.com/heptio/tgik).

<iframe width="560" height="315"
src="https://www.youtube.com/embed/ILMK65YVSKw" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

[guestbook]: https://raw.githubusercontent.com/pulumi/pulumi-kubernetes/master/tests/examples/yaml-guestbook/yaml/guestbook.yaml
