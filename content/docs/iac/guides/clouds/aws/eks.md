---
title_tag: "Using AWS Elastic Kubernetes Service (EKS) | AWS Guides"
title: EKS
h1: AWS Elastic Kubernetes Service (EKS)
meta_desc: Pulumi simplifies the creation, configuration, and management of EKS clusters,
           offering a single programming model and deployment workflow.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  iac:
    parent: iac-guides-clouds-aws
    name: EKS
    identifier: aws-guides-eks
    weight: 60

aliases:
- /docs/integrations/clouds/aws/guides/eks/
- /docs/iac/clouds/aws/guides/eks/
- /docs/reference/crosswalk/aws/eks/
- /eks/
- /docs/guides/crosswalk/aws/eks/
- /docs/clouds/aws/guides/eks/
---

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks) makes it easy to deploy,
manage, and scale containerized applications using Kubernetes on AWS. Amazon EKS runs the Kubernetes management
infrastructure for you across multiple AWS availability zones to eliminate a single point of failure. Amazon EKS is
certified Kubernetes conformant so you can use existing tooling and plugins from partners and the Kubernetes
community. Applications running on any standard Kubernetes environment are fully compatible and can be easily migrated
to Amazon EKS.

## Overview

Pulumi's EKS component simplifies the creation, configuration, and management of EKS clusters. When used in combination with the [Pulumi Kubernetes Provider](/registry/packages/kubernetes/), [AWS Provider](/registry/packages/aws/), and [AWSx component package](/registry/packages/awsx/), you can use a single tool to manage your Kubernetes application configuration as well as your cluster and associated infrastructure.

Amazon EKS runs up-to-date versions of the open-source Kubernetes software, so you can use all the existing plugins and
tooling from the Kubernetes community, including Pulumi's support for deploying Helm charts. Applications running on
Amazon EKS are fully compatible with applications running on any standard Kubernetes environment, whether running in
on-premises data centers or public clouds, easing porting from other Kubernetes environments to EKS.

Expressing your infrastructure and Kubernetes configuration in code using Pulumi ensures your
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

{{< example-program path="aws-eks-cluster-default" >}}

This cluster uses reasonable defaults, like placing the cluster into your default VPC with a CNI interface, using
AWS IAM Authenticator to leverage IAM for secure access to your cluster, and using two `t2.medium` nodes.

After running `pulumi up`, we will see the resulting cluster's `kubeconfig` file exported for easy access:

