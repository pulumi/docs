---
title: Module elastictranscoder
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn">
<code class="sig-name descname">aws_kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config">
<code class="sig-name descname">content_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config_permissions">
<code class="sig-name descname">content_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <code class="docutils literal notranslate"><span class="pre">content_config</span></code> object. (documented below)</p>
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
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions">
<code class="sig-name descname">thumbnail_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <code class="docutils literal notranslate"><span class="pre">thumbnail_config</span></code> object. (documented below)</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown</a>.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio">
<code class="sig-name descname">audio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio" title="Permalink to this definition">¶</a></dt>
<dd><p>Audio parameters object (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio_codec_options">
<code class="sig-name descname">audio_codec_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio_codec_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Codec options for the audio parameters (documented below)</p>
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
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video">
<code class="sig-name descname">video</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video" title="Permalink to this definition">¶</a></dt>
<dd><p>Video parameters object (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video_watermarks">
<code class="sig-name descname">video_watermarks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video_watermarks" title="Permalink to this definition">¶</a></dt>
<dd><p>Watermark parameters for the video parameters (documented below)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">video_codec_options</span></code> (Optional, Forces new resource) Codec options for the video parameters</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown</a>.</p>
</div></blockquote>
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
