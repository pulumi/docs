---
title: Modify the Program
weight: 8
menu:
  quickstart:
    parent: gcp
    identifier: gcp-modify-program
---

Now that we have an instance of our Pulumi program deployed, let's update it to use our own encryption key instead of the default Google-managed one.

> You must enable the Google KMS API for your project on the GCP console before proceeding. You can enable the API by following this link: `https://console.cloud.google.com/security/kms/noaccess?project={your_project_id}`. Be sure to replace the `{your_project_id}` with your actual Google project ID.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo >}}

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

Next, we'll deploy the changes.

{{< get-started-stepper >}}
