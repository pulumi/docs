<div class="section" id="module-pulumi_azuread">
<span id="pulumi-azure-active-directory"></span><h1>Pulumi Azure Active Directory<a class="headerlink" href="#module-pulumi_azuread" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azuread.Application">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>available_to_other_tenants=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Application" title="Permalink to this definition">¶</a></dt>
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
<li><strong>available_to_other_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Azure AD Application available to other tenants? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>homepage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the application’s home page. If no homepage is specified this defaults to <code class="docutils literal notranslate"><span class="pre">https://{name}</span></code>.</li>
<li><strong>identifier_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user-defined URI(s) that uniquely identify a Web application within it’s Azure AD tenant, or within a verified custom domain if the application is multi-tenant.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</li>
<li><strong>oauth2_allow_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>reply_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</li>
<li><strong>required_resource_accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dt id="pulumi_azuread.Application.reply_urls">
<code class="descname">reply_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.reply_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.Application.required_resource_accesses">
<code class="descname">required_resource_accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Application.required_resource_accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of <code class="docutils literal notranslate"><span class="pre">required_resource_access</span></code> blocks as documented below.</p>
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
<dt id="pulumi_azuread.GetApplicationResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetApplicationResult</code><span class="sig-paren">(</span><em>application_id=None</em>, <em>available_to_other_tenants=None</em>, <em>homepage=None</em>, <em>identifier_uris=None</em>, <em>name=None</em>, <em>oauth2_allow_implicit_flow=None</em>, <em>object_id=None</em>, <em>reply_urls=None</em>, <em>required_resource_accesses=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetServicePrincipalResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetServicePrincipalResult</code><span class="sig-paren">(</span><em>application_id=None</em>, <em>display_name=None</em>, <em>object_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServicePrincipal.</p>
<dl class="attribute">
<dt id="pulumi_azuread.GetServicePrincipalResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.GetServicePrincipalResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azuread.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>account_enabled=None</em>, <em>display_name=None</em>, <em>mail=None</em>, <em>mail_nickname=None</em>, <em>user_principal_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.GetUserResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuread.Group">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Group" title="Permalink to this definition">¶</a></dt>
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
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the Group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azuread.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the Group.</p>
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
<dt id="pulumi_azuread.Provider">
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>client_certificate_password=None</em>, <em>client_certificate_path=None</em>, <em>client_id=None</em>, <em>client_secret=None</em>, <em>environment=None</em>, <em>msi_endpoint=None</em>, <em>subscription_id=None</em>, <em>tenant_id=None</em>, <em>use_msi=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azuread package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">ServicePrincipal</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Azure AD Application for which to create a Service Principal.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to apply to the Service Principal.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dt id="pulumi_azuread.ServicePrincipal.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.ServicePrincipal.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to apply to the Service Principal.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">ServicePrincipalPassword</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>end_date=None</em>, <em>end_date_relative=None</em>, <em>key_id=None</em>, <em>service_principal_id=None</em>, <em>start_date=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.ServicePrincipalPassword" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azuread.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_enabled=None</em>, <em>display_name=None</em>, <em>force_password_change=None</em>, <em>mail_nickname=None</em>, <em>password=None</em>, <em>user_principal_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.User" title="Permalink to this definition">¶</a></dt>
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
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 16 characters.</li>
<li><strong>user_principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User Principal Name of the Azure AD User.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dt id="pulumi_azuread.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 16 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azuread.User.user_principal_name">
<code class="descname">user_principal_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuread.User.user_principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The User Principal Name of the Azure AD User.</p>
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
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_application</code><span class="sig-paren">(</span><em>name=None</em>, <em>object_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_domains">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_domains</code><span class="sig-paren">(</span><em>include_unverified=None</em>, <em>only_default=None</em>, <em>only_initial=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Domains within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Directory.Read.All</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_group">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory group.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_service_principal">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_service_principal</code><span class="sig-paren">(</span><em>application_id=None</em>, <em>display_name=None</em>, <em>object_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an existing Service Principal associated with an Application within Azure Active Directory.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to both <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">and</span> <span class="pre">write</span> <span class="pre">all</span> <span class="pre">applications</span></code> and <code class="docutils literal notranslate"><span class="pre">Sign</span> <span class="pre">in</span> <span class="pre">and</span> <span class="pre">read</span> <span class="pre">user</span> <span class="pre">profile</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azuread.get_user">
<code class="descclassname">pulumi_azuread.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>user_principal_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuread.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets information about an Azure Active Directory user.</p>
<blockquote>
<div><strong>NOTE:</strong> If you’re authenticating using a Service Principal then it must have permissions to <code class="docutils literal notranslate"><span class="pre">Read</span> <span class="pre">directory</span> <span class="pre">data</span></code> within the <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> API.</div></blockquote>
</dd></dl>

</div>