```bash
$ pulumi up
Updating (dev):

     Type                       Name                            Status
 +   pulumi:pulumi:Stack        eks-cluster-dev                 created
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

By default, Pulumi targets clusters based on your local kubeconfig, just like `kubectl` does. So if your `kubectl`
client is set up to talk to your EKS cluster, deployments will target it. We saw earlier in
[Provisioning a New EKS Cluster](#provisioning-a-new-eks-cluster), however, that you can deploy into any
Kubernetes cluster created in your Pulumi program. This is because each Kubernetes object specification accepts
an optional "provider" that can programmatically specify a kubeconfig to use.

This is done by instantiating a new `kubernetes.Provider` object, and providing one or many of these properties:

* `cluster`: A cluster name to target, if there are many in your kubeconfig to choose from.
* `context`: The name of the kubeconfig context to use, if there are many to choose from.
* `kubeconfig`: A stringified JSON representing a full kubeconfig to use instead of your local machine's.

From here, we have a fully functioning EKS cluster in Amazon, which we can deploy Kubernetes applications to.
Any existing tools will work here, including `kubectl`, Helm, and other CI/CD products. Pulumi offers the ability
to define Kubernetes application-level objects and configuration in code too. For instance, we can deploy a canary
to our EKS cluster in the same program if we want to test that it is working as part of `pulumi up`:

{{< example-program path="aws-eks-cluster-k8s-canary" >}}

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
arguments to the constructor. For instance, this example changes the desired capacity and enables certain cluster
logging types:

{{< example-program path="aws-eks-cluster-settings" >}}

For a full list of options that you may set on your cluster, see the [API documentation](/registry/packages/eks/api-docs/cluster/#inputs). Many common cases are described below.

## Configuring Your EKS Cluster's Networking

By default, your EKS cluster is put into your region's default VPC. This is a reasonable default, however this is
configurable if you want specific network isolation or to place your cluster work nodes on private subnets. This works
in conjunction with [the Pulumi VPC guide](/docs/clouds/aws/guides/vpc/), which makes configuring VPCs easier.

This example creates a new VPC with private subnets only and creates our EKS cluster inside of it:

{{< example-program path="aws-eks-cluster" >}}

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

If you would like to disable the creation of a default node group, and instead rely on creating your own, pass
[`skipDefaultNodeGroup`](/registry/packages/eks/api-docs/cluster/#skipdefaultnodegroup_nodejs)
as `true` to the `eks.Cluster` constructor. Additional node groups may then be created by
[creating an `eks.NodeGroupV2`](/registry/packages/eks/api-docs/nodegroupv2) explicitly. In both cases, you
would likely want to configure IAM roles for your worker nodes explicitly, which can be supplied to your EKS cluster
using the [`instanceRole`](/registry/packages/eks/api-docs/cluster/#instancerole_nodejs) or
[`instanceRoles`](/registry/packages/eks/api-docs/cluster/#instanceroles_nodejs) properties.

For instance, let's say we want to have two node groups: one for our fixed, known workloads, and another that is
burstable and might use more expensive compute, but which can be scaled down when possible (possibly to zero).
We would skip the default node group, and create our own node groups:

{{< example-program path="aws-eks-cluster-node-groups" >}}

After configuring such a cluster, we would then want to ensure our workload's pods are scheduled correctly on the
right nodes. To do so, you will use a combination of node selectors, taints, and/or tolerances. For more information,
see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) and
[Taints and Tolerances](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/).

## Managing EKS Cluster Authentication with IAM

When you create an Amazon EKS cluster, the IAM entity user or role (for example, for federated users) that creates the
cluster is automatically granted `system:masters` permissions in the cluster's RBAC configuration. To grant additional
AWS users or roles the ability to interact with your cluster, you must edit the `aws-auth` ConfigMap within Kubernetes.

The [`roleMappings` property](/registry/packages/eks/api-docs/cluster/#rolemappings_nodejs)
for your EKS cluster lets you configure custom IAM roles. For example, you can create different IAM roles for cluster
admins, automation accounts (for CI/CD), and production roles, and supply them to `roleMappings`; this has the effect of
placing them in the `aws-auth` ConfigMap for your cluster automatically. Pulumi also lets you configure Kubernetes
objects, so that can also then create the RBAC cluster role bindings in your cluster to tie everything together.

For a complete example of this in action, see
[Simplifying Kubernetes RBAC in Amazon EKS](/blog/simplify-kubernetes-rbac-in-amazon-eks-with-open-source-pulumi-packages/).

## Deploying Kubernetes Apps to Your EKS Cluster

Pulumi supports the entire Kubernetes object model in the [@pulumi/kubernetes](/registry/packages/kubernetes/api-docs)
package. For more information on these object types, including Deployments, Services, and Pods, see
[Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

With Pulumi, you describe your desired Kubernetes configuration, and `pulumi up` will diff between the current
state and what is desired, and then drive the API server to bring your desired state into existence.

For example, this program creates a simple load balanced NGINX service, exporting its URL:

{{< example-program path="aws-k8s-nginx-deploy" >}}

Running `pulumi up` deploys these Kubernetes objects, providing rich status updates along the way:

```bash
Updating (dev):

     Type                           Name               Status
     pulumi:pulumi:Stack            eks-cluster-dev
 +   ├─ kubernetes:core:Service     my-app-svc         created
 +   └─ kubernetes:apps:Deployment  my-app-dep         created

Outputs:
 + url       : "a2861638e011e98a329401e61c-1335818318.us-west-2.elb.amazonaws.com"

Resources:
    + 2 created

