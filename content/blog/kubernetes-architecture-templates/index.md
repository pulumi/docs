---
title: "Using Kubernetes Arch Templates with Poetry and Python"
date: 2022-12-07
meta_desc: Set up a Google Kubernetes Engine cluster for a web application with archtecture
  templates, all with Python and Poetry.
meta_image: meta.png
authors:
  - laura-santamaria
tags:
  - kubernetes
  - arch-templates
  - templates
search:
  keywords:
    - poetry
    - kubernetes
    - arch
    - templates
    - archtecture
    - python
    - engine
---

When building with Kubernetes for the first time, we often need to stand up a lot of infrastructure just to get to the point of having a base to build an application. Let's explore how we can wire together two of our architecture templates to generate a base for a web application running on Kubernetes on Google Cloud with Python and Poetry.

<!--more-->

## A primer on microservices

To work with Kubernetes, you're generally following a microservices architecture. In short, here's how to think about a microservices architecture: Each logical component of your application is its own individual process acting as a closed box that defines what data must come in and what data is delivered on the other end---what's known as a _service_. Services communicate with one another via APIs or similar small interfaces, and each service addresses one part of your business logic inside your application.

In a typical, very basic web application set up in a generic microservices architecture, you might have a data store, a backend, and a frontend (a user interface, or UI). In practice, you might have multiple backends and data stores to address multiple activities like logging in, running a shopping cart, delivering shipping updates, and more.

To ensure all of these services work together, an orchestrator like Kubernetes ensures each service is running and healthy, is connected to the others, and runs as expected.

## A typical Kubernetes architecture

A Kubernetes _cluster_ is a collection of one or more machines (either virtual or bare-metal) called _nodes_ that host groups of _containers_, with each group containing multiple copies of a microservice. These groups of containers are called _pods_. And then, to connect and expose those pods to one another and the world, we add in _services_.

For our system that we'll build today, we're going to have a cluster running on Google Kubernetes Engine (GKE). We'll create a namespace on that Kubernetes instance, which will hold all of our Kubernetes app resources. We'll have a _deployment_ that takes the configuration we need for NGINX (a _ConfigMap_) and spins up a pod holding the containers running that NGINX server. Then, we'll have a service that exposes the ports so we can access our NGINX server from anywhere.

## Start with templates

We're going to build our entire architecture starting with two templates: Our GKE template and our Kubernetes web app template. [Learn more about our new architecture templates.](/blog/intro-architecture-templates)

This will be a bit different than our usual workflow. Generally, we here at Pulumi prefer to stand up different stacks for each type of infrastructure (so one project with one or more stacks for the Kubernetes cluster and then one project with one or more stacks for the web application). However, in this case, let's explore together what happens if we're want to have it all go up together as one project and stack while keeping the code in different files.

First, create a new directory to hold all of our project files, and add `app` and `infra` directories inside this root directory.

```bash
$ mkdir k8s-templates && cd k8s-templates
$ mkdir app
$ mkdir infra
```

