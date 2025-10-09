---
title: "How to Create an AWS EKS Kubernetes Cluster with Pulumi"
meta_desc: "Deploy a managed Kubernetes cluster on AWS using EKS (Elastic Kubernetes Service) with Pulumi for container orchestration in TypeScript, Python, Go, C#, or Java."
canonical_url: "https://www.pulumi.com/recipes/aws/eks-cluster-basic"
date: 2025-10-08
category: "Compute"
tags: ["aws", "eks", "kubernetes", "containers", "orchestration"]
faq:
  - question: Do I need to create a node group to run applications on EKS?
    answer: Yes, this example creates only the EKS control plane. To run actual workloads, you need to add node groups (managed or self-managed EC2 instances) or use AWS Fargate for serverless container execution. The control plane alone cannot run your pods.
  - question: How much does an EKS cluster cost?
    answer: AWS charges $0.10 per hour (approximately $73 per month) for each EKS cluster control plane, regardless of the number of nodes or workloads. You also pay for the EC2 instances (node groups) or Fargate pods that run your applications separately.
  - question: Which Kubernetes version should I use?
    answer: Specify an explicit version like 1.31 to avoid unexpected upgrades. AWS supports the latest three minor Kubernetes versions. When a new version is released, the oldest supported version is deprecated after about 14 months. Plan for regular upgrades.
  - question: What VPC requirements does EKS have?
    answer: Your VPC must have at least two subnets in different availability zones for high availability. These subnets must be properly tagged for EKS to discover them for load balancers and other resources. Private subnets are recommended for nodes.
  - question: How do I access my EKS cluster after creation?
    answer: Use kubectl with the AWS CLI to authenticate. Run 'aws eks update-kubeconfig --name your-cluster-name' to add the cluster to your kubeconfig. You may also need to configure the aws-auth ConfigMap to grant access to additional IAM users or roles.
---

## How do I create an AWS EKS Kubernetes cluster?

**To deploy a managed Kubernetes cluster on AWS**, create an EKS cluster with the necessary IAM roles and VPC configuration. EKS manages the Kubernetes control plane for you, providing high availability and automatic upgrades. The following example shows how to create an EKS cluster in TypeScript, Python, Go, C#, and Java.

{{< chooser language "typescript,python,go,csharp,java" >}}
{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const cluster = new aws.iam.Role("cluster", {
    name: "eks-cluster-example",
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: [
                "sts:AssumeRole",
                "sts:TagSession",
            ],
            Effect: "Allow",
            Principal: {
                Service: "eks.amazonaws.com",
            },
        }],
    }),
});

const clusterAmazonEKSClusterPolicy = new aws.iam.RolePolicyAttachment("cluster_AmazonEKSClusterPolicy", {
    policyArn: "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
    role: cluster.name,
});

const example = new aws.eks.Cluster("example", {
    name: "example",
    accessConfig: {
        authenticationMode: "API",
    },
    roleArn: cluster.arn,
    version: "1.31",
    vpcConfig: {
        subnetIds: [
            az1.id,
            az2.id,
            az3.id,
        ],
    },
}, {
    dependsOn: [clusterAmazonEKSClusterPolicy],
});
```
{{% /choosable %}}

{{% choosable language python %}}
```python
import pulumi
import pulumi_aws as aws
import json

cluster = aws.iam.Role("cluster",
    name="eks-cluster-example",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
            ],
            "Effect": "Allow",
            "Principal": {
                "Service": "eks.amazonaws.com",
            },
        }],
    }))

cluster_amazon_eks_cluster_policy = aws.iam.RolePolicyAttachment("cluster_AmazonEKSClusterPolicy",
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
    role=cluster.name)

