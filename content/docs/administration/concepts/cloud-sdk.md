---
title: Cloud SDK
title_tag: Pulumi Cloud SDK
h1: Pulumi Cloud SDK
meta_desc: Learn what the Pulumi Cloud SDK is, when to use it, and how to call the Pulumi Cloud REST API from TypeScript, Python, Go, .NET, and Java.
menu:
  administration:
    name: Cloud SDK
    parent: administration-concepts
    weight: 12
---

The Pulumi Cloud SDK is a set of client libraries for the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/). It's available for TypeScript, Python, Go, .NET, and Java, and it's generated from the same API specification that the REST API reference is built from, so every operation in the API is available as a typed method: stacks, deployments, environments, organizations, teams, access tokens, Neo tasks, and more.

## When to use the SDK

Use the Cloud SDK when you want to call Pulumi Cloud from your own code. For example:

- **Scripts and automation** that query or change Pulumi Cloud, such as auditing stack tags across an organization, rotating access tokens, or triggering deployments.
- **Internal tools and services** that show Pulumi Cloud data, such as a dashboard of stack updates or a service that opens Neo tasks.

The SDK handles request construction, serialization, and error responses, so you work with typed request and response objects instead of raw HTTP. In every language except Go, it also sets the authentication header from the token you configure.

## When not to use the SDK

Other tools fit some jobs better:

- **To manage Pulumi Cloud resources declaratively**, such as teams, access tokens, webhooks, or deployment settings, use the [Pulumi Cloud provider](/registry/packages/pulumiservice/) in a Pulumi program. The provider tracks those resources in state and reconciles them like any other infrastructure.
- **For one-off calls from a terminal**, use [`pulumi api`](/docs/iac/cli/api/), which calls any REST API endpoint with your existing CLI credentials.
- **To read configuration and secrets from ESC environments** at runtime, use the [Pulumi ESC SDK](/docs/esc/concepts/sdks/), which is built for opening environments and reading their resolved values.
- **To run Pulumi programs from code**, use the [Automation API](/docs/iac/concepts/automation-api/).

## Authentication

The SDK authenticates with a Pulumi [access token](/docs/administration/concepts/access-tokens/), sent with each request in the `Authorization` header. Use a personal access token for scripts that act as you, and an organization or team access token (a machine token, not tied to a user account) for automation that shouldn't depend on an individual's account. The examples on this page read the token from the `PULUMI_ACCESS_TOKEN` environment variable.

By default, the SDK calls `https://api.pulumi.com`. If you [self-host Pulumi Cloud](/docs/administration/self-hosting/), point the client at your own API endpoint instead.

## Install the SDK

{{< chooser language "typescript,python,go,csharp,java" />}}

{{% choosable language typescript %}}

```bash
npm install @pulumi/cloud-sdk
```

The TypeScript SDK requires Node.js 22 or later.

{{% /choosable %}}

{{% choosable language python %}}

```bash
pip install pulumi_cloud_sdk
```

The Python SDK requires Python 3.10 or later.

{{% /choosable %}}

{{% choosable language go %}}

```bash
go get github.com/pulumi/pulumi-cloud-sdk/go/apiclient
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
dotnet add package Pulumi.Cloud.Sdk
```

{{% /choosable %}}

{{% choosable language java %}}

Add the `com.pulumi:pulumi-cloud-sdk` artifact to your build, replacing `<version>` with the [latest release](https://central.sonatype.com/artifact/com.pulumi/pulumi-cloud-sdk). For Gradle:

```groovy
implementation 'com.pulumi:pulumi-cloud-sdk:<version>'
```

For Maven:

```xml
<dependency>
    <groupId>com.pulumi</groupId>
    <artifactId>pulumi-cloud-sdk</artifactId>
    <version><!-- version --></version>
</dependency>
```

{{% /choosable %}}

## Make your first call

This example creates a client and gets the current user, which is the identity that the access token belongs to.

{{< chooser language "typescript,python,go,csharp,java" />}}

{{% choosable language typescript %}}

```typescript
import { ApiClient, ApiClientConfiguration, ApiService } from "@pulumi/cloud-sdk";

const config = new ApiClientConfiguration(
    "https://api.pulumi.com/api/",
    "my-app",
    () => process.env.PULUMI_ACCESS_TOKEN ?? null,
);
const api = new ApiService(new ApiClient(config));

async function main() {
    const user = await api.Users.GetCurrentUser();
    console.log(`Logged in as ${user.githubLogin}`);
}

main();
```

`ApiService` groups the API's operations by area (`Stacks`, `Deployments`, `Environments`, and so on). The first `ApiClientConfiguration` argument is the API base URL, including the `/api/` path and a trailing slash, and the second is a name for your application.

{{% /choosable %}}

{{% choosable language python %}}

```python
import os

from pulumi_cloud_sdk import ApiClient, Configuration
from pulumi_cloud_sdk.apis import UsersApi

config = Configuration()
config.access_token = os.environ["PULUMI_ACCESS_TOKEN"]

users = UsersApi(ApiClient(config))

user = users.get_current_user()
print(f"Logged in as {user.github_login}")
```

Each area of the API has its own class in `pulumi_cloud_sdk.apis` (`StacksApi`, `DeploymentsApi`, `EnvironmentsApi`, and so on). To use a different API endpoint, set `config.host`.

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/pulumi/pulumi-cloud-sdk/go/apiclient"
)

