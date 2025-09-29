---
title: Get Started with Pulumi & Oracle Cloud
meta_desc: Set up Pulumi to manage infrastructure on Oracle Cloud Infrastructure - follow these 6 simple steps
type: page
layout: cloud-integrated
subtitle: 6 simple steps

cloud:
  name: Oracle Cloud Infrastructure
  slug: oci
  provider: oci
---

## What You'll Build

You'll create an **Object Storage bucket** in Oracle Cloud using infrastructure as code.

This covers the fundamentals: authentication, defining resources, and deploying to Oracle Cloud Infrastructure.

## Install Pulumi

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
brew install pulumi/tap/pulumi
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
Invoke-WebRequest -Uri "https://get.pulumi.com/install.ps1" -OutFile install.ps1; .\install.ps1
```

{{% /choosable %}}

Verify the installation:

```bash
pulumi version
```

## Check Prerequisites

Ensure you have the language runtime for your chosen language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
**Required:** [Node.js](https://nodejs.org/) version 14 or later

Check your version:

```bash
node --version
```

{{% /choosable %}}

{{% choosable language python %}}
**Required:** [Python](https://www.python.org/) 3.8 or later

Check your version:

```bash
python3 --version
```

{{% /choosable %}}

{{% choosable language go %}}
**Required:** [Go](https://golang.org/) 1.20 or later

Check your version:

```bash
go version
```

{{% /choosable %}}

{{% choosable language csharp %}}
**Required:** [.NET](https://dotnet.microsoft.com/) 6.0 or later

Check your version:

```bash
dotnet --version
```

{{% /choosable %}}

{{% choosable language java %}}
**Required:**

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later

Check your versions:

```bash
java --version
mvn --version
```

{{% /choosable %}}

{{% choosable language yaml %}}
No additional language runtime required - YAML is built into Pulumi!
{{% /choosable %}}

## Configure Oracle Cloud

Set up your OCI credentials for Pulumi to use:

### Install OCI CLI

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

{{% /choosable %}}

{{% choosable os windows %}}
Download and run the [Windows installer](https://github.com/oracle/oci-cli/releases/latest)
{{% /choosable %}}

### Configure Credentials

```bash
oci setup config
```

This will prompt you for:

- **User OCID**: Find in OCI Console → Identity → Users → Your User
- **Tenancy OCID**: Find in OCI Console → Administration → Tenancy Details
- **Region**: e.g., `us-ashburn-1`
- **API Signing Key**: Path to your private key (will be created if doesn't exist)

### Verify Configuration

```bash
oci iam region list
```

You should see a list of available OCI regions.

## Create Your Project

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-typescript
```

This creates:

- `index.ts` - Your infrastructure code
- `package.json` - Node.js dependencies
- `Pulumi.yaml` - Project configuration

**Your infrastructure code:**

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as oci from "@pulumi/oci";

// Get configuration
const config = new pulumi.Config();
const compartmentId = config.require("compartmentId");

// Get the namespace for Object Storage
const namespace = oci.objectstorage.getNamespaceOutput();

// Create an Object Storage bucket
const bucket = new oci.objectstorage.Bucket("my-bucket", {
    compartmentId: compartmentId,
    namespace: namespace.namespace,
    name: `my-bucket-${Date.now()}`,
    accessType: "NoPublicAccess",
});

// Export the bucket name
export const bucketName = bucket.name;
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-python
```

This creates:

- `__main__.py` - Your infrastructure code
- `requirements.txt` - Python dependencies
- `Pulumi.yaml` - Project configuration

**Your infrastructure code:**

```python
import pulumi
import pulumi_oci as oci
import time

# Get configuration
config = pulumi.Config()
compartment_id = config.require("compartmentId")

# Get the namespace for Object Storage
namespace = oci.objectstorage.get_namespace()

# Create an Object Storage bucket
bucket = oci.objectstorage.Bucket("my-bucket",
    compartment_id=compartment_id,
    namespace=namespace.namespace,
    name=f"my-bucket-{int(time.time())}",
    access_type="NoPublicAccess"
)

# Export the bucket name
pulumi.export("bucketName", bucket.name)
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-go
```

This creates:

- `main.go` - Your infrastructure code
- `go.mod` - Go module dependencies
- `Pulumi.yaml` - Project configuration

**Your infrastructure code:**

```go
package main

