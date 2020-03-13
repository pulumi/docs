
---
title: "BucketPublicAccessBlock"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleBucket = new aws.s3.Bucket("example", {});
const exampleBucketPublicAccessBlock = new aws.s3.BucketPublicAccessBlock("example", {
    blockPublicAcls: true,
    blockPublicPolicy: true,
    bucket: exampleBucket.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown.



## Create a BucketPublicAccessBlock Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketPublicAccessBlock">BucketPublicAccessBlock</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketPublicAccessBlockArgs">BucketPublicAccessBlockArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BucketPublicAccessBlock</span><span class="p">(resource_name, id, opts=None, </span>block_public_acls=None<span class="p">, </span>block_public_policy=None<span class="p">, </span>bucket=None<span class="p">, </span>ignore_public_acls=None<span class="p">, </span>restrict_public_buckets=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucketPublicAccessBlock<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketPublicAccessBlockArgs">BucketPublicAccessBlockArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketPublicAccessBlock">BucketPublicAccessBlock</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketPublicAccessBlock.html">BucketPublicAccessBlock</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketPublicAccessBlockArgs.html">BucketPublicAccessBlockArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a BucketPublicAccessBlock resource with the given unique name, arguments, and options.

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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>public_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict_<wbr>public_<wbr>buckets</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## BucketPublicAccessBlock Output Properties

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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>public_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict_<wbr>public_<wbr>buckets</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing BucketPublicAccessBlock Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketPublicAccessBlockState, opts?: pulumi.CustomResourceOptions): BucketPublicAccessBlock;
```

```python
def get(resource_name, id, opts=None, block_<wbr>public_<wbr>acls=None, block_<wbr>public_<wbr>policy=None, bucket=None, ignore_<wbr>public_<wbr>acls=None, restrict_<wbr>public_<wbr>buckets=None)
```

```go
func GetBucketPublicAccessBlock(ctx *pulumi.Context, name string, id pulumi.IDInput, state *BucketPublicAccessBlockState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static BucketPublicAccessBlock Get(string name, Input<string> id, BucketPublicAccessBlockState? state = null, CustomResourceOptions? options = null);
```

Get an existing BucketPublicAccessBlock resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
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
            <td class="align-top">block_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>public_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
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
S3 Bucket to which this Public Access Block configuration should be applied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict_<wbr>public_<wbr>buckets</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









