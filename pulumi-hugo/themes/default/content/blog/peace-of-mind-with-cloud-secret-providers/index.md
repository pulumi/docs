---
title: "Peace of Mind with Cloud Secret Providers"

date: 2020-05-07
draft: false
meta_desc: "Encrypt your Pulumi secrets with a cloud secrets provider"
meta_image: secrets.png
authors:
    - lee-briggs
tags:
    - features
    - security
---

The secrets in your infrastructure are a vital part of your security model, and provisioning infrastructure is an inherently privileged process. [Previously]({{< relref "/blog/managing-secrets-with-pulumi" >}}) we introduced secret encryption and started encrypting secret configuration values inside the Pulumi state so that users could be confident their passwords, tokens, and other secret values were viewable only by them while managing their infrastructure.
Our first iteration of the encryption used either a passphrase for encrypting the secret or encryption via the Pulumi service backend. However, these options didn't meet the needs of our users who needed more control over their data.
That's why we also added support for "Cloud Secret Providers," giving users full confidence that their sensitive values are for their eyes only.

<!--more-->

Pulumi supports encryption via the [Pulumi service]({{< relref "/docs/intro/concepts/config#configuring-secrets-encryption" >}}), [AWS KMS](https://aws.amazon.com/kms/), [Azure KeyVault](https://azure.microsoft.com/en-us/services/key-vault/), [Google Cloud KMS](https://cloud.google.com/kms) and [HashiCorp Vault](https://www.vaultproject.io/). This post shows you _one_ example of using a cloud secret provider in a Pulumi stack using AWS KMS.

## Create a KMS Key

First, create a KMS key. We also can set an alias on the key to make it easier to reference later:
{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a new KMS key
const key = new aws.kms.Key("stack-encryption-key", {
    deletionWindowInDays: 10,
    description: "KMS key for encrypting Pulumi secret values",
});

// Create a new alias to the key
const alias = new aws.kms.Alias("alias/stack-encryption-key", {
    targetKeyId: key.keyId,
});

// Export the arns
export const keyArn = key.arn
export const aliasArn = alias.arn
```

{{% /choosable %}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

// Create a nw KMS Key
const key = new aws.kms.Key("stack-encryption-key", {
        deletionWindowInDays: 10,
        description: "KMS key for encrypting Pulumi secret values"
});


// Create an alias to the key
const alias = new aws.kms.Alias("alias/stack-encryption-key", {
    targetKeyId: key.keyId
});


// Export the arns
exports.keyArn = key.arn;
exports.aliasArn = alias.arn;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import kms

# Create a new KMS key
key = kms.Key("stack-encryption-key",
    deletion_window_in_days=10,
    description="KMS key for encrypting Pulumi secret values"
)

// Create an alias to the key
alias = kms.Alias("alias/stack-encryption-key",
    target_key_id=key.key_id
)

# Export the arns
pulumi.export('key_arn',  key.arn)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/kms"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create a new KMS key
		key, err := kms.NewKey(ctx, "stack-encryption-key", &kms.KeyArgs{
			Description: pulumi.String("KMS key for encrypting Pulumi secret values"),
			DeletionWindowInDays: pulumi.Int(10),
		})
		if err != nil {
			return err
		}

		// Create an alias to the key
		alias, err := kms.NewAlias(ctx, "alias/stack-encryption-key", &kms.AliasArgs{
			TargetKeyId: key.KeyId,
		})
		if err != nil {
			return err
		}

		// Export the arns
		ctx.Export("keyArn", key.Arn)
		ctx.Export("keyAlias", alias.Arn)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Kms = Pulumi.Aws.Kms;

class KeyStack : Stack
{
    public KeyStack()
    {
        // Create a new KMS key
        var key = new Kms.Key("stack-encryption-key", new Kms.KeyArgs
        {
            DeletionWindowInDays = 10,
            Description = "KMS key for encrypting Pulumi secret values"
        });

        // Create a new alias to the key
        var alias = new Kms.Alias("alias/stack-encryption-key", new Kms.AliasArgs
        {
            TargetKeyId = key.KeyId
        });

        this.KeyArn = key.Arn;
        this.AliasArn = alias.Arn;
    }

    [Output("keyArn")] public Output<string> KeyArn { get; set; }
    [Output("aliasArn")] public Output<string> AliasArn { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

Creating the key is enough to allow us to start using it for our encryption provider. However, we need to consider who has access to the key before we start encrypting our sensitive values with it in our Pulumi programs.

## Scoping Permission to our Key

Generally, in AWS, you scope access to resources using IAM roles. However, for sensitive values like KMS keys, IAM roles alone aren't enough to provide the security you might need. As an example, if someone in your AWS account has an IAM role with the following policy attached:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1588215924595",
      "Action": "kms:*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

That user gets access to every KMS key in your account, which would also mean they could decrypt any secret in your Pulumi stack.

To rectify this, we need to attach a Key Policy to the key. We can do this by updating our previous code:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const iamRole = config.require("iamRole");
const accountID = config.require("accountID");


const keyPolicy = {
    Version: "2012-10-17",
    Id: "policy",
    Statement: [
        // This statement allows all users to view the key in the console
        {
            Sid: "AllowGetKeys",
            Effect: "Allow",
            Action: ["kms:Describe*", "kms:Get*", "kms:List*"],
            Principal: {
                "AWS": [`arn:aws:iam::${accountID}:root`]
            },
            Resource: "*",
        },
        // This is a configurable statement that we can use to allow access to an IAM arn
        {
            Sid: "AllowIAMUserAccessKeys",
            Effect: "Allow",
            Action: ["kms:*"],
            Principal: {
                "AWS": iamRole,
            },
            Resource: "*",
        }
    ]
}

// Create a new KMS key
const key = new aws.kms.Key("stack-encryption-key", {
    deletionWindowInDays: 10,
    description: "KMS key for encrypting Pulumi secret values",
    policy: JSON.stringify(keyPolicy),
});

// Create a new alias to the key
const alias = new aws.kms.Alias("alias/stack-encryption-key", {
    targetKeyId: key.keyId,
});

// Export the arns
export const keyArn = key.arn
export const aliasArn = alias.arn

```

{{% /choosable %}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

let config = new pulumi.Config();
let iamRole = config.require("iamRole");
let accountID = config.require("accountID");

const keyPolicy = {
    Version: "2012-10-17",
    Id: "policy",
    Statement: [
        // This statement allows all users to view the key in the console
        {
            Sid: "AllowGetKeys",
            Effect: "Allow",
            Action: ["kms:Describe*", "kms:Get*", "kms:List*"],
            Principal: {
                "AWS": [`arn:aws:iam::${accountID}:root`]
            },
            Resource: "*",
        },
        // This is a configurable statement that we can use to allow access to an IAM arn
        {
            Sid: "AllowIAMUserAccessKeys",
            Effect: "Allow",
            Action: ["kms:*"],
            Principal: {
                "AWS": iamRole,
            },
            Resource: "*",
        }
    ]
}

// Create a nw KMS Key
const key = new aws.kms.Key("stack-encryption-key", {
        deletionWindowInDays: 10,
        description: "KMS key for encrypting Pulumi secret values",
        policy: JSON.stringify(keyPolicy),
});


// Create an alias to the key
const alias = new aws.kms.Alias("alias/stack-encryption-key", {
    targetKeyId: key.keyId
});


// Export the arns
exports.keyArn = key.arn;
exports.aliasArn = alias.arn;

});


// Export the arns
exports.keyArn = key.arn;
exports.aliasArn = alias.arn;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import json
from pulumi_aws import kms

config = pulumi.Config()
iam_role = config.require("iamRole")
account_id = config.require("accountID")


key_policy = {
    "Version": "2012-10-17",
    "Id": "policy",
    "Statement": [
        # This statement allows all users to view the key in the console
        {
            "Sid": "AllowGetKeys",
            "Effect": "Allow",
            "Action": ["kms:Describe*", "kms:Get*", "kms:List*"],
            "Principal": {
                "AWS": ["arn:aws:iam::{}:root".format(account_id)]
            },
            "Resource": "*",
        },
        # This is a configurable statement that we can use to allow access to an IAM arn
        {
            "Sid": "AllowIAMUserAccessKeys",
            "Effect": "Allow",
            "Action": ["kms:*"],
            "Principal": {
                "AWS": iam_role,
            },
            "Resource": "*",
        }
    ]
}
# Create an AWS KMS key
key = kms.Key("stack-encryption-key",
    deletion_window_in_days=10,
    description="KMS key for encrypting Pulumi secret values",
    policy=json.dumps(key_policy)
)

alias = kms.Alias("alias/stack-encryption-key",
    target_key_id=key.key_id
)

# Export the name of the bucket
pulumi.export('key_arn',  key.arn)
pulumi.export('alias_arn', alias.arn)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/kms"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

func main() {

	type Principal struct {
		AWS string `json:"AWS"`
	}
	type Statement struct {
		Sid       string    `json:"Sid"`
		Effect    string    `json:"Effect"`
		Principal Principal `json:"Principal"`
		Action    []string  `json:"Action"`
		Resource  string    `json:"Resource"`
	}

	type KeyPolicy struct {
		Version    string      `json:"Version"`
		ID         string      `json:"Id"`
		Statements []Statement `json:"Statement"`
	}

	pulumi.Run(func(ctx *pulumi.Context) error {

		config := config.New(ctx, "")

		iamRole := config.Require("iamRole")
		accountID := config.Require("accountID")

		rootIamRole := fmt.Sprintf("arn:aws:iam::%s:root", accountID)

		rawKeyPolicy := &KeyPolicy{
			Version: "2012-10-17",
			ID:      "policy",
			Statements: []Statement{
				{
					Sid:    "AllowGetKeys",
					Effect: "Allow",
					Action: []string{
						"kms:Describe*", "kms:Get*", "kms:List*",
					},
					Resource: "*",
					Principal: Principal{
						AWS: rootIamRole,
					},
				},
				{
					Sid:      "AllowIAMUserAccessKeys",
					Effect:   "Allow",
					Action:   []string{"kms:*"},
					Resource: "*",
					Principal: Principal{
						AWS: iamRole,
					},
				},
			},
		}

		keyPolicy, err := json.Marshal(rawKeyPolicy)

		if err != nil {
			panic("Error formatting keypolicy")
		}

		// Create an AWS KMS key
		key, err := kms.NewKey(ctx, "stack-encryption-key", &kms.KeyArgs{
			Description:          pulumi.String("KMS key for encrypting Pulumi secret values"),
			DeletionWindowInDays: pulumi.Int(10),
			Policy:               pulumi.String(string(keyPolicy)),
		})
		if err != nil {
			return err
		}

		// Create an alias to the key
		alias, err := kms.NewAlias(ctx, "alias/stack-encryption-key", &kms.AliasArgs{
			TargetKeyId: key.KeyId,
		})
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("keyArn", key.Arn)
		ctx.Export("keyAlias", alias.Arn)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Kms = Pulumi.Aws.Kms;

class KeyStack : Stack
{
    public KeyStack()
    {
        var config = new Config();
        var iamRole = config.Require("iamRole");
        var accountID = config.Require("accountID");

        var keyPolicy = $@"{{
            ""Version"": ""2012-10-17"",
            ""Id"": ""policy"",
            ""Statement"": [
            {{
                ""Sid"": ""AllowGetKeys"",
                ""Effect"": ""Allow"",
                ""Action"": [""kms:Describe*"", ""kms:Get*"", ""kms:List*""],
                ""Principal"": {{
                    ""AWS"": [""arn:aws:iam::{accountID}:root""]
                }},
                ""Resource"": ""*""
            }},
            {{
                ""Sid"": ""AllowIAMUserAccessKeys"",
                ""Effect"": ""Allow"",
                ""Action"": [""kms:*""],
                ""Principal"": {{
                    ""AWS"": ""{iamRole}""
                }},
                ""Resource"": ""*""
            }}
            ]
        }}";

        // Create a new KMS key
        var key = new Kms.Key("stack-encryption-key", new Kms.KeyArgs
        {
            DeletionWindowInDays = 10,
            Description = "KMS key for encrypting Pulumi secret values",
            Policy = keyPolicy
        });

        // Create a new alias to the key
        var alias = new Kms.Alias("alias/stack-encryption-key", new Kms.AliasArgs
        {
            TargetKeyId = key.KeyId
        });

        this.KeyArn = key.Arn;
        this.AliasArn = alias.Arn;
    }

    [Output("keyArn")] public Output<string> KeyArn { get; set; }
    [Output("aliasArn")] public Output<string> AliasArn { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

In this example, we've created a key policy which allows full access to a defined IAM role, and we've also given _read_ permissions to the key to everyone in this AWS account. We've made the IAM role configurable, so let's set the IAM role now so we can be sure we can use this key for our next Pulumi stack:

```bash
# Get the current AWS account ID and set it as a config variable
aws sts get-caller-identity | jq .Account -r | pulumi config set accountID
# Get the current IAM role we're using as set it as a config variable
aws sts get-caller-identity | jq .Arn -r | pulumi config set iamRole
```

## Initialize a New Stack

Now our key has been created and is adequately scoped; we can create a new stack and use the `secrets-provider` flag on creation to specify the KMS key to encrypt our secrets.

```bash
# We need to first retrieve the stack encryption key from our previous stack
KEY_ALIAS=$(pulumi stack output aliasArn | cut -d/ -f2)
# Note, we need to set the region we're deploying to
pulumi new aws-<language> -n <projectname> -s <stackname> -d "An example stack encrypted with AWS KMS" --secrets-provider="awskms://alias/${KEY_ALIAS}?region=us-west-2" --config aws:region=us-west-2 --dir $HOME/git/new-stack
```

You can check inside your `Pulumi.<stackname>.yaml` for which key you're using to encrypt your secrets:

```yaml
secretsprovider: awskms://alias/<stack-encryption-key-alias>?region=us-west-2
encryptedkey: AQICAHjqW3rb5Hw5Vpxi0c1sayz52VXj7yn20WVwsVILJSBU8wFDjvGuox3wDCJX99TxZFzAAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMWNeFRZIg8kVXMxrUAgEQgDtz6zV0aqegeAbmaQUNllMp8PQJa1qbjBH813I/XH6LbfynxZO9NE3sYPG89G0u/ltYsADiUAFS0bnadQ==
config:
  aws:region: us-west-2
```

It's worth noting here that the "encryptedkey" field here is an encrypted version of the data key in AWS KMS. You can read more about this [here](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys).

## Use your Encrypted Secret

Now we've initialized our stack we can add a secret configuration value using the secret flag and see the encrypted config value in the stack configuration:

```bash
pulumi config set --secret supersecret correct-horse-battery-stable
```

## Verify the encryption

To verify that the secret is indeed only accessible to the KMS key we created earlier, we can remove access to the key temporarily and try to perform a Pulumi operation. There are a few ways to remove your access, but first, let's use the secret in our stack:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
export const superSecret = config.requireSecret("supersecret");
```

{{% /choosable %}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const config = new pulumi.Config();
exports.superSecret = config.requireSecret("supersecret");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
config = pulumi.Config()

pulumi.export('superSecret',  config.require_secret("supersecret"))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		config := config.New(ctx, "")
		superSecret := config.RequireSecret("supersecret")

		ctx.Export("superSecret", pulumi.Sprintf("%s", superSecret))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

class AnotherStack : Stack
{
    public AnotherStack()
    {
        var config = new Config();
        this.SuperSecret = config.RequireSecret("supersecret");
    }

    [Output("superSecret")] public Output<string> SuperSecret { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

Now we need to verify if the value is _actually_ encrypted. An easy way to do that is to try and export the secret value without access to the key. How this is done depends on your AWS configuration, however in my setup, I use the `AWS_PROFILE` environment variable which refers to a [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) to configure access to AWS. If I unset this environment variable, I will no longer be using the AWS credentials that have access to this KMS key. Let's unset the AWS_PROFILE environment variable and then rerun `pulumi up`:

```bash
unset AWS_PROFILE
pulumi up
error: getting secrets manager: secrets (code=Unknown): InvalidSignatureException: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.
	status code: 400, request id: 9cf7508d-a7d5-40bb-b40f-98f68e82ac74
```

Excellent! We can't read these values without access to this KMS key. We can be safe in the knowledge our secret values are only readable by us.

## Examine the Pulumi State

The final part is to make sure our values are stored encrypted inside the Pulumi state. To do this, we need to use our secret value from earlier and use it in a resource. Let's create an s3 bucket, and write out super secret value to a file in the bucket. Update the Pulumi program you used before like so:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();

const superSecret = config.requireSecret("supersecret");

// Create a private bucket
const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
});

// Create an object from the secret value
const superSecretObject = new aws.s3.BucketObject("secret", {
    bucket: bucket.id,
    key: "secret",
    content: superSecret, // use our secret value as the content
})
```

{{% /choosable %}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

const config = new pulumi.Config();

const superSecret = config.requireSecret("supersecret");

// Create a private bucket
const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
});

const superSecretObject = new aws.s3.BucketObject("secret", {
    bucket: bucket.id,
    key: "secret",
    content: superSecret, // use our secret value as the content
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3

config = pulumi.Config()

superSecret = config.require_secret("supersecret")

# Create a private bucket
bucket = s3.Bucket('bucket', acl="private")

# Create an object from the secret value
bucketObject = s3.BucketObject("secret", bucket=bucket.id, key="secret", content=superSecret)
```

{{% /choosable %}}

{{% choosable language go %}}

```go

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		config := config.New(ctx, "")

		superSecret := config.RequireSecret("supersecret")

		// Create a a private bucket
		bucket, err := s3.NewBucket(ctx, "bucket", &s3.BucketArgs{Acl: pulumi.String("private")})
		if err != nil {
			return err
		}

		_, err = s3.NewBucketObject(ctx, "secret", &s3.BucketObjectArgs{
			Bucket:  bucket.ID(),
			Key:     pulumi.String("secret"),
			Content: pulumi.Sprintf("%s", superSecret),
		})

		ctx.Export("superSecret", pulumi.String(superSecret))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;

class AnotherStack : Stack
{
    public AnotherStack()
    {
        var config = new Config();
        this.SuperSecret = config.RequireSecret("supersecret");

        var bucket = new Bucket("bucket", new BucketArgs {
            Acl = "private",
        });

        var bucketObject = new BucketObject("secret", new BucketObjectArgs {
            Bucket = bucket.Id,
            Key = "secret",
            Content = SuperSecret

        });
    }
    [Output("superSecret")] public Output<string> SuperSecret { get; set; }
}

```

{{% /choosable %}}

{{< /chooser >}}

We now need to look inside our Pulumi statefile to verify the value is encoded there. We can do this with `pulumi stack export` and some JSON manipulation magic using [jq](https://stedolan.github.io/jq/):

```bash
pulumi stack export | jq '.deployment.resources[].outputs | select(.content).content'
```

The result should look like this:

```json
{
  "4dabf18193072939515e22adb298388d": "1b47061264138c4ac30d75fd1eb44270",
  "ciphertext": "v1:cQ5qr21hTdb2PTM5:ZwEW8pN1kC6fUlppi1eS84D/lodoe54wV2dgEsqu0csu2VyTQg0wTf8Qv7axCQ=="
}
```

## Wrap up

This example showed how to use client-side encryption with AWS KMS. Pulumi, as mentioned before, has support for Azure KeyVault, Google Cloud KMS, and HashiCorp Vault for storing your keys. You can find examples of how to use these encryption methods in our [examples repo](https://github.com/pulumi/examples/tree/master/secrets-provider) and take a look at our [secrets provider documentation]({{< relref "/docs/intro/concepts/config#available-encryption-providers" >}}).

We hope your next compliance audit is more relaxed with this feature available!
