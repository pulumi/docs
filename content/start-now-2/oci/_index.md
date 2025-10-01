---
title: Get Started with Pulumi and Oracle Cloud
meta_desc: Create, deploy, and manage infrastructure on Oracle Cloud Infrastructure using Pulumi - progressive guide with language-specific examples
type: page
layout: cloud-progressive
no_on_this_page: true

cloud_name: Oracle Cloud
subtitle: Choose your language and deploy Oracle Cloud infrastructure in minutes
---

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

## Get Started with TypeScript

Build Oracle Cloud infrastructure using familiar TypeScript syntax and tooling.

### Prerequisites

- **Node.js**: version 14 or later ([install](https://nodejs.org/))
- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-typescript
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml       # Project metadata
├── Pulumi.dev.yaml   # Stack configuration
├── index.ts          # Infrastructure code
├── package.json      # Node dependencies
└── tsconfig.json     # TypeScript config
```

##### 3. Define Infrastructure

Replace `index.ts` with:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as oci from "@pulumi/oci";

// Get configuration
const config = new pulumi.Config();
const compartmentId = config.require("compartmentId");

// Create a VCN (Virtual Cloud Network)
const vcn = new oci.core.Vcn("my-vcn", {
    compartmentId: compartmentId,
    cidrBlocks: ["10.0.0.0/16"],
    displayName: "my-vcn",
    dnsLabel: "myvcn",
});

// Create an Internet Gateway
const internetGateway = new oci.core.InternetGateway("my-internet-gateway", {
    compartmentId: compartmentId,
    vcnId: vcn.id,
    displayName: "my-internet-gateway",
    enabled: true,
});

// Create an Object Storage bucket
const namespace = oci.objectstorage.getNamespaceOutput();
const bucket = new oci.objectstorage.Bucket("my-bucket", {
    compartmentId: compartmentId,
    namespace: namespace.namespace,
    name: `my-pulumi-bucket-${Date.now()}`,
    accessType: "ObjectRead",
});

// Export the outputs
export const vcnId = vcn.id;
export const vcnCidrBlock = vcn.cidrBlocks[0];
export const bucketName = bucket.name;
export const bucketNamespace = bucket.namespace;
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

```bash
pulumi up
```

This command:

1. Shows a preview of resources to be created
2. Asks for your confirmation
3. Creates the VCN and bucket in OCI
4. Outputs the resource IDs

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI TypeScript Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI TypeScript Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn TypeScript with Pulumi →](/docs/iac/concepts/languages/javascript/)

{{% /choosable %}}

{{% choosable language python %}}

## Get Started with Python

Build Oracle Cloud infrastructure using familiar Python syntax and tooling.

### Prerequisites

- **Python**: version 3.8 or later ([install](https://www.python.org/))
- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-python
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml           # Project metadata
├── Pulumi.dev.yaml       # Stack configuration
├── __main__.py           # Infrastructure code
├── requirements.txt      # Python dependencies
└── venv/                 # Virtual environment
```

##### 3. Define Infrastructure

Replace `__main__.py` with:

```python
"""An Oracle Cloud Python Pulumi program"""

import pulumi
from pulumi import Config
import pulumi_oci as oci

# Get configuration
config = Config()
compartment_id = config.require("compartmentId")

# Create a VCN (Virtual Cloud Network)
vcn = oci.core.Vcn("my-vcn",
    compartment_id=compartment_id,
    cidr_blocks=["10.0.0.0/16"],
    display_name="my-vcn",
    dns_label="myvcn"
)

# Create an Internet Gateway
internet_gateway = oci.core.InternetGateway("my-internet-gateway",
    compartment_id=compartment_id,
    vcn_id=vcn.id,
    display_name="my-internet-gateway",
    enabled=True
)

# Get the namespace for Object Storage
namespace = oci.objectstorage.get_namespace()

# Create an Object Storage bucket
import time
bucket = oci.objectstorage.Bucket("my-bucket",
    compartment_id=compartment_id,
    namespace=namespace.namespace,
    name=f"my-pulumi-bucket-{int(time.time())}",
    access_type="ObjectRead"
)

# Export the outputs
pulumi.export("vcn_id", vcn.id)
pulumi.export("vcn_cidr_block", vcn.cidr_blocks[0])
pulumi.export("bucket_name", bucket.name)
pulumi.export("bucket_namespace", bucket.namespace)
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

```bash
pulumi up
```

This command:

1. Shows a preview of resources to be created
2. Asks for your confirmation
3. Creates the VCN and bucket in OCI
4. Outputs the resource IDs

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI Python Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI Python Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn Python with Pulumi →](/docs/iac/concepts/languages/python/)

{{% /choosable %}}

{{% choosable language go %}}

## Get Started with Go

Build Oracle Cloud infrastructure using Go's type safety and performance.

### Prerequisites

- **Go**: version 1.20 or later ([install](https://golang.org/))
- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-go
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml       # Project metadata
├── Pulumi.dev.yaml   # Stack configuration
├── main.go           # Infrastructure code
├── go.mod            # Go module file
└── go.sum            # Go dependencies
```

##### 3. Define Infrastructure

Replace `main.go` with:

```go
package main

import (
    "fmt"
    "time"

    "github.com/pulumi/pulumi-oci/sdk/v2/go/oci/core"
    "github.com/pulumi/pulumi-oci/sdk/v2/go/oci/objectstorage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Get configuration
        cfg := config.New(ctx, "")
        compartmentId := cfg.Require("compartmentId")

        // Create a VCN (Virtual Cloud Network)
        vcn, err := core.NewVcn(ctx, "my-vcn", &core.VcnArgs{
            CompartmentId: pulumi.String(compartmentId),
            CidrBlocks: pulumi.StringArray{
                pulumi.String("10.0.0.0/16"),
            },
            DisplayName: pulumi.String("my-vcn"),
            DnsLabel:    pulumi.String("myvcn"),
        })
        if err != nil {
            return err
        }

        // Create an Internet Gateway
        _, err = core.NewInternetGateway(ctx, "my-internet-gateway", &core.InternetGatewayArgs{
            CompartmentId: pulumi.String(compartmentId),
            VcnId:         vcn.ID(),
            DisplayName:   pulumi.String("my-internet-gateway"),
            Enabled:       pulumi.Bool(true),
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
        bucketName := fmt.Sprintf("my-pulumi-bucket-%d", time.Now().Unix())
        bucket, err := objectstorage.NewBucket(ctx, "my-bucket", &objectstorage.BucketArgs{
            CompartmentId: pulumi.String(compartmentId),
            Namespace:     pulumi.String(namespace.Namespace),
            Name:          pulumi.String(bucketName),
            AccessType:    pulumi.String("ObjectRead"),
        })
        if err != nil {
            return err
        }

        // Export the outputs
        ctx.Export("vcnId", vcn.ID())
        ctx.Export("vcnCidrBlock", vcn.CidrBlocks.Index(pulumi.Int(0)))
        ctx.Export("bucketName", bucket.Name)
        ctx.Export("bucketNamespace", bucket.Namespace)

        return nil
    })
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

```bash
pulumi up
```

This command:

1. Shows a preview of resources to be created
2. Asks for your confirmation
3. Creates the VCN and bucket in OCI
4. Outputs the resource IDs

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI Go Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI Go Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn Go with Pulumi →](/docs/iac/concepts/languages/go/)

{{% /choosable %}}

{{% choosable language csharp %}}

## Get Started with C\#

Build Oracle Cloud infrastructure using C# and .NET ecosystem.

### Prerequisites

- **.NET SDK**: version 6.0 or later ([install](https://dotnet.microsoft.com/))
- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-csharp
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml                # Project metadata
├── Pulumi.dev.yaml            # Stack configuration
├── Program.cs                 # Infrastructure code
├── pulumi-oci-quickstart.csproj  # .NET project file
```

##### 3. Define Infrastructure

Replace `Program.cs` with:

```csharp
using System;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Oci.Core;
using Pulumi.Oci.Core.Inputs;
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

        // Create a VCN (Virtual Cloud Network)
        var vcn = new Vcn("my-vcn", new VcnArgs
        {
            CompartmentId = compartmentId,
            CidrBlocks = new[] { "10.0.0.0/16" },
            DisplayName = "my-vcn",
            DnsLabel = "myvcn",
        });

        // Create an Internet Gateway
        var internetGateway = new InternetGateway("my-internet-gateway", new InternetGatewayArgs
        {
            CompartmentId = compartmentId,
            VcnId = vcn.Id,
            DisplayName = "my-internet-gateway",
            Enabled = true,
        });

        // Get the namespace for Object Storage
        var @namespace = GetNamespace.Invoke();

        // Create an Object Storage bucket
        var bucketName = $"my-pulumi-bucket-{DateTimeOffset.UtcNow.ToUnixTimeSeconds()}";
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            CompartmentId = compartmentId,
            Namespace = @namespace.Apply(ns => ns.Namespace),
            Name = bucketName,
            AccessType = "ObjectRead",
        });

        // Export the outputs
        this.VcnId = vcn.Id;
        this.VcnCidrBlock = vcn.CidrBlocks.GetAt(0);
        this.BucketName = bucket.Name;
        this.BucketNamespace = bucket.Namespace;
    }

    [Output]
    public Output<string> VcnId { get; set; }

    [Output]
    public Output<string> VcnCidrBlock { get; set; }

    [Output]
    public Output<string> BucketName { get; set; }

    [Output]
    public Output<string> BucketNamespace { get; set; }
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

```bash
pulumi up
```

This command:

1. Shows a preview of resources to be created
2. Asks for your confirmation
3. Creates the VCN and bucket in OCI
4. Outputs the resource IDs

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI C# Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI C# Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn C# with Pulumi →](/docs/iac/concepts/languages/dotnet/)

{{% /choosable %}}

{{% choosable language java %}}

## Get Started with Java

Build Oracle Cloud infrastructure using Java and familiar build tools.

### Prerequisites

- **Java**: version 11 or later ([install](https://www.oracle.com/java/))
- **Maven**: version 3.6.1 or later ([install](https://maven.apache.org/))
- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-java
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml                # Project metadata
├── Pulumi.dev.yaml            # Stack configuration
├── pom.xml                    # Maven configuration
└── src/
    └── main/
        └── java/
            └── myproject/
                └── App.java   # Infrastructure code
```

##### 3. Define Infrastructure

Replace `src/main/java/myproject/App.java` with:

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.oci.core.Vcn;
import com.pulumi.oci.core.VcnArgs;
import com.pulumi.oci.core.InternetGateway;
import com.pulumi.oci.core.InternetGatewayArgs;
import com.pulumi.oci.objectstorage.Bucket;
import com.pulumi.oci.objectstorage.BucketArgs;
import com.pulumi.oci.objectstorage.ObjectstorageFunctions;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Get configuration
        var config = ctx.config();
        var compartmentId = config.require("compartmentId");

        // Create a VCN (Virtual Cloud Network)
        var vcn = new Vcn("my-vcn", VcnArgs.builder()
            .compartmentId(compartmentId)
            .cidrBlocks("10.0.0.0/16")
            .displayName("my-vcn")
            .dnsLabel("myvcn")
            .build());

        // Create an Internet Gateway
        var internetGateway = new InternetGateway("my-internet-gateway", InternetGatewayArgs.builder()
            .compartmentId(compartmentId)
            .vcnId(vcn.id())
            .displayName("my-internet-gateway")
            .enabled(true)
            .build());

        // Get the namespace for Object Storage
        var namespace = ObjectstorageFunctions.getNamespace();

        // Create an Object Storage bucket
        var bucketName = "my-pulumi-bucket-" + System.currentTimeMillis();
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .compartmentId(compartmentId)
            .namespace(namespace.applyValue(ns -> ns.namespace()))
            .name(bucketName)
            .accessType("ObjectRead")
            .build());

        // Export the outputs
        ctx.export("vcnId", vcn.id());
        ctx.export("vcnCidrBlock", vcn.cidrBlocks().applyValue(blocks -> blocks.get(0)));
        ctx.export("bucketName", bucket.name());
        ctx.export("bucketNamespace", bucket.namespace());
    }
}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

