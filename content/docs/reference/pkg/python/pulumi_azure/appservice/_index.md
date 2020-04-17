---
title: Module appservice
title_tag: Module appservice | Package pulumi_azure | Python SDK
linktitle: appservice
notitle: true
---

<div class="section" id="appservice">
<h1>appservice<a class="headerlink" href="#appservice" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.appservice"></span><dl class="class">
<dt id="pulumi_azure.appservice.ActiveSlot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">ActiveSlot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">app_service_slot_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot" title="Permalink to this definition">¶</a></dt>
<dd><p>Promotes an App Service Slot to Production within an App Service.</p>
<blockquote>
<div><p><strong>Note:</strong> When using Slots - the <code class="docutils literal notranslate"><span class="pre">app_settings</span></code>, <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> and <code class="docutils literal notranslate"><span class="pre">site_config</span></code> blocks on the <code class="docutils literal notranslate"><span class="pre">appservice.AppService</span></code> resource will be overwritten when promoting a Slot using the <code class="docutils literal notranslate"><span class="pre">appservice.ActiveSlot</span></code> resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_service_slot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service Slot which should be promoted to the Production Slot within the App Service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.app_service_name">
<code class="sig-name descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.app_service_slot_name">
<code class="sig-name descname">app_service_slot_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.app_service_slot_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service Slot which should be promoted to the Production Slot within the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.ActiveSlot.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.ActiveSlot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">app_service_slot_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActiveSlot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_service_slot_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service Slot which should be promoted to the Production Slot within the App Service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.ActiveSlot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.ActiveSlot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.ActiveSlot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.AppService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AppService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">client_cert_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service (within an App Service Plan).</p>
<blockquote>
<div><p><strong>Note:</strong> When using Slots - the <code class="docutils literal notranslate"><span class="pre">app_settings</span></code>, <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> and <code class="docutils literal notranslate"><span class="pre">site_config</span></code> blocks on the <code class="docutils literal notranslate"><span class="pre">appservice.AppService</span></code> resource will be overwritten when promoting a Slot using the <code class="docutils literal notranslate"><span class="pre">appservice.ActiveSlot</span></code> resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backup</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>client_cert_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the App Service require client certificates for incoming requests? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> blocks as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">logs</span></code> block as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Backup enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name for this Backup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">schedule</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Sets how often the backup should be executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the unit of time for how often the backup should be executed. Possible values are <code class="docutils literal notranslate"><span class="pre">Day</span></code> or <code class="docutils literal notranslate"><span class="pre">Hour</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keepAtLeastOneBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPeriodInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after which Backups should be deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets when the schedule should start working.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SAS URL to a Storage Container where Backups should be saved.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">application_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The level at which to log. Possible values include <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Information</span></code>, <code class="docutils literal notranslate"><span class="pre">Verbose</span></code> and <code class="docutils literal notranslate"><span class="pre">Off</span></code>. <strong>NOTE:</strong> this field is not available for <code class="docutils literal notranslate"><span class="pre">http_logs</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">http_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">file_system</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionInMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum size in megabytes that http log files can use before being removed.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the .net framework’s CLR used in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State of FTP / FTPS service for this App Service. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address used for this IP Restriction in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JAVA</span></code>, <code class="docutils literal notranslate"><span class="pre">JETTY</span></code>, and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code> and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Linux App Framework and version for the App Service. Possible options are a Docker container (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>), a base-64 encoded Docker Compose file (<code class="docutils literal notranslate"><span class="pre">COMPOSE|${filebase64(&quot;compose.yml&quot;)}</span></code>) or a base-64 encoded Kubernetes Manifest (<code class="docutils literal notranslate"><span class="pre">KUBE|${filebase64(&quot;kubernetes.yml&quot;)}</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of PHP to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Python to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code> and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Source Control enabled for this App Service. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the App Service run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Windows Docker container image (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>)</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The access key for the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the storage within the site’s runtime environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the file share (container name, for Blob storage).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of storage. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureBlob</span></code> and <code class="docutils literal notranslate"><span class="pre">AzureFiles</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.app_service_plan_id">
<code class="sig-name descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.app_settings">
<code class="sig-name descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.auth_settings">
<code class="sig-name descname">auth_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.auth_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.backup">
<code class="sig-name descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">backup</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Backup enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name for this Backup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">schedule</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Sets how often the backup should be executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets the unit of time for how often the backup should be executed. Possible values are <code class="docutils literal notranslate"><span class="pre">Day</span></code> or <code class="docutils literal notranslate"><span class="pre">Hour</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keepAtLeastOneBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPeriodInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of days after which Backups should be deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets when the schedule should start working.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SAS URL to a Storage Container where Backups should be saved.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.client_affinity_enabled">
<code class="sig-name descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.client_cert_enabled">
<code class="sig-name descname">client_cert_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.client_cert_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the App Service require client certificates for incoming requests? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value for the Connection String.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.default_site_hostname">
<code class="sig-name descname">default_site_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.default_site_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Hostname associated with the App Service - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.https_only">
<code class="sig-name descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A Managed Service Identity block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.logs">
<code class="sig-name descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">logs</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">application_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The level at which to log. Possible values include <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Information</span></code>, <code class="docutils literal notranslate"><span class="pre">Verbose</span></code> and <code class="docutils literal notranslate"><span class="pre">Off</span></code>. <strong>NOTE:</strong> this field is not available for <code class="docutils literal notranslate"><span class="pre">http_logs</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">http_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystem</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">file_system</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionInMb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum size in megabytes that http log files can use before being removed.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the App Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.outbound_ip_addresses">
<code class="sig-name descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.possible_outbound_ip_addresses">
<code class="sig-name descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12,52.143.43.17</span></code> - not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.site_config">
<code class="sig-name descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the .net framework’s CLR used in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - State of FTP / FTPS service for this App Service. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP Address used for this IP Restriction in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JAVA</span></code>, <code class="docutils literal notranslate"><span class="pre">JETTY</span></code>, and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code> and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Linux App Framework and version for the App Service. Possible options are a Docker container (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>), a base-64 encoded Docker Compose file (<code class="docutils literal notranslate"><span class="pre">COMPOSE|${filebase64(&quot;compose.yml&quot;)}</span></code>) or a base-64 encoded Kubernetes Manifest (<code class="docutils literal notranslate"><span class="pre">KUBE|${filebase64(&quot;kubernetes.yml&quot;)}</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of PHP to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Python to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code> and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Source Control enabled for this App Service. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the App Service run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Windows Docker container image (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.site_credentials">
<code class="sig-name descname">site_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.site_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.source_controls">
<code class="sig-name descname">source_controls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.source_controls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source_control</span></code> block as defined below, which contains the Source Control information when <code class="docutils literal notranslate"><span class="pre">scm_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Branch name of the Git repository for this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - URL of the Git repository for this App Service.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The access key for the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to mount the storage within the site’s runtime environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the storage account identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the file share (container name, for Blob storage).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of storage. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureBlob</span></code> and <code class="docutils literal notranslate"><span class="pre">AzureFiles</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.AppService.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.AppService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.AppService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">client_cert_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_site_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">source_controls=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backup</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>client_cert_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the App Service require client certificates for incoming requests? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> blocks as defined below.</p></li>
<li><p><strong>default_site_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Default Hostname associated with the App Service - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">logs</span></code> block as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12</span></code></p></li>
<li><p><strong>possible_outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12,52.143.43.17</span></code> - not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> block as defined below.</p></li>
<li><p><strong>site_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p></li>
<li><p><strong>source_controls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_control</span></code> block as defined below, which contains the Source Control information when <code class="docutils literal notranslate"><span class="pre">scm_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Backup enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name for this Backup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">schedule</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Sets how often the backup should be executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the unit of time for how often the backup should be executed. Possible values are <code class="docutils literal notranslate"><span class="pre">Day</span></code> or <code class="docutils literal notranslate"><span class="pre">Hour</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keepAtLeastOneBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPeriodInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days after which Backups should be deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets when the schedule should start working.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SAS URL to a Storage Container where Backups should be saved.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">application_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The level at which to log. Possible values include <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Information</span></code>, <code class="docutils literal notranslate"><span class="pre">Verbose</span></code> and <code class="docutils literal notranslate"><span class="pre">Off</span></code>. <strong>NOTE:</strong> this field is not available for <code class="docutils literal notranslate"><span class="pre">http_logs</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">http_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">file_system</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionInMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum size in megabytes that http log files can use before being removed.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the .net framework’s CLR used in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State of FTP / FTPS service for this App Service. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address used for this IP Restriction in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JAVA</span></code>, <code class="docutils literal notranslate"><span class="pre">JETTY</span></code>, and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code> and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Linux App Framework and version for the App Service. Possible options are a Docker container (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>), a base-64 encoded Docker Compose file (<code class="docutils literal notranslate"><span class="pre">COMPOSE|${filebase64(&quot;compose.yml&quot;)}</span></code>) or a base-64 encoded Kubernetes Manifest (<code class="docutils literal notranslate"><span class="pre">KUBE|${filebase64(&quot;kubernetes.yml&quot;)}</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of PHP to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Python to use in this App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code> and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Source Control enabled for this App Service. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the App Service run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Windows Docker container image (<code class="docutils literal notranslate"><span class="pre">DOCKER|&lt;user/image:tag&gt;</span></code>)</p></li>
</ul>
<p>The <strong>site_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
<p>The <strong>source_controls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Branch name of the Git repository for this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL of the Git repository for this App Service.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The access key for the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to mount the storage within the site’s runtime environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the file share (container name, for Blob storage).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of storage. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureBlob</span></code> and <code class="docutils literal notranslate"><span class="pre">AzureFiles</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.AppService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.AppService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AppService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.AwaitableGetAppServiceEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetAppServiceEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param">front_end_scale_factor=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_tier=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetAppServiceEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AwaitableGetAppServicePlanResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetAppServicePlanResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_environment_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_xenon=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_elastic_worker_count=None</em>, <em class="sig-param">maximum_number_of_workers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_site_scaling=None</em>, <em class="sig-param">reserved=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetAppServicePlanResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AwaitableGetAppServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetAppServiceResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">client_cert_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_site_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_configs=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">source_controls=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetAppServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AwaitableGetCertificateOrderResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetCertificateOrderResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_certificate_not_renewable_reasons=None</em>, <em class="sig-param">auto_renew=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">distinguished_name=None</em>, <em class="sig-param">domain_verification_token=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">intermediate_thumbprint=None</em>, <em class="sig-param">is_private_key_external=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">root_thumbprint=None</em>, <em class="sig-param">signed_certificate_thumbprint=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">validity_in_years=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetCertificateOrderResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AwaitableGetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">expiration_date=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">host_names=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issue_date=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">thumbprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.AwaitableGetFunctionAppResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">AwaitableGetFunctionAppResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.AwaitableGetFunctionAppResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_vault_secret_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pfx_blob=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_vault_secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault secret. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to access the certificate’s private key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pfx_blob</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded contents of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.host_names">
<code class="sig-name descname">host_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.host_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of host names the certificate applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.issue_date">
<code class="sig-name descname">issue_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.issue_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The issue date for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the certificate issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.key_vault_secret_id">
<code class="sig-name descname">key_vault_secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.key_vault_secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key Vault secret. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to access the certificate’s private key. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.pfx_blob">
<code class="sig-name descname">pfx_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.pfx_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded contents of the certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.subject_name">
<code class="sig-name descname">subject_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.subject_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Certificate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint for the certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">host_names=None</em>, <em class="sig-param">issue_date=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">key_vault_secret_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">pfx_blob=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">thumbprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration date for the certificate.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of the certificate.</p></li>
<li><p><strong>host_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of host names the certificate applies to.</p></li>
<li><p><strong>issue_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The issue date for the certificate.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the certificate issuer.</p></li>
<li><p><strong>key_vault_secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Key Vault secret. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to access the certificate’s private key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pfx_blob</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded contents of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subject_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject name of the certificate.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thumbprint for the certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.CertificateOrder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">CertificateOrder</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_renew=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">distinguished_name=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">validity_in_years=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Certificate Order.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last CSR that was created for this order.</p></li>
<li><p><strong>distinguished_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Distinguished Name for the App Service Certificate Order.</p></li>
<li><p><strong>key_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Certificate key size.  Defaults to 2048.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate product type, such as <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">WildCard</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>validity_in_years</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in years (must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">3</span></code>).  Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.app_service_certificate_not_renewable_reasons">
<code class="sig-name descname">app_service_certificate_not_renewable_reasons</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.app_service_certificate_not_renewable_reasons" title="Permalink to this definition">¶</a></dt>
<dd><p>Reasons why App Service Certificate is not renewable at the current moment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the Key Vault secret. A <code class="docutils literal notranslate"><span class="pre">certificates</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the App Service Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key Vault resource Id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyVaultSecretName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key Vault secret name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Status of the Key Vault secret.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.csr">
<code class="sig-name descname">csr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>Last CSR that was created for this order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.distinguished_name">
<code class="sig-name descname">distinguished_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.distinguished_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Distinguished Name for the App Service Certificate Order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.domain_verification_token">
<code class="sig-name descname">domain_verification_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.domain_verification_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain verification token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate expiration time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.intermediate_thumbprint">
<code class="sig-name descname">intermediate_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.intermediate_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint intermediate certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.is_private_key_external">
<code class="sig-name descname">is_private_key_external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.is_private_key_external" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the private key is external or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.key_size">
<code class="sig-name descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate key size.  Defaults to 2048.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.product_type">
<code class="sig-name descname">product_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.product_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate product type, such as <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">WildCard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.root_thumbprint">
<code class="sig-name descname">root_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.root_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint for root certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.signed_certificate_thumbprint">
<code class="sig-name descname">signed_certificate_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.signed_certificate_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint for signed certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current order status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CertificateOrder.validity_in_years">
<code class="sig-name descname">validity_in_years</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.validity_in_years" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in years (must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">3</span></code>).  Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CertificateOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_certificate_not_renewable_reasons=None</em>, <em class="sig-param">auto_renew=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">distinguished_name=None</em>, <em class="sig-param">domain_verification_token=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">intermediate_thumbprint=None</em>, <em class="sig-param">is_private_key_external=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">root_thumbprint=None</em>, <em class="sig-param">signed_certificate_thumbprint=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">validity_in_years=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertificateOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_certificate_not_renewable_reasons</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Reasons why App Service Certificate is not renewable at the current moment.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – State of the Key Vault secret. A <code class="docutils literal notranslate"><span class="pre">certificates</span></code> block as defined below.</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last CSR that was created for this order.</p></li>
<li><p><strong>distinguished_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Distinguished Name for the App Service Certificate Order.</p></li>
<li><p><strong>domain_verification_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain verification token.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate expiration time.</p></li>
<li><p><strong>intermediate_thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate thumbprint intermediate certificate.</p></li>
<li><p><strong>is_private_key_external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the private key is external or not.</p></li>
<li><p><strong>key_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Certificate key size.  Defaults to 2048.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate product type, such as <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">WildCard</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>root_thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate thumbprint for root certificate.</p></li>
<li><p><strong>signed_certificate_thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate thumbprint for signed certificate.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current order status.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>validity_in_years</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in years (must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">3</span></code>).  Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the App Service Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key Vault resource Id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyVaultSecretName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key Vault secret name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Status of the Key Vault secret.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CertificateOrder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.CertificateOrder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CertificateOrder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.CustomHostnameBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">CustomHostnameBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">ssl_state=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Hostname Binding within an App Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Custom Hostname to use for the App Service, example <code class="docutils literal notranslate"><span class="pre">www.example.com</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ssl_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL type. Possible values are <code class="docutils literal notranslate"><span class="pre">IpBasedEnabled</span></code> and <code class="docutils literal notranslate"><span class="pre">SniEnabled</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL certificate thumbprint. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.app_service_name">
<code class="sig-name descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Custom Hostname to use for the App Service, example <code class="docutils literal notranslate"><span class="pre">www.example.com</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.ssl_state">
<code class="sig-name descname">ssl_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.ssl_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL type. Possible values are <code class="docutils literal notranslate"><span class="pre">IpBasedEnabled</span></code> and <code class="docutils literal notranslate"><span class="pre">SniEnabled</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL certificate thumbprint. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.virtual_ip">
<code class="sig-name descname">virtual_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.virtual_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual IP address assigned to the hostname if IP based SSL is enabled.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">ssl_state=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">virtual_ip=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomHostnameBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Custom Hostname to use for the App Service, example <code class="docutils literal notranslate"><span class="pre">www.example.com</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ssl_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL type. Possible values are <code class="docutils literal notranslate"><span class="pre">IpBasedEnabled</span></code> and <code class="docutils literal notranslate"><span class="pre">SniEnabled</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL certificate thumbprint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>virtual_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual IP address assigned to the hostname if IP based SSL is enabled.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.CustomHostnameBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.CustomHostnameBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.CustomHostnameBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Environment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">Environment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">front_end_scale_factor=None</em>, <em class="sig-param">internal_load_balancing_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_tier=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Environment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>front_end_scale_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Scale factor for front end instances. Possible values are between <code class="docutils literal notranslate"><span class="pre">5</span></code> and <code class="docutils literal notranslate"><span class="pre">15</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">15</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service Environment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pricing_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pricing tier for the front end instances. Possible values are <code class="docutils literal notranslate"><span class="pre">I1</span></code>, <code class="docutils literal notranslate"><span class="pre">I2</span></code> and <code class="docutils literal notranslate"><span class="pre">I3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">I1</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet which the App Service Environment should be connected to. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.front_end_scale_factor">
<code class="sig-name descname">front_end_scale_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.front_end_scale_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Scale factor for front end instances. Possible values are between <code class="docutils literal notranslate"><span class="pre">5</span></code> and <code class="docutils literal notranslate"><span class="pre">15</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">15</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the App Service Environment exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service Environment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.pricing_tier">
<code class="sig-name descname">pricing_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.pricing_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Pricing tier for the front end instances. Possible values are <code class="docutils literal notranslate"><span class="pre">I1</span></code>, <code class="docutils literal notranslate"><span class="pre">I2</span></code> and <code class="docutils literal notranslate"><span class="pre">I3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">I1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the App Service Environment exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Environment.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Environment.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet which the App Service Environment should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Environment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">front_end_scale_factor=None</em>, <em class="sig-param">internal_load_balancing_mode=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_tier=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Environment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Environment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>front_end_scale_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Scale factor for front end instances. Possible values are between <code class="docutils literal notranslate"><span class="pre">5</span></code> and <code class="docutils literal notranslate"><span class="pre">15</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">15</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the App Service Environment exists.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service Environment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pricing_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pricing tier for the front end instances. Possible values are <code class="docutils literal notranslate"><span class="pre">I1</span></code>, <code class="docutils literal notranslate"><span class="pre">I2</span></code> and <code class="docutils literal notranslate"><span class="pre">I3</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">I1</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the App Service Environment exists.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet which the App Service Environment should be connected to. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Environment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Environment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.FunctionApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">FunctionApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">daily_memory_time_quota=None</em>, <em class="sig-param">enable_builtin_logging=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">storage_connection_string=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Function App.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this Function App.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p></li>
<li><p><strong>daily_memory_time_quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps under the consumption plan. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>enable_builtin_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the built-in logging of this Function App be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the Function App enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the Function App only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Function App. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string indicating the Operating System type for this function app.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Function App.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p></li>
<li><p><strong>storage_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime version associated with the Function App. Defaults to <code class="docutils literal notranslate"><span class="pre">~1</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Function App. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Function App be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State of FTP / FTPS service for this function app. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether or not the http2 protocol should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address CIDR notation used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Linux App Framework and version for the AppService, e.g. <code class="docutils literal notranslate"><span class="pre">DOCKER|(golang:latest)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the function app. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new function apps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.app_service_plan_id">
<code class="sig-name descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this Function App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.app_settings">
<code class="sig-name descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.auth_settings">
<code class="sig-name descname">auth_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.auth_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.client_affinity_enabled">
<code class="sig-name descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value for the Connection String.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.daily_memory_time_quota">
<code class="sig-name descname">daily_memory_time_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.daily_memory_time_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps under the consumption plan. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.default_hostname">
<code class="sig-name descname">default_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.default_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default hostname associated with the Function App - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.enable_builtin_logging">
<code class="sig-name descname">enable_builtin_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.enable_builtin_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the built-in logging of this Function App be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Function App enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.https_only">
<code class="sig-name descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the Function App only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the Function App. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function App kind - such as <code class="docutils literal notranslate"><span class="pre">functionapp,linux,container</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Function App. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A string indicating the Operating System type for this function app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.outbound_ip_addresses">
<code class="sig-name descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.possible_outbound_ip_addresses">
<code class="sig-name descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12,52.143.43.17</span></code> - not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Function App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.site_config">
<code class="sig-name descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the Function App be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - State of FTP / FTPS service for this function app. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether or not the http2 protocol should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP Address CIDR notation used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Linux App Framework and version for the AppService, e.g. <code class="docutils literal notranslate"><span class="pre">DOCKER|(golang:latest)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum supported TLS version for the function app. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new function apps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should WebSockets be enabled?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.site_credentials">
<code class="sig-name descname">site_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.site_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.storage_connection_string">
<code class="sig-name descname">storage_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.storage_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.FunctionApp.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime version associated with the Function App. Defaults to <code class="docutils literal notranslate"><span class="pre">~1</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.FunctionApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">daily_memory_time_quota=None</em>, <em class="sig-param">default_hostname=None</em>, <em class="sig-param">enable_builtin_logging=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">storage_connection_string=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FunctionApp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this Function App.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p></li>
<li><p><strong>daily_memory_time_quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of memory in gigabyte-seconds that your application is allowed to consume per day. Setting this value only affects function apps under the consumption plan. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>default_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default hostname associated with the Function App - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p></li>
<li><p><strong>enable_builtin_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the built-in logging of this Function App be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the Function App enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the Function App only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function App kind - such as <code class="docutils literal notranslate"><span class="pre">functionapp,linux,container</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Function App. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string indicating the Operating System type for this function app.</p></li>
<li><p><strong>outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12</span></code></p></li>
<li><p><strong>possible_outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12,52.143.43.17</span></code> - not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Function App.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p></li>
<li><p><strong>site_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p></li>
<li><p><strong>storage_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime version associated with the Function App. Defaults to <code class="docutils literal notranslate"><span class="pre">~1</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code> and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Function App. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Function App be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State of FTP / FTPS service for this function app. Possible values include: <code class="docutils literal notranslate"><span class="pre">AllAllowed</span></code>, <code class="docutils literal notranslate"><span class="pre">FtpsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether or not the http2 protocol should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address CIDR notation used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Linux App Framework and version for the AppService, e.g. <code class="docutils literal notranslate"><span class="pre">DOCKER|(golang:latest)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the function app. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new function apps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
</ul>
<p>The <strong>site_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.FunctionApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.FunctionApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.FunctionApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.GetAppServiceEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetAppServiceEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param">front_end_scale_factor=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_tier=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppServiceEnvironment.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceEnvironmentResult.front_end_scale_factor">
<code class="sig-name descname">front_end_scale_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceEnvironmentResult.front_end_scale_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of app instances per App Service Environment Front End</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceEnvironmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceEnvironmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceEnvironmentResult.pricing_tier">
<code class="sig-name descname">pricing_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceEnvironmentResult.pricing_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Pricing Tier (Isolated SKU) of the App Service Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceEnvironmentResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceEnvironmentResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetAppServicePlanResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_environment_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_xenon=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_elastic_worker_count=None</em>, <em class="sig-param">maximum_number_of_workers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_site_scaling=None</em>, <em class="sig-param">reserved=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppServicePlan.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.app_service_environment_id">
<code class="sig-name descname">app_service_environment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.app_service_environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Environment where the App Service Plan is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.is_xenon">
<code class="sig-name descname">is_xenon</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.is_xenon" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag that indicates if it’s a xenon plan (support for Windows Container)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Operating System type of the App Service Plan</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the App Service Plan exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.maximum_elastic_worker_count">
<code class="sig-name descname">maximum_elastic_worker_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.maximum_elastic_worker_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.maximum_number_of_workers">
<code class="sig-name descname">maximum_number_of_workers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.maximum_number_of_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of workers supported with the App Service Plan’s sku.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.per_site_scaling">
<code class="sig-name descname">per_site_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.per_site_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Apps assigned to this App Service Plan be scaled independently?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.reserved">
<code class="sig-name descname">reserved</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.reserved" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this App Service Plan <code class="docutils literal notranslate"><span class="pre">Reserved</span></code>?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServicePlanResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServicePlanResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetAppServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetAppServiceResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">client_cert_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_site_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_configs=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">source_controls=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppService.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.app_service_plan_id">
<code class="sig-name descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which the App Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.app_settings">
<code class="sig-name descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings for the App Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.client_affinity_enabled">
<code class="sig-name descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.client_cert_enabled">
<code class="sig-name descname">client_cert_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.client_cert_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the App Service require client certificates for incoming requests?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.default_site_hostname">
<code class="sig-name descname">default_site_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.default_site_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Hostname associated with the App Service - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.https_only">
<code class="sig-name descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service only be accessed via HTTPS?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the App Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Connection String.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.outbound_ip_addresses">
<code class="sig-name descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.possible_outbound_ip_addresses">
<code class="sig-name descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses - such as <code class="docutils literal notranslate"><span class="pre">52.23.25.3,52.143.43.12,52.143.43.17</span></code> - not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.site_configs">
<code class="sig-name descname">site_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.site_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetAppServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetAppServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetCertificateOrderResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_certificate_not_renewable_reasons=None</em>, <em class="sig-param">auto_renew=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">distinguished_name=None</em>, <em class="sig-param">domain_verification_token=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">intermediate_thumbprint=None</em>, <em class="sig-param">is_private_key_external=None</em>, <em class="sig-param">key_size=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">root_thumbprint=None</em>, <em class="sig-param">signed_certificate_thumbprint=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">validity_in_years=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificateOrder.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.app_service_certificate_not_renewable_reasons">
<code class="sig-name descname">app_service_certificate_not_renewable_reasons</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.app_service_certificate_not_renewable_reasons" title="Permalink to this definition">¶</a></dt>
<dd><p>Reasons why App Service Certificate is not renewable at the current moment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>true if the certificate should be automatically renewed when it expires; otherwise, false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the Key Vault secret. A <code class="docutils literal notranslate"><span class="pre">certificates</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.csr">
<code class="sig-name descname">csr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>Last CSR that was created for this order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.distinguished_name">
<code class="sig-name descname">distinguished_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.distinguished_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Distinguished Name for the App Service Certificate Order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.domain_verification_token">
<code class="sig-name descname">domain_verification_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.domain_verification_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain verification token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate expiration time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.intermediate_thumbprint">
<code class="sig-name descname">intermediate_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.intermediate_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint intermediate certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.is_private_key_external">
<code class="sig-name descname">is_private_key_external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.is_private_key_external" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the private key is external or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.key_size">
<code class="sig-name descname">key_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.key_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate key size.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the App Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.product_type">
<code class="sig-name descname">product_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.product_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate product type, such as <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">WildCard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.root_thumbprint">
<code class="sig-name descname">root_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.root_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint for root certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.signed_certificate_thumbprint">
<code class="sig-name descname">signed_certificate_thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.signed_certificate_thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate thumbprint for signed certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current order status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateOrderResult.validity_in_years">
<code class="sig-name descname">validity_in_years</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateOrderResult.validity_in_years" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in years (must be between 1 and 3).</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">expiration_date=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">host_names=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issue_date=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">thumbprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.host_names">
<code class="sig-name descname">host_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.host_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of host names the certificate applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.issue_date">
<code class="sig-name descname">issue_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.issue_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The issue date for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the certificate issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.subject_name">
<code class="sig-name descname">subject_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.subject_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetCertificateResult.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetCertificateResult.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint for the certificate.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.GetFunctionAppResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">GetFunctionAppResult</code><span class="sig-paren">(</span><em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">outbound_ip_addresses=None</em>, <em class="sig-param">possible_outbound_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFunctionApp.</p>
<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.app_service_plan_id">
<code class="sig-name descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this Function App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.app_settings">
<code class="sig-name descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.default_hostname">
<code class="sig-name descname">default_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.default_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default hostname associated with the Function App.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Function App enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Connection String.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A string indicating the Operating System type for this function app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.outbound_ip_addresses">
<code class="sig-name descname">outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.possible_outbound_ip_addresses">
<code class="sig-name descname">possible_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.possible_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of outbound IP addresses, not all of which are necessarily in use. Superset of <code class="docutils literal notranslate"><span class="pre">outbound_ip_addresses</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.GetFunctionAppResult.site_credentials">
<code class="sig-name descname">site_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.GetFunctionAppResult.site_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appservice.Plan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">Plan</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_environment_id=None</em>, <em class="sig-param">is_xenon=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_elastic_worker_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_site_scaling=None</em>, <em class="sig-param">reserved=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Plan component.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The kind of the App Service Plan to create. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows</span></code> (also available as <code class="docutils literal notranslate"><span class="pre">App</span></code>), <code class="docutils literal notranslate"><span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">elastic</span></code> (for Premium Consumption) and <code class="docutils literal notranslate"><span class="pre">FunctionApp</span></code> (for a Consumption Plan). Defaults to <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_elastic_worker_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.</p></li>
<li><p><strong>per_site_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can Apps assigned to this App Service Plan be scaled independently? If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> apps assigned to this plan will scale to all instances of the plan.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reserved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this App Service Plan <code class="docutils literal notranslate"><span class="pre">Reserved</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service Plan component.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of workers associated with this App Service Plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the plan’s instance size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the plan’s pricing tier.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.app_service_environment_id">
<code class="sig-name descname">app_service_environment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.app_service_environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of the App Service Plan to create. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows</span></code> (also available as <code class="docutils literal notranslate"><span class="pre">App</span></code>), <code class="docutils literal notranslate"><span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">elastic</span></code> (for Premium Consumption) and <code class="docutils literal notranslate"><span class="pre">FunctionApp</span></code> (for a Consumption Plan). Defaults to <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.maximum_elastic_worker_count">
<code class="sig-name descname">maximum_elastic_worker_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.maximum_elastic_worker_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.maximum_number_of_workers">
<code class="sig-name descname">maximum_number_of_workers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.maximum_number_of_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of workers supported with the App Service Plan’s sku.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.per_site_scaling">
<code class="sig-name descname">per_site_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.per_site_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Can Apps assigned to this App Service Plan be scaled independently? If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> apps assigned to this plan will scale to all instances of the plan.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.reserved">
<code class="sig-name descname">reserved</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.reserved" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this App Service Plan <code class="docutils literal notranslate"><span class="pre">Reserved</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service Plan component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of workers associated with this App Service Plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the plan’s instance size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the plan’s pricing tier.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Plan.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Plan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Plan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_environment_id=None</em>, <em class="sig-param">is_xenon=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">maximum_elastic_worker_count=None</em>, <em class="sig-param">maximum_number_of_workers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_site_scaling=None</em>, <em class="sig-param">reserved=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Plan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Environment where the App Service Plan should be located. Changing forces a new resource to be created.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The kind of the App Service Plan to create. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows</span></code> (also available as <code class="docutils literal notranslate"><span class="pre">App</span></code>), <code class="docutils literal notranslate"><span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">elastic</span></code> (for Premium Consumption) and <code class="docutils literal notranslate"><span class="pre">FunctionApp</span></code> (for a Consumption Plan). Defaults to <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_elastic_worker_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</p></li>
<li><p><strong>maximum_number_of_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of workers supported with the App Service Plan’s sku.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service Plan component. Changing this forces a new resource to be created.</p></li>
<li><p><strong>per_site_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can Apps assigned to this App Service Plan be scaled independently? If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> apps assigned to this plan will scale to all instances of the plan.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reserved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this App Service Plan <code class="docutils literal notranslate"><span class="pre">Reserved</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service Plan component.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of workers associated with this App Service Plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the plan’s instance size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the plan’s pricing tier.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Plan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Plan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Plan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Slot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">Slot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Slot (within an App Service).</p>
<blockquote>
<div><p><strong>Note:</strong> When using Slots - the <code class="docutils literal notranslate"><span class="pre">app_settings</span></code>, <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> and <code class="docutils literal notranslate"><span class="pre">site_config</span></code> blocks on the <code class="docutils literal notranslate"><span class="pre">appservice.AppService</span></code> resource will be overwritten when promoting a Slot using the <code class="docutils literal notranslate"><span class="pre">appservice.ActiveSlot</span></code> resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Slot Enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service Slot only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service Slot component. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service Slot component.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code>, and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">application_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The level at which to log. Possible values include <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Information</span></code>, <code class="docutils literal notranslate"><span class="pre">Verbose</span></code> and <code class="docutils literal notranslate"><span class="pre">Off</span></code>. <strong>NOTE:</strong> this field is not available for <code class="docutils literal notranslate"><span class="pre">http_logs</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">http_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">file_system</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionInMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum size in megabytes that http log files can use before being removed.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the swap to automatically swap to during deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the .net framework’s CLR used in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional.The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JETTY</span></code> and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of PHP to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Python to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code>, and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Source Control enabled for this App Service Slot. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_service_name">
<code class="sig-name descname">app_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_service_plan_id">
<code class="sig-name descname">app_service_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_service_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.app_settings">
<code class="sig-name descname">app_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.app_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value pair of App Settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.auth_settings">
<code class="sig-name descname">auth_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.auth_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.client_affinity_enabled">
<code class="sig-name descname">client_affinity_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.client_affinity_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code>, and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value for the Connection String.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.default_site_hostname">
<code class="sig-name descname">default_site_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.default_site_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Hostname associated with the App Service Slot - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the App Service Slot Enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.https_only">
<code class="sig-name descname">https_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.https_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Can the App Service Slot only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A Managed Service Identity block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the App Service Slot component. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Service Slot component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.site_config">
<code class="sig-name descname">site_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.site_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the swap to automatically swap to during deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the .net framework’s CLR used in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP Address used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Optional.The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JETTY</span></code> and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of PHP to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Python to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code>, and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Source Control enabled for this App Service Slot. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.site_credentials">
<code class="sig-name descname">site_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.site_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.Slot.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.Slot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Slot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_name=None</em>, <em class="sig-param">app_service_plan_id=None</em>, <em class="sig-param">app_settings=None</em>, <em class="sig-param">auth_settings=None</em>, <em class="sig-param">client_affinity_enabled=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">default_site_hostname=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">site_config=None</em>, <em class="sig-param">site_credentials=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Slot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_service_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value pair of App Settings.</p></li>
<li><p><strong>auth_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auth_settings</span></code> block as defined below.</p></li>
<li><p><strong>client_affinity_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">connection_string</span></code> block as defined below.</p></li>
<li><p><strong>default_site_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Default Hostname associated with the App Service Slot - such as <code class="docutils literal notranslate"><span class="pre">mysite.azurewebsites.net</span></code></p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the App Service Slot Enabled?</p></li>
<li><p><strong>https_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can the App Service Slot only be accessed via HTTPS? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Service Slot component. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Service Slot component.</p></li>
<li><p><strong>site_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_config</span></code> object as defined below.</p></li>
<li><p><strong>site_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">site_credential</span></code> block as defined below, which contains the site-level credentials used to publish to this App Service.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allowed audience values to consider when validating JWTs issued by Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLoginParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form “key=value”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedExternalRedirectUrls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External URLs that can be redirected to as part of logging in or logging out of the app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default provider to use when multiple providers have been set up. Possible values are <code class="docutils literal notranslate"><span class="pre">AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">Google</span></code>, <code class="docutils literal notranslate"><span class="pre">MicrosoftAccount</span></code> and <code class="docutils literal notranslate"><span class="pre">Twitter</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Authentication enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">facebook</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App ID of the Facebook app used for login</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The App Secret of the Facebook app used for Facebook Login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. <a class="reference external" href="https://developers.facebook.com/docs/facebook-login">https://developers.facebook.com/docs/facebook-login</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">google</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">google</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OpenID Connect Client ID for the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client secret associated with the Google web application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. <a class="reference external" href="https://developers.google.com/identity/sign-in/web/">https://developers.google.com/identity/sign-in/web/</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. <a class="reference external" href="https://sts.windows.net">https://sts.windows.net</a>/{tenant-guid}/.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">microsoft</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client ID that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret that was created for the app used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. <a class="reference external" href="https://msdn.microsoft.com/en-us/library/dn631845.aspx">https://msdn.microsoft.com/en-us/library/dn631845.aspx</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtimeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The runtime version of the Authentication/Authorization module.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenRefreshExtensionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenStoreEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">twitter</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticatedClientAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take when an unauthenticated client attempts to access the app. Possible values are <code class="docutils literal notranslate"><span class="pre">AllowAnonymous</span></code> and <code class="docutils literal notranslate"><span class="pre">RedirectToLoginPage</span></code>.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Connection String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the Connection String. Possible values are <code class="docutils literal notranslate"><span class="pre">APIHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>, <code class="docutils literal notranslate"><span class="pre">DocDb</span></code>, <code class="docutils literal notranslate"><span class="pre">EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">NotificationHub</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">RedisCache</span></code>, <code class="docutils literal notranslate"><span class="pre">ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLAzure</span></code>, and  <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value for the Connection String.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the App Service. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">application_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The level at which to log. Possible values include <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Information</span></code>, <code class="docutils literal notranslate"><span class="pre">Verbose</span></code> and <code class="docutils literal notranslate"><span class="pre">Off</span></code>. <strong>NOTE:</strong> this field is not available for <code class="docutils literal notranslate"><span class="pre">http_logs</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">http_logs</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlobStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_blob_storage</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the storage container, with a Service SAS token appended. <strong>NOTE:</strong> there is currently no means of generating Service SAS tokens with the <code class="docutils literal notranslate"><span class="pre">azurerm</span></code> provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileSystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">file_system</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain logs for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionInMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum size in megabytes that http log files can use before being removed.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>site_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the app be loaded at all times? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appCommandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App command line to launch, e.g. <code class="docutils literal notranslate"><span class="pre">/sbin/myserver</span> <span class="pre">-b</span> <span class="pre">0.0.0.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSwapSlotName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the swap to automatically swap to during deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cors</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of origins which should be able to make cross-origin calls. <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to allow all calls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are credentials supported?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDocuments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ordering of default documents to load, if an address isn’t specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dotnetFrameworkVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the .net framework’s CLR used in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">v2.0</span></code> (which will use the latest version of the .net framework for the .net CLR v2 - currently <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">3.5</span></code>) and <code class="docutils literal notranslate"><span class="pre">v4.0</span></code> (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is <code class="docutils literal notranslate"><span class="pre">.net</span> <span class="pre">4.7.1</span></code>). <a class="reference external" href="https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview">For more information on which .net CLR version to use based on the .net framework you’re targeting - please see this table</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">v4.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ftpsState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP2 Enabled on this App Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRestrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of objects representing ip restrictions as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Address used for this IP Restriction.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional.The Virtual Network Subnet ID used for this IP Restriction.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">JETTY</span></code> and <code class="docutils literal notranslate"><span class="pre">TOMCAT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaContainerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Java Container to use. If specified <code class="docutils literal notranslate"><span class="pre">java_version</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container</span></code> must also be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Java to use. If specified <code class="docutils literal notranslate"><span class="pre">java_container</span></code> and <code class="docutils literal notranslate"><span class="pre">java_container_version</span></code> must also be specified. Possible values are <code class="docutils literal notranslate"><span class="pre">1.7</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code> and their specific versions - except for Java 11 (e.g. <code class="docutils literal notranslate"><span class="pre">1.7.0_80</span></code>, <code class="docutils literal notranslate"><span class="pre">1.8.0_181</span></code>, <code class="docutils literal notranslate"><span class="pre">11</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linuxFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localMysqlEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is “MySQL In App” Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedPipelineMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Pipeline Mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Integrated</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Integrated</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum supported TLS version for the app service. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code>, and <code class="docutils literal notranslate"><span class="pre">1.2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1.2</span></code> for new app services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of PHP to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">5.5</span></code>, <code class="docutils literal notranslate"><span class="pre">5.6</span></code>, <code class="docutils literal notranslate"><span class="pre">7.0</span></code>, <code class="docutils literal notranslate"><span class="pre">7.1</span></code>, <code class="docutils literal notranslate"><span class="pre">7.2</span></code>, and <code class="docutils literal notranslate"><span class="pre">7.3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Python to use in this App Service Slot. Possible values are <code class="docutils literal notranslate"><span class="pre">2.7</span></code> and <code class="docutils literal notranslate"><span class="pre">3.4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Remote Debugging Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteDebuggingVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are <code class="docutils literal notranslate"><span class="pre">VS2012</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2013</span></code>, <code class="docutils literal notranslate"><span class="pre">VS2015</span></code>, and <code class="docutils literal notranslate"><span class="pre">VS2017</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scmType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Source Control enabled for this App Service Slot. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>. Possible values are: <code class="docutils literal notranslate"><span class="pre">BitbucketGit</span></code>, <code class="docutils literal notranslate"><span class="pre">BitbucketHg</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexGit</span></code>, <code class="docutils literal notranslate"><span class="pre">CodePlexHg</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">ExternalHg</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>, <code class="docutils literal notranslate"><span class="pre">LocalGit</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>, <code class="docutils literal notranslate"><span class="pre">Tfs</span></code>, <code class="docutils literal notranslate"><span class="pre">VSO</span></code>, and <code class="docutils literal notranslate"><span class="pre">VSTSRM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use32BitWorkerProcess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websocketsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should WebSockets be enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowsFxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>site_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the username, which can be used to publish to this App Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username which can be used to publish to this App Service</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.Slot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.Slot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.Slot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.SourceCodeToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">SourceCodeToken</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">token_secret=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service source control token.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Source Control Tokens are configured at the subscription level, not on each App Service - as such this can only be configured Subscription-wide</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth access token.</p></li>
<li><p><strong>token_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth access token secret.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source control type. Possible values are <code class="docutils literal notranslate"><span class="pre">BitBucket</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> and <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.SourceCodeToken.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAuth access token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.SourceCodeToken.token_secret">
<code class="sig-name descname">token_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.token_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAuth access token secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.SourceCodeToken.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The source control type. Possible values are <code class="docutils literal notranslate"><span class="pre">BitBucket</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> and <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.SourceCodeToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">token_secret=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SourceCodeToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth access token.</p></li>
<li><p><strong>token_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth access token secret.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source control type. Possible values are <code class="docutils literal notranslate"><span class="pre">BitBucket</span></code>, <code class="docutils literal notranslate"><span class="pre">Dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> and <code class="docutils literal notranslate"><span class="pre">OneDrive</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.SourceCodeToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.SourceCodeToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.SourceCodeToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">VirtualNetworkSwiftConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Service Virtual Network Association (this is for the <a class="reference external" href="https://docs.microsoft.com/en-us/azure/app-service/web-sites-integrate-with-vnet#regional-vnet-integration">Regional VNet Integration</a> which is still in preview).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service to associate to the VNet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet the app service will be associated to (the subnet must have a <code class="docutils literal notranslate"><span class="pre">service_delegation</span></code> configured for <code class="docutils literal notranslate"><span class="pre">Microsoft.Web/serverFarms</span></code>).</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection.app_service_id">
<code class="sig-name descname">app_service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection.app_service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the App Service to associate to the VNet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet the app service will be associated to (the subnet must have a <code class="docutils literal notranslate"><span class="pre">service_delegation</span></code> configured for <code class="docutils literal notranslate"><span class="pre">Microsoft.Web/serverFarms</span></code>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service_id=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkSwiftConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the App Service to associate to the VNet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet the app service will be associated to (the subnet must have a <code class="docutils literal notranslate"><span class="pre">service_delegation</span></code> configured for <code class="docutils literal notranslate"><span class="pre">Microsoft.Web/serverFarms</span></code>).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.VirtualNetworkSwiftConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.VirtualNetworkSwiftConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appservice.get_app_service">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_app_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_app_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the App Service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the App Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_app_service_environment">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_app_service_environment</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_app_service_environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service Environment</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the App Service Environment.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the App Service Environment exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_app_service_plan">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_app_service_plan</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_app_service_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service Plan (formerly known as a <code class="docutils literal notranslate"><span class="pre">Server</span> <span class="pre">Farm</span></code>).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the App Service Plan.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the App Service Plan exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_certificate">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_certificate</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an App Service Certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the certificate.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which to create the certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_certificate_order">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_certificate_order</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_certificate_order" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing App Service Certificate Order.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the App Service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the App Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.appservice.get_function_app">
<code class="sig-prename descclassname">pulumi_azure.appservice.</code><code class="sig-name descname">get_function_app</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appservice.get_function_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Function App.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Function App resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group where the Function App exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
