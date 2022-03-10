---
date: "2020-06-04"
title: "What's new in Pulumi 2.0 for Kubernetes"
authors: ["mike-metral"]
tags: ["Kubernetes"]
meta_desc: "What's new in Pulumi 2.0 for Kubernetes covers the major highlights of features and improvement to Pulumi's Kubernetes support."
meta_image: pulumi_k8s.png
---

We recently announced the 2.0 release of Pulumi which includes parity for
[Node.js (JavaScript, TypeScript)]({{< relref "/docs/intro/languages/javascript" >}}), [Python]({{< relref "/docs/intro/languages/python" >}}), [.NET (C#, F#, etc)]({{< relref "/docs/intro/languages/dotnet" >}}) and [Go]({{< relref "/docs/intro/languages/go" >}}),
and improvements to Kubernetes and dozens of other [supported cloud resource providers]({{< relref "/registry" >}}) and [packages]({{< relref "/docs/reference/pkg#package-documentation" >}}).

[Kubernetes support]({{< relref "/registry/packages/kubernetes" >}}) in Pulumi spans orchestration of clusters and application
workloads. Clusters can be managed by cloud providers or self-managed.
Workloads use the same [Kubernetes API](https://kubernetes.io/docs/reference/) to create and manage API resources in the
supported Pulumi languages through packages directly generated from the [OpenAPI specification](https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec).

<!--more-->

## Overview

In our march towards v2.0, we've been working on improvements and added new
features for Kubernetes thanks to the valuable feedback we've received from our
community of users and customers.

Let's review some of the major highlights.

## Managing Workloads

Users provision and manage Kubernetes workloads in various ways: YAML
manifests, Helm charts, operators, and direct API access. Pulumi can help to
unify this resource management using a programming language of your choice.

Some of the recent highlights for the [pulumi/kubernetes](https://github.com/pulumi/pulumi-kubernetes) package include:

* Added [language support](https://www.pulumi.com/registry/packages/kubernetes/#library-packages) for Go and .NET

```go
// Create an EKS cluster in Go.
func main() {
        pulumi.Run(func(ctx *pulumi.Context) error {
            // Create EKS Cluster
            eksCluster, err := eks.NewCluster(ctx, "eks-cluster", &eks.ClusterArgs{
                RoleArn: pulumi.StringInput(eksRole.Arn),
                VpcConfig: &eks.ClusterVpcConfigArgs{
                PublicAccessCidrs: pulumi.StringArray{
                    pulumi.String("0.0.0.0/0"),
                },
                SecurityGroupIds: pulumi.StringArray{
                    clusterSg.ID().ToStringOutput(),
                },
                SubnetIds: toPulumiStringArray(subnet.Ids),
                },
            })
            if err != nil {
                return err
            }

            // Create the NodeGroup.
            _, err = eks.NewNodeGroup(ctx, "node-group-2", &eks.NodeGroupArgs{
            	ClusterName:   eksCluster.Name,
            	NodeGroupName: pulumi.String("demo-eks-nodegroup-2"),
            	NodeRoleArn:   pulumi.StringInput(nodeGroupRole.Arn),
            	SubnetIds:     toPulumiStringArray(subnet.Ids),
            	ScalingConfig: &eks.NodeGroupScalingConfigArgs{
            		DesiredSize: pulumi.Int(2),
            		MaxSize:     pulumi.Int(2),
            		MinSize:     pulumi.Int(1),
            	},
            })
            if err != nil {
                return err
            }

            ctx.Export("kubeconfig", generateKubeconfig(eksCluster.Endpoint,
            eksCluster.CertificateAuthority.Data().Elem(), eksCluster.Name))

            return nil
        })
}
```

```csharp
    // Create an EKS cluster in C#
    var cluster = new Eks.Cluster("eks-cluster", new Eks.ClusterArgs
    {
        RoleArn = eksRole.Arn,
        VpcConfig = new ClusterVpcConfigArgs
        {
            PublicAccessCidrs = {"0.0.0.0/0"},
            SecurityGroupIds = {clusterSg.Id},
            SubnetIds = subnetIds,
        },
    });

    // Create the NodeGroup.
    var nodeGroup = new Eks.NodeGroup("node-group", new Eks.NodeGroupArgs
    {
        ClusterName = cluster.Name,
        NodeGroupName = "demo-eks-nodegroup",
        NodeRoleArn = nodeGroupRole.Arn,
        SubnetIds = subnetIds,
        ScalingConfig = new NodeGroupScalingConfigArgs{DesiredSize = 2},
    });
```

* Kubernetes version support now includes the latest [v1.18 release](https://kubernetes.io/docs/setup/release/notes/), which builds on Pulumi's [support](https://github.com/pulumi/pulumi-kubernetes#kubernetes-api-version-support) for clusters >= v1.9.0
    * Warnings are displayed for Kubernetes resources using deprecated apiVersions.
    * [Updated the client-go](https://kubernetes.io/docs/setup/release/notes/#client-go) dependency in the provider to take advantage of the latest upstream fixes and changes.
* General house cleaning and fixes
    * Helm v3 CRD's are included as expected when the `include-crds` flag is used.
    * Fixed CRD resource patch updates by changing their default merge behavior.

## Managing Clusters

Kubernetes clusters come in different shapes and sizes, and with various operational
requirements to run. We’ve expanded our support for managed Kubernetes clusters
across the respective cloud provider packages.

* [pulumi/eks](https://github.com/pulumi/pulumi-eks)
    * More [examples](https://github.com/pulumi/pulumi-eks/tree/master/examples) are provided to cover various EKS-specific scenarios.
    * Support for [additional security groups](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#NodeGroup-extraNodeSecurityGroups) for node groups to attach to user-specified rules
    * Support for [envelope encrypted secrets](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#ClusterOptions-encryptionConfigKeyArn) so that Kubernetes Secrets are encrypted in etcd
    * Support for [alternative authentication](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#ClusterOptions-providerCredentialOpts) approaches on the cluster and infrastructure created, such as using AWS named profiles
    * Create [kubeconfig files](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#Cluster-getKubeconfig) that are scoped to IAM users or roles -- this is used to limit access to the cluster.
    * Use the EKS package on clients operating in [HTTP proxy](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#ClusterOptions-proxy) environments, such as corporate proxies.
    * [Default to the latest AMIs](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/eks/#ClusterNodeGroupOptions-amiId) for node groups, using the latest release from the AWS SSM parameter store.

## Wrap-Up

As our community continues to grow, we’re committed to improving our Kubernetes
experience even further. You can help to shape this experience directly by
providing feedback on [GitHub](https://github.com/pulumi/pulumi-kubernetes/). We love to hear from our users!

Learn more about how [Pulumi works with Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/), and [Get Started](https://www.pulumi.com/docs/get-started/kubernetes/) if you're
new.

You can explore more content by checking out [PulumiTV on YouTube](https://www.youtube.com/pulumitv), work through
Kubernetes [tutorials](https://www.pulumi.com/docs/tutorials/kubernetes/) to dive deeper, and join the [Community Slack](https://slack.pulumi.com/) to engage
with users and the Pulumi team.