Duration: 22s
```

## Deploying Existing Kubernetes YAML Config to Your EKS Cluster

Specifying your Kubernetes object configurations in Pulumi lets you take advantage of programming language features,
like variables, loops, conditionals, functions, and classes. It is possible, however, to deploy existing Kubernetes
YAML. The two approaches can be mixed, which is useful when converting an existing project.

The [`ConfigFile` class](/registry/packages/kubernetes/api-docs/yaml/v2/configfile) can be
used to deploy a single YAML file, whereas the [`ConfigGroup` class](
/registry/packages/kubernetes/api-docs/yaml/v2/configgroup) can deploy
a collection of files, either from a set of files or in-memory representations.

For example, imagine we have a directory, `yaml/`, containing the full YAML for the [Kubernetes Guestbook application](
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/), perhaps across multiple files. We can deploy
it using Pulumi into our EKS cluster with the following code and by running `pulumi up`:

{{< example-program path="aws-eks-k8s-configgroup" >}}

The `ConfigFile` and `ConfigGroup` classes support [`transforms`](
/docs/concepts/options/transforms/) via `ResourceOptions`, which can be used to ['monkey patch'](
https://en.wikipedia.org/wiki/Monkey_patch) Kubernetes configuration on the fly. This can be used to rewrite
configuration to include additional services (like Envoy sidecars), inject tags, and so on.

For example, a transformation like the following can make all services private to a cluster, by
changing `LoadBalancer` specs into `ClusterIPs`, in addition to placing objects into a desired namespace:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
{{< example-program-snippet path="aws-eks-k8s-configgroup-transform" language="typescript" from="10" to="28" >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< example-program-snippet path="aws-eks-k8s-configgroup-transform" language="python" from="10" to="30" >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< example-program-snippet path="aws-eks-k8s-configgroup-transform" language="go" from="31" to="55" >}}
{{% /choosable %}}

{{% choosable language csharp %}}
{{< example-program-snippet path="aws-eks-k8s-configgroup-transform" language="csharp" from="23" to="51" >}}
{{% /choosable %}}

{{% choosable language java %}}
{{% notes type="info" %}}
Transforms are not yet supported for this resource in Java.
{{% /notes %}}
{{% /choosable %}}

{{% choosable language yaml %}}
{{% notes type="info" %}}
Transforms are not yet supported for this resource in Pulumi YAML.
{{% /notes %}}
{{% /choosable %}}

Of course, it is easy to create invalid transformations that break your applications, by changing settings the
application or configuration did not expect, so this capability must be used with care.

## Deploying Existing Helm Charts to Your EKS Cluster

Pulumi can deploy [Helm charts](https://helm.sh/) through a variety of means. This includes deploying a chart
by name from any Helm repository (over the Internet or on-premises), or from a tarball directly.

> For these examples to work, you will need to [install Helm](https://helm.sh/docs/intro/install/).

This program installs the Wordpress chart into our EKS cluster, using the [Release resource type](/registry/packages/kubernetes/api-docs/helm/v3/release/):

{{< example-program path="aws-eks-helm-wordpress" >}}

The `values` array provides the configurable parameters for the chart. If we leave off the `version`, the latest
available chart will be fetched from the repository (including on subsequent updates, which may trigger an upgrade).

The `getResource` function on a chart can be used to get an internal resource provisioned by the chart.
Sometimes this is needed to discover attributes such as a provisioned load balancer's address. Be careful when
depending on this, however, as it is an implementation detail of the chart and will change as the chart evolves.

> Note that Pulumi support for Helm does not use Tiller. There are known problems, particularly around security,
> with Tiller, and so the Helm project is discouraging its use and
> [deprecating it as part of Helm](https://helm.sh/docs/faq/#removal-of-tiller). As a result of this, certain
> charts that depend on Tiller being present will not work with Pulumi. This is by design, affects only a
> small number of charts, and given Helm's direction, this should be considered a bug in the chart itself.

Alternatively, we can use a tarball fetched from a web URL:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="typescript" from="3" to="5" >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="python" from="3" to="3" >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="go" from="8" to="18" >}}
{{% /choosable %}}

{{% choosable language csharp %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="csharp" from="5" to="12" >}}
{{% /choosable %}}

{{% choosable language java %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="java" from="6" to="17" >}}
{{% /choosable %}}

{{% choosable language yaml %}}
{{< example-program-snippet path="aws-eks-helm-tarball" language="yaml" from="4" to="8" >}}
{{% /choosable %}}

## Using an ECR Container Image from an EKS Kubernetes Deployment

[The Pulumi ECR component](/docs/clouds/aws/guides/ecr/) enables you to build, publish, and consume private Docker
images easily using Amazon's Elastic Container Registry (ECR). In the following example, creating an `Image` resource will
build an image from the "./app" directory (relative to the project and containing Dockerfile), and publish it to the
provisioned ECR repository.

> *Note:* for more complete examples of building and publishing to _any_ private container registry, including AWS, Azure,
> Google Cloud, and the Docker Hub, please refer to the article [Build and publish container images to any cloud with
> Infrastructure as Code](/blog/build-publish-containers-iac/).

For example, let's say we have an `app/` directory containing a fully Dockerized application (including a
`Dockerfile`), and would like to deploy that as a Deployment and Service running in our EKS cluster. This program
accomplishes this with a single `pulumi up` command:

{{< example-program path="awsx-ecr-eks-deployment-service" >}}

For more information about ECR, see [the Pulumi ECR documentation](/docs/clouds/aws/guides/ecr/).

## Additional EKS Resources

For more information about Kubernetes and EKS, see the following:

* [Pulumi Kubernetes API Documentation](/registry/packages/kubernetes/api-docs/)
* [Pulumi EKS API Documentation](/registry/packages/eks/api-docs/)
* [Amazon Elastic Kubernetes Service homepage](https://aws.amazon.com/eks/)
* [Kubernetes Documentation](https://kubernetes.io)
