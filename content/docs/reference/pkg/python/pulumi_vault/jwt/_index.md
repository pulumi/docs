---
title: Module jwt
title_tag: Module jwt | Package pulumi_vault | Python SDK
linktitle: jwt
notitle: true
---

<div class="section" id="jwt">
<h1>jwt<a class="headerlink" href="#jwt" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.jwt"></span><dl class="py class">
<dt id="pulumi_vault.jwt.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.jwt.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_ca_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_supported_algs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_validation_pubkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_discovery_ca_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_discovery_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for managing an
<a class="reference external" href="https://www.vaultproject.io/docs/auth/jwt.html">JWT auth backend within Vault</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bound_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value against which to match the iss claim in a JWT</p></li>
<li><p><strong>default_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default role to use if none is provided during login</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the auth backend</p></li>
<li><p><strong>jwks_ca_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used.</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JWKS URL to use to authenticate signatures. Cannot be used with “oidc_discovery_url” or “jwt_validation_pubkeys”.</p></li>
<li><p><strong>jwt_supported_algs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of supported signing algorithms. Vault 1.1.0 defaults to [RS256] but future or past versions of Vault may differ</p></li>
<li><p><strong>jwt_validation_pubkeys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">oidc_discovery_url</span></code></p></li>
<li><p><strong>oidc_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID used for OIDC backends</p></li>
<li><p><strong>oidc_client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret used for OIDC backends</p></li>
<li><p><strong>oidc_discovery_ca_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used</p></li>
<li><p><strong>oidc_discovery_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OIDC Discovery URL, without any .well-known component (base path). Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">jwt_validation_pubkeys</span></code></p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the JWT/OIDC auth backend</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of auth backend. Should be one of <code class="docutils literal notranslate"><span class="pre">jwt</span></code> or <code class="docutils literal notranslate"><span class="pre">oidc</span></code>. Default - <code class="docutils literal notranslate"><span class="pre">jwt</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>tune</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedResponseHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of headers to whitelist and allowing
a plugin to include them in the response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auditNonHmacRequestKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of keys that will
not be HMAC’d by audit devices in the request data object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auditNonHmacResponseKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of keys that will
not be HMAC’d by audit devices in the response data object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultLeaseTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default time-to-live.
If set, this overrides the global default.
Must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">listing_visibility</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are “unauth” or “hidden”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLeaseTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the maximum time-to-live.
If set, this overrides the global default.
Must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughRequestHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of headers to whitelist and
pass from the request to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of tokens that should be returned by
the mount. Valid values are “default-service”, “default-batch”, “service”, “batch”.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.accessor">
<code class="sig-name descname">accessor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor of the JWT auth backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.bound_issuer">
<code class="sig-name descname">bound_issuer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.bound_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The value against which to match the iss claim in a JWT</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.default_role">
<code class="sig-name descname">default_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.default_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The default role to use if none is provided during login</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the auth backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.jwks_ca_pem">
<code class="sig-name descname">jwks_ca_pem</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.jwks_ca_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.jwks_url">
<code class="sig-name descname">jwks_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.jwks_url" title="Permalink to this definition">¶</a></dt>
<dd><p>JWKS URL to use to authenticate signatures. Cannot be used with “oidc_discovery_url” or “jwt_validation_pubkeys”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.jwt_supported_algs">
<code class="sig-name descname">jwt_supported_algs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.jwt_supported_algs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of supported signing algorithms. Vault 1.1.0 defaults to [RS256] but future or past versions of Vault may differ</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.jwt_validation_pubkeys">
<code class="sig-name descname">jwt_validation_pubkeys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.jwt_validation_pubkeys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">oidc_discovery_url</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.oidc_client_id">
<code class="sig-name descname">oidc_client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.oidc_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID used for OIDC backends</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.oidc_client_secret">
<code class="sig-name descname">oidc_client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.oidc_client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Secret used for OIDC backends</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.oidc_discovery_ca_pem">
<code class="sig-name descname">oidc_discovery_ca_pem</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.oidc_discovery_ca_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.oidc_discovery_url">
<code class="sig-name descname">oidc_discovery_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.oidc_discovery_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The OIDC Discovery URL, without any .well-known component (base path). Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">jwt_validation_pubkeys</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to mount the JWT/OIDC auth backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackend.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of auth backend. Should be one of <code class="docutils literal notranslate"><span class="pre">jwt</span></code> or <code class="docutils literal notranslate"><span class="pre">oidc</span></code>. Default - <code class="docutils literal notranslate"><span class="pre">jwt</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.jwt.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_ca_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_supported_algs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_validation_pubkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_discovery_ca_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_discovery_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The accessor of the JWT auth backend</p></li>
<li><p><strong>bound_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value against which to match the iss claim in a JWT</p></li>
<li><p><strong>default_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default role to use if none is provided during login</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the auth backend</p></li>
<li><p><strong>jwks_ca_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used.</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JWKS URL to use to authenticate signatures. Cannot be used with “oidc_discovery_url” or “jwt_validation_pubkeys”.</p></li>
<li><p><strong>jwt_supported_algs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of supported signing algorithms. Vault 1.1.0 defaults to [RS256] but future or past versions of Vault may differ</p></li>
<li><p><strong>jwt_validation_pubkeys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">oidc_discovery_url</span></code></p></li>
<li><p><strong>oidc_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID used for OIDC backends</p></li>
<li><p><strong>oidc_client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Secret used for OIDC backends</p></li>
<li><p><strong>oidc_discovery_ca_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used</p></li>
<li><p><strong>oidc_discovery_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OIDC Discovery URL, without any .well-known component (base path). Cannot be used in combination with <code class="docutils literal notranslate"><span class="pre">jwt_validation_pubkeys</span></code></p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the JWT/OIDC auth backend</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of auth backend. Should be one of <code class="docutils literal notranslate"><span class="pre">jwt</span></code> or <code class="docutils literal notranslate"><span class="pre">oidc</span></code>. Default - <code class="docutils literal notranslate"><span class="pre">jwt</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>tune</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedResponseHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of headers to whitelist and allowing
a plugin to include them in the response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auditNonHmacRequestKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of keys that will
not be HMAC’d by audit devices in the request data object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auditNonHmacResponseKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of keys that will
not be HMAC’d by audit devices in the response data object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultLeaseTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default time-to-live.
If set, this overrides the global default.
Must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">listing_visibility</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are “unauth” or “hidden”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLeaseTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the maximum time-to-live.
If set, this overrides the global default.
Must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passthroughRequestHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of headers to whitelist and
pass from the request to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of tokens that should be returned by
the mount. Valid values are “default-service”, “default-batch”, “service”, “batch”.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.jwt.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.jwt.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.jwt.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.jwt.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clock_skew_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_claim</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_claim_delimiter_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_before_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_claim</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verbose_oidc_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an JWT/OIDC auth backend role in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/jwt.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of allowed values for redirect_uri during OIDC logins.
Required for OIDC roles</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">jwt</span></code>.</p></li>
<li><p><strong>bound_audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of <code class="docutils literal notranslate"><span class="pre">aud</span></code> claims to match
against. Any match is sufficient.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>bound_claims</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If set, a map of claims/values to match against.
The expected value may be a single string or a list of strings.</p></li>
<li><p><strong>bound_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, requires that the <code class="docutils literal notranslate"><span class="pre">sub</span></code> claim matches
this value.</p></li>
<li><p><strong>claim_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If set, a map of claims (keys) to be copied
to specified metadata fields (values).</p></li>
<li><p><strong>clock_skew_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to all claims to account for clock skew, in
seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>expiration_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to expiration (<code class="docutils literal notranslate"><span class="pre">exp</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>groups_claim</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The claim to use to uniquely identify
the set of groups to which the user belongs; this will be used as the names
for the Identity group aliases created due to a successful login. The claim
value must be a list of strings.</p></li>
<li><p><strong>groups_claim_delimiter_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Deprecated. This field has been
removed since Vault 1.1. If the groups claim is not at the top level, it can
now be specified as a <a class="reference external" href="https://tools.ietf.org/html/rfc6901">JSONPointer</a>.)
A pattern of delimiters
used to allow the groups_claim to live outside of the top-level JWT structure.
For instance, a groups_claim of meta/user.name/groups with this field
set to // will expect nested structures named meta, user.name, and groups.
If this field was set to /./ the groups information would expect to be
via nested structures of meta, user, name, and groups.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>not_before_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to not before (<code class="docutils literal notranslate"><span class="pre">nbf</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, puts a use-count
limitation on the issued token.</p></li>
<li><p><strong>oidc_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of OIDC scopes to be used with an OIDC role.
The standard scope “openid” is automatically included and need not be specified.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>role_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of role, either “oidc” (default) or “jwt”.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
<li><p><strong>user_claim</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The claim to use to uniquely identify
the user; this will be used as the name for the Identity entity alias created
due to a successful login.</p></li>
<li><p><strong>verbose_oidc_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Log received OIDC tokens and claims when debug-level
logging is active. Not recommended in production since sensitive information may be present
in OIDC responses.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.allowed_redirect_uris">
<code class="sig-name descname">allowed_redirect_uris</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.allowed_redirect_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of allowed values for redirect_uri during OIDC logins.
Required for OIDC roles</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">jwt</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.bound_audiences">
<code class="sig-name descname">bound_audiences</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.bound_audiences" title="Permalink to this definition">¶</a></dt>
<dd><p>List of <code class="docutils literal notranslate"><span class="pre">aud</span></code> claims to match
against. Any match is sufficient.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.bound_cidrs">
<code class="sig-name descname">bound_cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.bound_claims">
<code class="sig-name descname">bound_claims</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.bound_claims" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a map of claims/values to match against.
The expected value may be a single string or a list of strings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.bound_subject">
<code class="sig-name descname">bound_subject</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.bound_subject" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, requires that the <code class="docutils literal notranslate"><span class="pre">sub</span></code> claim matches
this value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.claim_mappings">
<code class="sig-name descname">claim_mappings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.claim_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a map of claims (keys) to be copied
to specified metadata fields (values).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.clock_skew_leeway">
<code class="sig-name descname">clock_skew_leeway</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.clock_skew_leeway" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of leeway to add to all claims to account for clock skew, in
seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.expiration_leeway">
<code class="sig-name descname">expiration_leeway</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.expiration_leeway" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of leeway to add to expiration (<code class="docutils literal notranslate"><span class="pre">exp</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.groups_claim">
<code class="sig-name descname">groups_claim</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.groups_claim" title="Permalink to this definition">¶</a></dt>
<dd><p>The claim to use to uniquely identify
the set of groups to which the user belongs; this will be used as the names
for the Identity group aliases created due to a successful login. The claim
value must be a list of strings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.groups_claim_delimiter_pattern">
<code class="sig-name descname">groups_claim_delimiter_pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.groups_claim_delimiter_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Deprecated. This field has been
removed since Vault 1.1. If the groups claim is not at the top level, it can
now be specified as a <a class="reference external" href="https://tools.ietf.org/html/rfc6901">JSONPointer</a>.)
A pattern of delimiters
used to allow the groups_claim to live outside of the top-level JWT structure.
For instance, a groups_claim of meta/user.name/groups with this field
set to // will expect nested structures named meta, user.name, and groups.
If this field was set to /./ the groups information would expect to be
via nested structures of meta, user, name, and groups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.not_before_leeway">
<code class="sig-name descname">not_before_leeway</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.not_before_leeway" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of leeway to add to not before (<code class="docutils literal notranslate"><span class="pre">nbf</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.num_uses">
<code class="sig-name descname">num_uses</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, puts a use-count
limitation on the issued token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.oidc_scopes">
<code class="sig-name descname">oidc_scopes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.oidc_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a list of OIDC scopes to be used with an OIDC role.
The standard scope “openid” is automatically included and need not be specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.role_type">
<code class="sig-name descname">role_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.role_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of role, either “oidc” (default) or “jwt”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.user_claim">
<code class="sig-name descname">user_claim</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.user_claim" title="Permalink to this definition">¶</a></dt>
<dd><p>The claim to use to uniquely identify
the user; this will be used as the name for the Identity entity alias created
due to a successful login.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.jwt.AuthBackendRole.verbose_oidc_logging">
<code class="sig-name descname">verbose_oidc_logging</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.verbose_oidc_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Log received OIDC tokens and claims when debug-level
logging is active. Not recommended in production since sensitive information may be present
in OIDC responses.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.jwt.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_claims</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clock_skew_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_claim</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_claim_delimiter_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_before_leeway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oidc_scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_claim</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verbose_oidc_logging</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of allowed values for redirect_uri during OIDC logins.
Required for OIDC roles</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">jwt</span></code>.</p></li>
<li><p><strong>bound_audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of <code class="docutils literal notranslate"><span class="pre">aud</span></code> claims to match
against. Any match is sufficient.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>bound_claims</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If set, a map of claims/values to match against.
The expected value may be a single string or a list of strings.</p></li>
<li><p><strong>bound_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, requires that the <code class="docutils literal notranslate"><span class="pre">sub</span></code> claim matches
this value.</p></li>
<li><p><strong>claim_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If set, a map of claims (keys) to be copied
to specified metadata fields (values).</p></li>
<li><p><strong>clock_skew_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to all claims to account for clock skew, in
seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>expiration_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to expiration (<code class="docutils literal notranslate"><span class="pre">exp</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>groups_claim</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The claim to use to uniquely identify
the set of groups to which the user belongs; this will be used as the names
for the Identity group aliases created due to a successful login. The claim
value must be a list of strings.</p></li>
<li><p><strong>groups_claim_delimiter_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Optional; Deprecated. This field has been
removed since Vault 1.1. If the groups claim is not at the top level, it can
now be specified as a <a class="reference external" href="https://tools.ietf.org/html/rfc6901">JSONPointer</a>.)
A pattern of delimiters
used to allow the groups_claim to live outside of the top-level JWT structure.
For instance, a groups_claim of meta/user.name/groups with this field
set to // will expect nested structures named meta, user.name, and groups.
If this field was set to /./ the groups information would expect to be
via nested structures of meta, user, name, and groups.</p>
</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>not_before_leeway</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of leeway to add to not before (<code class="docutils literal notranslate"><span class="pre">nbf</span></code>) claims to account for
clock skew, in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds if set to <code class="docutils literal notranslate"><span class="pre">0</span></code> and can be disabled if set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>.
Only applicable with “jwt” roles.</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, puts a use-count
limitation on the issued token.</p></li>
<li><p><strong>oidc_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of OIDC scopes to be used with an OIDC role.
The standard scope “openid” is automatically included and need not be specified.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>role_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of role, either “oidc” (default) or “jwt”.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
<li><p><strong>user_claim</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The claim to use to uniquely identify
the user; this will be used as the name for the Identity entity alias created
due to a successful login.</p></li>
<li><p><strong>verbose_oidc_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Log received OIDC tokens and claims when debug-level
logging is active. Not recommended in production since sensitive information may be present
in OIDC responses.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.jwt.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.jwt.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.jwt.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
