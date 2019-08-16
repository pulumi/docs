---
title: Package pulumi_azuread
---

<div class="section" id="pulumi-azure-active-directory">
<h1>Pulumi Azure Active Directory<a class="headerlink" href="#pulumi-azure-active-directory" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuread/issues">pulumi/pulumi-azuread repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/issues">terraform-providers/terraform-provider-azuread repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azuread"></span><dl class="class">
<dt id="pulumi_azuread.Application">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>app_roles=None</em>, <em>available_to_other_tenants=None</em>, <em>group_membership_claims=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>oauth2_permissions=None</em>, <em>public_client=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>type=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>app_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></li>
<li><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>group_membership_claims</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</li>
<li><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</li>
<li><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</li>
<li><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</li>
<li><strong>public_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</li>
<li><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.Application.app_roles">
<code class="descname">app_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.available_to_other_tenants">
<code class="descname">available_to_other_tenants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.group_membership_claims">
<code class="descname">group_membership_claims</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.homepage">
<code class="descname">homepage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.homepage" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.identifier_uris">
<code class="descname">identifier_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.oauth2_allow_implicit_flow">
<code class="descname">oauth2_allow_implicit_flow</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.oauth2_permissions">
<code class="descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s Object ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.public_client">
<code class="descname">public_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.public_client" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.reply_urls">
<code class="descname">reply_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.required_resource_accesses">
<code class="descname">required_resource_accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.Application.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>app_roles=None</em>, <em>application_id=None</em>, <em>available_to_other_tenants=None</em>, <em>group_membership_claims=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>public_client=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] app_roles: A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a>
:param pulumi.Input[str] application_id: The Application ID.
:param pulumi.Input[bool] available_to_other_tenants: Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] group_membership_claims: Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.
:param pulumi.Input[str] homepage: The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.
:param pulumi.Input[list] identifier_uris: A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
:param pulumi.Input[str] name: The display name for the application.
:param pulumi.Input[bool] oauth2_allow_implicit_flow: Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[list] oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.
:param pulumi.Input[str] object_id: The Application’s Object ID.
:param pulumi.Input[bool] public_client: Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[list] reply_urls: A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
:param pulumi.Input[list] required_resource_accesses: A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.
:param pulumi.Input[str] type: Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Application.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Application.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ApplicationPassword">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">ApplicationPassword</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>application_object_id=None</em>, <em>end_date=None</em>, <em>end_date_relative=None</em>, <em>key_id=None</em>, <em>start_date=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</li>
<li><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</li>
<li><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</li>
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</li>
<li><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Application .</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.application_object_id">
<code class="descname">application_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.end_date">
<code class="descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.end_date_relative">
<code class="descname">end_date_relative</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.start_date">
<code class="descname">start_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Application .</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.ApplicationPassword.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>application_object_id=None</em>, <em>end_date=None</em>, <em>end_date_relative=None</em>, <em>key_id=None</em>, <em>start_date=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] application_object_id: The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
:param pulumi.Input[str] end_date: The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.
:param pulumi.Input[str] end_date_relative: A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.
:param pulumi.Input[str] key_id: A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
:param pulumi.Input[str] start_date: The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.
:param pulumi.Input[str] value: The Password for this Application .</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ApplicationPassword.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ApplicationPassword.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.AwaitableGetApplicationResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetApplicationResult</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>application_id=None</em>, <em>available_to_other_tenants=None</em>, <em>group_membership_claims=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetDomainsResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetDomainsResult</code><span class="sig-paren">(</span><em>domains=None</em>, <em>include_unverified=None</em>, <em>only_default=None</em>, <em>only_initial=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em>members=None</em>, <em>name=None</em>, <em>object_id=None</em>, <em>owners=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetGroupsResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em>names=None</em>, <em>object_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetServicePrincipalResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetServicePrincipalResult</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>application_id=None</em>, <em>display_name=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em>account_enabled=None</em>, <em>display_name=None</em>, <em>mail=None</em>, <em>mail_nickname=None</em>, <em>object_id=None</em>, <em>user_principal_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetUsersResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em>object_ids=None</em>, <em>user_principal_names=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetApplicationResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetApplicationResult</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>application_id=None</em>, <em>available_to_other_tenants=None</em>, <em>group_membership_claims=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.app_roles">
<code class="descname">app_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Application ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.available_to_other_tenants">
<code class="descname">available_to_other_tenants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.group_membership_claims">
<code class="descname">group_membership_claims</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.identifier_uris">
<code class="descname">identifier_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow">
<code class="descname">oauth2_allow_implicit_flow</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_permissions">
<code class="descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Object ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.reply_urls">
<code class="descname">reply_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.required_resource_accesses">
<code class="descname">required_resource_accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the permission</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetDomainsResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetDomainsResult</code><span class="sig-paren">(</span><em>domains=None</em>, <em>include_unverified=None</em>, <em>only_default=None</em>, <em>only_initial=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomains.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetDomainsResult.domains">
<code class="descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">domain</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetDomainsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>members=None</em>, <em>name=None</em>, <em>object_id=None</em>, <em>owners=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetGroupsResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetGroupsResult</code><span class="sig-paren">(</span><em>names=None</em>, <em>object_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.names">
<code class="descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Names of the Azure AD Groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.object_ids">
<code class="descname">object_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetServicePrincipalResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetServicePrincipalResult</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>application_id=None</em>, <em>display_name=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServicePrincipal.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetServicePrincipalResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetServicePrincipalResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>account_enabled=None</em>, <em>display_name=None</em>, <em>mail=None</em>, <em>mail_nickname=None</em>, <em>object_id=None</em>, <em>user_principal_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.account_enabled">
<code class="descname">account_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">True</span></code> if the account is enabled; otherwise <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.mail">
<code class="descname">mail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.mail_nickname">
<code class="descname">mail_nickname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail_nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>The email alias of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.user_principal_name">
<code class="descname">user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetUsersResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetUsersResult</code><span class="sig-paren">(</span><em>object_ids=None</em>, <em>user_principal_names=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.object_ids">
<code class="descname">object_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.user_principal_names">
<code class="descname">user_principal_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.user_principal_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Names of the Azure AD Users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.Group">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>name=None</em>, <em>owners=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Group within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">groups</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. In addition it must also have either the <code class="docutils literal notranslate"><span class="pre">Company</span> <span class="pre">Administrator</span></code> or <code class="docutils literal notranslate"><span class="pre">User</span> <span class="pre">Account</span> <span class="pre">Administrator</span></code> Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the <strong>AzureAD PowerShell Module</strong>, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to <a class="reference external" href="https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember">this documentation</a> for more details.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group. Changing this forces a new resource to be created.</li>
<li><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of owners who own this Group. Supported Object types are Users or Service Principals.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.Group.members">
<code class="descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Group.owners">
<code class="descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of owners who own this Group. Supported Object types are Users or Service Principals.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.Group.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>members=None</em>, <em>name=None</em>, <em>object_id=None</em>, <em>owners=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] members: A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
:param pulumi.Input[str] name: The display name for the Group. Changing this forces a new resource to be created.
:param pulumi.Input[list] owners: A set of owners who own this Group. Supported Object types are Users or Service Principals.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.GroupMember">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GroupMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>group_object_id=None</em>, <em>member_object_id=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single Group Membership within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> Do not use this resource at the same time as <code class="docutils literal notranslate"><span class="pre">azuread_group.members</span></code>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>group_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</li>
<li><strong>member_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.GroupMember.group_object_id">
<code class="descname">group_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GroupMember.group_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GroupMember.member_object_id">
<code class="descname">member_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GroupMember.member_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.GroupMember.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>group_object_id=None</em>, <em>member_object_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] group_object_id: The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
:param pulumi.Input[str] member_object_id: The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.GroupMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.GroupMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Provider">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>client_certificate_password=None</em>, <em>client_certificate_path=None</em>, <em>client_id=None</em>, <em>client_secret=None</em>, <em>environment=None</em>, <em>msi_endpoint=None</em>, <em>subscription_id=None</em>, <em>tenant_id=None</em>, <em>use_msi=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azuread package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_azuread.Provider.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipal">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">ServicePrincipal</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>oauth2_permissions=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. Please see The Granting a Service Principal permission to manage AAD for the required steps.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</li>
<li><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to apply to the Service Principal.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Azure AD Application for which to create a Service Principal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure Active Directory Application associated with this Service Principal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.oauth2_permissions">
<code class="descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Principal’s Object ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to apply to the Service Principal.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.ServicePrincipal.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>display_name=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipal resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] application_id: The ID of the Azure AD Application for which to create a Service Principal.
:param pulumi.Input[str] display_name: The Display Name of the Azure Active Directory Application associated with this Service Principal.
:param pulumi.Input[list] oauth2_permissions: A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.
:param pulumi.Input[str] object_id: The Service Principal’s Object ID.
:param pulumi.Input[list] tags: A list of tags to apply to the Service Principal.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipal.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipal.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipalPassword">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">ServicePrincipalPassword</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>end_date=None</em>, <em>end_date_relative=None</em>, <em>key_id=None</em>, <em>service_principal_id=None</em>, <em>start_date=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with a Service Principal within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</li>
<li><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</li>
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</li>
<li><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</li>
<li><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Service Principal.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date">
<code class="descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date_relative">
<code class="descname">end_date_relative</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.service_principal_id">
<code class="descname">service_principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.start_date">
<code class="descname">start_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Service Principal.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.ServicePrincipalPassword.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>end_date=None</em>, <em>end_date_relative=None</em>, <em>key_id=None</em>, <em>service_principal_id=None</em>, <em>start_date=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipalPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] end_date: The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.
:param pulumi.Input[str] end_date_relative: A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.
:param pulumi.Input[str] key_id: A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
:param pulumi.Input[str] service_principal_id: The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
:param pulumi.Input[str] start_date: The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.
:param pulumi.Input[str] value: The Password for this Service Principal.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.User">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_enabled=None</em>, <em>display_name=None</em>, <em>force_password_change=None</em>, <em>mail_nickname=None</em>, <em>password=None</em>, <em>user_principal_name=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a User within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.ReadWrite.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</li>
<li><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</li>
<li><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azuread.User.account_enabled">
<code class="descname">account_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">mail_nickname</span></code>- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to display in the address book for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.force_password_change">
<code class="descname">force_password_change</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.force_password_change" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.mail">
<code class="descname">mail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.user_principal_name">
<code class="descname">user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azuread.User.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>account_enabled=None</em>, <em>display_name=None</em>, <em>force_password_change=None</em>, <em>mail=None</em>, <em>mail_nickname=None</em>, <em>object_id=None</em>, <em>password=None</em>, <em>user_principal_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] account_enabled: <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</li>
<li><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary email address of the Azure AD User.</li>
<li><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD User.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</li>
<li><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.get_application">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_application</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>name=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/application.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_domains">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_domains</code><span class="sig-paren">(</span><em>include_unverified=None</em>, <em>only_default=None</em>, <em>only_initial=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Domains within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.Read.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/domains.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/domains.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_group">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>object_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_groups">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_groups</code><span class="sig-paren">(</span><em>names=None</em>, <em>object_ids=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or Display Names for multiple Azure Active Directory groups.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/groups.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/groups.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_service_principal">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_service_principal</code><span class="sig-paren">(</span><em>app_roles=None</em>, <em>application_id=None</em>, <em>display_name=None</em>, <em>oauth2_permissions=None</em>, <em>object_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an existing Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/service_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/service_principal.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_user">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>object_id=None</em>, <em>user_principal_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/user.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_users">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_users</code><span class="sig-paren">(</span><em>object_ids=None</em>, <em>user_principal_names=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or UPNs for multiple Azure Active Directory users.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/users.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/users.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
