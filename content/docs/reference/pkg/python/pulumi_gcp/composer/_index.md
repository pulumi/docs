---
---

<div class="section" id="composer">
<h1>composer<a class="headerlink" href="#composer" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp/issues">terraform-providers/terraform-provider-gcp repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.composer"></span><dl class="class">
<dt id="pulumi_gcp.composer.Environment">
<em class="property">class </em><code class="descclassname">pulumi_gcp.composer.</code><code class="descname">Environment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>config=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Environment resource with the given unique name, props, and options.</p>
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
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/composer_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/composer_environment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.composer.Environment.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.composer.Environment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.composer.Environment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.composer.GetImageVersionsResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.composer.</code><code class="descname">GetImageVersionsResult</code><span class="sig-paren">(</span><em>image_versions=None</em>, <em>project=None</em>, <em>region=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImageVersions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.composer.GetImageVersionsResult.image_versions">
<code class="descname">image_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult.image_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of composer image versions available in the given project and location. Each <code class="docutils literal notranslate"><span class="pre">image_version</span></code> contains:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.composer.GetImageVersionsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.composer.get_image_versions">
<code class="descclassname">pulumi_gcp.composer.</code><code class="descname">get_image_versions</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.get_image_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Cloud Composer versions in a region for a given project.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/composer_image_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/composer_image_versions.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
