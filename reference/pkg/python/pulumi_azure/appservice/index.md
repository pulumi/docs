<div class="section" id="module-pulumi_azure.appservice">
<span id="appservice"></span><h1>appservice<a class="headerlink" href="#module-pulumi_azure.appservice" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.appservice.ActiveSlot">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">ActiveSlot</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_name=None</em>, <em>app_service_slot_name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot" title="Permalink to this definition">¶</a></dt>
<dd><p>Promotes an App Service Slot to Production within an App Service.</p>
<p>-&gt; <strong>Note:</strong> When using Slots - the <cite>app_settings</cite>, <cite>connection_string</cite> and <cite>site_config</cite> blocks on the <cite>azurerm_app_service</cite> resource will be overwritten when promoting a Slot using the <cite>azurerm_app_service_active_slot</cite> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.</li>
<li><strong>app_service_slot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service Slot which should be promoted to the Production Slot within the App Service.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.app_service_name">
<code class="descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.app_service_slot_name">
<code class="descname">app_service_slot_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.app_service_slot_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service Slot which should be promoted to the Production Slot within the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.ActiveSlot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.ActiveSlot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AppService">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">AppService</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_plan_id=None</em>, <em>app_settings=None</em>, <em>client_affinity_enabled=None</em>, <em>connection_strings=None</em>, <em>enabled=None</em>, <em>https_only=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>site_config=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service (within an App Service Plan).</p>
<p>-&gt; <strong>Note:</strong> When using Slots - the <cite>app_settings</cite>, <cite>connection_string</cite> and <cite>site_config</cite> blocks on the <cite>azurerm_app_service</cite> resource will be overwritten when promoting a Slot using the <cite>azurerm_app_service_active_slot</cite> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.</li>
<li><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</li>
<li><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?</li>
<li><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <cite>connection_string</cite> block as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Enabled? Changing this forces a new resource to be created.</li>
<li><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service only be accessed via HTTPS? Defaults to <cite>false</cite>.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Connection String.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service.</li>
<li><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>site_config</cite> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.app_service_plan_id">
<code class="descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this App Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.app_settings">
<code class="descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.client_affinity_enabled">
<code class="descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.connection_strings">
<code class="descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>connection_string</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.default_site_hostname">
<code class="descname">default_site_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.default_site_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Hostname associated with the App Service - such as <cite>mysite.azurewebsites.net</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Enabled? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.https_only">
<code class="descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service only be accessed via HTTPS? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A Managed Service Identity block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Connection String.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.outbound_ip_addresses">
<code class="descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <cite>52.23.25.3,52.143.43.12</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.possible_outbound_ip_addresses">
<code class="descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <cite>52.23.25.3,52.143.43.12,52.143.43.17</cite> - not all of which are necessarily in use. Superset of <cite>outbound_ip_addresses</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.site_config">
<code class="descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_config</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.site_credential">
<code class="descname">site_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.site_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_credential</cite> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.source_control">
<code class="descname">source_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.source_control" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>source_control</cite> block as defined below, which contains the Source Control information when <cite>scm_type</cite> is set to <cite>LocalGit</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.AppService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.AppService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.CustomHostnameBinding">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">CustomHostnameBinding</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_name=None</em>, <em>hostname=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Hostname Binding within an App Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.</li>
<li><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Custom Hostname to use for the App Service, example <cite>www.example.com</cite>. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.app_service_name">
<code class="descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Custom Hostname to use for the App Service, example <cite>www.example.com</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.FunctionApp">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">FunctionApp</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_plan_id=None</em>, <em>app_settings=None</em>, <em>client_affinity_enabled=None</em>, <em>connection_strings=None</em>, <em>enable_builtin_logging=None</em>, <em>enabled=None</em>, <em>https_only=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>site_config=None</em>, <em>storage_connection_string=None</em>, <em>tags=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Function App.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.</li>
<li><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</li>
<li><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?</li>
<li><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <cite>connection_string</cite> block as defined below.</li>
<li><strong>enable_builtin_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the built-in logging of this Function App be enabled? Defaults to <cite>true</cite>.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the Function App enabled?</li>
<li><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the Function App only be accessed via HTTPS? Defaults to <cite>false</cite>.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <cite>identity</cite> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Connection String.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Function App.</li>
<li><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>site_config</cite> object as defined below.</li>
<li><strong>storage_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime version associated with the Function App. Defaults to <cite>~1</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.app_service_plan_id">
<code class="descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.app_settings">
<code class="descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.client_affinity_enabled">
<code class="descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.connection_strings">
<code class="descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>connection_string</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.default_hostname">
<code class="descname">default_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.default_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default hostname associated with the Function App - such as <cite>mysite.azurewebsites.net</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.enable_builtin_logging">
<code class="descname">enable_builtin_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.enable_builtin_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the built-in logging of this Function App be enabled? Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Function App enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.https_only">
<code class="descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the Function App only be accessed via HTTPS? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>identity</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Connection String.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.outbound_ip_addresses">
<code class="descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <cite>52.23.25.3,52.143.43.12</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Function App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.site_config">
<code class="descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_config</cite> object as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.site_credential">
<code class="descname">site_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.site_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_credential</cite> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.storage_connection_string">
<code class="descname">storage_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.storage_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime version associated with the Function App. Defaults to <cite>~1</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.FunctionApp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.FunctionApp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">GetAppServicePlanResult</code><span class="sig-paren">(</span><em>kind=None</em>, <em>location=None</em>, <em>maximum_number_of_workers=None</em>, <em>properties=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppServicePlan.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Operating System type of the App Service Plan</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the App Service Plan exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.maximum_number_of_workers">
<code class="descname">maximum_number_of_workers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.maximum_number_of_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of instances that can be assigned to this App Service plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.properties">
<code class="descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>properties</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetAppServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">GetAppServiceResult</code><span class="sig-paren">(</span><em>app_service_plan_id=None</em>, <em>app_settings=None</em>, <em>client_affinity_enabled=None</em>, <em>connection_strings=None</em>, <em>default_site_hostname=None</em>, <em>enabled=None</em>, <em>https_only=None</em>, <em>location=None</em>, <em>outbound_ip_addresses=None</em>, <em>possible_outbound_ip_addresses=None</em>, <em>site_config=None</em>, <em>site_credentials=None</em>, <em>source_controls=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppService.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.app_service_plan_id">
<code class="descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which the App Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.app_settings">
<code class="descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings for the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.client_affinity_enabled">
<code class="descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.connection_strings">
<code class="descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>connection_string</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.https_only">
<code class="descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service only be accessed via HTTPS?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the App Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.outbound_ip_addresses">
<code class="descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <cite>52.23.25.3,52.143.43.12</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.possible_outbound_ip_addresses">
<code class="descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <cite>52.23.25.3,52.143.43.12,52.143.43.17</cite> - not all of which are necessarily in use. Superset of <cite>outbound_ip_addresses</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.site_config">
<code class="descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_config</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.Plan">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">Plan</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_environment_id=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>per_site_scaling=None</em>, <em>properties=None</em>, <em>reserved=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an App Service Plan component.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.</li>
<li><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of the App Service Plan to create. Possible values are <cite>Windows</cite> (also available as <cite>App</cite>), <cite>Linux</cite> and <cite>FunctionApp</cite> (for a Consumption Plan). Defaults to <cite>Windows</cite>. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.</li>
<li><strong>per_site_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can Apps assigned to this App Service Plan be scaled independently? If set to <cite>false</cite> apps assigned to this plan will scale to all instances of the plan.  Defaults to <cite>false</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] properties
:param pulumi.Input[bool] reserved: Is this App Service Plan <cite>Reserved</cite>. Defaults to <cite>false</cite>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Service Plan component.
:param pulumi.Input[dict] sku: A <cite>sku</cite> block as documented below.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.app_service_environment_id">
<code class="descname">app_service_environment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.app_service_environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of the App Service Plan to create. Possible values are <cite>Windows</cite> (also available as <cite>App</cite>), <cite>Linux</cite> and <cite>FunctionApp</cite> (for a Consumption Plan). Defaults to <cite>Windows</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.maximum_number_of_workers">
<code class="descname">maximum_number_of_workers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.maximum_number_of_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of workers supported with the App Service Plan’s sku.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.per_site_scaling">
<code class="descname">per_site_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.per_site_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Apps assigned to this App Service Plan be scaled independently? If set to <cite>false</cite> apps assigned to this plan will scale to all instances of the plan.  Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.reserved">
<code class="descname">reserved</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.reserved" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this App Service Plan <cite>Reserved</cite>. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service Plan component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Plan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Plan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.Slot">
<em class="property">class </em><code class="descclassname">pulumi_azure.appservice.</code><code class="descname">Slot</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_service_name=None</em>, <em>app_service_plan_id=None</em>, <em>app_settings=None</em>, <em>client_affinity_enabled=None</em>, <em>connection_strings=None</em>, <em>enabled=None</em>, <em>https_only=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>site_config=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Slot (within an App Service).</p>
<p>-&gt; <strong>Note:</strong> When using Slots - the <cite>app_settings</cite>, <cite>connection_string</cite> and <cite>site_config</cite> blocks on the <cite>azurerm_app_service</cite> resource will be overwritten when promoting a Slot using the <cite>azurerm_app_service_active_slot</cite> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.</li>
<li><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.</li>
<li><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</li>
<li><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?</li>
<li><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <cite>connection_string</cite> block as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Slot Enabled?</li>
<li><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service Slot only be accessed via HTTPS? Defaults to <cite>false</cite>.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Connection String.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service Slot component.</li>
<li><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>site_config</cite> object as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_service_name">
<code class="descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_service_plan_id">
<code class="descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_settings">
<code class="descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.client_affinity_enabled">
<code class="descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.connection_strings">
<code class="descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>connection_string</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.default_site_hostname">
<code class="descname">default_site_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.default_site_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Hostname associated with the App Service Slot - such as <cite>mysite.azurewebsites.net</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Slot Enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.https_only">
<code class="descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service Slot only be accessed via HTTPS? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A Managed Service Identity block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Connection String.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service Slot component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.site_config">
<code class="descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>site_config</cite> object as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Slot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Slot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_app_service">
<code class="descclassname">pulumi_azure.appservice.</code><code class="descname">get_app_service</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>site_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_app_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_app_service_plan">
<code class="descclassname">pulumi_azure.appservice.</code><code class="descname">get_app_service_plan</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_app_service_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service Plan (formerly known as a <cite>Server Farm</cite>).</p>
</dd></dl>

</div>
