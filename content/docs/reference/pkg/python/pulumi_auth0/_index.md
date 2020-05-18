---
title: Package pulumi_auth0
title_tag: Package pulumi_auth0 | Python SDK
linktitle: pulumi_auth0
notitle: true
---

<div class="section" id="pulumi-auth0">
<h1>Pulumi Auth0<a class="headerlink" href="#pulumi-auth0" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-auth0">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-auth0/issues">pulumi/pulumi-auth0 repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-auth0/issues">terraform-providers/terraform-provider-auth0 repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_auth0"></span><dl class="py class">
<dt id="pulumi_auth0.Client">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Client</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can set up applications that use Auth0 for authentication and configure allowed callback URLs and secrets for these applications. Depending on your plan, you may also configure add-ons to allow your application to call another application’s API (such as Firebase and AWS) on behalf of an authenticated user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_client</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;myClient&quot;</span><span class="p">,</span>
    <span class="n">addons</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;firebase&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;client_email&quot;</span><span class="p">:</span> <span class="s2">&quot;john.doe@example.com&quot;</span><span class="p">,</span>
            <span class="s2">&quot;lifetime_in_seconds&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;private_key&quot;</span><span class="p">:</span> <span class="s2">&quot;wer&quot;</span><span class="p">,</span>
            <span class="s2">&quot;private_key_id&quot;</span><span class="p">:</span> <span class="s2">&quot;qwreerwerwe&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;samlp&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;audience&quot;</span><span class="p">:</span> <span class="s2">&quot;https://example.com/saml&quot;</span><span class="p">,</span>
            <span class="s2">&quot;createUpnClaim&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
            <span class="s2">&quot;mapIdentities&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
            <span class="s2">&quot;mapUnknownClaimsAsIs&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
            <span class="s2">&quot;mappings&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress&quot;</span><span class="p">,</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">&quot;nameIdentifierFormat&quot;</span><span class="p">:</span> <span class="s2">&quot;urn:oasis:names:tc:SAML:2.0:nameid-format:persistent&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nameIdentifierProbes&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress&quot;</span><span class="p">],</span>
            <span class="s2">&quot;passthroughClaimsWithNoMapping&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">allowed_logout_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">],</span>
    <span class="n">allowed_origins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">],</span>
    <span class="n">app_type</span><span class="o">=</span><span class="s2">&quot;non_interactive&quot;</span><span class="p">,</span>
    <span class="n">callbacks</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com/callback&quot;</span><span class="p">],</span>
    <span class="n">client_metadata</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;zoo&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">custom_login_page_on</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Applications Long Description&quot;</span><span class="p">,</span>
    <span class="n">grant_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;authorization_code&quot;</span><span class="p">,</span>
        <span class="s2">&quot;http://auth0.com/oauth/grant-type/password-realm&quot;</span><span class="p">,</span>
        <span class="s2">&quot;implicit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;password&quot;</span><span class="p">,</span>
        <span class="s2">&quot;refresh_token&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">is_first_party</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">jwt_configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;alg&quot;</span><span class="p">:</span> <span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
        <span class="s2">&quot;lifetimeInSeconds&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
        <span class="s2">&quot;scopes&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;secretEncoded&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">mobile</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ios&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;appBundleIdentifier&quot;</span><span class="p">:</span> <span class="s2">&quot;com.my.bundle.id&quot;</span><span class="p">,</span>
            <span class="s2">&quot;teamId&quot;</span><span class="p">:</span> <span class="s2">&quot;9JA89QQLNQ&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">oidc_conformant</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="s2">&quot;client_secret_post&quot;</span><span class="p">,</span>
    <span class="n">web_origins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>allowed_origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p></li>