import (
    "fmt"
    "time"

    "github.com/pulumi/pulumi-oci/sdk/v2/go/oci/objectstorage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Get configuration
        cfg := config.New(ctx, "")
        compartmentId := cfg.Require("compartmentId")

        // Get the namespace for Object Storage
        namespace, err := objectstorage.GetNamespace(ctx, nil)
        if err != nil {
            return err
        }

        // Create an Object Storage bucket
        bucketName := fmt.Sprintf("my-bucket-%d", time.Now().Unix())
        bucket, err := objectstorage.NewBucket(ctx, "my-bucket", &objectstorage.BucketArgs{
            CompartmentId: pulumi.String(compartmentId),
            Namespace:     pulumi.String(namespace.Namespace),
            Name:          pulumi.String(bucketName),
            AccessType:    pulumi.String("NoPublicAccess"),
        })
        if err != nil {
            return err
        }

        // Export the bucket name
        ctx.Export("bucketName", bucket.Name)

        return nil
    })
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-csharp
```

This creates:

- `Program.cs` - Your infrastructure code
- `*.csproj` - .NET project file
- `Pulumi.yaml` - Project configuration

**Your infrastructure code:**

```csharp
using System;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Oci.ObjectStorage;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        // Get configuration
        var config = new Config();
        var compartmentId = config.Require("compartmentId");

        // Get the namespace for Object Storage
        var @namespace = GetNamespace.Invoke();

        // Create an Object Storage bucket
        var bucketName = $"my-bucket-{DateTimeOffset.UtcNow.ToUnixTimeSeconds()}";
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            CompartmentId = compartmentId,
            Namespace = @namespace.Apply(ns => ns.Namespace),
            Name = bucketName,
            AccessType = "NoPublicAccess",
        });

        // Export the bucket name
        this.BucketName = bucket.Name;
    }

    [Output]
    public Output<string> BucketName { get; set; }
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-java
```

This creates:

- `src/main/java/myproject/App.java` - Your infrastructure code
- `pom.xml` - Maven configuration
- `Pulumi.yaml` - Project configuration

**Your infrastructure code:**

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.oci.objectstorage.Bucket;
import com.pulumi.oci.objectstorage.BucketArgs;
import com.pulumi.oci.objectstorage.ObjectstorageFunctions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Get configuration
        var config = ctx.config();
        var compartmentId = config.require("compartmentId");

        // Get the namespace for Object Storage
        var namespace = ObjectstorageFunctions.getNamespace();

        // Create an Object Storage bucket
        var bucketName = "my-bucket-" + System.currentTimeMillis();
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .compartmentId(compartmentId)
            .namespace(namespace.applyValue(ns -> ns.namespace()))
            .name(bucketName)
            .accessType("NoPublicAccess")
            .build());

        // Export the bucket name
        ctx.export("bucketName", bucket.name());
    }
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-yaml
```

This creates:

- `Pulumi.yaml` - Project configuration and resources
- `Pulumi.dev.yaml` - Stack configuration

**Your infrastructure code:**

```yaml
name: oci-quickstart
runtime: yaml
description: A minimal Oracle Cloud Infrastructure Pulumi YAML program

config:
  compartmentId:
    type: string

variables:
  namespace:
    fn::invoke:
      function: oci:ObjectStorage:getNamespace
  timestamp:
    fn::invoke:
      function: std:datetime:timestamp
      arguments:
        format: unix

resources:
  # Create an Object Storage bucket
  my-bucket:
    type: oci:ObjectStorage:Bucket
    properties:
      compartmentId: ${compartmentId}
      namespace: ${namespace.namespace}
      name: my-bucket-${timestamp.unix}
      accessType: NoPublicAccess

outputs:
  # Export the bucket name
  bucketName: ${my-bucket.name}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

{{% /choosable %}}

## Deploy Your Bucket

Run Pulumi to create your resources:

```bash
pulumi up
```

Pulumi will:

1. Show a preview of the Object Storage bucket to be created
2. Ask for your confirmation
3. Create your bucket in OCI
4. Save the state in Pulumi Cloud

## 🎉 Congratulations!

You've just deployed your first infrastructure with Pulumi on Oracle Cloud!

### What's Next?

- **[View your stack in Pulumi Cloud →](https://app.pulumi.com/stacks)**
  Explore resource details, deployment history, and manage your infrastructure

- **[Complete OCI Tutorial →](/docs/iac/get-started/oci/)**
  Learn how to build more complex infrastructure on Oracle Cloud

- **[Browse Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)**
  Explore production-ready OCI examples

- **[Join the Community →](https://slack.pulumi.com)**
  Get help and share with 10,000+ developers

### Quick Tips

- Run `pulumi stack` to see your current stack details
- Run `pulumi destroy` to delete your bucket
- Run `pulumi config set` to configure stack settings
- View your deployments at [app.pulumi.com](https://app.pulumi.com)