```bash
pulumi up
```

This command:

1. Shows a preview of resources to be created
2. Asks for your confirmation
3. Creates the VCN and bucket in OCI
4. Outputs the resource IDs

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI Java Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI Java Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn Java with Pulumi →](/docs/iac/concepts/languages/java/)

{{% /choosable %}}

{{% choosable language yaml %}}

## Get Started with YAML

Define Oracle Cloud infrastructure using simple, declarative YAML configuration.

### Prerequisites

- **Oracle Cloud account**: [Sign up for free tier](https://signup.cloud.oracle.com/)
- **OCI credentials**: configured locally

### Quick Start

#### 1. Sign up for Pulumi Cloud (Free)

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

Pulumi Cloud provides free state management, secrets encryption, and deployment history.

#### 2. Install Pulumi

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

#### 3. Configure OCI Access

##### 1. Install OCI CLI

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

##### 2. Configure Credentials

```bash
oci setup config
```

This will prompt for:

- User OCID: `ocid1.user.oc1..xxxxx`
- Tenancy OCID: `ocid1.tenancy.oc1..xxxxx`
- Region: `us-ashburn-1`
- Path to your API signing key

Verify:

```bash
oci iam region list
```

#### 4. Create Your First Project

##### 1. New Project

```bash
mkdir pulumi-oci-quickstart
cd pulumi-oci-quickstart
pulumi new oci-yaml
```

##### 2. Project Structure

```
pulumi-oci-quickstart/
├── Pulumi.yaml       # Project and resource definitions
└── Pulumi.dev.yaml   # Stack configuration
```

##### 3. Define Infrastructure

Your project includes example YAML to create OCI resources:

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
  # Create a VCN (Virtual Cloud Network)
  my-vcn:
    type: oci:Core:Vcn
    properties:
      compartmentId: ${compartmentId}
      cidrBlocks:
        - 10.0.0.0/16
      displayName: my-vcn
      dnsLabel: myvcn

  # Create an Internet Gateway
  my-internet-gateway:
    type: oci:Core:InternetGateway
    properties:
      compartmentId: ${compartmentId}
      vcnId: ${my-vcn.id}
      displayName: my-internet-gateway
      enabled: true

  # Create an Object Storage bucket
  my-bucket:
    type: oci:ObjectStorage:Bucket
    properties:
      compartmentId: ${compartmentId}
      namespace: ${namespace.namespace}
      name: my-pulumi-bucket-${timestamp.unix}
      accessType: ObjectRead

outputs:
  # Export the VCN and bucket information
  vcnId: ${my-vcn.id}
  vcnCidrBlock: ${my-vcn.cidrBlocks[0]}
  bucketName: ${my-bucket.name}
  bucketNamespace: ${my-bucket.namespace}
```

Set your compartment ID:

```bash
pulumi config set compartmentId <your-compartment-ocid>
```

##### 4. Deploy Infrastructure

Deploy it:

```bash
pulumi up
```

### Next steps

- [**View your stack in Pulumi Cloud →**](https://app.pulumi.com/stacks)
  Explore resource details, deployment history, and manage your infrastructure
- [Complete OCI YAML Tutorial →](/docs/iac/get-started/oci/)
- [Browse OCI YAML Examples →](https://github.com/pulumi/examples#oracle-cloud-infrastructure)
- [Learn Pulumi YAML Concepts →](/docs/iac/concepts/languages/yaml/)

{{% /choosable %}}
