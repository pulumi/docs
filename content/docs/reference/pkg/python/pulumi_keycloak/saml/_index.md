---
title: Module saml
title_tag: Module saml | Package pulumi_keycloak | Python SDK
linktitle: saml
notitle: true
---

<div class="section" id="module-pulumi_keycloak.saml">
<span id="saml"></span><h1>saml<a class="headerlink" href="#module-pulumi_keycloak.saml" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_keycloak.saml.AwaitableGetClientInstallationProviderResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">AwaitableGetClientInstallationProviderResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.AwaitableGetClientInstallationProviderResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.saml.Client">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">Client</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">assertion_consumer_post_url=None</em>, <em class="sig-param">assertion_consumer_redirect_url=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_signature_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">force_name_id_format=None</em>, <em class="sig-param">force_post_binding=None</em>, <em class="sig-param">front_channel_logout=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">idp_initiated_sso_relay_state=None</em>, <em class="sig-param">idp_initiated_sso_url_name=None</em>, <em class="sig-param">include_authn_statement=None</em>, <em class="sig-param">logout_service_post_binding_url=None</em>, <em class="sig-param">logout_service_redirect_binding_url=None</em>, <em class="sig-param">master_saml_processing_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_id_format=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">root_url=None</em>, <em class="sig-param">sign_assertions=None</em>, <em class="sig-param">sign_documents=None</em>, <em class="sig-param">signing_certificate=None</em>, <em class="sig-param">signing_private_key=None</em>, <em class="sig-param">valid_redirect_uris=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.Client" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Keycloak clients that use the SAML protocol.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">include_authn_statement</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, an <code class="docutils literal notranslate"><span class="pre">AuthnStatement</span></code> will be included in the SAML response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sign_documents</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the SAML document will be signed by Keycloak using the realm’s private key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sign_assertions</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the SAML assertions will be signed by Keycloak using the realm’s private key, and embedded within the SAML XML Auth response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_signature_required</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, Keycloak will expect that documents originating from a client will be signed using the certificate and/or key configured via <code class="docutils literal notranslate"><span class="pre">signing_certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">signing_private_key</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">force_post_binding</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, Keycloak will always respond to an authentication request via the SAML POST Binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">front_channel_logout</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, this client will require a browser redirect in order to perform a logout.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_id_format</span></code> - (Optional) Sets the Name ID format for the subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">root_url</span></code> - (Optional) When specified, this value is prepended to all relative URLs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valid_redirect_uris</span></code> - (Optional) When specified, Keycloak will use this list to validate given Assertion Consumer URLs specified in the authentication request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">base_url</span></code> - (Optional) When specified, this URL will be used whenever Keycloak needs to link to this client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_saml_processing_url</span></code> - (Optional) When specified, this URL will be used for all SAML requests.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signing_certificate</span></code> - (Optional) If documents or assertions from the client are signed, this certificate will be used to verify the signature.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signing_private_key</span></code> - (Optional) If documents or assertions from the client are signed, this private key will be used to verify the signature.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idp_initiated_sso_url_name</span></code> - (Optional) URL fragment name to reference client when you want to do IDP Initiated SSO.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idp_initiated_sso_relay_state</span></code> - (Optional) Relay state you want to send with SAML request when you want to do IDP Initiated SSO.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">assertion_consumer_post_url</span></code> - (Optional) SAML POST Binding URL for the client’s assertion consumer service (login responses).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">assertion_consumer_redirect_url</span></code> - (Optional) SAML Redirect Binding URL for the client’s assertion consumer service (login responses).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout_service_post_binding_url</span></code> - (Optional) SAML POST Binding URL for the client’s single logout service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout_service_redirect_binding_url</span></code> - (Optional) SAML Redirect Binding URL for the client’s single logout service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">full_scope_allowed</span></code> - (Optional) - Allow to include all roles mappings in the access token</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.saml.Client.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">assertion_consumer_post_url=None</em>, <em class="sig-param">assertion_consumer_redirect_url=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_signature_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">force_name_id_format=None</em>, <em class="sig-param">force_post_binding=None</em>, <em class="sig-param">front_channel_logout=None</em>, <em class="sig-param">full_scope_allowed=None</em>, <em class="sig-param">idp_initiated_sso_relay_state=None</em>, <em class="sig-param">idp_initiated_sso_url_name=None</em>, <em class="sig-param">include_authn_statement=None</em>, <em class="sig-param">logout_service_post_binding_url=None</em>, <em class="sig-param">logout_service_redirect_binding_url=None</em>, <em class="sig-param">master_saml_processing_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_id_format=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">root_url=None</em>, <em class="sig-param">sign_assertions=None</em>, <em class="sig-param">sign_documents=None</em>, <em class="sig-param">signing_certificate=None</em>, <em class="sig-param">signing_private_key=None</em>, <em class="sig-param">valid_redirect_uris=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.Client.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.saml.Client.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.Client.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.Client.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.Client.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.GetClientInstallationProviderResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">GetClientInstallationProviderResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.GetClientInstallationProviderResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientInstallationProvider.</p>
<dl class="attribute">
<dt id="pulumi_keycloak.saml.GetClientInstallationProviderResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.GetClientInstallationProviderResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_keycloak.saml.IdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">IdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">force_authn=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">name_id_policy_format=None</em>, <em class="sig-param">post_binding_authn_request=None</em>, <em class="sig-param">post_binding_logout=None</em>, <em class="sig-param">post_binding_response=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">signing_certificate=None</em>, <em class="sig-param">single_logout_service_url=None</em>, <em class="sig-param">single_sign_on_service_url=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">validate_signature=None</em>, <em class="sig-param">want_assertions_encrypted=None</em>, <em class="sig-param">want_assertions_signed=None</em>, <em class="sig-param">xml_sign_key_info_key_name_transformer=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows to create and manage SAML Identity Providers within Keycloak.</p>
<p>SAML (Security Assertion Markup Language) identity providers allows to authenticate through a third-party system, using SAML standard.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> - (Required) The name of the realm. This is unique across Keycloak.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alias</span></code> - (Optional) The uniq name of identity provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> - (Optional) When false, users and clients will not be able to access this realm. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> - (Optional) The display name for the realm that is shown when logging in to the admin console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">store_token</span></code> - (Optional) Enable/disable if tokens must be stored after authenticating users. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">add_read_token_role_on_create</span></code> - (Optional) Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trust_email</span></code> - (Optional) If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">link_only</span></code> - (Optional) If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t want to allow login from the provider, but want to integrate with a provider. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hide_on_login_page</span></code> - (Optional) If hidden, then login with this provider is possible only if requested explicitly, e.g. using the ‘kc_idp_hint’ parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">first_broker_login_flow_alias</span></code> - (Optional) Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Defaults to <code class="docutils literal notranslate"><span class="pre">first</span> <span class="pre">broker</span> <span class="pre">login</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">post_broker_login_flow_alias</span></code> - (Optional) Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Defaults to empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticate_by_default</span></code> - (Optional) Authenticate users by default. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">single_sign_on_service_url</span></code> - (Optional) The Url that must be used to send authentication requests (SAML AuthnRequest).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">single_logout_service_url</span></code> - (Optional) The Url that must be used to send logout requests.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backchannel_supported</span></code> - (Optional) Does the external IDP support back-channel logout ?.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_id_policy_format</span></code> - (Optional) Specifies the URI reference corresponding to a name identifier format. Defaults to empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">post_binding_response</span></code> - (Optional) Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used..</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">post_binding_authn_request</span></code> - (Optional) Indicates whether the AuthnRequest must be sent using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">post_binding_logout</span></code> - (Optional) Indicates whether to respond to requests using HTTP-POST binding. If false, HTTP-REDIRECT binding will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">want_assertions_signed</span></code> - (Optional) Indicates whether this service provider expects a signed Assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">want_assertions_encrypted</span></code> - (Optional) Indicates whether this service provider expects an encrypted Assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">force_authn</span></code> - (Optional) Indicates whether the identity provider must authenticate the presenter directly rather than rely on a previous security context.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validate_signature</span></code> - (Optional) Enable/disable signature validation of SAML responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signing_certificate</span></code> - (Optional) Signing Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signature_algorithm</span></code> - (Optional) Signing Algorithm. Defaults to empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xml_sign_key_info_key_name_transformer</span></code> - (Optional) Sign Key Transformer. Defaults to empty.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>backchannel_supported</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the external IDP support backchannel logout?</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for Identity Providers.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>force_authn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Require Force Authn.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>name_id_policy_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name ID Policy Format.</p></li>
<li><p><strong>post_binding_authn_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Authn Request.</p></li>
<li><p><strong>post_binding_logout</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Logout.</p></li>
<li><p><strong>post_binding_response</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Response.</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signing Algorithm.</p></li>
<li><p><strong>signing_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signing Certificate.</p></li>
<li><p><strong>single_logout_service_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logout URL.</p></li>
<li><p><strong>single_sign_on_service_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSO Logout URL.</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>validate_signature</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable signature validation of SAML responses.</p></li>
<li><p><strong>want_assertions_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Want Assertions Encrypted.</p></li>
<li><p><strong>want_assertions_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Want Assertions Signed.</p></li>
<li><p><strong>xml_sign_key_info_key_name_transformer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign Key Transformer.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.add_read_token_role_on_create">
<code class="sig-name descname">add_read_token_role_on_create</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.add_read_token_role_on_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.authenticate_by_default">
<code class="sig-name descname">authenticate_by_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.authenticate_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable authenticate users by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.backchannel_supported">
<code class="sig-name descname">backchannel_supported</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.backchannel_supported" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the external IDP support backchannel logout?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name for Identity Providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable this identity provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.first_broker_login_flow_alias">
<code class="sig-name descname">first_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.first_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.force_authn">
<code class="sig-name descname">force_authn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.force_authn" title="Permalink to this definition">¶</a></dt>
<dd><p>Require Force Authn.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.hide_on_login_page">
<code class="sig-name descname">hide_on_login_page</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.hide_on_login_page" title="Permalink to this definition">¶</a></dt>
<dd><p>Hide On Login Page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.internal_id">
<code class="sig-name descname">internal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.internal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal Identity Provider Id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.link_only">
<code class="sig-name descname">link_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.link_only" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.name_id_policy_format">
<code class="sig-name descname">name_id_policy_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.name_id_policy_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Name ID Policy Format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.post_binding_authn_request">
<code class="sig-name descname">post_binding_authn_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.post_binding_authn_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Post Binding Authn Request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.post_binding_logout">
<code class="sig-name descname">post_binding_logout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.post_binding_logout" title="Permalink to this definition">¶</a></dt>
<dd><p>Post Binding Logout.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.post_binding_response">
<code class="sig-name descname">post_binding_response</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.post_binding_response" title="Permalink to this definition">¶</a></dt>
<dd><p>Post Binding Response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.post_broker_login_flow_alias">
<code class="sig-name descname">post_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.post_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.realm">
<code class="sig-name descname">realm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.signature_algorithm">
<code class="sig-name descname">signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Signing Algorithm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.signing_certificate">
<code class="sig-name descname">signing_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.signing_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Signing Certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.single_logout_service_url">
<code class="sig-name descname">single_logout_service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.single_logout_service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Logout URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.single_sign_on_service_url">
<code class="sig-name descname">single_sign_on_service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.single_sign_on_service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>SSO Logout URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.store_token">
<code class="sig-name descname">store_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.store_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if tokens must be stored after authenticating users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.trust_email">
<code class="sig-name descname">trust_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.trust_email" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.validate_signature">
<code class="sig-name descname">validate_signature</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.validate_signature" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable signature validation of SAML responses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.want_assertions_encrypted">
<code class="sig-name descname">want_assertions_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.want_assertions_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Want Assertions Encrypted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.want_assertions_signed">
<code class="sig-name descname">want_assertions_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.want_assertions_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Want Assertions Signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.saml.IdentityProvider.xml_sign_key_info_key_name_transformer">
<code class="sig-name descname">xml_sign_key_info_key_name_transformer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.xml_sign_key_info_key_name_transformer" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign Key Transformer.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.saml.IdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">force_authn=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">internal_id=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">name_id_policy_format=None</em>, <em class="sig-param">post_binding_authn_request=None</em>, <em class="sig-param">post_binding_logout=None</em>, <em class="sig-param">post_binding_response=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">signing_certificate=None</em>, <em class="sig-param">single_logout_service_url=None</em>, <em class="sig-param">single_sign_on_service_url=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">validate_signature=None</em>, <em class="sig-param">want_assertions_encrypted=None</em>, <em class="sig-param">want_assertions_signed=None</em>, <em class="sig-param">xml_sign_key_info_key_name_transformer=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>backchannel_supported</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the external IDP support backchannel logout?</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for Identity Providers.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>force_authn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Require Force Authn.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>internal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal Identity Provider Id</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>name_id_policy_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name ID Policy Format.</p></li>
<li><p><strong>post_binding_authn_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Authn Request.</p></li>
<li><p><strong>post_binding_logout</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Logout.</p></li>
<li><p><strong>post_binding_response</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Post Binding Response.</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signing Algorithm.</p></li>
<li><p><strong>signing_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signing Certificate.</p></li>
<li><p><strong>single_logout_service_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logout URL.</p></li>
<li><p><strong>single_sign_on_service_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSO Logout URL.</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>validate_signature</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable signature validation of SAML responses.</p></li>
<li><p><strong>want_assertions_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Want Assertions Encrypted.</p></li>
<li><p><strong>want_assertions_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Want Assertions Signed.</p></li>
<li><p><strong>xml_sign_key_info_key_name_transformer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign Key Transformer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.saml.IdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.IdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.IdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.UserAttributeProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">UserAttributeProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">saml_attribute_name=None</em>, <em class="sig-param">saml_attribute_name_format=None</em>, <em class="sig-param">user_attribute=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserAttributeProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user attribute protocol mappers for
SAML clients within Keycloak.</p>
<p>SAML user attribute protocol mappers allow you to map custom attributes defined
for a user within Keycloak to an attribute in a SAML assertion. Protocol mappers
can be defined for a single client, or they can be defined for a client scope which
can be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The SAML client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The SAML client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_attribute</span></code> - (Required) The custom user attribute to map.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">friendly_name</span></code> - (Optional) An optional human-friendly name for this attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml_attribute_name</span></code> - (Required) The name of the SAML attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml_attribute_name_format</span></code> - (Required) The SAML attribute Name Format. Can be one of <code class="docutils literal notranslate"><span class="pre">Unspecified</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, or <code class="docutils literal notranslate"><span class="pre">URI</span> <span class="pre">Reference</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.saml.UserAttributeProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">saml_attribute_name=None</em>, <em class="sig-param">saml_attribute_name_format=None</em>, <em class="sig-param">user_attribute=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserAttributeProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.saml.UserAttributeProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserAttributeProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.UserAttributeProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserAttributeProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.UserPropertyProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">UserPropertyProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">saml_attribute_name=None</em>, <em class="sig-param">saml_attribute_name_format=None</em>, <em class="sig-param">user_property=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserPropertyProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user property protocol mappers for
SAML clients within Keycloak.</p>
<p>SAML user property protocol mappers allow you to map properties of the Keycloak
user model to an attribute in a SAML assertion. Protocol mappers
can be defined for a single client, or they can be defined for a client scope which
can be shared between multiple different clients.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not specified) The SAML client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> - (Required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not specified) The SAML client scope this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_property</span></code> - (Required) The property of the Keycloak user model to map.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">friendly_name</span></code> - (Optional) An optional human-friendly name for this attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml_attribute_name</span></code> - (Required) The name of the SAML attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml_attribute_name_format</span></code> - (Required) The SAML attribute Name Format. Can be one of <code class="docutils literal notranslate"><span class="pre">Unspecified</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, or <code class="docutils literal notranslate"><span class="pre">URI</span> <span class="pre">Reference</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_keycloak.saml.UserPropertyProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_scope_id=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">saml_attribute_name=None</em>, <em class="sig-param">saml_attribute_name_format=None</em>, <em class="sig-param">user_property=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserPropertyProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.saml.UserPropertyProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserPropertyProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.UserPropertyProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.UserPropertyProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.saml.get_client_installation_provider">
<code class="sig-prename descclassname">pulumi_keycloak.saml.</code><code class="sig-name descname">get_client_installation_provider</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.saml.get_client_installation_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
