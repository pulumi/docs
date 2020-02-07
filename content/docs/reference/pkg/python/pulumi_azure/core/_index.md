---
title: Module core
title_tag: Module core | Package pulumi_azure | Python SDK
linktitle: core
notitle: true
---

<div class="section" id="core">
<h1>core<a class="headerlink" href="#core" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.core"></span><dl class="class">
<dt id="pulumi_azure.core.AwaitableGetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">service_principal_application_id=None</em>, <em class="sig-param">service_principal_object_id=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.AwaitableGetResourceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetResourceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetResourceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.AwaitableGetResourcesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetResourcesResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">required_tags=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetResourcesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.AwaitableGetSubscriptionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetSubscriptionResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">location_placement_id=None</em>, <em class="sig-param">quota_id=None</em>, <em class="sig-param">spending_limit=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetSubscriptionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.AwaitableGetSubscriptionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetSubscriptionsResult</code><span class="sig-paren">(</span><em class="sig-param">display_name_contains=None</em>, <em class="sig-param">display_name_prefix=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetSubscriptionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.AwaitableGetUserAssignedIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">AwaitableGetUserAssignedIdentityResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.AwaitableGetUserAssignedIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">service_principal_application_id=None</em>, <em class="sig-param">service_principal_object_id=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetClientConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetResourceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetResourceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetResourceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetResourceGroupResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourceGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetResourceGroupResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourceGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetResourceGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourceGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetResourcesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetResourcesResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">required_tags=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetResourcesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResources.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetResourcesResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourcesResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetResourcesResult.resources">
<code class="sig-name descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourcesResult.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">resource</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetResourcesResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourcesResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this Resource. (e.g. <code class="docutils literal notranslate"><span class="pre">Microsoft.Network/virtualNetworks</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetResourcesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetResourcesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetSubscriptionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetSubscriptionResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">location_placement_id=None</em>, <em class="sig-param">quota_id=None</em>, <em class="sig-param">spending_limit=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubscription.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.location_placement_id">
<code class="sig-name descname">location_placement_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.location_placement_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription location placement ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.quota_id">
<code class="sig-name descname">quota_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.quota_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription quota ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.spending_limit">
<code class="sig-name descname">spending_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.spending_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription spending limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.subscription_id">
<code class="sig-name descname">subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription GUID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription tenant ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetSubscriptionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetSubscriptionsResult</code><span class="sig-paren">(</span><em class="sig-param">display_name_contains=None</em>, <em class="sig-param">display_name_prefix=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubscriptions.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionsResult.subscriptions">
<code class="sig-name descname">subscriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionsResult.subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">subscription</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetSubscriptionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetSubscriptionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">GetUserAssignedIdentityResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUserAssignedIdentity.</p>
<dl class="attribute">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client ID of the User Assigned Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the User Assigned Identity exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult.principal_id">
<code class="sig-name descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Principal ID of the User Assigned Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the User Assigned Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.GetUserAssignedIdentityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.GetUserAssignedIdentityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.core.ResourceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">ResourceGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.ResourceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a resource group on Azure.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the resource group should be created.
For a list of all Azure locations, please consult <a class="reference external" href="http://azure.microsoft.com/en-us/regions/">this link</a> or run <code class="docutils literal notranslate"><span class="pre">az</span> <span class="pre">account</span> <span class="pre">list-locations</span> <span class="pre">--output</span> <span class="pre">table</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Must be unique on your
Azure subscription.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/resource_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/resource_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.core.ResourceGroup.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the resource group should be created.
For a list of all Azure locations, please consult <a class="reference external" href="http://azure.microsoft.com/en-us/regions/">this link</a> or run <code class="docutils literal notranslate"><span class="pre">az</span> <span class="pre">account</span> <span class="pre">list-locations</span> <span class="pre">--output</span> <span class="pre">table</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.ResourceGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group. Must be unique on your
Azure subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.ResourceGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.core.ResourceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The location where the resource group should be created.
For a list of all Azure locations, please consult <a class="reference external" href="http://azure.microsoft.com/en-us/regions/">this link</a> or run <code class="docutils literal notranslate"><span class="pre">az</span> <span class="pre">account</span> <span class="pre">list-locations</span> <span class="pre">--output</span> <span class="pre">table</span></code>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Must be unique on your
Azure subscription.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/resource_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/resource_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.core.ResourceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.core.ResourceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.ResourceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.core.TemplateDeployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">TemplateDeployment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">parameters_body=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">template_body=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TemplateDeployment resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deployment_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode that is used to deploy resources. This value could be either <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> or <code class="docutils literal notranslate"><span class="pre">Complete</span></code>.
Note that you will almost <em>always</em> want this to be set to <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> otherwise the deployment will destroy all infrastructure not
specified within the template, and this provider will not be aware of this.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the template deployment. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the name and value pairs that define the deployment parameters for the template.</p></li>
<li><p><strong>parameters_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the template deployment.</p></li>
<li><p><strong>template_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON definition for the template.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/template_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/template_deployment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.deployment_mode">
<code class="sig-name descname">deployment_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.deployment_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mode that is used to deploy resources. This value could be either <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> or <code class="docutils literal notranslate"><span class="pre">Complete</span></code>.
Note that you will almost <em>always</em> want this to be set to <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> otherwise the deployment will destroy all infrastructure not
specified within the template, and this provider will not be aware of this.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the template deployment. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.outputs">
<code class="sig-name descname">outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using <code class="docutils literal notranslate"><span class="pre">.outputs[&quot;name&quot;]</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name and value pairs that define the deployment parameters for the template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.parameters_body">
<code class="sig-name descname">parameters_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.parameters_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the template deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.core.TemplateDeployment.template_body">
<code class="sig-name descname">template_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.template_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the JSON definition for the template.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.core.TemplateDeployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outputs=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">parameters_body=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">template_body=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TemplateDeployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deployment_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode that is used to deploy resources. This value could be either <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> or <code class="docutils literal notranslate"><span class="pre">Complete</span></code>.
Note that you will almost <em>always</em> want this to be set to <code class="docutils literal notranslate"><span class="pre">Incremental</span></code> otherwise the deployment will destroy all infrastructure not
specified within the template, and this provider will not be aware of this.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the template deployment. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>outputs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using <code class="docutils literal notranslate"><span class="pre">.outputs[&quot;name&quot;]</span></code>.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the name and value pairs that define the deployment parameters for the template.</p></li>
<li><p><strong>parameters_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the template deployment.</p></li>
<li><p><strong>template_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON definition for the template.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/template_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/template_deployment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.core.TemplateDeployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.core.TemplateDeployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.TemplateDeployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.core.get_client_config">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_client_config</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the configuration of the AzureRM provider.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/client_config.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/client_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.core.get_resource_group">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_resource_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Resource Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specifies the name of the resource group.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/resource_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/resource_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.core.get_resources">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_resources</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">required_tags=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about existing resources.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Resource.</p></li>
<li><p><strong>required_tags</strong> (<em>dict</em>) – A mapping of tags which the resource has to have in order to be included in the result.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource group where the Resources are located.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The Resource Type of the Resources you want to list (e.g. <code class="docutils literal notranslate"><span class="pre">Microsoft.Network/virtualNetworks</span></code>). A full list of available Resource Types can be found <a class="reference external" href="https://docs.microsoft.com/en-us/azure/azure-resource-manager/azure-services-resource-providers">here</a>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/resources.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/resources.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.core.get_subscription">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_subscription</code><span class="sig-paren">(</span><em class="sig-param">subscription_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Subscription.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>subscription_id</strong> (<em>str</em>) – Specifies the ID of the subscription. If this argument is omitted, the subscription ID of the current Azure Resource Manager provider is used.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subscription.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.core.get_subscriptions">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_subscriptions</code><span class="sig-paren">(</span><em class="sig-param">display_name_contains=None</em>, <em class="sig-param">display_name_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about all the Subscriptions currently available.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name_contains</strong> (<em>str</em>) – A case-insensitive value which must be contained within the <code class="docutils literal notranslate"><span class="pre">display_name</span></code> field, used to filter the results</p></li>
<li><p><strong>display_name_prefix</strong> (<em>str</em>) – A case-insensitive prefix which can be used to filter on the <code class="docutils literal notranslate"><span class="pre">display_name</span></code> field</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subscriptions.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subscriptions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.core.get_user_assigned_identity">
<code class="sig-prename descclassname">pulumi_azure.core.</code><code class="sig-name descname">get_user_assigned_identity</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.core.get_user_assigned_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing User Assigned Identity.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the User Assigned Identity.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the User Assigned Identity exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/user_assigned_identity_legacy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/user_assigned_identity_legacy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
