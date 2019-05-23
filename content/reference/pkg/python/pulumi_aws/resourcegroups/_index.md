---
---

<div class="section" id="module-pulumi_aws.resourcegroups">
<span id="resourcegroups"></span><h1>resourcegroups<a class="headerlink" href="#module-pulumi_aws.resourcegroups" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.resourcegroups.Group">
<em class="property">class </em><code class="descclassname">pulumi_aws.resourcegroups.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>resource_query=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.resourcegroups.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the resource group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group’s name. A resource group name can have a maximum of 127 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</li>
<li><strong>resource_query</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">resource_query</span></code> block. Resource queries are documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.resourcegroups.Group.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.resourcegroups.Group.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.resourcegroups.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group’s name. A resource group name can have a maximum of 127 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.resourcegroups.Group.resource_query">
<code class="descname">resource_query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.resource_query" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">resource_query</span></code> block. Resource queries are documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.resourcegroups.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.resourcegroups.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.resourcegroups.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
