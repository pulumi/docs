---
title: Modify the Program | GCP
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update Google Cloud (GCP) project from a Pulumi program.
weight: 8
menu:
  getstarted:
    parent: gcp
    identifier: gcp-modify-program

aliases: ["/docs/quickstart/gcp/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's update it to use our own encryption key instead of the default Google-managed one.

> You must enable the Google KMS API for your project on the GCP console before proceeding. You can enable the API by following this link: `https://console.cloud.google.com/security/kms/noaccess?project={your_project_id}`. Be sure to replace the `{your_project_id}` with your actual Google project ID.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Let's create a customer managed key and use that for encryption instead of the default Google-managed key.
const keyRing = new gcp.kms.KeyRing("my-keyring", {
    location: "global",
});

const cryptoKey = new gcp.kms.CryptoKey("my-cryptokey", {
    keyRing: keyRing.selfLink,
    rotationPeriod: "100000s",
});

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    encryption: {
        defaultKmsKeyName: cryptoKey.selfLink,
    }
});

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Let's create a customer managed key and use that for encryption instead of the default Google-managed key.
const keyRing = new gcp.kms.KeyRing("my-keyring", {
    location: "global",
});

const cryptoKey = new gcp.kms.CryptoKey("my-cryptokey", {
    keyRing: keyRing.selfLink,
    rotationPeriod: "100000s",
});

// Create a GCP resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    encryption: {
        defaultKmsKeyName: cryptoKey.selfLink,
    }
});

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

```python
import pulumi
from pulumi_gcp import storage, kms

# Create a KMS KeyRing and CryptoKey to use with the Bucket
keyRing = kms.KeyRing('my-keyring', location='global')
cryptoKey = kms.CryptoKey('my-cryptokey',
                          key_ring=keyRing.self_link,
                          rotation_period="100000s")

# Create a GCP resource (Storage Bucket) with customer-managed encryption key
bucket = storage.Bucket('my-bucket',
                        encryption={'defaultKmsKeyName': cryptoKey.self_link})

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
```

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms"
    "github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a KMS KeyRing and CryptoKey to use with the Bucket
        keyRing, err := kms.NewKeyRing(ctx, "my-keyring", &kms.KeyRingArgs{
            Location: "global",
        })
        if err != nil {
            return err
        }
        cryptoKey, err := kms.NewCryptoKey(ctx, "my-cryptokey", &kms.CryptoKeyArgs{
            KeyRing:        keyRing.SelfLink(),
            RotationPeriod: "100000s",
        })
        if err != nil {
            return err
        }

        // Create a GCP resource (Storage Bucket) with customer-managed encryption key
        bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
            Encryption: map[string]interface{}{
                "defaultKmsKeyName": cryptoKey.SelfLink(),
            },
        })
        if err != nil {
            return err
        }

        // Export the DNS name of the bucket
        ctx.Export("bucketName", bucket.Url())
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Gcp = Pulumi.Gcp;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() =>
        {
            // Let's create a customer managed key and use that for encryption
            // instead of the default Google-managed key.
            var keyRing = new Gcp.Kms.KeyRing("my-keyring", new Gcp.Kms.KeyRingArgs
            {
                Location = "global",
            });

            var cryptoKey = new Gcp.Kms.CryptoKey("my-cryptokey", new Gcp.Kms.CryptoKeyArgs
            {
                KeyRing = keyRing.SelfLink,
                RotationPeriod = "100000s",
            });

            // Create a GCP resource (Storage Bucket)
            var bucket = new Gcp.Storage.Bucket("my-bucket", new Gcp.Storage.BucketArgs
            {
                Encryption = new Gcp.Storage.Inputs.BucketEncryptionArgs
                {
                    DefaultKmsKeyName = cryptoKey.SelfLink,
                },
            });

            // Export the DNS name of the bucket
            return new Dictionary<string, object> {
                { "bucketName", bucket.Url },
            };
        });
    }
}
```

Next, we'll deploy the changes.

{{< get-started-stepper >}}