<li><p><strong>app_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p></li>
<li><p><strong>callbacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>client_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String)</p></li>
<li><p><strong>client_secret_rotation_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map.</p></li>
<li><p><strong>cross_origin_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p></li>
<li><p><strong>cross_origin_loc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p></li>
<li><p><strong>custom_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Content of the custom login page.</p></li>
<li><p><strong>custom_login_page_on</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not a custom login page is to be used.</p></li>
<li><p><strong>custom_login_page_preview</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, (Max length = 140 characters). Description of the purpose of the client.</p></li>
<li><p><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String).</p></li>
<li><p><strong>form_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Form template for WS-Federation protocol.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Types of grants that this client is authorized to use.</p></li>
<li><p><strong>is_first_party</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client is a first-party client.</p></li>
<li><p><strong>is_token_endpoint_ip_header_trusted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the token endpoint IP header is trusted.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the client.</p></li>
<li><p><strong>oidc_conformant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p></li>
<li><p><strong>sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p></li>
<li><p><strong>sso_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not SSO is disabled.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p></li>
<li><p><strong>web_origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that represent valid web origins for use with web message response mode.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aws</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureSb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">box</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudbees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">concur</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropbox</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">echosign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">egnyte</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firebase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">layer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mscrm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">newrelic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">office365</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforce</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceSandboxApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">samlp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for a SAML add-on. For details, see SAML.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Audience of the SAML Assertion. Default will be the Issuer on SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authnContextClassRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Class reference of the authentication context.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Protocol binding used for SAML logout responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createUpnClaim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true) Indicates whether or not a UPN claim should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Destination of the SAML Response. If not specified, it will be AssertionConsumerUrlof SAMLRequest or Callback URL if there was no SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digestAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">sha1</span></code>). Algorithm used to calculate the digest of the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">defaultsha1</span></code> and <code class="docutils literal notranslate"><span class="pre">sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAttributeNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean,(Default=true). Indicates whether or not we should infer the NameFormat based on the attribute name. If set to false, the attribute NameFormat is not set in the assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer, (Default=3600). Number of seconds during which the token is valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(Resource). Configuration settings for logout. For details, see Logout.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">callback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Service provider’s Single Logout Service URL, to which Auth0 will send logout requests and responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sloEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not Auth0 should notify service providers of session termination.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not to add additional identity information in the token, such as the provider used and the access_token, if available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapUnknownClaimsAsIs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=false). Indicates whether or not to add a prefix of <code class="docutils literal notranslate"><span class="pre">http://schema.auth0.com</span></code> to any claims that are not mapped to the common profile when passed through in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String). Mappings between the Auth0 user profile property name (<code class="docutils literal notranslate"><span class="pre">name</span></code>) and the output attributes on the SAML attribute in the assertion (<code class="docutils literal notranslate"><span class="pre">value</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</span></code>). Format of the name identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierProbes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). Attributes that can be used for Subject/NameID. Auth0 will try each of the attributes of this array in order and use the first value it finds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughClaimsWithNoMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not to passthrough claims that are not mapped to the common profile in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Recipient of the SAML Assertion (SubjectConfirmationData). Default is AssertionConsumerUrl on SAMLRequest or Callback URL if no SAMLRequest was sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the SAML Response should be signed instead of the SAML Assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code>). Algorithm used to sign the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typedAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not we should infer the <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> of the element. Types include <code class="docutils literal notranslate"><span class="pre">xs:string</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:double</span></code>, and <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>. When set to false, all <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> are <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sapApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sentry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sharepoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">springcm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zendesk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
</ul>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Algorithm used to sign JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Number of seconds during which the JWT will be valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String). Permissions (scopes) included in JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEncoded</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the client secret is base64 encoded.</p></li>
</ul>
<p>The <strong>mobile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">android</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for Android native apps. For details, see Android.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appPackageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256CertFingerprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ios</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for i0S native apps. For details, see iOS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appBundleIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.Client.addons">
<code class="sig-name descname">addons</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.addons" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aws</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureSb</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">box</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudbees</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">concur</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropbox</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">echosign</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">egnyte</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firebase</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">layer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mscrm</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">newrelic</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">office365</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rms</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforce</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceApi</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceSandboxApi</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">samlp</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for a SAML add-on. For details, see SAML.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Audience of the SAML Assertion. Default will be the Issuer on SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authnContextClassRef</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Class reference of the authentication context.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Protocol binding used for SAML logout responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createUpnClaim</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean, (Default=true) Indicates whether or not a UPN claim should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Destination of the SAML Response. If not specified, it will be AssertionConsumerUrlof SAMLRequest or Callback URL if there was no SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digestAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">sha1</span></code>). Algorithm used to calculate the digest of the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">defaultsha1</span></code> and <code class="docutils literal notranslate"><span class="pre">sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAttributeNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean,(Default=true). Indicates whether or not we should infer the NameFormat based on the attribute name. If set to false, the attribute NameFormat is not set in the assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer, (Default=3600). Number of seconds during which the token is valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(Resource). Configuration settings for logout. For details, see Logout.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">callback</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Service provider’s Single Logout Service URL, to which Auth0 will send logout requests and responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sloEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not Auth0 should notify service providers of session termination.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean, (Default=true). Indicates whether or not to add additional identity information in the token, such as the provider used and the access_token, if available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapUnknownClaimsAsIs</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean, (Default=false). Indicates whether or not to add a prefix of <code class="docutils literal notranslate"><span class="pre">http://schema.auth0.com</span></code> to any claims that are not mapped to the common profile when passed through in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(String). Mappings between the Auth0 user profile property name (<code class="docutils literal notranslate"><span class="pre">name</span></code>) and the output attributes on the SAML attribute in the assertion (<code class="docutils literal notranslate"><span class="pre">value</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</span></code>). Format of the name identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierProbes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(String). Attributes that can be used for Subject/NameID. Auth0 will try each of the attributes of this array in order and use the first value it finds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughClaimsWithNoMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean, (Default=true). Indicates whether or not to passthrough claims that are not mapped to the common profile in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Recipient of the SAML Assertion (SubjectConfirmationData). Default is AssertionConsumerUrl on SAMLRequest or Callback URL if no SAMLRequest was sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the SAML Response should be signed instead of the SAML Assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code>). Algorithm used to sign the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typedAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean, (Default=true). Indicates whether or not we should infer the <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> of the element. Types include <code class="docutils literal notranslate"><span class="pre">xs:string</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:double</span></code>, and <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>. When set to false, all <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> are <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sapApi</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sentry</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sharepoint</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">springcm</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zendesk</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoom</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.allowed_logout_urls">
<code class="sig-name descname">allowed_logout_urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.allowed_logout_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). URLs that Auth0 may redirect to after logout.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.allowed_origins">
<code class="sig-name descname">allowed_origins</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.allowed_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.app_type">
<code class="sig-name descname">app_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.app_type" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.callbacks">
<code class="sig-name descname">callbacks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.callbacks" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>String. ID of the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.client_metadata">
<code class="sig-name descname">client_metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.client_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Map(String)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.client_secret">
<code class="sig-name descname">client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Secret for the client; keep this private.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.client_secret_rotation_trigger">
<code class="sig-name descname">client_secret_rotation_trigger</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.client_secret_rotation_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Map.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.cross_origin_auth">
<code class="sig-name descname">cross_origin_auth</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.cross_origin_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.cross_origin_loc">
<code class="sig-name descname">cross_origin_loc</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.cross_origin_loc" title="Permalink to this definition">¶</a></dt>
<dd><p>String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.custom_login_page">
<code class="sig-name descname">custom_login_page</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Content of the custom login page.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.custom_login_page_on">
<code class="sig-name descname">custom_login_page_on</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page_on" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not a custom login page is to be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.custom_login_page_preview">
<code class="sig-name descname">custom_login_page_preview</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.custom_login_page_preview" title="Permalink to this definition">¶</a></dt>
<dd><p>String.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.description" title="Permalink to this definition">¶</a></dt>
<dd><p>String, (Max length = 140 characters). Description of the purpose of the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.encryption_key">
<code class="sig-name descname">encryption_key</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.encryption_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Map(String).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.form_template">
<code class="sig-name descname">form_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.form_template" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Form template for WS-Federation protocol.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.grant_types">
<code class="sig-name descname">grant_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.grant_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). Types of grants that this client is authorized to use.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.is_first_party">
<code class="sig-name descname">is_first_party</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.is_first_party" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not this client is a first-party client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.is_token_endpoint_ip_header_trusted">
<code class="sig-name descname">is_token_endpoint_ip_header_trusted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.is_token_endpoint_ip_header_trusted" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the token endpoint IP header is trusted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.jwt_configuration">
<code class="sig-name descname">jwt_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.jwt_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Algorithm used to sign JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer. Number of seconds during which the JWT will be valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(String). Permissions (scopes) included in JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEncoded</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the client secret is base64 encoded.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.logo_uri">
<code class="sig-name descname">logo_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.logo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.mobile">
<code class="sig-name descname">mobile</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.mobile" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">android</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for Android native apps. For details, see Android.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appPackageName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256CertFingerprints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(String)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ios</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for i0S native apps. For details, see iOS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appBundleIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.oidc_conformant">
<code class="sig-name descname">oidc_conformant</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.oidc_conformant" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.sso">
<code class="sig-name descname">sso</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.sso" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.sso_disabled">
<code class="sig-name descname">sso_disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.sso_disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not SSO is disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.token_endpoint_auth_method">
<code class="sig-name descname">token_endpoint_auth_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.token_endpoint_auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Client.web_origins">
<code class="sig-name descname">web_origins</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Client.web_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). URLs that represent valid web origins for use with web message response mode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Client resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for add-ons for this client. For details, see Add-ons.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>allowed_origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that represent valid origins for cross-origin resource sharing. By default, all your callback URLs will be allowed.</p></li>
<li><p><strong>app_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of application the client represents. Options include <code class="docutils literal notranslate"><span class="pre">native</span></code>, <code class="docutils literal notranslate"><span class="pre">spa</span></code>, <code class="docutils literal notranslate"><span class="pre">regular_web</span></code>, <code class="docutils literal notranslate"><span class="pre">non_interactive</span></code>, <code class="docutils literal notranslate"><span class="pre">rms</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudbees</span></code>, <code class="docutils literal notranslate"><span class="pre">concur</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">mscrm</span></code>, <code class="docutils literal notranslate"><span class="pre">echosign</span></code>, <code class="docutils literal notranslate"><span class="pre">egnyte</span></code>, <code class="docutils literal notranslate"><span class="pre">newrelic</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">sentry</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">springcm</span></code>, <code class="docutils literal notranslate"><span class="pre">zendesk</span></code>, <code class="docutils literal notranslate"><span class="pre">zoom</span></code>.</p></li>
<li><p><strong>callbacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may call back to after a user authenticates for the client. Make sure to specify the protocol (<a class="reference external" href="https://">https://</a>) otherwise the callback may fail in some cases. With the exception of custom URI schemes for native clients, all callbacks should use protocol <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client.</p></li>
<li><p><strong>client_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String)</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret for the client; keep this private.</p></li>
<li><p><strong>client_secret_rotation_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map.</p></li>
<li><p><strong>cross_origin_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client can be used to make cross-origin authentication requests.</p></li>
<li><p><strong>cross_origin_loc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL for the location on your site where the cross-origin verification takes place for the cross-origin auth flow. Used when performing auth in your own domain instead of through the Auth0-hosted login page.</p></li>
<li><p><strong>custom_login_page</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Content of the custom login page.</p></li>
<li><p><strong>custom_login_page_on</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not a custom login page is to be used.</p></li>
<li><p><strong>custom_login_page_preview</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, (Max length = 140 characters). Description of the purpose of the client.</p></li>
<li><p><strong>encryption_key</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String).</p></li>
<li><p><strong>form_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Form template for WS-Federation protocol.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Types of grants that this client is authorized to use.</p></li>
<li><p><strong>is_first_party</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client is a first-party client.</p></li>
<li><p><strong>is_token_endpoint_ip_header_trusted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the token endpoint IP header is trusted.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the JWTs issued for this client. For details, see JWT Configuration.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. URL of the logo for the client. Recommended size is 150px x 150px. If none is set, the default badge for the application type will be shown.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for mobile native applications. For details, see Mobile.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the client.</p></li>
<li><p><strong>oidc_conformant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this client will conform to strict OIDC specifications.</p></li>
<li><p><strong>sso</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the client should use Auth0 rather than the IdP to perform Single Sign-On (SSO). True = Use Auth0.</p></li>
<li><p><strong>sso_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not SSO is disabled.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Defines the requested authentication method for the token endpoint. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code> (public client without a client secret), <code class="docutils literal notranslate"><span class="pre">client_secret_post</span></code> (client uses HTTP POST parameters), <code class="docutils literal notranslate"><span class="pre">client_secret_basic</span></code> (client uses HTTP Basic).</p></li>
<li><p><strong>web_origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that represent valid web origins for use with web message response mode.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aws</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureSb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">box</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudbees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">concur</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropbox</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">echosign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">egnyte</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firebase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">layer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mscrm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">newrelic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">office365</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforce</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceSandboxApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">samlp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for a SAML add-on. For details, see SAML.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Audience of the SAML Assertion. Default will be the Issuer on SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authnContextClassRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Class reference of the authentication context.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Protocol binding used for SAML logout responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createUpnClaim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true) Indicates whether or not a UPN claim should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Destination of the SAML Response. If not specified, it will be AssertionConsumerUrlof SAMLRequest or Callback URL if there was no SAMLRequest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digestAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">sha1</span></code>). Algorithm used to calculate the digest of the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">defaultsha1</span></code> and <code class="docutils literal notranslate"><span class="pre">sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAttributeNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean,(Default=true). Indicates whether or not we should infer the NameFormat based on the attribute name. If set to false, the attribute NameFormat is not set in the assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer, (Default=3600). Number of seconds during which the token is valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(Resource). Configuration settings for logout. For details, see Logout.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">callback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Service provider’s Single Logout Service URL, to which Auth0 will send logout requests and responses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sloEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not Auth0 should notify service providers of session termination.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not to add additional identity information in the token, such as the provider used and the access_token, if available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapUnknownClaimsAsIs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=false). Indicates whether or not to add a prefix of <code class="docutils literal notranslate"><span class="pre">http://schema.auth0.com</span></code> to any claims that are not mapped to the common profile when passed through in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String). Mappings between the Auth0 user profile property name (<code class="docutils literal notranslate"><span class="pre">name</span></code>) and the output attributes on the SAML attribute in the assertion (<code class="docutils literal notranslate"><span class="pre">value</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</span></code>). Format of the name identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierProbes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). Attributes that can be used for Subject/NameID. Auth0 will try each of the attributes of this array in order and use the first value it finds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughClaimsWithNoMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not to passthrough claims that are not mapped to the common profile in the output assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Recipient of the SAML Assertion (SubjectConfirmationData). Default is AssertionConsumerUrl on SAMLRequest or Callback URL if no SAMLRequest was sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the SAML Response should be signed instead of the SAML Assertion.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, (Default=<code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code>). Algorithm used to sign the SAML Assertion or response. Options include <code class="docutils literal notranslate"><span class="pre">rsa-sha1</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-sha256</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typedAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean, (Default=true). Indicates whether or not we should infer the <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> of the element. Types include <code class="docutils literal notranslate"><span class="pre">xs:string</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">xs:double</span></code>, and <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>. When set to false, all <code class="docutils literal notranslate"><span class="pre">xs:type</span></code> are <code class="docutils literal notranslate"><span class="pre">xs:anyType</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sapApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sentry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sharepoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">springcm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zendesk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String</p></li>
</ul>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Algorithm used to sign JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Number of seconds during which the JWT will be valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String). Permissions (scopes) included in JWTs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEncoded</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the client secret is base64 encoded.</p></li>
</ul>
<p>The <strong>mobile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">android</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for Android native apps. For details, see Android.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appPackageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256CertFingerprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ios</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for i0S native apps. For details, see iOS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appBundleIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Client.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Client.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Client.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.ClientGrant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">ClientGrant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth0 uses various grant types, or methods by which you grant limited access to your resources to another entity without exposing credentials. The OAuth 2.0 protocol supports several types of grants, which allow different types of access. This resource allows you to create and manage client grants used with configured Auth0 clients.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_client</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;myClient&quot;</span><span class="p">)</span>
<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;https://api.example.com/client-grant&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Create foos&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;create:foo&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Create bars&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;create:bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
<span class="n">my_client_grant</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ClientGrant</span><span class="p">(</span><span class="s2">&quot;myClientGrant&quot;</span><span class="p">,</span>
    <span class="n">audience</span><span class="o">=</span><span class="n">my_resource_server</span><span class="o">.</span><span class="n">identifier</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">my_client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;create:foo&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Audience or API Identifier for this grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client for this grant.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Permissions (scopes) included in this grant.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.ClientGrant.audience">
<code class="sig-name descname">audience</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ClientGrant.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Audience or API Identifier for this grant.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ClientGrant.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ClientGrant.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>String. ID of the client for this grant.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ClientGrant.scopes">
<code class="sig-name descname">scopes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ClientGrant.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). Permissions (scopes) included in this grant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientGrant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Audience or API Identifier for this grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the client for this grant.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Permissions (scopes) included in this grant.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ClientGrant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.ClientGrant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ClientGrant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_clients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_domain_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can define sources of users, otherwise known as connections, which may include identity providers (such as Google or LinkedIn), databases, or passwordless authentication methods. This resource allows you to configure and manage connections to be used with your clients and users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_connection</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Connection</span><span class="p">(</span><span class="s2">&quot;myConnection&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;bruteForceProtection&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="s2">&quot;configuration&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;bar&quot;</span><span class="p">:</span> <span class="s2">&quot;baz&quot;</span><span class="p">,</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;customScripts&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;getUser&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;function getByEmail (email, callback) {</span>
<span class="s2">  return callback(new Error(&quot;Whoops!&quot;))</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;enabledDatabaseCustomization&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="s2">&quot;passwordHistory&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;enable&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;size&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;passwordPolicy&quot;</span><span class="p">:</span> <span class="s2">&quot;excellent&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;auth0&quot;</span><span class="p">)</span>
<span class="n">my_waad_connection</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Connection</span><span class="p">(</span><span class="s2">&quot;myWaadConnection&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;apiEnableUsers&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;appDomain&quot;</span><span class="p">:</span> <span class="s2">&quot;my-auth0-app.eu.auth0.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;basicProfile&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;clientId&quot;</span><span class="p">:</span> <span class="s2">&quot;1234&quot;</span><span class="p">,</span>
        <span class="s2">&quot;clientSecret&quot;</span><span class="p">:</span> <span class="s2">&quot;1234&quot;</span><span class="p">,</span>
        <span class="s2">&quot;domainAliases&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;example.io&quot;</span><span class="p">],</span>
        <span class="s2">&quot;extGroups&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;extProfile&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;tenantDomain&quot;</span><span class="p">:</span> <span class="s2">&quot;exmaple.onmicrosoft.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useWsfed&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;waadCommonEndpoint&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;waadProtocol&quot;</span><span class="p">:</span> <span class="s2">&quot;openid-connect&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;waad&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used in login screen</p></li>
<li><p><strong>enabled_clients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(String). IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p></li>
<li><p><strong>is_domain_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the connection is domain level.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for connection options. For details, see Options.</p></li>
<li><p><strong>realms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p></li>
<li><p><strong>strategy_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Int. Version 1 is deprecated, use version 2.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adfsServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. ADFS Metadata source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiEnableUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Azure AD domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bruteForceProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to enable brute force protection, which will limit the number of signups and failed logins from a suspicious IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Client ID given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. Client secret given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">communityBaseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String), Case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customScripts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSignup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to allow user sign-ups to your application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">discoveryUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Usually an URL ending with <code class="docutils literal notranslate"><span class="pre">/.well-known/openid-configuration</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). List of the domains that can be authenticated using the Identity Provider. Only needed for Identifier First authentication flows.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledDatabaseCustomization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">from_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SMS number for the sender. Used when SMS Source is From.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iconUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">importMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not you have a legacy user store and want to gradually migrate those users to the Auth0 user store. <a class="reference external" href="https://auth0.com/docs/users/guides/configure-automatic-migration">Learn more</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. URL of the issuer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jwksUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxGroupsToRetrieve</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Maximum number of groups to retrieve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messagingServiceSid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SID for Copilot. Used when SMS Source is Copilot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordComplexityOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for password complexity. For details, see Password Complexity Options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Minimum number of characters allowed in passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordDictionary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for the password dictionary check, which does not allow passwords that are part of the password dictionary. For details, see Password Dictionary.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set(String), (Maximum=2000 characters). Customized contents of the password dictionary. By default, the password dictionary contains a list of the <a class="reference external" href="https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt">10,000 most common passwords</a>; your customized content is used in addition to the default password dictionary. Matching is not case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordHistories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(Resource). Configuration settings for the password history that is maintained for each user to prevent the reuse of passwords. For details, see Password History.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer, (Maximum=24). Indicates the number of passwords to keep in history.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordNoPersonalInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for the password personal info check, which does not allow passwords that contain any part of the user’s personal data, including user’s name, username, nickname, user_metadata.name, user_metadata.first, user_metadata.last, user’s email, or first part of the user’s email. For details, see Password No Personal Info.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether the password personal info check is enabled for this connection.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Indicates level of password strength to enforce during authentication. A strong password policy will make it difficult, if not improbable, for someone to guess a password through either manual or automated means. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">low</span></code>, <code class="docutils literal notranslate"><span class="pre">fair</span></code>, <code class="docutils literal notranslate"><span class="pre">good</span></code>, <code class="docutils literal notranslate"><span class="pre">excellent</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiresUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the user is required to provide a username in addition to an email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). Value must be a list of scopes. For example <code class="docutils literal notranslate"><span class="pre">[&quot;openid&quot;,</span> <span class="pre">&quot;profile&quot;,</span> <span class="pre">&quot;email&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Int. Version 1 is deprecated, use version 2.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syntax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Syntax of the SMS. Options include <code class="docutils literal notranslate"><span class="pre">markdown</span></code> and <code class="docutils literal notranslate"><span class="pre">liquid</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Template for the SMS. You can use <code class="docutils literal notranslate"><span class="pre">&#64;&#64;password&#64;&#64;</span></code> as a placeholder for the password value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">totp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(Resource). Configuration options for one-time passwords. For details, see TOTP.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Length of the one-time password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Seconds between allowed generation of new passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioSid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SID for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AuthToken for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Value must be <code class="docutils literal notranslate"><span class="pre">back_channel</span></code> or <code class="docutils literal notranslate"><span class="pre">front_channel</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCertAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useWsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Bool</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userinfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadCommonEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the common endpoint rather than the default endpoint. Typically enabled if you’re using this for a multi-tenant application in Azure AD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.Connection.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name used in login screen</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.enabled_clients">
<code class="sig-name descname">enabled_clients</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.enabled_clients" title="Permalink to this definition">¶</a></dt>
<dd><p>Set(String). IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.is_domain_connection">
<code class="sig-name descname">is_domain_connection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.is_domain_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the connection is domain level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.options">
<code class="sig-name descname">options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.options" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for connection options. For details, see Options.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adfsServer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. ADFS Metadata source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiEnableUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Azure AD domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bruteForceProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to enable brute force protection, which will limit the number of signups and failed logins from a suspicious IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Client ID given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. Client secret given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">communityBaseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(String), Case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customScripts</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableCache</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSignup</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to allow user sign-ups to your application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">discoveryUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Usually an URL ending with <code class="docutils literal notranslate"><span class="pre">/.well-known/openid-configuration</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(String). List of the domains that can be authenticated using the Identity Provider. Only needed for Identifier First authentication flows.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledDatabaseCustomization</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">from_</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. SMS number for the sender. Used when SMS Source is From.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iconUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityApi</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">importMode</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not you have a legacy user store and want to gradually migrate those users to the Auth0 user store. <a class="reference external" href="https://auth0.com/docs/users/guides/configure-automatic-migration">Learn more</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. URL of the issuer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jwksUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxGroupsToRetrieve</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Maximum number of groups to retrieve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messagingServiceSid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. SID for Copilot. Used when SMS Source is Copilot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordComplexityOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for password complexity. For details, see Password Complexity Options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer. Minimum number of characters allowed in passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordDictionary</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for the password dictionary check, which does not allow passwords that are part of the password dictionary. For details, see Password Dictionary.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaries</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set(String), (Maximum=2000 characters). Customized contents of the password dictionary. By default, the password dictionary contains a list of the <a class="reference external" href="https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt">10,000 most common passwords</a>; your customized content is used in addition to the default password dictionary. Matching is not case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordHistories</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(Resource). Configuration settings for the password history that is maintained for each user to prevent the reuse of passwords. For details, see Password History.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer, (Maximum=24). Indicates the number of passwords to keep in history.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordNoPersonalInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for the password personal info check, which does not allow passwords that contain any part of the user’s personal data, including user’s name, username, nickname, user_metadata.name, user_metadata.first, user_metadata.last, user’s email, or first part of the user’s email. For details, see Password No Personal Info.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether the password personal info check is enabled for this connection.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Indicates level of password strength to enforce during authentication. A strong password policy will make it difficult, if not improbable, for someone to guess a password through either manual or automated means. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">low</span></code>, <code class="docutils literal notranslate"><span class="pre">fair</span></code>, <code class="docutils literal notranslate"><span class="pre">good</span></code>, <code class="docutils literal notranslate"><span class="pre">excellent</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiresUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the user is required to provide a username in addition to an email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(String). Value must be a list of scopes. For example <code class="docutils literal notranslate"><span class="pre">[&quot;openid&quot;,</span> <span class="pre">&quot;profile&quot;,</span> <span class="pre">&quot;email&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy_version</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Int. Version 1 is deprecated, use version 2.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syntax</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Syntax of the SMS. Options include <code class="docutils literal notranslate"><span class="pre">markdown</span></code> and <code class="docutils literal notranslate"><span class="pre">liquid</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Template for the SMS. You can use <code class="docutils literal notranslate"><span class="pre">&#64;&#64;password&#64;&#64;</span></code> as a placeholder for the password value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">totp</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map(Resource). Configuration options for one-time passwords. For details, see TOTP.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer. Length of the one-time password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeStep</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer. Seconds between allowed generation of new passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioSid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. SID for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. AuthToken for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Value must be <code class="docutils literal notranslate"><span class="pre">back_channel</span></code> or <code class="docutils literal notranslate"><span class="pre">front_channel</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCertAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useWsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Bool</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userinfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validation</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadCommonEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to use the common endpoint rather than the default endpoint. Typically enabled if you’re using this for a multi-tenant application in Azure AD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.realms">
<code class="sig-name descname">realms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.realms" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.strategy">
<code class="sig-name descname">strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Connection.strategy_version">
<code class="sig-name descname">strategy_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Connection.strategy_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Int. Version 1 is deprecated, use version 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_clients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_domain_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy_version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used in login screen</p></li>
<li><p><strong>enabled_clients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(String). IDs of the clients for which the connection is enabled. If not specified, no clients are enabled.</p></li>
<li><p><strong>is_domain_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the connection is domain level.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for connection options. For details, see Options.</p></li>
<li><p><strong>realms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). Defines the realms for which the connection will be used (i.e., email domains). If not specified, the connection name is added as the realm.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Type of the connection, which indicates the identity provider. Options include <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">adfs</span></code>, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aol</span></code>, <code class="docutils literal notranslate"><span class="pre">apple</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0-oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">baidu</span></code>, <code class="docutils literal notranslate"><span class="pre">bitbucket</span></code>, <code class="docutils literal notranslate"><span class="pre">bitly</span></code>, <code class="docutils literal notranslate"><span class="pre">box</span></code>, <code class="docutils literal notranslate"><span class="pre">custom</span></code>, <code class="docutils literal notranslate"><span class="pre">daccount</span></code>, <code class="docutils literal notranslate"><span class="pre">dropbox</span></code>, <code class="docutils literal notranslate"><span class="pre">dwolla</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote</span></code>, <code class="docutils literal notranslate"><span class="pre">evernote-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">exact</span></code>, <code class="docutils literal notranslate"><span class="pre">facebook</span></code>, <code class="docutils literal notranslate"><span class="pre">fitbit</span></code>, <code class="docutils literal notranslate"><span class="pre">flickr</span></code>, <code class="docutils literal notranslate"><span class="pre">github</span></code>, <code class="docutils literal notranslate"><span class="pre">google-apps</span></code>, <code class="docutils literal notranslate"><span class="pre">google-oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">guardian</span></code>, <code class="docutils literal notranslate"><span class="pre">instagram</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>, <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">linkedin</span></code>, <code class="docutils literal notranslate"><span class="pre">miicard</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth1</span></code>, <code class="docutils literal notranslate"><span class="pre">oauth2</span></code>, <code class="docutils literal notranslate"><span class="pre">office365</span></code>, <code class="docutils literal notranslate"><span class="pre">oidc</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal</span></code>, <code class="docutils literal notranslate"><span class="pre">paypal-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">pingfederate</span></code>, <code class="docutils literal notranslate"><span class="pre">planningcenter</span></code>, <code class="docutils literal notranslate"><span class="pre">renren</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-community</span></code>, <code class="docutils literal notranslate"><span class="pre">salesforce-sandbox</span></code> <code class="docutils literal notranslate"><span class="pre">samlp</span></code>, <code class="docutils literal notranslate"><span class="pre">sharepoint</span></code>, <code class="docutils literal notranslate"><span class="pre">shopify</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">soundcloud</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity</span></code>, <code class="docutils literal notranslate"><span class="pre">thecity-sandbox</span></code>, <code class="docutils literal notranslate"><span class="pre">thirtysevensignals</span></code>, <code class="docutils literal notranslate"><span class="pre">twitter</span></code>, <code class="docutils literal notranslate"><span class="pre">untappd</span></code>, <code class="docutils literal notranslate"><span class="pre">vkontakte</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, <code class="docutils literal notranslate"><span class="pre">weibo</span></code>, <code class="docutils literal notranslate"><span class="pre">windowslive</span></code>, <code class="docutils literal notranslate"><span class="pre">wordpress</span></code>, <code class="docutils literal notranslate"><span class="pre">yahoo</span></code>, <code class="docutils literal notranslate"><span class="pre">yammer</span></code>, <code class="docutils literal notranslate"><span class="pre">yandex</span></code>.</p></li>
<li><p><strong>strategy_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Int. Version 1 is deprecated, use version 2.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adfsServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. ADFS Metadata source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedAudiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiEnableUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Azure AD domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bruteForceProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to enable brute force protection, which will limit the number of signups and failed logins from a suspicious IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Client ID given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. Client secret given by your OIDC provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">communityBaseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String), Case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customScripts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSignup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to allow user sign-ups to your application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">discoveryUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Usually an URL ending with <code class="docutils literal notranslate"><span class="pre">/.well-known/openid-configuration</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). List of the domains that can be authenticated using the Identity Provider. Only needed for Identifier First authentication flows.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledDatabaseCustomization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">from_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SMS number for the sender. Used when SMS Source is From.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iconUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">importMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not you have a legacy user store and want to gradually migrate those users to the Auth0 user store. <a class="reference external" href="https://auth0.com/docs/users/guides/configure-automatic-migration">Learn more</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. URL of the issuer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jwksUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxGroupsToRetrieve</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Maximum number of groups to retrieve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messagingServiceSid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SID for Copilot. Used when SMS Source is Copilot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordComplexityOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for password complexity. For details, see Password Complexity Options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Minimum number of characters allowed in passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordDictionary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for the password dictionary check, which does not allow passwords that are part of the password dictionary. For details, see Password Dictionary.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set(String), (Maximum=2000 characters). Customized contents of the password dictionary. By default, the password dictionary contains a list of the <a class="reference external" href="https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt">10,000 most common passwords</a>; your customized content is used in addition to the default password dictionary. Matching is not case-sensitive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordHistories</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(Resource). Configuration settings for the password history that is maintained for each user to prevent the reuse of passwords. For details, see Password History.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether password history is enabled for the connection. When enabled, any existing users in this connection will be unaffected; the system will maintain their password history going forward.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer, (Maximum=24). Indicates the number of passwords to keep in history.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordNoPersonalInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for the password personal info check, which does not allow passwords that contain any part of the user’s personal data, including user’s name, username, nickname, user_metadata.name, user_metadata.first, user_metadata.last, user’s email, or first part of the user’s email. For details, see Password No Personal Info.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether the password personal info check is enabled for this connection.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">passwordPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Indicates level of password strength to enforce during authentication. A strong password policy will make it difficult, if not improbable, for someone to guess a password through either manual or automated means. Options include <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">low</span></code>, <code class="docutils literal notranslate"><span class="pre">fair</span></code>, <code class="docutils literal notranslate"><span class="pre">good</span></code>, <code class="docutils literal notranslate"><span class="pre">excellent</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiresUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the user is required to provide a username in addition to an email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(String). Value must be a list of scopes. For example <code class="docutils literal notranslate"><span class="pre">[&quot;openid&quot;,</span> <span class="pre">&quot;profile&quot;,</span> <span class="pre">&quot;email&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Int. Version 1 is deprecated, use version 2.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syntax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Syntax of the SMS. Options include <code class="docutils literal notranslate"><span class="pre">markdown</span></code> and <code class="docutils literal notranslate"><span class="pre">liquid</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Template for the SMS. You can use <code class="docutils literal notranslate"><span class="pre">&#64;&#64;password&#64;&#64;</span></code> as a placeholder for the password value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">totp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map(Resource). Configuration options for one-time passwords. For details, see TOTP.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Length of the one-time password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Seconds between allowed generation of new passwords.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioSid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SID for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twilioToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AuthToken for your Twilio account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Value must be <code class="docutils literal notranslate"><span class="pre">back_channel</span></code> or <code class="docutils literal notranslate"><span class="pre">front_channel</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCertAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useWsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Bool</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userinfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - String.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadCommonEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the common endpoint rather than the default endpoint. Typically enabled if you’re using this for a multi-tenant application in Azure AD.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waadProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.CustomDomain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">CustomDomain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can use a custom domain to maintain a consistent user experience. This resource allows you to create and manage a custom domain within your Auth0 tenant.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_custom_domain</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">CustomDomain</span><span class="p">(</span><span class="s2">&quot;myCustomDomain&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;auth.example.com&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;auth0_managed_certs&quot;</span><span class="p">,</span>
    <span class="n">verification_method</span><span class="o">=</span><span class="s2">&quot;txt&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the custom domain.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p></li>
<li><p><strong>verification_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the custom domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.primary">
<code class="sig-name descname">primary</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.primary" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not this is a primary domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.status" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Configuration status for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">pending_verification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ready</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.type" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.verification">
<code class="sig-name descname">verification</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.verification" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for verification. For details, see Verification.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List(Map). Verification methods for the domain.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.CustomDomain.verification_method">
<code class="sig-name descname">verification_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.CustomDomain.verification_method" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_method</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomDomain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the custom domain.</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not this is a primary domain.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Configuration status for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">pending_verification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ready</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Provisioning type for the custom domain. Options include <code class="docutils literal notranslate"><span class="pre">auth0_managed_certs</span></code> and <code class="docutils literal notranslate"><span class="pre">self_managed_certs</span></code>.</p></li>
<li><p><strong>verification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for verification. For details, see Verification.</p></li>
<li><p><strong>verification_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Domain verification method. Options include <code class="docutils literal notranslate"><span class="pre">txt</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>verification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List(Map). Verification methods for the domain.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.CustomDomain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.CustomDomain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.CustomDomain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Email">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Email</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_from_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can have standard welcome, password reset, and account verification email-based workflows built right into Auth0. This resource allows you to configure email providers so you can route all emails that are part of Auth0’s authentication workflows through the supported high-volume email service of your choice.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_email_provider</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Email</span><span class="p">(</span><span class="s2">&quot;myEmailProvider&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;accessKeyId&quot;</span><span class="p">:</span> <span class="s2">&quot;AKIAXXXXXXXXXXXXXXXX&quot;</span><span class="p">,</span>
        <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;secretAccessKey&quot;</span><span class="p">:</span> <span class="s2">&quot;7e8c2148xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">default_from_address</span><span class="o">=</span><span class="s2">&quot;accounts@example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p></li>
<li><p><strong>default_from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address to use as the sender when no other “from” address is specified.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email provider is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AWS Access Key ID. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. API Key for your email service. Will always be encrypted in our database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. API User for your email service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Default region. Used only for AWS, Mailgun, and SparkPost.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretAccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AWS Secret Key. Will always be encrypted in our database. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Hostname or IP address of your SMTP server. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. SMTP password. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Port used by your SMTP server. Please avoid using port 25 if possible because many providers have limitations on this port. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SMTP username. Used only for SMTP.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.Email.credentials">
<code class="sig-name descname">credentials</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Email.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. AWS Access Key ID. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. API Key for your email service. Will always be encrypted in our database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUser</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. API User for your email service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Default region. Used only for AWS, Mailgun, and SparkPost.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretAccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. AWS Secret Key. Will always be encrypted in our database. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Hostname or IP address of your SMTP server. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Case-sensitive. SMTP password. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer. Port used by your SMTP server. Please avoid using port 25 if possible because many providers have limitations on this port. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpUser</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. SMTP username. Used only for SMTP.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Email.default_from_address">
<code class="sig-name descname">default_from_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Email.default_from_address" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Email address to use as the sender when no other “from” address is specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Email.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Email.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the email provider is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Email.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Email.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_from_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Email resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the credentials for the email provider. For details, see Credentials.</p></li>
<li><p><strong>default_from_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address to use as the sender when no other “from” address is specified.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email provider is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the email provider. Options include <code class="docutils literal notranslate"><span class="pre">mailgun</span></code>, <code class="docutils literal notranslate"><span class="pre">mandrill</span></code>, <code class="docutils literal notranslate"><span class="pre">sendgrid</span></code>, <code class="docutils literal notranslate"><span class="pre">ses</span></code>, <code class="docutils literal notranslate"><span class="pre">smtp</span></code>, and <code class="docutils literal notranslate"><span class="pre">sparkpost</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AWS Access Key ID. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. API Key for your email service. Will always be encrypted in our database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. API User for your email service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Default region. Used only for AWS, Mailgun, and SparkPost.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretAccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. AWS Secret Key. Will always be encrypted in our database. Used only for AWS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Hostname or IP address of your SMTP server. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Case-sensitive. SMTP password. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer. Port used by your SMTP server. Please avoid using port 25 if possible because many providers have limitations on this port. Used only for SMTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. SMTP username. Used only for SMTP.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Email.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Email.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Email.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.EmailTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">EmailTemplate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">from_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">result_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syntax</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_lifetime_in_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can have standard welcome, password reset, and account verification email-based workflows built right into Auth0. This resource allows you to configure email templates to customize the look, feel, and sender identities of emails sent by Auth0. Used in conjunction with configured email providers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_email_provider</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Email</span><span class="p">(</span><span class="s2">&quot;myEmailProvider&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">default_from_address</span><span class="o">=</span><span class="s2">&quot;accounts@example.com&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;accessKeyId&quot;</span><span class="p">:</span> <span class="s2">&quot;AKIAXXXXXXXXXXXXXXXX&quot;</span><span class="p">,</span>
        <span class="s2">&quot;secretAccessKey&quot;</span><span class="p">:</span> <span class="s2">&quot;7e8c2148xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
        <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">my_email_template</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">EmailTemplate</span><span class="p">(</span><span class="s2">&quot;myEmailTemplate&quot;</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;welcome_email&quot;</span><span class="p">,</span>
    <span class="n">body</span><span class="o">=</span><span class="s2">&quot;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome!&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;&quot;</span><span class="p">,</span>
    <span class="n">from_</span><span class="o">=</span><span class="s2">&quot;welcome@example.com&quot;</span><span class="p">,</span>
    <span class="n">result_url</span><span class="o">=</span><span class="s2">&quot;https://example.com/welcome&quot;</span><span class="p">,</span>
    <span class="n">subject</span><span class="o">=</span><span class="s2">&quot;Welcome&quot;</span><span class="p">,</span>
    <span class="n">syntax</span><span class="o">=</span><span class="s2">&quot;liquid&quot;</span><span class="p">,</span>
    <span class="n">url_lifetime_in_seconds</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the template is enabled.</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[str] from*: String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] result_url: String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.
:param pulumi.Input[str] subject: String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] syntax: String. Syntax of the template body. You can use either text or HTML + Liquid syntax.
:param pulumi.Input[str] template: String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).
:param pulumi.Input[float] url_lifetime_in_seconds: Integer. Number of seconds during which the link within the email will be valid.</p>
<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.body" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the template is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.from_">
<code class="sig-name descname">from_</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.from_" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.result_url">
<code class="sig-name descname">result_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.result_url" title="Permalink to this definition">¶</a></dt>
<dd><p>String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.subject">
<code class="sig-name descname">subject</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.subject" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.syntax">
<code class="sig-name descname">syntax</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.syntax" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Syntax of the template body. You can use either text or HTML + Liquid syntax.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.template" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.EmailTemplate.url_lifetime_in_seconds">
<code class="sig-name descname">url_lifetime_in_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.EmailTemplate.url_lifetime_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Number of seconds during which the link within the email will be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">from_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">result_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syntax</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_lifetime_in_seconds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EmailTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>String. Body of the email template. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the template is enabled.</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[str] from*: String. Email address to use as the sender. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] result_url: String. URL to redirect the user to after a successful action. <a class="reference external" href="https://auth0.com/docs/email/templates#configuring-the-redirect-to-url">Learn more</a>.
:param pulumi.Input[str] subject: String. Subject line of the email. You can include <a class="reference external" href="https://auth0.com/docs/email/templates#common-variables">common variables</a>.
:param pulumi.Input[str] syntax: String. Syntax of the template body. You can use either text or HTML + Liquid syntax.
:param pulumi.Input[str] template: String. Template name. Options include <code class="docutils literal notranslate"><span class="pre">verify_email</span></code>, <code class="docutils literal notranslate"><span class="pre">reset_email</span></code>, <code class="docutils literal notranslate"><span class="pre">welcome_email</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked_account</span></code>, <code class="docutils literal notranslate"><span class="pre">stolen_credentials</span></code>, <code class="docutils literal notranslate"><span class="pre">enrollment_email</span></code>, <code class="docutils literal notranslate"><span class="pre">mfa_oob_code</span></code>, <code class="docutils literal notranslate"><span class="pre">change_password</span></code> (legacy), and <code class="docutils literal notranslate"><span class="pre">password_reset</span></code> (legacy).
:param pulumi.Input[float] url_lifetime_in_seconds: Integer. Number of seconds during which the link within the email will be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.EmailTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.EmailTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.EmailTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.GlobalClient">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">GlobalClient</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GlobalClient resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aws</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureSb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">box</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudbees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">concur</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropbox</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">echosign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">egnyte</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firebase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">layer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mscrm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">newrelic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">office365</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforce</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceSandboxApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">samlp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authnContextClassRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createUpnClaim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digestAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAttributeNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">callback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sloEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapUnknownClaimsAsIs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierProbes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughClaimsWithNoMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typedAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sapApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sentry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sharepoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">springcm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zendesk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEncoded</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>mobile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">android</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appPackageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256CertFingerprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ios</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appBundleIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="py method">
<dt id="pulumi_auth0.GlobalClient.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">callbacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret_rotation_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cross_origin_loc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_login_page_preview</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">form_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initiate_login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_first_party</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_token_endpoint_ip_header_trusted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_conformant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_origins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalClient resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aws</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureSb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">box</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudbees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">concur</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropbox</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">echosign</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">egnyte</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firebase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">layer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mscrm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">newrelic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">office365</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforce</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">salesforceSandboxApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">samlp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authnContextClassRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">binding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createUpnClaim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digestAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAttributeNameFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">callback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sloEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapUnknownClaimsAsIs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nameIdentifierProbes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughClaimsWithNoMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatureAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typedAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sapApi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sentry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sharepoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">springcm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsfed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zendesk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifetimeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEncoded</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>mobile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">android</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appPackageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256CertFingerprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ios</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appBundleIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.GlobalClient.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.GlobalClient.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.GlobalClient.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Hook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Hook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook" title="Permalink to this definition">¶</a></dt>
<dd><p>Hooks are secure, self-contained functions that allow you to customize the behavior of Auth0 when executed for selected extensibility points of the Auth0 platform. Auth0 invokes Hooks during runtime to execute your custom Node.js code.</p>
<p>Depending on the extensibility point, you can use Hooks with Database Connections and/or Passwordless Connections.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_hook</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Hook</span><span class="p">(</span><span class="s2">&quot;myHook&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) { </span>
<span class="s2">  callback(null, { user }); </span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">trigger_id</span><span class="o">=</span><span class="s2">&quot;pre-user-registration&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hook is enabled, or disabled</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of this hook</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code to be executed when this hook runs</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.Hook.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Hook.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the hook is enabled, or disabled</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Hook.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Hook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of this hook</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Hook.script">
<code class="sig-name descname">script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Hook.script" title="Permalink to this definition">¶</a></dt>
<dd><p>Code to be executed when this hook runs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Hook.trigger_id">
<code class="sig-name descname">trigger_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Hook.trigger_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hook is enabled, or disabled</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of this hook</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code to be executed when this hook runs</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution stage of this rule. Can be credentials-exchange, pre-user-registration, post-user-registration, post-change-password, or send-phone-message</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Hook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Hook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Hook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Prompt">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Prompt</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login_experience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can manage your Auth0 prompts, including choosing the login experience version.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Prompt</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">universal_login_experience</span><span class="o">=</span><span class="s2">&quot;classic&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Prompt.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login_experience</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Prompt resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Prompt.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Prompt.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Prompt.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">debug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the auth0 package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_auth0.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.ResourceServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">ResourceServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_offline_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_alg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_dialect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime_for_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can set up APIs that can be consumed from your authorized applications.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">allow_offline_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;https://api.example.com&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Create foos&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;create:foo&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Create bars&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;create:bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">signing_alg</span><span class="o">=</span><span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
    <span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">token_lifetime</span><span class="o">=</span><span class="mi">8600</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_offline_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p></li>
<li><p><strong>enforce_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not authorization polices are enforced.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String). Used to store additional metadata</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p></li>
<li><p><strong>signing_alg</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p></li>
<li><p><strong>signing_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret used to sign tokens when using symmetric algorithms (HS256).</p></li>
<li><p><strong>skip_consent_for_verifiable_first_party_clients</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p></li>
<li><p><strong>token_dialect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p></li>
<li><p><strong>token_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p></li>
<li><p><strong>token_lifetime_for_web</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p></li>
<li><p><strong>verification_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scopes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Description of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Name of the permission (scope). Examples include <code class="docutils literal notranslate"><span class="pre">read:appointments</span></code> or <code class="docutils literal notranslate"><span class="pre">delete:appointments</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.allow_offline_access">
<code class="sig-name descname">allow_offline_access</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.allow_offline_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.enforce_policies">
<code class="sig-name descname">enforce_policies</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.enforce_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not authorization polices are enforced.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.identifier">
<code class="sig-name descname">identifier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.options">
<code class="sig-name descname">options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Map(String). Used to store additional metadata</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.scopes">
<code class="sig-name descname">scopes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Description of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Name of the permission (scope). Examples include <code class="docutils literal notranslate"><span class="pre">read:appointments</span></code> or <code class="docutils literal notranslate"><span class="pre">delete:appointments</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.signing_alg">
<code class="sig-name descname">signing_alg</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.signing_alg" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.signing_secret">
<code class="sig-name descname">signing_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.signing_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Secret used to sign tokens when using symmetric algorithms (HS256).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.skip_consent_for_verifiable_first_party_clients">
<code class="sig-name descname">skip_consent_for_verifiable_first_party_clients</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.skip_consent_for_verifiable_first_party_clients" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.token_dialect">
<code class="sig-name descname">token_dialect</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_dialect" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.token_lifetime">
<code class="sig-name descname">token_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.token_lifetime_for_web">
<code class="sig-name descname">token_lifetime_for_web</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.token_lifetime_for_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.ResourceServer.verification_location">
<code class="sig-name descname">verification_location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.ResourceServer.verification_location" title="Permalink to this definition">¶</a></dt>
<dd><p>String</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_offline_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_alg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signing_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_dialect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_lifetime_for_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_location</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_offline_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not refresh tokens can be issued for this resource server.</p></li>
<li><p><strong>enforce_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not authorization polices are enforced.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Unique identifier for the resource server. Used as the audience parameter for authorization calls. Can not be changed once set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the resource server. Cannot include <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> or <code class="docutils literal notranslate"><span class="pre">&gt;</span></code> characters.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map(String). Used to store additional metadata</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(Resource).  List of permissions (scopes) used by this resource server. For details, see Scopes.</p></li>
<li><p><strong>signing_alg</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Algorithm used to sign JWTs. Options include <code class="docutils literal notranslate"><span class="pre">HS256</span></code> and <code class="docutils literal notranslate"><span class="pre">RS256</span></code>.</p></li>
<li><p><strong>signing_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Secret used to sign tokens when using symmetric algorithms (HS256).</p></li>
<li><p><strong>skip_consent_for_verifiable_first_party_clients</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not to skip user consent for applications flagged as first party.</p></li>
<li><p><strong>token_dialect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Dialect of access tokens that should be issued for this resource server. Options include <code class="docutils literal notranslate"><span class="pre">access_token</span></code> or <code class="docutils literal notranslate"><span class="pre">access_token_authz</span></code> (includes permissions).</p></li>
<li><p><strong>token_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server from the token endpoint remain valid.</p></li>
<li><p><strong>token_lifetime_for_web</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of seconds during which access tokens issued for this resource server via implicit or hybrid flows remain valid. Cannot be greater than the <code class="docutils literal notranslate"><span class="pre">token_lifetime</span></code> value.</p></li>
<li><p><strong>verification_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scopes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Description of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Name of the permission (scope). Examples include <code class="docutils literal notranslate"><span class="pre">read:appointments</span></code> or <code class="docutils literal notranslate"><span class="pre">delete:appointments</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.ResourceServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.ResourceServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.ResourceServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can created and manage collections of permissions that can be assigned to users, which are otherwise known as roles. Permissions (scopes) are created on auth0_resource_server, then associated with roles and optionally, users using this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_resource_server</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">ResourceServer</span><span class="p">(</span><span class="s2">&quot;myResourceServer&quot;</span><span class="p">,</span>
    <span class="n">enforce_policies</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;my-resource-server-identifier&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;read something&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;read:something&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">signing_alg</span><span class="o">=</span><span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
    <span class="n">skip_consent_for_verifiable_first_party_clients</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">token_lifetime</span><span class="o">=</span><span class="mi">86400</span><span class="p">)</span>