example = aws.eks.Cluster("example",
    name="example",
    access_config=aws.eks.ClusterAccessConfigArgs(
        authentication_mode="API",
    ),
    role_arn=cluster.arn,
    version="1.31",
    vpc_config=aws.eks.ClusterVpcConfigArgs(
        subnet_ids=[
            az1.id,
            az2.id,
            az3.id,
        ],
    ),
    opts=pulumi.ResourceOptions(depends_on=[cluster_amazon_eks_cluster_policy]))
```
{{% /choosable %}}

{{% choosable language go %}}
```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/eks"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		assumeRolePolicyJSON, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action": []string{
						"sts:AssumeRole",
						"sts:TagSession",
					},
					"Effect": "Allow",
					"Principal": map[string]interface{}{
						"Service": "eks.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}

		cluster, err := iam.NewRole(ctx, "cluster", &iam.RoleArgs{
			Name:             pulumi.String("eks-cluster-example"),
			AssumeRolePolicy: pulumi.String(string(assumeRolePolicyJSON)),
		})
		if err != nil {
			return err
		}

		clusterAmazonEKSClusterPolicy, err := iam.NewRolePolicyAttachment(ctx, "cluster_AmazonEKSClusterPolicy", &iam.RolePolicyAttachmentArgs{
			PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"),
			Role:      cluster.Name,
		})
		if err != nil {
			return err
		}

		_, err = eks.NewCluster(ctx, "example", &eks.ClusterArgs{
			Name: pulumi.String("example"),
			AccessConfig: &eks.ClusterAccessConfigArgs{
				AuthenticationMode: pulumi.String("API"),
			},
			RoleArn: cluster.Arn,
			Version: pulumi.String("1.31"),
			VpcConfig: &eks.ClusterVpcConfigArgs{
				SubnetIds: pulumi.StringArray{
					az1.Id,
					az2.Id,
					az3.Id,
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{clusterAmazonEKSClusterPolicy}))
		if err != nil {
			return err
		}
		return nil
	})
}
```
{{% /choosable %}}

{{% choosable language csharp %}}
```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var cluster = new Aws.Iam.Role("cluster", new()
    {
        Name = "eks-cluster-example",
        AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object>
        {
            ["Version"] = "2012-10-17",
            ["Statement"] = new[]
            {
                new Dictionary<string, object>
                {
                    ["Action"] = new[]
                    {
                        "sts:AssumeRole",
                        "sts:TagSession",
                    },
                    ["Effect"] = "Allow",
                    ["Principal"] = new Dictionary<string, object>
                    {
                        ["Service"] = "eks.amazonaws.com",
                    },
                },
            },
        }),
    });

    var clusterAmazonEKSClusterPolicy = new Aws.Iam.RolePolicyAttachment("cluster_AmazonEKSClusterPolicy", new()
    {
        PolicyArn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
        Role = cluster.Name,
    });

    var example = new Aws.Eks.Cluster("example", new()
    {
        Name = "example",
        AccessConfig = new Aws.Eks.Inputs.ClusterAccessConfigArgs
        {
            AuthenticationMode = "API",
        },
        RoleArn = cluster.Arn,
        Version = "1.31",
        VpcConfig = new Aws.Eks.Inputs.ClusterVpcConfigArgs
        {
            SubnetIds = new[]
            {
                az1.Id,
                az2.Id,
                az3.Id,
            },
        },
    }, new CustomResourceOptions
    {
        DependsOn = new[]
        {
            clusterAmazonEKSClusterPolicy,
        },
    });
});
```
{{% /choosable %}}

{{% choosable language java %}}
```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.iam.RolePolicyAttachment;
import com.pulumi.aws.iam.RolePolicyAttachmentArgs;
import com.pulumi.aws.eks.Cluster;
import com.pulumi.aws.eks.ClusterArgs;
import com.pulumi.aws.eks.inputs.ClusterAccessConfigArgs;
import com.pulumi.aws.eks.inputs.ClusterVpcConfigArgs;
import com.pulumi.resources.CustomResourceOptions;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var cluster = new Role("cluster", RoleArgs.builder()
            .name("eks-cluster-example")
            .assumeRolePolicy(serializeJson(
                jsonObject(
                    jsonProperty("Version", "2012-10-17"),
                    jsonProperty("Statement", jsonArray(jsonObject(
                        jsonProperty("Action", jsonArray(
                            "sts:AssumeRole",
                            "sts:TagSession"
                        )),
                        jsonProperty("Effect", "Allow"),
                        jsonProperty("Principal", jsonObject(
                            jsonProperty("Service", "eks.amazonaws.com")
                        ))
                    )))
                )))
            .build());

        var clusterAmazonEKSClusterPolicy = new RolePolicyAttachment("cluster_AmazonEKSClusterPolicy", RolePolicyAttachmentArgs.builder()
            .policyArn("arn:aws:iam::aws:policy/AmazonEKSClusterPolicy")
            .role(cluster.name())
            .build());

        var example = new Cluster("example", ClusterArgs.builder()
            .name("example")
            .accessConfig(ClusterAccessConfigArgs.builder()
                .authenticationMode("API")
                .build())
            .roleArn(cluster.arn())
            .version("1.31")
            .vpcConfig(ClusterVpcConfigArgs.builder()
                .subnetIds(
                    az1.id(),
                    az2.id(),
                    az3.id())
                .build())
            .build(), CustomResourceOptions.builder()
                .dependsOn(clusterAmazonEKSClusterPolicy)
                .build());
    }
}
```
{{% /choosable %}}
{{< /chooser >}}

## Key configuration details

**IAM role for EKS**: The cluster requires an IAM role that allows the EKS service to assume it. This role must have the `AmazonEKSClusterPolicy` attached, which grants permissions to manage AWS resources on behalf of Kubernetes.

**Cluster version**: Specify an explicit Kubernetes version (e.g., `1.31`) to control when upgrades happen. AWS supports the latest three minor versions and deprecates older versions approximately 14 months after a new version is released.

**VPC configuration**: The `vpcConfig` block specifies which subnets the cluster uses. You need at least two subnets in different availability zones for high availability. These subnets must be tagged appropriately for EKS.

**Authentication mode**: Setting `authenticationMode: "API"` enables the EKS API for cluster authentication. You can also use `CONFIG_MAP` for legacy aws-auth ConfigMap authentication or `API_AND_CONFIG_MAP` for both.

**Node groups not included**: This example creates only the control plane. You must separately create managed node groups, self-managed node groups, or configure Fargate profiles to run actual workloads.

**Cluster dependencies**: The `dependsOn` option ensures the IAM policy attachment completes before creating the cluster. This prevents authorization failures during cluster creation.

## Frequently asked questions

**Do I need to create a node group to run applications on EKS?**
Yes, this example creates only the EKS control plane. To run actual workloads, you need to add node groups (managed or self-managed EC2 instances) or use AWS Fargate for serverless container execution. The control plane alone cannot run your pods.

**How much does an EKS cluster cost?**
AWS charges $0.10 per hour (approximately $73 per month) for each EKS cluster control plane, regardless of the number of nodes or workloads. You also pay for the EC2 instances (node groups) or Fargate pods that run your applications separately.

**Which Kubernetes version should I use?**
Specify an explicit version like 1.31 to avoid unexpected upgrades. AWS supports the latest three minor Kubernetes versions. When a new version is released, the oldest supported version is deprecated after about 14 months. Plan for regular upgrades.

**What VPC requirements does EKS have?**
Your VPC must have at least two subnets in different availability zones for high availability. These subnets must be properly tagged for EKS to discover them for load balancers and other resources. Private subnets are recommended for nodes.

**How do I access my EKS cluster after creation?**
Use kubectl with the AWS CLI to authenticate. Run 'aws eks update-kubeconfig --name your-cluster-name' to add the cluster to your kubeconfig. You may also need to configure the aws-auth ConfigMap to grant access to additional IAM users or roles.

