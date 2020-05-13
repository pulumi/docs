---
title: "Welcoming Go to the Pulumi Family"
date: 2020-05-06T13:10:24-05:00
meta_desc: "Go is fully supported in Pulumi 2.0 for Infrastructure as Code."
meta_image: meta.png
authors:
    - evan-boyle
tags:
    - Go
---

Over the last 10 years, Go has quickly become the "language of the cloud" for building application servers and services that run in and on today's cloud platforms. With [Pulumi 2.0](https://www.pulumi.com/blog/pulumi-2-0/, Go can also be used to manage and provision modern infrastructure as well.  Across any cloud (AWS, Azure, GCP, Kubernetes and [more than 50 others](https://www.pulumi.com/docs/reference/pkg/)!) and across a variety of workloads (containers, serverless, kubernetes, core infrastructure and more), you can now use the rich software engineering strengths of the Go language and ecosystem to manage your cloud infrastructure.  The [Pulumi open source project](https://github.com/pulumi/pulumi) itself has been built on Go from day 1, and so we're really excited to bring full Go support for cloud infrastructure as code to the same language ecosystem that Pulumi itself has been part of.

<!--more-->

## What is Pulumi?

Pulumi is a modern infrastructure as code tool for the cloud.  It is built around four key ideas.

- Programming Languages. Pulumi offers best-in-class productivity and software engineering capabilities by allowing you to use existing rich programming languages like JavaScript, Python, .NET and of course Go.  Pulumi combines this with still getting the reliability of a desired-state infrastructure as code.  The best of both worlds! ```

- Multi-Cloud. Give operators the tools to build consistent workflows across any cloud(s). Whether public, private, or hybrid — you can use the full breadth and depth of any cloud services.

- Modern Application Architectures. Pulumi fully supports legacy workloads, but it is designed for the world of modern containers, serverless, and cloud-native architectures. Build the architecture that works for you by mixing and matching infrastructure components.

- Cloud Engineering Teams. Pulumi is for the entire team; everyone ranging from developers, infrastructure and operations engineers, and security engineers can use Pulumi.  Together, they can tackle cloud solutions together without technology or team silos.

## Giving you superpowers

Pulumi gives you the productivity superpowers of real programming languages. But what can you do with them?

### Serverless

Pulumi has first-class support for serverless workloads, allowing your application and infrastructure code to live side by side (and both be written in Go if you want!). Easily deploy [a lambda running a Go handler on AWS]([https://github.com/pulumi/examples/tree/master/aws-go-lambda):

```go
		args := &lambda.FunctionArgs{
			Handler: pulumi.String("handler"),
			Role:    role.Arn,
			Runtime: pulumi.String("go1.x"),
			Code:    pulumi.NewFileArchive("./handler/handler.zip"),
		}

		// Create the lambda using the args.
		function, err := lambda.NewFunction(
			ctx,
			"basicLambda",
			args,
			pulumi.DependsOn([]pulumi.Resource{logPolicy}),
		)
		if err != nil {
			return err
		}

		// Export the lambda ARN.
		ctx.Export("lambda", function.Arn)

```

And with Pulumi’s multi-cloud approach [you can do the equivalent on Google Cloud]([https://github.com/pulumi/examples/tree/master/gcp-go-functions):

```go
		// Set arguments for creating the function resource.
		args := &cloudfunctions.FunctionArgs{
			SourceArchiveBucket: bucket.Name,
			Runtime:             pulumi.String("go111"),
			SourceArchiveObject: bucketObject.Name,
			EntryPoint:          pulumi.String("Handler"),
			TriggerHttp:         pulumi.Bool(true),
			AvailableMemoryMb:   pulumi.Int(128),
		}

		// Create the function using the args.
		function, err := cloudfunctions.NewFunction(ctx, "basicFunction", args)
		if err != nil {
			return err
		}

		// Export the trigger URL.
		ctx.Export("function", function.HttpsTriggerUrl)
```

### Containers

Pulumi makes it easy to work with containers.  To start with, you can build and publish your docker images as part of a Pulumi deployment. [This example](https://github.com/pulumi/examples/tree/master/azure-go-aci) uses the Azure Container Registry:

```go
		// Create a registry.
		registryArgs := containerservice.RegistryArgs{
			ResourceGroupName: resourceGroup.Name,
			AdminEnabled:      pulumi.Bool(true),
			Sku:               pulumi.String("Premium"),
		}
		registry, err := containerservice.NewRegistry(ctx, "registry", &registryArgs)
		if err != nil {
			return err
		}

		// Create the docker image.
		imageArgs := docker.ImageArgs{
			ImageName: pulumi.Sprintf("%s/mynodeapp:v1.0.0", registry.LoginServer),
			Build: &docker.DockerBuildArgs{
				Context: pulumi.String("./app"),
			},
			Registry: &docker.ImageRegistryArgs{
				Server:   registry.LoginServer,
				Username: registry.AdminUsername,
				Password: registry.AdminPassword,
			},
		}
		image, err := docker.NewImage(ctx, "node-app", &imageArgs)
		if err != nil {
			return err
		}
