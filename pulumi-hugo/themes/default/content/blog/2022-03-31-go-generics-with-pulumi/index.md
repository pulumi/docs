---
title: "Using Go Generics with Pulumi"
date: 2022-03-31T14:00:00Z
draft: false
meta_desc: In this article, @rawkode shows you how to take advantage of Go's latest feature, Generics, in your Pulumi programs
meta_image: meta.png
authors: ["david-flanagan"]
tags: ["community"]
---

March 15th, 2022... just two weeks ago. The Go team [released Go 1.18](https://go.dev/blog/go1.18) to the world. What seems like a trivial point release actually brings a huge new feature to the Go language: Generics.

In this article, I want to show you how you can use this new feature to build a great developer experience with your abstractions for your Pulumi programs.

<!--more-->

## Using Go 1.18

The first thing you need to do is ensure you have Go 1.18 installed. You can run `go version` to check. If you see anything less than 1.18, you'll need to go upgrade first. The second thing you need to do is update the `go.mod` in your Pulumi program to specify 1.18 as the minimum version.

```go
go 1.18
```

Once you've done these two steps, you're ready to start using generics in your Pulumi programs.

## Using Generics

Let's start by asking a question. What is a good use-case for generics? In my experience, generics work really well for allowing us to provide a common interface to our consumers (developers using our APIs) that allows them to use that same interface to accomplish a collection of similar tasks that require different implementations.

For example, let's assume we want to provide a platform to our developers and allow them to install **ANY** Kubernetes resource. Our goal is to provide an `AddComponent` method that they can call to install either pre-supported components, components created by the platform team, or their own custom components. The glue and important aspect here is that all these components conform to the same interface.

### Defining The Interface

In the simplest form, we just need an `Install` function to call that returns either an error or an array of Pulumi resources.

```go
type Component interface {
    Install(ctx *pulumi.Context, name string) ([]pulumi.Resource, error)
}
```

### Creating our Components

Now we need to provide a component that satisfies this interface. So let's assume that we want to install nginx. First, we create a struct that contains fields for any points of configuration. For today's example, we'll just request the version to be installed and a name; the name being used to ensure if the component is installed more than once, it can be uniquely identified.

```go
type Nginx struct {
	Version string
}

func (c *Nginx) Install(ctx *pulumi.Context, name string) ([]pulumi.Resource, error) {
    return []
}
```

From there, we can begin to flesh out the `Install` implementation for nginx.

```go
func (c *Nginx) Install(ctx *pulumi.Context) ([]pulumi.Resource, error) {
	deployment, err := appsv1.NewDeployment(ctx, name, &appsv1.DeploymentArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Labels: pulumi.StringMap{
				"app": pulumi.String(name),
			},
		},
		Spec: &appsv1.DeploymentSpecArgs{
			Replicas: pulumi.Int(3),
			Selector: &metav1.LabelSelectorArgs{
				MatchLabels: pulumi.StringMap{
					"app": pulumi.String(name),
				},
			},
			Template: &corev1.PodTemplateSpecArgs{
				Metadata: &metav1.ObjectMetaArgs{
					Labels: pulumi.StringMap{
						"app": pulumi.String(name),
					},
				},
				Spec: &corev1.PodSpecArgs{
					Containers: corev1.ContainerArray{
						&corev1.ContainerArgs{
							Name:  pulumi.String("nginx"),
							Image: pulumi.String(fmt.Sprintf("nginx:%s", c.Version)),
							Ports: corev1.ContainerPortArray{
								&corev1.ContainerPortArgs{
									ContainerPort: pulumi.Int(80),
								},
							},
						},
					},
				},
			},
		},
	})
	if err != nil {
		return nil, err
	}

	return []pulumi.Resource{
		deployment,
	}, nil
}
```

This is rather contrived, but hopefully you can see the power of using generics as an interface for platform engineering. Our `AddComponent` implementation for nginx could return a deployment, a service, an ingress with horizontal pod auto-scalers, or any other resource that you want.

## Using the Components

Finally, we create our generic function, `AddComponent`, and start having some fun.

```go
func AddComponent[C Component](ctx *pulumi.Context, name string, component C) ([]pulumi.Resource, error) {
	return component.Install(ctx, name)
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		AddComponent(ctx, "my-nginx", &Nginx{Version: "1.14.2"})

		return nil
	})
}
```

Now you and your organization can provide a repository of these components for your developers to consume with their platforms.

The possibilities are endless.

Have fun and see you soon! 👋
