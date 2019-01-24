<div class="section" id="module-pulumi_aws.elastictranscoder">
<span id="elastictranscoder"></span><h1>elastictranscoder<a class="headerlink" href="#module-pulumi_aws.elastictranscoder" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.elastictranscoder.Pipeline">
<em class="property">class </em><code class="descclassname">pulumi_aws.elastictranscoder.</code><code class="descname">Pipeline</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>aws_kms_key_arn=None</em>, <em>content_config=None</em>, <em>content_config_permissions=None</em>, <em>input_bucket=None</em>, <em>name=None</em>, <em>notifications=None</em>, <em>output_bucket=None</em>, <em>role=None</em>, <em>thumbnail_config=None</em>, <em>thumbnail_config_permissions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Transcoder pipeline resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>aws_kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</li>
<li><strong>content_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</li>
<li><strong>content_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <cite>content_config</cite> object. (documented below)</li>
<li><strong>input_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pipeline. Maximum 40 characters</li>
<li><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)</li>
<li><strong>output_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</li>
<li><strong>thumbnail_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)</li>
<li><strong>thumbnail_config_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The permissions for the <cite>thumbnail_config</cite> object. (documented below)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn">
<code class="descname">aws_kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.aws_kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config">
<code class="descname">content_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.content_config_permissions">
<code class="descname">content_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.content_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <cite>content_config</cite> object. (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.input_bucket">
<code class="descname">input_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.input_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pipeline. Maximum 40 characters</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.notifications">
<code class="descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.output_bucket">
<code class="descname">output_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.output_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.thumbnail_config">
<code class="descname">thumbnail_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.thumbnail_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions">
<code class="descname">thumbnail_config_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.thumbnail_config_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions for the <cite>thumbnail_config</cite> object. (documented below)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Pipeline.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Pipeline.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Pipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elastictranscoder.Preset">
<em class="property">class </em><code class="descclassname">pulumi_aws.elastictranscoder.</code><code class="descname">Preset</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>audio=None</em>, <em>audio_codec_options=None</em>, <em>container=None</em>, <em>description=None</em>, <em>name=None</em>, <em>thumbnails=None</em>, <em>type=None</em>, <em>video=None</em>, <em>video_codec_options=None</em>, <em>video_watermarks=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Transcoder preset resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>audio</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Audio parameters object (documented below).</li>
<li><strong>audio_codec_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Codec options for the audio parameters (documented below)</li>
<li><strong>container</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container type for the output file. Valid values are <cite>flac</cite>, <cite>flv</cite>, <cite>fmp4</cite>, <cite>gif</cite>, <cite>mp3</cite>, <cite>mp4</cite>, <cite>mpg</cite>, <cite>mxf</cite>, <cite>oga</cite>, <cite>ogg</cite>, <cite>ts</cite>, and <cite>webm</cite>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the preset (maximum 255 characters)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the preset. (maximum 40 characters)</li>
<li><strong>thumbnails</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Thumbnail parameters object (documented below)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] type
:param pulumi.Input[dict] video: Video parameters object (documented below)
:param pulumi.Input[dict] video_codec_options
:param pulumi.Input[list] video_watermarks: Watermark parameters for the video parameters (documented below)</p>
<blockquote>
<div><ul class="simple">
<li><cite>video_codec_options</cite> (Optional, Forces new resource) Codec options for the video parameters</li>
</ul>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio">
<code class="descname">audio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio" title="Permalink to this definition">¶</a></dt>
<dd><p>Audio parameters object (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.audio_codec_options">
<code class="descname">audio_codec_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.audio_codec_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Codec options for the audio parameters (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.container">
<code class="descname">container</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.container" title="Permalink to this definition">¶</a></dt>
<dd><p>The container type for the output file. Valid values are <cite>flac</cite>, <cite>flv</cite>, <cite>fmp4</cite>, <cite>gif</cite>, <cite>mp3</cite>, <cite>mp4</cite>, <cite>mpg</cite>, <cite>mxf</cite>, <cite>oga</cite>, <cite>ogg</cite>, <cite>ts</cite>, and <cite>webm</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the preset (maximum 255 characters)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the preset. (maximum 40 characters)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.thumbnails">
<code class="descname">thumbnails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.thumbnails" title="Permalink to this definition">¶</a></dt>
<dd><p>Thumbnail parameters object (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video">
<code class="descname">video</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video" title="Permalink to this definition">¶</a></dt>
<dd><p>Video parameters object (documented below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elastictranscoder.Preset.video_watermarks">
<code class="descname">video_watermarks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.video_watermarks" title="Permalink to this definition">¶</a></dt>
<dd><p>Watermark parameters for the video parameters (documented below)
* <cite>video_codec_options</cite> (Optional, Forces new resource) Codec options for the video parameters</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Preset.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elastictranscoder.Preset.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elastictranscoder.Preset.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