<span class="n">my_role</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;myRole&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Role Description...&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;read:something&quot;</span><span class="p">,</span>
        <span class="s2">&quot;resourceServerIdentifier&quot;</span><span class="p">:</span> <span class="n">my_resource_server</span><span class="o">.</span><span class="n">identifier</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">my_user</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;myUser&quot;</span><span class="p">,</span>
    <span class="n">connection_name</span><span class="o">=</span><span class="s2">&quot;Username-Password-Authentication&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test@test.com&quot;</span><span class="p">,</span>
    <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;testnick&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;passpass$$12$$12&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">my_role</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">user_id</span><span class="o">=</span><span class="s2">&quot;auth0|1234567890&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;testnick&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name for this role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Name of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceServerIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Unique identifier for the resource server.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.Role.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Description of the role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Role.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name for this role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Role.permissions">
<code class="sig-name descname">permissions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Role.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Name of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceServerIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. Unique identifier for the resource server.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name for this role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(Resource). Configuration settings for permissions (scopes) attached to the role. For details, see Permissions.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Name of the permission (scope).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceServerIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. Unique identifier for the resource server.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can create custom Javascript snippets that run in a secure, isolated sandbox as part of your authentication pipeline, which are otherwise known as rules. This resource allows you to create and manage rules. You can create global variable for use with rules by using the .RuleConfig resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_rule</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Rule</span><span class="p">(</span><span class="s2">&quot;myRule&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) {</span>
<span class="s2">  callback(null, user, context);</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">my_rule_config</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">RuleConfig</span><span class="p">(</span><span class="s2">&quot;myRuleConfig&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether the rule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Code to be executed when the rule runs.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.Rule.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Rule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether the rule is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Rule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Rule.order">
<code class="sig-name descname">order</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Rule.order" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Rule.script">
<code class="sig-name descname">script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Rule.script" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Code to be executed when the rule runs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether the rule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the rule. May only contain alphanumeric characters, spaces, and hyphens. May neither start nor end with hyphens or spaces.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Order in which the rule executes relative to other rules. Lower-valued rules execute first.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Code to be executed when the rule runs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.RuleConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">RuleConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>With Auth0, you can create custom Javascript snippets that run in a secure, isolated sandbox as part of your authentication pipeline, which are otherwise known as rules. This resource allows you to create and manage variables that are available to all rules via Auth0’s global configuration object. Used in conjunction with configured rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">my_rule</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Rule</span><span class="p">(</span><span class="s2">&quot;myRule&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;function (user, context, callback) {</span>
<span class="s2">  callback(null, user, context);</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">my_rule_config</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">RuleConfig</span><span class="p">(</span><span class="s2">&quot;myRuleConfig&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Key for a rules configuration variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Value for a rules configuration variable.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.RuleConfig.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.RuleConfig.key" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Key for a rules configuration variable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.RuleConfig.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.RuleConfig.value" title="Permalink to this definition">¶</a></dt>
<dd><p>String, Case-sensitive. Value for a rules configuration variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Key for a rules configuration variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Value for a rules configuration variable.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.RuleConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.RuleConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.RuleConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Tenant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">Tenant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">change_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_redirection_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_locales</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guardian_mfa_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sandbox_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can manage Auth0 tenants, including setting logos and support contact information, setting error pages, and configuring default tenant behaviors.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">tenant</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Tenant</span><span class="p">(</span><span class="s2">&quot;tenant&quot;</span><span class="p">,</span>
    <span class="n">allowed_logout_urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://mysite/logout&quot;</span><span class="p">],</span>
    <span class="n">change_password</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./password_reset.html&quot;</span><span class="p">),</span>
    <span class="p">},</span>
    <span class="n">default_audience</span><span class="o">=</span><span class="s2">&quot;&lt;client_id&gt;&quot;</span><span class="p">,</span>
    <span class="n">default_directory</span><span class="o">=</span><span class="s2">&quot;Connection-Name&quot;</span><span class="p">,</span>
    <span class="n">error_page</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./error.html&quot;</span><span class="p">),</span>
        <span class="s2">&quot;showLogLink&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;http://mysite/errors&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">friendly_name</span><span class="o">=</span><span class="s2">&quot;Tenant Name&quot;</span><span class="p">,</span>
    <span class="n">guardian_mfa_page</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;./guardian_multifactor.html&quot;</span><span class="p">),</span>
    <span class="p">},</span>
    <span class="n">picture_url</span><span class="o">=</span><span class="s2">&quot;http://mysite/logo.png&quot;</span><span class="p">,</span>
    <span class="n">sandbox_version</span><span class="o">=</span><span class="s2">&quot;8&quot;</span><span class="p">,</span>
    <span class="n">session_lifetime</span><span class="o">=</span><span class="mi">46000</span><span class="p">,</span>
    <span class="n">support_email</span><span class="o">=</span><span class="s2">&quot;support@mysite&quot;</span><span class="p">,</span>
    <span class="n">support_url</span><span class="o">=</span><span class="s2">&quot;http://mysite/support&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>change_password</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p></li>
