---
title: "Introducing Pulumi ESC SDK: Streamline Your Application Secrets Management"
allow_long_title: true
date: 2024-06-05T00:00:00-04:00
draft: false
meta_desc: "The new Pulumi ESC SDK allows developers to seamlessly integrate Pulumi
  ESC with their applications for secrets management"
meta_image: "meta.png"
authors:
  - arun-loganathan
  - cleve-littlefield
tags:
  - esc
  - secrets
  - features
search:
  keywords:
    - SDK
    - Secrets
    - Application Secrets
    - Secrets Management
---

Managing secrets and application configurations effectively is crucial for building secure and maintainable software. However, developers often face challenges such as hardcoded credentials, configuration inconsistencies, and security risks. [Pulumi Environments Secrets and Configuration](/product/esc) (ESC) simplifies the management of sensitive data and configuration across your entire application lifecycle. Today, we're thrilled to introduce the official Pulumi ESC SDK in [TypeScript/JavaScript](/docs/esc/development/languages-sdks/javascript/), [Go](/docs/esc/development/languages-sdks/go/), and [Python](/docs/esc/development/languages-sdks/python/), making it even easier to integrate ESC directly into your applications.

<!--more-->

## Primer on Pulumi ESC

Pulumi ESC (Environments, Secrets, and Configuration) provides a developer-first solution to simplify how you manage sensitive data and configuration across your entire application lifecycle. It's a fully managed solution allowing teams to generate [dynamic cloud provider](/docs/esc/integrations/) credentials, aggregate secrets and configuration from multiple sources, and manage them through composable collections called "[environments](/docs/esc/environments/)." These environments can be consumed from anywhere, making Pulumi ESC ideal for any [application and development workflow](/docs/esc/integrations/). Additionally, while Pulumi ESC works independently to eliminate duplication and reduce drift and sprawl of secrets and configuration for all your applications, it also [integrates](/docs/esc/get-started/integrate-with-pulumi-iac/) smoothly with Pulumi Infrastructure as Code (IaC) to enhance these capabilities within the Pulumi ecosystem.

## Introducing the Pulumi ESC SDK

We're excited to unveil the official Pulumi ESC SDK, making it even easier to harness the power of ESC directly within your applications using your favorite programming languages. The SDK provides a simple programmatic interface to all of Pulumi ESC's robust features, allowing you to:

- **Manage the Entire Lifecycle of Your Environments:** Create new environments, list existing ones, and easily update or delete them as your needs evolve. You can even add [version tags](/docs/esc/environments/versioning/#tagging-versions) to your environments, making it simple to track changes and roll back to previous states if needed.
- **Seamlessly Integrate Secrets and Configurations:** Securely access and utilize secrets and configurations within your applications, ensuring consistency of configuration across environments. The SDK provides a streamlined way to fetch the information you need, whether it's dynamic cloud credentials, database connection strings, feature flags, or any other sensitive data.

The Pulumi ESC SDK streamlines secret and configuration management, promoting secure handling best practices. It handles the secure storage and retrieval of your sensitive data at runtime, eliminating the need to store credentials long-term and minimizing the risk of accidental exposure. The SDK is a natural extension of your development workflow, offering familiar objects and methods, smooth integration with your IDE, and the benefits of type safety such as compile-time checks and helpful code suggestions that reduce errors and accelerate development.

## How to Get Started

Here are a few examples of how to use the ESC SDK for various languages:

{{< chooser language "typescript,python,go" />}}

{{% choosable language typescript %}}

```typescript
import * as esc from "@pulumi/esc-sdk";

async function main() {
    const PULUMI_ACCESS_TOKEN = process.env.PULUMI_ACCESS_TOKEN!;
    const orgName = process.env.PULUMI_ORG!;
    const config = new esc.Configuration({ accessToken: PULUMI_ACCESS_TOKEN });
    const client = new esc.EscApi(config);

    const envName = "sdk-typescript-example";

    // Create a new environment
    await client.createEnvironment(orgName, envName);

    const envDef: esc.EnvironmentDefinition = {
        values: {
            my_secret: {
                "fn::secret": "shh! don't tell anyone",
            },
        },
    };

    // Update the environment with the new definition
    await client.updateEnvironment(orgName, envName, envDef);

    // Open and read the environment
    const openEnv = await client.openAndReadEnvironment(orgName, envName);

    if (!openEnv) {
        console.error("Failed to open and read the environment");
        return;
    }

    // Acces the value of the secret
    const secretValue = openEnv.values?.my_secret;
    console.log(`Secret value: ${secretValue}\n`);

    // List all the environments in the organization
    const orgEnvs = await client.listEnvironments(orgName);
    if (!orgEnvs || !orgEnvs.environments) {
        console.log("No environments found");
        return;
    }

    for (const env of orgEnvs.environments) {
        console.log(`Environment: ${env.name}`);
    }
}

(async ()=>{
    await main();
})();
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_esc_sdk as esc
import os

accessToken = os.getenv("PULUMI_ACCESS_TOKEN")

orgName = os.getenv("PULUMI_ORG")

configuration = esc.Configuration(access_token=accessToken)
client = esc.EscClient(configuration)

envName = "sdk-python-example"

# Create environment
client.create_environment(orgName, envName)

# create a new EnvironmentDefinition with "my_secret" as a secret in values additional_properties
envDef = esc.EnvironmentDefinition(
    imports=[],
    values=esc.EnvironmentDefinitionValues(
        additional_properties={
            "my_secret": {
                "fn::secret": "shh! don't tell anyone"
            }
        }
    )
)

# Update environment
client.update_environment(orgName, envName, envDef)

# Open and read the environment

env, values, yaml = client.open_and_read_environment(orgName, envName)

secret = values["my_secret"]
print(f'Secret: {secret}\n')

# List environments

environments = client.list_environments(orgName)

for env in environments.environments:
    print(f'Environment: {env.name}')
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"log"
	"os"

	esc "github.com/pulumi/esc-sdk/sdk/go"
)

func main() {
	accessToken := os.Getenv("PULUMI_ACCESS_TOKEN")
	orgName := os.Getenv("PULUMI_ORG")
	configuration := esc.NewConfiguration()
	escClient := esc.NewClient(configuration)
	authCtx := esc.NewAuthContext(accessToken)

	envName := "sdk-go-example"
	// Create Environment
	err := escClient.CreateEnvironment(authCtx, orgName, envName)
	if err != nil {
		log.Fatalf("Failed to create environment: %v", err)
	}

	// Update Environment with Secrets
	updatePayload := &esc.EnvironmentDefinition{
		Values: &esc.EnvironmentDefinitionValues{
			AdditionalProperties: map[string]interface{}{
				"my_secret": map[string]string{
					"fn::secret": "shh! don't tell anyone",
				},
			},
		},
	}

	_, err = escClient.UpdateEnvironment(authCtx, orgName, envName, updatePayload)
	if err != nil {
		log.Fatalf("Failed to update environment: %v", err)
	}

	// Open and View Secrets
	_, values, err := escClient.OpenAndReadEnvironment(authCtx, orgName, envName)
	if err != nil {
		log.Fatalf("Failed to open environment: %v", err)
	}

	mySecret, ok := values["my_secret"]
	if !ok {
		log.Fatalf("Secret 'my_secret' not found in environment %s", envName)
	}

	log.Printf("my_secret: %v\n", mySecret)

	orgEnvs, err := escClient.ListEnvironments(authCtx, orgName, nil)
	if err != nil {
		log.Fatalf("Failed to list environments: %v", err)
	}

	for _, orgEnv := range orgEnvs.Environments {
		log.Printf("Environment: %v\n", orgEnv.Name)
	}

}
```
{{% /choosable %}}

## Example Scenarios: Pulumi ESC SDK in Action

Here are some real-world scenarios showcasing how you can leverage the Pulumi ESC SDK:

- **Database Credentials**: Applications can use the ESC SDK to fetch database credentials with a specified TTL, ensuring they always use valid credentials, even as the credentials are rotated in the background. This eliminates service interruptions due to expired credentials.
- **Secure Serverless Deployments**: A Google Cloud Function requiring access to an AWS S3 bucket can leverage the ESC SDK to obtain temporary AWS credentials during runtime. This enables secure cross-cloud interactions without embedding long-lived AWS credentials directly within the function's code.
- **Microservices Configuration**: With ESC, development teams can manage diverse configurations for their microservices, including API endpoints, retry policies, and logging levels, specific to each environment (development, staging, production). The ESC SDK allows each microservice to retrieve the correct configuration values during runtime, simplifying environment-based customizations.

## Get Started Today!

The Pulumi ESC SDK is available now! To learn more and start simplifying your application secrets workflow, check out the [Pulumi ESC SDK](/docs/esc/development/languages-sdks/) Documentation. We're confident that this powerful new tool will streamline your development process, enhance your application security, and empower you to build innovative solutions with confidence. Join us on this journey towards a more secure and manageable future for application secrets and configurations!