```

You can even deploy a container into your cloud environment based on that image from within [the same Pulumi program](https://github.com/pulumi/examples/tree/master/azure-go-aci) ensuring that application and infrastructure deployments are always in sync:

```go
		portArgs := containerservice.GroupContainerPortArgs{
			Port:     pulumi.Int(80),
			Protocol: pulumi.String("TCP"),
		}
		containerArgs := containerservice.GroupContainerArgs{
			Cpu:    pulumi.Float64(0.5),
			Image:  image.ImageName,
			Memory: pulumi.Float64(1.5),
			Name:   pulumi.String("hello-world"),
			Ports:  containerservice.GroupContainerPortArray{portArgs},
		}
		groupArgs := containerservice.GroupArgs{
			ResourceGroupName:        resourceGroup.Name,
			ImageRegistryCredentials: containerservice.GroupImageRegistryCredentialArray{credentialArgs},
			OsType:                   pulumi.String("Linux"),
			Containers:               containerservice.GroupContainerArray{containerArgs},
			IpAddressType:            pulumi.String("public"),
			DnsNameLabel:             pulumi.String("acigo"),
		}
		group, err := containerservice.NewGroup(ctx, "aci", &groupArgs)
		if err != nil {
			return err
		}

		ctx.Export("endpoint", group.Fqdn)
```

### Kubernetes

Pulumi provides access not just to your cloud (AWS, Azure, GCP and more), but also to the whole Kubernetes API.  The Pulumi  [Kubernetes provider](https://github.com/pulumi/pulumi-kubernetes) is based on the OpenAPI specification, so is always up to date with the full functionality of the Kubernetes API. Using Pulumi to provision your Kuberentes resources gives you the declarative benefits of YAML without any of the drawbacks. Using a real language to orchestrate resources brings the benefits of strong typing, safety, and opens up options for encapsulation. Here’s a snippet from the [guestbook example](https://github.com/pulumi/examples/tree/master/kubernetes-go-guestbook):

```go
		// Redis leader Service
		_, err = corev1.NewService(ctx, "redis-leader", &corev1.ServiceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name:   pulumi.String("redis-master"),
				Labels: redisLeaderLabels,
			},
			Spec: &corev1.ServiceSpecArgs{
				Ports: corev1.ServicePortArray{
					corev1.ServicePortArgs{
						Port:       pulumi.Int(6379),
						TargetPort: pulumi.Int(6379),
					},
				},
				Selector: redisLeaderLabels,
			},
		})
		if err != nil {
			return err
		}
```

With the expressiveness of go, we have the power to [encapsulate services and deployments](https://github.com/pulumi/examples/blob/master/kubernetes-go-guestbook/components/serviceDeployment.go) behind higher-order components:

```go
type ServiceDeployment struct {
	pulumi.ResourceState

	FrontendIP pulumi.StringPtrOutput
	Deployment *appsv1.Deployment
	Service    *corev1.Service
}

type ServiceDeploymentArgs struct {
	AllocateIPAddress pulumi.Bool
	Image             pulumi.StringInput
	IsMinikube        pulumi.Bool
	Ports             pulumi.IntArrayInput
	Replicas          pulumi.IntPtrInput
}

func NewServiceDeployment(...){...}
```

This allows us to simplify boilerplate and design strongly-typed APIs for our Kubernetes infrastructure (in this case, combining a `Service` and a `Deployment` into a single, simple, API with nice defaults for our use case):

```go
                       _, err := NewServiceDeployment(ctx, "redis-leader", &ServiceDeploymentArgs{
			Image: pulumi.String("k8s.gcr.io/redis:e2e"),
			Ports: pulumi.IntArray{pulumi.Int(6379)},
		})
```

### Kubernetes + Infra

The power doesn’t stop with managing Kubernetes resources. You can provision cloud resources right alongside. Here we use Go to [provision an EKS cluster](https://github.com/pulumi/examples/tree/master/aws-go-eks):

```go
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
```

## Try Go + Pulumi Today

The magic doesn’t stop here. There’s a [wealth of examples](https://github.com/pulumi/examples), and we’re excited to see where the community takes it. If you’d like to try out Pulumi today, you can get started with your favorite cloud here:

- [AWS](https://www.pulumi.com/docs/get-started/aws/)
- [Azure](https://www.pulumi.com/docs/get-started/azure/)
- [Google Cloud](https://www.pulumi.com/docs/get-started/gcp/)
- [Kubernetes](https://www.pulumi.com/docs/get-started/kubernetes/)

We’d love to hear what you think. We look forward to hanging out on [Pulumi Slack](https://slack.pulumi.com/) or hearing from your thoughts in a [GitHub issue](https://github.com/pulumi/pulumi/issues/new).