func main() {
	token := os.Getenv("PULUMI_ACCESS_TOKEN")

	client := &apiclient.CloudClient{
		BaseURL: "https://api.pulumi.com",
		Executor: func(req *http.Request) (*http.Response, error) {
			req.Header.Set("Authorization", "token "+token)
			return http.DefaultClient.Do(req)
		},
	}

	user, err := client.GetCurrentUser(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Logged in as %s\n", user.GitHubLogin)
}
```

Every operation is a method on `CloudClient`. The client sends requests through its `Executor` function, which is where you add the `Authorization` header and any other HTTP behavior you need, such as retries or a custom transport.

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System;
using Pulumi.Cloud.Sdk;
using Pulumi.Cloud.Sdk.Api;

var config = new ApiClientConfiguration()
    .WithAccessToken(Environment.GetEnvironmentVariable("PULUMI_ACCESS_TOKEN"));
var users = new UsersApi(new ApiClient(config));

var user = users.GetCurrentUser();
Console.WriteLine($"Logged in as {user.GithubLogin}");
```

Each area of the API has its own class in the `Pulumi.Cloud.Sdk.Api` namespace (`StacksApi`, `DeploymentsApi`, `EnvironmentsApi`, and so on). To use a different API endpoint, set `Host` on the configuration.

{{% /choosable %}}

{{% choosable language java %}}

```java
package myapp;

import com.pulumi.cloud.sdk.ApiClient;
import com.pulumi.cloud.sdk.ApiClientConfiguration;
import com.pulumi.cloud.sdk.api.UsersApi;
import com.pulumi.cloud.sdk.model.User;

public class App {
    public static void main(String[] args) {
        ApiClientConfiguration config = new ApiClientConfiguration()
            .setAccessToken(System.getenv("PULUMI_ACCESS_TOKEN"));
        UsersApi users = new UsersApi(new ApiClient(config));

        User user = users.getCurrentUser();
        System.out.println("Logged in as " + user.githubLogin);
    }
}
```

Each area of the API has its own class in the `com.pulumi.cloud.sdk.api` package (`StacksApi`, `DeploymentsApi`, `EnvironmentsApi`, and so on). To use a different API endpoint, call `setHost` on the configuration.

{{% /choosable %}}

## Versioning

The Cloud SDK doesn't follow semantic versioning. Pulumi Cloud is a continuously updated service, and its API always reflects the current live service rather than numbered releases. The SDK is regenerated from that API and released frequently, using date-based versions such as `2026.10.9`. Treat each release as a snapshot of the API on that date, and upgrade regularly to pick up new endpoints.

The Go module is the one exception to the date format. Go requires a module whose major version is 2 or higher to include that version in its import path, so the Go module keeps a major version of 1 and carries the date in the minor version, as in `v1.20261009.0`.

## API reference

| Language | Package | Reference |
|---|---|---|
| TypeScript | `@pulumi/cloud-sdk` | [TypeScript reference](/docs/reference/pkg/nodejs/pulumi/cloud-sdk/) |
| Python | `pulumi_cloud_sdk` | [Python reference](/docs/reference/pkg/python/pulumi_cloud_sdk/) |
| Go | `github.com/pulumi/pulumi-cloud-sdk/go` | [Go reference](https://pkg.go.dev/github.com/pulumi/pulumi-cloud-sdk/go/apiclient) |
| .NET | `Pulumi.Cloud.Sdk` | [.NET reference](/docs/reference/pkg/dotnet/cloud-sdk/pulumi.cloud.sdk/pulumi.cloud.sdk.html) |
| Java | `com.pulumi:pulumi-cloud-sdk` | [Java reference](/docs/reference/pkg/java/cloud-sdk/) |

For the endpoints themselves, including request and response schemas, see the [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/). The SDK source is in the [pulumi/pulumi-cloud-sdk](https://github.com/pulumi/pulumi-cloud-sdk) repository.
