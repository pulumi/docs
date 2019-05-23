---
---

<div class="section" id="module-pulumi_aws.mediapackage">
<span id="mediapackage"></span><h1>mediapackage<a class="headerlink" href="#module-pulumi_aws.mediapackage" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.mediapackage.Channel">
<em class="property">class </em><code class="descclassname">pulumi_aws.mediapackage.</code><code class="descname">Channel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>channel_id=None</em>, <em>description=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediapackage.Channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Elemental MediaPackage Channel.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>channel_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier describing the channel</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the channel</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.mediapackage.Channel.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the channel</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediapackage.Channel.channel_id">
<code class="descname">channel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.channel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier describing the channel</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediapackage.Channel.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the channel</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediapackage.Channel.hls_ingests">
<code class="descname">hls_ingests</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.hls_ingests" title="Permalink to this definition">¶</a></dt>
<dd><p>A single item list of HLS ingest information</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediapackage.Channel.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediapackage.Channel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediapackage.Channel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediapackage.Channel.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
