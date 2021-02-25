---
title: "Build and publish container images to any cloud with Infrastructure as Code"
allow_long_title: True
authors: ["joe-duffy"]
tags: ["Docker", "Kubernetes"]
meta_desc: "Go from Dockerfile to a fully running containerized service on your cloud of choice using infrastructure as code."
date: "2020-12-08"
meta_image: "containers.png"
---

Going from a containerized application to a service running in the cloud requires a few steps beyond an application's normal build-and-test cycle. Namely, it means building and publishing a container image in a registry and then consuming that image from your target environment, whether that's Kubernetes, Amazon ECS, or another container orchestrator. It's not enough to just write a `Dockerfile` &mdash; you will need to pick a container registry, decide whether that registry should be public or private, authenticate against it, and ideally automate deploying subsequent updates. Infrastructure as code to the rescue! In this article, we'll see how to build, publish, and consume a simple container image across any cloud, using just a few lines of code.

<!--more-->

## Approach

The general approach will be to create a new infrastructure as code project that

* Prepares a container registry, either public or private
* Builds and publishes your container image to that registry
* Optionally, consumes the resulting image URL from a containerized task definition in Kubernetes, Amazon ECS, or any other container orchestrator

All told, this will be just a few dozen lines of code. This article demonstrates doing this in AWS, Azure, GCP, DigitalOcean, and Docker Hub, and offers code examples in each supported Pulumi language, namely Python, JavaScript, TypeScript, Go, and C#. These steps will work for any application that has a `Dockerfile` and is buildable by Docker. In principle, similar steps could be applied if you prefer to build your container image using different means, such as Buildpack.

For purposes of illustration, we'll create a simple Nginx web server whose `Dockerfile` contains:

```dockerfile
FROM nginx
RUN echo "<h1>Hello, World!</h1>" > \
    /usr/share/nginx/html/index.html
```

Now, let's dive in!

## Prepare a Container Registry

The first step is to prepare a new container _registry_. A registry holds one or more _repositories_, each of which can store and serve many different container images with different tags and versions. Afterward we'll show how to build and publish to this registry.

The specific details of how to prepare your registry differ by cloud provider, often significantly, particularly when it comes to authenticating. Pick your cloud provider to see the details:

{{% chooser cloud "aws,azure,gcp,digitalocean,docker" / %}}

{{% choosable cloud aws %}}

<p></p>

### Amazon Elastic Container Registry (ECR)

Amazon Elastic Container Registry (ECR) provides managed Docker container hosting that makes it easy to run containerized applications in your AWS account using Amazon Elastic Container Service (ECS) and Elastic Kubernetes Service (EKS). Each account has a default registry per region, and each registry may have any number of repositories, each for a different Docker image. Each repository can store many versions of that particular image.

#### Create a New Project

To start, create a new project and [ensure it is configured to use your AWS account]({{< relref "/docs/intro/cloud-providers/aws/setup" >}}), and then scaffold your project with the imports and overall program structure that we will fill in one piece at a time:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
var aws = require("@pulumi/aws");
var docker = require("@pulumi/docker");

// [Placeholder 1: Create a private ECR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
import * as aws from "@pulumi/aws";
import * as docker from "@pulumi/docker";

// [Placeholder 1: Create a private ECR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language python >}}

```python
import base64
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker

# [Placeholder 1: Create a private ECR registry.]

# [Placeholder 2: Get registry info (creds and endpoint).]

# [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    "encoding/base64"
    "errors"
    "strings"

    "github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ecr"
    "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Placeholder 1: Create a private ECR registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
        return nil
    })
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws.Ecr;
using Pulumi.Docker;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Placeholder 1: Create a private ECR repository.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
    }
}
```

{{< /choosable >}}

#### Provision an ECR Repository

