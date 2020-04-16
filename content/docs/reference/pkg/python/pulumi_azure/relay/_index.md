---
title: Module relay
title_tag: Module relay | Package pulumi_azure | Python SDK
linktitle: relay
notitle: true
---

<div class="section" id="relay">
<h1>relay<a class="headerlink" href="#relay" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.relay"></span><dl class="class">
<dt id="pulumi_azure.relay.HybridConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.relay.</code><code class="sig-name descname">HybridConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">relay_namespace_name=None</em>, <em class="sig-param">requires_client_authorization=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.HybridConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Relay Hybrid Connection.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>relay_namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Azure Relay in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_client_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if client authorization is needed for this hybrid connection. True by default. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.relay.HybridConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.HybridConnection.relay_namespace_name">
<code class="sig-name descname">relay_namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.relay_namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure Relay in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.HybridConnection.requires_client_authorization">
<code class="sig-name descname">requires_client_authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.requires_client_authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify if client authorization is needed for this hybrid connection. True by default. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.HybridConnection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.HybridConnection.user_metadata">
<code class="sig-name descname">user_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.relay.HybridConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">relay_namespace_name=None</em>, <em class="sig-param">requires_client_authorization=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HybridConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>relay_namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Azure Relay in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_client_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if client authorization is needed for this hybrid connection. True by default. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Relay Hybrid Connection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usermetadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.relay.HybridConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.relay.HybridConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.HybridConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.relay.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.relay.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Relay Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Relay Namespace.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.metric_id">
<code class="sig-name descname">metric_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.metric_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for Azure Insights metrics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Azure Relay Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.relay.Namespace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.relay.Namespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.relay.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">metric_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metric_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for Azure Insights metrics.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Relay Namespace.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SKU to use. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.relay.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.relay.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.relay.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
