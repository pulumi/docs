
---
title: "Bucket"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a S3 bucket resource.

## Example Usage

### Private Bucket w/ Tags

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("b", {
    acl: "private",
    tags: {
        Environment: "Dev",
        Name: "My bucket",
    },
});
```

### Static Website Hosting

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const bucket = new aws.s3.Bucket("b", {
    acl: "public-read",
    policy: fs.readFileSync("policy.json", "utf-8"),
    website: {
        errorDocument: "error.html",
        indexDocument: "index.html",
        routingRules: `[{
    "Condition": {
        "KeyPrefixEquals": "docs/"
    },
    "Redirect": {
        "ReplaceKeyPrefixWith": "documents/"
    }
}]
`,
    },
});
```

### Using CORS

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("b", {
    acl: "public-read",
    corsRules: [{
        allowedHeaders: ["*"],
        allowedMethods: [
            "PUT",
            "POST",
        ],
        allowedOrigins: ["https://s3-website-test.mydomain.com"],
        exposeHeaders: ["ETag"],
        maxAgeSeconds: 3000,
    }],
});
```

### Using versioning

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("b", {
    acl: "private",
    versioning: {
        enabled: true,
    },
});
```

### Enable Logging

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const logBucket = new aws.s3.Bucket("log_bucket", {
    acl: "log-delivery-write",
});
const bucket = new aws.s3.Bucket("b", {
    acl: "private",
    loggings: [{
        targetBucket: logBucket.id,
        targetPrefix: "log/",
    }],
});
```

### Using object lifecycle

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
    lifecycleRules: [
        {
            enabled: true,
            expiration: {
                days: 90,
            },
            id: "log",
            prefix: "log/",
            tags: {
                autoclean: "true",
                rule: "log",
            },
            transitions: [
                {
                    days: 30,
                    storageClass: "STANDARD_IA", // or "ONEZONE_IA"
                },
                {
                    days: 60,
                    storageClass: "GLACIER",
                },
            ],
        },
        {
            enabled: true,
            expiration: {
                date: "2016-01-12",
            },
            id: "tmp",
            prefix: "tmp/",
        },
    ],
});
const versioningBucket = new aws.s3.Bucket("versioning_bucket", {
    acl: "private",
    lifecycleRules: [{
        enabled: true,
        noncurrentVersionExpiration: {
            days: 90,
        },
        noncurrentVersionTransitions: [
            {
                days: 30,
                storageClass: "STANDARD_IA",
            },
            {
                days: 60,
                storageClass: "GLACIER",
            },
        ],
        prefix: "config/",
    }],
    versioning: {
        enabled: true,
    },
});
```

### Using replication configuration

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const central = new aws.Provider("central", {
    region: "eu-central-1",
});
const replicationRole = new aws.iam.Role("replication", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const destination = new aws.s3.Bucket("destination", {
    region: "eu-west-1",
    versioning: {
        enabled: true,
    },
});
const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
    region: "eu-central-1",
    replicationConfiguration: {
        role: replicationRole.arn,
        rules: [{
            destination: {
                bucket: destination.arn,
                storageClass: "STANDARD",
            },
            id: "foobar",
            prefix: "foo",
            status: "Enabled",
        }],
    },
    versioning: {
        enabled: true,
    },
}, {provider: central});
const replicationPolicy = new aws.iam.Policy("replication", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetReplicationConfiguration",
        "s3:ListBucket"
      ],
      "Effect": "Allow",
      "Resource": [
        "${bucket.arn}"
      ]
    },
    {
      "Action": [
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl"
      ],
      "Effect": "Allow",
      "Resource": [
        "${bucket.arn}/*"
      ]
    },
    {
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete"
      ],
      "Effect": "Allow",
      "Resource": "${destination.arn}/*"
    }
  ]
}
`,
});
const replicationRolePolicyAttachment = new aws.iam.RolePolicyAttachment("replication", {
    policyArn: replicationPolicy.arn,
    role: replicationRole.name,
});
```

