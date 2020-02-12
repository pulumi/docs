---
title: Module notificationhub
title_tag: Module notificationhub | Package pulumi_azure | Python SDK
linktitle: notificationhub
notitle: true
---

<div class="section" id="notificationhub">
<h1>notificationhub<a class="headerlink" href="#notificationhub" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.notificationhub"></span><dl class="class">
<dt id="pulumi_azure.notificationhub.AuthorizationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">AuthorizationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">notification_hub_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule associated with a Notification Hub within a Notification Hub Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification_hub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.listen">
<code class="sig-name descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Listen access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.manage">
<code class="sig-name descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Manage access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.notification_hub_name">
<code class="sig-name descname">notification_hub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.notification_hub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key associated with this Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key associated with this Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Send access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">listen=None</em>, <em class="sig-param">manage=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">notification_hub_name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthorizationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Authorization Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification_hub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Access Key associated with this Authorization Rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Access Key associated with this Authorization Rule.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send access to the Notification Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_authorization_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.AuthorizationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.AwaitableGetHubResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">AwaitableGetHubResult</code><span class="sig-paren">(</span><em class="sig-param">apns_credentials=None</em>, <em class="sig-param">gcm_credentials=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AwaitableGetHubResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.AwaitableGetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">AwaitableGetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">servicebus_endpoint=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AwaitableGetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.GetHubResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">GetHubResult</code><span class="sig-paren">(</span><em class="sig-param">apns_credentials=None</em>, <em class="sig-param">gcm_credentials=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getHub.</p>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.apns_credentials">
<code class="sig-name descname">apns_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.apns_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">apns_credential</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.gcm_credentials">
<code class="sig-name descname">gcm_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.gcm_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gcm_credential</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">GetNamespaceResult</code><span class="sig-paren">(</span><em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">servicebus_endpoint=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Notification Hub Namespace enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SKU to use for this Notification Hub Namespace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard.</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.namespace_type">
<code class="sig-name descname">namespace_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.namespace_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Namespace, such as <code class="docutils literal notranslate"><span class="pre">Messaging</span></code> or <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.Hub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">Hub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apns_credential=None</em>, <em class="sig-param">gcm_credential=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Notification Hub within a Notification Hub Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apns_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">apns_credential</span></code> block as defined below.</p></li>
<li><p><strong>gcm_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gcm_credential</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>apns_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bundleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gcm_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.apns_credential">
<code class="sig-name descname">apns_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.apns_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">apns_credential</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bundleId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.gcm_credential">
<code class="sig-name descname">gcm_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.gcm_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gcm_credential</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Notification Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Hub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apns_credential=None</em>, <em class="sig-param">gcm_credential=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apns_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">apns_credential</span></code> block as defined below.</p></li>
<li><p><strong>gcm_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gcm_credential</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>apns_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bundleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gcm_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Hub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.Hub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Notification Hub Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Notification Hub Namespace enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Type of Namespace - possible values are <code class="docutils literal notranslate"><span class="pre">Messaging</span></code> or <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SKU to use for this Notification Hub Namespace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Notification Hub Namespace enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.namespace_type">
<code class="sig-name descname">namespace_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.namespace_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Namespace - possible values are <code class="docutils literal notranslate"><span class="pre">Messaging</span></code> or <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.servicebus_endpoint">
<code class="sig-name descname">servicebus_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.servicebus_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The ServiceBus Endpoint for this Notification Hub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SKU to use for this Notification Hub Namespace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">servicebus_endpoint=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sku_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Notification Hub Namespace enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Type of Namespace - possible values are <code class="docutils literal notranslate"><span class="pre">Messaging</span></code> or <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>servicebus_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ServiceBus Endpoint for this Notification Hub Namespace.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SKU to use for this Notification Hub Namespace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/notification_hub_namespace.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.get_hub">
<code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">get_hub</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">namespace_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.get_hub" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Notification Hub within a Notification Hub Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Notification Hub.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – Specifies the Name of the Notification Hub Namespace which contains the Notification Hub.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the Notification Hub exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.notificationhub.get_namespace">
<code class="sig-prename descclassname">pulumi_azure.notificationhub.</code><code class="sig-name descname">get_namespace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.get_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Notification Hub Namespace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Notification Hub Namespace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the Notification Hub exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub_namespace.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
