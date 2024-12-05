---
title: "Creating Resources on Kubernetes"
title_tag: "Creating Resources on Kubernetes"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to define and provision resources on Kubernetes using Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to define and provision resources on Kubernetes using Pulumi.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
  In Pulumi, resources represent the fundamental units that make up your infrastructure, such as virtual machines, networks, storage, and databases. A resource is used to define and manage an infrastructure object in your Pulumi configuration.
  
  In this tutorial, you will create a simple Nginx server hosted on Kubernetes. You will then refer to documentation in the Pulumi Registry to create a service to make the Nginx deployment accessible.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
  - How to create a new resource
  - How to reference resource definitions in the Pulumi documentation

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
  - The [Pulumi CLI](/docs/install/)
  - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
  - A running [Minikube](https://minikube.sigs.k8s.io/docs/start/) cluster
  - The Kubernetes command line tool [kubectl](https://kubernetes.io/docs/tasks/tools/) installed
  - Your desired [language runtime installed](/docs/iac/get-started/aws/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
  - kubernetes
---

## Create a new project

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and [create a new project and stack](/docs/iac/get-started/kubernetes/create-project/).

```bash
# Login to Pulumi by following the prompts
$ pulumi login

Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :

-------------

# Create new project (example using Python)
$ mkdir pulumi-tutorial-k8s
$ cd pulumi-tutorial-k8s
$ pulumi new python
```

Then replace the default code with the following code snippet to scaffold your project with the required imports and overall program structure:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="1" to="6" >}}

// Create a deployment

// Create a service
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="1" to="6" >}}

// Create a deployment

// Create a service
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="1" to="6" >}}

# Create a deployment

# Create a service
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="1" to="16" >}}

        // Create a deployment

        // Create a service

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="72" to="74" >}}  
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="1" to="14" >}}

    // Create a deployment

    // Create a service

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="80" to="80" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="1" to="9" >}}

# Create a deployment

# Create a service
```

{{% /choosable %}}

This tutorial will define resources using the [Kubernetes provider](/registry/packages/kubernetes/), so you will also need to make sure to [install the Kubernetes dependency](/registry/packages/kubernetes/installation-configuration/#installation) into your project.

## Configure Kubernetes access

Now that you have a Pulumi project created, you will need to configure the Pulumi CLI to access your Kubernetes environment, in this case the Minikube cluster. Start by verifying that Minikube is running in your environment:

```bash
$ minikube status

minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

Then configure the Pulumi CLI to connect to your Minikube cluster by running the following command:

```bash
$ pulumi config set kubernetes:context minikube
```

For the purposes of this tutorial, the default `kubeconfig` is used, but you are also able to specify a custom `kubeconfig file` if desired as shown below:

```bash
pulumi config set kubernetes:kubeconfig ./minikube-config.yaml
```

## Create a deployment

The first resource you will create will be a Kubernetes deployment. The [Pulumi Registry](/registry/) provides the documentation for all of the Pulumi providers and their associated resources. Open the [kubernetes.apps/v1.Deployment documentation page](/registry/packages/kubernetes/api-docs/apps/v1/deployment/) to view a description of this resource, example usage, the resource definition, and supported properties. You will now define your deployment resource as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="1" to="16" >}}

// Create a service
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="1" to="16" >}}

// Create a service
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="1" to="17" >}}

# Create a service
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="1" to="39" >}}

        // Create a service

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="72" to="74" >}}  
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="1" to="51" >}}

    // Create a service

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="80" to="80" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="1" to="23" >}}

# Create a service
```

{{% /choosable %}}

All resources have a required [`name`](https://www.pulumi.com/docs/concepts/resources/names/) argument. Each resource has both a [logical name](https://www.pulumi.com/docs/concepts/resources/names/#logicalname) and a [physical name](https://www.pulumi.com/docs/concepts/resources/names/#autonaming). The **logical name** is how the resource is known inside Pulumi. This is the value provided to the required `name` argument. The **physical name** is the name used for the resource in the cloud provider that a Pulumi program is deploying to. It is a combination of the logical name plus a random suffix which helps to prevent resource naming collisions.

In the above example, the logical name for our `deployment` resource is **"nginx"**, and the physical name might typically look something like **"nginx-d7c2fa0"**.

In addition to names, resources have properties and options.

**Properties** are used to specify what type of resource to create. Properties are often resource-specific, and they can be required or optional depending on the specifications of the provider.

The property defined in your `kubernetes.apps/v1.Deployment` resource is:

| Property | Description |
|--------------|-------------|
| **spec** | tells the Kubernetes provider the specification of the desired behavior of the deployment |

**Options** let you control certain aspects of a resource (such as showing explicit dependencies or importing existing infrastructure). You do not have any options defined for this resource, but you can learn more about how it works in the [Resource options documentation](/docs/iac/concepts/options/).

## Deploy your resources

Now run the `pulumi up` command to preview and deploy the resouces you've just defined in your project.

```bash
$ pulumi up -y

Previewing update (k8s-tutorial)

     Type                              Name              Plan
 +   pulumi:pulumi:Stack               k8s-tutorial      create
 +   └─ kubernetes:apps/v1:Deployment  nginx             create

Resources:
    + 2 to create

Updating (k8s-tutorial)

     Type                              Name              Status
 +   pulumi:pulumi:Stack               k8s-tutorial      created (14s)
 +   └─ kubernetes:apps/v1:Deployment  nginx             created (12s)

Resources:
    + 2 created

Duration: 16s
```

## Create a service

In this section, you will use Pulumi documentation to configure a Kubernetes Service. Use the following steps as a guide for adding the Service resource:

- Navigate to the [Kubernetes Registry documentation page](/registry/packages/kubernetes/)
- Search for the `kubernetes.core/v1.Service` resource
- Define the Service resource in your project code
- Preview and deploy your updated project code

Once you have completed these steps, forward the Nginx service to make it accessible from localhost. First, retrieve the name and port of your service using the following command:

```bash
$ kubectl get service
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   44h
nginx-9e5d5cd4   ClusterIP   10.103.199.118   <none>        80/TCP    6m47s
```

In the example above, the name of the service is `nginx-9e5d5cd4`. Then run the following command to perform the forwarding, making sure to provide the name and port of your own Nginx service in your own environment:

```bash
$ kubectl port-forward service/nginx-9e5d5cd4 8080:80
 Forwarding from 127.0.0.1:8080 -> 80
 Forwarding from [::1]:8080 -> 80
```

In a new terminal, verify that Nginx is running and accessible by running curl against the localhost as shown in the below example:

```bash
curl "http://localhost:8080"

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

You should be greated with the HTML code of the Nginx landing page as shown above.

### View complete solution

You can view the complete project code below:

{{< example-program path="k8s-deployment-service-for-minikube" >}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you created a Kubernetes deployment resource, and you created a Service resource by referencing the Pulumi registry. You also reviewed resource properties and example usage of various resources.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Stack Outputs and References](/tutorials/stack-outputs-and-references/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
