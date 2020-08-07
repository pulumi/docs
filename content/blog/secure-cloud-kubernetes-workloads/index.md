---
title: "Securely access cloud resources in Kubernetes workloads"
date: 2020-08-06T20:56:15-07:00
draft: true
meta_desc: An overview of running accessing cloud resources securely for Kubernetes workloads
meta_image: meta.png
authors:
    - lee-briggs
tags:
    - kubernetes
    - security
---

As you build your cloud-native Kubernetes applications, you might eventually find you need to access cloud resources which reside outside your Kubernetes cluster. Perhaps you need to store static files in an object store (Amazon S3, Google Cloud Storage or Azure Blog Storage) or use a queuing system to pass messages to other services (Amazon SQS, Azure Service Bus or Google Pub/Sub).

Once you start to access these services from within your application, you'll need to find some way to authenticate to the cloud providers API, and that involves somehow managing credentials. It can be tempting at this point to create a user in your cloud provider and create credentials like AWS Access Keys or a Google Cloud Service Account Key and store those inside your Kubernetes workload. A common approach is to store these credentials as a Kubernetes secret and then consume that secret as an environment variable in your running pods:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
data:
  username: bXktYXBw
  password: Mzk1MjgkdmRnN0pi
---
apiVersion: v1
kind: Pod
metadata:
  name: secret-test-pod
spec:
  containers:
    - name: test-container
      image: nginx
      volumeMounts:
        # name must match the volume name below
        - name: secret-volume
          mountPath: /etc/secret-volume
  # The secret data is exposed to Containers in the Pod through a Volume.
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
```

This method works and will allow access to cloud resources from your app. You can approach this with a security-conscious mindset and make sure the permissions that the keys are associated with are narrowly scoped (following the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)). However, unfortunately, if you have an information security team looking over your shoulder, they will still see this practice and be extremely concerned. In this post, we'll talk about why this might be a problem, and show you how to deploy Kubernetes applications following security best practices and still allow them to access cloud resources.

<!--more-->

## The Static Credential Problem

Static credentials (such as AWS Access Keys) are easy to use for consumers, but they create a myriad of problems from a security perspective. To understand these problems, it's essential to take a quick look at how potential attackers might operate.

It's rare for a malicious user to find the keys to the kingdom immediately when they decide to target you. Commonly, an attacker will find a small bug or hole in your application or infrastructure and then attempt to use that bug to escalate their privileges to move horizontally or vertically through your infrastructure. Navigating through the gaps in your infrastructure takes time. The longer an attacker has access to your systems, the more likely they are to be able to escalate their access to the point where they can access sensitive data.

A well-secured environment attempts to limit the capability for an attacker to [pivot](https://en.wikipedia.org/wiki/Exploit_(computer_security)#Pivoting) by adding more layers for them to get through and restricting the amount of time they have to get through those layers.

If you decide to use static credentials, the most important thing to consider is that they can be easily stolen and copied by an attacker. They live indefinitely and will continue to work until someone manually revokes them.
Alongside this, by hard coding these credentials into a Kubernetes secret, it presents multiple layers from which an attacker could steal them:

The Kubernetes API (by retrieving the secret)
Inside the running pod (by grabbing the environment variables, where they're in plaintext)
Hopefully, I've made a compelling case for why you should reconsider using static credentials for your application, now let's talk about the solution.

## Introducing roles

Some variant of "machine identity" is offered by all the major cloud providers, and you've probably used them when deploying workloads to virtual machines. At a basic level, the idea is that you'd assign a "role" to the virtual machine, and the cloud provider automatically provides authenticated access to its API. This way, you never have to store credentials locally, where they could potentially get compromised.

It's reasonably straightforward using roles on a virtual machine, but if you're using Kubernetes an issue arises. Kubernetes worker nodes can be assigned a role, but that role gets shared across all pods running on that node. Suppose your worker nodes are running pods with multiple applications that have different requirements. In that case, you have the unfortunate option of assigning widely scoped roles to your nodes, which could present an opportunity for an attacker to pivot quickly.

To mitigate this, many cloud providers offer a solution to push roles all the way down to the Kubernetes pod. To see how this works, let's attempt to deploy the popular ChartMuseum application to Kubernetes clusters in AWS EKS, Azure AKS and Google Cloud GKE. We'll provision an S3 bucket that stores the charts in each of the cloud providers and use the native mechanism for each cloud provider to allow access to that bucket.

### AWS EKS

EKS is the youngest of the managed Kubernetes offerings and was the last of the three to provider the native capability to push IAM roles down to pods. Previously, operators could install third-party solutions like KIAM and Kube2IAM in their clusters, and both of these solutions are widely used and well tested.

EKS now offers a native solution, which involves creating a cluster with an OpenID connect issuer attached to it. You can read more about this [here](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html)

Creating a cluster with IAM roles for service accounts enabled is straightforward with the pulumi-eks package (currently only available in TypeScript). Set the OIDC flag on the cluster:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("vpc", { numberOfAvailabilityZones: 2 });

// Create the EKS cluster itself and a deployment of the Kubernetes dashboard.
const cluster = new eks.Cluster("cluster", {
    vpcId: vpc.id,
    subnetIds: vpc.publicSubnetIds,
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 2,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

You'll notice here that I'm using `export` to ensure we can reference these URLs in another stack.

#### Create an S3 bucket

We need an S3 bucket to store the Helm chart tarballs in, and we can easily create a bucket using Pulumi. Here's the code

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a bucket to store helm charts
const chartMuseumBucket = new aws.s3.Bucket("chartMuseumBucket", {});
export const bucketName = chartMuseumBucket.bucket;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import json
import pulumi_aws as aws

chart_museum_bucket = aws.s3.Bucket("chartMuseumBucket")
pulumi.export("bucketName", chart_museum_bucket.bucket)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		chartMuseumBucket, err := s3.NewBucket(ctx, "chartMuseumBucket", nil)
		if err != nil {
			return err
		}
		ctx.Export("bucketName", chartMuseumBucket.Bucket)
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

class MyStack : Stack
{
    public MyStack()
    {
        // Create a bucket to store helm charts
        var chartMuseumBucket = new Aws.S3.Bucket("chartMuseumBucket", new Aws.S3.BucketArgs
        {
        });
    }

    [Output("bucketName")]
    public Output<string> BucketName { get; set; }
}
```

