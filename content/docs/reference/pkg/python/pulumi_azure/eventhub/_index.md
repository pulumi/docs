---
title: Module eventhub
title_tag: Module eventhub | Package pulumi_azure | Python SDK
linktitle: eventhub
notitle: true
---

<div class="section" id="eventhub">
<h1>eventhub<a class="headerlink" href="#eventhub" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.eventhub"></span><dl class="class">
<dt id="pulumi_azure.eventhub.AuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs authorization Rule within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.AuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.AuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the Event Hubs authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the Event Hubs authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the Event Hubs Authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the Event Hubs Authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.AuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.AuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.AwaitableGetAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.AwaitableGetConsumeGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetConsumeGroupResult</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetConsumeGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.AwaitableGetEventhubNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetEventhubNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kafka_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetEventhubNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.AwaitableGetNamespaceAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetNamespaceAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetNamespaceAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.AwaitableGetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kafka_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.AwaitableGetServiceBusNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">AwaitableGetServiceBusNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.AwaitableGetServiceBusNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.ConsumerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">ConsumerGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_consumer_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_consumer_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user metadata.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.ConsumerGroup.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.ConsumerGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.ConsumerGroup.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.ConsumerGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.ConsumerGroup.user_metadata">
<code class="sig-name descname">user_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the user metadata.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.ConsumerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConsumerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user metadata.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.ConsumerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.ConsumerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.ConsumerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">input_mapping_default_values=None</em>, <em class="sig-param">input_mapping_fields=None</em>, <em class="sig-param">input_schema=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Domain</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_domain.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>input_mapping_default_values</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p></li>
<li><p><strong>input_mapping_fields</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p></li>
<li><p><strong>input_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>input_mapping_default_values</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>input_mapping_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.input_mapping_default_values">
<code class="sig-name descname">input_mapping_default_values</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.input_mapping_default_values" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.input_mapping_fields">
<code class="sig-name descname">input_mapping_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.input_mapping_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.input_schema">
<code class="sig-name descname">input_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.input_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Domain.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">input_mapping_default_values=None</em>, <em class="sig-param">input_mapping_fields=None</em>, <em class="sig-param">input_schema=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint associated with the EventGrid Domain.</p></li>
<li><p><strong>input_mapping_default_values</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p></li>
<li><p><strong>input_mapping_fields</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p></li>
<li><p><strong>input_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Shared Access Key associated with the EventGrid Domain.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Shared Access Key associated with the EventGrid Domain.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>input_mapping_default_values</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>input_mapping_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventGridTopic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Topic</p>
<blockquote>
<div><p><strong>Note:</strong> at this time EventGrid Topic’s are only available in a limited number of regions.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventGridTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventGridTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint associated with the EventGrid Topic.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Shared Access Key associated with the EventGrid Topic.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Shared Access Key associated with the EventGrid Topic.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventGridTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capture_description=None</em>, <em class="sig-param">message_retention=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">partition_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs as a nested resource within a Event Hubs namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capture_description</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">capture_description</span></code> block as defined below.</p></li>
<li><p><strong>message_retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub’s parent Namespace exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capture_description</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">archiveNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeLimitInBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipEmptyArchives</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.capture_description">
<code class="sig-name descname">capture_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.capture_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">capture_description</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">archiveNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeLimitInBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipEmptyArchives</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.message_retention">
<code class="sig-name descname">message_retention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.message_retention" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.partition_count">
<code class="sig-name descname">partition_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.partition_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.partition_ids">
<code class="sig-name descname">partition_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.partition_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers for partitions created for Event Hubs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub’s parent Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capture_description=None</em>, <em class="sig-param">message_retention=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">partition_count=None</em>, <em class="sig-param">partition_ids=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capture_description</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">capture_description</span></code> block as defined below.</p></li>
<li><p><strong>message_retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identifiers for partitions created for Event Hubs.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub’s parent Namespace exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capture_description</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">archiveNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeLimitInBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipEmptyArchives</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventHubAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs authorization Rule within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHubAuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the Event Hubs authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the Event Hubs authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the Event Hubs Authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the Event Hubs Authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventHubConsumerGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_consumer_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_consumer_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user metadata.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.user_metadata">
<code class="sig-name descname">user_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the user metadata.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHubConsumerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user metadata.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventHubNamespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rulesets=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventHub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_inflate_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Auto Inflate enabled for the EventHub Namespace?</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_throughput_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rulesets</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rulesets</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rulesets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreMissingVirtualNetworkServiceEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.auto_inflate_enabled">
<code class="sig-name descname">auto_inflate_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.auto_inflate_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Auto Inflate enabled for the EventHub Namespace?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.maximum_throughput_units">
<code class="sig-name descname">maximum_throughput_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.maximum_throughput_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.network_rulesets">
<code class="sig-name descname">network_rulesets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.network_rulesets" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_rulesets</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreMissingVirtualNetworkServiceEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rulesets=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHubNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_inflate_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Auto Inflate enabled for the EventHub Namespace?</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>default_primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_throughput_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rulesets</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rulesets</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rulesets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreMissingVirtualNetworkServiceEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventHubNamespaceAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule for an Event Hub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHubNamespaceAuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the Authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the Authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the Authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the Authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventSubscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">event_delivery_schema=None</em>, <em class="sig-param">eventhub_endpoint=None</em>, <em class="sig-param">hybrid_connection_endpoint=None</em>, <em class="sig-param">included_event_types=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retry_policy=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">storage_blob_dead_letter_destination=None</em>, <em class="sig-param">storage_queue_endpoint=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">webhook_endpoint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Event Subscription</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_event_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_event_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>event_delivery_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p></li>
<li><p><strong>eventhub_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>hybrid_connection_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>included_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applicable event types that need to be part of the event subscription.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of labels to assign to the event subscription.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retry_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_blob_dead_letter_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p></li>
<li><p><strong>storage_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the topic to associate with the event subscription.</p></li>
<li><p><strong>webhook_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>eventhub_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>hybrid_connection_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>retry_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
<p>The <strong>storage_blob_dead_letter_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
<p>The <strong>storage_queue_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
</ul>
<p>The <strong>subject_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
<p>The <strong>webhook_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.event_delivery_schema">
<code class="sig-name descname">event_delivery_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.event_delivery_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.eventhub_endpoint">
<code class="sig-name descname">eventhub_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.eventhub_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.hybrid_connection_endpoint">
<code class="sig-name descname">hybrid_connection_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.hybrid_connection_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.included_event_types">
<code class="sig-name descname">included_event_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.included_event_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applicable event types that need to be part of the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of labels to assign to the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.retry_policy">
<code class="sig-name descname">retry_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.retry_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.storage_blob_dead_letter_destination">
<code class="sig-name descname">storage_blob_dead_letter_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.storage_blob_dead_letter_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.storage_queue_endpoint">
<code class="sig-name descname">storage_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.storage_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.subject_filter">
<code class="sig-name descname">subject_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.subject_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the topic to associate with the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventSubscription.webhook_endpoint">
<code class="sig-name descname">webhook_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.webhook_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">event_delivery_schema=None</em>, <em class="sig-param">eventhub_endpoint=None</em>, <em class="sig-param">hybrid_connection_endpoint=None</em>, <em class="sig-param">included_event_types=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retry_policy=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">storage_blob_dead_letter_destination=None</em>, <em class="sig-param">storage_queue_endpoint=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">webhook_endpoint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>event_delivery_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p></li>
<li><p><strong>eventhub_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>hybrid_connection_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>included_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applicable event types that need to be part of the event subscription.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of labels to assign to the event subscription.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retry_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_blob_dead_letter_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p></li>
<li><p><strong>storage_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the topic to associate with the event subscription.</p></li>
<li><p><strong>webhook_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>eventhub_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>hybrid_connection_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>retry_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
<p>The <strong>storage_blob_dead_letter_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
<p>The <strong>storage_queue_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
</ul>
<p>The <strong>subject_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
<p>The <strong>webhook_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">EventhubNamespaceDisasterRecoveryConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternate_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">partner_namespace_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Disaster Recovery Config for an Event Hub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace_disaster_recovery_config.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventhub_namespace_disaster_recovery_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternate name to use when the Disaster Recovery Config’s name is the same as the replicated namespace’s name.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Disaster Recovery Config. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the primary EventHub Namespace to replicate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partner_namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EventHub Namespace to replicate to.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Disaster Recovery Config exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.alternate_name">
<code class="sig-name descname">alternate_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.alternate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>An alternate name to use when the Disaster Recovery Config’s name is the same as the replicated namespace’s name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Disaster Recovery Config. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the primary EventHub Namespace to replicate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.partner_namespace_id">
<code class="sig-name descname">partner_namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.partner_namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the EventHub Namespace to replicate to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Disaster Recovery Config exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternate_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">partner_namespace_id=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventhubNamespaceDisasterRecoveryConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternate name to use when the Disaster Recovery Config’s name is the same as the replicated namespace’s name.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Disaster Recovery Config. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the primary EventHub Namespace to replicate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partner_namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EventHub Namespace to replicate to.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Disaster Recovery Config exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventhubNamespaceDisasterRecoveryConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthorizationRule.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Event Hubs Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetAuthorizationRuleResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetAuthorizationRuleResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Event Hubs Authorization Rule.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetConsumeGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetConsumeGroupResult</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetConsumeGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConsumeGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetConsumeGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetConsumeGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetConsumeGroupResult.user_metadata">
<code class="sig-name descname">user_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetConsumeGroupResult.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the user metadata.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetEventhubNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kafka_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEventhubNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.auto_inflate_enabled">
<code class="sig-name descname">auto_inflate_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.auto_inflate_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Auto Inflate enabled for the EventHub Namespace?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the EventHub Namespace exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.maximum_throughput_units">
<code class="sig-name descname">maximum_throughput_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.maximum_throughput_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of throughput units when Auto Inflate is Enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the EventHub Namespace.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetNamespaceAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespaceAuthorizationRule.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Listen to the Event Hub?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Manage to the Event Hub?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the EventHub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceAuthorizationRuleResult.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Send to the Event Hub?</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">auto_inflate_enabled=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kafka_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_throughput_units=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.auto_inflate_enabled">
<code class="sig-name descname">auto_inflate_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.auto_inflate_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Auto Inflate enabled for the EventHub Namespace?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the EventHub Namespace exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.maximum_throughput_units">
<code class="sig-name descname">maximum_throughput_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.maximum_throughput_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of throughput units when Auto Inflate is Enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetNamespaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the EventHub Namespace.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">GetServiceBusNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceBusNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The capacity of the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Resource Group in which the ServiceBus Namespace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tier used for the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this ServiceBus Namespace is zone redundant.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code> or <code class="docutils literal notranslate"><span class="pre">8</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Options are basic, standard or premium.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this resource is zone redundant. <code class="docutils literal notranslate"><span class="pre">sku</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code> or <code class="docutils literal notranslate"><span class="pre">8</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use. Options are basic, standard or premium.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this resource is zone redundant. <code class="docutils literal notranslate"><span class="pre">sku</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code> or <code class="docutils literal notranslate"><span class="pre">8</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</p></li>
<li><p><strong>default_primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>default_secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Options are basic, standard or premium.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this resource is zone redundant. <code class="docutils literal notranslate"><span class="pre">sku</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">NamespaceAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace authorization Rule within a ServiceBus.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_namespace_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_namespace_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NamespaceAuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the ServiceBus Namespace authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the ServiceBus Namespace authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the ServiceBus Namespace authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the ServiceBus Namespace authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Queue.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</p></li>
<li><p><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p></li>
<li><p><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.dead_lettering_on_message_expiration">
<code class="sig-name descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.duplicate_detection_history_time_window">
<code class="sig-name descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.enable_express">
<code class="sig-name descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.enable_partitioning">
<code class="sig-name descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.lock_duration">
<code class="sig-name descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.max_delivery_count">
<code class="sig-name descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.max_size_in_megabytes">
<code class="sig-name descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.requires_duplicate_detection">
<code class="sig-name descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.requires_session">
<code class="sig-name descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</p></li>
<li><p><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p></li>
<li><p><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">QueueAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule for a ServiceBus Queue.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_queue_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_queue_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.queue_name">
<code class="sig-name descname">queue_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.queue_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QueueAuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the Authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the Authorization Rule.</p></li>
<li><p><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the Authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the Authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Subscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">Subscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">forward_dead_lettered_messages_to=None</em>, <em class="sig-param">forward_to=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Subscription.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.</p></li>
<li><p><strong>forward_dead_lettered_messages_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward Dead Letter messages to.</p></li>
<li><p><strong>forward_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward messages to.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of deliveries.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.dead_lettering_on_message_expiration">
<code class="sig-name descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.enable_batched_operations">
<code class="sig-name descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.forward_dead_lettered_messages_to">
<code class="sig-name descname">forward_dead_lettered_messages_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.forward_dead_lettered_messages_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Queue or Topic to automatically forward Dead Letter messages to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.forward_to">
<code class="sig-name descname">forward_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.forward_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Queue or Topic to automatically forward messages to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.lock_duration">
<code class="sig-name descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.max_delivery_count">
<code class="sig-name descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of deliveries.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.requires_session">
<code class="sig-name descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Subscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">forward_dead_lettered_messages_to=None</em>, <em class="sig-param">forward_to=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.</p></li>
<li><p><strong>forward_dead_lettered_messages_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward Dead Letter messages to.</p></li>
<li><p><strong>forward_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward messages to.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of deliveries.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Subscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Subscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.SubscriptionRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">SubscriptionRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">correlation_filter=None</em>, <em class="sig-param">filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sql_filter=None</em>, <em class="sig-param">subscription_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Subscription Rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_subscription_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_subscription_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</p></li>
<li><p><strong>correlation_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">correlation_filter</span></code> block as documented below to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p></li>
<li><p><strong>filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sql_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</p></li>
<li><p><strong>subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>correlation_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Content type of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">correlationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the correlation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Application specific label.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Address of the queue to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Session identifier to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Session identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Address to send to.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.correlation_filter">
<code class="sig-name descname">correlation_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.correlation_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">correlation_filter</span></code> block as documented below to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Content type of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">correlationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the correlation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Application specific label.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Address of the queue to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Session identifier to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Session identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Address to send to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.filter_type">
<code class="sig-name descname">filter_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.sql_filter">
<code class="sig-name descname">sql_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.sql_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.subscription_name">
<code class="sig-name descname">subscription_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.SubscriptionRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">correlation_filter=None</em>, <em class="sig-param">filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sql_filter=None</em>, <em class="sig-param">subscription_name=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubscriptionRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</p></li>
<li><p><strong>correlation_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">correlation_filter</span></code> block as documented below to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p></li>
<li><p><strong>filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sql_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</p></li>
<li><p><strong>subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>correlation_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Content type of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">correlationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the correlation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Application specific label.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Address of the queue to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Session identifier to reply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Session identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Address to send to.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.SubscriptionRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.SubscriptionRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">support_ordering=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Topic.</p>
<p><strong>Note</strong> Topics can only be created in Namespaces with an SKU of <code class="docutils literal notranslate"><span class="pre">standard</span></code> or higher.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</p></li>
<li><p><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</p></li>
<li><p><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</p></li>
<li><p><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p></li>
<li><p><strong>support_ordering</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.duplicate_detection_history_time_window">
<code class="sig-name descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_batched_operations">
<code class="sig-name descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_express">
<code class="sig-name descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_partitioning">
<code class="sig-name descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.max_size_in_megabytes">
<code class="sig-name descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.requires_duplicate_detection">
<code class="sig-name descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.support_ordering">
<code class="sig-name descname">support_ordering</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.support_ordering" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">support_ordering=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</p></li>
<li><p><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</p></li>
<li><p><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</p></li>
<li><p><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p></li>
<li><p><strong>support_ordering</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">TopicAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Topic authorization Rule within a ServiceBus Topic.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_topic_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_topic_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicAuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Connection String for the ServiceBus Topic authorization Rule.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key for the ServiceBus Topic authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Connection String for the ServiceBus Topic authorization Rule.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key for the ServiceBus Topic authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.eventhub.get_authorization_rule">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_authorization_rule</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_authorization_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Event Hubs Authorization Rule within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>eventhub_name</strong> (<em>str</em>) – Specifies the name of the EventHub.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the EventHub Authorization Rule resource. be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – Specifies the name of the grandparent EventHub Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the EventHub Authorization Rule’s grandparent Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_consume_group">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_consume_group</code><span class="sig-paren">(</span><em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_consume_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Event Hubs Consumer Group within an Event Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_consumer_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_consumer_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>eventhub_name</strong> (<em>str</em>) – Specifies the name of the EventHub.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the EventHub Consumer Group resource.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – Specifies the name of the grandparent EventHub Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_eventhub_namespace">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_eventhub_namespace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_eventhub_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing EventHub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the EventHub Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the EventHub Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_namespace">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_namespace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing EventHub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the EventHub Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the EventHub Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_namespace_authorization_rule">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_namespace_authorization_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_namespace_authorization_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an Authorization Rule for an Event Hub Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_namespace_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the EventHub Authorization Rule resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the EventHub Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_service_bus_namespace">
<code class="sig-prename descclassname">pulumi_azure.eventhub.</code><code class="sig-name descname">get_service_bus_namespace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_service_bus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing ServiceBus Namespace.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/servicebus_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/servicebus_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the ServiceBus Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the ServiceBus Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
