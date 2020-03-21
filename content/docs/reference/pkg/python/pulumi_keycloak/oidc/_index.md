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
<dd><p>Create a GoogleIdentityProvider resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In</p>
<blockquote>
<div><p>case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret.</p></li>
<li><p><strong>default_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value’. Default: ‘openid profile email’</p></li>
<li><p><strong>disable_user_info</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>hosted_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set ‘hd’ query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When ‘*’ is entered, any hosted account can be used.</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – provider id, is always google, unless you have a extended custom implementation</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>request_refresh_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set ‘access_type’ query parameter to ‘offline’ when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>use_user_ip_param</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set ‘userIp’ query parameter when invoking on Google’s User Info service. This will use the user’s ip address. Useful if
Google is throttling access to the User Info service.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.accepts_prompt_none_forward_from_client">
<code class="sig-name descname">accepts_prompt_none_forward_from_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.accepts_prompt_none_forward_from_client" title="Permalink to this definition">¶</a></dt>
<dd><p>This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.add_read_token_role_on_create">
<code class="sig-name descname">add_read_token_role_on_create</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.add_read_token_role_on_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.authenticate_by_default">
<code class="sig-name descname">authenticate_by_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.authenticate_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable authenticate users by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.default_scopes">
<code class="sig-name descname">default_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.default_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value’. Default: ‘openid profile email’</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.disable_user_info">
<code class="sig-name descname">disable_user_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.disable_user_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Not used by this provider, Will be implicitly Google</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable this identity provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.first_broker_login_flow_alias">
<code class="sig-name descname">first_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.first_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.hide_on_login_page">
<code class="sig-name descname">hide_on_login_page</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.hide_on_login_page" title="Permalink to this definition">¶</a></dt>
<dd><p>Hide On Login Page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.hosted_domain">
<code class="sig-name descname">hosted_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.hosted_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Set ‘hd’ query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When ‘*’ is entered, any hosted account can be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.internal_id">
<code class="sig-name descname">internal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.internal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal Identity Provider Id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.link_only">
<code class="sig-name descname">link_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.link_only" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.post_broker_login_flow_alias">
<code class="sig-name descname">post_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.post_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.provider_id">
<code class="sig-name descname">provider_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>provider id, is always google, unless you have a extended custom implementation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.realm">
<code class="sig-name descname">realm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.request_refresh_token">
<code class="sig-name descname">request_refresh_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.request_refresh_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Set ‘access_type’ query parameter to ‘offline’ when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.store_token">
<code class="sig-name descname">store_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.store_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if tokens must be stored after authenticating users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.trust_email">
<code class="sig-name descname">trust_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.trust_email" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.GoogleIdentityProvider.use_user_ip_param">
<code class="sig-name descname">use_user_ip_param</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.GoogleIdentityProvider.use_user_ip_param" title="Permalink to this definition">¶</a></dt>
<dd><p>Set ‘userIp’ query parameter when invoking on Google’s User Info service. This will use the user’s ip address. Useful if
Google is throttling access to the User Info service.</p>
</dd></dl>

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
<li><p><strong>accepts_prompt_none_forward_from_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p></li>
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret.</p></li>
<li><p><strong>default_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value’. Default: ‘openid profile email’</p></li>
<li><p><strong>disable_user_info</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Not used by this provider, Will be implicitly Google</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>hosted_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set ‘hd’ query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When ‘*’ is entered, any hosted account can be used.</p></li>
<li><p><strong>internal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal Identity Provider Id</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – provider id, is always google, unless you have a extended custom implementation</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>request_refresh_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set ‘access_type’ query parameter to ‘offline’ when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>use_user_ip_param</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set ‘userIp’ query parameter when invoking on Google’s User Info service. This will use the user’s ip address. Useful if
Google is throttling access to the User Info service.</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.oidc.</code><code class="sig-name descname">IdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepts_prompt_none_forward_from_client=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">login_hint=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">ui_locales=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">validate_signature=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IdentityProvider resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In</p>
<blockquote>
<div><p>case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>authorization_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OIDC authorization URL.</p></li>
<li><p><strong>backchannel_supported</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the external IDP support backchannel logout?</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret.</p></li>
<li><p><strong>default_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes to be sent when asking for authorization. It can be a space-separated list of scopes. Defaults to ‘openid’.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for Identity Providers.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON Web Key Set URL</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>login_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login Hint.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logout URL</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – provider id, is always oidc, unless you have a custom implementation</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>token_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token URL.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>ui_locales</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Pass current locale to identity provider</p></li>
<li><p><strong>user_info_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User Info URL</p></li>
<li><p><strong>validate_signature</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable signature validation of external IDP signatures.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.accepts_prompt_none_forward_from_client">
<code class="sig-name descname">accepts_prompt_none_forward_from_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.accepts_prompt_none_forward_from_client" title="Permalink to this definition">¶</a></dt>
<dd><p>This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.add_read_token_role_on_create">
<code class="sig-name descname">add_read_token_role_on_create</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.add_read_token_role_on_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.authenticate_by_default">
<code class="sig-name descname">authenticate_by_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.authenticate_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable authenticate users by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.authorization_url">
<code class="sig-name descname">authorization_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.authorization_url" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC authorization URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.backchannel_supported">
<code class="sig-name descname">backchannel_supported</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.backchannel_supported" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the external IDP support backchannel logout?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Secret.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.default_scopes">
<code class="sig-name descname">default_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.default_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes to be sent when asking for authorization. It can be a space-separated list of scopes. Defaults to ‘openid’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name for Identity Providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable this identity provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.first_broker_login_flow_alias">
<code class="sig-name descname">first_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.first_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.hide_on_login_page">
<code class="sig-name descname">hide_on_login_page</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.hide_on_login_page" title="Permalink to this definition">¶</a></dt>
<dd><p>Hide On Login Page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.internal_id">
<code class="sig-name descname">internal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.internal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal Identity Provider Id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.jwks_url">
<code class="sig-name descname">jwks_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.jwks_url" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON Web Key Set URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.link_only">
<code class="sig-name descname">link_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.link_only" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.login_hint">
<code class="sig-name descname">login_hint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.login_hint" title="Permalink to this definition">¶</a></dt>
<dd><p>Login Hint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.logout_url">
<code class="sig-name descname">logout_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.logout_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Logout URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.post_broker_login_flow_alias">
<code class="sig-name descname">post_broker_login_flow_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.post_broker_login_flow_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.provider_id">
<code class="sig-name descname">provider_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>provider id, is always oidc, unless you have a custom implementation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.realm">
<code class="sig-name descname">realm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.store_token">
<code class="sig-name descname">store_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.store_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable if tokens must be stored after authenticating users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.token_url">
<code class="sig-name descname">token_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.token_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Token URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.trust_email">
<code class="sig-name descname">trust_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.trust_email" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.ui_locales">
<code class="sig-name descname">ui_locales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.ui_locales" title="Permalink to this definition">¶</a></dt>
<dd><p>Pass current locale to identity provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.user_info_url">
<code class="sig-name descname">user_info_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.user_info_url" title="Permalink to this definition">¶</a></dt>
<dd><p>User Info URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.oidc.IdentityProvider.validate_signature">
<code class="sig-name descname">validate_signature</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.validate_signature" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/disable signature validation of external IDP signatures.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.oidc.IdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepts_prompt_none_forward_from_client=None</em>, <em class="sig-param">add_read_token_role_on_create=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">authenticate_by_default=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">backchannel_supported=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scopes=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra_config=None</em>, <em class="sig-param">first_broker_login_flow_alias=None</em>, <em class="sig-param">hide_on_login_page=None</em>, <em class="sig-param">internal_id=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">link_only=None</em>, <em class="sig-param">login_hint=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">post_broker_login_flow_alias=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">realm=None</em>, <em class="sig-param">store_token=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">trust_email=None</em>, <em class="sig-param">ui_locales=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">validate_signature=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.oidc.IdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepts_prompt_none_forward_from_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.</p></li>
<li><p><strong>add_read_token_role_on_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias uniquely identifies an identity provider and it is also used to build the redirect uri.</p></li>
<li><p><strong>authenticate_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable authenticate users by default.</p></li>
<li><p><strong>authorization_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OIDC authorization URL.</p></li>
<li><p><strong>backchannel_supported</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does the external IDP support backchannel logout?</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret.</p></li>
<li><p><strong>default_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes to be sent when asking for authorization. It can be a space-separated list of scopes. Defaults to ‘openid’.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for Identity Providers.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable this identity provider.</p></li>
<li><p><strong>first_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after first login with this identity provider. Term ‘First Login’ means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.</p></li>
<li><p><strong>hide_on_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Hide On Login Page.</p></li>
<li><p><strong>internal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal Identity Provider Id</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON Web Key Set URL</p></li>
<li><p><strong>link_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don’t
want to allow login from the provider, but want to integrate with a provider</p></li>
<li><p><strong>login_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login Hint.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logout URL</p></li>
<li><p><strong>post_broker_login_flow_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don’t want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – provider id, is always oidc, unless you have a custom implementation</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>store_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable if tokens must be stored after authenticating users.</p></li>
<li><p><strong>token_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token URL.</p></li>
<li><p><strong>trust_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled then email provided by this provider is not verified even if verification is enabled for the realm.</p></li>
<li><p><strong>ui_locales</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Pass current locale to identity provider</p></li>
<li><p><strong>user_info_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User Info URL</p></li>
<li><p><strong>validate_signature</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable signature validation of external IDP signatures.</p></li>
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
