---
title: Module servicebus
title_tag: Module servicebus | Package pulumi_azure | Python SDK
linktitle: servicebus
notitle: true
---

<div class="section" id="servicebus">
<h1>servicebus<a class="headerlink" href="#servicebus" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.servicebus"></span><dl class="class">
<dt id="pulumi_azure.servicebus.AwaitableGetNamespaceAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">AwaitableGetNamespaceAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.AwaitableGetNamespaceAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.AwaitableGetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">AwaitableGetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.AwaitableGetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.AwaitableGetTopicAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">AwaitableGetTopicAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.AwaitableGetTopicAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">GetNamespaceAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespaceAuthorizationRule.</p>
<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the authorization rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceAuthorizationRuleResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.GetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">GetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The capacity of the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Resource Group in which the ServiceBus Namespace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tier used for the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetNamespaceResult.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetNamespaceResult.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this ServiceBus Namespace is zone redundant.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">GetTopicAuthorizationRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopicAuthorizationRule.</p>
<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.GetTopicAuthorizationRuleResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.servicebus.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace.</p>
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
<dt id="pulumi_azure.servicebus.Namespace.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code> or <code class="docutils literal notranslate"><span class="pre">8</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, capacity can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.default_primary_connection_string">
<code class="sig-name descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.default_primary_key">
<code class="sig-name descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.default_secondary_connection_string">
<code class="sig-name descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.default_secondary_key">
<code class="sig-name descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use. Options are basic, standard or premium.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Namespace.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this resource is zone redundant. <code class="docutils literal notranslate"><span class="pre">sku</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">capacity=None</em>, <em class="sig-param">default_primary_connection_string=None</em>, <em class="sig-param">default_primary_key=None</em>, <em class="sig-param">default_secondary_connection_string=None</em>, <em class="sig-param">default_secondary_key=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">NamespaceAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace authorization Rule within a ServiceBus.</p>
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
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.NamespaceAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">NamespaceNetworkRuleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">ip_rules=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">network_rules=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace Network Rule Set Set.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default action for the ServiceBus Namespace Network Rule Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>ip_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ServiceBus Namespace name to which to attach the ServiceBus Namespace Network Rule Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the ServiceBus Namespace Network Rule Set should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignore_missing_vnet_service_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Subnet ID which should be able to access this ServiceBus Namespace.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.default_action">
<code class="sig-name descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the default action for the ServiceBus Namespace Network Rule Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.ip_rules">
<code class="sig-name descname">ip_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.ip_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ServiceBus Namespace name to which to attach the ServiceBus Namespace Network Rule Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.network_rules">
<code class="sig-name descname">network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignore_missing_vnet_service_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Subnet ID which should be able to access this ServiceBus Namespace.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group where the ServiceBus Namespace Network Rule Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">ip_rules=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">network_rules=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NamespaceNetworkRuleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default action for the ServiceBus Namespace Network Rule Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>ip_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ServiceBus Namespace name to which to attach the ServiceBus Namespace Network Rule Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the ServiceBus Namespace Network Rule Set should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignore_missing_vnet_service_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Subnet ID which should be able to access this ServiceBus Namespace.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.NamespaceNetworkRuleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.NamespaceNetworkRuleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Queue.</p>
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
<dt id="pulumi_azure.servicebus.Queue.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.dead_lettering_on_message_expiration">
<code class="sig-name descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.duplicate_detection_history_time_window">
<code class="sig-name descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.enable_express">
<code class="sig-name descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.enable_partitioning">
<code class="sig-name descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.lock_duration">
<code class="sig-name descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.max_delivery_count">
<code class="sig-name descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.max_size_in_megabytes">
<code class="sig-name descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.requires_duplicate_detection">
<code class="sig-name descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.requires_session">
<code class="sig-name descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Queue.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Queue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Queue.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">QueueAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule for a ServiceBus Queue.</p>
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
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.queue_name">
<code class="sig-name descname">queue_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.queue_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.QueueAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.QueueAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Subscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">Subscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">forward_dead_lettered_messages_to=None</em>, <em class="sig-param">forward_to=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Subscription.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The idle interval after which the topic is automatically deleted as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The minimum duration is <code class="docutils literal notranslate"><span class="pre">5</span></code> minutes or <code class="docutils literal notranslate"><span class="pre">P5M</span></code>.</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Default message timespan to live as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</p>
</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Subscription supports batched operations. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>forward_dead_lettered_messages_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward Dead Letter messages to.</p></li>
<li><p><strong>forward_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward messages to.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The lock duration for the subscription as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> minute or <code class="docutils literal notranslate"><span class="pre">P1M</span></code>.</p>
</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of deliveries.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The idle interval after which the topic is automatically deleted as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The minimum duration is <code class="docutils literal notranslate"><span class="pre">5</span></code> minutes or <code class="docutils literal notranslate"><span class="pre">P5M</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.dead_lettering_on_message_expiration">
<code class="sig-name descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default message timespan to live as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.enable_batched_operations">
<code class="sig-name descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Subscription supports batched operations. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.forward_dead_lettered_messages_to">
<code class="sig-name descname">forward_dead_lettered_messages_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.forward_dead_lettered_messages_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Queue or Topic to automatically forward Dead Letter messages to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.forward_to">
<code class="sig-name descname">forward_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.forward_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Queue or Topic to automatically forward messages to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.lock_duration">
<code class="sig-name descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The lock duration for the subscription as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> minute or <code class="docutils literal notranslate"><span class="pre">P1M</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.max_delivery_count">
<code class="sig-name descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of deliveries.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.requires_session">
<code class="sig-name descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Subscription.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.Subscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">dead_lettering_on_message_expiration=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">forward_dead_lettered_messages_to=None</em>, <em class="sig-param">forward_to=None</em>, <em class="sig-param">lock_duration=None</em>, <em class="sig-param">max_delivery_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_session=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The idle interval after which the topic is automatically deleted as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The minimum duration is <code class="docutils literal notranslate"><span class="pre">5</span></code> minutes or <code class="docutils literal notranslate"><span class="pre">P5M</span></code>.</p>
</p></li>
<li><p><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Default message timespan to live as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</p>
</p></li>
<li><p><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Subscription supports batched operations. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>forward_dead_lettered_messages_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward Dead Letter messages to.</p></li>
<li><p><strong>forward_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward messages to.</p></li>
<li><p><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The lock duration for the subscription as an <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration</a>. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> minute or <code class="docutils literal notranslate"><span class="pre">P1M</span></code>.</p>
</p></li>
<li><p><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of deliveries.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.Subscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Subscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.SubscriptionRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">SubscriptionRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">correlation_filter=None</em>, <em class="sig-param">filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sql_filter=None</em>, <em class="sig-param">subscription_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Subscription Rule.</p>
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
<dt id="pulumi_azure.servicebus.SubscriptionRule.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.correlation_filter">
<code class="sig-name descname">correlation_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.correlation_filter" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.SubscriptionRule.filter_type">
<code class="sig-name descname">filter_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.sql_filter">
<code class="sig-name descname">sql_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.sql_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.subscription_name">
<code class="sig-name descname">subscription_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.SubscriptionRule.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.SubscriptionRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">correlation_filter=None</em>, <em class="sig-param">filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sql_filter=None</em>, <em class="sig-param">subscription_name=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.SubscriptionRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.SubscriptionRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.SubscriptionRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">support_ordering=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Topic.</p>
<p><strong>Note</strong> Topics can only be created in Namespaces with an SKU of <code class="docutils literal notranslate"><span class="pre">standard</span></code> or higher.</p>
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
<dt id="pulumi_azure.servicebus.Topic.auto_delete_on_idle">
<code class="sig-name descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.default_message_ttl">
<code class="sig-name descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.duplicate_detection_history_time_window">
<code class="sig-name descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.enable_batched_operations">
<code class="sig-name descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.enable_express">
<code class="sig-name descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.enable_partitioning">
<code class="sig-name descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.max_size_in_megabytes">
<code class="sig-name descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.requires_duplicate_detection">
<code class="sig-name descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.Topic.support_ordering">
<code class="sig-name descname">support_ordering</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.Topic.support_ordering" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_delete_on_idle=None</em>, <em class="sig-param">default_message_ttl=None</em>, <em class="sig-param">duplicate_detection_history_time_window=None</em>, <em class="sig-param">enable_batched_operations=None</em>, <em class="sig-param">enable_express=None</em>, <em class="sig-param">enable_partitioning=None</em>, <em class="sig-param">max_size_in_megabytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">requires_duplicate_detection=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">support_ordering=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Topic.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">TopicAuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Topic authorization Rule within a ServiceBus Topic.</p>
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
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.TopicAuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.TopicAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicebus.get_namespace">
<code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">get_namespace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.get_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing ServiceBus Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the ServiceBus Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the ServiceBus Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.servicebus.get_namespace_authorization_rule">
<code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">get_namespace_authorization_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.get_namespace_authorization_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing ServiceBus Namespace Authorization Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the ServiceBus Namespace Authorization Rule.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – Specifies the name of the ServiceBus Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the ServiceBus Namespace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.servicebus.get_topic_authorization_rule">
<code class="sig-prename descclassname">pulumi_azure.servicebus.</code><code class="sig-name descname">get_topic_authorization_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicebus.get_topic_authorization_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a ServiceBus Topic Authorization Rule within a ServiceBus Topic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the ServiceBus Topic Authorization Rule resource.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – The name of the ServiceBus Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the ServiceBus Namespace exists.</p></li>
<li><p><strong>topic_name</strong> (<em>str</em>) – The name of the ServiceBus Topic.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
