<div class="section" id="module-pulumi_gcp.filestore">
<span id="filestore"></span><h1>filestore<a class="headerlink" href="#module-pulumi_gcp.filestore" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.filestore.Instance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.filestore.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>file_shares=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>networks=None</em>, <em>project=None</em>, <em>tier=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Filestore instance.</p>
<blockquote>
<div><strong>Warning:</strong> This resource is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta resources.</div></blockquote>
<p>To get more information about Instance, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/filestore/docs/creating-instances">Official Documentation</a></li>
<li><a class="reference external" href="https://cloud.google.com/filestore/docs/accessing-fileshares">Use with Kubernetes</a></li>
<li><a class="reference external" href="https://cloud.google.com/filestore/docs/copying-data">Copying Data In/Out</a></li>
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
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="pulumi_gcp.filestore.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.filestore.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
