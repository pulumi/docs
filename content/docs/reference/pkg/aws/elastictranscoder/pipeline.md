
---
title: "Pipeline"
block_external_search_index: true
---

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

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Pipeline">Pipeline</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PipelineArgs">PipelineArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Pipeline</span><span class="p">(resource_name, opts=None, </span>aws_kms_key_arn=None<span class="p">, </span>content_config=None<span class="p">, </span>content_config_permissions=None<span class="p">, </span>input_bucket=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, </span>output_bucket=None<span class="p">, </span>role=None<span class="p">, </span>thumbnail_config=None<span class="p">, </span>thumbnail_config_permissions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPipeline<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineArgs">PipelineArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Pipeline">Pipeline</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Pipeline.html">Pipeline</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.ElasticTranscoder.Inputs.PipelineArgs.html">PipelineArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Content<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Content<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Notifications<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">*Pipeline<wbr>Content<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">*Pipeline<wbr>Thumbnail<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aws_<wbr>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>input_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Pipeline Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Outputs.<wbr>Pipeline<wbr>Content<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Outputs.<wbr>Pipeline<wbr>Content<wbr>Config<wbr>Permission&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Outputs.<wbr>Pipeline<wbr>Notifications?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Outputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Outputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>aws_<wbr>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>input_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>thumbnail_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>thumbnail_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Pipeline Resource

Get an existing Pipeline resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PipelineState">PipelineState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Pipeline">Pipeline</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>aws_kms_key_arn=None<span class="p">, </span>content_config=None<span class="p">, </span>content_config_permissions=None<span class="p">, </span>input_bucket=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, </span>output_bucket=None<span class="p">, </span>role=None<span class="p">, </span>thumbnail_config=None<span class="p">, </span>thumbnail_config_permissions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPipeline<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineState">PipelineState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Pipeline">Pipeline</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Pipeline.html">Pipeline</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PipelineState.html">PipelineState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Content<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Content<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Notifications<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List&lt;Pulumi.<wbr>Aws.<wbr>Elastic<wbr>Transcoder.<wbr>Inputs.<wbr>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">*Pipeline<wbr>Content<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">[]Pipeline<wbr>Content<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">*Pipeline<wbr>Notifications</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">*Pipeline<wbr>Thumbnail<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">[]Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>aws<wbr>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Pipeline<wbr>Content<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">Pipeline<wbr>Content<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>input<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Pipeline<wbr>Notifications?</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Pipeline<wbr>Thumbnail<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail<wbr>Config<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>aws_<wbr>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfig">Dict[Pipeline<wbr>Content<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinecontentconfigpermission">List[Pipeline<wbr>Content<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `content_config` object. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>input_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the pipeline. Maximum 40 characters
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinenotifications">Dict[Pipeline<wbr>Notifications]</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfig">Dict[Pipeline<wbr>Thumbnail<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbnail_<wbr>config_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#pipelinethumbnailconfigpermission">List[Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}The permissions for the `thumbnail_config` object. (documented below)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Pipeline<wbr>Content<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineContentConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineContentConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pipeline<wbr>Content<wbr>Config<wbr>Permission</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineContentConfigPermission">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineContentConfigPermission">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigPermissionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineContentConfigPermissionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to transcoded files and playlists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pipeline<wbr>Notifications</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineNotifications">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineNotifications">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineNotificationsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineNotificationsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Completed</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Progressing</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Warning</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Completed</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Progressing</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Warning</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>completed</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>error</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>progressing</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>warning</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>completed</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>error</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>progressing</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>warning</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pipeline<wbr>Thumbnail<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineThumbnailConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineThumbnailConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pipeline<wbr>Thumbnail<wbr>Config<wbr>Permission</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PipelineThumbnailConfigPermission">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PipelineThumbnailConfigPermission">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigPermissionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PipelineThumbnailConfigPermissionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS user or group that you want to have access to thumbnail files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grantee<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







