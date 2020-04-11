---
title: Package pulumi_azuread
title_tag: Package pulumi_azuread | Python SDK
linktitle: pulumi_azuread
notitle: true
---

<div class="section" id="pulumi-azure-active-directory">
<h1>Pulumi Azure Active Directory<a class="headerlink" href="#pulumi-azure-active-directory" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuread/issues">pulumi/pulumi-azuread repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/issues">terraform-providers/terraform-provider-azuread repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuread"></span><dl class="class">
<dt id="pulumi_azuread.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_roles=None</em>, <em class="sig-param">available_to_other_tenants=None</em>, <em class="sig-param">group_membership_claims=None</em>, <em class="sig-param">homepage=None</em>, <em class="sig-param">identifier_uris=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oauth2_allow_implicit_flow=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">public_client=None</em>, <em class="sig-param">reply_urls=None</em>, <em class="sig-param">required_resource_accesses=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">owned</span> <span class="pre">by</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p></li>
<li><p><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>group_membership_claims</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</p></li>
<li><p><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the logout page.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p></li>
<li><p><strong>public_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p></li>
<li><p><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMemberTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Permission help text that appears in the admin app assignment and consent experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
<p>The <strong>required_resource_accesses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAccesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of <code class="docutils literal notranslate"><span class="pre">resource_access</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azuread.Application.app_roles">
<code class="sig-name descname">app_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMemberTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Permission help text that appears in the admin app assignment and consent experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.available_to_other_tenants">
<code class="sig-name descname">available_to_other_tenants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.group_membership_claims">
<code class="sig-name descname">group_membership_claims</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.homepage">
<code class="sig-name descname">homepage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.homepage" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.identifier_uris">
<code class="sig-name descname">identifier_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.logout_url">
<code class="sig-name descname">logout_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.logout_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the logout page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.oauth2_allow_implicit_flow">
<code class="sig-name descname">oauth2_allow_implicit_flow</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.oauth2_permissions">
<code class="sig-name descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s Object ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.owners">
<code class="sig-name descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.public_client">
<code class="sig-name descname">public_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.public_client" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.reply_urls">
<code class="sig-name descname">reply_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.required_resource_accesses">
<code class="sig-name descname">required_resource_accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAccesses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A collection of <code class="docutils literal notranslate"><span class="pre">resource_access</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_roles=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">available_to_other_tenants=None</em>, <em class="sig-param">group_membership_claims=None</em>, <em class="sig-param">homepage=None</em>, <em class="sig-param">identifier_uris=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oauth2_allow_implicit_flow=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">public_client=None</em>, <em class="sig-param">reply_urls=None</em>, <em class="sig-param">required_resource_accesses=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application ID.</p></li>
<li><p><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>group_membership_claims</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</p></li>
<li><p><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the logout page.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s Object ID.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p></li>
<li><p><strong>public_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p></li>
<li><p><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMemberTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Permission help text that appears in the admin app assignment and consent experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines if the app role is enabled: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
<p>The <strong>required_resource_accesses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAccesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of <code class="docutils literal notranslate"><span class="pre">resource_access</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the id property references an <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code> or an <code class="docutils literal notranslate"><span class="pre">AppRole</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Scope</span></code> or <code class="docutils literal notranslate"><span class="pre">Role</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ApplicationPassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ApplicationPassword</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">application_object_id=None</em>, <em class="sig-param">end_date=None</em>, <em class="sig-param">end_date_relative=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">start_date=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/application_password.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Application .</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.application_object_id">
<code class="sig-name descname">application_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.end_date">
<code class="sig-name descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.end_date_relative">
<code class="sig-name descname">end_date_relative</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.start_date">
<code class="sig-name descname">start_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ApplicationPassword.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Application .</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ApplicationPassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">application_object_id=None</em>, <em class="sig-param">end_date=None</em>, <em class="sig-param">end_date_relative=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">start_date=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Application .</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ApplicationPassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ApplicationPassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.AwaitableGetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param">app_roles=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">available_to_other_tenants=None</em>, <em class="sig-param">group_membership_claims=None</em>, <em class="sig-param">homepage=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identifier_uris=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oauth2_allow_implicit_flow=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">reply_urls=None</em>, <em class="sig-param">required_resource_accesses=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param">domains=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">include_unverified=None</em>, <em class="sig-param">only_default=None</em>, <em class="sig-param">only_initial=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">object_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetServicePrincipalResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetServicePrincipalResult</code><span class="sig-paren">(</span><em class="sig-param">app_roles=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">account_enabled=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">immutable_id=None</em>, <em class="sig-param">mail=None</em>, <em class="sig-param">mail_nickname=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">onpremises_sam_account_name=None</em>, <em class="sig-param">onpremises_user_principal_name=None</em>, <em class="sig-param">usage_location=None</em>, <em class="sig-param">user_principal_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">mail_nicknames=None</em>, <em class="sig-param">object_ids=None</em>, <em class="sig-param">user_principal_names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param">app_roles=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">available_to_other_tenants=None</em>, <em class="sig-param">group_membership_claims=None</em>, <em class="sig-param">homepage=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identifier_uris=None</em>, <em class="sig-param">logout_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oauth2_allow_implicit_flow=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">reply_urls=None</em>, <em class="sig-param">required_resource_accesses=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.app_roles">
<code class="sig-name descname">app_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Application ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.available_to_other_tenants">
<code class="sig-name descname">available_to_other_tenants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.group_membership_claims">
<code class="sig-name descname">group_membership_claims</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.identifier_uris">
<code class="sig-name descname">identifier_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.logout_url">
<code class="sig-name descname">logout_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.logout_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the logout page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow">
<code class="sig-name descname">oauth2_allow_implicit_flow</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_permissions">
<code class="sig-name descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Object ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.owners">
<code class="sig-name descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of User Object IDs that are assigned ownership of the application registration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.reply_urls">
<code class="sig-name descname">reply_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.required_resource_accesses">
<code class="sig-name descname">required_resource_accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetApplicationResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the permission</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetClientConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param">domains=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">include_unverified=None</em>, <em class="sig-param">only_default=None</em>, <em class="sig-param">only_initial=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomains.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetDomainsResult.domains">
<code class="sig-name descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">domain</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetDomainsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the AD Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.members" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Group members.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure AD Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.owners">
<code class="sig-name descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Group owners.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">object_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Names of the Azure AD Groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetGroupsResult.object_ids">
<code class="sig-name descname">object_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Groups.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetServicePrincipalResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetServicePrincipalResult</code><span class="sig-paren">(</span><em class="sig-param">app_roles=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServicePrincipal.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetServicePrincipalResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetServicePrincipalResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">account_enabled=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">immutable_id=None</em>, <em class="sig-param">mail=None</em>, <em class="sig-param">mail_nickname=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">onpremises_sam_account_name=None</em>, <em class="sig-param">onpremises_user_principal_name=None</em>, <em class="sig-param">usage_location=None</em>, <em class="sig-param">user_principal_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.account_enabled">
<code class="sig-name descname">account_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">True</span></code> if the account is enabled; otherwise <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.immutable_id">
<code class="sig-name descname">immutable_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.immutable_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The value used to associate an on-premises Active Directory user account with their Azure AD user object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.mail">
<code class="sig-name descname">mail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.mail_nickname">
<code class="sig-name descname">mail_nickname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail_nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>The email alias of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.onpremises_sam_account_name">
<code class="sig-name descname">onpremises_sam_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.onpremises_sam_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on premise sam account name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.onpremises_user_principal_name">
<code class="sig-name descname">onpremises_user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.onpremises_user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on premise user principal name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.usage_location">
<code class="sig-name descname">usage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.usage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The usage location of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUserResult.user_principal_name">
<code class="sig-name descname">user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUserResult.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">mail_nicknames=None</em>, <em class="sig-param">object_ids=None</em>, <em class="sig-param">user_principal_names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.mail_nicknames">
<code class="sig-name descname">mail_nicknames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.mail_nicknames" title="Permalink to this definition">¶</a></dt>
<dd><p>The email aliases of the Azure AD Users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.object_ids">
<code class="sig-name descname">object_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GetUsersResult.user_principal_names">
<code class="sig-name descname">user_principal_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetUsersResult.user_principal_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Names of the Azure AD Users.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owners=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Group within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">groups</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. In addition it must also have either the <code class="docutils literal notranslate"><span class="pre">Company</span> <span class="pre">Administrator</span></code> or <code class="docutils literal notranslate"><span class="pre">User</span> <span class="pre">Account</span> <span class="pre">Administrator</span></code> Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the <strong>AzureAD PowerShell Module</strong>, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to <a class="reference external" href="https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember">this documentation</a> for more details.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Group.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of owners who own this Group. Supported Object types are Users or Service Principals.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azuread.Group.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Group.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Group.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Group.owners">
<code class="sig-name descname">owners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of owners who own this Group. Supported Object types are Users or Service Principals.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">owners=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Group.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of owners who own this Group. Supported Object types are Users or Service Principals.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.GroupMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GroupMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_object_id=None</em>, <em class="sig-param">member_object_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single Group Membership within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Do not use this resource at the same time as <code class="docutils literal notranslate"><span class="pre">azuread_group.members</span></code>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>member_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azuread.GroupMember.group_object_id">
<code class="sig-name descname">group_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GroupMember.group_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.GroupMember.member_object_id">
<code class="sig-name descname">member_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GroupMember.member_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.GroupMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_object_id=None</em>, <em class="sig-param">member_object_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>member_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.GroupMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.GroupMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_certificate_password=None</em>, <em class="sig-param">client_certificate_path=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">msi_endpoint=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">use_msi=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azuread package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_azuread.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipal">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ServicePrincipal</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_role_assignment_required=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. Please see The Granting a Service Principal permission to manage AAD for the required steps.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_role_assignment_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to apply to the Service Principal.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for one of the <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this permission enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the permission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of this permission.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.app_role_assignment_required">
<code class="sig-name descname">app_role_assignment_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.app_role_assignment_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Azure AD Application for which to create a Service Principal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure Active Directory Application associated with this Service Principal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.oauth2_permissions">
<code class="sig-name descname">oauth2_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier for one of the <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this permission enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the permission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of this permission.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Principal’s Object ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipal.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to apply to the Service Principal.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipal.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_role_assignment_required=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipal resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_role_assignment_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name of the Azure Active Directory Application associated with this Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Principal’s Object ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to apply to the Service Principal.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the admin consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for one of the <code class="docutils literal notranslate"><span class="pre">OAuth2Permission</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this permission enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the permission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name of the user consent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of this permission.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipal.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipal.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipalPassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ServicePrincipalPassword</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_date=None</em>, <em class="sig-param">end_date_relative=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">service_principal_id=None</em>, <em class="sig-param">start_date=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with a Service Principal within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/service_principal_password.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Service Principal.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date">
<code class="sig-name descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date_relative">
<code class="sig-name descname">end_date_relative</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.service_principal_id">
<code class="sig-name descname">service_principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.start_date">
<code class="sig-name descname">start_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.ServicePrincipalPassword.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Service Principal.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipalPassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_date=None</em>, <em class="sig-param">end_date_relative=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">service_principal_id=None</em>, <em class="sig-param">start_date=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipalPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Service Principal.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_enabled=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">force_password_change=None</em>, <em class="sig-param">immutable_id=None</em>, <em class="sig-param">mail_nickname=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">usage_location=None</em>, <em class="sig-param">user_principal_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a User within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.ReadWrite.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `mail_nickname`- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</p></li>
<li><p><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>immutable_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p></li>
<li><p><strong>usage_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p></li>
<li><p><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azuread.User.account_enabled">
<code class="sig-name descname">account_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mail_nickname</span></code>- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to display in the address book for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.force_password_change">
<code class="sig-name descname">force_password_change</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.force_password_change" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.immutable_id">
<code class="sig-name descname">immutable_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.immutable_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.mail">
<code class="sig-name descname">mail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.onpremises_sam_account_name">
<code class="sig-name descname">onpremises_sam_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.onpremises_sam_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on premise sam account name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.onpremises_user_principal_name">
<code class="sig-name descname">onpremises_user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.onpremises_user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on premise user principal name of the Azure AD User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.usage_location">
<code class="sig-name descname">usage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.usage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.user_principal_name">
<code class="sig-name descname">user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_enabled=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">force_password_change=None</em>, <em class="sig-param">immutable_id=None</em>, <em class="sig-param">mail=None</em>, <em class="sig-param">mail_nickname=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">onpremises_sam_account_name=None</em>, <em class="sig-param">onpremises_user_principal_name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">usage_location=None</em>, <em class="sig-param">user_principal_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `mail_nickname`- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</p></li>
<li><p><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>immutable_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary email address of the Azure AD User.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD User.</p></li>
<li><p><strong>onpremises_sam_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The on premise sam account name of the Azure AD User.</p></li>
<li><p><strong>onpremises_user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The on premise user principal name of the Azure AD User.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p></li>
<li><p><strong>usage_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p></li>
<li><p><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azuread.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.get_application">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_application</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">(or</span> <span class="pre">owned</span> <span class="pre">by)</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/application.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/application.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Application within Azure Active Directory.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the Application within Azure Active Directory.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the admin consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the admin consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines if the app role is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the permission</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the user consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the user consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_client_config">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_client_config</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the configuration of the AzureRM provider.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/client_config.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/client_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_domains">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_domains</code><span class="sig-paren">(</span><em class="sig-param">include_unverified=None</em>, <em class="sig-param">only_default=None</em>, <em class="sig-param">only_initial=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Domains within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.Read.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/domains.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/domains.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>include_unverified</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if unverified Azure AD Domains should be included. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>only_default</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to only return the default domain.</p></li>
<li><p><strong>only_initial</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to only return the initial domain, which is your primary Azure Active Directory tenant domain. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_group">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The Name of the AD Group we want to lookup.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the AD Group within Azure Active Directory.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_groups">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">object_ids=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or Display Names for multiple Azure Active Directory groups.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/groups.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/groups.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>names</strong> (<em>list</em>) – The Display Names of the Azure AD Groups.</p></li>
<li><p><strong>object_ids</strong> (<em>list</em>) – The Object IDs of the Azure AD Groups.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_service_principal">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_service_principal</code><span class="sig-paren">(</span><em class="sig-param">application_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">oauth2_permissions=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an existing Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/service_principal.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/service_principal.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>application_id</strong> (<em>str</em>) – The ID of the Azure AD Application.</p></li>
<li><p><strong>display_name</strong> (<em>str</em>) – The Display Name of the Azure AD Application associated with this Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>list</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – The ID of the Azure AD Service Principal.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>oauth2_permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the admin consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the admin consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of the <code class="docutils literal notranslate"><span class="pre">app_role</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines if the app role is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the permission</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the user consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userConsentDisplayName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name of the user consent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_user">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">mail_nickname=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">user_principal_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/user.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/user.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mail_nickname</strong> (<em>str</em>) – The email alias of the Azure AD User.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the Application within Azure Active Directory.</p></li>
<li><p><strong>user_principal_name</strong> (<em>str</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_users">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param">mail_nicknames=None</em>, <em class="sig-param">object_ids=None</em>, <em class="sig-param">user_principal_names=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or UPNs for multiple Azure Active Directory users.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/users.html.markdown">https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/users.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mail_nicknames</strong> (<em>list</em>) – The email aliases of the Azure AD Users.</p></li>
<li><p><strong>object_ids</strong> (<em>list</em>) – The Object IDs of the Azure AD Users.</p></li>
<li><p><strong>user_principal_names</strong> (<em>list</em>) – The User Principal Names of the Azure AD Users.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
