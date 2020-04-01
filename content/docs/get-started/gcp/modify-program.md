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

> You must enable the Google KMS API on the GCP console before proceeding. You can enable the API by going to the [KMS API Library](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com) page and clicking 'ENABLE'.

Replace the entire contents of {{< langfile >}} with the following:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v2/go/gcp/kms"
	"github.com/pulumi/pulumi-gcp/sdk/v2/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a KMS KeyRing and CryptoKey to use with the Bucket
		keyRing, err := kms.NewKeyRing(ctx, "my-keyring", &kms.KeyRingArgs{
			Location: pulumi.String("global"),
		})
		if err != nil {
			return err
		}
		cryptoKey, err := kms.NewCryptoKey(ctx, "my-cryptokey", &kms.CryptoKeyArgs{
			KeyRing:        keyRing.SelfLink,
			RotationPeriod: pulumi.String("100000s"),
		})
		if err != nil {
			return err
		}

		// Create a GCP resource (Storage Bucket) with customer-managed encryption key
		bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
			Encryption: storage.BucketEncryptionArgs{
				DefaultKmsKeyName: cryptoKey.SelfLink,
			},
		})
		if err != nil {
			return err
		}

		// Export the DNS name of the bucket
		ctx.Export("bucketName", bucket.Url)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Gcp = Pulumi.Gcp;

class MyStack : Stack
{
    public MyStack()
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
        this.BucketName = bucket.Url;
    }

    [Output]
    public Output<string> BucketName { get; set; }
}
```

{{% /choosable %}}

Next, we'll deploy the changes.

{{< get-started-stepper >}}
