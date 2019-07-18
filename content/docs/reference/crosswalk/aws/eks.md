---
title: "AWS Elastic Kubernetes Service (EKS)"
menu:
  reference:
    parent: crosswalk-aws
    name: Elastic Kubernetes Service (EKS)
    weight: 6
---

<a href="{{< relref "_index.md" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks) makes it easy to deploy,
manage, and scale containerized applications using Kubernetes on AWS. Amazon EKS runs the Kubernetes management
infrastructure for you across multiple AWS availability zones to eliminate a single point of failure. Amazon EKS is
certified Kubernetes conformant so you can use existing tooling and plugins from partners and the Kubernetes
community. Applications running on any standard Kubernetes environment are fully compatible and can be easily migrated
to Amazon EKS.

{{< mini-toc >}}

## Overview

Pulumi Crosswalk for AWS simplifies the creation, configuration, and management of EKS clusters, in addition to
offering a single programming model and deployment workflow that works for your Kubernetes application configuration,
in addition to infrastructure. This support ensures your EKS resources are fully integrated properly with the
related AWS services. This includes

* [ECR]({{< relref "ecr.md" >}}) for private container images
* [ELB]({{< relref "elb.md" >}}) for load balancing
* [IAM]({{< relref "iam.md" >}}) for security
* [VPC]({{< relref "vpc.md" >}}) for network isolation
* [CloudWatch]({{< relref "cloudwatch.md" >}}) for monitoring

Amazon EKS runs up-to-date versions of the open-source Kubernetes software, so you can use all the existing plugins and
tooling from the Kubernetes community, including Pulumi's support for deploying Helm charts. Applications running on
Amazon EKS are fully compatible with applications running on any standard Kubernetes environment, whether running in
on-premises data centers or public clouds, easing porting from other Kubernetes environments to EKS.

Expressing your infrastructure and Kubernetes configuration in code using Pulumi Crosswalk for AWS ensures your
resulting system is ready for production using built-in best practices.

## Prerequisites

Before getting started, you will need to install some pre-requisites:

* [`aws-iam-authenticator`](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html):
  Amazon EKS uses IAM to provide secure authentication to your Kubernetes cluster.

