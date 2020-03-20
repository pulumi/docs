
---
title: "AmiCopy"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

The "AMI copy" resource allows duplication of an Amazon Machine Image (AMI),
including cross-region copies.

If the source AMI has associated EBS snapshots, those will also be duplicated
along with the AMI.

This is useful for taking a single AMI provisioned in one region and making
it available in another for a multi-region deployment.

Copying an AMI can take several minutes. The creation of this resource will
block until the new AMI is available for use on new instances.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ec2.AmiCopy("example", {
    description: "A copy of ami-xxxxxxxx",
    sourceAmiId: "ami-xxxxxxxx",
    sourceAmiRegion: "us-west-1",
    tags: {
        Name: "HelloWorld",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_copy.html.markdown.



## Create a AmiCopy Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#AmiCopy">AmiCopy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#AmiCopyArgs">AmiCopyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AmiCopy</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>ebs_block_devices=None<span class="p">, </span>encrypted=None<span class="p">, </span>ephemeral_block_devices=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>name=None<span class="p">, </span>source_ami_id=None<span class="p">, </span>source_ami_region=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAmiCopy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyArgs">AmiCopyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopy">AmiCopy</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopy.html">AmiCopy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyArgs.html">AmiCopyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a AmiCopy resource with the given unique name, arguments, and options.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
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
A mapping of tags to assign to the resource.
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">[]Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">[]Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
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
A mapping of tags to assign to the resource.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
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
A mapping of tags to assign to the resource.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List[Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List[Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## AmiCopy Output Properties

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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ena<wbr>Support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">[]Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ena<wbr>Support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">[]Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ena<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List[Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ena_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List[Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">manage_<wbr>ebs_<wbr>snapshots</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov_<wbr>net_<wbr>support</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing AmiCopy Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#AmiCopyState">AmiCopyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#AmiCopy">AmiCopy</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>architecture=None<span class="p">, </span>description=None<span class="p">, </span>ebs_block_devices=None<span class="p">, </span>ena_support=None<span class="p">, </span>encrypted=None<span class="p">, </span>ephemeral_block_devices=None<span class="p">, </span>image_location=None<span class="p">, </span>kernel_id=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>manage_ebs_snapshots=None<span class="p">, </span>name=None<span class="p">, </span>ramdisk_id=None<span class="p">, </span>root_device_name=None<span class="p">, </span>root_snapshot_id=None<span class="p">, </span>source_ami_id=None<span class="p">, </span>source_ami_region=None<span class="p">, </span>sriov_net_support=None<span class="p">, </span>tags=None<span class="p">, </span>virtualization_type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAmiCopy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyState">AmiCopyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopy">AmiCopy</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopy.html">AmiCopy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyState.html">AmiCopyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing AmiCopy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ena<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">[]Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ena<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">[]Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ena<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">ec2.<wbr>Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">manage<wbr>Ebs<wbr>Snapshots</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ami<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Machine architecture for created instances. Defaults to &#34;x86_64&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A longer, human-readable description for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyebsblockdevice">List[Ami<wbr>Copy<wbr>Ebs<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an EBS block device that should be
attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ena_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#amicopyephemeralblockdevice">List[Ami<wbr>Copy<wbr>Ephemeral<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block describing an ephemeral block device that
should be attached to created instances. The structure of this block is described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Path to an S3 object containing an image manifest, e.g. created
by the `ec2-upload-bundle` command in the EC2 command line tools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the kernel image (AKI) that will be used as the paravirtual
kernel in created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">manage_<wbr>ebs_<wbr>snapshots</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A region-unique name for the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an initrd image (ARI) that will be used when booting the
created instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the AMI to copy. This id must be valid in the region
given by `source_ami_region`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>ami_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov_<wbr>net_<wbr>support</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to &#34;simple&#34; (the default), enables enhanced networking
for created instances. No other value is supported at this time.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Keyword to choose what virtualization mode created instances
will use. Can be either &#34;paravirtual&#34; (the default) or &#34;hvm&#34;. The choice of virtualization type
changes the set of further arguments that are required, as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### AmiCopyEbsBlockDevice
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AmiCopyEbsBlockDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AmiCopyEbsBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyEbsBlockDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyEbsBlockDeviceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyEbsBlockDeviceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyEbsBlockDevice.html">output</a> API doc for this type.
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### AmiCopyEphemeralBlockDevice
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AmiCopyEphemeralBlockDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AmiCopyEphemeralBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyEphemeralBlockDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#AmiCopyEphemeralBlockDeviceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyEphemeralBlockDeviceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.AmiCopyEphemeralBlockDevice.html">output</a> API doc for this type.
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
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







