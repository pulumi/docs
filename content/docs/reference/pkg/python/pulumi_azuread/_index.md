---
title: Package pulumi_azuread
title_tag: Package pulumi_azuread | Python SDK
linktitle: pulumi_azuread
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuread" >}}

<div class="section" id="pulumi-azure-active-directory">
<h1>Pulumi Azure Active Directory<a class="headerlink" href="#pulumi-azure-active-directory" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuread/issues">pulumi/pulumi-azuread repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuread/issues">terraform-providers/terraform-provider-azuread repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuread"></span><dl class="py class">
<dt id="pulumi_azuread.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationAppRoleArgs, Mapping[str, Any], Awaitable[Union[ApplicationAppRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationAppRoleArgs, Mapping[str, Any], Awaitable[Union[ApplicationAppRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_to_other_tenants</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_membership_claims</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_uris</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logout_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_allow_implicit_flow</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_claims</span><span class="p">:</span> <span class="n">Union[ApplicationOptionalClaimsArgs, Mapping[str, Any], Awaitable[Union[ApplicationOptionalClaimsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prevent_duplicate_names</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_client</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reply_urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_resource_accesses</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any], Awaitable[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any], Awaitable[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">owned</span> <span class="pre">by</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">app_roles</span><span class="o">=</span><span class="p">[</span><span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationAppRoleArgs</span><span class="p">(</span>
        <span class="n">allowed_member_types</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;User&quot;</span><span class="p">,</span>
            <span class="s2">&quot;Application&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Admins can manage roles and perform all task actions&quot;</span><span class="p">,</span>
        <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Admin&quot;</span><span class="p">,</span>
        <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;Admin&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">available_to_other_tenants</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">homepage</span><span class="o">=</span><span class="s2">&quot;https://homepage&quot;</span><span class="p">,</span>
    <span class="n">identifier_uris</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://uri&quot;</span><span class="p">],</span>
    <span class="n">oauth2_allow_implicit_flow</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">oauth2_permissions</span><span class="o">=</span><span class="p">[</span>
        <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOauth2PermissionArgs</span><span class="p">(</span>
            <span class="n">admin_consent_description</span><span class="o">=</span><span class="s2">&quot;Allow the application to access example on behalf of the signed-in user.&quot;</span><span class="p">,</span>
            <span class="n">admin_consent_display_name</span><span class="o">=</span><span class="s2">&quot;Access example&quot;</span><span class="p">,</span>
            <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">,</span>
            <span class="n">user_consent_description</span><span class="o">=</span><span class="s2">&quot;Allow the application to access example on your behalf.&quot;</span><span class="p">,</span>
            <span class="n">user_consent_display_name</span><span class="o">=</span><span class="s2">&quot;Access example&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;user_impersonation&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOauth2PermissionArgs</span><span class="p">(</span>
            <span class="n">admin_consent_description</span><span class="o">=</span><span class="s2">&quot;Administer the example application&quot;</span><span class="p">,</span>
            <span class="n">admin_consent_display_name</span><span class="o">=</span><span class="s2">&quot;Administer&quot;</span><span class="p">,</span>
            <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Admin&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;administer&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">optional_claims</span><span class="o">=</span><span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOptionalClaimsArgs</span><span class="p">(</span>
        <span class="n">access_tokens</span><span class="o">=</span><span class="p">[</span>
            <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOptionalClaimsAccessTokenArgs</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;myclaim&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOptionalClaimsAccessTokenArgs</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;otherclaim&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
        <span class="n">id_tokens</span><span class="o">=</span><span class="p">[</span><span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOptionalClaimsIdTokenArgs</span><span class="p">(</span>
            <span class="n">additional_properties</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;emit_as_roles&quot;</span><span class="p">],</span>
            <span class="n">essential</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;userclaim&quot;</span><span class="p">,</span>
            <span class="n">source</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">),</span>
    <span class="n">owners</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;00000004-0000-0000-c000-000000000000&quot;</span><span class="p">],</span>
    <span class="n">reply_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://replyurl&quot;</span><span class="p">],</span>
    <span class="n">required_resource_accesses</span><span class="o">=</span><span class="p">[</span>
        <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessArgs</span><span class="p">(</span>
            <span class="n">resource_accesses</span><span class="o">=</span><span class="p">[</span>
                <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessResourceAccessArgs</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Role&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessResourceAccessArgs</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Scope&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessResourceAccessArgs</span><span class="p">(</span>
                    <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Scope&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
            <span class="n">resource_app_id</span><span class="o">=</span><span class="s2">&quot;00000003-0000-0000-c000-000000000000&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessArgs</span><span class="p">(</span>
            <span class="n">resource_accesses</span><span class="o">=</span><span class="p">[</span><span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationRequiredResourceAccessResourceAccessArgs</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Scope&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
            <span class="n">resource_app_id</span><span class="o">=</span><span class="s2">&quot;00000002-0000-0000-c000-000000000000&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webapp/api&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Azure Active Directory Applications can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/application:Application <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationAppRoleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p></li>
<li><p><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>group_membership_claims</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>, <code class="docutils literal notranslate"><span class="pre">DirectoryRole</span></code>, <code class="docutils literal notranslate"><span class="pre">ApplicationGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page.</p></li>
<li><p><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the logout page.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the optional claim.</p></li>
<li><p><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationOauth2PermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by <code class="docutils literal notranslate"><span class="pre">oauth2_permissions</span></code> blocks as documented below.</p></li>
<li><p><strong>optional_claims</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationOptionalClaimsArgs'</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">id_token</span></code> blocks as documented below which list the optional claims configured for each token type. For more information see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims">https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims</a></p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p></li>
<li><p><strong>prevent_duplicate_names</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Application is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>public_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p></li>
<li><p><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationRequiredResourceAccessArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of an application: <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code> or <code class="docutils literal notranslate"><span class="pre">native</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code>. For <code class="docutils literal notranslate"><span class="pre">native</span></code> apps type <code class="docutils literal notranslate"><span class="pre">identifier_uris</span></code> property can not not be set.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationAppRoleArgs, Mapping[str, Any], Awaitable[Union[ApplicationAppRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationAppRoleArgs, Mapping[str, Any], Awaitable[Union[ApplicationAppRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_to_other_tenants</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_membership_claims</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_uris</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logout_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_allow_implicit_flow</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ApplicationOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_claims</span><span class="p">:</span> <span class="n">Union[ApplicationOptionalClaimsArgs, Mapping[str, Any], Awaitable[Union[ApplicationOptionalClaimsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prevent_duplicate_names</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_client</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reply_urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_resource_accesses</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any], Awaitable[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any], Awaitable[Union[ApplicationRequiredResourceAccessArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.application.Application<a class="headerlink" href="#pulumi_azuread.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationAppRoleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application ID.</p></li>
<li><p><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>group_membership_claims</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>, <code class="docutils literal notranslate"><span class="pre">DirectoryRole</span></code>, <code class="docutils literal notranslate"><span class="pre">ApplicationGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page.</p></li>
<li><p><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p></li>
<li><p><strong>logout_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the logout page.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the optional claim.</p></li>
<li><p><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationOauth2PermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by <code class="docutils literal notranslate"><span class="pre">oauth2_permissions</span></code> blocks as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s Object ID.</p></li>
<li><p><strong>optional_claims</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationOptionalClaimsArgs'</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">id_token</span></code> blocks as documented below which list the optional claims configured for each token type. For more information see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims">https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims</a></p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p></li>
<li><p><strong>prevent_duplicate_names</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Application is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>public_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p></li>
<li><p><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApplicationRequiredResourceAccessArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of an application: <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code> or <code class="docutils literal notranslate"><span class="pre">native</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code>. For <code class="docutils literal notranslate"><span class="pre">native</span></code> apps type <code class="docutils literal notranslate"><span class="pre">identifier_uris</span></code> property can not not be set.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.app_roles">
<em class="property">property </em><code class="sig-name descname">app_roles</code><a class="headerlink" href="#pulumi_azuread.Application.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.application_id">
<em class="property">property </em><code class="sig-name descname">application_id</code><a class="headerlink" href="#pulumi_azuread.Application.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.available_to_other_tenants">
<em class="property">property </em><code class="sig-name descname">available_to_other_tenants</code><a class="headerlink" href="#pulumi_azuread.Application.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.Application.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.group_membership_claims">
<em class="property">property </em><code class="sig-name descname">group_membership_claims</code><a class="headerlink" href="#pulumi_azuread.Application.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">SecurityGroup</span></code>, <code class="docutils literal notranslate"><span class="pre">DirectoryRole</span></code>, <code class="docutils literal notranslate"><span class="pre">ApplicationGroup</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.homepage">
<em class="property">property </em><code class="sig-name descname">homepage</code><a class="headerlink" href="#pulumi_azuread.Application.homepage" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the application’s home page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.identifier_uris">
<em class="property">property </em><code class="sig-name descname">identifier_uris</code><a class="headerlink" href="#pulumi_azuread.Application.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.logout_url">
<em class="property">property </em><code class="sig-name descname">logout_url</code><a class="headerlink" href="#pulumi_azuread.Application.logout_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the logout page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuread.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the optional claim.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.oauth2_allow_implicit_flow">
<em class="property">property </em><code class="sig-name descname">oauth2_allow_implicit_flow</code><a class="headerlink" href="#pulumi_azuread.Application.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.oauth2_permissions">
<em class="property">property </em><code class="sig-name descname">oauth2_permissions</code><a class="headerlink" href="#pulumi_azuread.Application.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by <code class="docutils literal notranslate"><span class="pre">oauth2_permissions</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.object_id">
<em class="property">property </em><code class="sig-name descname">object_id</code><a class="headerlink" href="#pulumi_azuread.Application.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s Object ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.optional_claims">
<em class="property">property </em><code class="sig-name descname">optional_claims</code><a class="headerlink" href="#pulumi_azuread.Application.optional_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">id_token</span></code> blocks as documented below which list the optional claims configured for each token type. For more information see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims">https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.owners">
<em class="property">property </em><code class="sig-name descname">owners</code><a class="headerlink" href="#pulumi_azuread.Application.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.prevent_duplicate_names">
<em class="property">property </em><code class="sig-name descname">prevent_duplicate_names</code><a class="headerlink" href="#pulumi_azuread.Application.prevent_duplicate_names" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Application is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.public_client">
<em class="property">property </em><code class="sig-name descname">public_client</code><a class="headerlink" href="#pulumi_azuread.Application.public_client" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application a public client? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.reply_urls">
<em class="property">property </em><code class="sig-name descname">reply_urls</code><a class="headerlink" href="#pulumi_azuread.Application.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.required_resource_accesses">
<em class="property">property </em><code class="sig-name descname">required_resource_accesses</code><a class="headerlink" href="#pulumi_azuread.Application.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuread.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of an application: <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code> or <code class="docutils literal notranslate"><span class="pre">native</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">webapp/api</span></code>. For <code class="docutils literal notranslate"><span class="pre">native</span></code> apps type <code class="docutils literal notranslate"><span class="pre">identifier_uris</span></code> property can not not be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ApplicationAppRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ApplicationAppRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_member_types</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an App Role associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_application_app_role</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationAppRole</span><span class="p">(</span><span class="s2">&quot;exampleApplicationAppRole&quot;</span><span class="p">,</span>
    <span class="n">application_object_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">allowed_member_types</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;User&quot;</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Admins can manage roles and perform all task actions&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Admin&quot;</span><span class="p">,</span>
    <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;administer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>App Roles can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of an Application and the <code class="docutils literal notranslate"><span class="pre">id</span></code> of the App Role, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/applicationAppRole:ApplicationAppRole <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/role/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_member_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the admin app assignment and consent experiences.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the app role is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_member_types</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.application_app_role.ApplicationAppRole<a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationAppRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_member_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the admin app assignment and consent experiences.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the app role is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.allowed_member_types">
<em class="property">property </em><code class="sig-name descname">allowed_member_types</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.allowed_member_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether this app role definition can be assigned to users and groups by setting to <code class="docutils literal notranslate"><span class="pre">User</span></code>, or to other applications (that are accessing this application in daemon service scenarios) by setting to <code class="docutils literal notranslate"><span class="pre">Application</span></code>, or to both.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.application_object_id">
<em class="property">property </em><code class="sig-name descname">application_object_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission help text that appears in the admin app assignment and consent experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.is_enabled">
<em class="property">property </em><code class="sig-name descname">is_enabled</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the app role is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.role_id">
<em class="property">property </em><code class="sig-name descname">role_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the roles claim that the application should expect in the authentication and access tokens.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ApplicationAppRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationAppRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ApplicationCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ApplicationCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Certificate associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_application_certificate</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationCertificate</span><span class="p">(</span><span class="s2">&quot;exampleApplicationCertificate&quot;</span><span class="p">,</span>
    <span class="n">application_object_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;AsymmetricX509Cert&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;cert.pem&quot;</span><span class="p">),</span>
    <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2021-05-01T01:02:03Z&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Certificates can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of an Application and the <code class="docutils literal notranslate"><span class="pre">key</span> <span class="pre">id</span></code> of the certificate, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/applicationCertificate:ApplicationCertificate <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/certificate/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate for this Service Principal.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.application_certificate.ApplicationCertificate<a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate for this Service Principal.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.application_object_id">
<em class="property">property </em><code class="sig-name descname">application_object_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.end_date_relative">
<em class="property">property </em><code class="sig-name descname">end_date_relative</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.key_id">
<em class="property">property </em><code class="sig-name descname">key_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate for this Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ApplicationCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ApplicationOAuth2Permission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ApplicationOAuth2Permission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_consent_description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_consent_display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_consent_description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_consent_display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an OAuth2 Permission (also known as a Scope) associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_application_o_auth2_permission</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationOAuth2Permission</span><span class="p">(</span><span class="s2">&quot;exampleApplicationOAuth2Permission&quot;</span><span class="p">,</span>
    <span class="n">application_object_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">admin_consent_description</span><span class="o">=</span><span class="s2">&quot;Administer the application&quot;</span><span class="p">,</span>
    <span class="n">admin_consent_display_name</span><span class="o">=</span><span class="s2">&quot;Administer&quot;</span><span class="p">,</span>
    <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">,</span>
    <span class="n">user_consent_description</span><span class="o">=</span><span class="s2">&quot;Administer the application&quot;</span><span class="p">,</span>
    <span class="n">user_consent_display_name</span><span class="o">=</span><span class="s2">&quot;Administer&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;administer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>OAuth2 Permissions can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of an Application and the <code class="docutils literal notranslate"><span class="pre">id</span></code> of the Permission, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/applicationOAuth2Permission:ApplicationOAuth2Permission <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/scope/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_consent_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>admin_consent_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this Permission should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the Permission is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>permission_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom UUID for the Permission. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this scope permission can be consented to by an end user, or whether it is a tenant-wide permission that must be consented to by an Administrator. Possible values are “User” or “Admin”.</p></li>
<li><p><strong>user_consent_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the end user consent experience.</p></li>
<li><p><strong>user_consent_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the end user consent experience.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_consent_description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_consent_display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_consent_description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_consent_display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.application_o_auth2_permission.ApplicationOAuth2Permission<a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationOAuth2Permission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_consent_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>admin_consent_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the admin consent and app assignment experiences.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this Permission should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the Permission is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>permission_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom UUID for the Permission. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this scope permission can be consented to by an end user, or whether it is a tenant-wide permission that must be consented to by an Administrator. Possible values are “User” or “Admin”.</p></li>
<li><p><strong>user_consent_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission help text that appears in the end user consent experience.</p></li>
<li><p><strong>user_consent_display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name for the permission that appears in the end user consent experience.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.admin_consent_description">
<em class="property">property </em><code class="sig-name descname">admin_consent_description</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.admin_consent_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission help text that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.admin_consent_display_name">
<em class="property">property </em><code class="sig-name descname">admin_consent_display_name</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.admin_consent_display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.application_object_id">
<em class="property">property </em><code class="sig-name descname">application_object_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this Permission should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.is_enabled">
<em class="property">property </em><code class="sig-name descname">is_enabled</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the Permission is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.permission_id">
<em class="property">property </em><code class="sig-name descname">permission_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.permission_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a custom UUID for the Permission. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether this scope permission can be consented to by an end user, or whether it is a tenant-wide permission that must be consented to by an Administrator. Possible values are “User” or “Admin”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.user_consent_description">
<em class="property">property </em><code class="sig-name descname">user_consent_description</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.user_consent_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission help text that appears in the end user consent experience.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.user_consent_display_name">
<em class="property">property </em><code class="sig-name descname">user_consent_display_name</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.user_consent_display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the end user consent experience.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ApplicationOAuth2Permission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationOAuth2Permission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ApplicationPassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ApplicationPassword</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with an Application within Azure Active Directory. Also can be referred to as Client secrets.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_application_password</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ApplicationPassword</span><span class="p">(</span><span class="s2">&quot;exampleApplicationPassword&quot;</span><span class="p">,</span>
    <span class="n">application_object_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My managed password&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#&quot;</span><span class="p">,</span>
    <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2099-01-01T01:02:03Z&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Passwords can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of an Application and the <code class="docutils literal notranslate"><span class="pre">key</span> <span class="pre">id</span></code> of the password, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/applicationPassword:ApplicationPassword <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/password/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Password.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Application.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.application_password.ApplicationPassword<a class="headerlink" href="#pulumi_azuread.ApplicationPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Password.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Application.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.application_object_id">
<em class="property">property </em><code class="sig-name descname">application_object_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Password.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.end_date_relative">
<em class="property">property </em><code class="sig-name descname">end_date_relative</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.key_id">
<em class="property">property </em><code class="sig-name descname">key_id</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ApplicationPassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ApplicationPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_to_other_tenants</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_membership_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logout_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_allow_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reply_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_resource_accesses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_unverified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_initial</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetServicePrincipalResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetServicePrincipalResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">department</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">immutable_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nickname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_sam_account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_user_principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_delivery_office_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">surname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_missing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nicknames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_to_other_tenants</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_membership_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logout_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_allow_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reply_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_resource_accesses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.app_roles">
<em class="property">property </em><code class="sig-name descname">app_roles</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.app_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">app_role</span></code> blocks as documented below. For more information <a class="reference external" href="https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles">https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.application_id">
<em class="property">property </em><code class="sig-name descname">application_id</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Application ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.available_to_other_tenants">
<em class="property">property </em><code class="sig-name descname">available_to_other_tenants</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.available_to_other_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Azure AD Application available to other tenants?</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.group_membership_claims">
<em class="property">property </em><code class="sig-name descname">group_membership_claims</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.group_membership_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">groups</span></code> claim issued in a user or OAuth 2.0 access token that the app expects.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.identifier_uris">
<em class="property">property </em><code class="sig-name descname">identifier_uris</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.identifier_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.logout_url">
<em class="property">property </em><code class="sig-name descname">logout_url</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.logout_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the logout page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the optional claim.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow">
<em class="property">property </em><code class="sig-name descname">oauth2_allow_implicit_flow</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_allow_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Azure AD Application allow OAuth2.0 implicit flow tokens?</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.oauth2_permissions">
<em class="property">property </em><code class="sig-name descname">oauth2_permissions</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.object_id">
<em class="property">property </em><code class="sig-name descname">object_id</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the Object ID of the Azure Active Directory Application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.optional_claims">
<em class="property">property </em><code class="sig-name descname">optional_claims</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.optional_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">id_token</span></code> blocks as documented below which list the optional claims configured for each token type. For more information see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims">https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.owners">
<em class="property">property </em><code class="sig-name descname">owners</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of User Object IDs that are assigned ownership of the application registration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.reply_urls">
<em class="property">property </em><code class="sig-name descname">reply_urls</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.required_resource_accesses">
<em class="property">property </em><code class="sig-name descname">required_resource_accesses</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetApplicationResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuread.GetApplicationResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the permission</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetClientConfigResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_unverified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_initial</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomains.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetDomainsResult.domains">
<em class="property">property </em><code class="sig-name descname">domains</code><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">domain</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetDomainsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetDomainsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetGroupResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuread.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the AD Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupResult.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.GetGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure AD Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupResult.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_azuread.GetGroupResult.members" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Group members.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupResult.owners">
<em class="property">property </em><code class="sig-name descname">owners</code><a class="headerlink" href="#pulumi_azuread.GetGroupResult.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Group owners.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetGroupsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupsResult.names">
<em class="property">property </em><code class="sig-name descname">names</code><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Names of the Azure AD Groups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetGroupsResult.object_ids">
<em class="property">property </em><code class="sig-name descname">object_ids</code><a class="headerlink" href="#pulumi_azuread.GetGroupsResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Groups.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetServicePrincipalResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetServicePrincipalResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">app_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServicePrincipal.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetServicePrincipalResult.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name for the permission that appears in the admin consent and app assignment experiences.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetServicePrincipalResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">department</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">immutable_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nickname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_sam_account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_user_principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_delivery_office_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">surname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.account_enabled">
<em class="property">property </em><code class="sig-name descname">account_enabled</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">True</span></code> if the account is enabled; otherwise <code class="docutils literal notranslate"><span class="pre">False</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.city">
<em class="property">property </em><code class="sig-name descname">city</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.city" title="Permalink to this definition">¶</a></dt>
<dd><p>The city in which the user is located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.company_name">
<em class="property">property </em><code class="sig-name descname">company_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.company_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The company name which the user is associated. This property can be useful for describing the company that an external user comes from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.country">
<em class="property">property </em><code class="sig-name descname">country</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country/region in which the user is located; for example, “US” or “UK”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.department">
<em class="property">property </em><code class="sig-name descname">department</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.department" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the department in which the user works.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.given_name">
<em class="property">property </em><code class="sig-name descname">given_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.given_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The given name (first name) of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.immutable_id">
<em class="property">property </em><code class="sig-name descname">immutable_id</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.immutable_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The value used to associate an on-premise Active Directory user account with their Azure AD user object.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.job_title">
<em class="property">property </em><code class="sig-name descname">job_title</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.job_title" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s job title.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.mail">
<em class="property">property </em><code class="sig-name descname">mail</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.mail_nickname">
<em class="property">property </em><code class="sig-name descname">mail_nickname</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.mail_nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>The email alias of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.mobile">
<em class="property">property </em><code class="sig-name descname">mobile</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.mobile" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary cellular telephone number for the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.onpremises_sam_account_name">
<em class="property">property </em><code class="sig-name descname">onpremises_sam_account_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.onpremises_sam_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on-premise SAM account name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.onpremises_user_principal_name">
<em class="property">property </em><code class="sig-name descname">onpremises_user_principal_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.onpremises_user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on-premise user principal name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.physical_delivery_office_name">
<em class="property">property </em><code class="sig-name descname">physical_delivery_office_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.physical_delivery_office_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The office location in the user’s place of business.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.postal_code">
<em class="property">property </em><code class="sig-name descname">postal_code</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.postal_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code for the user’s postal address. The postal code is specific to the user’s country/region. In the United States of America, this attribute contains the ZIP code.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state or province in the user’s address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.street_address">
<em class="property">property </em><code class="sig-name descname">street_address</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address of the user’s place of business.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.surname">
<em class="property">property </em><code class="sig-name descname">surname</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.surname" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s surname (family name or last name).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.usage_location">
<em class="property">property </em><code class="sig-name descname">usage_location</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.usage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The usage location of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUserResult.user_principal_name">
<em class="property">property </em><code class="sig-name descname">user_principal_name</code><a class="headerlink" href="#pulumi_azuread.GetUserResult.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_missing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nicknames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="py method">
<dt id="pulumi_azuread.GetUsersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuread.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUsersResult.mail_nicknames">
<em class="property">property </em><code class="sig-name descname">mail_nicknames</code><a class="headerlink" href="#pulumi_azuread.GetUsersResult.mail_nicknames" title="Permalink to this definition">¶</a></dt>
<dd><p>The email aliases of the Azure AD Users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUsersResult.object_ids">
<em class="property">property </em><code class="sig-name descname">object_ids</code><a class="headerlink" href="#pulumi_azuread.GetUsersResult.object_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object IDs of the Azure AD Users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUsersResult.user_principal_names">
<em class="property">property </em><code class="sig-name descname">user_principal_names</code><a class="headerlink" href="#pulumi_azuread.GetUsersResult.user_principal_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Names of the Azure AD Users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GetUsersResult.users">
<em class="property">property </em><code class="sig-name descname">users</code><a class="headerlink" href="#pulumi_azuread.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of Azure AD Users. Each <code class="docutils literal notranslate"><span class="pre">user</span></code> object consists of the fields documented below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuread.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prevent_duplicate_names</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Group within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">groups</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. In addition it must also have either the <code class="docutils literal notranslate"><span class="pre">Company</span> <span class="pre">Administrator</span></code> or <code class="docutils literal notranslate"><span class="pre">User</span> <span class="pre">Account</span> <span class="pre">Administrator</span></code> Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the <strong>AzureAD PowerShell Module</strong>, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to <a class="reference external" href="https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember">this documentation</a> for more details.</p>
</div></blockquote>
<p><em>Basic example</em></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;A-AD-Group&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p><em>A group with members</em></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;J Doe&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;notSecure123&quot;</span><span class="p">,</span>
    <span class="n">user_principal_name</span><span class="o">=</span><span class="s2">&quot;jdoe@hashicorp.com&quot;</span><span class="p">)</span>
<span class="n">example_group</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;exampleGroup&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;MyGroup&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="n">example_user</span><span class="o">.</span><span class="n">object_id</span><span class="p">])</span>
</pre></div>
</div>
<p>Azure Active Directory Groups can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/group:Group my_group <span class="m">00000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Group.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of owners who own this Group. Supported Object types are Users or Service Principals.</p></li>
<li><p><strong>prevent_duplicate_names</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Group is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prevent_duplicate_names</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.group.Group<a class="headerlink" href="#pulumi_azuread.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the Group.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p></li>
<li><p><strong>owners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of owners who own this Group. Supported Object types are Users or Service Principals.</p></li>
<li><p><strong>prevent_duplicate_names</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Group is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuread.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the Group.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_azuread.Group.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.owners">
<em class="property">property </em><code class="sig-name descname">owners</code><a class="headerlink" href="#pulumi_azuread.Group.owners" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of owners who own this Group. Supported Object types are Users or Service Principals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.prevent_duplicate_names">
<em class="property">property </em><code class="sig-name descname">prevent_duplicate_names</code><a class="headerlink" href="#pulumi_azuread.Group.prevent_duplicate_names" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, will return an error when an existing Group is found with the same name. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.GroupMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">GroupMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single Group Membership within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Do not use this resource at the same time as <code class="docutils literal notranslate"><span class="pre">azuread_group.members</span></code>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">user_principal_name</span><span class="o">=</span><span class="s2">&quot;jdoe@hashicorp.com&quot;</span><span class="p">)</span>
<span class="n">example_group</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;exampleGroup&quot;</span><span class="p">)</span>
<span class="n">example_group_member</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">GroupMember</span><span class="p">(</span><span class="s2">&quot;exampleGroupMember&quot;</span><span class="p">,</span>
    <span class="n">group_object_id</span><span class="o">=</span><span class="n">example_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">member_object_id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Azure Active Directory Group Members can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/groupMember:GroupMember <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/member/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_azuread.GroupMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.group_member.GroupMember<a class="headerlink" href="#pulumi_azuread.GroupMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>member_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GroupMember.group_object_id">
<em class="property">property </em><code class="sig-name descname">group_object_id</code><a class="headerlink" href="#pulumi_azuread.GroupMember.group_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GroupMember.member_object_id">
<em class="property">property </em><code class="sig-name descname">member_object_id</code><a class="headerlink" href="#pulumi_azuread.GroupMember.member_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.GroupMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.GroupMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GroupMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_terraform_partner_id</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">msi_endpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partner_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_msi</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azuread package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_certificate_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
Principal using a Client Certificate.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID which should be used for service principal authentication.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to decrypt the Client Certificate. For use when authenticating as a Service Principal using a Client
Certificate</p></li>
<li><p><strong>disable_terraform_partner_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disable the Terraform Partner ID which is used if a custom <code class="docutils literal notranslate"><span class="pre">partner_id</span></code> isn’t specified.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud Environment which should be used. Possible values are <code class="docutils literal notranslate"><span class="pre">public</span></code>, <code class="docutils literal notranslate"><span class="pre">usgovernment</span></code>, <code class="docutils literal notranslate"><span class="pre">german</span></code>, and <code class="docutils literal notranslate"><span class="pre">china</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p></li>
<li><p><strong>metadata_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Hostname which should be used for the Azure Metadata Service.</p></li>
<li><p><strong>msi_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected
automatically.</p></li>
<li><p><strong>partner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Tenant ID which should be used. Works with all authentication methods except MSI.</p></li>
<li><p><strong>use_msi</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow Managed Service Identity to be used for Authentication.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ServicePrincipal">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ServicePrincipal</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_role_assignment_required</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API. Please see The Granting a Service Principal permission to manage AAD for the required steps.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">,</span>
    <span class="n">homepage</span><span class="o">=</span><span class="s2">&quot;http://homepage&quot;</span><span class="p">,</span>
    <span class="n">identifier_uris</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://uri&quot;</span><span class="p">],</span>
    <span class="n">reply_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://replyurl&quot;</span><span class="p">],</span>
    <span class="n">available_to_other_tenants</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">oauth2_allow_implicit_flow</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">example_service_principal</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ServicePrincipal</span><span class="p">(</span><span class="s2">&quot;exampleServicePrincipal&quot;</span><span class="p">,</span>
    <span class="n">application_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">,</span>
    <span class="n">app_role_assignment_required</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;example&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tags&quot;</span><span class="p">,</span>
        <span class="s2">&quot;here&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Azure Active Directory Service Principals can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/servicePrincipal:ServicePrincipal <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_role_assignment_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePrincipalOauth2PermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to apply to the Service Principal.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_role_assignment_required</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServicePrincipalAppRoleArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalAppRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServicePrincipalAppRoleArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalAppRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any], Awaitable[Union[ServicePrincipalOauth2PermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.service_principal.ServicePrincipal<a class="headerlink" href="#pulumi_azuread.ServicePrincipal.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipal resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_role_assignment_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name of the Azure Active Directory Application associated with this Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePrincipalOauth2PermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Principal’s Object ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to apply to the Service Principal.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.app_role_assignment_required">
<em class="property">property </em><code class="sig-name descname">app_role_assignment_required</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.app_role_assignment_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.application_id">
<em class="property">property </em><code class="sig-name descname">application_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Azure AD Application for which to create a Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name of the Azure Active Directory Application associated with this Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.oauth2_permissions">
<em class="property">property </em><code class="sig-name descname">oauth2_permissions</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.oauth2_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.object_id">
<em class="property">property </em><code class="sig-name descname">object_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Principal’s Object ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to apply to the Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipal.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ServicePrincipalCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ServicePrincipalCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Certificate associated with a Service Principal within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_service_principal</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ServicePrincipal</span><span class="p">(</span><span class="s2">&quot;exampleServicePrincipal&quot;</span><span class="p">,</span> <span class="n">application_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">)</span>
<span class="n">example_service_principal_certificate</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ServicePrincipalCertificate</span><span class="p">(</span><span class="s2">&quot;exampleServicePrincipalCertificate&quot;</span><span class="p">,</span>
    <span class="n">service_principal_id</span><span class="o">=</span><span class="n">example_service_principal</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;AsymmetricX509Cert&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;cert.pem&quot;</span><span class="p">),</span>
    <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2021-05-01T01:02:03Z&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Certificates can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of the Service Principal and the <code class="docutils literal notranslate"><span class="pre">key</span> <span class="pre">id</span></code> of the certificate, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/servicePrincipalCertificate:ServicePrincipalCertificate <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/certificate/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate for this Service Principal.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.service_principal_certificate.ServicePrincipalCertificate<a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipalCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate for this Service Principal.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.end_date_relative">
<em class="property">property </em><code class="sig-name descname">end_date_relative</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Certificate is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.key_id">
<em class="property">property </em><code class="sig-name descname">key_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.service_principal_id">
<em class="property">property </em><code class="sig-name descname">service_principal_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of key/certificate. Must be one of <code class="docutils literal notranslate"><span class="pre">AsymmetricX509Cert</span></code> or <code class="docutils literal notranslate"><span class="pre">Symmetric</span></code>. Changing this fields forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate for this Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.ServicePrincipalPassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">ServicePrincipalPassword</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Password associated with a Service Principal within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_application</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;exampleApplication&quot;</span><span class="p">)</span>
<span class="n">example_service_principal</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ServicePrincipal</span><span class="p">(</span><span class="s2">&quot;exampleServicePrincipal&quot;</span><span class="p">,</span> <span class="n">application_id</span><span class="o">=</span><span class="n">example_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">)</span>
<span class="n">example_service_principal_password</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">ServicePrincipalPassword</span><span class="p">(</span><span class="s2">&quot;exampleServicePrincipalPassword&quot;</span><span class="p">,</span>
    <span class="n">service_principal_id</span><span class="o">=</span><span class="n">example_service_principal</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My managed password&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#&quot;</span><span class="p">,</span>
    <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2099-01-01T01:02:03Z&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Passwords can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code> of a Service Principal and the <code class="docutils literal notranslate"><span class="pre">key</span> <span class="pre">id</span></code> of the password, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/servicePrincipalPassword:ServicePrincipalPassword <span class="nb">test</span> <span class="m">00000000</span>-0000-0000-0000-000000000000/11111111-1111-1111-1111-111111111111
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Password.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p></li>
<li><p><strong>end_date_relative</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>service_principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password for this Service Principal.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date_relative</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_principal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.service_principal_password.ServicePrincipalPassword<a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePrincipalPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Password.</p></li>
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

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Password.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.end_date_relative">
<em class="property">property </em><code class="sig-name descname">end_date_relative</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.end_date_relative" title="Permalink to this definition">¶</a></dt>
<dd><p>A relative duration for which the Password is valid until, for example <code class="docutils literal notranslate"><span class="pre">240h</span></code> (10 days) or <code class="docutils literal notranslate"><span class="pre">2400h30m</span></code>. Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.key_id">
<em class="property">property </em><code class="sig-name descname">key_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.service_principal_id">
<em class="property">property </em><code class="sig-name descname">service_principal_id</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.service_principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. <code class="docutils literal notranslate"><span class="pre">2018-01-01T01:02:03Z</span></code>). If this isn’t specified, the current date is used.  Changing this field forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password for this Service Principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.ServicePrincipalPassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azuread.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">department</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_password_change</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">immutable_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nickname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_delivery_office_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">surname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage_location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a User within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.ReadWrite.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;J. Doe&quot;</span><span class="p">,</span>
    <span class="n">mail_nickname</span><span class="o">=</span><span class="s2">&quot;jdoe&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;SecretP@sswd99!&quot;</span><span class="p">,</span>
    <span class="n">user_principal_name</span><span class="o">=</span><span class="s2">&quot;jdoe@hashicorp.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Azure Active Directory Users can be imported using the <code class="docutils literal notranslate"><span class="pre">object</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuread:index/user:User my_user <span class="m">00000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>city</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The city in which the user is located.</p></li>
<li><p><strong>company_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The company name which the user is associated. This property can be useful for describing the company that an external user comes from.</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country/region in which the user is located; for example, “US” or “UK”.</p></li>
<li><p><strong>department</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the department in which the user works.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</p></li>
<li><p><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>given_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The given name (first name) of the user.</p></li>
<li><p><strong>immutable_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p></li>
<li><p><strong>job_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s job title.</p></li>
<li><p><strong>mail_nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail alias for the user. Defaults to the user name part of the User Principal Name.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary cellular telephone number for the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p></li>
<li><p><strong>physical_delivery_office_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The office location in the user’s place of business.</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code for the user’s postal address. The postal code is specific to the user’s country/region. In the United States of America, this attribute contains the ZIP code.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state or province in the user’s address.</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address of the user’s place of business.</p></li>
<li><p><strong>surname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s surname (family name or last name).</p></li>
<li><p><strong>usage_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p></li>
<li><p><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuread.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">department</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_password_change</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">immutable_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nickname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_sam_account_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">onpremises_user_principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">physical_delivery_office_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">surname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage_location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.user.User<a class="headerlink" href="#pulumi_azuread.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>city</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The city in which the user is located.</p></li>
<li><p><strong>company_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The company name which the user is associated. This property can be useful for describing the company that an external user comes from.</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country/region in which the user is located; for example, “US” or “UK”.</p></li>
<li><p><strong>department</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the department in which the user works.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display in the address book for the user.</p></li>
<li><p><strong>force_password_change</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>given_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The given name (first name) of the user.</p></li>
<li><p><strong>immutable_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p></li>
<li><p><strong>job_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s job title.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary email address of the Azure AD User.</p></li>
<li><p><strong>mail_nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail alias for the user. Defaults to the user name part of the User Principal Name.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary cellular telephone number for the user.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Object ID of the Azure AD User.</p></li>
<li><p><strong>onpremises_sam_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The on-premise SAM account name of the Azure AD User.</p></li>
<li><p><strong>onpremises_user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The on-premise user principal name of the Azure AD User.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p></li>
<li><p><strong>physical_delivery_office_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The office location in the user’s place of business.</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code for the user’s postal address. The postal code is specific to the user’s country/region. In the United States of America, this attribute contains the ZIP code.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state or province in the user’s address.</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address of the user’s place of business.</p></li>
<li><p><strong>surname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s surname (family name or last name).</p></li>
<li><p><strong>usage_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p></li>
<li><p><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.account_enabled">
<em class="property">property </em><code class="sig-name descname">account_enabled</code><a class="headerlink" href="#pulumi_azuread.User.account_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the account should be enabled, otherwise <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.city">
<em class="property">property </em><code class="sig-name descname">city</code><a class="headerlink" href="#pulumi_azuread.User.city" title="Permalink to this definition">¶</a></dt>
<dd><p>The city in which the user is located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.company_name">
<em class="property">property </em><code class="sig-name descname">company_name</code><a class="headerlink" href="#pulumi_azuread.User.company_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The company name which the user is associated. This property can be useful for describing the company that an external user comes from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.country">
<em class="property">property </em><code class="sig-name descname">country</code><a class="headerlink" href="#pulumi_azuread.User.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country/region in which the user is located; for example, “US” or “UK”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.department">
<em class="property">property </em><code class="sig-name descname">department</code><a class="headerlink" href="#pulumi_azuread.User.department" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the department in which the user works.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuread.User.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to display in the address book for the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.force_password_change">
<em class="property">property </em><code class="sig-name descname">force_password_change</code><a class="headerlink" href="#pulumi_azuread.User.force_password_change" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the User is forced to change the password during the next sign-in. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.given_name">
<em class="property">property </em><code class="sig-name descname">given_name</code><a class="headerlink" href="#pulumi_azuread.User.given_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The given name (first name) of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.immutable_id">
<em class="property">property </em><code class="sig-name descname">immutable_id</code><a class="headerlink" href="#pulumi_azuread.User.immutable_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user’s userPrincipalName (UPN) property when creating a new user account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.job_title">
<em class="property">property </em><code class="sig-name descname">job_title</code><a class="headerlink" href="#pulumi_azuread.User.job_title" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s job title.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.mail">
<em class="property">property </em><code class="sig-name descname">mail</code><a class="headerlink" href="#pulumi_azuread.User.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary email address of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.mail_nickname">
<em class="property">property </em><code class="sig-name descname">mail_nickname</code><a class="headerlink" href="#pulumi_azuread.User.mail_nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>The mail alias for the user. Defaults to the user name part of the User Principal Name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.mobile">
<em class="property">property </em><code class="sig-name descname">mobile</code><a class="headerlink" href="#pulumi_azuread.User.mobile" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary cellular telephone number for the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.object_id">
<em class="property">property </em><code class="sig-name descname">object_id</code><a class="headerlink" href="#pulumi_azuread.User.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Object ID of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.onpremises_sam_account_name">
<em class="property">property </em><code class="sig-name descname">onpremises_sam_account_name</code><a class="headerlink" href="#pulumi_azuread.User.onpremises_sam_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on-premise SAM account name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.onpremises_user_principal_name">
<em class="property">property </em><code class="sig-name descname">onpremises_user_principal_name</code><a class="headerlink" href="#pulumi_azuread.User.onpremises_user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The on-premise user principal name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_azuread.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.physical_delivery_office_name">
<em class="property">property </em><code class="sig-name descname">physical_delivery_office_name</code><a class="headerlink" href="#pulumi_azuread.User.physical_delivery_office_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The office location in the user’s place of business.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.postal_code">
<em class="property">property </em><code class="sig-name descname">postal_code</code><a class="headerlink" href="#pulumi_azuread.User.postal_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code for the user’s postal address. The postal code is specific to the user’s country/region. In the United States of America, this attribute contains the ZIP code.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_azuread.User.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state or province in the user’s address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.street_address">
<em class="property">property </em><code class="sig-name descname">street_address</code><a class="headerlink" href="#pulumi_azuread.User.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address of the user’s place of business.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.surname">
<em class="property">property </em><code class="sig-name descname">surname</code><a class="headerlink" href="#pulumi_azuread.User.surname" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s surname (family name or last name).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.usage_location">
<em class="property">property </em><code class="sig-name descname">usage_location</code><a class="headerlink" href="#pulumi_azuread.User.usage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: <code class="docutils literal notranslate"><span class="pre">NO</span></code>, <code class="docutils literal notranslate"><span class="pre">JP</span></code>, and <code class="docutils literal notranslate"><span class="pre">GB</span></code>. Cannot be reset to null once set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.user_principal_name">
<em class="property">property </em><code class="sig-name descname">user_principal_name</code><a class="headerlink" href="#pulumi_azuread.User.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuread.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_azuread.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_azuread.get_application">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetApplicationOauth2PermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_claims</span><span class="p">:</span> <span class="n">Union[GetApplicationOptionalClaimsArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_application.AwaitableGetApplicationResult<a class="headerlink" href="#pulumi_azuread.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">(or</span> <span class="pre">owned</span> <span class="pre">by)</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_application</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My First AzureAD Application&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;azureAdObjectId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>application_id</strong> (<em>str</em>) – Specifies the Application ID of the Azure Active Directory Application.</p></li>
<li><p><strong>display_name</strong> (<em>str</em>) – Specifies the display name of the Application within Azure Active Directory.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the optional claim.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetApplicationOauth2PermissionArgs'</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the Application within Azure Active Directory.</p></li>
<li><p><strong>optional_claims</strong> (<em>pulumi.InputType</em><em>[</em><em>'GetApplicationOptionalClaimsArgs'</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">id_token</span></code> blocks as documented below which list the optional claims configured for each token type. For more information see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims">https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims</a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_client_config">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_client_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_client_config.AwaitableGetClientConfigResult<a class="headerlink" href="#pulumi_azuread.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the configuration of the AzureAD provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;accountId&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">client_id</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_domains">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_domains</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">include_unverified</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_initial</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_domains.AwaitableGetDomainsResult<a class="headerlink" href="#pulumi_azuread.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about existing Domains within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.Read.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">aad_domains</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_domains</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;domains&quot;</span><span class="p">,</span> <span class="n">aad_domains</span><span class="o">.</span><span class="n">domains</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>include_unverified</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if unverified Azure AD domains should be included. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>only_default</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to only return the default domain.</p></li>
<li><p><strong>only_initial</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to only return the initial domain, which is your primary Azure Active Directory tenant domain. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_group">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_azuread.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;A-AD-Group&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>str</em>) – The splay name of the Group within Azure Active Directory.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the Group within Azure Active Directory.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_groups">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_names</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_groups.AwaitableGetGroupsResult<a class="headerlink" href="#pulumi_azuread.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or Display Names for multiple Azure Active Directory groups.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">groups</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_groups</span><span class="p">(</span><span class="n">names</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;group-a&quot;</span><span class="p">,</span>
    <span class="s2">&quot;group-b&quot;</span><span class="p">,</span>
<span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>names</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – The Display Names of the Azure AD Groups.</p></li>
<li><p><strong>object_ids</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – The Object IDs of the Azure AD Groups.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_service_principal">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_service_principal</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oauth2_permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetServicePrincipalOauth2PermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_service_principal.AwaitableGetServicePrincipalResult<a class="headerlink" href="#pulumi_azuread.get_service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an existing Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_service_principal</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;my-awesome-application&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_service_principal</span><span class="p">(</span><span class="n">application_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_service_principal</span><span class="p">(</span><span class="n">object_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>application_id</strong> (<em>str</em>) – The ID of the Azure AD Application.</p></li>
<li><p><strong>display_name</strong> (<em>str</em>) – The Display Name of the Azure AD Application associated with this Service Principal.</p></li>
<li><p><strong>oauth2_permissions</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetServicePrincipalOauth2PermissionArgs'</em><em>]</em><em>]</em>) – A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a <code class="docutils literal notranslate"><span class="pre">oauth2_permission</span></code> block as documented below.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – The ID of the Azure AD Service Principal.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_user">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">mail_nickname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_azuread.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">user_principal_name</span><span class="o">=</span><span class="s2">&quot;user@hashicorp.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mail_nickname</strong> (<em>str</em>) – The email alias of the Azure AD User.</p></li>
<li><p><strong>object_id</strong> (<em>str</em>) – Specifies the Object ID of the User within Azure Active Directory.</p></li>
<li><p><strong>user_principal_name</strong> (<em>str</em>) – The User Principal Name of the Azure AD User.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuread.get_users">
<code class="sig-prename descclassname">pulumi_azuread.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ignore_missing</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail_nicknames</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_principal_names</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuread.get_users.AwaitableGetUsersResult<a class="headerlink" href="#pulumi_azuread.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets Object IDs or UPNs for multiple Azure Active Directory users.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">users</span> <span class="o">=</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">user_principal_names</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;kat@hashicorp.com&quot;</span><span class="p">,</span>
    <span class="s2">&quot;byte@hashicorp.com&quot;</span><span class="p">,</span>
<span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ignore_missing</strong> (<em>bool</em>) – Ignore missing users and return users that were found. The data source will still fail if no users are found. Defaults to false.</p></li>
<li><p><strong>mail_nicknames</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – The email aliases of the Azure AD Users.</p></li>
<li><p><strong>object_ids</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – The Object IDs of the Azure AD Users.</p></li>
<li><p><strong>user_principal_names</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – The User Principal Names of the Azure AD Users.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
