---
title: Module securitycenter
title_tag: Module securitycenter | Package pulumi_azure | Python SDK
linktitle: securitycenter
notitle: true
---

<div class="section" id="securitycenter">
<h1>securitycenter<a class="headerlink" href="#securitycenter" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.securitycenter"></span><dl class="class">
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.securitycenter.</code><code class="sig-name descname">AdvancedThreatProtection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a resources Advanced Threat Protection setting.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Advanced Threat Protection be enabled on this resource?</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure Resource which to enable Advanced Threat Protection on. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Advanced Threat Protection be enabled on this resource?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Azure Resource which to enable Advanced Threat Protection on. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AdvancedThreatProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Advanced Threat Protection be enabled on this resource?</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure Resource which to enable Advanced Threat Protection on. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.AdvancedThreatProtection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.AdvancedThreatProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Contact">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.securitycenter.</code><code class="sig-name descname">Contact</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_notifications=None</em>, <em class="sig-param">alerts_to_admins=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">phone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the subscription’s Security Center Contact.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Owner access permission is required.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to the security contact.</p></li>
<li><p><strong>alerts_to_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to subscription admins.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of the Security Center Contact.</p></li>
<li><p><strong>phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The phone number of the Security Center Contact.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.alert_notifications">
<code class="sig-name descname">alert_notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.alert_notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to send security alerts notifications to the security contact.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.alerts_to_admins">
<code class="sig-name descname">alerts_to_admins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.alerts_to_admins" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to send security alerts notifications to subscription admins.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of the Security Center Contact.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.phone">
<code class="sig-name descname">phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.phone" title="Permalink to this definition">¶</a></dt>
<dd><p>The phone number of the Security Center Contact.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Contact.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_notifications=None</em>, <em class="sig-param">alerts_to_admins=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">phone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Contact resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to the security contact.</p></li>
<li><p><strong>alerts_to_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to subscription admins.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of the Security Center Contact.</p></li>
<li><p><strong>phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The phone number of the Security Center Contact.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Contact.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Contact.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.SubscriptionPricing">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.securitycenter.</code><code class="sig-name descname">SubscriptionPricing</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the Pricing Tier for Azure Security Center in the current subscription.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource requires the <code class="docutils literal notranslate"><span class="pre">Owner</span></code> permission on the Subscription.</p>
<p><strong>NOTE:</strong> Deletion of this resource does not change or reset the pricing tier to <code class="docutils literal notranslate"><span class="pre">Free</span></code></p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing tier to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing tier to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubscriptionPricing resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing tier to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Workspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.securitycenter.</code><code class="sig-name descname">Workspace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">workspace_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the subscription’s Security Center Workspace.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Owner access permission is required.</p>
<p><strong>NOTE:</strong> The subscription’s pricing model can not be <code class="docutils literal notranslate"><span class="pre">Free</span></code> for this to have any affect.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.</p></li>
<li><p><strong>workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace to save the data in.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Workspace.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Workspace.workspace_id">
<code class="sig-name descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Log Analytics Workspace to save the data in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Workspace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">workspace_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workspace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.</p></li>
<li><p><strong>workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace to save the data in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Workspace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Workspace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
