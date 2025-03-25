---
title_tag: Go SDK | Pulumi ESC
title: Go
h1: "Pulumi ESC: Go SDK"
meta_desc: This page provides an overview on how to use Pulumi ESC Go SDK.
menu:
  esc:
    parent: esc-languages-sdks
    identifier: esc-go-sdk
    weight: 3
aliases:
  - /docs/esc/sdk/go/
---

The [Go SDK](https://github.com/pulumi/esc-sdk) for [Pulumi ESC (Environments, Secrets, and Configuration)](/product/esc/) allows you to automate Pulumi ESC.

Here are some of the scenarios the SDK can automate:

* List environments and read environment definitions
* Open environments to access config and resolve secrets
* Create, update, decrypt, and delete environment definitions
    * Supports both structured types and yaml text
* List environment revisions and create new revision tags
* Check environment definitions for errors

## Install the SDK package

Run `go get github.com/pulumi/esc-sdk/sdk` to install the SDK package.

### Initializing ESC SDK client

The easiest way to initialize an ESC SDK client and authorization context is to run:

```go
import (
	esc "github.com/pulumi/esc-sdk/sdk/go"
)

authCtx, escClient, err := esc.DefaultLogin()
```

This method will first look for the `PULUMI_ACCESS_TOKEN` environment variable, and if it's not present, it will fall back to CLI credentials that are present on your machine if you have logged in using Pulumi CLI or ESC CLI.

If the default behavior does not work for you, you can always manually initialize the client configuration and pass it into the client constructor:

```go
import (
	esc "github.com/pulumi/esc-sdk/sdk/go"
)

configuration := esc.NewConfiguration()
escClient := esc.NewClient(configuration)
authCtx := esc.NewAuthContext(myAccessToken)
```

## Examples

All of these examples expect a `PULUMI_ACCESS_TOKEN` and `PULUMI_ORG` environment variable to be set.

### Manage environment example

This example creates a new environment, opens that environment to access a secret, and the list the environments.

{{< chooser language "go" >}}

{{% choosable language "go" %}}

```go
package main

import (
	"log"
	"os"

	esc "github.com/pulumi/esc-sdk/sdk/go"
)

func main() {
	orgName := os.Getenv("PULUMI_ORG")
	authCtx, escClient, err := esc.DefaultLogin()

	projName := "examples"
	envName := "sdk-go-example"
	// Create Environment
	err = escClient.CreateEnvironment(authCtx, orgName, projName, envName)
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

	_, err = escClient.UpdateEnvironment(authCtx, orgName, projName, envName, updatePayload)
	if err != nil {
		log.Fatalf("Failed to update environment: %v", err)
	}

	// Open and View Secrets
	_, values, err := escClient.OpenAndReadEnvironment(authCtx, orgName, projName, envName)
	if err != nil {
		log.Fatalf("Failed to open environment: %v", err)
	}

	mySecret, ok := values["my_secret"]
	if !ok {
		log.Fatalf("Secret 'my_secret' not found in environment %s/%s", projName, envName)
	}

	log.Printf("my_secret: %v\n", mySecret)

	orgEnvs, err := escClient.ListEnvironments(authCtx, orgName, nil)
	if err != nil {
		log.Fatalf("Failed to list environments: %v", err)
	}

	for _, orgEnv := range orgEnvs.Environments {
		log.Printf("Environment: %v/%v\n", orgEnv.Project, orgEnv.Name)
	}

}

```

{{% /choosable %}}
{{< /chooser >}}

### Tag revision example

This example lists revisions for an environment, tags a revision, and lists revision tags.

{{< chooser language "go" >}}

{{% choosable language "go" %}}

```go
package main

import (
	"log"
	"os"

	esc "github.com/pulumi/esc-sdk/sdk/go"
)

func main() {
	orgName := os.Getenv("PULUMI_ORG")
	authCtx, escClient, err := esc.DefaultLogin()

	projName := "examples"
	envName := "sdk-go-example"
	revs, err := escClient.ListEnvironmentRevisions(authCtx, orgName, projName, envName)
	if err != nil {
		log.Fatalf("Failed to list environment revisions: %v", err)
	}

	if len(revs) < 2 {
		return
	}

	// get the second latest revision
	secondLatestRev := revs[1]
	err = escClient.CreateEnvironmentRevisionTag(authCtx, orgName, projName, envName, "stable", secondLatestRev.Number)
	if err != nil {
		log.Fatalf("Failed to tag environment revision: %v", err)
	}

	log.Printf("Tagged revision %d as 'stable'", secondLatestRev.Number)

	tags, err := escClient.ListEnvironmentRevisionTags(authCtx, orgName, projName, envName)
	if err != nil {
		log.Fatalf("Failed to list environment revision tags: %v", err)
	}

	for _, tag := range tags.Tags {
		log.Printf("Tag %s at revision %d", tag.Name, tag.Revision)
	}
}

```

{{% /choosable %}}
{{< /chooser >}}

## Documentation

* [API Reference Documentation](https://pkg.go.dev/github.com/pulumi/esc-sdk/sdk/go)
