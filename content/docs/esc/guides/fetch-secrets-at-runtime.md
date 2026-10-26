---
title_tag: Fetch Secrets at Runtime with the ESC SDK | Pulumi ESC
title: Fetch secrets at runtime with the ESC SDK
h1: Fetch secrets at runtime with the ESC SDK
meta_desc: Learn how to read secrets and configuration from a Pulumi ESC environment inside a running application using the TypeScript, Python, Go, or .NET SDK.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-fetch-secrets-at-runtime
    weight: 45
---

Applications often need a database password, an API key, or a short-lived cloud credential at the moment they start. This guide shows how to have your application read those values directly from a [Pulumi ESC](/docs/esc/) environment by using the ESC SDK, so that no secret needs to be written into your code, your container image, or your deployment manifests.

The examples focus on the application code. If you want to consume an environment from a Pulumi IaC program, use [stack configuration](/docs/esc/guides/pulumi-iac/) instead of the SDK.

## Choose how your application receives environment values

The SDK is one of several ways to deliver ESC values to a workload. Pick the one that matches how your application runs:

| Approach | Use it when |
|----------|-------------|
| ESC SDK (this guide) | Your application can call Pulumi Cloud directly and needs fresh values on startup or while it runs, including dynamic values such as short-lived credentials. |
| [`pulumi env run`](/docs/esc/guides/running-commands/) | You want to inject values as environment variables into a process without changing application code, such as in local development or a CI job. |
| [External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/) or [Secrets Store CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/) | Your workload runs on Kubernetes and you prefer to deliver values as Kubernetes Secrets or mounted files. |
| [Sync to an external platform](/docs/esc/guides/sync-secrets-to-external-platforms/) | The platform running your application has its own secret store that the application already reads from. |

## Prerequisites

- A Pulumi Cloud account and an ESC environment that defines the values your application needs. The examples below assume an environment named `my-project/my-app-prod` that looks like this:

  ```yaml
  values:
    databaseUrl: postgres://db.example.com:5432/app
    apiKey:
      fn::secret: my-api-key-value
  ```

