---
title: "Kubernetes Fundamentals Part One"
date: 2021-07-23T12:54:53-05:00
draft: false
meta_image: k8s-fundamentals.png
meta_desc: "Kubernetes is everywhere now, but it’s largely been the domain of people who work on the Ops side of things. What about devs, though?"
authors:
    - kat-cosgrove
tags:
    - kubernetes
---
Kubernetes is everywhere now, but it’s primarily been the domain of people working on the Ops side of infrastructure. What about devs, though? You benefit from knowing what Kubernetes is and how to use it, too -- otherwise, we’re still putting teams in silos. In this tutorial, we’re going to define Kubernetes at a high level, talk about the anatomy of a cluster, and learn not just why you should care but how to try it for yourself. We’ll start with local deployments using YAML before getting a little help from infrastructure as code with Pulumi to stand up everything right inside our sample application in a programming language you’re already writing!

<!--more-->

## What is Kubernetes?

Kubernetes is a container orchestration tool. If we think of it in the context of an actual container ship, then Kubernetes is the person who determines how many shipping containers of particular goods go on the ship and where they should be in relation to each other. It makes deploying containerized workloads a bit less painful to maintain.

## Anatomy of a Cluster

Let’s talk about what Kubernetes looks like. Inside a cluster, there is a master node responsible for the overall maintenance of the cluster and several worker nodes where our containers and other workloads live. There are other pieces here, but generally, that’s the high level. You end up with something that looks like a big box containing many smaller boxes, which, in turn, contain more boxes.

So, the master node takes care of the worker nodes, and the worker nodes house our containers, which may be running application code, or a database, or volume storage, or some other service. Instead of managing each of these individual components yourself, you tell Kubernetes how to manage them and let it deal with that for you.

## Deployment

There are a few ways to do this. We can use `kubectl` in the terminal by pointing it at config files written in a format called YAML, or we can use an infrastructure as code tool like Pulumi to help. For now, we’ll use YAML and let `kubectl` handle it for us.

Kubernetes is useful because it scales your application without quite as much work. Below is an example of the deployment YAML for a small containerized demo application with two replicas. If you want to follow along with an application of your own, you will need [Minikube](https://minikube.sigs.k8s.io/docs/start/) and [kubectl](https://kubernetes.io/docs/tasks/tools/) installed.

`deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-deployment
  labels:
    app: hello-kubernetes
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-kubernetes
  template:
    metadata:
      labels:
        app: hello-kubernetes
    spec:
      containers:
      - name: flask
        image: dockerhub.io/katcosgrove/fake-container:latest
        ports:
        - containerPort: 5000
```

This deployment YAML describes what I want to happen:

- the name of the pod and application,
- the number of replicas I want,
- the image to run,
- and the port I need.

The Flask application uses port 5000, so the deployment spec does, too. The image isn’t real, but if it were, it would be in a repository called fake-container on my Dockerhub account.

If you were to deploy this with `kubectl apply -f deployment.yaml` and then run `kubectl get pods`, you would see the Deployment created two pods for our application.

What if you decide you need more replicas, though? Go back to your deployment configuration, bump the number of replicas to 5, and apply it again with `kubectl apply -f deployment.yaml`. Run `kubectl get pods`, and you’ll see three more pods coming online!

## Exposing the Application

We probably want to SEE our app, though. The quick and dirty way to do that is port forwarding within the cluster, like this:

`kubectl port-forward deployment/demo-deployment 5000:5000`

Here, we're using kubectl to forward the demo-deployment's port 5000 to our local port 5000. If you go to localhost:5000 in a browser, you'll see your application.

That’s not very convenient, though, and it doesn’t offer much in the way of customization or control. We need to add an ingress controller. NGINX-ingress is popular, and minikube already has an addon, but there are many other options.

Install it by running `minikube addons enable ingress`.

To confirm that the pods are up, run `kubectl get pods -n kube-system` and look for pods that start with "ingress-nginx". Note that other Kubernetes environments will put these in the "ingress-nginx" namespace instead. Now let’s add a `ClusterIP` service. That's what exposes your deployment within the cluster.

`service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 5000
  selector:
    app: demo-deployment
  type: ClusterIP
```

Like always, we have metadata like a name, we tell it which ports to target (remember our Flask app is targeting port 5000), and we give the name of the deployment.

The last thing we need to do is define the ingress resource. It’s the final piece that allows our application to be this is what exposes your application to the outside world.

`ingress.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-ingress
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
          name: demo-service
          port:
            Number: 8080
```

Like with all of our other config files, we're giving it metadata and telling it what to target. In this case, it's the service we defined and the service's port.

As before, apply it with `kubectl apply -f ingress.yaml`

Now, if you run `kubectl get ingress`, you’ll get an IP address. Go there in a browser, and there's your app, deployed on Kubernetes!

## Python instead of YAML

Okay, but this all feels very Ops-centric still -- we’re writing YAML, not a programming language, and I promised you a familiar programming language. Let’s use Pulumi to do it with Python instead.

Before, we had a ton of YAML, now infrastructure as code tools lets us cut a window from the Ops silo to the Dev silo, so we can share stuff, talk a bit more, and work together. You can stand up the infrastructure to deploy your application on Kubernetes right there in the application code! Fortunately, Pulumi has a bunch of different examples of how to do this.

First, you need [Pulumi installed](https://www.pulumi.com/docs/get-started/install/). Then, you need to [configure Kubernetes for Pulumi](https://www.pulumi.com/registry/packages/kubernetes/installation-configuration/). From here, we can deploy to Kubernetes without touching a shred of YAML directly.

Below is an example of the code required to deploy NGINX to Kubernetes, with two replicas, but this time, in more familiar Python instead of YAML.

```python
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, ContainerPortArgs, PodSpecArgs, PodTemplateSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs

config = pulumi.Config()
nginxLabels = {"app": "nginx"}
nginxDeployment = Deployment(
    "nginx-deployment",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=nginxLabels),
        replicas=2 if config.get_int("replicas") is None else config.get_int("replicas"),
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=nginxLabels),
            spec=PodSpecArgs(
                containers=[ContainerArgs(
                    name="nginx",
                    image="nginx:1.7.9",
                    ports=[ContainerPortArgs(container_port=80)],
                )],
            ),
        ),
    ))

pulumi.export("nginx", nginxDeployment.metadata.apply(lambda m: m.name))
```

In just 25 lines and one file, we’ve set up a deployment with two replicas of a containerized application and exposed it. It’s happening in a language you’re familiar with, and it can live right alongside your application code, rather than keeping everything in silos. If you want to increase the number of replicas, it requires no more effort than it did when using YAML.

Keeping the Dev team and the Ops team isolated from one another leads to misunderstandings, confusion, and a slower release cycle. At the very least, both parties need to understand each other, which means Devs need to learn a bit more about Kubernetes. Pulumi can help you speak Kubernetes in your favorite language.

This example is all local, though, and you might not be running Kubernetes on-prem. What if you want to abstract things away even further? Tune in next time for Kubernetes on cloud providers!
