
---
title: "Pipeline"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an Elastic Transcoder pipeline resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bar = new aws.elastictranscoder.Pipeline("bar", {
    contentConfig: {
        bucket: aws_s3_bucket_content_bucket.bucket,
        storageClass: "Standard",
    },
    inputBucket: aws_s3_bucket_input_bucket.bucket,
    role: aws_iam_role_test_role.arn,
    thumbnailConfig: {
        bucket: aws_s3_bucket_thumb_bucket.bucket,
        storageClass: "Standard",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown.



## Create a Pipeline Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Pipeline">Pipeline</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PipelineArgs">PipelineArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Pipeline</span><span class="p">(resource_name, opts=None, </span>aws_kms_key_arn=None<span class="p">, </span>content_config=None<span class="p">, </span>content_config_permissions=None<span class="p">, </span>input_bucket=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, </span>output_bucket=None<span class="p">, </span>role=None<span class="p">, </span>thumbnail_config=None<span class="p">, </span>thumbnail_config_permissions=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPipeline<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineArgs">PipelineArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Pipeline">Pipeline</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Pipeline.html">Pipeline</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineArgs.html">PipelineArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Pipeline resource with the given unique name, arguments, and options.

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
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List&lt;Pipeline<wbr>Content<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List&lt;Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">*Pipeline<wbr>Content<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">*Pipeline<wbr>Thumbnail<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">aws_<wbr>kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Pipeline Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List&lt;Pipeline<wbr>Content<wbr>Config<wbr>Permission&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List&lt;Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} The permissions for the `thumbnail_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Pipeline Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PipelineState">PipelineState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Pipeline">Pipeline</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>aws_kms_key_arn=None<span class="p">, </span>content_config=None<span class="p">, </span>content_config_permissions=None<span class="p">, </span>input_bucket=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, </span>output_bucket=None<span class="p">, </span>role=None<span class="p">, </span>thumbnail_config=None<span class="p">, </span>thumbnail_config_permissions=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPipeline<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineState">PipelineState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Pipeline">Pipeline</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Pipeline.html">Pipeline</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineState.html">PipelineState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Pipeline resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List&lt;Pipeline<wbr>Content<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List&lt;Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">*Pipeline<wbr>Content<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">*Pipeline<wbr>Thumbnail<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail<wbr>Config<wbr>Permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">content_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `content_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
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
The name of the pipeline. Maximum 40 characters
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notifications</td>
            <td class="align-top">
                
                <code><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnail_<wbr>config_<wbr>permissions</td>
            <td class="align-top">
                
                <code><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permissions for the `thumbnail_config` object. (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### PipelineContentConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineContentConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineContentConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineContentConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineContentConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PipelineContentConfigPermission
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineContentConfigPermission">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineContentConfigPermission">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigPermissionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigPermissionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineContentConfigPermissionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineContentConfigPermission.html">output</a> API doc for this type.
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
            <td class="align-top">Accesses</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">Accesses</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">accesses</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">accesses</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PipelineNotifications
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineNotifications">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineNotifications">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineNotificationsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineNotificationsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineNotificationsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineNotifications.html">output</a> API doc for this type.
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
            <td class="align-top">Completed</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Progressing</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Warning</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
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
            <td class="align-top">Completed</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Progressing</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Warning</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
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
            <td class="align-top">completed</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">progressing</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">warning</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
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
            <td class="align-top">completed</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">progressing</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">warning</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PipelineThumbnailConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineThumbnailConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineThumbnailConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineThumbnailConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineThumbnailConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
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
The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PipelineThumbnailConfigPermission
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineThumbnailConfigPermission">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineThumbnailConfigPermission">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigPermissionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigPermissionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineThumbnailConfigPermissionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineThumbnailConfigPermission.html">output</a> API doc for this type.
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
            <td class="align-top">Accesses</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">Accesses</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">accesses</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
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
            <td class="align-top">accesses</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS user or group that you want to have access to thumbnail files.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grantee<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







