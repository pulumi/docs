---
title_tag: "Stash | Pulumi Concepts"
meta_desc: The Stash resource allows you to save values to state for retrieval in later deployments. Learn more about the Pulumi Stash resource and how to use it.
title: Stash
h1: Stash
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Stash
        parent: iac-concepts
        weight: 30
    concepts:
        weight: 2
---

The `Stash` resource is a built-in Pulumi resource that allows you to save values to your stack's state for later retrieval. A stash takes a single input value and stores it in state, making it available as an output property. Stashes are commonly used to persist computed values, pass data between program executions, or save intermediate results that need to be accessed later.

Every `Stash` resource accepts any value as its `input` property and makes that value available through its `output` property. This value is stateful and won't change on later deployments if `input` is changed. The current `input` value is exposed as an output called `input` on the `Stash` resource if that is needed to be looked at.

## Create a stash {#create-stash}

To create a new stash, instantiate a `Stash` resource and provide a value for the `input` property. The stash will store this value in your stack's state and make it available through the `output` property.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const myStash = new pulumi.Stash("myStash", {
    input: "Hello, World!",
});

export const stashedValue = myStash.output;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

my_stash = pulumi.Stash("myStash", input="Hello, World!")

pulumi.export("stashedValue", my_stash.output)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        myStash, err := pulumi.NewStash(ctx, "myStash", &pulumi.StashArgs{
            Input: pulumi.String("Hello, World!"),
        })
        if err != nil {
            return err
        }

        ctx.Export("stashedValue", myStash.Output)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var myStash = new Stash("myStash", new StashArgs
    {
        Input = "Hello, World!",
    });

    return new Dictionary<string, object?>
    {
        ["stashedValue"] = myStash.Output,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.resources.Stash;
import com.pulumi.resources.StashArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var myStash = new Stash("myStash", StashArgs.builder()
                .input("Hello, World!")
                .build());

            ctx.export("stashedValue", myStash.output());
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  myStash:
    type: pulumi:pulumi:Stash
    properties:
      input: "Hello, World!"

outputs:
  stashedValue: ${myStash.output}
```

{{% /choosable %}}

{{< /chooser >}}

Stash is like any other resource in that it's name must be unique across the whole program.

## Stashing complex values

The `input` property of a `Stash` resource can accept any value, including complex objects, arrays, and nested structures. The value will be serialized as a Pulumi property value when stored in state.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const configStash = new pulumi.Stash("configStash", {
    input: {
        region: "us-west-2",
        instanceType: "t3.micro",
        tags: {
            Environment: "production",
            Team: "platform",
        },
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config_stash = pulumi.Stash("configStash", input={
    "region": "us-west-2",
    "instanceType": "t3.micro",
    "tags": {
        "Environment": "production",
        "Team": "platform",
    },
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
configStash, err := pulumi.NewStash(ctx, "configStash", &pulumi.StashArgs{
    Input: pulumi.Map{
        "region":       pulumi.String("us-west-2"),
        "instanceType": pulumi.String("t3.micro"),
        "tags": pulumi.Map{
            "Environment": pulumi.String("production"),
            "Team":        pulumi.String("platform"),
        },
    },
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var configStash = new Stash("configStash", new StashArgs
{
    Input = new Dictionary<string, object>
    {
        ["region"] = "us-west-2",
        ["instanceType"] = "t3.micro",
        ["tags"] = new Dictionary<string, object>
        {
            ["Environment"] = "production",
            ["Team"] = "platform",
        },
    },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var configStash = new Stash("configStash", StashArgs.builder()
    .input(Map.of(
        "region", "us-west-2",
        "instanceType", "t3.micro",
        "tags", Map.of(
            "Environment", "production",
            "Team", "platform"
        )
    ))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  configStash:
    type: pulumi:pulumi:Stash
    properties:
      input:
        region: us-west-2
        instanceType: t3.micro
        tags:
          Environment: production
          Team: platform
```

{{% /choosable %}}

{{< /chooser >}}

## Stashing secret values

The `Stash` resource respects secret annotations. If the `input` value is marked as a secret, the `output` will also be secret, and the value will be encrypted in your stack's state.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const apiKeyStash = new pulumi.Stash("apiKeyStash", {
    input: pulumi.secret("my-secret-api-key"),
});

