---
---

<div class="section" id="privatedns">
<h1>privatedns<a class="headerlink" href="#privatedns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.privatedns"></span><dl class="class">
<dt id="pulumi_azure.privatedns.Zone">
<em class="property">class </em><code class="descclassname">pulumi_azure.privatedns.</code><code class="descname">Zone</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage Private DNS zones within Azure DNS. These zones are hosted on Azure’s name servers.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS Zone. Must be a valid domain name.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_record_sets">
<code class="descname">max_number_of_record_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_record_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of record sets that can be created in this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links">
<code class="descname">max_number_of_virtual_network_links</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of virtual networks that can be linked to this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links_with_registration">
<code class="descname">max_number_of_virtual_network_links_with_registration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links_with_registration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private DNS Zone. Must be a valid domain name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.number_of_record_sets">
<code class="descname">number_of_record_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.number_of_record_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>The current number of record sets in this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.Zone.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.Zone.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