<li><p><strong>default_audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p></li>
<li><p><strong>default_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p></li>
<li><p><strong>default_redirection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. The default absolute redirection uri, must be https and cannot contain a fragment.</p></li>
<li><p><strong>error_page</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for error pages. For details, see Error Page.</p></li>
<li><p><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for tenant flags. For details, see Flags.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the tenant.</p></li>
<li><p><strong>guardian_mfa_page</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p></li>
<li><p><strong>idle_session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session can be inactive before the user must log in again.</p></li>
<li><p><strong>picture_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p></li>
<li><p><strong>sandbox_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session will stay valid.</p></li>
<li><p><strong>support_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support email address for authenticating users.</p></li>
<li><p><strong>support_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support URL for authenticating users.</p></li>
<li><p><strong>universal_login</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>change_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the custom change password page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the change password page.</p></li>
</ul>
<p>The <strong>error_page</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLogLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to show the link to logs as part of the default error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. URL to redirect to when an error occurs rather than showing the default error page.</p></li>
</ul>
<p>The <strong>flags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changePwdFlowV1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the older v1 change password flow. Not recommended except for backward compatibility.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableClickjackProtectionHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicated whether or not classic Universal Login prompts include additional security headers to prevent clickjacking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableApisSection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the APIs section is enabled for the tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableClientConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not all current connections should be enabled when a new client is created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableCustomDomainInEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant allows custom domains in emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDynamicClientRegistration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant allows dynamic client registration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableLegacyLogsSearchV2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the older v2 legacy logs search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePipeline2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not advanced API Authorization scenarios are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePublicSignupUserExistsError</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the public sign up process shows a user_exists error if the user already exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal_login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant uses universal login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useScopeDescriptionsForConsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>guardian_mfa_page</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the custom Guardian page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the Guardian page.</p></li>
</ul>
<p>The <strong>universal_login</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">colors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for Universal Login colors. See Universal Login - Colors.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pageBackground</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Hexadecimal. Background color of login pages.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Hexadecimal. Primary button background color.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.allowed_logout_urls">
<code class="sig-name descname">allowed_logout_urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.allowed_logout_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List(String). URLs that Auth0 may redirect to after logout.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.change_password">
<code class="sig-name descname">change_password</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.change_password" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to use the custom change password page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the change password page.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.default_audience">
<code class="sig-name descname">default_audience</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.default_audience" title="Permalink to this definition">¶</a></dt>
<dd><p>String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.default_directory">
<code class="sig-name descname">default_directory</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.default_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.default_redirection_uri">
<code class="sig-name descname">default_redirection_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.default_redirection_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>String. The default absolute redirection uri, must be https and cannot contain a fragment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.error_page">
<code class="sig-name descname">error_page</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.error_page" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for error pages. For details, see Error Page.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLogLink</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to show the link to logs as part of the default error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String. URL to redirect to when an error occurs rather than showing the default error page.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.flags">
<code class="sig-name descname">flags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.flags" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for tenant flags. For details, see Flags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changePwdFlowV1</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to use the older v1 change password flow. Not recommended except for backward compatibility.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableClickjackProtectionHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicated whether or not classic Universal Login prompts include additional security headers to prevent clickjacking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableApisSection</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the APIs section is enabled for the tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableClientConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not all current connections should be enabled when a new client is created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableCustomDomainInEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the tenant allows custom domains in emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDynamicClientRegistration</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the tenant allows dynamic client registration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableLegacyLogsSearchV2</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to use the older v2 legacy logs search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePipeline2</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not advanced API Authorization scenarios are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePublicSignupUserExistsError</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the public sign up process shows a user_exists error if the user already exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal_login</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not the tenant uses universal login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useScopeDescriptionsForConsent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Friendly name for the tenant.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.guardian_mfa_page">
<code class="sig-name descname">guardian_mfa_page</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.guardian_mfa_page" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean. Indicates whether or not to use the custom Guardian page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the Guardian page.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.idle_session_lifetime">
<code class="sig-name descname">idle_session_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.idle_session_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Number of hours during which a session can be inactive before the user must log in again.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.picture_url">
<code class="sig-name descname">picture_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.picture_url" title="Permalink to this definition">¶</a></dt>
<dd><p>. String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.sandbox_version">
<code class="sig-name descname">sandbox_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.sandbox_version" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.session_lifetime">
<code class="sig-name descname">session_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.session_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer. Number of hours during which a session will stay valid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.support_email">
<code class="sig-name descname">support_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.support_email" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Support email address for authenticating users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.support_url">
<code class="sig-name descname">support_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.support_url" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Support URL for authenticating users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.Tenant.universal_login">
<code class="sig-name descname">universal_login</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.Tenant.universal_login" title="Permalink to this definition">¶</a></dt>
<dd><p>List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">colors</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - List(Resource). Configuration settings for Universal Login colors. See Universal Login - Colors.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pageBackground</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Hexadecimal. Background color of login pages.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String, Hexadecimal. Primary button background color.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_logout_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">change_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_redirection_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_locales</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guardian_mfa_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sandbox_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">universal_login</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Tenant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List(String). URLs that Auth0 may redirect to after logout.</p></li>
<li><p><strong>change_password</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for change passsword page. For details, see Change Password Page.</p></li>
<li><p><strong>default_audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.</p></li>
<li><p><strong>default_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection to be used for Password Grant exchanges. Options include <code class="docutils literal notranslate"><span class="pre">auth0-adldap</span></code>, <code class="docutils literal notranslate"><span class="pre">ad</span></code>, <code class="docutils literal notranslate"><span class="pre">auth0</span></code>, <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">waad</span></code>, and <code class="docutils literal notranslate"><span class="pre">adfs</span></code>.</p></li>
<li><p><strong>default_redirection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. The default absolute redirection uri, must be https and cannot contain a fragment.</p></li>
<li><p><strong>error_page</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for error pages. For details, see Error Page.</p></li>
<li><p><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for tenant flags. For details, see Flags.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Friendly name for the tenant.</p></li>
<li><p><strong>guardian_mfa_page</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for the Guardian MFA page. For details, see Guardian MFA Page.</p></li>
<li><p><strong>idle_session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session can be inactive before the user must log in again.</p></li>
<li><p><strong>picture_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . String URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.</p></li>
<li><p><strong>sandbox_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0’s functionality.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer. Number of hours during which a session will stay valid.</p></li>
<li><p><strong>support_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support email address for authenticating users.</p></li>
<li><p><strong>support_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Support URL for authenticating users.</p></li>
<li><p><strong>universal_login</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – List(Resource). Configuration settings for Universal Login. For details, see Universal Login.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>change_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the custom change password page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the change password page.</p></li>
</ul>
<p>The <strong>error_page</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLogLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to show the link to logs as part of the default error page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String. URL to redirect to when an error occurs rather than showing the default error page.</p></li>
</ul>
<p>The <strong>flags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">changePwdFlowV1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the older v1 change password flow. Not recommended except for backward compatibility.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableClickjackProtectionHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicated whether or not classic Universal Login prompts include additional security headers to prevent clickjacking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableApisSection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the APIs section is enabled for the tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableClientConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not all current connections should be enabled when a new client is created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableCustomDomainInEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant allows custom domains in emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDynamicClientRegistration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant allows dynamic client registration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableLegacyLogsSearchV2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the older v2 legacy logs search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePipeline2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not advanced API Authorization scenarios are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePublicSignupUserExistsError</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the public sign up process shows a user_exists error if the user already exists.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal_login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not the tenant uses universal login.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useScopeDescriptionsForConsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>guardian_mfa_page</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean. Indicates whether or not to use the custom Guardian page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, HTML format with supported Liquid syntax. Customized content of the Guardian page.</p></li>
</ul>
<p>The <strong>universal_login</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">colors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - List(Resource). Configuration settings for Universal Login colors. See Universal Login - Colors.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pageBackground</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Hexadecimal. Background color of login pages.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String, Hexadecimal. Primary button background color.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.Tenant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.Tenant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.Tenant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_auth0.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User" title="Permalink to this definition">¶</a></dt>
<dd><p>With this resource, you can manage user identities, including resetting passwords, and creating, provisioning, blocking, and deleting users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_auth0</span> <span class="k">as</span> <span class="nn">auth0</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Administrator&quot;</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">auth0</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">connection_name</span><span class="o">=</span><span class="s2">&quot;Username-Password-Authentication&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;unique_username&quot;</span><span class="p">,</span>
    <span class="n">given_name</span><span class="o">=</span><span class="s2">&quot;Firstname&quot;</span><span class="p">,</span>
    <span class="n">family_name</span><span class="o">=</span><span class="s2">&quot;Lastname&quot;</span><span class="p">,</span>
    <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;some.nickname&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test@test.com&quot;</span><span class="p">,</span>
    <span class="n">email_verified</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;passpass$12$12&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">admin</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p></li>