In the `infra` directory, we'll add [the GKE template](/templates/kubernetes/gcp) first. We're [using the `--generate-only` flag](/docs/cli/commands/pulumi_new#options) to avoid creating the default virtual environment and the various extra stack information since we're using Poetry and will be running everything from the root directory later:

```bash
$ cd infra
$ pulumi new kubernetes-gcp-python --generate-only
```

Accept all of the standard default values, except give your Google Cloud project name here instead of the default.

In the `app` directory, we'll add the [web app template](/templates/kubernetes-application/web-application):

```bash
$ cd ../app
$ pulumi new webapp-kubernetes-python --generate-only
```

When it asks you for a project name in the `app` directory, give it the name `app-mi-k8s`. Otherwise, accept all of the default values (using your Google Cloud details).

And now, the real fun begins!

## Putting it all together

We're going to use [Poetry](https://python-poetry.org/docs/) instead of the default virtual environment as we're going to be working in a number of different directories that all need the same virtual environment and dependencies. In the root of the project, let's initialize a Poetry project. We'll need to define all of the dependencies from the application and infrastructure requirements:

```bash
$ cd ../ # if you need to go back to your project root
$ poetry init
# In the dynamic generation of dependencies, add pulumi, pulumi-gcp, and pulumi-kubernetes.
# Otherwise, fill in the other pieces as you would normally.
```

Then install the dependencies:

```bash
$ poetry install
```

Now, we can pull the metadata file for Pulumi in:

```bash
$ touch Pulumi.yaml
$ cat infra/Pulumi.yaml > Pulumi.yaml
$ touch Pulumi.dev.yaml
```

And do a quick cleanup of the `Pulumi.dev.yaml` file:

{{< code-filename file="<root>/Pulumi.dev.yaml" />}}

```yaml {.line-numbers}
config:
  namespace: fake-ns
  replicas: 1
  gcp:project: <your-project>
  gcp:region: <your-region>
```

{{% notes type="info" %}}
Since we're running on GKE, we need to define a different namespace than `default`. I used `fake-ns`.
{{% /notes %}}

We'll need to modify the `Pulumi.yaml` file to remove the virtual environment:

{{< code-filename file="<root>/Pulumi.yaml" />}}

```yaml {.line-numbers}
name: k8s-combo-infra
description: A Python program to deploy a Kubernetes cluster and application on Google Cloud
runtime: python
```

And now we can set up our new `__main__.py` file! Create a new `__main__.py` file in the root of the repo, and add this code:

{{< code-filename file="<root>/__main__.py" />}}

```python {.line-numbers}
from pulumi import export as pulumi_export
from pulumi import Output
import app.__main__ as app
import infra.__main__ as infra_code

infra = infra_code

kubeconf = infra.cluster_kubeconfig
app_infra = kubeconf.apply(
    lambda val: app.create_app(kubeconfig_val=val)
)

pulumi_export("endpoint_url", Output.unsecret(app_infra))
```

We do need to make a couple small changes to the `app/__main__.py` file. We need to

1. wrap the code in a callable function so we can use that `apply()` call in the root file,
1. add a custom provider to use the right `kubeconfig` settings,
1. pass that provider context to all of the resources, and
1. get the endpoint from our app:

{{< code-filename file="<root>/app/__main__.py" />}}

```python {.line-numbers hl_lines=[5,"14-19",27,51,93,109,111,117]}
import pulumi
import pulumi_kubernetes as kubernetes


def create_app(kubeconfig_val):
    # Get some values from the Pulumi stack configuration, or use defaults
    config = pulumi.Config()
    k8s_namespace = config.get("namespace", "default")
    num_replicas = config.get_float("replicas", 1)
    app_labels = {
        "app": "nginx",
    }

    # NEW: Create a provider that consumes the upstream kubeconfig
    new_provider = kubernetes.Provider(
        "app_provider",
        kubeconfig=kubeconfig_val,
        namespace=k8s_namespace
    )

    # Create a namespace
    webserverns = kubernetes.core.v1.Namespace(
        "webserver",
        metadata=kubernetes.meta.v1.ObjectMetaArgs(
            name=k8s_namespace,
        ),
        opts=pulumi.ResourceOptions(provider=new_provider)
    )

    # Create a ConfigMap for the Nginx configuration
    webserverconfig = kubernetes.core.v1.ConfigMap(
        "webserverconfig",
        metadata=kubernetes.meta.v1.ObjectMetaArgs(
            namespace=webserverns.metadata.name,
        ),
        data={
            "nginx.conf": """events { }
    http {
      server {
        listen 80;
        root /usr/share/nginx/html;
        index index.html index.htm index.nginx-debian.html
        server_name _;
        location / {
          try_files $uri $uri/ =404;
        }
      }
    }
    """,
        },
        opts=pulumi.ResourceOptions(provider=new_provider)
    )

    # Create a Deployment with a user-defined number of replicas
    webserverdeployment = kubernetes.apps.v1.Deployment(
        "webserverdeployment",
        metadata=kubernetes.meta.v1.ObjectMetaArgs(
            namespace=webserverns.metadata.name,
        ),
        spec=kubernetes.apps.v1.DeploymentSpecArgs(
            selector=kubernetes.meta.v1.LabelSelectorArgs(
                match_labels=app_labels,
            ),
            replicas=num_replicas,
            template=kubernetes.core.v1.PodTemplateSpecArgs(
                metadata=kubernetes.meta.v1.ObjectMetaArgs(
                    labels=app_labels,
                ),
                spec=kubernetes.core.v1.PodSpecArgs(
                    containers=[kubernetes.core.v1.ContainerArgs(
                        image="nginx",
                        name="nginx",
                        volume_mounts=[kubernetes.core.v1.VolumeMountArgs(
                            mount_path="/etc/nginx/nginx.conf",
                            name="nginx-conf-volume",
                            read_only=True,
                            sub_path="nginx.conf",
                        )],
                    )],
                    volumes=[kubernetes.core.v1.VolumeArgs(
                        config_map=kubernetes.core.v1.ConfigMapVolumeSourceArgs(
                            items=[kubernetes.core.v1.KeyToPathArgs(
                                key="nginx.conf",
                                path="nginx.conf",
                            )],
                            name=webserverconfig.metadata.name,
                        ),
                        name="nginx-conf-volume",
                    )],
                ),
            ),
        ),
        opts=pulumi.ResourceOptions(provider=new_provider)
    )

    # Expose the Deployment as a Kubernetes Service
    webserverservice = kubernetes.core.v1.Service(
        "webserverservice",
        metadata=kubernetes.meta.v1.ObjectMetaArgs(
            namespace=webserverns.metadata.name,
        ),
        spec=kubernetes.core.v1.ServiceSpecArgs(
            ports=[kubernetes.core.v1.ServicePortArgs(
                port=80,
                target_port=80,
                protocol="TCP",
            )],
            selector=app_labels,
            type="LoadBalancer"
        ),
        opts=pulumi.ResourceOptions(provider=new_provider)
    )

    # Export some values for use elsewhere
    pulumi.export("deploymentName", webserverdeployment.metadata.name)
    pulumi.export("serviceName", webserverservice.metadata.name)
    return webserverservice.status.apply(lambda val: val.load_balancer.ingress[0].ip)
```

Now that all our changes have been made, let's try running it! We'll need to prepend `poetry run` to the commands, unless you choose to switch to the Poetry shell ahead of time:

```bash
$ poetry run pulumi stack init dev
$ poetry run pulumi stack select dev
$ poetry run pulumi up
```

And up they all go! Note that this takes a while, so don't panic!

{{< code-filename file="output" />}}

```bash
Previewing update (dev)

View Live: https://app.pulumi.com/nimbinatus/k8s-combo-infra/dev/previews/fe73460a-a846-475c-9a69-23626e56b4e4

     Type                           Name                 Plan
 +   pulumi:pulumi:Stack            k8s-combo-infra-dev  create
 +   ├─ gcp:compute:Network         gke-network          create
 +   ├─ gcp:compute:Subnetwork      gke-subnet           create
 +   ├─ gcp:container:Cluster       gke-cluster          create
 +   ├─ gcp:serviceAccount:Account  gke-nodepool-sa      create
 +   └─ gcp:container:NodePool      gke-nodepool         create


Outputs:
    clusterId   : output<string>
    clusterName : "gke-cluster-dd00d9f"
    endpoint_url: output<string>
    kubeconfig  : output<string>
    networkId   : output<string>
    networkName : "gke-network-e0ce7fb"

Resources:
    + 6 to create

Do you want to perform this update? yes
Updating (dev)

View Live: https://app.pulumi.com/nimbinatus/k8s-combo-infra/dev/updates/109

     Type                              Name                 Status
 +   pulumi:pulumi:Stack               k8s-combo-infra-dev  created (915s)
 +   ├─ gcp:compute:Network            gke-network          created (21s)
 +   ├─ gcp:compute:Subnetwork         gke-subnet           created (11s)
 +   ├─ gcp:container:Cluster          gke-cluster          created (682s)
 +   ├─ pulumi:providers:kubernetes    app_provider         created (0.17s)
 +   ├─ gcp:serviceAccount:Account     gke-nodepool-sa      created (1s)
 +   ├─ kubernetes:core/v1:Namespace   webserver            created (0.52s)
 +   ├─ gcp:container:NodePool         gke-nodepool         created (125s)
 +   ├─ kubernetes:core/v1:ConfigMap   webserverconfig      created (0.32s)
 +   ├─ kubernetes:core/v1:Service     webserverservice     created (193s)
 +   └─ kubernetes:apps/v1:Deployment  webserverdeployment  created (144s)


Outputs:
    clusterId   : "projects/pulumi-development/locations/us-central1/clusters/gke-cluster-6cc9507"
    clusterName : "gke-cluster-6cc9507"
    endpoint_url: "35.224.177.197"
    kubeconfig  : [secret]
    networkId   : "projects/pulumi-development/global/networks/gke-network-68b9493"
    networkName : "gke-network-68b9493"

Resources:
    + 11 created

Duration: 15m17s
```

If you `CURL` the endpoint, you get the default NGINX page that tells us the webserver is ready to go:

```bash
$ curl $(pulumi stack output endpoint_url)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Finally, if you're done with the cluster, don't forget to pull it down so you don't get charged!

```bash
$ poetry run pulumi destroy -y
```

If you run into an issue where the cluster gets deleted before the various app resources (the namespace, the service, etc.) get removed, you may get an error that you can't finish destroying the stack. Because the cluster is already gone, the Kubernetes provider can't access it to update the status of the various app resources. So you'll need to remove those resources from your state file as they were removed with the deletion of the cluster:

```bash
$ poetry run pulumi state delete urn:pulumi:dev::k8s-combo-infra::kubernetes:core/v1:Namespace::webserver --target-dependents
```

Then, refresh and destroy the rest of the resources, including the outputs:

```bash
$ poetry run pulumi refresh -y
$ poetry run pulumi destroy -y
```

<hr/>

If you want to try this out, head over to [this example repo](https://github.com/pulumi/pulumitv/tree/master/2022-11-mi-k8s-templates) to explore the code and pull it down to run yourself. Don't forget to [create a Pulumi account](https://app.pulumi.com/signup) first!

If you want to explore the other templates we have available for you, head to [our templates page](/templates) to explore.
