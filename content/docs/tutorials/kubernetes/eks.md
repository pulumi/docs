---
title: ECS for Kubernetes (EKS) - Hello World!
meta_desc: How to launch a new Managed Kubernetes Cluster on Elastic Container Service for Kubernetes (EKS) on AWS.
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-eks/"]
---

In this tutorial, we'll launch a new Managed Kubernetes cluster in Elastic Container Service for Kubernetes (EKS) on AWS. The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-ts-eks-hello-world) is available on GitHub.

{{< aws-eks-prereqs >}}

## Create a new EKS cluster {#new-eks-cluster}

1. In a new folder `eks-hello-world`, create an empty project with `pulumi new`.

    This will create a base Pulumi program in TypeScript, and is great
    recommendation to begin your journey.

    ```bash
    $ mkdir eks-hello-world && cd eks-hello-world
    $ pulumi new aws-typescript
    ```

    * Enter in a Pulumi project name, and description to detail what this
      Pulumi program does
    * Enter in a name for the [Pulumi stack]({{< relref "/docs/intro/concepts/stack" >}}), which is an instance of our Pulumi program, and is used to distinguish amongst different development phases and environments of your work streams.

1. Add the required dependencies:

    This installs the dependent packages [needed]({{< relref "/docs/intro/concepts/how-pulumi-works" >}}) for our Pulumi program.

	```bash
	$ npm install --save @pulumi/eks @pulumi/kubernetes
	```