<li><p><strong>connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection from which the user information was sourced.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address of the user.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email address has been verified.</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Preferred nickname or alias of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p></li>
<li><p><strong>phone_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p></li>
<li><p><strong>phone_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the phone number has been verified.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(String). Set of IDs of roles assigned to the user.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the user.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Username of the user. Only valid if the connection requires a username.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_auth0.User.app_metadata">
<code class="sig-name descname">app_metadata</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.app_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.connection_name">
<code class="sig-name descname">connection_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Name of the connection from which the user information was sourced.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Email address of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.email_verified">
<code class="sig-name descname">email_verified</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.email_verified" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the email address has been verified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.nickname">
<code class="sig-name descname">nickname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Preferred nickname or alias of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.phone_number">
<code class="sig-name descname">phone_number</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.phone_number" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.phone_verified">
<code class="sig-name descname">phone_verified</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.phone_verified" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the phone number has been verified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.roles">
<code class="sig-name descname">roles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Set(String). Set of IDs of roles assigned to the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.user_id">
<code class="sig-name descname">user_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>String. ID of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.user_metadata">
<code class="sig-name descname">user_metadata</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>String. Username of the user. Only valid if the connection requires a username.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_auth0.User.verify_email">
<code class="sig-name descname">verify_email</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_auth0.User.verify_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">given_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">picture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that impact the user’s core functionality, such as how an application functions or what the user can access. Examples include support plans and IDs for external accounts.</p></li>
<li><p><strong>connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Name of the connection from which the user information was sourced.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Email address of the user.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the email address has been verified.</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Preferred nickname or alias of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, Case-sensitive. Initial password for this user. Used for non-SMS connections.</p></li>
<li><p><strong>phone_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Phone number for the user; follows the E.164 recommendation. Used for SMS connections.</p></li>
<li><p><strong>phone_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the phone number has been verified.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set(String). Set of IDs of roles assigned to the user.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. ID of the user.</p></li>
<li><p><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String, JSON format. Custom fields that store info about the user that does not impact a user’s core functionality. Examples include work address, home address, and user preferences.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String. Username of the user. Only valid if the connection requires a username.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean. Indicates whether or not the user will receive a verification email after creation. Overrides behavior of <code class="docutils literal notranslate"><span class="pre">email_verified</span></code> parameter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_auth0.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_auth0.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_auth0.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
