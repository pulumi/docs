<div class="section" id="module-pulumi_azure.notificationhub">
<span id="notificationhub"></span><h1>notificationhub<a class="headerlink" href="#module-pulumi_azure.notificationhub" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.notificationhub.AuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">AuthorizationRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>listen=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>notification_hub_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule associated with a Notification Hub within a Notification Hub Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen access to the Notification Hub? Defaults to <cite>false</cite>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage access to the Notification Hub? Defaults to <cite>false</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Authorization Rule. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.</li>
<li><strong>notification_hub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send access to the Notification Hub? Defaults to <cite>false</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Listen access to the Notification Hub? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Manage access to the Notification Hub? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.notification_hub_name">
<code class="descname">notification_hub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.notification_hub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key associated with this Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key associated with this Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Send access to the Notification Hub? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.AuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.AuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.AuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.notificationhub.GetHubResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">GetHubResult</code><span class="sig-paren">(</span><em>apns_credentials=None</em>, <em>gcm_credentials=None</em>, <em>location=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getHub.</p>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.apns_credentials">
<code class="descname">apns_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.apns_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>apns_credential</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.gcm_credentials">
<code class="descname">gcm_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.gcm_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>gcm_credential</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetHubResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetHubResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">GetNamespaceResult</code><span class="sig-paren">(</span><em>enabled=None</em>, <em>location=None</em>, <em>namespace_type=None</em>, <em>servicebus_endpoint=None</em>, <em>sku=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Notification Hub Namespace enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.namespace_type">
<code class="descname">namespace_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.namespace_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Namespace, such as <cite>Messaging</cite> or <cite>NotificationHub</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.GetNamespaceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.GetNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.notificationhub.Hub">
<em class="property">class </em><code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">Hub</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>apns_credential=None</em>, <em>gcm_credential=None</em>, <em>location=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Notification Hub within a Notification Hub Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>apns_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>apns_credential</cite> block as defined below.</li>
<li><strong>gcm_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>gcm_credential</cite> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.apns_credential">
<code class="descname">apns_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.apns_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>apns_credential</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.gcm_credential">
<code class="descname">gcm_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.gcm_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>gcm_credential</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Notification Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Hub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Hub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.Hub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Hub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.notificationhub.Namespace">
<em class="property">class </em><code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">Namespace</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>name=None</em>, <em>namespace_type=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Notification Hub Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Notification Hub Namespace enabled? Defaults to <cite>true</cite>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which this Notification Hub Namespace should be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</li>
<li><strong>namespace_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Type of Namespace - possible values are <cite>Messaging</cite> or <cite>NotificationHub</cite>. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Notification Hub Namespace enabled? Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Notification Hub Namespace should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.namespace_type">
<code class="descname">namespace_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.namespace_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Namespace - possible values are <cite>Messaging</cite> or <cite>NotificationHub</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.servicebus_endpoint">
<code class="descname">servicebus_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.servicebus_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The ServiceBus Endpoint for this Notification Hub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.notificationhub.Namespace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.notificationhub.Namespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.notificationhub.Namespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.notificationhub.get_hub">
<code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">get_hub</code><span class="sig-paren">(</span><em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.get_hub" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Notification Hub within a Notification Hub Namespace.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.notificationhub.get_namespace">
<code class="descclassname">pulumi_azure.notificationhub.</code><code class="descname">get_namespace</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.notificationhub.get_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Notification Hub Namespace.</p>
</dd></dl>

</div>