1. Open the existing file `index.ts`, and replace the contents with the following:

    The `index.ts` occupies the role as the *main* entrypoint in our Pulumi
    program. In it, we are going to declare:

	* The resources we want in AWS to provision the EKS cluster based on our
      cluster configuration settings,
	* The `kubeconfig` file to access the cluster, and
	* The initialization of a Pulumi Kubernetes provider with the
	`kubeconfig`, so that we can deploy Kubernetes resources to the cluster
    once its ready in the next steps.

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as awsx from "@pulumi/awsx";
    import * as eks from "@pulumi/eks";
    import * as k8s from "@pulumi/kubernetes";

    const name = "helloworld";

    // Create an EKS cluster with non-default configuration
    const vpc = new awsx.ec2.Vpc("vpc", { subnets: [{ type: "public" }] });
    const cluster = new eks.Cluster(name, {
    vpcId: vpc.id,
        subnetIds: vpc.publicSubnetIds,
        desiredCapacity: 2,
        minSize: 1,
        maxSize: 2,
        storageClasses: "gp2",
        deployDashboard: false,
    });

    // Export the clusters' kubeconfig.
    export const kubeconfig = cluster.kubeconfig
    ```

1. To preview and deploy changes, run `pulumi up` and select "yes."

    The `up` sub-command shows a preview of the resources that will be created
    and prompts on whether to proceed with the deployment. Note that the stack
    itself is counted as a resource, though it does not correspond
    to a physical cloud resource.

    You can also run `pulumi up --diff` to see and inspect the diffs of the
    overall changes expected to take place.

    Running `pulumi up` will deploy the EKS cluster. Note, provisioning a
    new EKS cluster takes between 10-15 minutes.

        $ pulumi up
        Previewing update (eks-demo):

            Type                                          Name                              	Plan
        +   pulumi:pulumi:Stack                           eks-hello-world-eks-demo     			create
        +   ├─ eks:index:Cluster                          helloworld                          	create
        +   │  ├─ eks:index:ServiceRole                   helloworld-eksRole                  	create
        +   │  │  ├─ aws:iam:Role                         helloworld-eksRole-role             	create
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-eksRole-90eb1c99         	create
        +   │  │  └─ aws:iam:RolePolicyAttachment         helloworld-eksRole-4b490823         	create
        +   │  ├─ eks:index:ServiceRole                   helloworld-instanceRole             	create
        +   │  │  ├─ aws:iam:Role                         helloworld-instanceRole-role        	create
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-03516f97    	create
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-e1b295bd    	create
        +   │  │  └─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-3eb088f2    	create
        +   │  ├─ pulumi-nodejs:dynamic:Resource          helloworld-cfnStackName             	create
        +   │  ├─ aws:ec2:SecurityGroup                   helloworld-eksClusterSecurityGroup  	create
        +   │  ├─ aws:iam:InstanceProfile                 helloworld-instanceProfile          	create
        +   │  ├─ aws:eks:Cluster                         helloworld-eksCluster               	create
        +   │  ├─ pulumi-nodejs:dynamic:Resource          helloworld-vpc-cni                  	create
        +   │  ├─ pulumi:providers:kubernetes             helloworld-eks-k8s                  	create
        +   │  ├─ aws:ec2:SecurityGroup                   helloworld-nodeSecurityGroup        	create
        +   │  ├─ kubernetes:core:ConfigMap               helloworld-nodeAccess               	create
        +   │  ├─ kubernetes:storage.k8s.io:StorageClass  helloworld-gp2                      	create
        +   │  ├─ aws:ec2:SecurityGroupRule               helloworld-eksClusterIngressRule    	create
        +   │  ├─ aws:ec2:LaunchConfiguration             helloworld-nodeLaunchConfiguration  	create
        +   │  ├─ aws:cloudformation:Stack                helloworld-nodes                    	create
        +   │  └─ pulumi:providers:kubernetes             helloworld-provider                 	create
        ...

        Resources:
            + 42 to create

        clusterng (eks-demo):

            Type                                          Name                              	Status      Info
        +   pulumi:pulumi:Stack                           eks-hello-world-eks-demo     			created
        +   ├─ eks:index:Cluster                          helloworld                          	created
        +   │  ├─ eks:index:ServiceRole                   helloworld-eksRole                  	created
        +   │  │  ├─ aws:iam:Role                         helloworld-eksRole-role             	created
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-eksRole-90eb1c99         	created
        +   │  │  └─ aws:iam:RolePolicyAttachment         helloworld-eksRole-4b490823         	created
        +   │  ├─ eks:index:ServiceRole                   helloworld-instanceRole             	created
        +   │  │  ├─ aws:iam:Role                         helloworld-instanceRole-role        	created
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-3eb088f2    	created
        +   │  │  ├─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-03516f97    	created
        +   │  │  └─ aws:iam:RolePolicyAttachment         helloworld-instanceRole-e1b295bd    	created
        +   │  ├─ pulumi-nodejs:dynamic:Resource          helloworld-cfnStackName             	created
        +   │  ├─ aws:iam:InstanceProfile                 helloworld-instanceProfile          	created
        +   │  ├─ aws:ec2:SecurityGroup                   helloworld-eksClusterSecurityGroup  	created
        +   │  ├─ aws:eks:Cluster                         helloworld-eksCluster               	created
        +   │  ├─ pulumi:providers:kubernetes             helloworld-eks-k8s                  	created
        +   │  ├─ pulumi-nodejs:dynamic:Resource          helloworld-vpc-cni                  	created
        +   │  ├─ aws:ec2:SecurityGroup                   helloworld-nodeSecurityGroup        	created
        +   │  ├─ kubernetes:core:ConfigMap               helloworld-nodeAccess               	created
        +   │  ├─ kubernetes:storage.k8s.io:StorageClass  helloworld-gp2                      	created
        +   │  ├─ aws:ec2:SecurityGroupRule               helloworld-eksClusterIngressRule    	created
        +   │  ├─ aws:ec2:LaunchConfiguration             helloworld-nodeLaunchConfiguration  	created
        +   │  ├─ aws:cloudformation:Stack                helloworld-nodes                    	created
        +   │  └─ pulumi:providers:kubernetes             helloworld-provider                 	created
        ...

        Diagnostics:
        pulumi:pulumi:Stack (eks-hello-world-eks-demo):

        Outputs:
            kubeconfig: {
                apiVersion     : "v1"
                clusters       : [
                    [0]: {
                        cluster: {
                            certificate-authority-data: "<CERT_DATA>"
                            server                    : "https://<SERVER_ADDR>.us-west-2.eks.amazonaws.com"
                        }
                        name   : "kubernetes"
                    }
                ]
                contexts       : [
                    [0]: {
                        context: {
                            cluster: "kubernetes"
                            user   : "aws"
                        }
                        name   : "aws"
                    }
                ]
                current-context: "aws"
                kind           : "Config"
                users          : [
                    [0]: {
                        name: "aws"
                        user: {
                            exec: {
                                apiVersion: "client.authentication.k8s.io/v1alpha1"
                                args      : [
                                    [0]: "token"
                                    [1]: "-i"
                                    [2]: "helloworld-eksCluster-e9e1711"
                                ]
                                command   : "aws-iam-authenticator"
                            }
                        }
                    }
                ]
            }

        Resources:
            + 42 created

        Duration: 13m7s

        Permalink: https://app.pulumi.com/metral/eks-hello-world/eks-demo/updates/1

## Access the Kubernetes Cluster using Pulumi Providers

Now that we have an instance of Kubernetes running, we may want to create API resources in Kubernetes to manage our workloads through Pulumi.

We can do this by configuring a Pulumi provider for our newly created cluster, and instantiating a new Kubernetes resource object in our Pulumi program. The concept of a provider allows us to abstract away Kubernetes clusters in Pulumi that are indendent of their underyling cloud provider, so that you can operate on and work with your Kubernetes clusters in a standard manner.

1. Create a new Kubernetes Namespace and Deployment:

	This declares a new Kubernetes Namespace, Deployment and Service to be
	created using the Pulumi Kubernetes provider to our cluster.

    Open the existing file `index.ts`, and append the following:

    ```typescript
    // Create a Kubernetes Namespace
    const ns = new k8s.core.v1.Namespace(name, {}, { provider: cluster.provider });

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
            provider: cluster.provider,
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
            provider: cluster.provider,
        }
    );

    // Export the Service name and public LoadBalancer Endpoint
    export const serviceName = service.metadata.apply(m => m.name);
    export const serviceHostname = service.status.apply(s => s.loadBalancer.ingress[0].hostname)
    ```

1. Run `pulumi up`, note the preview diff, and select "yes" to preview and deploy the changes.

    As part of the update, you'll see some new objects in the output: a
    `Namespace` in Kubernetes to deploy into, a `Deployment` resource for
    the NGINX app, and a LoadBalancer `Service` to publicly access NGINX.

    Pulumi understands which changes to a given cloud resource can be made
    in-place, and which require replacement, and computes
    the minimally disruptive change to achieve the desired state. The CLI
    will also output incremental status updates, as the Kubernetes changes progress.

	> **Note:** Pulumi auto-generates a suffix for all objects.
    > See the [Pulumi Programming Model]({{< relref "/docs/intro/concepts/programming-model#autonaming" >}}) for more info.
	>
	> ```
	> ...
	> deploymentName : "helloworld-tlsr4sg5"
	> ...
	> namespaceName  : "helloworld-pz4u5kyq"
	> serviceHostname: "a71f5ab3f2a6e11e3ac39200f4a9ad5d-1297981966.us-west-2.elb.amazonaws.com"
	> serviceName    : "helloworld-l61b5dby"
	> ```

    If you visit the FQDN listed in `serviceHostname` you should land on the
    NGINX welcome page. Note, that it may take a minute or so for the
    LoadBalancer to become active on AWS.

## Access the Kubernetes Cluster using `kubectl`

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file and download `kubectl`. We can leverage the Pulumi stack
output in the CLI, as Pulumi faciliates exporting these objects for us.

```bash
$ pulumi stack output kubeconfig > kubeconfig
$ export KUBECONFIG=`pwd`/kubeconfig
$ export KUBERNETES_VERSION=1.11.5 && sudo curl -s -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl && sudo chmod +x /usr/local/bin/kubectl

