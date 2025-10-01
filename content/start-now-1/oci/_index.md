---
title: Get Started with Pulumi and Oracle Cloud
meta_desc: Create, deploy, and manage infrastructure on Oracle Cloud Infrastructure using Pulumi - unified guide with examples in multiple languages
type: page
layout: cloud-unified
no_on_this_page: true

cloud_name: Oracle Cloud
subtitle: Deploy your first Oracle Cloud resources in under 5 minutes
---

## Quick Setup

### 1. Sign up for Pulumi (Free)

Get started with Pulumi Cloud for free. Includes state management, secrets, and more.

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

### 2. Install Pulumi CLI

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}
Install with Homebrew:

```bash
brew install pulumi/tap/pulumi
```

Or download the [macOS installer](https://get.pulumi.com/releases/sdk/pulumi-latest-darwin-x64.pkg).

{{% /choosable %}}

{{% choosable os linux %}}
Install with curl:

```bash
curl -fsSL https://get.pulumi.com | sh
```

Or download a [Linux package](https://www.pulumi.com/docs/install/versions/).

{{% /choosable %}}

{{% choosable os windows %}}
Install with PowerShell:

```powershell
Invoke-WebRequest -Uri "https://get.pulumi.com/install.ps1" -OutFile install.ps1; .\install.ps1
```

Or download the [Windows installer](https://get.pulumi.com/releases/sdk/pulumi-latest-windows-x64.msi).

{{% /choosable %}}

Verify installation:

```bash
pulumi version
```

### 3. Configure Oracle Cloud Credentials

Configure your Oracle Cloud Infrastructure credentials using one of these methods:

#### Option 1: OCI CLI Configuration (Recommended)

First install and configure the OCI CLI:

```bash
# Install OCI CLI
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

# Configure OCI CLI with your credentials
oci setup config
```

This will prompt you for:

- User OCID
- Tenancy OCID
- Region
- Path to your API signing key

#### Option 2: Environment Variables

Set the required environment variables:

```bash
export OCI_TENANCY_OCID="ocid1.tenancy.oc1..xxxxx"
export OCI_USER_OCID="ocid1.user.oc1..xxxxx"
export OCI_FINGERPRINT="xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx"
export OCI_REGION="us-ashburn-1"
export OCI_PRIVATE_KEY_PATH="~/.oci/oci_api_key.pem"
```

Verify your configuration:

```bash
oci iam region list
```

### 4. Deploy Your First Resource

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
Create a new TypeScript project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-typescript
```

This creates a new Pulumi project with TypeScript configured for OCI.

Deploy your first resource by modifying `index.ts`:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as oci from "@pulumi/oci";

// Get the compartment OCID
const compartmentId = pulumi.config.require("compartmentId");

// Create a VCN (Virtual Cloud Network)
const vcn = new oci.core.Vcn("my-vcn", {
    compartmentId: compartmentId,
    cidrBlocks: ["10.0.0.0/16"],
    displayName: "my-vcn",
});

// Create an Object Storage bucket
const bucket = new oci.objectstorage.Bucket("my-bucket", {
    compartmentId: compartmentId,
    namespace: oci.objectstorage.getNamespaceOutput().namespace,
    name: "my-pulumi-bucket",
    accessType: "NoPublicAccess",
});

// Export the VCN and bucket information
export const vcnId = vcn.id;
export const bucketName = bucket.name;
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}
Create a new Python project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-python
```

This creates a new Pulumi project with Python configured for OCI.

Deploy your first resource by modifying `__main__.py`:

```python
import pulumi
import pulumi_oci as oci

# Get the compartment OCID
config = pulumi.Config()
compartment_id = config.require("compartmentId")

# Create a VCN (Virtual Cloud Network)
vcn = oci.core.Vcn("my-vcn",
    compartment_id=compartment_id,
    cidr_blocks=["10.0.0.0/16"],
    display_name="my-vcn"
)

# Get the namespace for Object Storage
namespace = oci.objectstorage.get_namespace()

# Create an Object Storage bucket
bucket = oci.objectstorage.Bucket("my-bucket",
    compartment_id=compartment_id,
    namespace=namespace.namespace,
    name="my-pulumi-bucket",
    access_type="NoPublicAccess"
)

# Export the VCN and bucket information
pulumi.export("vcnId", vcn.id)
pulumi.export("bucketName", bucket.name)
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language go %}}
Create a new Go project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-go
```

This creates a new Pulumi project with Go configured for OCI.

Deploy your first resource by modifying `main.go`:

```go
package main

import (
    "github.com/pulumi/pulumi-oci/sdk/v2/go/oci/core"
    "github.com/pulumi/pulumi-oci/sdk/v2/go/oci/objectstorage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Get the compartment OCID
        cfg := config.New(ctx, "")
        compartmentId := cfg.Require("compartmentId")

        // Create a VCN (Virtual Cloud Network)
        vcn, err := core.NewVcn(ctx, "my-vcn", &core.VcnArgs{
            CompartmentId: pulumi.String(compartmentId),
            CidrBlocks: pulumi.StringArray{
                pulumi.String("10.0.0.0/16"),
            },
            DisplayName: pulumi.String("my-vcn"),
        })
        if err != nil {
            return err
        }

        // Get the namespace for Object Storage
        namespace, err := objectstorage.GetNamespace(ctx, nil)
        if err != nil {
            return err
        }

        // Create an Object Storage bucket
        bucket, err := objectstorage.NewBucket(ctx, "my-bucket", &objectstorage.BucketArgs{
            CompartmentId: pulumi.String(compartmentId),
            Namespace:     pulumi.String(namespace.Namespace),
            Name:          pulumi.String("my-pulumi-bucket"),
            AccessType:    pulumi.String("NoPublicAccess"),
        })
        if err != nil {
            return err
        }

        // Export the VCN and bucket information
        ctx.Export("vcnId", vcn.ID())
        ctx.Export("bucketName", bucket.Name)

        return nil
    })
}
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language csharp %}}
Create a new C# project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-csharp
```

This creates a new Pulumi project with C# configured for OCI.

Deploy your first resource by modifying `Program.cs`:

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Oci.Core;
using Pulumi.Oci.ObjectStorage;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        // Get the compartment OCID
        var config = new Config();
        var compartmentId = config.Require("compartmentId");

        // Create a VCN (Virtual Cloud Network)
        var vcn = new Vcn("my-vcn", new VcnArgs
        {
            CompartmentId = compartmentId,
            CidrBlocks = { "10.0.0.0/16" },
            DisplayName = "my-vcn",
        });

        // Get the namespace for Object Storage
        var @namespace = GetNamespace.Invoke();

        // Create an Object Storage bucket
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            CompartmentId = compartmentId,
            Namespace = @namespace.Apply(ns => ns.Namespace),
            Name = "my-pulumi-bucket",
            AccessType = "NoPublicAccess",
        });

        // Export the VCN and bucket information
        this.VcnId = vcn.Id;
        this.BucketName = bucket.Name;
    }

    [Output]
    public Output<string> VcnId { get; set; }

    [Output]
    public Output<string> BucketName { get; set; }
}
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language java %}}
Create a new Java project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-java
```

This creates a new Pulumi project with Java configured for OCI.

Deploy your first resource by modifying `src/main/java/myproject/App.java`:

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.oci.core.Vcn;
import com.pulumi.oci.core.VcnArgs;
import com.pulumi.oci.objectstorage.Bucket;
import com.pulumi.oci.objectstorage.BucketArgs;
import com.pulumi.oci.objectstorage.ObjectstorageFunctions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Get the compartment OCID
        var config = ctx.config();
        var compartmentId = config.require("compartmentId");

        // Create a VCN (Virtual Cloud Network)
        var vcn = new Vcn("my-vcn", VcnArgs.builder()
            .compartmentId(compartmentId)
            .cidrBlocks("10.0.0.0/16")
            .displayName("my-vcn")
            .build());

        // Get the namespace for Object Storage
        var namespace = ObjectstorageFunctions.getNamespace();

        // Create an Object Storage bucket
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .compartmentId(compartmentId)
            .namespace(namespace.applyValue(ns -> ns.namespace()))
            .name("my-pulumi-bucket")
            .accessType("NoPublicAccess")
            .build());

        // Export the VCN and bucket information
        ctx.export("vcnId", vcn.id());
        ctx.export("bucketName", bucket.name());
    }
}
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language yaml %}}
Create a new YAML project:

```bash
mkdir oci-quickstart && cd oci-quickstart
pulumi new oci-yaml
```

This creates a new Pulumi project with YAML configured for OCI.

Deploy your first resource by modifying `Pulumi.yaml`:

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

resources:
  # Create a VCN (Virtual Cloud Network)
  my-vcn:
    type: oci:Core:Vcn
    properties:
      compartmentId: ${compartmentId}
      cidrBlocks:
        - 10.0.0.0/16
      displayName: my-vcn

  # Create an Object Storage bucket
  my-bucket:
    type: oci:ObjectStorage:Bucket
    properties:
      compartmentId: ${compartmentId}
      namespace: ${namespace.namespace}
      name: my-pulumi-bucket
      accessType: NoPublicAccess

outputs:
  # Export the VCN and bucket information
  vcnId: ${my-vcn.id}
  bucketName: ${my-bucket.name}
```

Set the compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

Deploy your infrastructure:

```bash
pulumi up
```

{{% /choosable %}}

## What's next?

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure

- [**Follow the complete OCI tutorial →**](/docs/iac/get-started/oci/)
  Learn how to build more complex infrastructure on Oracle Cloud

- [**Explore OCI examples →**](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
  Browse production-ready examples for common OCI architectures

- [**Learn Pulumi concepts →**](/docs/iac/concepts/)
  Understand stacks, state, configuration, and more

- [**Join the community →**](https://slack.pulumi.com)
  Get help and share knowledge with other Pulumi users