// The output is also marked as secret
export const apiKey = apiKeyStash.output;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
api_key_stash = pulumi.Stash("apiKeyStash",
    input=pulumi.Output.secret("my-secret-api-key"))

# The output is also marked as secret
pulumi.export("apiKey", api_key_stash.output)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
apiKeyStash, err := pulumi.NewStash(ctx, "apiKeyStash", &pulumi.StashArgs{
    Input: pulumi.ToSecret(pulumi.String("my-secret-api-key")),
})
if err != nil {
    return err
}

// The output is also marked as secret
ctx.Export("apiKey", apiKeyStash.Output)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var apiKeyStash = new Stash("apiKeyStash", new StashArgs
{
    Input = Output.CreateSecret("my-secret-api-key"),
});

// The output is also marked as secret
return new Dictionary<string, object?>
{
    ["apiKey"] = apiKeyStash.Output,
};
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var apiKeyStash = new Stash("apiKeyStash", StashArgs.builder()
    .input(Output.secret("my-secret-api-key"))
    .build());

// The output is also marked as secret
ctx.export("apiKey", apiKeyStash.output());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  apiKeyStash:
    type: pulumi:pulumi:Stash
    properties:
      input:
        fn::secret: my-secret-api-key

outputs:
  apiKey: ${apiKeyStash.output}
