---
---

<div class="section" id="module-pulumi_azure.ddosprotection">
<span id="ddosprotection"></span><h1>ddosprotection<a class="headerlink" href="#module-pulumi_azure.ddosprotection" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.ddosprotection.Plan">
<em class="property">class </em><code class="descclassname">pulumi_azure.ddosprotection.</code><code class="descname">Plan</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure DDoS Protection Plan.</p>
<blockquote>
<div><p><strong>NOTE</strong> Azure only allow <code class="docutils literal notranslate"><span class="pre">one</span></code> DDoS Protection Plan per region.</p>
<p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">azurerm_network_ddos_protection_plan</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DDoS Protection Plan. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/ddos_protection_plan.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/ddos_protection_plan.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.ddosprotection.Plan.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.ddosprotection.Plan.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DDoS Protection Plan. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.ddosprotection.Plan.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.ddosprotection.Plan.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.ddosprotection.Plan.virtual_network_ids">
<code class="descname">virtual_network_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.virtual_network_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource ID list of the Virtual Networks associated with DDoS Protection Plan.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.ddosprotection.Plan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.ddosprotection.Plan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.ddosprotection.Plan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