{{% /choosable %}}
{{< /chooser >}}

#### Create IAM Role

Once we've created a cluster, we need an IAM role that has access to the bucket we created:
{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a bucket to store helm charts
const chartMuseumBucket = new aws.s3.Bucket("chartMuseumBucket", {});
// Create an IAM role that can read the bucket
const chartMuseumRole = new aws.iam.Role("chartMuseumRole", {assumeRolePolicy: JSON.stringify({
    Version: "2012-10-17",
    Statement: [{
        Action: ["s3:*"],
        Effect: "Allow",
        Resource: ["chartMuseumBucket.arn"],
    }],
})});
export const bucketName = chartMuseumBucket.bucket;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import json
import pulumi_aws as aws

# Create a bucket to store helm charts
chart_museum_bucket = aws.s3.Bucket("chartMuseumBucket")
# Create an IAM role that can read the bucket
chart_museum_role = aws.iam.Role("chartMuseumRole", assume_role_policy=json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": ["s3:*"],
        "Effect": "Allow",
        "Resource": ["chartMuseumBucket.arn"],
    }],
}))
pulumi.export("bucketName", chart_museum_bucket.bucket)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		chartMuseumBucket, err := s3.NewBucket(ctx, "chartMuseumBucket", nil)
		if err != nil {
			return err
		}
		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": []string{
						"s3:*",
					},
					"Effect": "Allow",
					"Resource": []string{
						"chartMuseumBucket.arn",
					},
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		_, err = iam.NewRole(ctx, "chartMuseumRole", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(json0),
		})
		if err != nil {
			return err
		}
		ctx.Export("bucketName", chartMuseumBucket.Bucket)
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

class MyStack : Stack
{
    public MyStack()
    {
        // Create a bucket to store helm charts
        var chartMuseumBucket = new Aws.S3.Bucket("chartMuseumBucket", new Aws.S3.BucketArgs
        {
        });
        // Create an IAM role that can read the bucket
        var chartMuseumRole = new Aws.Iam.Role("chartMuseumRole", new Aws.Iam.RoleArgs
        {
            AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
            {
                { "Version", "2012-10-17" },
                { "Statement", new[]
                    {
                        new Dictionary<string, object?>
                        {
                            { "Action", new[]
                                {
                                    "s3:*",
                                }
                             },
                            { "Effect", "Allow" },
                            { "Resource", new[]
                                {
                                    "chartMuseumBucket.arn",
                                }
                             },
                        },
                    }
                 },
            }),
        });
        this.BucketName = chartMuseumBucket.BucketName;
    }

    [Output("bucketName")]
    public Output<string> BucketName { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

I'm providing full `s3:*` access to this bucket so that ChartMuseum can read, write and list the contents. Any workload that assumes this role can now manage the bucket as needed.

#### Assign IAM role to Chart Musem

Now we need to deploy Chart Museum to our cluster.  To use the role that we created previously, you need to specify an annotation on the Kubernetes service account which references the AWS IAM role we want to assume. Here's an example of deploying chart museum and specifying the correct annotation on the Service account:

```
Chart museum helm chart
```

You'll notice here we're also specifying the path to our S3 bucket, and letting chart museum know we're using Amazon as a storage backend.

#### Verify

We should now be able to verify that Chart Museum has connected to the backend. <update this>

### Azure AKS

Azure AKS uses an operator to assign roles to pods. The AAD Pod Identity project allows operators to create a CustomResource which can be assigned to pods and will reference an Azure Active Directory service principal.

### Google Cloud GKE

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}
{{% /choosable %}}

{{% choosable language python %}}
{{% /choosable %}}

{{% choosable language go %}}
{{% /choosable %}}

{{% choosable language csharp %}}
{{% /choosable %}}

{{< /chooser >}}
