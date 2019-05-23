---
---

<div class="section" id="module-pulumi_azure.autoscale">
<span id="autoscale"></span><h1>autoscale<a class="headerlink" href="#module-pulumi_azure.autoscale" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.autoscale.Setting">
<em class="property">class </em><code class="descclassname">pulumi_azure.autoscale.</code><code class="descname">Setting</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notification=None</em>, <em>profiles=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>target_resource_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.autoscale.Setting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.</p>
<blockquote>
<div><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">azurerm_monitor_autoscale_setting</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AutoScale Setting. Changing this forces a new resource to be created.</li>
<li><strong>notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</li>
<li><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource ID of the resource that the autoscale setting should be added to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AutoScale Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.notification">
<code class="descname">notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.profiles">
<code class="descname">profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.autoscale.Setting.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.autoscale.Setting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource ID of the resource that the autoscale setting should be added to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.autoscale.Setting.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.autoscale.Setting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.autoscale.Setting.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.autoscale.Setting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