- A Pulumi access token that can open that environment. Create a dedicated machine token for the application rather than reusing a personal token:
  - A [team token](/docs/administration/concepts/access-tokens/#team-access-tokens) for a team that has the `Environment Open` permission set on only the environments the application needs. Teams are available in {{< pulumi-cloud-editions "teams" >}}.
  - An [organization token](/docs/administration/concepts/access-tokens/#creating-an-organization-access-token) assigned a [custom role](/docs/administration/concepts/rbac/roles/#custom-roles) that grants the same access. Organization tokens are available in {{< pulumi-cloud-editions "org-team-access-tokens" >}}, and custom roles in {{< pulumi-cloud-editions "custom-roles" >}}.

  A team token also receives your organization's default Member permissions, and an organization token created without a role receives the Member role. If your [organization-wide role settings](/docs/administration/concepts/rbac/roles/#organization-wide-role-settings) give members access to environments, the token can open those environments too, so set **Environment permissions** there to **None** if you rely on the token's team or role to limit what it can read.
- The name of your Pulumi organization.

The SDK reads credentials from the `PULUMI_ACCESS_TOKEN` environment variable, and the backend URL from `PULUMI_BACKEND_URL`, which defaults to `https://api.pulumi.com`. The examples read the organization name from a `PULUMI_ORG` environment variable.

## Install the SDK and open the environment

Opening an environment evaluates it, resolves any secrets and dynamic values, and returns the result. The SDK provides a single call that opens the environment and reads its values in one step.

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

Install the package:

```bash
npm install @pulumi/esc-sdk
```

Then open the environment and read its values:

```typescript
import * as esc from "@pulumi/esc-sdk";

async function main() {
    const orgName = process.env.PULUMI_ORG!;
    const client = esc.DefaultClient();

    const openEnv = await client.openAndReadEnvironment(orgName, "my-project", "my-app-prod");
    if (!openEnv || !openEnv.values) {
        throw new Error("Failed to open the environment");
    }

    const databaseUrl = openEnv.values["databaseUrl"] as string;
    const apiKey = openEnv.values["apiKey"] as string;

    // Pass the values to your database client, HTTP client, and so on.
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
```

{{% /choosable %}}

{{% choosable language python %}}

Install the package:

```bash
pip install pulumi-esc-sdk
```

Then open the environment and read its values:

```python
import os

from pulumi_esc_sdk import esc_client

org_name = os.environ["PULUMI_ORG"]
client = esc_client.default_client()

_, values, _ = client.open_and_read_environment(org_name, "my-project", "my-app-prod")

database_url = values["databaseUrl"]
api_key = values["apiKey"]

# Pass the values to your database client, HTTP client, and so on.
```

{{% /choosable %}}

{{% choosable language go %}}

Add the module to your project:

```bash
go get github.com/pulumi/esc-sdk/sdk
```

Then open the environment and read its values:

```go
package main

import (
	"log"
	"os"

	esc "github.com/pulumi/esc-sdk/sdk/go"
)

func main() {
	orgName := os.Getenv("PULUMI_ORG")

	authCtx, client, err := esc.DefaultLogin()
	if err != nil {
		log.Fatalf("Failed to create the ESC client: %v", err)
	}

	_, values, err := client.OpenAndReadEnvironment(authCtx, orgName, "my-project", "my-app-prod")
	if err != nil {
		log.Fatalf("Failed to open the environment: %v", err)
	}

	databaseURL, ok := values["databaseUrl"].(string)
	if !ok {
		log.Fatal("databaseUrl is missing or is not a string")
	}
	apiKey, ok := values["apiKey"].(string)
	if !ok {
		log.Fatal("apiKey is missing or is not a string")
	}

	// Pass the values to your database client, HTTP client, and so on.
	_ = databaseURL
	_ = apiKey
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

Add the package to your project:

```bash
dotnet add package Pulumi.Esc.Sdk
```

Then open the environment and read its values:

```csharp
using Pulumi.Esc.Sdk;

var orgName = Environment.GetEnvironmentVariable("PULUMI_ORG")!;

using var client = EscClient.CreateDefault();

var (_, values) = await client.OpenAndReadEnvironmentAsync(orgName, "my-project", "my-app-prod");

var databaseUrl = values?["databaseUrl"]?.ToString();
var apiKey = values?["apiKey"]?.ToString();

// Pass the values to your database client, HTTP client, and so on.
```

{{% /choosable %}}

{{< /chooser >}}

Secret values come back as plain values in the result, so treat them accordingly: do not log them, and avoid including them in error messages or telemetry. Plain configuration values and secrets are returned side by side, and the application does not need to distinguish between them.

For the full list of client options, such as passing an access token explicitly instead of reading it from the environment, see the SDK reference for your language: [TypeScript](/docs/esc/languages-sdks/javascript/), [Python](/docs/esc/languages-sdks/python/), [Go](/docs/esc/languages-sdks/go/), or [.NET](/docs/esc/languages-sdks/dotnet/).

## Handle failures and refresh values

Opening an environment makes a network call to Pulumi Cloud and can fail if the token is invalid, the token doesn't have permission to open the environment, or the service is unreachable. Decide ahead of time what your application should do in each case:

- **At startup**, fail fast if the environment cannot be opened, so that your orchestrator restarts the workload and surfaces the problem instead of running without credentials.
- **While running**, keep using the values you already have if a refresh fails, and retry with backoff.

The values you read are a snapshot taken when the environment was opened. If the environment contains dynamic values, such as credentials from the [`aws-login` provider](/docs/esc/providers/login/aws-login/), they expire on their own schedule, so open the environment again before they do. Likewise, open it again when you rotate a secret and want a running process to pick up the new value. Each call to open the environment evaluates it again and returns current values.

Avoid opening the environment on every request. Open it once at startup, hold the values in memory, and refresh them on a timer that is shorter than the shortest lifetime of any dynamic value.

## Provide the access token to your deployed application

The application still needs a Pulumi access token to call Pulumi Cloud, so deliver that single token through the mechanism your platform provides for secrets, such as a managed secret store or an encrypted deployment variable, and expose it to the process as `PULUMI_ACCESS_TOKEN`. Every other secret then lives in ESC, where you can audit access, rotate values, and change them without redeploying the application.

Scope the token as described in [Prerequisites](#prerequisites), so that a leaked token exposes only the environments this application uses.

If your application runs on a platform that issues OIDC tokens to its workloads, such as Amazon EKS, Google Kubernetes Engine, or GitHub Actions, you can avoid storing a long-lived Pulumi token at all. Register the platform as an [OIDC issuer](/docs/administration/concepts/oidc-issuers/), have the application exchange its ID token for a short-lived Pulumi access token at startup, and pass that token to the SDK client. The exchanged token expires, so repeat the exchange before you open the environment again.

## Next steps

- Learn how environments are structured in [Environments](/docs/esc/concepts/environments/).
- Review the [ESC SDK overview](/docs/esc/concepts/sdks/) for other scenarios, such as managing environments programmatically.
- Inject values into a command without changing application code with [`pulumi env run`](/docs/esc/guides/running-commands/).