Next, declare a new ECR repository resource:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Create a private ECR repository.
var repo = new aws.ecr.Repository("my-repo");
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Create a private ECR repository.
const repo = new aws.ecr.Repository("my-repo");
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Create a private ECR repository.
repo = aws.ecr.Repository('my-repo')
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Create a private ECR repository.
repo, err := ecr.NewRepository(ctx, "my-repo", nil)
if err != nil {
    return err
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Create a private ECR repository.
var repo = new Repository("my-repo");
```

{{< /choosable >}}

#### Authenticate with Temporary ECR Access Token

Next, we will need to generate authentication information to access the repository to build and publish our image. ECR supports this in multiple different ways; however, here, we will demonstrate generating a temporary access token:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Get registry info (creds and endpoint).
var imageName = repo.repositoryUrl;
var registryInfo = repo.registryId.apply(id => {
    return aws.ecr.getCredentials({ registryId: id }).then(credentials => {
        var decodedCredentials = Buffer.from(credentials.authorizationToken, "base64").toString();
        var [username, password] = decodedCredentials.split(":");
        if (!password || !username) {
            throw new Error("Invalid credentials");
        }
        return {
            server: credentials.proxyEndpoint,
            username: username,
            password: password,
        };
    });
});
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Get registry info (creds and endpoint).
const imageName = repo.repositoryUrl;
const registryInfo = repo.registryId.apply(async id => {
    const credentials = await aws.ecr.getCredentials({ registryId: id });
    const decodedCredentials = Buffer.from(credentials.authorizationToken, "base64").toString();
    const [username, password] = decodedCredentials.split(":");
    if (!password || !username) {
        throw new Error("Invalid credentials");
    }
    return {
        server: credentials.proxyEndpoint,
        username: username,
        password: password,
    };
});
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Get registry info (creds and endpoint).
def getRegistryInfo(rid):
    creds = aws.ecr.get_credentials(registry_id=rid)
    decoded = base64.b64decode(creds.authorization_token).decode()
    parts = decoded.split(':')
    if len(parts) != 2:
        raise Exception("Invalid credentials")
    return docker.ImageRegistry(creds.proxy_endpoint, parts[0], parts[1])
image_name = repo.repository_url
registry_info = repo.registry_id.apply(getRegistryInfo)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Get registry info (creds and endpoint).
imageName := repo.RepositoryUrl
registryInfo := repo.RegistryId.ApplyT(func(id string) (docker.ImageRegistry, error) {
    creds, err := ecr.GetCredentials(ctx, &ecr.GetCredentialsArgs{RegistryId: id})
    if err != nil {
        return docker.ImageRegistry{}, err
    }
    decoded, err := base64.StdEncoding.DecodeString(creds.AuthorizationToken)
    if err != nil {
        return docker.ImageRegistry{}, err
    }
    parts := strings.Split(string(decoded), ":")
    if len(parts) != 2 {
        return docker.ImageRegistry{}, errors.New("Invalid credentials")
    }
    return docker.ImageRegistry{
        Server:   creds.ProxyEndpoint,
        Username: parts[0],
        Password: parts[1],
    }, nil
}).(docker.ImageRegistryOutput)
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Get registry info (creds and endpoint).
var imageName = repo.RepositoryUrl;
var registryInfo = repo.RegistryId.Apply(async (id) =>
{
    var creds = await GetCredentials.InvokeAsync(new GetCredentialsArgs { RegistryId = id });
    var decodedData = Convert.FromBase64String(creds.AuthorizationToken);
    var decoded = ASCIIEncoding.ASCII.GetString(decodedData);

    var parts = decoded.Split(':');
    if (parts.Length != 2)
    {
        throw new Exception("Invalid credentials");
    }

    return new ImageRegistry
    {
        Server = creds.ProxyEndpoint,
        Username = parts[0],
        Password = parts[1],
    };
});
```

{{< /choosable >}}

#### Alternatively, Authenticate with ECR Credential Helper

An alternative approach ECR supports is to [use the Docker credential helper from Amazon](https://aws.amazon.com/blogs/compute/authenticating-amazon-ecr-repositories-for-docker-cli-with-credential-helper/), which integrates with local IAM settings, adds smart caching, and removes the need for Docker to login. If you elect to go this route, leave out the username/password parts of the `docker.ImageRegistry`:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Get registry info (creds and endpoint).
var imageName = repo.repositoryUrl;
var registryInfo = undefined; // use ECR credentials helper.
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Get registry info (creds and endpoint).
const imageName = repo.repositoryUrl;
const registryInfo = undefined; // use ECR credentials helper.
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Get registry info (creds and endpoint).
image_name = repo.repository_url
registry_info = None # use ECR credentials helper.
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Get registry info (creds and endpoint).
imageName := repo.RepositoryUrl
registryInfo := docker.ImageRegistryArgs{} // use ECR credentials helper.
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Get registry info (creds and endpoint).
var imageName = repo.RepositoryUrl;
// Omit registryInfo and use ECR credentials helper.
```

{{< /choosable >}}

#### Learn More About ECR

ECR offers many additional options not shown here. This includes configuring advanced IAM permissions, enabling image vulnerability scanning, managing the lifetime of images so that older, unused images are deleted based on configured policies, encrypting images, and more. For details on these advanced capabilities and more, refer to [Pulumi's ECR user guide](https://www.pulumi.com/docs/guides/crosswalk/aws/ecr/), [Pulumi's ECR API reference](https://www.pulumi.com/docs/reference/pkg/aws/ecr/repository/), or [Amazon's product documentation](https://aws.amazon.com/ecr/).

> To view another cloud provider's registry details, [select a new cloud in the switcher above](#prepare-a-container-registry).

{{% /choosable %}}

{{% choosable cloud azure %}}

<p></p>

### Azure Container Registry (ACR)

Azure Container Registry (ACR) allows you to build, store, secure, scan, replicate, and manage container images and artifacts using a fully managed and geo-replicated instance of OCI distribution. This makes it easy to deploy containerized workloads to native Azure services like Azure Kubernetes Service (AKS), Red Hat OpenShift, and App Service. Each registry is capable of storing and serving multiple versions of multiple container images.

#### Create a New Project

To start, create a new project and [ensure it is configured to use your Azure account]({{< relref "/docs/intro/cloud-providers/azure/setup" >}}), and then scaffold your project with the imports and overall program structure that we will fill in one piece at a time:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
var azure = require("@pulumi/azure");
var docker = require("@pulumi/docker");

// [Placeholder 1: Create a private ACR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
import * as azure from "@pulumi/azure";
import * as docker from "@pulumi/docker";

// [Placeholder 1: Create a private ACR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language python >}}

```python
import pulumi
import pulumi_azure as azure
import pulumi_docker as docker

# [Placeholder 1: Create a private ACR registry.]

# [Placeholder 2: Get registry info (creds and endpoint).]

# [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure/sdk/v2/go/azure/containerservice"
    "github.com/pulumi/pulumi-azure/sdk/v2/go/azure/core"
    "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Placeholder 1: Create a private ECR registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
        return nil
    })
}        
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Azure.Core;
using Pulumi.Azure.ContainerService;
using Pulumi.Docker;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Placeholder 1: Create a private ECR registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
    }
}
```

{{< /choosable >}}

#### Provision a New ACR Registry

Next, declare a new ACR registry resource. To create a new registry, we need an Azure resource group; here we will create a new one, but feel free to use an existing one by passing its name in the resource group's place:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Create a private ACR registry.
var rg = new azure.core.ResourceGroup("myrg");
var registry = new azure.containerservice.Registry("myregistry", {
    resourceGroupName: rg.name,
    adminEnabled: true,
    sku: "Basic",
});
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Create a private ACR registry.
const rg = new azure.core.ResourceGroup("myrg");
const registry = new azure.containerservice.Registry("myregistry", {
    resourceGroupName: rg.name,
    adminEnabled: true,
    sku: "Basic",
});
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Create a private ACR registry.
rg = azure.core.ResourceGroup('myrg')
registry = azure.containerservice.Registry('myregistry',
    resource_group_name=rg.name,
    admin_enabled=True,
    sku='Basic'
)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Create a private ACR registry.
rg, err := core.NewResourceGroup(ctx, "myrg", nil)
if err != nil {
    return err
}
registry, err := containerservice.NewRegistry(ctx, "my-repo", &containerservice.RegistryArgs{
    ResourceGroupName: rg.Name,
    AdminEnabled:      pulumi.Bool(true),
    Sku:               pulumi.String("Basic"),
})
if err != nil {
    return err
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Create a private ACR registry.
var rg = new ResourceGroup("myrg");
var registry = new Registry("myregistry", new RegistryArgs
{
    ResourceGroupName = rg.Name,
    AdminEnabled = true,
    Sku = "basic"
});
```

{{< /choosable >}}

#### Authenticate with Admin Account

