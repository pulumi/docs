<div class="section" id="module-pulumi_gcp.sourcerepo">
<span id="sourcerepo"></span><h1>sourcerepo<a class="headerlink" href="#module-pulumi_gcp.sourcerepo" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.sourcerepo.Repository">
<em class="property">class </em><code class="descclassname">pulumi_gcp.sourcerepo.</code><code class="descname">Repository</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>For more information, see [the official
documentation](<a class="reference external" href="https://cloud.google.com/source-repositories/">https://cloud.google.com/source-repositories/</a>) and
[API](<a class="reference external" href="https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos">https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos</a>)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the repository that will be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.sourcerepo.Repository.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the repository that will be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sourcerepo.Repository.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sourcerepo.Repository.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sourcerepo.Repository.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The url to clone the repository.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sourcerepo.Repository.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sourcerepo.Repository.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sourcerepo.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