$ kubectl version
$ kubectl cluster-info
$ kubectl get nodes
```

We can also use the stack output to query the cluster for our newly created Deployment:

```bash
$ kubectl get deployment $(pulumi stack output deploymentName) --namespace=$(pulumi stack output namespaceName)
$ kubectl get service $(pulumi stack output serviceName) --namespace=$(pulumi stack output namespaceName)
```

We can also create another NGINX Deployment into the `default` namespace using
`kubectl` natively:

```bash
$ kubectl create deployment my-nginx --image=nginx
$ kubectl get pods
$ kubectl delete deployment my-nginx
```

Of course, by doing so, resources are outside of Pulumi's purview, but this simply
demonstrates that all the `kubectl` commands you're used to will work.

## Experimentation

From here on, feel free to experiment with Pulumi. Simply making edits and
running `pulumi up` afterwords, will incrementally update your stack.

### Running Off-the-Shelf Guestbook YAML

For example, if you wish to pull existing Kubernetes YAML manifests into
Pulumi to aid in your transition, append the following code block to the existing
`index.ts` file and run `pulumi up`.

This is an example of how to create the standard Kubernetes Guestbook manifests in
Pulumi using the Guestbook YAML manifests. We take the additional steps of transforming
its properties to use the same Namespace and metadata labels that
the NGINX stack uses, and also make its frontend service use a
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
export const guestbookPublicHostname =
	guestbook.getResourceProperty("v1/Service", "frontend", "status").apply(s => s.loadBalancer.ingress[0].hostname);
```

## Clean up

Run the following command to tear down the resources that are part of our stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources.

1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console and cannot be undone.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and launch a
Managed Kubernetes cluster on AWS EKS.

For a follow-up example on how to use Pulumi programs to create a Kubernetes
apps on your new cluster, see [Kubernetes Tutorial: Getting Started With Pulumi]({{< relref "configmap-rollout" >}}).

We also encourage you to watch Joe Beda, co-founder of Kubernetes and Heptio,
take Pulumi for a spin in an episode of [TGIK8s](https://github.com/heptio/tgik).

<iframe width="560" height="315"
src="https://www.youtube.com/embed/ILMK65YVSKw" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>