These are not required but are recommended if you plan on interacting with your Kubernetes cluster:

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/): the standard Kubernetes command line interface.
* [`helm`](https://helm.sh/docs/using_helm/): if you plan on deploying Helm charts to your cluster.

## Provisioning a New EKS Cluster

To create a new EKS cluster, allocate an instance of an `eks.Cluster` class in your Pulumi program:

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

This cluster uses reasonable defaults, like placing the cluster into your default VPC with a CNI interface, using
AWS IAM Authenticator to leverage IAM for secure access to your cluster, and using two `t2.medium` nodes.

After running `pulumi up`, we will see the resulting cluster's `kubeconfig` file exported for easy access:

```bash
$ pulumi up
Updating (dev):

     Type                       Name                            Status
 +   pulumi:pulumi:Stack        crosswalk-aws-dev               created
 +   └─ eks:index:Cluster       my-cluster                      created
     ... dozens of resources omitted ...

Outputs:
    kubeconfig: {
        apiVersion     : "v1"
        clusters       : [
            [0]: {
                cluster: {
                    certificate-authority-data: "...",
                    server                    : "https://D34E7144F46CB.sk1.us-west-2.eks.amazonaws.com"
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
                            [2]: "my-cluster-eksCluster-22c2275"
                        ]
                        command   : "aws-iam-authenticator"
                    }
                }
            }
        ]
    }

Resources:
    + 43 created

Duration: 11m26s
```

It is easy to take this file and use it with the `kubectl` CLI:

```bash
$ pulumi stack output kubeconfig > kubeconfig.yml
$ KUBECONFIG=./kubeconfig.yml kubectl get nodes
NAME                                         STATUS    ROLES     AGE       VERSION
ip-172-31-29-62.us-west-2.compute.internal   Ready     <none>    1m       v1.12.7
ip-172-31-40-32.us-west-2.compute.internal   Ready     <none>    2m       v1.12.7
```

From here, we have a fully functioning EKS cluster in Amazon, which we can deploy Kubernetes applications to.
Any existing tools will work here, including `kubectl`, Helm, and other CI/CD products. Pulumi offers the ability
to define Kubernetes application-level objects and configuration in code too. For instance, we can deploy a canary
to our EKS cluster in the same program if we want to test that it is working as part of `pulumi up`:

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

// Deploy a small canary service (NGINX), to test that the cluster is working.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

If we deploy this on top of our existing EKS cluster, we will see the diff is just the creation of Kubernetes
Deployment and Service objects, and the resulting URL for the load balanced service will be printed out. We
can see that Pods have been spun up and we can use this URL to check the health of our cluster:

```bash
$ pulumi stack output kubeconfig > kubeconfig.yml
$ KUBECONFIG=./kubeconfig.yml kubectl get po
NAME                                 READY     STATUS    RESTARTS   AGE
my-app-de-6gfz4ap5-dc8c6584f-6xmcl   1/1       Running   0          3m
my-app-de-6gfz4ap5-dc8c6584f-wzlf9   1/1       Running   0          3m
$ curl http://$(pulumi stack output url)
<html>
<head>
<title>Welcome to nginx!</title>
</head>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

For more detail on how to deploy Kubernetes applications using Pulumi, refer to one of these sections:

* [Deploying Kubernetes Apps to Your EKS Cluster](#deploying-kubernetes-apps-to-your-eks-cluster)
* [Deploying Existing Kubernetes YAML Config to Your EKS Cluster](#deploying-existing-kubernetes-yaml-config-to-your-eks-cluster)
* [Deploying Existing Helm Charts to Your EKS Cluster](#deploying-existing-helm-charts-to-your-eks-cluster)

## Changing the Default Settings on an EKS Cluster

The above example showed using the default settings for your EKS cluster. It is easy to override them by passing
arguments to the constructor. For instance, this example changes the desired capacity, disables the Kubernetes
dashboard, and enables certain cluster logging types:

```typescript
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster", {
    desiredCapacity: 5,
    minSize: 3,
    maxSize: 5,
    deployDashboard: false,
    enabledClusterLogTypes: [
        "api",
        "audit",
        "authenticator",
    ],
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

For a full list of options that you may set on your cluster, please [see the API documentation](
{{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#ClusterOptions" >}}). Many common cases are described below.

## Configuring Your EKS Cluster's Networking

By default, your EKS cluster is put into your region's default VPC. This is a reasonable default, however this is
configurable if you want specific network isolation or to place your cluster work nodes on private subnets. This works
in conjunction with [Pulumi Crosswalk for AWS VPC]({{< relref "vpc.md" >}}) which makes configuring VPCs easier.

This example creates a new VPC with private subnets only and creates our EKS cluster inside of it:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc");
const allVpcSubnets = vpc.privateSubnetIds.concat(vpc.publicSubnetIds);

// Create an EKS cluster inside of the VPC.
const cluster2 = new eks.Cluster("my-cluster", {
    vpcId: vpc.vpcId,
    subnetIds: allVpcSubnets,
    nodeAssociatedPublicIpAddress: false,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

When you create an Amazon EKS cluster, you specify the Amazon VPC subnets for your cluster to use. These must be
in at least two Availability Zones. We recommend a network architecture that uses private subnets for your
worker nodes and public subnets for Kubernetes to create Internet-facing load balancers within. When you create your
cluster, specify all of the subnets that will host resources for your cluster (including workers and load balancers).

In the above example, we passed both the private and public subnets from our VPC. The EKS package
figures out which ones are public and which ones are private -- and creates the worker nodes inside
only the private subnets if any are specified. EKS will tag the provided subnets so that Kubernetes
can discover them.   If additional control is needed over how load balancers are allocated to
subnets, users can attach additional subnet tags themselves as outlined in
[Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html).

> Note that by default the `eks.Cluster` will do the same as what is described here, just inside of the default
> VPC inside of your account, rather than a custom VPC as shown in this example.

## Configuring Your EKS Cluster's Worker Nodes and Node Groups

Worker machines in Kubernetes are called nodes. Amazon EKS worker nodes run in your AWS account and connect to your
cluster's control plane via the cluster API server endpoint. These are standard Amazon EC2 instances, and you are
billed for them based on normal EC2 On-Demand prices. By default, an AMI using Amazon Linux 2 is used as the base
image for EKS worker nodes, and includes Docker, kubelet, and the AWS IAM Authenticator.

Nodes exist in groups and you can create multiple groups for workloads that require it. By default, your EKS cluster
is given a default node group, with the instance sizes and counts that you specify (or the defaults of two `t2.medium`
instances otherwise). The latest version of Kubernetes available is used by default.

If you would like to disable the creation of a default node group, and instead rely on creating your own, simply pass
[`skipDefaultNodeGroup`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#ClusterOptions-skipDefaultNodeGroup" >}})
as `true` to the `eks.Cluster` constructor. Additional node groups may then be created by calling
[the `createNodeGroup` function]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#Cluster-createNodeGroup" >}}) on
your EKS cluster, or by [creating an `eks.NodeGroup`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#NodeGroup" >}})
explicitly. In both cases, you are likely to want to configure IAM roles for your worker nodes explicitly, which can be
supplied to your EKS cluster using the
[`instanceRole`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#ClusterOptions-instanceRole" >}}) or
[`instanceRoles`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#ClusterOptions-instanceRoles" >}}) properties.

For instance, let's say we want to have two node groups: one for our fixed, known workloads, and another that is
burstable and might use more expensive compute, but which can be scaled down when possible (possibly to zero).
We would skip the default node group, and create our own node groups:

```typescript
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";

/**
 * Per NodeGroup IAM: each NodeGroup will bring its own, specific instance role and profile.
 */

const managedPolicyArns: string[] = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];

// Creates a role and attaches the EKS worker node IAM managed policies. Used a few times below,
// to create multiple roles, so we use a function to avoid repeating ourselves.
export function createRole(name: string): aws.iam.Role {
    const role = new aws.iam.Role(name, {
        assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
            Service: "ec2.amazonaws.com",
        }),
    });

    let counter = 0;
    for (const policy of managedPolicyArns) {
        // Create RolePolicyAttachment without returning it.
        const rpa = new aws.iam.RolePolicyAttachment(`${name}-policy-${counter++}`,
            { policyArn: policy, role: role },
        );
    }

    return role;
}

// Now create the roles and instance profiles for the two worker groups.
const role1 = createRole("my-worker-role1");
const role2 = createRole("my-worker-role2");
const instanceProfile1 = new aws.iam.InstanceProfile("my-instance-profile1", {role: role1});
const instanceProfile2 = new aws.iam.InstanceProfile("my-instance-profile2", {role: role2});

// Create an EKS cluster with many IAM roles to register with the cluster auth.
const cluster = new eks.Cluster("my-cluster", {
    skipDefaultNodeGroup: true,
    instanceRoles: [ role1, role2 ],
});

// Now create multiple node groups, each using a different instance profile for each role.

// First, create a node group for fixed compute.
const fixedNodeGroup = cluster.createNodeGroup("my-cluster-ng1", {
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    labels: {"ondemand": "true"},
    instanceProfile: instanceProfile1,
});

// Now create a preemptible node group, using spot pricing, for our variable, ephemeral workloads.
const spotNodeGroup = new eks.NodeGroup("my-cluster-ng2", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 1,
    spotPrice: "1",
    minSize: 1,
    maxSize: 2,
    labels: {"preemptible": "true"},
    taints: {
        "special": {
            value: "true",
            effect: "NoSchedule",
        },
    },
    instanceProfile: instanceProfile2,
}, {
    providers: { kubernetes: cluster.provider},
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

After configuring such a cluster, we would then want to ensure our workload's pods are scheduled correctly on the
right nodes. To do so, you will use a combination of node selectors, taints, and/or tolerances. For more information,
please see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) and
[Taints and Tolerances](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/).

## Managing EKS Cluster Authentication with IAM

When you create an Amazon EKS cluster, the IAM entity user or role (for example, for federated users) that creates the
cluster is automatically granted `system:masters` permissions in the cluster's RBAC configuration. To grant additional
AWS users or roles the ability to interact with your cluster, you must edit the `aws-auth` ConfigMap within Kubernetes.

The [`roleMappings` property]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#ClusterOptions-roleMappings" >}})
for your EKS cluster lets you configure custom IAM roles. For example, you can create different IAM roles for cluster
admins, automation accounts (for CI/CD), and production roles, and supply them to `roleMappings`; this has the effect of
placing them in the `aws-auth` ConfigMap for your cluster automatically. Pulumi also lets you configure Kubernetes
objects, so that can also then create the RBAC cluster role bindings in your cluster to tie everything together.

For a complete example of this in action, please see
[Simplifying Kubernetes RBAC in Amazon EKS]({{< relref "simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages" >}}).

## Deploying Kubernetes Apps to Your EKS Cluster

Pulumi supports the entire Kubernetes object model in the [@pulumi/kubernetes]({{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes" >}})
package. For more information on these object types, including Deployments, Services, and Pods, please see
[Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

With Pulumi, you describe your desired Kubernetes configuration, and `pulumi up` will diff between the current
state and what is desired, and then drive the API server to bring your desired state into existence.

For example, this program creates a simple load balanced NGINX service, exporting its URL:

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create an NGINX Deployment and load balanced Service.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
});
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
});

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

Running `pulumi up` deploys these Kubernetes objects, providing rich status updates along the way:

```bash
Updating (dev):

     Type                           Name               Status
     pulumi:pulumi:Stack            crosswalk-aws-dev
 +   ├─ kubernetes:core:Service     my-app-svc         created
 +   └─ kubernetes:apps:Deployment  my-app-dep         created

Outputs:
 + url       : "a2861638e011e98a329401e61c-1335818318.us-west-2.elb.amazonaws.com"

Resources:
    + 2 created

Duration: 22s
```

### Deploying to Specific Clusters

By default, Pulumi targets clusters based on your local kubeconfig, just like `kubectl` does. So if your `kubectl`
client is set up to talk to your EKS cluster, deployments will target it. We saw earlier in
[Provisioning a New EKS Cluster](#provisioning-a-new-eks-cluster), however, that you can deploy into any
Kubernetes cluster created in your Pulumi program. This is because each Kubernetes object specification accepts
an optional "provider" that can programmatically specify a kubeconfig to use.

This is done by instantiating a new `kubernetes.Provider` object, and providing one or many of these properties:

* `cluster`: A cluster name to target, if there are many in your kubeconfig to choose from.
* `context`: The name of the kubeconfig context to use, if there are many to choose from.
* `kubeconfig`: A stringified JSON representing a full kubeconfig to use instead of your local machine's.

For example, to deploy an NGINX Deployment into a cluster whose kubeconfig our program has access to:

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a provider using our Kubernetes config:
const provider = new k8s.Provider("custom-provider", { kubeconfig: "..." });

// Declare a deployment that targets this provider:
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`,
    {
        metadata: { labels: appLabels },
        spec: {
            replicas: 2,
            selector: { matchLabels: appLabels },
            template: {
                metadata: { labels: appLabels },
                spec: {
                    containers: [{
                        name: appName,
                        image: "nginx",
                        ports: [{ name: "http", containerPort: 80 }]
                    }],
                }
            }
        },
    },
    {
        // Use our custom provider for this object.
        provider: provider,
    },
);
```

To ease doing this against an EKS cluster just created, the cluster object itself offers a [`provider` property](
{{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md#Cluster-provider" >}}) of type `kubernetes.Provider`, already pre-configured.

For more information about configuring access to multiple clusters, see [Configure Access to Multiple Clusters](
https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) and the
[Pulumi Kubernetes Setup documentation]({{< relref "/docs/reference/clouds/kubernetes/setup.md" >}}).

## Deploying Existing Kubernetes YAML Config to Your EKS Cluster

Specifying your Kubernetes object configurations in Pulumi lets you take advantage of programming language features,
like variables, loops, conditionals, functions, and classes. It is possible, however, to deploy existing Kubernetes
YAML. The two approaches can be mixed, which is useful when converting an existing project.

The [`ConfigFile` class]({{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes/yaml/_index.md#ConfigFile" >}}) can be
used to deploy a single YAML file, whereas the [`ConfigGroup` class](
{{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes/yaml/_index.md#ConfigFile" >}}) can deploy
a collection of files, either from a set of files or in-memory representations.

For example, imagine we have a directory, `yaml/`, containing the full YAML for the [Kubernetes Guestbook application](
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/), perhaps across multiple files. We can deploy
it using Pulumi into our EKS cluster with the following code and by running `pulumi up`:

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.ConfigGroup("guestbook",
    { files: "yaml/*.yaml" },
    { provider: cluster.provider },
);

// Export the (cluster-private) IP address of the Guestbook frontend.
export const frontendIp = guestbook.getResource("v1/Service", "frontend", "spec").clusterIP;
```

The `ConfigFile` and `ConfigGroup` classes both support a [`transformations` property](
{{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes/_index.md#ConfigGroup-transformations" >}}) which can be used to ["monkey patch"](
https://en.wikipedia.org/wiki/Monkey_patch) Kubernetes configuration on the fly. This can be used to rewrite
configuration to include additional services (like Envoy sidecars), inject tags, and so on.

For example, a transformation like the following can make all services private to a cluster, by
changing `LoadBalancer` specs into `ClusterIPs`, in addition to placing objects into a desired namespace:

```typescript
const guestbook = new k8s.yaml.ConfigGroup("guestbook",
    {
        files: "yaml/*.yaml",
        transformations: [
            (obj: any) => {
                // Make every service private to the cluster.
                if (obj.kind == "Service" && obj.apiVersion == "v1") {
                    if (obj.spec && obj.spec.type && obj.spec.type == "LoadBalancer") {
                        obj.spec.type = "ClusterIP";
                    }
                }
            },
            // Put every resource in the created namespace.
            (obj: any) => {
                if (obj.metadata !== undefined) {
                    obj.metadata.namespace = namespaceName
                } else {
                    obj.metadata = {namespace: namespaceName}
                }
            }
        ],
    },
);
```

Of course, it is easy to create invalid transformations that break your applications, by changing settings the
application or configuration did not expect, so this capability must be used with care.

## Deploying Existing Helm Charts to Your EKS Cluster

Pulumi can deploy [Helm charts](https://helm.sh/) through a variety of means. This includes deploying a chart
by name from the [default Helm "stable charts" repository](https://github.com/helm/charts), from a custom Helm
repository (over the Internet or on-premises), or from a tarball directly.

> For these examples to work, you will need to [install Helm](https://helm.sh/docs/using_helm/#installing-helm)
> and, once installed, initialize it with `helm init --client-only`.

This program installs the stable Wordpress chart into our EKS cluster:

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Deploy Wordpress into our cluster.
const wordpress = new k8s.helm.v2.Chart("wordpress", {
    repo: "stable",
    chart: "wordpress",
    values: {
        wordpressBlogName: "My Cool Kubernetes Blog!",
    },
}, { providers: { "kubernetes": cluster.provider } });

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

The `values` array provides the configurable parameters for the chart. If we leave off the `version`, the latest
available chart will be fetched from the repository (including on subsequent updates, which may trigger an upgrade).

The `getResourceProperty` function on a chart can be used to get an internal resource provisioned by the chart.
Sometimes this is needed to discover attributes such as a provisioned load balancer's address. Be careful when
depending on this, however, as it is an implementation detail of the chart and will change as the chart evolves.

> Note that Pulumi support for Helm does not use Tiller. There are known problems, particularly around security,
> with Tiller, and so the Helm project is discouraging its use and
> [deprecating it as part of Helm](https://github.com/helm/helm/wiki/Roadmap). As a result of this, certain
> charts that depend on Tiller being present will not work with Pulumi. This is by design, affects only a
> small number of charts, and given Helm's direction, this should be considered a bug in the chart itself.

As mentioned, there are other ways to fetch the chart's contents. For example, we can use a custom repo:

```typescript
const chart = new k8s.helm.v2.Chart("empty", {
    chart: "raw",
    version: "0.1.0",
    fetchOpts: {
        repo: "https://kubernetes-charts-incubator.storage.googleapis.com/",
    },
});
```

Or, we can use a tarball fetched from a web URL:

```typescript
const chart = new k8s.helm.v2.Chart("empty1", {
    chart: "https://kubernetes-charts-incubator.storage.googleapis.com/raw-0.1.0.tgz",
});
```

## Using an ECR Container Image from an EKS Kubernetes Deployment

[Pulumi Crosswalk for AWS ECR]({{< relref "ecr.md" >}}) enables you to build, publish, and consume private Docker
images easily using Amazon's Elastic Container Registry (ECR). The [`aws.ecr.buildAndPushImage` function](
{{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ecr/_index.md#buildAndPushImage" >}}) takes a name and a relative location on disk, and will

* Provision a private ECR registry using that name
* Build the `Dockerfile` found at the relative location supplied
* Push the resulting image to that registry
* Return the repository image information, including an image name your Kubernetes objects can use

This makes it easy to version your container images alongside the Kubernetes specifications that consume them.

For example, let's say we have an `app/` directory containing a fully Dockerized application (including a
`Dockerfile`), and would like to deploy that as a Deployment and Service running in our EKS cluster. This program
accomplishes this with a single `pulumi up` command:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create a new EKS cluster.
const cluster = new eks.Cluster("cluster");

// Create a NGINX Deployment and load balanced Service, running our app.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: awsx.ecr.buildAndPushImage("my-repo", "./app").image(),
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

For more information about ECR, please see [the Pulumi Crosswalk for AWS ECR documentation]({{< relref "ecr.md" >}}).

## Additional EKS Resources

For more information about Kubernetes and EKS, please see the following:

* [Pulumi Kubernetes API Documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes" >}})
* [Pulumi EKS API Documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks/_index.md" >}})
* [Amazon Elastic Kubernetes Service homepage](https://aws.amazon.com/eks/)
* [Kubernetes Documentation](https://kubernetes.io)
