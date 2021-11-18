---
title: "Deploying new Azure Container Apps with familiar languages"
date: 2021-11-02T09:00:00-07:00
meta_desc: "Use the Pulumi Azure Native Provider to deploy containerized apps to Microsoft's new Azure Container Apps platform for serverless apps."
meta_image: container-apps.jpg
authors:
    - mikhail-shilkov
tags:
    - azure
---

Today, Microsoft [announced](https://aka.ms/containerapps/ignite-blog) a new general-purpose serverless container platform: [Azure Container Apps](https://aka.ms/containerapps/). Container Apps is a fully managed platform for microservice applications that runs on top of Kubernetes and open-source technologies like KEDA, Envoy, and Dapr.

Container Apps are designed to abstract infrastructure management with flexible serverless containers. Developers can run containers at scale without the burden of standing up and managing a Kubernetes cluster manually.

We are happy to announce same-day support for Azure Container Apps in the Pulumi [Azure Native Provider](/registry/packages/azure-native), which covers 100% of the Azure Resource Manager APIs and gives you highest fidelity integration with Azure's resources.

<!--more-->

<div class="bg-purple-100 text-sm rounded-lg py-1 px-4">

#### Azure Container Apps QuickStart

Ready to get up and running quickly right away?

- Bootstrap a project `$ pulumi new https://github.com/pulumi/apps/container-apps`
- Add your container logic to the `app` folder
- Deploy with `$ pulumi up`
- Test with `$ curl $(pulumi stack output url)`

For additional information on how Azure Container Apps work and advanced options, please read on.

</div>

The new service supports a broad range of usage scenarios, including

- Microservices over HTTP or gRPC
- HTTP APIs and websites
- Event processing workers
- Long-running background jobs

## Serverless containers

Container Apps provide serverless containers for microservice developers.

- **Managed infrastructure**. Microsoft operates the control plane that takes care of orchestrating containers and their configuration, allowing developers to focus on apps, not cloud infrastructure.
- **Fully integrated auto-scaling with scale to zero**. The platform relies on Kubernetes Event-driven Autoscaling (KEDA) to scale apps and microservices dynamically based on HTTP traffic or event workload.
- **Consumption pricing**. The billing model is based on the actual resource consumption with per-second granularity. Applications incur charges per request, compute time and memory used with no need to pre-provision a fixed capacity.
- **Any language, any base image**. Container Apps put no limitation on the container images. You may use an arbitrary base image and host any web server or a console application, ensuring flexibility and interoperability with other container orchestrators.

## How it works

Microsoft has built Container Apps as a managed service on the foundation of open-source technology in the Kubernetes ecosystem. This enables teams to build microservices without having to manage Kubernetes directly while providing application portability by leveraging open standards and APIs. Behind the scenes, every container app runs on the [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/overview/kubernetes-on-azure/). Enabling open-source integrations include:

**Envoy**, a built-in ingress controller that exposes user containers internally and externally via HTTP endpoints. It supports multiple container versions with dynamic load balancing and several traffic rollout strategies.

**KEDA** enables dynamic auto-scaling for user applications based on the current workload, including scaling down to zero during idle periods.

Container Apps are also tightly integrated with **Dapr**&mdash;an open-source runtime system designed to support cloud-native microservice applications. It provides extra blocks for service discovery, state management, asynchronous message passing.

## How it's different

A few other services provided by Microsoft Azure and other cloud providers operate in the space of running container-based workloads:

**Azure Kubernetes Service** delivers the full power of Kubernetes but requires expertise in configuring and operating the cluster. When building on AKS, users handle most infrastructure management aspects themselves. Instead, Container Apps provide a platform built on top of AKS, focusing on developer productivity and switching to consumption-based pricing.

**Azure Container Instances** (ACI) provides atomic infrastructure units with per-usage pricing. However, ACI comes without higher-level functionality like auto-scaling, load balancing, versioning, and managed rollouts.

**Azure App Service** is a Platform-as-a-Service comparable to Container Apps in terms of being simple-to-operate and developer-friendly. App Service can also run arbitrary containers. However, it is best suited to run websites. The billing model is mostly capacity-based with some built-in autoscaling but without scaling to zero.

**Azure Functions** is a developer-oriented truly-serverless offering. However, it comes with an opinionated programming model that is focused on achieving a high developer productivity as long as your application can use the Azure Functions SDK or container base images. Unlike Container APps, it does not support long-running jobs in consumption mode.

Comparing to other vendors: Azure Container Apps are in the same space as **Google Cloud Run** and **AWS App Runner**. In contrast to the competition, Azure Container Apps is built on Kubernetes and related open-source projects, which should benefit its users in terms of interoperability and transparency. Additionally, Container Apps is the only service that provides features like service discovery for microservices-style communication out of the box.

## Example: Run an HTTP API with Azure Container Apps and Pulumi

Let's walk through the steps to build an example application with Azure Container Apps using infrastructure as code in familiar languages. In this scenario, we create an HTTP application that is available via a public domain name. We'll use Pulumi to provision the necessary resources. In this example, we will use TypeScript however you could also use JavaScript, Python, Go, and C#.

You can check out the complete source code in the Pulumi Examples:

- [TypeScript Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-ts-containerapps)
- [C# Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-cs-containerapps)
- [Python Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-py-containerapps)
- [Go Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-go-containerapps)

### Define a Dockerfile and app

Here are the key features of the container image for our application:

- Based on the `node:8.9.3-alpine` image
- Installs `express` with NPM
- Runs a node web app using `index.js` and `index.html` user files

[Full Dockerfile](https://github.com/pulumi/examples/tree/master/azure-ts-containerapps/node-app/Dockerfile).

### Set up the environment

The resource `KubeEnvironment` defines a cluster that can host multiple Container Apps. Behind the scenes, it creates an AKS cluster in a subscription managed internally by Microsoft and deploys the Apps control plane.

{{< chooser language "typescript,csharp,python,go" / >}}

{{% choosable language typescript %}}

```ts
import * as web from "@pulumi/azure-native/web/v20210301";

const env = new web.KubeEnvironment("env", {
   resourceGroupName: resourceGroup.name,
   type: "Managed",
});
```

{{% /choosable %}}
{{% choosable language csharp %}}

```cs
using Pulumi.AzureNative.Web.V20210301;

var kubeEnv = new KubeEnvironment("env", new KubeEnvironmentArgs
{
    ResourceGroupName = resourceGroup.Name,
    Type = "Managed"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```py
import pulumi_azure_native.web.v20210301 as web

kube_env = web.KubeEnvironment("env",
    resource_group_name=resource_group.name,
    type="Managed")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import web "github.com/pulumi/pulumi-azure-native/sdk/go/azure/web/v20210301"

kubeEnvironment, err := web.NewKubeEnvironment(ctx, "kubeEnvironment", &web.KubeEnvironmentArgs{
    ResourceGroupName: resourceGroup.Name,
    Type:              pulumi.String("Managed"),
})
```

{{% /choosable %}}

### Build and publish a container image

We can build the Docker image and publish it to a new Azure Container Registry (ACR) repository. The code below assumes

{{< chooser language "typescript,csharp,python,go" / >}}

{{% choosable language typescript %}}

```ts
import * as docker from "@pulumi/docker";
import * as containerregistry from "@pulumi/azure-native/containerregistry";

const customImage = "node-app";
const registry = new containerregistry.Registry("registry", {
   resourceGroupName: resourceGroup.name,
   sku: {
       name: "Basic",
   },
   adminUserEnabled: true,
});

const credentials = containerregistry.listRegistryCredentialsOutput({
    resourceGroupName: resourceGroup.name,
    registryName: registry.name,
});
const adminUsername = credentials.apply(c => c.username!);
const adminPassword = credentials.apply(c => c.passwords![0].value!);

const myImage = new docker.Image(customImage, {
   imageName: pulumi.interpolate`${registry.loginServer}/${customImage}:v1.0.0`,
   build: { context: `./${customImage}` },
   registry: {
       server: registry.loginServer,
       username: adminUsername,
       password: adminPassword,
   },
});
```

{{% /choosable %}}
{{% choosable language csharp %}}

```cs
using Pulumi.AzureNative.ContainerRegistry;
using Pulumi.Docker;

var registry = new Registry("registry", new RegistryArgs
{
    ResourceGroupName = resourceGroup.Name,
    Sku = new SkuArgs { Name = "Basic" },
    AdminUserEnabled = true
});

var credentials = Output.Tuple(resourceGroup.Name, registry.Name)
                        .Apply(items =>
    ListRegistryCredentials.InvokeAsync(new ListRegistryCredentialsArgs
    {
        ResourceGroupName = items.Item1,
        RegistryName = items.Item2
    }));
var adminUsername = credentials.Apply(c => c.Username);
var adminPassword = credentials.Apply(c => c.Passwords[0].Value);

var customImage = "node-app";
var myImage = new Image(customImage, new ImageArgs
{
    ImageName = Output.Format($"{registry.LoginServer}/{customImage}:v1.0.0"),
    Build = new DockerBuild { Context = $"./{customImage}" },
    Registry = new ImageRegistry
    {
        Server = registry.LoginServer,
        Username = adminUsername,
        Password = adminPassword
    }
});
```

{{% /choosable %}}
{{% choosable language python %}}

```py
from pulumi_azure_native import containerregistry
import pulumi_docker as docker

registry = containerregistry.Registry("registry",
    resource_group_name=resource_group.name,
    sku=containerregistry.SkuArgs(name="Basic"),
    admin_user_enabled=True)

credentials = pulumi.Output.all(resource_group.name, registry.name).apply(
    lambda args: containerregistry.list_registry_credentials(
        resource_group_name=args[0],
        registry_name=args[1]))
admin_username = credentials.username
admin_password = credentials.passwords[0]["value"]

custom_image = "node-app"
my_image = docker.Image(custom_image,
    image_name=registry.login_server.apply(
        lambda login_server: f"{login_server}/{custom_image}:v1.0.0"),
    build=docker.DockerBuild(context=f"./{custom_image}"),
    registry=docker.ImageRegistry(
        server=registry.login_server,
        username=admin_username,
        password=admin_password))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/containerregistry"
	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

registry, err := containerregistry.NewRegistry(ctx, "registry", &containerregistry.RegistryArgs{
    ResourceGroupName: resourceGroup.Name,
    Sku: containerregistry.SkuArgs{
        Name: pulumi.String("Basic"),
    },
    AdminUserEnabled: pulumi.Bool(true),
})
if err != nil {
    return err
}
credentials := pulumi.All(resourceGroup.Name, registry.Name).ApplyT(
    func(args []interface{}) (*containerregistry.ListRegistryCredentialsResult, error) {
        resourceGroupName := args[0].(string)
        registryName := args[1].(string)
        return containerregistry.ListRegistryCredentials(ctx, &containerregistry.ListRegistryCredentialsArgs{
            ResourceGroupName: resourceGroupName,
            RegistryName:      registryName,
        })
    },
)

adminUsername := credentials.ApplyT(func(result interface{}) (string, error) {
    credentials := result.(*containerregistry.ListRegistryCredentialsResult)
    return *credentials.Username, nil
}).(pulumi.StringOutput)
adminPassword := credentials.ApplyT(func(result interface{}) (string, error) {
    credentials := result.(*containerregistry.ListRegistryCredentialsResult)
    return *credentials.Passwords[0].Value, nil
}).(pulumi.StringOutput)

newImage, err := docker.NewImage(ctx, "node-app", &docker.ImageArgs{
    ImageName: pulumi.Sprintf("https://%s/node-app:v1.0.0", registry.LoginServer),
    Build: docker.DockerBuildArgs{
        Context: pulumi.String("/node-app"),
    },
    Registry: docker.ImageRegistryArgs{
        Server:   registry.LoginServer,
        Username: adminUsername,
        Password: adminPassword,
    },
})
if err != nil {
    return err
}
```

{{% /choosable %}}

## Deploy the container app

Finally, we can define the Container App itself. We point the App to the environment resource and instruct it to run our custom image. Image container credentials are specified in the `configuration` block, with the password marked as a secret. We've also enabled external ingress to publish the app on the web.

{{< chooser language "typescript,csharp,python,go" / >}}

{{% choosable language typescript %}}

```ts
const containerApp = new web.ContainerApp("app", {
   resourceGroupName: resourceGroup.name,
   kubeEnvironmentId: env.id,
   configuration: {
       ingress: {
           external: true,
           targetPort: 80,
       },
       registries: [{
           server: registry.loginServer,
           username: adminUsername,
           passwordSecretRef: "pwd",
       }],
       secrets: [{
           name: "pwd",
           value: adminPassword,
       }],
   },
   template: {
       containers: [{
           name: "myapp",
           image: myImage.imageName,
       }],
   }
});

export const url = pulumi.interpolate`https://${containerApp.configuration.ingress.fqdn}`;
```

{{% /choosable %}}
{{% choosable language csharp %}}

```cs
var containerApp = new ContainerApp("app", new ContainerAppArgs
{
    ResourceGroupName = resourceGroup.Name,
    KubeEnvironmentId = kubeEnv.Id,
    Configuration = new ConfigurationArgs
    {
        Ingress = new IngressArgs
        {
            External = true,
            TargetPort = 80
        },
        Registries = {
            new RegistryCredentialsArgs
            {
                Server = registry.LoginServer,
                Username = adminUsername,
                PasswordSecretRef = "pwd"
            }
        },
        Secrets = {
            new SecretArgs
            {
                Name = "pwd",
                Value = adminPassword
            }
        },
    },
    Template = new TemplateArgs
    {
        Containers = {
            new ContainerArgs
            {
                Name = "myapp",
                Image = myImage.ImageName
            }
        }
    }
});

this.Url = Output.Format($"https://{containerApp.Configuration.Apply(c => c.Ingress).Apply(i => i.Fqdn)}");
```

{{% /choosable %}}
{{% choosable language python %}}

```py
container_app = web.ContainerApp("app",
    resource_group_name=resource_group.name,
    kube_environment_id=kube_env.id,
    configuration=web.ConfigurationArgs(
        ingress=web.IngressArgs(
            external=True,
            target_port=80),
        registries=[web.RegistryCredentialsArgs(
            server=registry.login_server,
            username=admin_username,
            password_secret_ref="pwd")],
        secrets=[web.SecretArgs(
            name="pwd",
            value=admin_password)],
    ),
    template=web.TemplateArgs(
        containers=[web.ContainerArgs(
            name="myapp",
            image=my_image.image_name)]))

pulumi.export("url", container_app.configuration.apply(lambda c: c.ingress).apply(lambda i: i.fqdn))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
containerApp, err := web.NewContainerApp(ctx, "app", &web.ContainerAppArgs{
    ResourceGroupName: resourceGroup.Name,
    KubeEnvironmentId: kubeEnvironment.ID(),
    Configuration: web.ConfigurationArgs{
        Ingress: web.IngressArgs{
            External:   pulumi.Bool(true),
            TargetPort: pulumi.IntPtr(80),
        },
        Registries: web.RegistryCredentialsArray{
            web.RegistryCredentialsArgs{
                Server:            registry.LoginServer,
                Username:          adminUsername,
                PasswordSecretRef: pulumi.String("pwd")},
        },
        Secrets: web.SecretArray{
            web.SecretArgs{
                Name:  pulumi.String("pwd"),
                Value: adminPassword,
            },
        },
    },
    Template: web.TemplateArgs{
        Containers: web.ContainerArray{
            web.ContainerArgs{
                Name:  pulumi.String("myapp"),
                Image: newImage.ImageName,
            },
        },
    },
})
if err != nil {
    return err
}

ctx.Export("url", pulumi.Sprintf("https://%s", containerApp.LatestRevisionFqdn))
```

{{% /choosable %}}

### Test the app

And that is it! We run `pulumi up` to get the application up and running. Once the deployment completes, we can send an HTTP request and check the response.

```sh
$ curl $(pulumi stack output url)
<html>
<body>
<h1>Your custom docker image is running in Azure Container Apps!</h1>
</body>
</html>
```

## Conclusion

Azure Container Apps enable you to build applications in your favorite language with any dependencies and tools, package them as a container image, and deploy them in seconds. Container Apps abstract away infrastructure management by automatically scaling up and down to zero and only charging for the exact resources you use.

This post shows how to use Pulumi to build a container image and publish it as an Azure Container App. Pulumi makes it easy to create artifacts and provision and manage cloud infrastructure on any cloud using familiar programming languages, including C#, TypeScript, Python, and Go. Docker images, ACR registries, container environments, and Apps can be managed within the same infrastructure definition.

### Further steps

- [Get Started with Pulumi for Azure today.]({{<relref "/docs/get-started/azure">}})
- [Read about Azure Container Apps announcement.](https://aka.ms/containerapps/ignite-blog)

#### Complete Azure Container Apps example

- [TypeScript Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-ts-containerapps)
- [C# Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-cs-containerapps)
- [Python Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-py-containerapps)
- [Go Azure Container Apps Example](https://github.com/pulumi/examples/tree/master/azure-go-containerapps)
