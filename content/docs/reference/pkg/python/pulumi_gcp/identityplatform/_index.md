---
title: Module identityplatform
title_tag: Module identityplatform | Package pulumi_gcp | Python SDK
linktitle: identityplatform
notitle: true
---

<div class="section" id="identityplatform">
<h1>identityplatform<a class="headerlink" href="#identityplatform" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.identityplatform"></span><dl class="class">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">DefaultSupportedIdpConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Configurations options for authenticating with a the standard set of Identity Toolkit-trusted IDPs.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client ID</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this IDP allows the user to sign in</p></li>
<li><p><strong>idp_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the IDP. Possible values include:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apple.com`
* `facebook.com`
* `gc.apple.com`
* `github.com`
* `google.com`
* `linkedin.com`
* `microsoft.com`
* `playgames.google.com`
* `twitter.com`
* `yahoo.com`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client secret</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this IDP allows the user to sign in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.idp_id">
<code class="sig-name descname">idp_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.idp_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the IDP. Possible values include:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apple.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gc.apple.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">github.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">google.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linkedin.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">playgames.google.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">yahoo.com</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the DefaultSupportedIdpConfig resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultSupportedIdpConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client ID</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this IDP allows the user to sign in</p></li>
<li><p><strong>idp_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the IDP. Possible values include:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apple.com`
* `facebook.com`
* `gc.apple.com`
* `github.com`
* `google.com`
* `linkedin.com`
* `microsoft.com`
* `playgames.google.com`
* `twitter.com`
* `yahoo.com`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the DefaultSupportedIdpConfig resource</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.DefaultSupportedIdpConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">InboundSamlConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sp_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Inbound SAML configuration for a Identity Toolkit project.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>idp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>idp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IdP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL to send Authentication request to.</p></li>
</ul>
<p>The <strong>sp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this config allows users to sign in with the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.idp_config">
<code class="sig-name descname">idp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.idp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The IdP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - URL to send Authentication request to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.sp_config">
<code class="sig-name descname">sp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.sp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sp_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InboundSamlConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>idp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>idp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IdP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL to send Authentication request to.</p></li>
</ul>
<p>The <strong>sp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.InboundSamlConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.InboundSamlConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">OauthIdpConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC IdP configuration for a Identity Toolkit project.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id of an OAuth client.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the OAuth client, to enable OIDC code flow.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC Idps, the issuer identifier.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The client id of an OAuth client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret of the OAuth client, to enable OIDC code flow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this config allows users to sign in with the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>For OIDC Idps, the issuer identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OauthIdpConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id of an OAuth client.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the OAuth client, to enable OIDC code flow.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC Idps, the issuer identifier.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.OauthIdpConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.OauthIdpConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.Tenant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">Tenant</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_password_signup=None</em>, <em class="sig-param">disable_auth=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enable_email_link_signin=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant configuration in a multi-tenant project.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<p>You must <a class="reference external" href="https://cloud.google.com/identity-platform/docs/multi-tenancy-quickstart">enable multi-tenancy</a> via
the Cloud Console prior to creating tenants.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_password_signup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow email/password user authentication.</p></li>
<li><p><strong>disable_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether authentication is disabled for the tenant. If true, the users under
the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
are not able to manage its users.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name of the tenant.</p></li>
<li><p><strong>enable_email_link_signin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable email link user authentication.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.allow_password_signup">
<code class="sig-name descname">allow_password_signup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.allow_password_signup" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow email/password user authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.disable_auth">
<code class="sig-name descname">disable_auth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.disable_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether authentication is disabled for the tenant. If true, the users under
the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
are not able to manage its users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly display name of the tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.enable_email_link_signin">
<code class="sig-name descname">enable_email_link_signin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.enable_email_link_signin" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable email link user authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tenant that is generated by the server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.Tenant.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.Tenant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_password_signup=None</em>, <em class="sig-param">disable_auth=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enable_email_link_signin=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Tenant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_password_signup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow email/password user authentication.</p></li>
<li><p><strong>disable_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether authentication is disabled for the tenant. If true, the users under
the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
are not able to manage its users.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name of the tenant.</p></li>
<li><p><strong>enable_email_link_signin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable email link user authentication.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant that is generated by the server</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.Tenant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.Tenant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.Tenant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">TenantDefaultSupportedIdpConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tenant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Configurations options for the tenant for authenticating with a the standard set of Identity Toolkit-trusted IDPs.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client ID</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this IDP allows the user to sign in</p></li>
<li><p><strong>idp_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the IDP. Possible values include:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apple.com`
* `facebook.com`
* `gc.apple.com`
* `github.com`
* `google.com`
* `linkedin.com`
* `microsoft.com`
* `playgames.google.com`
* `twitter.com`
* `yahoo.com`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this DefaultSupportedIdpConfig resource exists</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client secret</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this IDP allows the user to sign in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.idp_id">
<code class="sig-name descname">idp_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.idp_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the IDP. Possible values include:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apple.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facebook.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gc.apple.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">github.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">google.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linkedin.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">microsoft.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">playgames.google.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">twitter.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">yahoo.com</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the default supported IDP config resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.tenant">
<code class="sig-name descname">tenant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tenant where this DefaultSupportedIdpConfig resource exists</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tenant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TenantDefaultSupportedIdpConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client ID</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this IDP allows the user to sign in</p></li>
<li><p><strong>idp_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the IDP. Possible values include:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apple.com`
* `facebook.com`
* `gc.apple.com`
* `github.com`
* `google.com`
* `linkedin.com`
* `microsoft.com`
* `playgames.google.com`
* `twitter.com`
* `yahoo.com`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the default supported IDP config resource</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this DefaultSupportedIdpConfig resource exists</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantDefaultSupportedIdpConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">TenantInboundSamlConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sp_config=None</em>, <em class="sig-param">tenant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Inbound SAML configuration for a Identity Toolkit tenant.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>idp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this inbound SAML config resource exists</p></li>
</ul>
</dd>
</dl>
<p>The <strong>idp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL to send Authentication request to.</p></li>
</ul>
<p>The <strong>sp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this config allows users to sign in with the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.idp_config">
<code class="sig-name descname">idp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.idp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - URL to send Authentication request to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.sp_config">
<code class="sig-name descname">sp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.sp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.tenant">
<code class="sig-name descname">tenant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tenant where this inbound SAML config resource exists</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sp_config=None</em>, <em class="sig-param">tenant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TenantInboundSamlConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>idp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML IdP configuration when the project acts as the relying party  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the InboundSamlConfig resource. Must start with ‘saml.’ and can only have alphanumeric characters,
hyphens, underscores or periods. The part after ‘saml.’ must also start with a lowercase letter, end with an
alphanumeric character, and have at least 2 characters.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SAML SP (Service Provider) configuration when the project acts as the relying party to receive
and accept an authentication assertion issued by a SAML identity provider.  Structure is documented below.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this inbound SAML config resource exists</p></li>
</ul>
</dd>
</dl>
<p>The <strong>idp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">idpCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if outbounding SAMLRequest should be signed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL to send Authentication request to.</p></li>
</ul>
<p>The <strong>sp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Callback URI where responses from IDP are handled. Must start with <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
The IDP’s certificate data to verify the signature in the SAMLResponse issued by the IDP.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">x509Certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The x509 certificate</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spEntityId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier for all SAML entities.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantInboundSamlConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantInboundSamlConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.identityplatform.</code><code class="sig-name descname">TenantOauthIdpConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tenant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC IdP configuration for a Identity Toolkit project within a tenant.</p>
<p>You must enable the
<a class="reference external" href="https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity">Google Identity Platform</a> in
the marketplace prior to using this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id of an OAuth client.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the OAuth client, to enable OIDC code flow.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC Idps, the issuer identifier.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this OIDC IDP configuration resource exists</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The client id of an OAuth client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret of the OAuth client, to enable OIDC code flow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this config allows users to sign in with the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>For OIDC Idps, the issuer identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.tenant">
<code class="sig-name descname">tenant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tenant where this OIDC IDP configuration resource exists</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tenant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TenantOauthIdpConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id of an OAuth client.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the OAuth client, to enable OIDC code flow.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly display name.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this config allows users to sign in with the provider.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC Idps, the issuer identifier.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OauthIdpConfig. Must start with <code class="docutils literal notranslate"><span class="pre">oidc.</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tenant where this OIDC IDP configuration resource exists</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.identityplatform.TenantOauthIdpConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.identityplatform.TenantOauthIdpConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
