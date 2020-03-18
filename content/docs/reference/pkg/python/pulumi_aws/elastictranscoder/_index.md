---
title: Module elastictranscoder
title_tag: Module elastictranscoder | Package pulumi_aws | Python SDK
linktitle: elastictranscoder
notitle: true
---

<div class="section" id="elastictranscoder">
<h1>elastictranscoder<a class="headerlink" href="#elastictranscoder" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.elastictranscoder"></span><dl class="class">
<dt id="pulumi_aws.elastictranscoder.Pipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elastictranscoder.</code><code class="sig-name descname">Pipeline</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_kms_key_arn=None</em>, <em class="sig-param">content_config=None</em>, <em class="sig-param">content_config_permissions=None</em>, <em class="sig-param">input_bucket=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">output_bucket=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">thumbnail_config=None</em>, <em class="sig-param">thumbnail_config_permissions=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Transcoder pipeline resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p></li>
<li><p><strong>content_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</p></li>
<li><p><strong>content_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <code class="docutils literal notranslate"><span class="pre">content_config</span></code> object. (documented below)</p></li>
<li><p><strong>input_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline. Maximum 40 characters</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)</p></li>
<li><p><strong>output_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</p></li>
<li><p><strong>thumbnail_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)</p></li>
<li><p><strong>thumbnail_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <code class="docutils literal notranslate"><span class="pre">thumbnail_config</span></code> object. (documented below)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
<p>The <strong>content_config_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">completed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">progressing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">warning</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.</p></li>
</ul>
<p>The <strong>thumbnail_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
<p>The <strong>thumbnail_config_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn">
<code class="sig-name descname">aws_kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config">
<code class="sig-name descname">content_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config_permissions">
<code class="sig-name descname">content_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <code class="docutils literal notranslate"><span class="pre">content_config</span></code> object. (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.input_bucket">
<code class="sig-name descname">input_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.input_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline. Maximum 40 characters</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.notifications">
<code class="sig-name descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">completed</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">progressing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">warning</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.output_bucket">
<code class="sig-name descname">output_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.output_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.thumbnail_config">
<code class="sig-name descname">thumbnail_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.thumbnail_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions">
<code class="sig-name descname">thumbnail_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <code class="docutils literal notranslate"><span class="pre">thumbnail_config</span></code> object. (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Pipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_kms_key_arn=None</em>, <em class="sig-param">content_config=None</em>, <em class="sig-param">content_config_permissions=None</em>, <em class="sig-param">input_bucket=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">output_bucket=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">thumbnail_config=None</em>, <em class="sig-param">thumbnail_config_permissions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p></li>
<li><p><strong>content_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</p></li>
<li><p><strong>content_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <code class="docutils literal notranslate"><span class="pre">content_config</span></code> object. (documented below)</p></li>
<li><p><strong>input_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline. Maximum 40 characters</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)</p></li>
<li><p><strong>output_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</p></li>
<li><p><strong>thumbnail_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)</p></li>
<li><p><strong>thumbnail_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <code class="docutils literal notranslate"><span class="pre">thumbnail_config</span></code> object. (documented below)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
<p>The <strong>content_config_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">completed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">progressing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">warning</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.</p></li>
</ul>
<p>The <strong>thumbnail_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_class</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p></li>
</ul>
<p>The <strong>thumbnail_config_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The permission that you want to give to the AWS user that you specified in <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantee</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS user or group that you want to have access to thumbnail files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">granteeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the type of value that appears in the <code class="docutils literal notranslate"><span class="pre">thumbnail_config_permissions.grantee</span></code> object.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Pipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Pipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elastictranscoder.Preset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elastictranscoder.</code><code class="sig-name descname">Preset</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audio=None</em>, <em class="sig-param">audio_codec_options=None</em>, <em class="sig-param">container=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">thumbnails=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">video=None</em>, <em class="sig-param">video_codec_options=None</em>, <em class="sig-param">video_watermarks=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Transcoder preset resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audio</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Audio parameters object (documented below).</p></li>
<li><p><strong>audio_codec_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Codec options for the audio parameters (documented below)</p></li>
<li><p><strong>container</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container type for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">flac</span></code>, <code class="docutils literal notranslate"><span class="pre">flv</span></code>, <code class="docutils literal notranslate"><span class="pre">fmp4</span></code>, <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">mp3</span></code>, <code class="docutils literal notranslate"><span class="pre">mp4</span></code>, <code class="docutils literal notranslate"><span class="pre">mpg</span></code>, <code class="docutils literal notranslate"><span class="pre">mxf</span></code>, <code class="docutils literal notranslate"><span class="pre">oga</span></code>, <code class="docutils literal notranslate"><span class="pre">ogg</span></code>, <code class="docutils literal notranslate"><span class="pre">ts</span></code>, and <code class="docutils literal notranslate"><span class="pre">webm</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the preset (maximum 255 characters)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the preset. (maximum 40 characters)</p></li>
<li><p><strong>thumbnails</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Thumbnail parameters object (documented below)</p></li>
<li><p><strong>video</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Video parameters object (documented below)</p></li>
<li><p><strong>video_watermarks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Watermark parameters for the video parameters (documented below)</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
</pre></div>
</div>
<p>The <strong>audio</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audioPackingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The number of audio channels in the output file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The sample rate of the audio stream in the output file, in hertz. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">22050</span></code>, <code class="docutils literal notranslate"><span class="pre">32000</span></code>, <code class="docutils literal notranslate"><span class="pre">44100</span></code>, <code class="docutils literal notranslate"><span class="pre">48000</span></code>, <code class="docutils literal notranslate"><span class="pre">96000</span></code></p></li>
</ul>
<p>The <strong>audio_codec_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bitDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are <code class="docutils literal notranslate"><span class="pre">16</span></code> and <code class="docutils literal notranslate"><span class="pre">24</span></code>. (FLAC/PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)</p></li>
</ul>
<p>The <strong>thumbnails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of thumbnails, if any. Valid formats are jpg and png.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
<p>The <strong>video</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">displayAspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedGop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The frames per second for the video stream in the output file. The following values are valid: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">23.97</span></code>, <code class="docutils literal notranslate"><span class="pre">24</span></code>, <code class="docutils literal notranslate"><span class="pre">25</span></code>, <code class="docutils literal notranslate"><span class="pre">29.97</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">50</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyframesMaxDist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum number of frames between key frames. Not applicable for containers of type gif.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFrameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
<p>The <strong>video_watermarks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The horizontal position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">horzontal_offset</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">horizontal_align</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that determines how Elastic Transcoder interprets values that you specified for <code class="docutils literal notranslate"><span class="pre">video_watermarks.horizontal_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.vertical_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_width</span></code>, and <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_height</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Content</span></code> and <code class="docutils literal notranslate"><span class="pre">Frame</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The vertical position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Top</span></code>, <code class="docutils literal notranslate"><span class="pre">Bottom</span></code>, <code class="docutils literal notranslate"><span class="pre">Center</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount by which you want the vertical position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code></p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio">
<code class="sig-name descname">audio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio" title="Permalink to this definition">¶</a></dt>
<dd><p>Audio parameters object (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audioPackingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channels</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The number of audio channels in the output file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleRate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The sample rate of the audio stream in the output file, in hertz. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">22050</span></code>, <code class="docutils literal notranslate"><span class="pre">32000</span></code>, <code class="docutils literal notranslate"><span class="pre">44100</span></code>, <code class="docutils literal notranslate"><span class="pre">48000</span></code>, <code class="docutils literal notranslate"><span class="pre">96000</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio_codec_options">
<code class="sig-name descname">audio_codec_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio_codec_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Codec options for the audio parameters (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bitDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are <code class="docutils literal notranslate"><span class="pre">16</span></code> and <code class="docutils literal notranslate"><span class="pre">24</span></code>. (FLAC/PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signed</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.container">
<code class="sig-name descname">container</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.container" title="Permalink to this definition">¶</a></dt>
<dd><p>The container type for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">flac</span></code>, <code class="docutils literal notranslate"><span class="pre">flv</span></code>, <code class="docutils literal notranslate"><span class="pre">fmp4</span></code>, <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">mp3</span></code>, <code class="docutils literal notranslate"><span class="pre">mp4</span></code>, <code class="docutils literal notranslate"><span class="pre">mpg</span></code>, <code class="docutils literal notranslate"><span class="pre">mxf</span></code>, <code class="docutils literal notranslate"><span class="pre">oga</span></code>, <code class="docutils literal notranslate"><span class="pre">ogg</span></code>, <code class="docutils literal notranslate"><span class="pre">ts</span></code>, and <code class="docutils literal notranslate"><span class="pre">webm</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the preset (maximum 255 characters)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the preset. (maximum 40 characters)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.thumbnails">
<code class="sig-name descname">thumbnails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.thumbnails" title="Permalink to this definition">¶</a></dt>
<dd><p>Thumbnail parameters object (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The format of thumbnails, if any. Valid formats are jpg and png.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video">
<code class="sig-name descname">video</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video" title="Permalink to this definition">¶</a></dt>
<dd><p>Video parameters object (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">displayAspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedGop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The frames per second for the video stream in the output file. The following values are valid: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">23.97</span></code>, <code class="docutils literal notranslate"><span class="pre">24</span></code>, <code class="docutils literal notranslate"><span class="pre">25</span></code>, <code class="docutils literal notranslate"><span class="pre">29.97</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">50</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyframesMaxDist</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum number of frames between key frames. Not applicable for containers of type gif.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFrameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video_watermarks">
<code class="sig-name descname">video_watermarks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video_watermarks" title="Permalink to this definition">¶</a></dt>
<dd><p>Watermark parameters for the video parameters (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">video_codec_options</span></code> (Optional, Forces new resource) Codec options for the video parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The horizontal position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">horzontal_offset</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">horizontal_align</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A value that determines how Elastic Transcoder interprets values that you specified for <code class="docutils literal notranslate"><span class="pre">video_watermarks.horizontal_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.vertical_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_width</span></code>, and <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_height</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Content</span></code> and <code class="docutils literal notranslate"><span class="pre">Frame</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The vertical position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Top</span></code>, <code class="docutils literal notranslate"><span class="pre">Bottom</span></code>, <code class="docutils literal notranslate"><span class="pre">Center</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The amount by which you want the vertical position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Preset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">audio=None</em>, <em class="sig-param">audio_codec_options=None</em>, <em class="sig-param">container=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">thumbnails=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">video=None</em>, <em class="sig-param">video_codec_options=None</em>, <em class="sig-param">video_watermarks=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Preset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audio</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Audio parameters object (documented below).</p></li>
<li><p><strong>audio_codec_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Codec options for the audio parameters (documented below)</p></li>
<li><p><strong>container</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container type for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">flac</span></code>, <code class="docutils literal notranslate"><span class="pre">flv</span></code>, <code class="docutils literal notranslate"><span class="pre">fmp4</span></code>, <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">mp3</span></code>, <code class="docutils literal notranslate"><span class="pre">mp4</span></code>, <code class="docutils literal notranslate"><span class="pre">mpg</span></code>, <code class="docutils literal notranslate"><span class="pre">mxf</span></code>, <code class="docutils literal notranslate"><span class="pre">oga</span></code>, <code class="docutils literal notranslate"><span class="pre">ogg</span></code>, <code class="docutils literal notranslate"><span class="pre">ts</span></code>, and <code class="docutils literal notranslate"><span class="pre">webm</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the preset (maximum 255 characters)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the preset. (maximum 40 characters)</p></li>
<li><p><strong>thumbnails</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Thumbnail parameters object (documented below)</p></li>
<li><p><strong>video</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Video parameters object (documented below)</p></li>
<li><p><strong>video_watermarks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Watermark parameters for the video parameters (documented below)</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
</pre></div>
</div>
<p>The <strong>audio</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audioPackingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The number of audio channels in the output file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The sample rate of the audio stream in the output file, in hertz. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">22050</span></code>, <code class="docutils literal notranslate"><span class="pre">32000</span></code>, <code class="docutils literal notranslate"><span class="pre">44100</span></code>, <code class="docutils literal notranslate"><span class="pre">48000</span></code>, <code class="docutils literal notranslate"><span class="pre">96000</span></code></p></li>
</ul>
<p>The <strong>audio_codec_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bitDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are <code class="docutils literal notranslate"><span class="pre">16</span></code> and <code class="docutils literal notranslate"><span class="pre">24</span></code>. (FLAC/PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitOrder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)</p></li>
</ul>
<p>The <strong>thumbnails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of thumbnails, if any. Valid formats are jpg and png.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
<p>The <strong>video</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display aspect ratio of the video in the output file. Valid values are: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">1:1</span></code>, <code class="docutils literal notranslate"><span class="pre">4:3</span></code>, <code class="docutils literal notranslate"><span class="pre">3:2</span></code>, <code class="docutils literal notranslate"><span class="pre">16:9</span></code>. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values <code class="docutils literal notranslate"><span class="pre">max_width</span></code>, <code class="docutils literal notranslate"><span class="pre">max_height</span></code>, <code class="docutils literal notranslate"><span class="pre">sizing_policy</span></code>, <code class="docutils literal notranslate"><span class="pre">padding_policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">display_aspect_ratio</span></code> instead of <code class="docutils literal notranslate"><span class="pre">resolution</span></code> and <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bitRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The video codec for the output file. Valid values are <code class="docutils literal notranslate"><span class="pre">gif</span></code>, <code class="docutils literal notranslate"><span class="pre">H.264</span></code>, <code class="docutils literal notranslate"><span class="pre">mpeg2</span></code>, <code class="docutils literal notranslate"><span class="pre">vp8</span></code>, and <code class="docutils literal notranslate"><span class="pre">vp9</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">displayAspectRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedGop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The frames per second for the video stream in the output file. The following values are valid: <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">23.97</span></code>, <code class="docutils literal notranslate"><span class="pre">24</span></code>, <code class="docutils literal notranslate"><span class="pre">25</span></code>, <code class="docutils literal notranslate"><span class="pre">29.97</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">50</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyframesMaxDist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum number of frames between key frames. Not applicable for containers of type gif.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFrameRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for <code class="docutils literal notranslate"><span class="pre">max_width</span></code> and <code class="docutils literal notranslate"><span class="pre">max_height</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The width and height of the video in the output file, in pixels. Valid values are <code class="docutils literal notranslate"><span class="pre">auto</span></code> and <code class="docutils literal notranslate"><span class="pre">widthxheight</span></code>. (see note for <code class="docutils literal notranslate"><span class="pre">aspect_ratio</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
</ul>
<p>The <strong>video_watermarks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The horizontal position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">horzontal_offset</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount by which you want the horizontal position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">horizontal_align</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxHeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum height of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWidth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum width of the watermark.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that controls scaling of the watermark. Valid values are: <code class="docutils literal notranslate"><span class="pre">Fit</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">ShrinkToFit</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A value that determines how Elastic Transcoder interprets values that you specified for <code class="docutils literal notranslate"><span class="pre">video_watermarks.horizontal_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.vertical_offset</span></code>, <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_width</span></code>, and <code class="docutils literal notranslate"><span class="pre">video_watermarks.max_height</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Content</span></code> and <code class="docutils literal notranslate"><span class="pre">Frame</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalAlign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The vertical position of the watermark unless you specify a nonzero value for <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">Top</span></code>, <code class="docutils literal notranslate"><span class="pre">Bottom</span></code>, <code class="docutils literal notranslate"><span class="pre">Center</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verticalOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount by which you want the vertical position of the watermark to be offset from the position specified by <code class="docutils literal notranslate"><span class="pre">vertical_align</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Preset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Preset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
