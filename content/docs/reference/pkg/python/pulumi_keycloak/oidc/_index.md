---
title: Module oidc
title_tag: Module oidc | Package pulumi_keycloak | Python SDK
linktitle: oidc
notitle: true
---

<div class="section" id="module-pulumi_keycloak.oidc">
<span id="oidc"></span><h1>oidc<a class="headerlink" href="#module-pulumi_keycloak.oidc" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.oidc.</code><code class="sig-name descname">GoogleIdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepts_prompt_none_forward_from_client=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">disable_user_info=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">hosted_domain=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">request_refresh_token=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">use_user_ip_param=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GoogleIdentityProvider resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepts_prompt_none_forward_from_client=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">disable_user_info=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">hosted_domain=None</em>, <em class="sig-param">internal_id=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">request_refresh_token=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">use_user_ip_param=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GoogleIdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.oidc.IdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.oidc.</code><code class="sig-name descname">IdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">login_hint=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">ui_locales=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">validate_signature=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IdentityProvider resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.oidc.IdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">internal_id=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">login_hint=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">ui_locales=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">validate_signature=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.oidc.IdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.oidc.IdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
