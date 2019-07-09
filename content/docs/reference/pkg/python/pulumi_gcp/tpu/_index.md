---
---

<div class="section" id="module-pulumi_gcp.tpu">
<span id="tpu"></span><h1>tpu<a class="headerlink" href="#module-pulumi_gcp.tpu" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.tpu.GetTensorflowVersionsResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.tpu.</code><code class="descname">GetTensorflowVersionsResult</code><span class="sig-paren">(</span><em>project=None</em>, <em>versions=None</em>, <em>zone=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.GetTensorflowVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTensorflowVersions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.tpu.GetTensorflowVersionsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.GetTensorflowVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.tpu.Node">
<em class="property">class </em><code class="descclassname">pulumi_gcp.tpu.</code><code class="descname">Node</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accelerator_type=None</em>, <em>cidr_block=None</em>, <em>description=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>network=None</em>, <em>project=None</em>, <em>scheduling_config=None</em>, <em>tensorflow_version=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node" title="Permalink to this definition">¶</a></dt>
<dd><p>A Cloud TPU instance.</p>
<p>To get more information about Node, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/tpu/docs/reference/rest/">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/tpu/docs/">Official Documentation</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/tpu_node.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/tpu_node.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.tpu.Node.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.tpu.Node.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
