---
title: Module privatedns
title_tag: Module privatedns | Package pulumi_azure | Python SDK
linktitle: privatedns
notitle: true
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
<dt id="pulumi_azure.privatedns.AAAARecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">AAAARecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage DNS AAAA Records within Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS A Record.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IPv6 Addresses.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_aaaa_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_aaaa_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.AAAARecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DNS A Record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.AAAARecord.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.records" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IPv6 Addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.AAAARecord.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.AAAARecord.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.AAAARecord.zone_name">
<code class="sig-name descname">zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.AAAARecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AAAARecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS A Record.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IPv6 Addresses.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_aaaa_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_aaaa_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.AAAARecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.AAAARecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.AAAARecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.LinkService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">LinkService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_approval_subscription_ids=None</em>, <em class="sig-param">load_balancer_frontend_ip_configuration_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_configurations=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">visibility_subscription_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.LinkService" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Private Link Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_approval_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subscription globally unique identifiers(GUID) that will be automatically be able to use this service.</p></li>
<li><p><strong>load_balancer_frontend_ip_configuration_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Standard Load Balancer(SLB) resource IDs. The Private Link service is tied to the frontend IP address of a SLB. All traffic destined for the private link service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the private link service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>nat_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">nat_ip_configuration</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the private link service resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>visibility_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subscription globally unique identifiers(GUID) that will be able to see this service. If left undefined all Azure subscriptions will be able to see this service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nat_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the private link service. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_link_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_link_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias is a globally unique name for your private link service which Azure generates for you. Your can use this alias to request a connection to your private link service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.auto_approval_subscription_ids">
<code class="sig-name descname">auto_approval_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.auto_approval_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subscription globally unique identifiers(GUID) that will be automatically be able to use this service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.load_balancer_frontend_ip_configuration_ids">
<code class="sig-name descname">load_balancer_frontend_ip_configuration_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.load_balancer_frontend_ip_configuration_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Standard Load Balancer(SLB) resource IDs. The Private Link service is tied to the frontend IP address of a SLB. All traffic destined for the private link service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the private link service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.nat_ip_configurations">
<code class="sig-name descname">nat_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.nat_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">nat_ip_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the private link service. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the private link service resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.LinkService.visibility_subscription_ids">
<code class="sig-name descname">visibility_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.visibility_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subscription globally unique identifiers(GUID) that will be able to see this service. If left undefined all Azure subscriptions will be able to see this service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.LinkService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">auto_approval_subscription_ids=None</em>, <em class="sig-param">load_balancer_frontend_ip_configuration_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_configurations=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">visibility_subscription_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias is a globally unique name for your private link service which Azure generates for you. Your can use this alias to request a connection to your private link service.</p></li>
<li><p><strong>auto_approval_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subscription globally unique identifiers(GUID) that will be automatically be able to use this service.</p></li>
<li><p><strong>load_balancer_frontend_ip_configuration_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Standard Load Balancer(SLB) resource IDs. The Private Link service is tied to the frontend IP address of a SLB. All traffic destined for the private link service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the private link service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>nat_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">nat_ip_configuration</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the private link service resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>visibility_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subscription globally unique identifiers(GUID) that will be able to see this service. If left undefined all Azure subscriptions will be able to see this service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nat_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the private link service. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_link_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_link_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.LinkService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.LinkService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.LinkService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.PTRRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">PTRRecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage DNS PTR Records within Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS PTR Record. Changing this forces a new resource to be created.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Fully Qualified Domain Names.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_ptr_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_ptr_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.PTRRecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DNS PTR Record. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.PTRRecord.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.records" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Fully Qualified Domain Names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.PTRRecord.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.PTRRecord.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.PTRRecord.zone_name">
<code class="sig-name descname">zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.PTRRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PTRRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS PTR Record. Changing this forces a new resource to be created.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Fully Qualified Domain Names.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_ptr_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_ptr_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.PTRRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.PTRRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.PTRRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.SRVRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">SRVRecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage DNS SRV Records within Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS SRV Record. Changing this forces a new resource to be created.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">record</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>records</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_srv_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_srv_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.SRVRecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DNS SRV Record. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.SRVRecord.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.records" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">record</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.SRVRecord.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.SRVRecord.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.SRVRecord.zone_name">
<code class="sig-name descname">zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.SRVRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SRVRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DNS SRV Record. Changing this forces a new resource to be created.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">record</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>records</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_srv_record.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_srv_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.SRVRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.SRVRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.SRVRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatedns.</code><code class="sig-name descname">ZoneVirtualNetworkLink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_dns_zone_name=None</em>, <em class="sig-param">registration_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_network_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to manage Private DNS zone Virtual Network Links. These Links enable DNS resolution and registration inside Azure Virtual Networks using Azure Private DNS.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_dns_zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.</p></li>
<li><p><strong>registration_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone_virtual_network_link.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone_virtual_network_link.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.private_dns_zone_name">
<code class="sig-name descname">private_dns_zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.private_dns_zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.registration_enabled">
<code class="sig-name descname">registration_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.registration_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.virtual_network_id">
<code class="sig-name descname">virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_dns_zone_name=None</em>, <em class="sig-param">registration_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_network_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneVirtualNetworkLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS Zone Virtual Network Link. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_dns_zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private DNS zone (without a terminating dot). Changing this forces a new resource to be created.</p></li>
<li><p><strong>registration_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource ID of the Virtual Network that should be linked to the DNS Zone. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone_virtual_network_link.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/private_dns_zone_virtual_network_link.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatedns.ZoneVirtualNetworkLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatedns.ZoneVirtualNetworkLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
