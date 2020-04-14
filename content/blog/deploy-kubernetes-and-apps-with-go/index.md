---
title: "Deploy Kubernetes and Applications with Go"
date: 2020-04-14
meta_desc: "Build Kubernetes deployments with Go using Pulumi's reusable components."
meta_image: gopher.png
authors:
    - levi-blackstone
tags:
    - Kubernetes
    - Go
    - containers
---

We're excited to announce that Go as a first-class language in Pulumi, and you can now build your infrastructure with Go on AWS, Azure, GCP, and many other clouds. Users often ask — "can I use Pulumi to manage Kubernetes infrastructure in Go today?" With the upcoming release of Pulumi 2.0., the answer is "yes!"

<!--more-->

Building your Kubernetes infrastructure with Infrastructure as Code offers several benefits:

- Strongly-typed inputs and outputs for resources and invokes
- First-class language support in editors/IDEs like vim, VS Code, GoLand, and atom
- Reusable components and classes: Abstract standard functionality into classes and libraries for code reuse, and clean infrastructure design, instead of copy/pasting pages of YAML.
- Embed Pulumi programs within other Go-based tools

These benefits provide a productive experience for Go developers using Kubernetes.

## Tour of Kubernetes with Go

Let's start with a basic example, e.g.,  deploying an Nginx pod into a Kubernetes cluster.

```go
pod, err := corev1.NewPod(ctx, "pod", &corev1.PodArgs{
	Spec: corev1.PodSpecArgs{
		Containers: corev1.ContainerArray{
			corev1.ContainerArgs{
				Name:  pulumi.String("nginx"),
				Image: pulumi.String("nginx"),
			}
		},
	},
})
if err != nil {
		return err
}
```

We can deploy this with `pulumi up`.

```bash
$ pulumi up
Previewing update (nginx):
     Type                    Name                 Plan
 +   pulumi:pulumi:Stack     kubernetes-go-nginx  create
 +   └─ kubernetes:core:Pod  pod                  create

Resources:
    + 2 to create

Do you want to perform this update? yes
Updating (nginx):
     Type                    Name                 Status
 +   pulumi:pulumi:Stack     kubernetes-go-nginx  created
 +   └─ kubernetes:core:Pod  pod                  created

Resources:
    + 2 created

Duration: 16s
```

Although programming languages are imperative, Pulumi describes the desired state of the infrastructure. If we change our program, Pulumi will compute the minimum delta and apply it to our Kubernetes cluster, which will transition to the new desired state. For example, we can modify our Kubernetes resources in place inside the cluster by adding a label to our Pod:

```patch
pod, err := corev1.NewPod(ctx, "pod", &corev1.PodArgs{
+	Metadata: &metav1.ObjectMetaArgs{
+		Labels: pulumi.StringMap{"app": pulumi.String("nginx")},
+	},
	Spec: corev1.PodSpecArgs{
		Containers: corev1.ContainerArray{
			corev1.ContainerArgs{
				Name:  pulumi.String("nginx"),
				Image: pulumi.String("nginx"),
			}},
	},
})
if err != nil {
	return err
}
```

The Pulumi preview shows that the pod is updated in place with the new label.

```bash
$ pulumi up
Previewing update (nginx):
     Type                    Name                 Plan       Info
     pulumi:pulumi:Stack     kubernetes-go-nginx
 ~   └─ kubernetes:core:Pod  pod                  update     [diff: ~metadata]

Resources:
    ~ 1 to update
    1 unchanged

Do you want to perform this update? details
  pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:nginx::kubernetes-go::pulumi:pulumi:Stack::kubernetes-go-nginx]
    ~ kubernetes:core/v1:Pod: (update)
        [id=default/pod-yxmgq7q2]
        [urn=urn:pulumi:nginx::kubernetes-go::kubernetes:core/v1:Pod::pod]
      ~ metadata: {
          ~ labels: {
              + app: "nginx"
            }
        }

Do you want to perform this update? yes
Updating (nginx):
     Type                    Name                 Status      Info
     pulumi:pulumi:Stack     kubernetes-go-nginx
 ~   └─ kubernetes:core:Pod  pod                  updated     [diff: ~metadata]

Resources:
    ~ 1 updated
    1 unchanged

Duration: 13s
```