Now we need to gather up the image name and registry authentication information, which has been auto-generated by Azure, in preparation for building and publishing to it. For this simple example, we have enabled admin access, which we will use to authenticate:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Get registry info (creds and endpoint).
var imageName = registry.loginServer.apply(s => `${s}/myapp`);
var registryInfo = {
    server: registry.loginServer,
    username: registry.adminUsername,
    password: registry.adminPassword,
};
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Get registry info (creds and endpoint).
const imageName = registry.loginServer.apply(s => `${s}/myapp`);
const registryInfo = {
    server: registry.loginServer,
    username: registry.adminUsername,
    password: registry.adminPassword,
};
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Get registry info (creds and endpoint).
image_name = registry.login_server.apply(lambda s: f'{s}/myapp')
registry_info = docker.ImageRegistry(
    server=registry.login_server,
    username=registry.admin_username,
    password=registry.admin_password
)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Get registry info (creds and endpoint).
imageName := pulumi.Sprintf("%s/myapp", registry.LoginServer)
registryInfo := docker.ImageRegistryArgs{
    Server:   registry.LoginServer,
    Username: registry.AdminUsername,
    Password: registry.AdminPassword,
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Get registry info (creds and endpoint).
var imageName = Output.Format($"{registry.LoginServer}/myapp");
var registryInfo = new ImageRegistry
{
    Server = registry.LoginServer,
    Username = registry.AdminUsername,
    Password = registry.AdminPassword,
};
```

{{< /choosable >}}

#### Alternatively, Authenticate with ActiveDirectory Service Principal

Although enabling admin access is "easy", it isn't the most secure approach. An alternative is to set "admin enabled" to `false` when declaring our registry, provision or assign an ActiveDirectory service principal with an `acrpush` role scoped to our registry, and use that for authentication instead:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// New imports:
var azuread = require("@pulumi/azuread");
var random = require("@pulumi/random");

// [As before...]

// Get registry info (creds and endpoint).
var sp = new azuread.ServicePrincipal("mysp", {
    applicationId: new azuread.Application("myspapp").applicationId,
});
var spPassword = new azuread.ServicePrincipalPassword("mysp-pass", {
    servicePrincipalId: sp.id,
    value: new random.RandomPassword("mypass", {
        length: 32,
    }, { additionalSecretOutputs: [ "result" ] }).result,
    endDateRelative: "8760h",
});
var spAuth = new azure.authorization.Assignment("myauth", {
    scope: registry.id,
    roleDefinitionName: "acrpush",
    principalId: sp.id,
});
var registryInfo = {
    server: registry.loginServer,
    username: sp.applicationId,
    password:  spAuth.id.apply(_ => spPassword.value),
};
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// New imports:
import * as azuread from "@pulumi/azuread";
import * as random from "@pulumi/random";

// [As before...]

// Get registry info (creds and endpoint).
const sp = new azuread.ServicePrincipal("mysp", {
    applicationId: new azuread.Application("myspapp").applicationId,
});
const spPassword = new azuread.ServicePrincipalPassword("mysp-pass", {
    servicePrincipalId: sp.id,
    value: new random.RandomPassword("mypass", {
        length: 32,
    }, { additionalSecretOutputs: [ "result" ] }).result,
    endDateRelative: "8760h",
});
const spAuth = new azure.authorization.Assignment("myauth", {
    scope: registry.id,
    roleDefinitionName: "acrpush",
    principalId: sp.id,
});
const registryInfo = {
    server: registry.loginServer,
    username: sp.applicationId,
    password:  spAuth.id.apply(_ => spPassword.value),
};
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# New imports:
import pulumi_azuread as azuread
import pulumi_random as random

# [As before...]

# Get registry info (creds and endpoint).
image_name = registry.login_server.apply(lambda s: f'{s}/myapp')
sp = azuread.ServicePrincipal('mysp',
    application_id=azuread.Application('myspapp').application_id,
)
sp_password = azuread.ServicePrincipalPassword('mysp-pass',
    service_principal_id=sp.id,
    value=random.RandomPassword('mypass',
        length=32,
        opts=pulumi.ResourceOptions(additional_secret_outputs=['result'])
    ).result,
    end_date_relative='8760h',
)
sp_auth = azure.authorization.Assignment('myauth',
    scope=registry.id,
    role_definition_name='acrpush',
    principal_id=sp.id,
)
registry_info = docker.ImageRegistry(
    server=registry.login_server,
    username=sp.application_id,
    password=sp_auth.id.apply(lambda _: sp_password.value),
)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// New imports:
import (
    "github.com/pulumi/pulumi-azure/sdk/v2/go/azure/authorization"
    "github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
    "github.com/pulumi/pulumi-random/sdk/v2/go/random"
)

// [As before...]

// Get registry info (creds and endpoint).
imageName := pulumi.Sprintf("%s/myapp", registry.LoginServer)
spApp, err := azuread.NewApplication(ctx, "myspapp", nil)
if err != nil {
    return err
}
sp, err := azuread.NewServicePrincipal(ctx, "mysp", &azuread.ServicePrincipalArgs{
    ApplicationId: spApp.ApplicationId,
})
if err != nil {
    return err
}
password, err := random.NewRandomPassword(ctx, "mypass",
    &random.RandomPasswordArgs{
        Length: pulumi.Int32(32),
    },
    pulumi.AdditionalSecretOutputs([]string{"result"}),
)
if err != nil {
    return err
}
spPassword, err := azuread.NewServicePrincipalPassword(ctx, "mysp-pass", &azuread.ServicePrincipalPasswordArgs{
    ServicePrincipalId: sp.ID(),
    Value:              password.Result,
    EndDateRelative:    pulumi.String("8760h"),
})
if err != nil {
    return err
}
apAuth, err := authorization.NewAssignment(ctx, "myauth", &authorization.AssignmentArgs{
    Scope:              registry.ID(),
    RoleDefinitionName: pulumi.String("acrpush"),
    PrincipalId:        sp.ID(),
})
if err != nil {
    return err
}
registryInfo := docker.ImageRegistryArgs{
    Server:   registry.LoginServer,
    Username: sp.ApplicationId,
    Password: spPassword.Value,
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// New imports:
using Pulumi.Azure.Authorization;
using AAD = Pulumi.AzureAD;
using Pulumi.Random;

// [As before...]

// Get registry info (creds and endpoint).
var imageName = Output.Format($"{registry.LoginServer}/myapp");
var sp = new AAD.ServicePrincipal("mysp", new AAD.ServicePrincipalArgs
{
    ApplicationId = new AAD.Application("myspapp").ApplicationId,
});
var spPassword = new AAD.ServicePrincipalPassword("mysp-pass", new AAD.ServicePrincipalPasswordArgs
{
    ServicePrincipalId = sp.Id,
    Value = new RandomPassword("mypass",
        new RandomPasswordArgs
        {
            Length = 32,
            },
        new CustomResourceOptions { AdditionalSecretOutputs = { "result" } }
    ).Result,
    EndDateRelative = "8760h",
});
var spAuth = new Assignment("myauth", new AssignmentArgs
{
    Scope = registry.Id,
    RoleDefinitionName = "acrpush",
    PrincipalId = sp.Id,
});
var registryInfo = new Docker.ImageRegistry
{
    Server = registry.LoginServer,
    Username = sp.ApplicationId,
    Password = spAuth.Id.Apply(_ => spPassword.Value),
};
```

{{< /choosable >}}

#### Learn More About ACR

ACR offers advanced functionality not shown here, including configuring retention policies, storage account details, and geo-replication options. For more details on these and more, see Pulumi's [Azure NextGen](https://www.pulumi.com/docs/reference/pkg/azure-nextgen/containerregistry/registry/) or [Azure](https://www.pulumi.com/docs/reference/pkg/azure/containerservice/registry/) API documentation, or [Azure's product page](https://azure.microsoft.com/en-us/services/container-registry/).

> To view another cloud provider's registry details, [select a new cloud in the switcher above](#prepare-a-container-registry).

{{% /choosable %}}

{{% choosable cloud gcp %}}

<p></p>

### Google Container Registry (GCR)

Google Container Registry (GCR) enables you to store, manage, and secure your Docker container images. It includes built-in security vulnerability scanning and fast, high-availability access by storing images in regional private repositories across the world. This makes it easy to deploy custom application images to Google Kubernetes Engine (GKE), App Engine, or Cloud Run. Each account has a default registry per project per region, backed by Google Cloud Storage (GCS), and each registry is capable of storing many images and many versions.

#### Create a New Project

To start, create a new project and [ensure it is configured to use your GCP account]({{< relref "/docs/intro/cloud-providers/gcp/setup" >}}), then scaffold your project with the imports and overall program structure that we will fill in one piece at a time:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
var gcp = require("@pulumi/gcp");
var docker = require("@pulumi/docker");

// [Placeholder 1: Create a private GCR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
import * as gcp from "@pulumi/gcp";
import * as docker from "@pulumi/docker";

// [Placeholder 1: Create a private GCR registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language python >}}

```python
import pulumi
import pulumi_gcp as gcp
import pulumi_docker as docker

# [Placeholder 1: Create a private GCR registry.]

# [Placeholder 2: Get registry info (creds and endpoint).]

# [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    "encoding/base64"
    "errors"
    "strings"

    "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
    "github.com/pulumi/pulumi-gcp/sdk/v2/go/gcp/container"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Placeholder 1: Create a private GCR registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
        return nil
    })
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Docker;
using Pulumi.Gcp.Container;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Placeholder 1: Create a private GCR registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
    }
}
```

{{< /choosable >}}

#### Ensure Your GCR Registry is Ready

Google Cloud automatically provisions a managed project-wide registry as needed. To ensure our GCP registry is ready, we allocate a registry object, and then fetch the autogenerated repository URL that we can use for images:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Create a private GCR registry.
var registry = new gcp.container.Registry("my-registry");
var registryUrl = registry.id.apply(_ =>
    gcp.container.getRegistryRepository().then(reg => reg.repositoryUrl));
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Create a private GCR registry.
const registry = new gcp.container.Registry("my-registry");
const registryUrl = registry.id.apply(_ =>
    gcp.container.getRegistryRepository().then(reg => reg.repositoryUrl));
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Create a private GCR repository.
registry = gcp.container.Registry('my-registry')
registry_url = registry.id.apply(lambda _: gcp.container.get_registry_repository().repository_url)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Create a private GCR registry.
registry, err := container.NewRegistry(ctx, "my-registry", nil)
if err != nil {
    return err
}
registryUrl := registry.ID().ApplyString(func(_ string) (string, error) {
    rep, err := container.GetRegistryRepository(ctx, nil)
    if err != nil {
        return "", err
    }
    return rep.RepositoryUrl, nil
})
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Create a private GCR registry.
var registry = new Registry("my-registry");
var registryUrl = registry.Id.Apply(async _ => {
    return (await GetRegistryRepository.InvokeAsync()).RepositoryUrl;
});
```

{{< /choosable >}}

Below we will append the container repository name to this registry URL.

#### Authenticate with the Google Cloud SDK

GCP offers [several mechanisms](https://cloud.google.com/container-registry/docs/advanced-authentication) to authenticate to your registry; however, the most secure and preferred option is to use the Google Cloud CLI, `gcloud`, as a Docker credential helper. After [setting up gcloud on your client](https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper), no explicit authentication is required in your code &mdash; instead, the ambient `gcloud` authentication settings will be used instead. As a result, we can leave the authentication information blank:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Get registry info (creds and endpoint).
var imageName = registryUrl.apply(url => `${url}/myapp`);
var registryInfo = undefined; // use gcloud for authentication.
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Get registry info (creds and endpoint).
const imageName = registryUrl.apply(url => `${url}/myapp`);
const registryInfo = undefined; // use gcloud for authentication.
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Get registry info (creds and endpoint).
image_name = registry_url.apply(lambda url: f'{url}/myapp')
registry_info = None # use gcloud for authentication.
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Get registry info (creds and endpoint).
imageName := pulumi.Sprintf("%s/myapp", registryUrl)
registryInfo := docker.ImageRegistryArgs{} // use gcloud for authentication.
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Get registry info (creds and endpoint).
var imageName = Output.Format($"{registryUrl}/myapp");
// Omit registryInfo and use gcloud for authentication.
```

{{< /choosable >}}

#### Learn More About GCR

GCR uses Google Cloud Storage to store images, which may be configured separately, including configuring IAM and lifecycle policies. For more details on this, please refer to [Pulumi's Google Cloud API](https://www.pulumi.com/docs/reference/pkg/gcp/container/registry/) or [Google's own Container Registry](https://cloud.google.com/container-registry) documentation.

> To view another cloud provider's registry details, [select a new cloud in the switcher above](#prepare-a-container-registry).

{{% /choosable %}}

{{% choosable cloud digitalocean %}}

<p></p>

### DigitalOcean Container Registry

DigitalOcean's Container Registry is an easy way to store and manage private container images for your applications for use with DigitalOcean's managed Kubernetes service.

#### Create a New Project

To start, create a new project and [ensure it is configured to use your DigitalOcean account]({{< relref "/docs/intro/cloud-providers/digitalocean/setup" >}}) and then scaffold your project with the imports and overall program structure that we will fill in one piece at a time:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
var digitalocean = require("@pulumi/digitalocean");
var docker = require("@pulumi/docker");
var pulumi = require("@pulumi/pulumi");

// [Placeholder 1: Create a private DigitalOcean container registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
import * as digitalocean from "@pulumi/digitalocean";
import * as docker from "@pulumi/docker";
import * as pulumi from "@pulumi/pulumi";

// [Placeholder 1: Create a private DigitalOcean container registry.]

// [Placeholder 2: Get registry info (creds and endpoint).]

// [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language python >}}

```python
import pulumi
import pulumi_digitalocean as digitalocean
import pulumi_docker as docker

# [Placeholder 1: Create a private DigitalOcean container registry.]

# [Placeholder 2: Get registry info (creds and endpoint).]

# [Placeholder 3: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    "encoding/base64"
    "encoding/json"
    "errors"
    "strings"
    
    "github.com/pulumi/pulumi-digitalocean/sdk/v2/go/digitalocean"
    "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Placeholder 1: Create a private DigitalOcean container registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
        return nil
    })
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.DigitalOcean;
using Pulumi.Docker;
using Newtonsoft.Json;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Placeholder 1: Create a private DigitalOcean container registry.]

        // [Placeholder 2: Get registry info (creds and endpoint).]

        // [Placeholder 3: Build and publish the container image.]
    }
}
```

{{< /choosable >}}

#### Create a DigitalOcean Container Registry

Next, declare a new DigitalOcean container registry resource:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Create a private DigitalOcean Container Registry.
var registry = new digitalocean.ContainerRegistry("my-reg", {
    subscriptionTierSlug: "starter",
});
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Create a private DigitalOcean Container Registry.
const registry = new digitalocean.ContainerRegistry("my-reg", {
    subscriptionTierSlug: "starter",
});
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Create a private DigitalOcean Container Registry.
repo = digitalocean.ContainerRegistry('my-reg',
    subscription_tier_slug='starter',
)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Create a private DigitalOcean Container Registry.
registry, err := digitalocean.NewContainerRegistry(ctx, "my-reg",
    &digitalocean.ContainerRegistryArgs{
        // SubscriptionTierSlug: pulumi.String("starter"),
    })
if err != nil {
    return err
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Create a private DigitalOcean Container Registry.
var registry = new ContainerRegistry("my-reg", new ContainerRegistryArgs
{
    SubscriptionTierSlug = "starter"
});
```

{{< /choosable >}}

#### Authenticate with Temporary Credentials

DigitalOcean supports generating temporary read or read/write credentials that Docker can use to authenticate with your new private container registry, which we'll now use. This resource returns a new credentials file similar to what the `docker login` command generates, and we can parse it and base64 decode its contents to discover the temporary username and password. Here, we gather the username and password plus the registry's URL endpoint in preparation for building and publishing the container image to the newly provisioned registry:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Get registry info (creds and endpoint) so we can build/publish to it.
var imageName = registry.endpoint.apply(s => `${s}/myapp`);
var creds = new digitalocean.ContainerRegistryDockerCredentials("my-reg-creds", {
    registryName: registry.name,
    write: true,
});
var registryInfo = pulumi.all(
    [creds.dockerCredentials, registry.serverUrl]
).apply(([authJson, serverUrl]) => {
    // We are given a Docker creds file; parse it to find the temp username/password.
    var auths = JSON.parse(authJson);
    var authToken = auths["auths"][serverUrl]["auth"];
    var decoded = Buffer.from(authToken, "base64").toString();
    var [username, password] = decoded.split(":");
    if (!password || !username) {
        throw new Error("Invalid credentials");
    }
    return {
        server: serverUrl,
        username: username,
        password: password,
    };
});
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Get registry info (creds and endpoint) so we can build/publish to it.
const imageName = registry.endpoint.apply(s => `${s}/myapp`);
const creds = new digitalocean.ContainerRegistryDockerCredentials("my-reg-creds", {
    registryName: registry.name,
    write: true,
});
const registryInfo = pulumi.all(
    [creds.dockerCredentials, registry.serverUrl]
).apply(([authJson, serverUrl]) => {
    // We are given a Docker creds file; parse it to find the temp username/password.
    const auths = JSON.parse(authJson);
    const authToken = auths["auths"][serverUrl]["auth"];
    const decoded = Buffer.from(authToken, "base64").toString();
    const [username, password] = decoded.split(":");
    if (!password || !username) {
        throw new Error("Invalid credentials");
    }
    return {
        server: serverUrl,
        username: username,
        password: password,
    };
});
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Get registry info (creds and endpoint).
image_name = registry.endpoint.apply(lambda s: f'{s}/myapp')
def getRegistryInfo(info):
    # We are given a Docker creds file; parse it to find the temp username/password.
    auth_json = info[0]
    auths = json.loads(auth_json)
    server_url = info[1]
    auth_token = auths['auths'][server_url]['auth']
    decoded = base64.b64decode(auth_token).decode()
    parts = decoded.split(':')
    if len(parts) != 2:
        raise Exception('Invalid credentials')
    return docker.ImageRegistry(server_url, parts[0], parts[1])
creds = digitalocean.ContainerRegistryDockerCredentials('reg-creds',
    registry_name=registry.name,
    write=True,
)
registry_info = pulumi.Output.all(
    creds.docker_credentials, registry.server_url).apply(getRegistryInfo)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Get registry info (creds and endpoint).
imageName := pulumi.Sprintf("%s/myapp", registry.Endpoint)
creds, err := digitalocean.NewContainerRegistryDockerCredentials(ctx, "my-reg-creds",
    &digitalocean.ContainerRegistryDockerCredentialsArgs{
        RegistryName: registry.Name,
        Write:        pulumi.Bool(true),
    },
)
if err != nil {
    return err
}

registryInfo := pulumi.All(creds.DockerCredentials, registry.ServerUrl).ApplyT(
    func(args []interface{}) (docker.ImageRegistry, error) {
        // We are given a Docker creds file; parse it to find the temp username/password.
        authJson := args[0].(string)
        serverUrl := args[1].(string)
        var auths map[string]interface{}
        if err := json.Unmarshal([]byte(authJson), &auths); err != nil {
            return docker.ImageRegistry{}, err
        }
        authMap := auths["auths"].(map[string]interface{})
        authToken := authMap[serverUrl].(map[string]interface{})["auth"].(string)
        decoded, err := base64.StdEncoding.DecodeString(authToken)
        if err != nil {
            return docker.ImageRegistry{}, err
        }
        parts := strings.Split(string(decoded), ":")
        if len(parts) != 2 {
            return docker.ImageRegistry{}, errors.New("Invalid credentials")
        }
        return docker.ImageRegistry{
            Server:   serverUrl,
            Username: parts[0],
            Password: parts[1],
        }, nil
    },
).(docker.ImageRegistryOutput)
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Get registry info (creds and endpoint).
var imageName = Output.Format($"{registry.Endpoint}/myapp");
var registryCreds = new ContainerRegistryDockerCredentials("my-reg-creds",
    new ContainerRegistryDockerCredentialsArgs
    {
        RegistryName = registry.Name,
        Write = true,
    });
var registryInfo = Output.All(
    registryCreds.DockerCredentials, registry.ServerUrl).
    Apply(args =>
    {
        var authJson = args[0];
        var serverUrl = args[1];
        dynamic auths = JsonConvert.DeserializeObject(authJson);
        var authToken = auths["auths"][serverUrl]["auth"];
        var decoded = ASCIIEncoding.ASCII.GetString(authToken);

        var parts = decoded.Split(':');
        if (parts.Length != 2)
        {
            throw new Exception("Invalid credentials");
        }

        return new ImageRegistry
        {
            Server = serverUrl,
            Username = parts[0],
            Password = parts[1],
        };
    });
```

{{< /choosable >}}

#### Learn More About DigitalOcean Container Registry

Each DigitalOcean account may have just a single registry, so you are likely to want to provision that in a separate stack for most "real world" examples. Also, this project uses the lowest subscription tier, `"starter"`, which is inexpensive but quite limited (you may only store a single repository of images). If you would like to use an advanced tier or configure any other options, please refer to [Pulumi's DigitalOcean API](https://www.pulumi.com/docs/reference/pkg/digitalocean/containerregistry/) or [DigitalOcean's product](https://www.digitalocean.com/products/container-registry/) documentation.

> To view another cloud provider's registry details, [select a new cloud in the switcher above](#prepare-a-container-registry).

{{% /choosable %}}

{{% choosable cloud docker %}}

<p></p>

### Docker Hub

Docker offers the Docker Hub as an easy way to store and consume public or private container images from a centralized location to any cloud. To start building and publishing to Docker Hub with infrastructure as code, create a new project and scaffold it with the imports and overall program structure that we will fill in one piece at a time:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
var docker = require("@pulumi/docker");
var pulumi = require("@pulumi/pulumi");

// [Placeholder 1: Get registry info (creds and endpoint).]

// [Placeholder 2: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
import * as docker from "@pulumi/docker";
import * as pulumi from "@pulumi/pulumi";

// [Placeholder 1: Get registry info (creds and endpoint).]

// [Placeholder 2: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language python >}}

```python
import pulumi
import pulumi_docker as docker

# [Placeholder 1: Get registry info (creds and endpoint).]

# [Placeholder 2: Build and publish the container image.]
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    "encoding/base64"
    "encoding/json"
    "errors"
    "strings"
    
    "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Placeholder 1: Get registry info (creds and endpoint).]

        // [Placeholder 2: Build and publish the container image.]
        return nil
    })
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Docker;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Placeholder 1: Get registry info (creds and endpoint).]

        // [Placeholder 2: Build and publish the container image.]
    }
}
```

{{< /choosable >}}

For purposes of this example, you will need to manually provision a repository, and select whether to make it public or private, via the Docker Hub's UI. Refer to the [Docker Hub documentation](https://docs.docker.com/docker-hub/repos/) for details on how to do this. Once you have an account and have set up your registry, [create an access token](https://docs.docker.com/docker-hub/access-tokens/). We will now use your username and this access token to configure authentication so that you can build and publish to your registry.

Because the repository was provisioned outside of the purview of Pulumi, we can jump straight to authenticating. To do this, we will simply use the Pulumi configuration system to store and retrieve  authentication information, using the token created above:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// Fetch the Docker Hub auth info from config.
var config = new pulumi.Config();
var username = config.require("dockerUsername");
var password = config.requireSecret("dockerPassword");

// Populate the registry info (creds and endpoint).
var imageName = `${username}/myapp`;
var registryInfo = {
    server: "docker.io",
    username: username,
    password: password,
};
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// Fetch the Docker Hub auth info from config.
const config = new pulumi.Config();
const username = config.require("dockerUsername");
const password = config.requireSecret("dockerPassword");

// Populate the registry info (creds and endpoint).
const imageName = `${username}/myapp`;
const registryInfo = {
    server: "docker.io",
    username: username,
    password: password,
};
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# Fetch the Docker Hub auth info from config.
config = pulumi.Config()
username = config.require('dockerUsername')
accessToken = config.require_secret('dockerAccessToken')

# Populate the registry info (creds and endpoint).
image_name=f'{username}/myapp',
def get_registry_info(token):
    return docker.ImageRegistry(
        server='docker.io',
        username=username,
        password=token,
    )
registry_info=accessToken.apply(get_registry_info)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// Fetch the Docker Hub auth info from config.
username := config.Require(ctx, "dockerUsername")
password := config.RequireSecret(ctx, "dockerPassword")

// Populate the registry info (creds and endpoint).
imageName := pulumi.String(username + "/myapp")
registryInfo := docker.ImageRegistryArgs{
    Server:   pulumi.String("docker.io"),
    Username: pulumi.String(username),
    Password: password.(pulumi.StringOutput),
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// Fetch the Docker Hub auth info from config.
var config = new Pulumi.Config();
var username = config.Require("dockerUsername");
var password = config.RequireSecret("dockerPassword");

// Populate the registry info (creds and endpoint).
var imageName = $"{username}/myapp";
var registryInfo = new ImageRegistry
{
    Server = "docker.io",
    Username = username,
    Password = password,
};
```

{{< /choosable >}}

After writing this code, add your Docker username and password to your Pulumi project:

```bash
$ pulumi config set dockerUsername [YOUR USERNAME]
$ pulumi config set --secret dockerAccessToken [YOUR TOKEN]
```

There are of course other ways to configure this authentication information, however, the Pulumi secrets system ensures that your token is encrypted and safe to use.

> To view another cloud provider's registry details, [select a new cloud in the switcher above](#prepare-a-container-registry).

{{% /choosable %}}

At this stage, we can run `pulumi up` to check that the program works and to provision any necessary cloud resources.

## Build and Publish Your Container

Now we are ready to build and publish your container image to the chosen registry. [The Docker provider's `Image` component]({{< relref "/docs/reference/pkg/docker" >}}) internally uses the Docker engine to perform the necessary steps to carry this out, including building, tagging, capturing, and streaming container build logs as progress is made and pushing the final result.

Simply pass the path to your application's `Dockerfile` as the build context, the registry's URL as the image's name, and the registry configuration object built up earlier to facilitate authentication:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// [Existing imports ...]
var docker = require("@pulumi/docker");

// [Registry configuration as shown above ...]

// Build and publish the container image.
var image = new docker.Image("my-image", {
    build: "app",
    imageName: imageName,
    registry: registry,
});

// Export the base and specific version image name.
module.exports = {
    baseImageName: image.baseImageName,
    fullImageName: image.imageName,
};
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// [Existing imports ...]
import * as docker from "@pulumi/docker";

// [Registry configuration as shown above ...]

// Build and publish the container image.
const image = new docker.Image("my-image", {
    build: "app",
    imageName,
    registry,
});

// Export the base and specific version image name.
export const baseImageName = image.baseImageName;
export const fullImageName = image.imageName;
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# [Existing imports ...]
import pulumi_docker as docker

# [Registry configuration as shown above ...]

# Build and publish the container image.
image = docker.Image('my-image',
    build='app',
    image_name=image_name,
    registry=registry_info,
)

# Export the base and specific version image name.
pulumi.export('baseImageName', image.base_image_name)
pulumi.export('fullImageName', image.image_name)
```

{{< /choosable >}}

{{< choosable language go >}}

```go
// [Existing imports ...]

import "github.com/pulumi/pulumi-docker/sdk/v2/go/docker"

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Registry configuration as shown above ...]

        // Build and publish the container image.
        image, err := docker.NewImage(ctx, "my-image", &docker.ImageArgs{
            Build:     &docker.DockerBuildArgs{Context: pulumi.String("app")},
            ImageName: imageName,
            Registry:  registryInfo,
        })

        // Export the base and specific version image name.
        ctx.Export("baseImageName", image.BaseImageName)
        ctx.Export("fullImageName", image.ImageName)
        return nil
    })
}
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// [Existing imports ...]

using Pulumi.Docker;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Registry configuration as shown above ...]

        // Build and publish the container image.
        var image = new Image("my-image", new ImageArgs
        {
            Build = new DockerBuild { Context = "app" },
            ImageName = imageName,
            Registry = registryInfo,
        });

        // Export the base and specific version image name.
        return new Dictionary<string, object>
        {
            { "baseImageName", image.BaseImageName },
            { "fullImageName", image.ImageName },
        };
    });
}
```

{{< /choosable >}}

Now let's run `pulumi up`. If you haven't already done so, this will provision the cloud resources, as well as build/publish the container image. As the build runs, you will see Docker build output streamed to your terminal:

```bash
$ pulumi up
Updating (dev)

     Type                   Name            Status
 +   pulumi:pulumi:Stack    project-dev     created
 ... cloud-specific resources omitted ...
 +   └─ docker:image:Image  my-image        created

Outputs:
    baseImageName: "...cloud-specific url.../my-repo-dc811b0"
    fullImageName: "...cloud-specific url.../my-repo-dc811b0:78d0fce7c2450c15a6153b6b11208fcb6b9edea7bb7ef3b7b6194f3fc101a170"
```

Also note the base and versioned image URLs are exported as stack outputs. These are optional but have three benefits:

1. As we see here, the CLI will print them after each deployment.
2. The CLI can fetch them on-demand, e.g., 'pulumi stack output fullImageName', making it easy to script access to these container images.
3. The [Pulumi `StackReference` component]({{< relref "/docs/intro/concepts/stack#stackreferences" >}}) can be used to depend on this stack from another, allowing us to build higher levels of infrastructure that consume these images.

As an example of (2) in action, let's run the image locally using the exported image name:

```bash
$ pulumi stack output fullImageName
...cloud-specific url.../my-repo-dc811b0:78d0fce7c2450c15a6153b6b11208fcb6b9edea7bb7ef3b7b6194f3fc101a170
```

> Note that this requires that our client can pull from our provisioned registry, which may require cloud-specific authentication first.

To redeploy changes to the `Dockerfile` or anything that image depends on, including application code, rerun `pulumi up`. It will detect the differences, rebuild and re-push the minimal layer changes necessary to update and retag the repository image, and then export the resulting image name.

To see this in action, change the `Dockerfile`'s contents to:

```dockerfile
FROM nginx
RUN echo "<h1>Hello, World -- from Pulumi!</h1>" > \
    /usr/share/nginx/html/index.html
```

And then rerun Pulumi -- notice how it detects the change, updates the image, and the versioned image hash changes (indicated by the tilde `~`):

```bash
$ pulumi up
Updating (dev)

     Type                   Name            Status
 +   pulumi:pulumi:Stack    project-dev     created
 ~   └─ docker:image:Image  my-image        updated

Outputs:
    baseImageName: "...cloud-specific url.../my-repo-dc811b0"
  ~ fullImageName: "...cloud-specific url.../my-repo-dc811b0:78d0fce7c2450c15a6153b6b11208fcb6b9edea7bb7ef3b7b6194f3fc101a170"
```

The Pulumi Docker `Image` component supports a number of additional options to control its behavior, including passing build arguments, environment variables, extra options for the Docker build, as well as various controls for image caching. For full details on each of these, refer to [the API documentation]({{< relref "/docs/reference/pkg/docker/image" >}}).

## Consume the Container Image

The same container image URLs exported above can be used as inputs to other resources, including infrastructure that will run your container inside of a container orchestration system such as Kubernetes, Amazon ECS, and so on.

> This article assumes you already have a containerized environment to deploy to, like a Kubernetes cluster, and have [configured your project accordingly]({{< relref "/docs/intro/cloud-providers/kubernetes/setup" >}}). If not, you can provision one using Pulumi first. Pulumi supports many clouds and infrastructure resources, but here are a few starting points to get up and running with: 

- [AWS Elastic Container Service ECS]({{< relref "/docs/guides/crosswalk/aws/ecs" >}}), 
- [AWS Elastic Kubernetes Service (EKS)]({{< relref "/docs/guides/crosswalk/aws/eks" >}}), 
- [Azure Kubernetes Service (AKS)]({{< relref "/docs/tutorials/kubernetes/aks" >}}), 
- [Google Cloud Kubernetes Engine (GKE)]({{< relref "/docs/tutorials/kubernetes/gke" >}}), 
- [DigitalOcean Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-manage-digitalocean-and-kubernetes-infrastructure-with-pulumi).

This example demonstrates deploying our Nginx web server as a load balanced service within Kubernetes. To do so, we'll declare our Kubernetes configuration, right inside of our existing program defined above, and export its resulting IP address:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{< choosable language javascript >}}

```javascript
// [Previous imports...]
var k8s = require("@pulumi/kubernetes");

// [Registry, build, etc., code from above...]

// Create a load balanced Kubernetes service using this image, and export its IP.
var appLabels = { app: "myapp" };
var appDep = new k8s.apps.v1.Deployment("app-dep", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 3,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: "myapp",
                    image: image.imageName,
                }],
            },
        },
    },
});
var appSvc = new k8s.core.v1.Service("app-svc", {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
        selector: appLabels,
    },
});

module.exports = {
    // [Previous exports...]
    appIp: appSvc.status.loadbalancer.ingress[0].ip,
};
```

{{< /choosable >}}

{{< choosable language typescript >}}

```typescript
// [Previous imports...]
import * as k8s from "@pulumi/kubernetes";

// [Registry, build, etc, code from above...]

// Create a load balanced Kubernetes service using this image, and export its IP.
const appLabels = { app: "myapp" };
const appDep = new k8s.apps.v1.Deployment("app-dep", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 3,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: "myapp",
                    image: image.imageName,
                }],
            },
        },
    },
});
const appSvc = new k8s.core.v1.Service("app-svc", {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
        selector: appLabels,
    },
});
export const appIp = appSvc.status.loadBalancer.ingress[0].ip;
```

{{< /choosable >}}

{{< choosable language python >}}

```python
# [Previous imports...]
import pulumi_kubernetes as k8s

# [Registry, build, etc, code from above...]

# Create a load balanced Kubernetes service using this image, and export its IP.
app_labels = { 'app': 'myapp' }
app_dep = k8s.apps.v1.Deployment('app-dep',
    spec={
        'selector': { 'matchLabels': app_labels },
        'replicas': 3,
        'template': {
            'metadata': { 'labels': app_labels },
            'spec': {
                'containers': [{
                    'name': 'myapp',
                    'image': image.image_name,
                }],
            },
        },
    },
)
app_svc = k8s.core.v1.Service('app-svc',
    metadata={ 'labels': app_labels },
    spec={
        'type': 'LoadBalancer',
        'ports': [{ 'port': 80, 'targetPort': 80, 'protocol': 'TCP' }],
        'selector': app_labels,
    }
)
pulumi.export('appIp', app_svc.status.apply(lambda s: s.loadbalancer.ingress[0].ip))
```

{{< /choosable >}}

{{< choosable language go >}}

```go
package main

import (
    // [Previous imports...]
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // [Registry, build, etc, code from above...]

        // Create a load balanced Kubernetes service using this image, and export its IP.
        appLabels := pulumi.StringMap{"app": pulumi.String("myapp")}
        _, deperr := appsv1.NewDeployment(ctx, "app-dep", &appsv1.DeploymentArgs{
            Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
            Spec: appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{MatchLabels: appLabels},
                Replicas: pulumi.Int(3),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            corev1.ContainerArgs{
                                Name:  pulumi.String("myapp"),
                                Image: image.ImageName,
                            },
                        },
                    },
                },
            },
        })
        if deperr != nil {
            return deperr
        }
        appSvc, svcerr := corev1.NewService(ctx, "app-svc", &corev1.ServiceArgs{
            Metadata: &metav1.ObjectMetaArgs{Labels: appLabels},
            Spec: &corev1.ServiceSpecArgs{
                Type: pulumi.String("LoadBalancer"),
                Ports: corev1.ServicePortArray{
                    corev1.ServicePortArgs{Port: pulumi.Int(80)},
                },
                Selector: appLabels,
            },
        })
        if svcerr != nil {
            return svcerr
        }
        ctx.Export("appIp", appSvc.Status.ApplyT(func(status *corev1.ServiceStatus) *string {
            return status.LoadBalancer.Ingress[0].Ip
        }))
        
        return nil
    })
}        
```

{{< /choosable >}}

{{< choosable language csharp >}}

```csharp
// [Previous imports...]
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(async () => {
        // [Registry, build, etc, code from above...]

        // Create a load balanced Kubernetes service using this image, and export its IP.
        var appLabels = new InputMap<string>
        {
            { "app", "myapp" }
        };
        var appDep = new Pulumi.Kubernetes.Apps.V1.Deployment("app-dep", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = appLabels
                },
                Replicas = 3,
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = appLabels,
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new Pulumi.Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                            {
                                Name = "myapp",
                                Image = image.ImageName,
                            }
                        }
                    }
                }
            }
        });
        var appSvc = new Pulumi.Kubernetes.Core.V1.Service("app-svc", new Pulumi.Kubernetes.Types.Inputs.Core.V1.ServiceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Labels = appLabels
            },
            Spec = new ServiceSpecArgs
            {
                Type = "LoadBalancer",
                Ports =
                {
                    new ServicePortArgs
                    {
                        Port = 80,
                        TargetPort = 80
                    }
                },
                Selector = appLabels
            }
        });

        return new Dictionary<string, object>
        {
            // [Previous exports...]
            { "appIp", appSvc.Status.Apply(status => status.LoadBalancer.Ingress[0].Ip) },
        };
    }
}
```

{{< /choosable >}}

Notice here that we are referring to the resulting image name from our service specification. All we need to do run a 'pulumi up' and Pulumi will now build, publish, and consume our application's container image from within our Kubernetes cluster:

```bash
$ pulumi up
Updating (dev)

     Type                              Name            Status
 +   pulumi:pulumi:Stack               project-dev     created
 ... prior output omitted ...
 +   ├─ kubernetes:apps/v1:Deployment  app-dep         created
 +   └─ kubernetes:core/v1:Service     app-svc         created

Outputs:
    appIp        : "34.82.32.166"
    baseImageName: "...cloud-specific url.../my-repo-dc811b0"
    fullImageName: "...cloud-specific url.../my-repo-dc811b0:fcbbd958636e4f8ac02568db7dbf8b89a043e210e917432cf12649aaedfa266c"
```

If this is the first time you've run `pulumi up`, all of the prior resources will be provisioned first, and in any case, the Kubernetes resources will follow.

Now that our deployment has completed, we can curl the endpoint:

```bash
$ curl $(pulumi stack output appIp)
<h1>Hello, World -- from Pulumi!</h1>
```

This image name is the versioned one, meaning that any time a new version is created, Pulumi will detect that it needs to update the Kubernetes deployment which references it, triggering a rollout of the new deployed image. As such, we just need to run `pulumi up` anytime the application or its `Dockerfile` changes and Pulumi will detect and trigger a deployment to Kubernetes.

To see this in action, let's change our `Dockerfile`'s contents once more:

```dockerfile
FROM nginx
RUN echo "<h1>Hello, World -- from Pulumi and Kubernetes!</h1>" > \
    /usr/share/nginx/html/index.html
```

And then rerun Pulumi -- notice that both the image _and_ the Kubernetes deployment has changed this time:

```bash
$ pulumi up
Updating (dev)

     Type                              Name            Status      Info
 +   pulumi:pulumi:Stack               project-dev     created
 ~   ├─ docker:image:Image             my-image        updated
 ~   └─ kubernetes:core/v1:Deployment  app-dep         updated     [diff: ~spec]

Outputs:
    appIp        : "34.82.32.166"
    baseImageName: "...cloud-specific url.../my-repo-dc811b0"
    fullImageName: "...cloud-specific url.../my-repo-dc811b0:36919b56f6b2dedfa879815443c9964d17a89506caed25025328b1d0204a083f"
```

Finally, if we re-curl the endpoint, we will now see that the updated container is now live!

```
$ curl $(pulumi stack output appIp)
<h1>Hello, World -- from Pulumi and Kubernetes!</h1>
```

And there we go: we have gone from a `Dockerfile` to a published container image in a container registry of our choosing, which has been used to spin up a load balanced Kubernetes service, and which is now ready for fully automated continuous deployments.

## Wrapping Up

In this article, we've seen how easy it is to build, publish, and use container images in many popular public and private container registry options. We have seen how to provision new registries using infrastructure as code and how easy it is to trigger deployments of application updates by running a single `pulumi up` command.

All of these steps were manually run from a CLI; however, a natural next step is to [wire the entire process up to a CI/CD system]({{< relref "/docs/guides/continuous-delivery" >}}) such as [GitHub Actions]({{< relref "/docs/guides/continuous-delivery/github-actions" >}}), [GitLab Pipelines]({{< relref "/docs/guides/continuous-delivery/gitlab-ci" >}}), [Jenkins]({{< relref "/docs/guides/continuous-delivery/jenkins" >}}), [Spinnaker]({{< relref "/docs/guides/continuous-delivery/spinnaker" >}}), or [one of the many available options]({{< relref "/docs/guides/continuous-delivery" >}}, so that you can deploy continuously as you merge code. For even more advanced scenarios, we might want to build a custom program such as a CLI that uses the [Automation API]({{< relref "/blog/automation-api" >}}) to perform these actions behind a simpler, purpose-built interface.

Although we've shown a very simple set of infrastructure resources, it would be natural to extend these examples by provisioning other ancillary services that your application needs, including databases, pub/sub topics, queues, metrics and dashboards, and more. Using an infrastructure as code approach to building, publishing, and consuming your container images means you can incrementally add on such infrastructure to the base code shown above and reference them from your containers easily with automatic dependency tracking.

The complete examples in this article are [available on GitHub here](https://github.com/pulumi/pulumi-docker/tree/master/examples/container-registries). Pulumi is open source and free to get started with &mdash; [give it a try, and get up and running with infrastructure as code for your containers today]({{< relref "/docs/get-started" >}})!
