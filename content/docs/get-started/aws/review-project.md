---
title: Review the New Project | AWS
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to a review a new AWS project.
weight: 6
menu:
  getstarted:
    parent: aws
    identifier: aws-review-project

aliases: ["/docs/quickstart/aws/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project.md" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config.md" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack.md" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose nogo csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
exports.bucketName = bucket.id;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
export const bucketName = bucket.id;
```

```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws.S3;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() => {
            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket");

            // Export the name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name" , bucket.Id },
            };
        });
    }
}
```

This Pulumi program creates an S3 bucket and exports the name of the bucket.

{{% lang python %}}

> *Note*: As a prerequisite, [install virtualenv](https://virtualenv.pypa.io/en/latest/installation/) to manage project requirements

For Python, before we deploy the stack, the following commands need to be run to create a virtual environment, activate it, and install dependencies:

Create a virtual environment:

```bash
$ python -m venv aws-env
```

Activate the environment in Linux and macOS:

```bash
$ source aws-env/bin/activate
```

Activate the environment in Windows:

```bat
 aws-env\Scripts\activate
```

Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}