The real benefits of Go come when we extract common code into a reusable component. We can create a new `ServiceDeployment` component that combines both a Kubernetes Service and Deployment with opinionated defaults. Our `ServiceDeployment` component can describe entire Kubernetes applications (100s of lines of YAML), in a short snippet of Go:

```go
// Initialize config
conf := config.New(ctx, "")

// Minikube does not implement services of type `LoadBalancer` so
// require the user to specify if we're running on minikube. If so, 
// create only services of type ClusterIP.
isMinikube := conf.GetBool("isMinikube")

// Redis leader Deployment + Service
_, err := NewServiceDeployment(ctx, "redis-master", &ServiceDeploymentArgs{
	Image: pulumi.String("k8s.gcr.io/redis:e2e"),
	Ports: pulumi.IntArray{pulumi.Int(6379)},
})
if err != nil {
	return err
}

// Redis follower Deployment + Service
_, err = NewServiceDeployment(ctx, "redis-slave", &ServiceDeploymentArgs{
	Image: pulumi.String("gcr.io/google_samples/gb-redisslave:v3"),
	Ports: pulumi.IntArray{pulumi.Int(6379)},
})
if err != nil {
	return err
}

// Frontend Deployment + Service
frontend, err := NewServiceDeployment(ctx, "frontend", &ServiceDeploymentArgs{
	AllocateIPAddress: true,
	Image:             pulumi.String("gcr.io/google-samples/gb-frontend:v4"),
	IsMinikube:        pulumi.Bool(isMinikube),
	Ports:             pulumi.IntArray{pulumi.Int(80)},
	Replicas:          pulumi.Int(3),
})
if err != nil {
	return err
}

if isMinikube {
	ctx.Export("frontendIP", frontend.Service.Spec.ApplyT(
		func(spec *corev1.ServiceSpec) *string { return spec.ClusterIP }))
} else {
	ctx.Export("frontendIP", frontend.FrontendIP)
}
```

