---
---

<div class="section" id="module-pulumi_aws.servicecatalog">
<span id="servicecatalog"></span><h1>servicecatalog<a class="headerlink" href="#module-pulumi_aws.servicecatalog" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.servicecatalog.Portfolio">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicecatalog.</code><code class="descname">Portfolio</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>provider_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a Service Catalog Portfolio.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the portfolio</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the portfolio.</li>
<li><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the person or organization who owns the portfolio.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Tags to apply to the connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.servicecatalog.Portfolio.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the portfolio</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicecatalog.Portfolio.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the portfolio.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicecatalog.Portfolio.provider_name">
<code class="descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the person or organization who owns the portfolio.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicecatalog.Portfolio.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to apply to the connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicecatalog.Portfolio.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicecatalog.Portfolio.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicecatalog.Portfolio.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
