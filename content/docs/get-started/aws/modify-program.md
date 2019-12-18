---
title: Modify the Program | AWS
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update an AWS project from a Pulumi program.
weight: 8
menu:
  getstarted:
    parent: aws
    identifier: aws-modify-program

aliases: ["/docs/quickstart/aws/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's enable encryption on our S3 bucket.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create a KMS Key for S3 server-side encryption
const key = new aws.kms.Key("my-key");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket", {
    serverSideEncryptionConfiguration: {
        rule: {
            applyServerSideEncryptionByDefault: {
                sseAlgorithm: "aws:kms",
                kmsMasterKeyId: key.id,
            }
        }
    }
});

// Export the name of the bucket
exports.bucketName = bucket.id;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create a KMS Key for S3 server-side encryption
const key = new aws.kms.Key("my-key");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket", {
    serverSideEncryptionConfiguration: {
        rule: {
            applyServerSideEncryptionByDefault: {
                sseAlgorithm: "aws:kms",
                kmsMasterKeyId: key.id,
            }
        }
    }
});

// Export the name of the bucket
export const bucketName = bucket.id;
```

```python
import pulumi
from pulumi_aws import kms, s3

# Create a KMS Key for S3 server-side encryption
key = kms.Key('my-key')

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket',
    server_side_encryption_configuration={
        'rule': {
            'apply_server_side_encryption_by_default': {
                'sse_algorithm': 'aws:kms',
                'kms_master_key_id': key.id
            }
        }
    })

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Aws = Pulumi.Aws;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() =>
        {
            // Create a KMS Key for S3 server-side encryption
            var key = new Aws.Kms.Key("my-key");

            // Create an AWS resource (S3 Bucket)
            var bucket = new Aws.S3.Bucket("my-bucket", new Aws.S3.BucketArgs
            {
                ServerSideEncryptionConfiguration = new Aws.S3.Inputs.BucketServerSideEncryptionConfigurationArgs
                {
                    Rule = new Aws.S3.Inputs.BucketServerSideEncryptionConfigurationRuleArgs
                    {
                        ApplyServerSideEncryptionByDefault = new Aws.S3.Inputs.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs
                        {
                            SseAlgorithm = "aws:kms",
                            KmsMasterKeyId = key.Id,
                        },
                    },
                },
            });

            // Export the name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name", bucket.Id },
            };
        });
    }
}
```

Our program now creates a KMS key and enables server-side encryption on the S3 bucket using the KMS key.

Next, we'll deploy the changes.

{{< get-started-stepper >}}