The complete implementation of the ServiceDeployment component is detailed in the [Guestbook example](https://github.com/pulumi/examples/tree/master/kubernetes-go-guestbook/components) in the Pulumi Examples repo on GitHub.

![Kubernetes Guestbook](guestbook.png)

## Building Docker Images for Kubernetes with Go

In the previous examples, we specified the Docker image to deploy as part of our Kubernetes Deployments by referring to an image in a registry. If we wanted to push our custom Docker image that uses our application's source code, and deploy that in our Kubernetes Pod or Deployment, we can do it with the [pulumi-docker](https://github.com/pulumi/pulumi-docker/tree/master/sdk/go/docker) package. For example, we can deploy our custom Nginx Docker image with the following:

```go
image, err := docker.NewImage(ctx, "node-app", &docker.ImageArgs{
	ImageName: pulumi.String("my-username/my-nginx"),
	Build: &docker.DockerBuildArgs{
		Context: pulumi.String("./app"),
	},
})
if err != nil {
	return err
}

pod, err := corev1.NewPod(ctx, "pod", &corev1.PodArgs{
	Metadata: &metav1.ObjectMetaArgs{
		Labels: pulumi.StringMap{"app": pulumi.String("nginx")},
	},
	Spec: corev1.PodSpecArgs{
		Containers: corev1.ContainerArray{
			corev1.ContainerArgs{
				Name:  pulumi.String("nginx"),
				Image: image.ImageName,
			}},
	},
})
if err != nil {
	return err
}
```

We can use our Dockerfile from the app folder in our Pulumi project, instead of using the default Nginx image from DockerHub. For example, adding the following in our Dockerfile deploys customized files in the app/content folder to our Nginx server:

```docker
FROM nginx
COPY content /usr/share/nginx/html
```

When we deploy this with Pulumi, the Dockerfile is built locally, pushed to a registry, then it is available by image name in the registry referenced from the Pod in Kubernetes. Our changes happen automatically, seamlessly deploying and versioning both the application code and infrastructure together with a simple `pulumi up`.

We can also push to another Docker container registry (like ACR, GCR, ECR, or others) by using additional parameters on the `pulumi.docker.ImageArgs` class.

## Cloud + Kubernetes with Go

Pulumi works with both Kubernetes and cloud providers (AWS, Azure, GCP, and more). In the same Pulumi program, you can build a Kubernetes cluster and then deploy applications and services into the cluster. Using Pulumi's programming model, we have access to all these various cloud technologies.

For example, we can deploy a managed GKE cluster, and then deploy a Pod into it:

```go
masterVersion := "1.14.10-gke.27"
cluster, err := container.NewCluster(ctx, "demo-cluster", &container.ClusterArgs{
	InitialNodeCount: pulumi.Int(2),
	MinMasterVersion: pulumi.String(masterVersion),
	NodeVersion:      pulumi.String(masterVersion),
	NodeConfig: &container.ClusterNodeConfigArgs{
		MachineType: pulumi.String("n1-standard-1"),
		OauthScopes: pulumi.StringArray{
			pulumi.String("https://www.googleapis.com/auth/compute"),
			pulumi.String("https://www.googleapis.com/auth/devstorage.read_only"),
			pulumi.String("https://www.googleapis.com/auth/logging.write"),
			pulumi.String("https://www.googleapis.com/auth/monitoring"),
		},
	},
})
if err != nil {
	return err
}

ctx.Export("kubeconfig", generateKubeconfig(
    cluster.Endpoint, cluster.Name, cluster.MasterAuth))

k8sProvider, err := providers.NewProvider(
    ctx, "k8sprovider", &providers.ProviderArgs{
	Kubeconfig: generateKubeconfig(
	    cluster.Endpoint, cluster.Name, cluster.MasterAuth),
}, pulumi.DependsOn([]pulumi.Resource{cluster}))
if err != nil {
	return err
}

namespace, err := corev1.NewNamespace(ctx, "app-ns", &corev1.NamespaceArgs{
	Metadata: &metav1.ObjectMetaArgs{
		Name: pulumi.String("demo-ns"),
	},
}, pulumi.Provider(k8sProvider))
if err != nil {
	return err
}

appLabels := pulumi.StringMap{
	"app": pulumi.String("demo-app"),
}
_, err = appsv1.NewDeployment(ctx, "app-dep", &appsv1.DeploymentArgs{
	Metadata: &metav1.ObjectMetaArgs{
		Namespace: namespace.Metadata.Elem().Name(),
	},
	Spec: appsv1.DeploymentSpecArgs{
		Selector: &metav1.LabelSelectorArgs{
			MatchLabels: appLabels,
		},
		Replicas: pulumi.Int(3),
		Template: &corev1.PodTemplateSpecArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: appLabels,
			},
			Spec: &corev1.PodSpecArgs{
				Containers: corev1.ContainerArray{
					corev1.ContainerArgs{
						Name:  pulumi.String("demo-app"),
						Image: pulumi.String("jocatalin/kubernetes-bootcamp:v2"),
					}},
			},
		},
	},
}, pulumi.Provider(k8sProvider))
if err != nil {
	return err
}
```

This example first deploys a GKE Kubernetes Cluster into GCP, then deploys Kubernetes resources into that GKE Cluster. This example combines infrastructure and application deployment in a few dozen lines of declarative and strongly typed Go code.

Check out the full [GKE in Go example](https://github.com/pulumi/examples/tree/master/gcp-go-gke) on Github.

## Conclusion

Kubernetes support is one of several significant new additions to the Pulumi Go support, and many more improvements are in progress over the coming weeks. Get started with Kubernetes and Go today, and let us know what you think!
