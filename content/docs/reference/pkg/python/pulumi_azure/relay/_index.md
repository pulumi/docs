---
title: Module relay
---

<div class="section" id="relay">
<h1>relay<a class="headerlink" href="#relay" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.relay"></span><dl class="class">
<dt id="pulumi_azure.relay.Namespace">
<em class="property">class </em><code class="descclassname">pulumi_azure.relay.</code><code class="descname">Namespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>sku_name=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Relay Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Relay Namespace.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</li>
<li><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/relay_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/relay_namespace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.metric_id">
<code class="descname">metric_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.metric_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for Azure Insights metrics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Azure Relay Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.sku_name">
<code class="descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.relay.Namespace.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>location=None</em>, <em>metric_id=None</em>, <em>name=None</em>, <em>primary_connection_string=None</em>, <em>primary_key=None</em>, <em>resource_group_name=None</em>, <em>secondary_connection_string=None</em>, <em>secondary_key=None</em>, <em>sku=None</em>, <em>sku_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] metric_id: The Identifier for Azure Insights metrics.
:param pulumi.Input[str] name: Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.
:param pulumi.Input[str] primary_connection_string: The primary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.
:param pulumi.Input[str] primary_key: The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Azure Relay Namespace.
:param pulumi.Input[str] secondary_connection_string: The secondary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.
:param pulumi.Input[str] secondary_key: The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.
:param pulumi.Input[dict] sku: ) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.
:param pulumi.Input[str] sku_name: The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/relay_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/relay_namespace.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.relay.Namespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.relay.Namespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
