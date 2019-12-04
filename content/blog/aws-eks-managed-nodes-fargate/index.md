---
title: "How to Scale Your Amazon EKS Cluster: EC2, Managed Node Groups, and Fargate"
authors: ["joe-duffy"]
tags: ["Pulumi-News", "AWS", "Kubernetes", "EKS"]
meta_desc: "."
date: "2019-12-04"

meta_image: "pulumi-eks-fargate.png"
---

AWS announced two new features just this week aimed at simplifying cluster management in their managed Kubernetes offering, Elastic Kubernetes Service (EKS): Managed Node Groups and Fargate support. We are now happy to announce that we've integrated support for both of these, including easy-to-use APIs in Pulumi Crosswalk, to the base EKS support customers have been using to run clusters in production since the service became generally available over a year ago. The result is a great spectrum of options for managing your cluster's compute &mdash; offering ease-of-use, in addition to full control and flexibility, based on your needs.

## EKS and Your Options

As of these new announcements, you have three primary options for powering your Kubernetes clusters:

* **Fargate**: Let AWS Fargate manage and scale your pods automatically and dynamically as needed
* **Managed Node Groups**: Let EKS manage and scale node pools based on declarative capacity specifications
* **EC2**: Manage EKS clusters by hand, using explicit node groups, EC2 instances, and Auto Scaling Groups (ASG)

These options control how your cluster's worker nodes are provisioned, managed, and scale. These worker nodes are what physically run the compute and host the storage used by your Kubernetes pods. The spectrum of options available provide a range of flexibility, from least control to most control for these worker nodes.

As Abby put it:

{{< tweet 1202020186234048512 >}}

Let's now see how each of these work. To fully appreciate the simplifications afforded by the easier options, we will go in the reverse order &mdash; from most control and most difficult, to the least control and easiest, option.

## Provisioning EKS Clusters

Running a Kubernetes cluster isn't easy, but Amazon EKS makes the task of doing so much simpler. It offers out-of-the-box integrations with essential AWS sevices like IAM, EBS, Route53, and CloudWatch.

