---
title: "Functions Now Accept Outputs"
date: 2021-11-12T13:14:58-05:00
draft: false
meta_desc: With Pulumi 3.17.1 you can now call functions directly with resource outputs without an extra apply.
meta_image: meta.png
authors:
    - anton-tayanovskyy
tags:
    - features
---

Pulumi 3.17.1 makes it easier to compose function calls and resources.
In practice you often need to call a function with a resource output.
Previous versions of Pulumi required an `apply` to do this, which
was unfortunate:

- new Pulumi users would get stuck and ask for help as the solution
  was not obvious

- experienced users found the code unpleasant, upvoting the relevant
  [GitHub Issue](https://github.com/pulumi/pulumi/issues/5758)

With Pulumi 3.17.1 you can now call functions directly with resource
outputs without an extra `apply`. Every function now has an additional
Output form that accepts `Input`-typed arguments and returns an
`Output`-wrapped result.

For a quick example, here is how you can call
[aws.ecr.getCredentials](https://www.pulumi.com/registry/packages/aws/api-docs/ecr/getcredentials/)
with a `registryId` of type `Output<string>`:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
const registryId: Output<string> = ...
getCredentialsOutput({registryId: registryId}): Output<GetCredentialsResult>
```

{{% /choosable %}}
{{% choosable language python %}}

```python
registry_id: Output[str] = ...
get_credentials_output(registry_id=registryId): Output[GetCredentialsResult]
```

{{% /choosable %}}
{{% choosable language go %}}

```go
var registryId StringOutput
var result GetCredentialsResultOutput
result = GetCredentialsOutput(ctx, GetCredentialsOutputArgs{
    RegistryId: result
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Output<string> registryId;
GetCredentials.Invoke(new GetCredentialsInvokeArgs
{
   RegistryId = registryId
});
```

{{% /choosable %}}

<!--more-->

## Complete Example: Publish Docker Image to ECR

Why would you call `aws.ecr.getCredentials` with an `Output`? Suppose
you want to provision an AWS Elastic Container Registry (ECR)
repository, build a Docker image locally and publish this image to the
registry.

- To configure the Docker Image resource, you need ECR credentials.

- To acquire the credentials, you need to call the
  `aws.ecr.getCredentials` function with the ECR registry ID.

- Because the ECR registry ID is only known once the actual repository
  is provisioned in the cloud, the registryId property of the
  ecr.Repository resource has the type `Output<string>` rather than
  string (see [Inputs and Outputs](https://www.pulumi.com/docs/intro/concepts/inputs-outputs/)).

In the code below, note how `getCredentialsOutput` now accepts
`appRepo.registryId` directly:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as docker from "@pulumi/docker";

function parseAuthToken(authToken: string): {username: string, password: string} {
    const parts = Buffer.from(authToken, "base64").toString("ascii").split(":");
    console.log(parts);
    return {
        username: parts[0],
        password: parts[1]
    }
}

const appRepo = new aws.ecr.Repository("app-repo");

const creds = aws.ecr.getCredentialsOutput({registryId: appRepo.registryId})
    .apply(creds => parseAuthToken(creds.authorizationToken))

const image = new docker.Image("app-img", {
    // ./my-app is a folder with a Dockerfile
    build: "./my-app",
    imageName: appRepo.repositoryUrl,
    registry: {
        server: appRepo.repositoryUrl,
        username: creds.username,
        password: creds.password
    }
});

export const imageUrn = image.urn;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from collections import namedtuple
import base64
from pulumi_aws import s3, ecr
import pulumi_docker as docker

Creds = namedtuple('Creds', 'username password')

def parse_auth_token(token):
    (u, p) = base64.b64decode(token).decode().split(':')
    return Creds(username=u, password=p)

repo = ecr.Repository('app-repo')

creds = ecr.get_credentials_output(registry_id=repo.registry_id).apply(
    lambda creds: parse_auth_token(creds.authorization_token))

image = docker.Image(
    'app-img',
    image_name=repo.repository_url,
    # ./my-app is a folder with a Dockerfile
    build=docker.DockerBuild(context='./my-app'),
    registry=docker.ImageRegistry(
        repo.repository_url,
        creds.username,
        creds.password))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/base64"
	"fmt"
	"strings"

	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ecr"
	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type creds struct {
	Username string
	Password string
}

func parseAuthToken(token string) (creds, error) {
	decoded, err := base64.StdEncoding.DecodeString(token)
	if err != nil {
		return creds{}, err
	}
	parts := strings.Split(string(decoded), ":")
	if len(parts) != 2 {
		return creds{}, fmt.Errorf("Failed to parse token")
	}
	return creds{parts[0], parts[1]}, nil
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		repo, err := ecr.NewRepository(ctx, "app-repo", &ecr.RepositoryArgs{})
		if err != nil {
			return err
		}

		creds := ecr.GetCredentialsOutput(ctx, ecr.GetCredentialsOutputArgs{
			RegistryId: repo.RegistryId,
		})

		username := creds.AuthorizationToken().
			ApplyT(func(token string) (string, error) {
				creds, err := parseAuthToken(token)
				return creds.Username, err
			}).(pulumi.StringOutput)

		password := creds.AuthorizationToken().
			ApplyT(func(token string) (string, error) {
				creds, err := parseAuthToken(token)
				return creds.Password, err
			}).(pulumi.StringOutput)

		image, err := docker.NewImage(ctx, "app-img", &docker.ImageArgs{
			Build: &docker.DockerBuildArgs{
				Context: pulumi.String("./my-app"),
			},
			ImageName: repo.RepositoryUrl,
			Registry: &docker.ImageRegistryArgs{
				Server:   repo.RepositoryUrl,
				Username: username,
				Password: password,
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("imageName", image.ImageName)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class MyStack : Pulumi.Stack
{
    public MyStack()
    {
        var repo = new Repository("app-repo");

        var creds = GetCredentials.Invoke(new GetCredentialsInvokeArgs
        {
            RegistryId = repo.RegistryId
        });

        var username = creds
            .Apply(c => ParseAuthToken(c.AuthorizationToken).Username);

        var password = creds
            .Apply(c => ParseAuthToken(c.AuthorizationToken).Password);

        var image = new Image("app-img", new ImageArgs
        {
            ImageName = repo.RepositoryUrl,
            Build = new DockerBuild
            {
                // ./my-app is a folder with a Dockerfile
                Context = "./my-app"
            },
            Registry = new ImageRegistry
            {
                Server = repo.RepositoryUrl,
                Username = username,
                Password = password,
            }
        });
    }

    public (string Username, string Password) ParseAuthToken(string token)
    {
        var parts = Encoding.UTF8.GetString(
            Convert.FromBase64String(token)).Split(":");
        return (Username: parts[0], Password: parts[1]);
    }
}
```

{{% /choosable %}}

Prior to the ability to call `aws.ecr.getCredentials` directly with an
`Output` this program required an `apply` form and was a lot more
verbose and harder to read:

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
const creds = appRepo.id
    .apply(id => aws.ecr.getCredentials({registryId: id})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
creds = app_repo.id.apply(lambda repo_id: ecr.get_credentials(registry_id=repo_id))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
creds := repo.ID().ToStringOutput().
	ApplyT(func(id string) *ecr.GetCredentialsResult {
		creds, err := ecr.GetCredentials(ctx,
			&ecr.GetCredentialsArgs{RegistryId: id})
		if err != nil {
			panic(err)
		}
		return creds
	}).(ecr.GetCredentialsResultOutput)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var creds = repo.Id.Apply(repoId =>
                          GetCredentials.InvokeAsync(new GetCredentialsArgs
                          {
                              RegistryId = repoId
                          }));
```

{{% /choosable %}}

## More examples

The above example is one of many practical situations where mixing
function calls and resources benefits from the new form. To find out
more, check out the following updated Pulumi examples:

- [azure-py-appservice example](https://github.com/pulumi/examples/tree/master/azure-py-appservice)
- [aws-ts-appsync example](https://github.com/pulumi/examples/tree/master/aws-ts-appsync)
- [azure-cs-aks-cosmos-helm](https://github.com/pulumi/examples/tree/master/azure-cs-aks-cosmos-helm)

## Compatibility

To keep existing Pulumi programs working without changes, the function
forms are added as separate functions or methods in each
Pulumi-supported language following a simple naming convention. To
illustrate with the `getCredentials` function:

| Language   | Existing non-Output form   | New Output form                      |
|------------|----------------------------|--------------------------------------|
| TypeScript | aws.ecr.getCredentials     | aws.ecr.getCredentials**Output**     |
| Python     | aws.ecr.get\_credentials   | aws.ecr.get\_credentials\_**output** |
| Go         | ecr.getCredentials         | ecr.getCredentials**Output**         |
| C#         | GetCredentials.InvokeAsync | GetCredentials.**Invoke**            |

Note that there are cases where the existing non-`Output` form may
still be the right choice. For example, retrieving the default VPC in
Python utilizing the existing form is simpler as it returns a result
that can be immediately inspected:

```python
default_vpc = aws.ec2.get_vpc(default=True)
print(default_vpc.id)
```

Prefer the new Output form when passing resource outputs to a function
or else using the outputs of the function as inputs to resources. You
may still want to use the existing non-Output form if you are using
the outputs of the function to inform control flow (`if` conditionals
or `for` loops).

## Get started

To use Output-versioned functions, please upgrade your install of
Pulumi to at least 3.17.1 and upgrade your providers to the latest
available version. Example compatible versions for major Pulumi
providers:

| Provider             | Version |
|----------------------|---------|
| pulumi-aws           | 4.27.0  |
| pulumi-azure-native  | 1.45.0  |
| pulumi-google-native | 0.8.0   |
| pulumi-azure         | 4.26.0  |
| pulumi-gcp           | 5.26.0  |
