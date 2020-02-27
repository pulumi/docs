---
title: Module open_id
title_tag: Module open_id | Package pulumi_keycloak | Python SDK
linktitle: open_id
notitle: true
---

<div class="section" id="module-pulumi_keycloak.open_id">
<span id="open-id"></span><h1>open_id<a class="headerlink" href="#module-pulumi_keycloak.open_id" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_keycloak.open_id.AudienceProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">AudienceProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">included_client_audience=None</em>, <em class="sig-param">included_custom_audience=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AudienceProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing audience protocol mappers within
Keycloak. This mapper was added in Keycloak v4.6.0.Final.</p>
<p>Audience protocol mappers allow you add audiences to the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim
within issued tokens. The audience can be a custom string, or it can be
mapped to the ID of a pre-existing client.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">included_client_audience</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">included_custom_audience</span></code> is not specified) A client ID to include within the token’s <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">included_custom_audience</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">included_client_audience</span></code> is not specified) A custom audience to include within the token’s <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the audience should be included in the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim for the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the audience should be included in the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim for the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_audience_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_audience_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.AudienceProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">included_client_audience=None</em>, <em class="sig-param">included_custom_audience=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AudienceProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AudienceProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_audience_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_audience_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.AudienceProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AudienceProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.AudienceProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AudienceProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.AwaitableGetClientAuthorizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">AwaitableGetClientAuthorizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">decision_strategy=None</em>, <em class="sig-param">logic=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AwaitableGetClientAuthorizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.AwaitableGetClientResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">AwaitableGetClientResult</code><span class="sig-paren">(</span><em class="sig-param">access_type=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direct_access_grants_enabled=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">implicit_flow_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">service_account_user_id=None</em>, <em class="sig-param">service_accounts_enabled=None</em>, <em class="sig-param">standard_flow_enabled=None</em>, <em class="sig-param">valid_redirect_uris=None</em>, <em class="sig-param">web_origins=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AwaitableGetClientResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.AwaitableGetClientServiceAccountUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">AwaitableGetClientServiceAccountUserResult</code><span class="sig-paren">(</span><em class="sig-param">attributes=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">federated_identities=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.AwaitableGetClientServiceAccountUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.Client">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">Client</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_type=None</em>, <em class="sig-param">admin_url=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">consent_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direct_access_grants_enabled=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">exclude_session_state_from_auth_response=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">implicit_flow_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pkce_code_challenge_method=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">service_accounts_enabled=None</em>, <em class="sig-param">standard_flow_enabled=None</em>, <em class="sig-param">valid_redirect_uris=None</em>, <em class="sig-param">web_origins=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.Client" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Keycloak clients that use the OpenID Connect protocol.</p>
<p>Clients are entities that can use Keycloak for user authentication. Typically,
clients are applications that redirect users to Keycloak for authentication
in order to take advantage of Keycloak’s user sessions for SSO.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this client is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required) The unique ID of this client, referenced in the URI during authentication and in issued tokens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) The display name of this client in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> - (Optional) When false, this client will not be able to initiate a login or obtain access tokens. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - (Optional) The description of this client in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_type</span></code> - (Required) Specifies the type of client, which can be one of the following:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">CONFIDENTIAL</span></code> - Used for server-side clients that require both client ID and secret when authenticating.
This client should be used for applications using the Authorization Code or Client Credentials grant flows.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> - Used for browser-only applications that do not require a client secret, and instead rely only on authorized redirect
URIs for security. This client should be used for applications using the Implicit grant flow.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BEARER-ONLY</span></code> - Used for services that never initiate a login. This client will only allow bearer token requests.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> - (Optional) The secret for clients with an <code class="docutils literal notranslate"><span class="pre">access_type</span></code> of <code class="docutils literal notranslate"><span class="pre">CONFIDENTIAL</span></code> or <code class="docutils literal notranslate"><span class="pre">BEARER-ONLY</span></code>. This value is sensitive and
should be treated with the same care as a password. If omitted, Keycloak will generate a GUID for this attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">standard_flow_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the OAuth2 Authorization Code Grant will be enabled for this client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">implicit_flow_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the OAuth2 Implicit Grant will be enabled for this client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direct_access_grants_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the OAuth2 Resource Owner Password Grant will be enabled for this client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_accounts_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the OAuth2 Client Credentials grant will be enabled for this client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valid_redirect_uris</span></code> - (Optional) A list of valid URIs a browser is permitted to redirect to after a successful login or logout. Simple
wildcards in the form of an asterisk can be used here. This attribute must be set if either <code class="docutils literal notranslate"><span class="pre">standard_flow_enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">implicit_flow_enabled</span></code>
is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">web_origins</span></code> - (Optional) A list of allowed CORS origins. <code class="docutils literal notranslate"><span class="pre">+</span></code> can be used to permit all valid redirect URIs, and <code class="docutils literal notranslate"><span class="pre">*</span></code> can be used to permit all origins.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_url</span></code> - (Optional) URL to the admin interface of the client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">base_url</span></code> - (Optional) Default URL to use when the auth server needs to redirect or link back to the client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pkce_code_challenge_method</span></code> - (Optional) The challenge method to use for Proof Key for Code Exchange. Can be either <code class="docutils literal notranslate"><span class="pre">plain</span></code> or <code class="docutils literal notranslate"><span class="pre">S256</span></code> or set to empty value <a href="#id1"><span class="problematic" id="id2">``</span></a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">full_scope_allowed</span></code> - (Optional) - Allow to include all roles mappings in the access token.</p></li>
</ul>
<p>In addition to the arguments listed above, the following computed attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_user_id</span></code> - When service accounts are enabled for this client, this attribute is the unique ID for the Keycloak user that represents this service account.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authorization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowRemoteResourceManagement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keepDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyEnforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.Client.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_type=None</em>, <em class="sig-param">admin_url=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">consent_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direct_access_grants_enabled=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">exclude_session_state_from_auth_response=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">implicit_flow_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pkce_code_challenge_method=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">service_account_user_id=None</em>, <em class="sig-param">service_accounts_enabled=None</em>, <em class="sig-param">standard_flow_enabled=None</em>, <em class="sig-param">valid_redirect_uris=None</em>, <em class="sig-param">web_origins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.Client.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Client resource’s state with the given name, id, and optional extra
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
<p>The <strong>authorization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowRemoteResourceManagement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keepDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyEnforcementMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.Client.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.Client.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.Client.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.Client.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationPermission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientAuthorizationPermission</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">decision_strategy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationPermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientAuthorizationPermission resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientAuthorizationPermission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">decision_strategy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationPermission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientAuthorizationPermission resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationPermission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationPermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationPermission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationPermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientAuthorizationResource</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">icon_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_managed_access=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uris=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationResource" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientAuthorizationResource resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientAuthorizationResource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">icon_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_managed_access=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uris=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationResource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientAuthorizationResource resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationResource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationResource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationResource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationResource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationScope">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientAuthorizationScope</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">icon_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationScope" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientAuthorizationScope resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientAuthorizationScope.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">icon_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationScope.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientAuthorizationScope resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationScope.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationScope.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientAuthorizationScope.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientAuthorizationScope.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientDefaultScopes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientDefaultScopes</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientDefaultScopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientDefaultScopes resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_default_scopes.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_default_scopes.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientDefaultScopes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientDefaultScopes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientDefaultScopes resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_default_scopes.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_default_scopes.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientDefaultScopes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientDefaultScopes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientDefaultScopes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientDefaultScopes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientOptionalScopes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientOptionalScopes</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">optional_scopes=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientOptionalScopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientOptionalScopes resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_optional_scopes.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_optional_scopes.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientOptionalScopes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">optional_scopes=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientOptionalScopes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientOptionalScopes resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_optional_scopes.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_optional_scopes.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientOptionalScopes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientOptionalScopes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientOptionalScopes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientOptionalScopes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientScope">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientScope</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">consent_screen_text=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientScope" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Keycloak client scopes that can be attached to
clients that use the OpenID Connect protocol.</p>
<p>Client Scopes can be used to share common protocol and role mappings between multiple
clients within a realm. They can also be used by clients to conditionally request
claims or roles for a user based on the OAuth 2.0 <code class="docutils literal notranslate"><span class="pre">scope</span></code> parameter.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this client scope belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this client scope in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - (Optional) The description of this client scope in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consent_screen_text</span></code> - (Optional) When set, a consent screen will be displayed to users
authenticating to clients with this scope attached. The consent screen will display the string
value of this attribute.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_scope.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_scope.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientScope.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">consent_screen_text=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientScope.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientScope resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_scope.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_client_scope.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientScope.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientScope.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientScope.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientScope.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRealmRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientServiceAccountRealmRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRealmRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientServiceAccountRealmRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRealmRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRealmRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientServiceAccountRealmRole resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRealmRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRealmRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRealmRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRealmRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">ClientServiceAccountRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ClientServiceAccountRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientServiceAccountRole resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.ClientServiceAccountRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.ClientServiceAccountRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.FullNameProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">FullNameProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.FullNameProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing full name protocol mappers within
Keycloak.</p>
<p>Full name protocol mappers allow you to map a user’s first and last name
to the OpenID Connect <code class="docutils literal notranslate"><span class="pre">name</span></code> claim in a token. Protocol mappers can be defined
for a single client, or they can be defined for a client scope which can
be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the user’s full name should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the user’s full name should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the user’s full name should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_full_name_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_full_name_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.FullNameProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.FullNameProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FullNameProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_full_name_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_full_name_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.FullNameProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.FullNameProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.FullNameProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.FullNameProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.GetClientAuthorizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">GetClientAuthorizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">decision_strategy=None</em>, <em class="sig-param">logic=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientAuthorizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientAuthorizationPolicy.</p>
<dl class="attribute">
<dt id="pulumi_keycloak.open_id.GetClientAuthorizationPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientAuthorizationPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.GetClientResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">GetClientResult</code><span class="sig-paren">(</span><em class="sig-param">access_type=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direct_access_grants_enabled=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">implicit_flow_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">service_account_user_id=None</em>, <em class="sig-param">service_accounts_enabled=None</em>, <em class="sig-param">standard_flow_enabled=None</em>, <em class="sig-param">valid_redirect_uris=None</em>, <em class="sig-param">web_origins=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClient.</p>
<dl class="attribute">
<dt id="pulumi_keycloak.open_id.GetClientResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.GetClientServiceAccountUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">GetClientServiceAccountUserResult</code><span class="sig-paren">(</span><em class="sig-param">attributes=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">federated_identities=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientServiceAccountUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientServiceAccountUser.</p>
<dl class="attribute">
<dt id="pulumi_keycloak.open_id.GetClientServiceAccountUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.open_id.GetClientServiceAccountUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.open_id.GroupMembershipProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">GroupMembershipProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GroupMembershipProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing group membership protocol mappers within
Keycloak.</p>
<p>Group membership protocol mappers allow you to map a user’s group memberships
to a claim in a token. Protocol mappers can be defined for a single client,
or they can be defined for a client scope which can be shared between multiple
different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Required) The name of the claim to insert into a token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">full_path</span></code> - (Optional) Indicates whether the full path of the group including its parents will be used. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the property should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the property should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the property should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_group_membership_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_group_membership_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.GroupMembershipProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GroupMembershipProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembershipProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_group_membership_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_group_membership_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.GroupMembershipProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GroupMembershipProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.GroupMembershipProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.GroupMembershipProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.HardcodedClaimProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">HardcodedClaimProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedClaimProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing hardcoded claim protocol mappers within
Keycloak.</p>
<p>Hardcoded claim protocol mappers allow you to define a claim with a hardcoded
value. Protocol mappers can be defined for a single client, or they can
be defined for a client scope which can be shared between multiple different
clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Required) The name of the claim to insert into a token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_value</span></code> - (Required) The hardcoded value of the claim.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_value_type</span></code> - (Optional) The claim type used when serializing JSON tokens. Can be one of <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">int</span></code>, or <code class="docutils literal notranslate"><span class="pre">boolean</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">String</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the property should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the property should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the property should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_claim_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_claim_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HardcodedClaimProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_claim_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_claim_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedClaimProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.HardcodedRoleProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">HardcodedRoleProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedRoleProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing hardcoded role protocol mappers within
Keycloak.</p>
<p>Hardcoded role protocol mappers allow you to specify a single role to
always map to an access token for a client. Protocol mappers can be
defined for a single client, or they can be defined for a client scope
which can be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the
GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_id</span></code> - (Required) The ID of the role to map to an access token.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_role_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_role_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HardcodedRoleProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_role_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_hardcoded_role_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.HardcodedRoleProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserAttributeProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">UserAttributeProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">multivalued=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_attribute=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserAttributeProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user attribute protocol mappers within
Keycloak.</p>
<p>User attribute protocol mappers allow you to map custom attributes defined
for a user within Keycloak to a claim in a token. Protocol mappers can be
defined for a single client, or they can be defined for a client scope which
can be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_attribute</span></code> - (Required) The custom user attribute to map a claim for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Required) The name of the claim to insert into a token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_value_type</span></code> - (Optional) The claim type used when serializing JSON tokens. Can be one of <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">int</span></code>, or <code class="docutils literal notranslate"><span class="pre">boolean</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">String</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">multivalued</span></code> - (Optional) Indicates whether this attribute is a single value or an array of values. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the attribute should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the attribute should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the attribute should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_attribute_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_attribute_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.UserAttributeProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">multivalued=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_attribute=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserAttributeProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserAttributeProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_attribute_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_attribute_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.UserAttributeProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserAttributeProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserAttributeProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserAttributeProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserPropertyProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">UserPropertyProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_property=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserPropertyProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user property protocol mappers within
Keycloak.</p>
<p>User property protocol mappers allow you to map built in properties defined
on the Keycloak user interface to a claim in a token. Protocol mappers can be
defined for a single client, or they can be defined for a client scope which
can be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_property</span></code> - (Required) The built in user property (such as email) to map a claim for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Required) The name of the claim to insert into a token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_value_type</span></code> - (Optional) The claim type used when serializing JSON tokens. Can be one of <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">int</span></code>, or <code class="docutils literal notranslate"><span class="pre">boolean</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">String</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the property should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the property should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the property should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_property_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_property_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.UserPropertyProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_property=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserPropertyProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPropertyProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_property_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_property_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.UserPropertyProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserPropertyProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserPropertyProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserPropertyProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserRealmRoleProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">UserRealmRoleProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">multivalued=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">realm_role_prefix=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserRealmRoleProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user realm role protocol mappers within
Keycloak.</p>
<p>User realm role protocol mappers allow you to define a claim containing the list of the realm roles.
Protocol mappers can be defined for a single client, or they can
be defined for a client scope which can be shared between multiple different
clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Required) The name of the claim to insert into a token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_value_type</span></code> - (Optional) The claim type used when serializing JSON tokens. Can be one of <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">int</span></code>, or <code class="docutils literal notranslate"><span class="pre">boolean</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">String</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">multivalued</span></code> - (Optional) Indicates if attribute supports multiple values. If true, then the list of all values of this attribute will be set as claim. If false, then just first value will be set as claim. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm_role_prefix</span></code> - (Optional) A prefix for each Realm Role.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_id_token</span></code> - (Optional) Indicates if the property should be added as a claim to the id token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_access_token</span></code> - (Optional) Indicates if the property should be added as a claim to the access token. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_to_userinfo</span></code> - (Optional) Indicates if the property should be added as a claim to the UserInfo response body. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_realm_role_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_realm_role_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_to_access_token=None</em>, <em class="sig-param">add_to_id_token=None</em>, <em class="sig-param">add_to_userinfo=None</em>, <em class="sig-param">claim_name=None</em>, <em class="sig-param">claim_value_type=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">multivalued=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">realm_role_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserRealmRoleProtocolMapper resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_realm_role_protocol_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/openid_user_realm_role_protocol_mapper.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.UserRealmRoleProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.open_id.get_client">
<code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">get_client</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.get_client" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak OpenID client for usage with other resources.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required) The client id.</p></li>
</ul>
<p>See the docs for the <code class="docutils literal notranslate"><span class="pre">OpenId.Client</span></code> resource for details on the exported attributes.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/d/openid_client.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/d/openid_client.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_keycloak.open_id.get_client_authorization_policy">
<code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">get_client_authorization_policy</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">resource_server_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.get_client_authorization_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_keycloak.open_id.get_client_service_account_user">
<code class="sig-prename descclassname">pulumi_keycloak.open_id.</code><code class="sig-name descname">get_client_service_account_user</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.open_id.get_client_service_account_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
