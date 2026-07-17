---
title_tag: .NET SDK | Pulumi ESC
title: .NET
h1: "Pulumi ESC: .NET SDK"
meta_desc: This page provides an overview on how to use Pulumi ESC .NET SDK.
menu:
  esc:
    parent: esc-languages-sdks
    identifier: esc-dotnet-sdk
    weight: 4
aliases:
  - /docs/esc/sdk/dotnet/
  - /docs/esc/development/languages-sdks/dotnet/
---

Pulumi ESC provides a .NET SDK for managing environments and reading their configuration and secrets from your own code. It supports C#, F#, and Visual Basic.

{{< esc-sdk-config-note >}}

Here are some of the scenarios the SDK can automate:

* List environments and read environment definitions
* Open environments to access config and resolve secrets
* Create, update, decrypt, and delete environment definitions
    * Supports both structured types and yaml text
* List environment revisions and create new revision tags
* Check environment definitions for errors

## Runtime support

The SDK supports any [supported version](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle) of .NET. We recommend using a recent release for the best experience. The SDK supports C#, F#, and Visual Basic.

## Install the SDK package

Run `dotnet add package Pulumi.Esc.Sdk` to install the SDK package.

### Initializing ESC SDK client

The easiest way to initialize an ESC SDK client is to run:

```csharp
using Pulumi.Esc.Sdk;

using var client = EscClient.CreateDefault();
```

This method will first look for the `PULUMI_ACCESS_TOKEN` environment variable, and if it's not present, it will fall back to CLI credentials that are present on your machine if you have logged in using the Pulumi CLI.

If the default behavior does not work for you, you can always pass an access token directly to the client constructor:

```csharp
using Pulumi.Esc.Sdk;

using var client = EscClient.Create(myAccessToken);
```

## Examples

All of these examples expect a `PULUMI_ACCESS_TOKEN` and `PULUMI_ORG` environment variable to be set.

### Manage environment example

This example creates a new environment, opens that environment to access a secret, and then lists the environments.

```csharp
using Pulumi.Esc.Sdk;

var orgName = Environment.GetEnvironmentVariable("PULUMI_ORG")!;

using var client = EscClient.CreateDefault();

var projName = "examples";
var envName = "sdk-dotnet-example";

// Create a new environment
await client.CreateEnvironmentAsync(orgName, projName, envName);

// Update the environment with a new definition containing a secret
var yaml = """
values:
  my_secret:
    fn::secret: "shh! don't tell anyone"
""";
await client.UpdateEnvironmentYamlAsync(orgName, projName, envName, yaml);

// Open and read the environment
var (_, values) = await client.OpenAndReadEnvironmentAsync(orgName, projName, envName);

// Access the value of the secret
var secretValue = values?["my_secret"];
Console.WriteLine($"Secret value: {secretValue}");

// List all the environments in the organization
var orgEnvs = await client.ListEnvironmentsAsync(orgName);
foreach (var env in orgEnvs.Environments ?? [])
{
    Console.WriteLine($"Environment: {env.Project}/{env.Name}");
}
```

### Tag revision example

This example lists revisions for an environment, tags a revision, and lists revision tags.

```csharp
using Pulumi.Esc.Sdk;

var orgName = Environment.GetEnvironmentVariable("PULUMI_ORG")!;

using var client = EscClient.CreateDefault();

var projName = "examples";
var envName = "sdk-dotnet-example";

// List environment revisions
var revisions = await client.ListEnvironmentRevisionsAsync(orgName, projName, envName);

if (revisions.Count < 2)
{
    throw new Exception($"Expected at least 2 revisions for environment {projName}/{envName}");
}

// Tag the second-latest revision
var revision = revisions[1];
await client.CreateEnvironmentRevisionTagAsync(orgName, projName, envName, "stable", revision.Number);

Console.WriteLine($"Tagged revision {revision.Number} as 'stable'");

// List revision tags
var tags = await client.ListEnvironmentRevisionTagsAsync(orgName, projName, envName);
foreach (var tag in tags.Tags ?? [])
{
    Console.WriteLine($"Tag {tag.Name} at revision {tag.Revision}");
}
```

## Documentation

* [API Reference Documentation](/docs/reference/pkg/dotnet/esc-sdk/)
* [NuGet package](https://www.nuget.org/packages/Pulumi.Esc.Sdk/)