```

{{% /choosable %}}

{{< /chooser >}}

When viewing stashed secret values, their plaintext content will not be shown by default. Instead, they will be displayed as `[secret]` in the CLI. Pass `--show-secrets` to reveal the plaintext value.

## Updating stashed values

To update the value stored in a `Stash`, simply modify the `input` property and run `pulumi up`. The new value
will be stored in state, and the `input` property will reflect the updated value. The `output` value will
continue to return the original value the `Stash` was constructed with.

To update the `output` value the `Stash` resource needs to be replaced. There are a few ways to do this.

1) Using the `--target-replace` argument to `up` to tell the engine to replace it.
2) Using `pulumi state taint` to mark the resource to be replaced on the next deployment.
3) Using the `TriggerReplacement` resource option to trigger the resource to replace on a change of value.

## Deleting a stash

To delete a `Stash` resource, remove it from your program and run `pulumi up`. Pulumi will remove the stash from your stack's state during the update.

## Common use cases

The `Stash` resource is useful for keeping track of a transient value across deployments. Examples include things like the first user running the deployment, the first time the stash was created, a generated random value that needs to be stable.

### Capturing the first deployment user

When you need to record who first deployed the infrastructure:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as os from "os";

const firstDeployer = new pulumi.Stash("firstDeployer", {
    input: os.userInfo().username,
});

// The output will always show the original deployer, even if others run updates later
export const originalDeployer = firstDeployer.output;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import getpass

first_deployer = pulumi.Stash("firstDeployer",
    input=getpass.getuser())

# The output will always show the original deployer, even if others run updates later
pulumi.export("originalDeployer", first_deployer.output)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "os"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        username, err := os.UserHomeDir()
        if err != nil {
            return err
        }

        firstDeployer, err := pulumi.NewStash(ctx, "firstDeployer", &pulumi.StashArgs{
            Input: pulumi.String(username),
        })
        if err != nil {
            return err
        }

        // The output will always show the original deployer, even if others run updates later
        ctx.Export("originalDeployer", firstDeployer.Output)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using System;

return await Deployment.RunAsync(() =>
{
    var firstDeployer = new Stash("firstDeployer", new StashArgs
    {
        Input = Environment.UserName,
    });

    // The output will always show the original deployer, even if others run updates later
    return new Dictionary<string, object?>
    {
        ["originalDeployer"] = firstDeployer.Output,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.resources.Stash;
import com.pulumi.resources.StashArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var firstDeployer = new Stash("firstDeployer", StashArgs.builder()
                .input(System.getProperty("user.name"))
                .build());

            // The output will always show the original deployer, even if others run updates later
            ctx.export("originalDeployer", firstDeployer.output());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

### Recording the initial creation time

When you need to persist the timestamp of when the infrastructure was first created:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const creationTime = new pulumi.Stash("creationTime", {
    input: new Date().toISOString(),
});

// This will always return the original creation time
export const firstDeployed = creationTime.output;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from datetime import datetime

creation_time = pulumi.Stash("creationTime",
    input=datetime.now().isoformat())

# This will always return the original creation time
pulumi.export("firstDeployed", creation_time.output)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "time"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        creationTime, err := pulumi.NewStash(ctx, "creationTime", &pulumi.StashArgs{
            Input: pulumi.String(time.Now().Format(time.RFC3339)),
        })
        if err != nil {
            return err
        }

        // This will always return the original creation time
        ctx.Export("firstDeployed", creationTime.Output)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using System;

return await Deployment.RunAsync(() =>
{
    var creationTime = new Stash("creationTime", new StashArgs
    {
        Input = DateTime.UtcNow.ToString("o"),
    });

    // This will always return the original creation time
    return new Dictionary<string, object?>
    {
        ["firstDeployed"] = creationTime.Output,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.resources.Stash;
import com.pulumi.resources.StashArgs;
import java.time.Instant;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var creationTime = new Stash("creationTime", StashArgs.builder()
                .input(Instant.now().toString())
                .build());

            // This will always return the original creation time
            ctx.export("firstDeployed", creationTime.output());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

### Preserving a stable random value

When you need a random value that remains constant across deployments:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";

// Generate a random password once
const randomPassword = generatePassword()

// Stash it so it doesn't change on subsequent deployments
const passwordStash = new pulumi.Stash("passwordStash", {
    input: pulumi.secret(randomPassword.result),
});

// Use the stashed password for database configuration
export const dbPassword = passwordStash.output;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_random as random

# Generate a random password once
random_password = generatePassword()

# Stash it so it doesn't change on subsequent deployments
password_stash = pulumi.Stash("passwordStash",
    input=pulumi.Output.secret(random_password.result))

# Use the stashed password for database configuration
pulumi.export("dbPassword", password_stash.output)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi-random/sdk/v4/go/random"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Generate a random password once
        randomPassword, err := generatePassword()
        if err != nil {
            return err
        }

        // Stash it so it doesn't change on subsequent deployments
        passwordStash, err := pulumi.NewStash(ctx, "passwordStash", &pulumi.StashArgs{
            Input: pulumi.ToSecret(randomPassword.Result),
        })
        if err != nil {
            return err
        }

        // Use the stashed password for database configuration
        ctx.Export("dbPassword", passwordStash.Output)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Random;

return await Deployment.RunAsync(() =>
{
    // Generate a random password once
    var randomPassword = generatePassword();

    // Stash it so it doesn't change on subsequent deployments
    var passwordStash = new Stash("passwordStash", new StashArgs
    {
        Input = Output.CreateSecret(randomPassword.Result),
    });

    // Use the stashed password for database configuration
    return new Dictionary<string, object?>
    {
        ["dbPassword"] = passwordStash.Output,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.resources.Stash;
import com.pulumi.resources.StashArgs;
import com.pulumi.random.RandomPassword;
import com.pulumi.random.RandomPasswordArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Generate a random password once
            var randomPassword = generatePassword();

            // Stash it so it doesn't change on subsequent deployments
            var passwordStash = new Stash("passwordStash", StashArgs.builder()
                .input(Output.secret(randomPassword.result()))
                .build());

            // Use the stashed password for database configuration
            ctx.export("dbPassword", passwordStash.output());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}