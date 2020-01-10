---
title: Review the New Project | GCP
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new GCP project.
weight: 6
menu:
  getstarted:
    parent: gcp
    identifier: gcp-review-project

aliases: ["/docs/quickstart/gcp/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project.md" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config.md" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack.md" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose nogo csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket");

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

```python
import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket')

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Gcp.Storage;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() =>
        {
            // Create a GCP resource (Storage Bucket)
            var bucket = new Storage.Bucket("my-bucket");

            // Export the DNS name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name", bucket.Url },
            };
        });
    }
}
```

This Pulumi program creates a storage bucket and exports the bucket URL.

{{% lang python %}}

> *Note*: As a prerequisite, [install virtualenv](https://virtualenv.pypa.io/en/latest/installation/) to manage project requirements

For Python, before we deploy the stack, the following commands need to be run to create a virtual environment, activate it, and install dependencies:

Create a virtual environment:

```bash
$ python3 -m venv venv
```

Activate the environment in Linux and MacOS:

```bash
$ source venv/bin/activate
```

Activate the environment in Windows:

```bat
> venv\Scripts\activate
```

Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}