It is great to have all of the building blocks at your fingertips, and the `@pulumi/aws` package [exposes all of the raw capabilities of EKS to you](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/aws/eks/#Cluster). We also created the `@pulumi/eks` package to simplify common tasks, however, including provisioning the Kubernetes data plane, configuring VPC/CNI and subnet networking, and managing node groups &mdash; this is what we'll use in our examples.

Provisioning a new EKS cluster today is already as simple as a dozen lines of code:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc");

// Create the EKS cluster itself, including a "gp2"-backed StorageClass.
const cluster = new eks.Cluster("my-cluster", {
    vpcId: vpc.vpcId,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    instanceType: "t2.medium",
    desiredCapacity: 5,
    minSize: 3,
    maxSize: 7,
    storageClasses: "gp2",
    deployDashboard: false,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

[This program](https://github.com/pulumi/examples/tree/master/aws-ts-eks), when deployed with `pulumi up`, will provision an entire EKS cluster, all of its related infrastructure and internal Kubernetes resources, and then print out the `kubeconfig` that can be used to access the cluster afterwards:

```
$ pulumi up
Updating (dev):

     Type                                          Name                                       Status
 +   pulumi:pulumi:Stack                           aws-ts-eks-dev                             created
 +   ├─ awsx:network:Network                       vpc                                        created
 +   │  ├─ aws:ec2:Vpc                             vpc                                        created
 +   │  ├─ aws:ec2:InternetGateway                 vpc                                        created
 +   │  ├─ aws:ec2:Subnet                          vpc-0                                      created
 +   │  ├─ aws:ec2:Subnet                          vpc-1                                      created
 +   │  ├─ aws:ec2:RouteTable                      vpc                                        created
 +   │  ├─ aws:ec2:RouteTableAssociation           vpc-0                                      created
 +   │  └─ aws:ec2:RouteTableAssociation           vpc-1                                      created
 +   └─ eks:index:Cluster                          cluster                                    created
 +      ├─ eks:index:ServiceRole                   cluster-instanceRole                       created
 +      │  ├─ aws:iam:Role                         cluster-instanceRole-role                  created
 +      │  ├─ aws:iam:RolePolicyAttachment         cluster-instanceRole-e1b295bd              created
 +      │  ├─ aws:iam:RolePolicyAttachment         cluster-instanceRole-3eb088f2              created
 +      │  └─ aws:iam:RolePolicyAttachment         cluster-instanceRole-03516f97              created
 +      ├─ eks:index:ServiceRole                   cluster-eksRole                            created
 +      │  ├─ aws:iam:Role                         cluster-eksRole-role                       created
 +      │  ├─ aws:iam:RolePolicyAttachment         cluster-eksRole-90eb1c99                   created
 +      │  └─ aws:iam:RolePolicyAttachment         cluster-eksRole-4b490823                   created
 +      ├─ pulumi-nodejs:dynamic:Resource          cluster-cfnStackName                       created
 +      ├─ aws:ec2:SecurityGroup                   cluster-eksClusterSecurityGroup            created
 +      ├─ aws:iam:InstanceProfile                 cluster-instanceProfile                    created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksClusterInternetEgressRule       created
 +      ├─ aws:eks:Cluster                         cluster-eksCluster                         created
 +      ├─ aws:ec2:SecurityGroup                   cluster-nodeSecurityGroup                  created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksNodeInternetEgressRule          created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksExtApiServerClusterIngressRule  created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksClusterIngressRule              created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksNodeClusterIngressRule          created
 +      ├─ aws:ec2:SecurityGroupRule               cluster-eksNodeIngressRule                 created
 +      ├─ aws:ec2:LaunchConfiguration             cluster-nodeLaunchConfiguration            created
 +      ├─ pulumi-nodejs:dynamic:Resource          cluster-vpc-cni                            created
 +      ├─ pulumi:providers:kubernetes             cluster-eks-k8s                            created
 +      ├─ kubernetes:core:ConfigMap               cluster-nodeAccess                         created
 +      ├─ kubernetes:storage.k8s.io:StorageClass  cluster-gp2                                created
 +      ├─ aws:cloudformation:Stack                cluster-nodes                              created
 +      └─ pulumi:providers:kubernetes             cluster-provider                           created

Outputs:
    kubeconfig: {
        apiVersion     : "v1"
        clusters       : [
            [0]: {
                cluster: {
                    certificate-authority-data: "..."
                    server                    : "https://312E10705C16E8095B2A79E8E76EA00D.gr7.us-west-2.eks.amazonaws.com"
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
                            [2]: "cluster-eksCluster-560236b"
                        ]
                        command   : "aws-iam-authenticator"
                    }
                }
            }
        ]
    }

Resources:
    + 37 created

Duration: 12m12s
```

A fully functioning production cluster typically requires many other considerations. For those, we've put together [a set of playbooks as part of Pulumi Crosswalk for Kubernetes](/docs/guides/crosswalk/kubernetes) that walk through how to go to production with EKS specifically, in addition to other managed Kubernetes offerings.

Notice, for instance, that we didn't need to even provision any worker nodes. This is thanks to the `eks.Cluster` abstraction creating a default node pool for us, which has an auto-scaling policy that attempts to maintain the `desiredCapacity` while remaining within the bounds of `minSize` and `maxSize`. Sometimes you need more explicit control over the worker nodes, however, for reasons such as having more control over capacity, specializing the kind of compute or storage your workload needs, and so on. This ultimately devolves into managing EC2 instances by hand, which [the `eks.NodeGroup` class supports](https://www.pulumi.com/docs/guides/crosswalk/kubernetes/worker-nodes/).

However, needing to manage individual EC2 instances, scaling policies, and connecting them to the right IAM and networking services, can be tedious and difficult to get right. That's where the new AWS features come into play.

## Using EKS Managed Node Groups

The new EKS feature [Managed Node Groups](https://aws.amazon.com/blogs/containers/eks-managed-node-groups/) simplifies the task of managing explicit pools of worker nodes, at the cost of some amount of control. The `@pulumi/eks` package already had many of these conveniences built-in but this is now an official feature of the AWS platform.

Managed Node Groups will automatically scale the EC2 instances powering your cluster using an Auto Scaling Group (ASG) managed by EKS. This ASG also runs the latest Amazon EKS-optimized Amazon Linux 2 AMI. This is great on one hand &mdash; because updates will be applied automatically for you &mdash; but if you want control over this you will want to manage your own node groups. Finally, security groups, IAM roles, and connecting them together is handled for you.

To opt-in to using Managed Node Groups, the raw [`aws.eks.NodeGroup` building block](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/aws/eks/#NodeGroup) is available. However, we've added the `eks.Cluster.createManagedNodeGroup` function to make it easier, and to integrate with cluster provisioning.

For instance, this code creates a new EKS cluster, disabling the default node group &mdash; using `skipDefaultNodeGroup: true`, since we will create our own &mdash; and creates a single Managed Node Group with an IAM role, the desired scaling parameters, instance types, labels, and more:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc");

// IAM roles for the node group.
const role = new aws.iam.Role("my-cluster-ng-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "ec2.amazonaws.com",
    }),
});
let counter = 0;
for (const policyArn of [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
]) {
    new aws.iam.RolePolicyAttachment(`my-cluster-ng-role-policy-${counter++}`,
        { policyArn, role },
    );
}

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster", {
    skipDefaultNodeGroup: true,
    vpcId: vpc.vpcId,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    deployDashboard: false,
    instanceRoles: [ role ],
});

// Create a simple AWS managed node group using a cluster as input.
const managedNodeGroup = eks.createManagedNodeGroup("my-cluster-ng", {
    cluster: cluster,
    nodeGroupName: "aws-managed-ng1",
    nodeRoleArn: role.arn,
    scalingConfig: {
        desiredSize: 1,
        minSize: 1,
        maxSize: 2,
    },
    instanceTypes: "t2.medium",
    labels: { "ondemand": "true" },
    tags: { "org": "pulumi" },
}, cluster);

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

This can be provisioned with a single `pulumi up`, just like before, but instead of the automatically created default node group, our cluster will use a Managed Node Group instead.

> This looks more complex than the earlier `eks.Cluster` example for two reasons. First, that example benefitted from the EKS package's internal smarts. Second, this approach gives you more control over the worker nodes, while still leaning on EKS to handle the EC2 node management based on your declarative specifications.

For a full list of properties you can configure, please refer to the [`createManagedNodeGroup` API docs](/docs/reference/pkg/nodejs/pulumi/eks/#createNodeGroup). And for complete information about this feature, [see AWS's own product documentation](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

## Using EKS for Fargate

Letting EKS manage node groups for us is a great step forward to simplifying how we run our Kubernetes workloads. It still means, however, that we need to declare requirements and think at the level of worker nodes. That's where [AWS Fargate support for EKS](https://aws.amazon.com/blogs/aws/amazon-eks-on-aws-fargate-now-generally-available/) offers another step function in simplifying our task of managing clusters.

AWS Fargate technology is essentially "serverless compute for containers." Instead of thinking at the level of nodes, we can let Fargate handle provisioning, scaling, and scheduling of our cluster's worker nodes. This means we can just operate at the level of Kubernetes pods abstractions and let AWS do all of the other hard work for us!

The key building block that enables this support is something called a [Fargate profile](/docs/reference/pkg/nodejs/pulumi/aws/eks/#FargateProfile). Like `eks.NodeGroup`s above, one of these can be allocated explicitly:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc");

// IAM roles for the node group.
const role = new aws.iam.Role("my-cluster-ng-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "eks-fargate-pods.amazonaws.com",
    }),
});
new aws.iam.RolePolicyAttachment(`my-cluster-ng-role-policy-${counter++}`,
    { policyArn, role: "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy" },
);

