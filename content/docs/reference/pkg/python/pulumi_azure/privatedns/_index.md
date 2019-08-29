---
title: Module privatedns
---

<div class="section" id="privatedns">
<h1>privatedns<a class="headerlink" href="#privatedns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.privatedns"></span><dl class="class">
<dt id="pulumi_azure.privatedns.ARecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">ARecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ARecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage DNS A Records within Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS A Record.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IPv4 Addresses.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_a_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_a_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.ARecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DNS A Record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ARecord.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.records" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IPv4 Addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ARecord.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ARecord.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ARecord.zone_name">
<code class="sig-name descname">zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.ARecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ARecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS A Record.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IPv4 Addresses.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_a_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_a_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.ARecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.ARecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ARecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.privatedns.CnameRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">CnameRecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">record=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage DNS CNAME Records within Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS CNAME Record.</p></li>
<li><p><strong>record</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target of the CNAME.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_cname_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_cname_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.CnameRecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DNS CNAME Record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.CnameRecord.record">
<code class="sig-name descname">record</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.record" title="Permalink to this definition">¶</a></dt>
<dd><p>The target of the CNAME.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.CnameRecord.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.CnameRecord.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.CnameRecord.zone_name">
<code class="sig-name descname">zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.CnameRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">record=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CnameRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS CNAME Record.</p></li>
<li><p><strong>record</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target of the CNAME.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_cname_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_cname_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.CnameRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.CnameRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.CnameRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.privatedns.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage Private DNS zones within Azure DNS. These zones are hosted on Azure’s name servers.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS Zone. Must be a valid domain name.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_record_sets">
<code class="sig-name descname">max_number_of_record_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_record_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of record sets that can be created in this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links">
<code class="sig-name descname">max_number_of_virtual_network_links</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of virtual networks that can be linked to this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links_with_registration">
<code class="sig-name descname">max_number_of_virtual_network_links_with_registration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.max_number_of_virtual_network_links_with_registration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private DNS Zone. Must be a valid domain name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.number_of_record_sets">
<code class="sig-name descname">number_of_record_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.number_of_record_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>The current number of record sets in this Private DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.Zone.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.Zone.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">max_number_of_record_sets=None</em>, <em class="sig-param">max_number_of_virtual_network_links=None</em>, <em class="sig-param">max_number_of_virtual_network_links_with_registration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">number_of_record_sets=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>max_number_of_record_sets</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of record sets that can be created in this Private DNS zone.</p></li>
<li><p><strong>max_number_of_virtual_network_links</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of virtual networks that can be linked to this Private DNS zone.</p></li>
<li><p><strong>max_number_of_virtual_network_links_with_registration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS Zone. Must be a valid domain name.</p></li>
<li><p><strong>number_of_record_sets</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The current number of record sets in this Private DNS zone.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