### Enable Default Server Side Encryption

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const mykey = new aws.kms.Key("mykey", {
    deletionWindowInDays: 10,
    description: "This key is used to encrypt bucket objects",
});
const mybucket = new aws.s3.Bucket("mybucket", {
    serverSideEncryptionConfiguration: {
        rule: {
            applyServerSideEncryptionByDefault: {
                kmsMasterKeyId: mykey.arn,
                sseAlgorithm: "aws:kms",
            },
        },
    },
});
```

### Using ACL policy grants

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const currentUser = aws.getCanonicalUserId();
const bucket = new aws.s3.Bucket("bucket", {
    grant: [
        {
            id: currentUser.id,
            permission: ["FULL_ACCESS"],
            type: "CanonicalUser",
        },
        {
            permission: [
                "READ",
                "WRITE",
            ],
            type: "Group",
            uri: "http://acs.amazonaws.com/groups/s3/LogDelivery",
        },
    ],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket.html.markdown.



## Create a Bucket Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#Bucket">Bucket</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketArgs">BucketArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Bucket</span><span class="p">(resource_name, opts=None, </span>acceleration_status=None<span class="p">, </span>acl=None<span class="p">, </span>arn=None<span class="p">, </span>bucket=None<span class="p">, </span>bucket_prefix=None<span class="p">, </span>cors_rules=None<span class="p">, </span>force_destroy=None<span class="p">, </span>grants=None<span class="p">, </span>hosted_zone_id=None<span class="p">, </span>lifecycle_rules=None<span class="p">, </span>loggings=None<span class="p">, </span>object_lock_configuration=None<span class="p">, </span>policy=None<span class="p">, </span>region=None<span class="p">, </span>replication_configuration=None<span class="p">, </span>request_payer=None<span class="p">, </span>server_side_encryption_configuration=None<span class="p">, </span>tags=None<span class="p">, </span>versioning=None<span class="p">, </span>website=None<span class="p">, </span>website_domain=None<span class="p">, </span>website_endpoint=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketArgs">BucketArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#Bucket">Bucket</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.Bucket.html">Bucket</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketArgs.html">BucketArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Bucket resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Cors<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Grant<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Logging<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Versioning<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Website<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">[]s3.<wbr>Bucket<wbr>Cors<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">[]s3.<wbr>Bucket<wbr>Grant</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">[]s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">[]s3.<wbr>Bucket<wbr>Logging</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">*s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">*s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">*s3.<wbr>Bucket<wbr>Versioning</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">*s3.<wbr>Bucket<wbr>Website</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>string | Canned<wbr>Acl</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">s3.<wbr>Bucket<wbr>Cors<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">s3.<wbr>Bucket<wbr>Grant[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">s3.<wbr>Bucket<wbr>Logging[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string | Policy<wbr>Document</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">s3.<wbr>Bucket<wbr>Versioning?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">s3.<wbr>Bucket<wbr>Website?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration_<wbr>status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List[Bucket<wbr>Grant]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List[Bucket<wbr>Logging]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>lock_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Dict[Bucket<wbr>Object<wbr>Lock<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Dict[Bucket<wbr>Replication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>payer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Bucket Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Cors<wbr>Rule&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Grant&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Logging&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Versioning</a></code>
            </td>
            <td class="align-top">{{% md %}} A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Website?</a></code>
            </td>
            <td class="align-top">{{% md %}} A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">[]s3.<wbr>Bucket<wbr>Cors<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">[]s3.<wbr>Bucket<wbr>Grant</a></code>
            </td>
            <td class="align-top">{{% md %}} An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">[]s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">[]s3.<wbr>Bucket<wbr>Logging</a></code>
            </td>
            <td class="align-top">{{% md %}} A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">*s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">*s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">s3.<wbr>Bucket<wbr>Versioning</a></code>
            </td>
            <td class="align-top">{{% md %}} A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">*s3.<wbr>Bucket<wbr>Website</a></code>
            </td>
            <td class="align-top">{{% md %}} A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">s3.<wbr>Bucket<wbr>Cors<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">s3.<wbr>Bucket<wbr>Grant[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">s3.<wbr>Bucket<wbr>Logging[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">s3.<wbr>Bucket<wbr>Versioning</a></code>
            </td>
            <td class="align-top">{{% md %}} A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">s3.<wbr>Bucket<wbr>Website?</a></code>
            </td>
            <td class="align-top">{{% md %}} A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration_<wbr>status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>regional_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List[Bucket<wbr>Grant]</a></code>
            </td>
            <td class="align-top">{{% md %}} An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List[Bucket<wbr>Logging]</a></code>
            </td>
            <td class="align-top">{{% md %}} A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>lock_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Dict[Bucket<wbr>Object<wbr>Lock<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Dict[Bucket<wbr>Replication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>payer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></code>
            </td>
            <td class="align-top">{{% md %}} A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></code>
            </td>
            <td class="align-top">{{% md %}} A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Bucket Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketState">BucketState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#Bucket">Bucket</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>acceleration_status=None<span class="p">, </span>acl=None<span class="p">, </span>arn=None<span class="p">, </span>bucket=None<span class="p">, </span>bucket_domain_name=None<span class="p">, </span>bucket_prefix=None<span class="p">, </span>bucket_regional_domain_name=None<span class="p">, </span>cors_rules=None<span class="p">, </span>force_destroy=None<span class="p">, </span>grants=None<span class="p">, </span>hosted_zone_id=None<span class="p">, </span>lifecycle_rules=None<span class="p">, </span>loggings=None<span class="p">, </span>object_lock_configuration=None<span class="p">, </span>policy=None<span class="p">, </span>region=None<span class="p">, </span>replication_configuration=None<span class="p">, </span>request_payer=None<span class="p">, </span>server_side_encryption_configuration=None<span class="p">, </span>tags=None<span class="p">, </span>versioning=None<span class="p">, </span>website=None<span class="p">, </span>website_domain=None<span class="p">, </span>website_endpoint=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketState">BucketState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#Bucket">Bucket</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.Bucket.html">Bucket</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketState.html">BucketState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Bucket resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Cors<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Grant<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Logging<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Versioning<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Website<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Acl</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">[]s3.<wbr>Bucket<wbr>Cors<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">[]s3.<wbr>Bucket<wbr>Grant</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">[]s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">[]s3.<wbr>Bucket<wbr>Logging</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">*s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Payer</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">*s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">*s3.<wbr>Bucket<wbr>Versioning</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">*s3.<wbr>Bucket<wbr>Website</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>string | Canned<wbr>Acl</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">s3.<wbr>Bucket<wbr>Cors<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">s3.<wbr>Bucket<wbr>Grant[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">s3.<wbr>Bucket<wbr>Logging[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Lock<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string | Policy<wbr>Document</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Payer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">s3.<wbr>Bucket<wbr>Versioning?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">s3.<wbr>Bucket<wbr>Website?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">acceleration_<wbr>status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">acl</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to &#34;private&#34;.  Conflicts with `grant`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>regional_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cors_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grants</td>
            <td class="align-top">
                
                <code><a href="#bucketgrant">List[Bucket<wbr>Grant]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An [ACL policy grant](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#sample-acl) (documented below). Conflicts with `acl`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket&#39;s region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">loggings</td>
            <td class="align-top">
                
                <code><a href="#bucketlogging">List[Bucket<wbr>Logging]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>lock_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfiguration">Dict[Bucket<wbr>Object<wbr>Lock<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfiguration">Dict[Bucket<wbr>Replication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>payer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfiguration">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">versioning</td>
            <td class="align-top">
                
                <code><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website</td>
            <td class="align-top">
                
                <code><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A website object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">website_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### BucketCorsRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketCorsRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketCorsRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketCorsRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketCorsRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketCorsRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketCorsRule.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allowed<wbr>Headers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies which headers are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which methods are allowed. Can be `GET`, `PUT`, `POST`, `DELETE` or `HEAD`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Origins</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which origins are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expose<wbr>Headers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies expose header in the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Age<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies time in seconds that browser can cache the response for a preflight request.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allowed<wbr>Headers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies which headers are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which methods are allowed. Can be `GET`, `PUT`, `POST`, `DELETE` or `HEAD`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Origins</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which origins are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expose<wbr>Headers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies expose header in the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Age<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies time in seconds that browser can cache the response for a preflight request.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allowed<wbr>Headers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies which headers are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which methods are allowed. Can be `GET`, `PUT`, `POST`, `DELETE` or `HEAD`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Origins</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which origins are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expose<wbr>Headers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies expose header in the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Age<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies time in seconds that browser can cache the response for a preflight request.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allowed<wbr>Headers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies which headers are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which methods are allowed. Can be `GET`, `PUT`, `POST`, `DELETE` or `HEAD`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Origins</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies which origins are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expose<wbr>Headers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies expose header in the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Age<wbr>Seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies time in seconds that browser can cache the response for a preflight request.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketGrant
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketGrant">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketGrant">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketGrantArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketGrantOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketGrantArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketGrant.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Permissions</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of permissions to apply for grantee. Valid values are `READ`, `WRITE`, `READ_ACP`, `WRITE_ACP`, `FULL_ACCESS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
- Type of grantee to apply for. Valid values are `CanonicalUser` and `Group`. `AmazonCustomerByEmail` is not supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Uri address to grant for. Used only when `type` is `Group`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Permissions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of permissions to apply for grantee. Valid values are `READ`, `WRITE`, `READ_ACP`, `WRITE_ACP`, `FULL_ACCESS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
- Type of grantee to apply for. Valid values are `CanonicalUser` and `Group`. `AmazonCustomerByEmail` is not supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Uri address to grant for. Used only when `type` is `Group`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">permissions</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of permissions to apply for grantee. Valid values are `READ`, `WRITE`, `READ_ACP`, `WRITE_ACP`, `FULL_ACCESS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
- Type of grantee to apply for. Valid values are `CanonicalUser` and `Group`. `AmazonCustomerByEmail` is not supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Uri address to grant for. Used only when `type` is `Group`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">permissions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of permissions to apply for grantee. Valid values are `READ`, `WRITE`, `READ_ACP`, `WRITE_ACP`, `FULL_ACCESS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
- Type of grantee to apply for. Valid values are `CanonicalUser` and `Group`. `AmazonCustomerByEmail` is not supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Uri address to grant for. Used only when `type` is `Group`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLifecycleRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLifecycleRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLifecycleRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRule.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Abort<wbr>Incomplete<wbr>Multipart<wbr>Upload<wbr>Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the number of days after initiating a multipart upload when the multipart upload must be completed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruleexpiration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Noncurrent<wbr>Version<wbr>Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversionexpiration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Expiration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Noncurrent<wbr>Version<wbr>Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversiontransition">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Transition<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruletransition">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Abort<wbr>Incomplete<wbr>Multipart<wbr>Upload<wbr>Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the number of days after initiating a multipart upload when the multipart upload must be completed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruleexpiration">*s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Noncurrent<wbr>Version<wbr>Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversionexpiration">*s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Expiration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Noncurrent<wbr>Version<wbr>Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversiontransition">[]s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Transition</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruletransition">[]s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">abort<wbr>Incomplete<wbr>Multipart<wbr>Upload<wbr>Days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the number of days after initiating a multipart upload when the multipart upload must be completed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruleexpiration">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">noncurrent<wbr>Version<wbr>Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversionexpiration">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Expiration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">noncurrent<wbr>Version<wbr>Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversiontransition">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Transition[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruletransition">s3.<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">abort<wbr>Incomplete<wbr>Multipart<wbr>Upload<wbr>Days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the number of days after initiating a multipart upload when the multipart upload must be completed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruleexpiration">Dict[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">noncurrent<wbr>Version<wbr>Expiration</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversionexpiration">Dict[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Expiration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions expire (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">noncurrent<wbr>Version<wbr>Transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecyclerulenoncurrentversiontransition">List[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Noncurrent<wbr>Version<wbr>Transition]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies when noncurrent object versions transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transitions</td>
            <td class="align-top">
                
                <code><a href="#bucketlifecycleruletransition">List[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a period in the object&#39;s transitions (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLifecycleRuleExpiration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLifecycleRuleExpiration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLifecycleRuleExpiration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleExpirationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleExpirationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleExpirationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleExpiration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expired<wbr>Object<wbr>Delete<wbr>Marker</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On a versioned bucket (versioning-enabled or versioning-suspended bucket), you can add this element in the lifecycle configuration to direct Amazon S3 to delete expired object delete markers.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expired<wbr>Object<wbr>Delete<wbr>Marker</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On a versioned bucket (versioning-enabled or versioning-suspended bucket), you can add this element in the lifecycle configuration to direct Amazon S3 to delete expired object delete markers.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expired<wbr>Object<wbr>Delete<wbr>Marker</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On a versioned bucket (versioning-enabled or versioning-suspended bucket), you can add this element in the lifecycle configuration to direct Amazon S3 to delete expired object delete markers.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expired<wbr>Object<wbr>Delete<wbr>Marker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On a versioned bucket (versioning-enabled or versioning-suspended bucket), you can add this element in the lifecycle configuration to direct Amazon S3 to delete expired object delete markers.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLifecycleRuleNoncurrentVersionExpiration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLifecycleRuleNoncurrentVersionExpiration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLifecycleRuleNoncurrentVersionExpiration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleNoncurrentVersionExpirationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleNoncurrentVersionExpirationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleNoncurrentVersionExpirationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleNoncurrentVersionExpiration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLifecycleRuleNoncurrentVersionTransition
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLifecycleRuleNoncurrentVersionTransition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLifecycleRuleNoncurrentVersionTransition">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleNoncurrentVersionTransitionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleNoncurrentVersionTransitionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleNoncurrentVersionTransitionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleNoncurrentVersionTransition.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLifecycleRuleTransition
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLifecycleRuleTransition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLifecycleRuleTransition">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleTransitionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLifecycleRuleTransitionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleTransitionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLifecycleRuleTransition.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the date after which you want the corresponding action to take effect.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketLogging
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketLogging">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketLogging">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLoggingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketLoggingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLoggingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketLogging.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Target<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that will receive the log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
To specify a key prefix for log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Target<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that will receive the log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
To specify a key prefix for log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">target<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that will receive the log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
To specify a key prefix for log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">target<wbr>Bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that will receive the log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
To specify a key prefix for log objects.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketObjectLockConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketObjectLockConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketObjectLockConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Enabled</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationrule">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Object<wbr>Lock<wbr>Enabled</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationrule">*s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">object<wbr>Lock<wbr>Enabled</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationrule">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">object<wbr>Lock<wbr>Enabled</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationrule">Dict[Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketObjectLockConfigurationRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketObjectLockConfigurationRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketObjectLockConfigurationRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfigurationRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfigurationRule.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Default<wbr>Retention</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationruledefaultretention">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule<wbr>Default<wbr>Retention<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default retention period that you want to apply to new objects placed in this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Default<wbr>Retention</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationruledefaultretention">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule<wbr>Default<wbr>Retention</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default retention period that you want to apply to new objects placed in this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">default<wbr>Retention</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationruledefaultretention">s3.<wbr>Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule<wbr>Default<wbr>Retention</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default retention period that you want to apply to new objects placed in this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">default<wbr>Retention</td>
            <td class="align-top">
                
                <code><a href="#bucketobjectlockconfigurationruledefaultretention">Dict[Bucket<wbr>Object<wbr>Lock<wbr>Configuration<wbr>Rule<wbr>Default<wbr>Retention]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default retention period that you want to apply to new objects placed in this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketObjectLockConfigurationRuleDefaultRetention
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketObjectLockConfigurationRuleDefaultRetention">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketObjectLockConfigurationRuleDefaultRetention">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationRuleDefaultRetentionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketObjectLockConfigurationRuleDefaultRetentionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfigurationRuleDefaultRetentionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketObjectLockConfigurationRuleDefaultRetention.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default Object Lock retention mode you want to apply to new objects placed in this bucket. Valid values are `GOVERNANCE` and `COMPLIANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Years</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of years that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default Object Lock retention mode you want to apply to new objects placed in this bucket. Valid values are `GOVERNANCE` and `COMPLIANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Years</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of years that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default Object Lock retention mode you want to apply to new objects placed in this bucket. Valid values are `GOVERNANCE` and `COMPLIANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">years</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of years that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default Object Lock retention mode you want to apply to new objects placed in this bucket. Valid values are `GOVERNANCE` and `COMPLIANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">years</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of years that you want to specify for the default retention period.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrule">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the rules managing the replication (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrule">[]s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the rules managing the replication (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrule">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the rules managing the replication (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrule">List[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the rules managing the replication (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRule.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestination">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the destination for the rule (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulefilter">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Filter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Filter that identifies subset of objects to which the replication rule applies (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority associated with the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Selection<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteria">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies special object selection criteria (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestination">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the destination for the rule (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulefilter">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Filter that identifies subset of objects to which the replication rule applies (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority associated with the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Selection<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteria">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies special object selection criteria (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestination">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the destination for the rule (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulefilter">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Filter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Filter that identifies subset of objects to which the replication rule applies (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority associated with the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Selection<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteria">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies special object selection criteria (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestination">Dict[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the destination for the rule (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulefilter">Dict[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Filter that identifies subset of objects to which the replication rule applies (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Canonical user id to grant for. Used only when `type` is `CanonicalUser`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority associated with the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Selection<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteria">Dict[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies special object selection criteria (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRuleDestination
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRuleDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRuleDestination">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleDestinationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleDestinationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleDestination.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Access<wbr>Control<wbr>Translation</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestinationaccesscontroltranslation">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination<wbr>Access<wbr>Control<wbr>Translation<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the overrides to use for object owners on replication. Must be used in conjunction with `account_id` owner override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replica<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with
`sse_kms_encrypted_objects` source selection criteria.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Access<wbr>Control<wbr>Translation</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestinationaccesscontroltranslation">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination<wbr>Access<wbr>Control<wbr>Translation</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the overrides to use for object owners on replication. Must be used in conjunction with `account_id` owner override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replica<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with
`sse_kms_encrypted_objects` source selection criteria.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">access<wbr>Control<wbr>Translation</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestinationaccesscontroltranslation">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination<wbr>Access<wbr>Control<wbr>Translation?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the overrides to use for object owners on replication. Must be used in conjunction with `account_id` owner override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replica<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with
`sse_kms_encrypted_objects` source selection criteria.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">access<wbr>Control<wbr>Translation</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationruledestinationaccesscontroltranslation">Dict[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Destination<wbr>Access<wbr>Control<wbr>Translation]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the overrides to use for object owners on replication. Must be used in conjunction with `account_id` owner override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replica<wbr>Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with
`sse_kms_encrypted_objects` source selection criteria.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRuleDestinationAccessControlTranslation
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRuleDestinationAccessControlTranslation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRuleDestinationAccessControlTranslation">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleDestinationAccessControlTranslationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleDestinationAccessControlTranslation.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The override value for the owner on replicated objects. Currently only `Destination` is supported.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The override value for the owner on replicated objects. Currently only `Destination` is supported.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The override value for the owner on replicated objects. Currently only `Destination` is supported.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The override value for the owner on replicated objects. Currently only `Destination` is supported.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRuleFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRuleFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRuleFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleFilterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleFilter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Object keyname prefix that identifies subset of objects to which the rule applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRuleSourceSelectionCriteria
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRuleSourceSelectionCriteria">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRuleSourceSelectionCriteria">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleSourceSelectionCriteriaOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleSourceSelectionCriteria.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Sse<wbr>Kms<wbr>Encrypted<wbr>Objects</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteriassekmsencryptedobjects">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria<wbr>Sse<wbr>Kms<wbr>Encrypted<wbr>Objects<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Match SSE-KMS encrypted objects (documented below). If specified, `replica_kms_key_id`
in `destination` must be specified as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Sse<wbr>Kms<wbr>Encrypted<wbr>Objects</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteriassekmsencryptedobjects">*s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria<wbr>Sse<wbr>Kms<wbr>Encrypted<wbr>Objects</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Match SSE-KMS encrypted objects (documented below). If specified, `replica_kms_key_id`
in `destination` must be specified as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">sse<wbr>Kms<wbr>Encrypted<wbr>Objects</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteriassekmsencryptedobjects">s3.<wbr>Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria<wbr>Sse<wbr>Kms<wbr>Encrypted<wbr>Objects?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Match SSE-KMS encrypted objects (documented below). If specified, `replica_kms_key_id`
in `destination` must be specified as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">sse<wbr>Kms<wbr>Encrypted<wbr>Objects</td>
            <td class="align-top">
                
                <code><a href="#bucketreplicationconfigurationrulesourceselectioncriteriassekmsencryptedobjects">Dict[Bucket<wbr>Replication<wbr>Configuration<wbr>Rule<wbr>Source<wbr>Selection<wbr>Criteria<wbr>Sse<wbr>Kms<wbr>Encrypted<wbr>Objects]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Match SSE-KMS encrypted objects (documented below). If specified, `replica_kms_key_id`
in `destination` must be specified as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketServerSideEncryptionConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketServerSideEncryptionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketServerSideEncryptionConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationrule">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationrule">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationrule">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationrule">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Object Lock rule in place for this bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketServerSideEncryptionConfigurationRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketServerSideEncryptionConfigurationRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketServerSideEncryptionConfigurationRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfigurationRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfigurationRule.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationruleapplyserversideencryptionbydefault">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule<wbr>Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A single object for setting server-side encryption by default. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationruleapplyserversideencryptionbydefault">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule<wbr>Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A single object for setting server-side encryption by default. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationruleapplyserversideencryptionbydefault">s3.<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule<wbr>Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A single object for setting server-side encryption by default. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default</td>
            <td class="align-top">
                
                <code><a href="#bucketserversideencryptionconfigurationruleapplyserversideencryptionbydefault">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Configuration<wbr>Rule<wbr>Apply<wbr>Server<wbr>Side<wbr>Encryption<wbr>By<wbr>Default]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A single object for setting server-side encryption by default. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Kms<wbr>Master<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sse<wbr>Algorithm</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Kms<wbr>Master<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sse<wbr>Algorithm</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">kms<wbr>Master<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sse<wbr>Algorithm</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">kms_<wbr>master_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sse<wbr>Algorithm</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketVersioning
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketVersioning">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketVersioning">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketVersioningArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketVersioningOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketVersioningArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketVersioning.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean which indicates if this criteria is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketWebsite
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketWebsite">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketWebsite">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketWebsiteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketWebsiteOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketWebsiteArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketWebsite.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Error<wbr>Document</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An absolute path to the document to return in case of a 4XX error.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Document</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redirect<wbr>All<wbr>Requests<wbr>To</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Rules</td>
            <td class="align-top">
                
                <code>Union&lt;string, Immutable<wbr>Array&lt;string&gt;&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Error<wbr>Document</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An absolute path to the document to return in case of a 4XX error.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Document</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redirect<wbr>All<wbr>Requests<wbr>To</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Rules</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">error<wbr>Document</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An absolute path to the document to return in case of a 4XX error.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index<wbr>Document</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redirect<wbr>All<wbr>Requests<wbr>To</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Rules</td>
            <td class="align-top">
                
                <code>string | Routing<wbr>Rule[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">error<wbr>Document</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An absolute path to the document to return in case of a 4XX error.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index<wbr>Document</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redirect<wbr>All<wbr>Requests<wbr>To</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Rules</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