// Create the EKS cluster itself, disabling the default node group.
const cluster = new eks.Cluster("my-cluster", {
    skipDefaultNodeGroup: true,
    deployDashboard: false,
    vpcId: vpc.id,
    privateSubnetIds: vpc.privateSubnetIds,
    instanceRoles: [ role ],
});

// Enable Fargate on this cluster.
const fargateProfile = new aws.eks.FargateProfile("my-cluster-fp", {
    clusterName: cluster.eksCluster.name,
    podExecutionRoleArn: role.arn,
    selectors: [{
        namespace: "example",
    }],
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

The EKS package, however, has also been enlightened to make allocating a Fargate-powered EKS cluster as simple as saying `fargate: true`. All we need to do is change our original cluster definition to the following:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("my-vpc");

// Create the EKS cluster itself with Fargate enabled.
const cluster = new eks.Cluster("my-cluster", {
    fargate: true,
    vpcId: vpc.id,
    privateSubnetIds: vpc.privateSubnetIds,
    deployDashboard: false,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

If we provision this with `pulumi up`, we've got a fully functioning Elastic Kubernetes cluster &mdash; with all of the hard work around managing and scaling the worker nodes left to AWS Fargate, letting us focus on our workload!

## In Conclusion

In this article, we've seen the full range of EKS cluster management options:

* Fargate, for easy auto-scaling of your cluster's worker compute
* Managed Node Groups, enabling more control, while still leveraging EKS to auto-scale
* EC2, for full control over your cluster's compute pools and nodes

Pulumi is excited to be able to offer support for this full range of options just a day after the features were announced at AWS re:Invent this week, including to enlightening `eks.Cluster` itself for ease-of-use.

To get started with Pulumi and try out these features, check out our [Getting Started guide](https://www.pulumi.com/docs/get-started/).
